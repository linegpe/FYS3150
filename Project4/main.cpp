#include <mpi.h>
#include <iostream>
#include <fstream>
#include <cmath>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

using namespace std;

void printSpinMatrix(int L, double** spins);
void createRandomSpins(int L, double **spins);
double calculateEnergy(int size, double J, double** spinMatrix);
double calculateMagnetization(int L, double **spinMatrix);
void metropolisAlgorithm(double T, double& E, double& M, double& E2, double& M2, double& cv, double& chi, int L, int N, double J, double** spinMatrix);
void printResults(double L, double T, double N, double energy, double E2, double M2, double magnetization, double cv, double chi);
double** createRandomMatrix(int L);
double** createOrderedMatrix(int L);
//void writeResultToFile(string myfile, double T, double E, double M, double E2, double M2, double cv, double chi);


int main(int nargs, char* args[]){
	//double temp = 1.0;
	int L = 20;
	double J = 1.0;
	int N = 1e6; // Number of Monte Carlo Cycles

	double** spins = createRandomMatrix(L);
	//double** spins = createOrderedMatrix(L);

	int numprocs, my_rank;
    MPI_Init (&nargs, &args);
    MPI_Comm_size (MPI_COMM_WORLD, &numprocs);
    MPI_Comm_rank (MPI_COMM_WORLD, &my_rank);

    //MPI_Reduce(&local_sum, &total_sum, 1, MPI_Double, MPI_SUM, 0, MPI_COMM_WORLD);

    for (double temp = 2.0; temp <= 2.3; temp += 0.05){
		srand (time(NULL));
		double E, M, E2, M2, cv, chi;
		double total_E = 0; 
		double total_M = 0;
		double total_E2 = 0;
		double total_M2 = 0;
		double total_cv = 0;
		double total_chi = 0;
		metropolisAlgorithm(temp, E, M, E2, M2, cv, chi, L, N, J, spins);
		MPI_Reduce(&E, &total_E, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);
		if (my_rank == 0){
			printResults(L,temp,N*numprocs,total_E,M,E2,M2,cv,chi);
		}
	}
	MPI_Finalize();
	return 0;
}






double calculateEnergy(int size, double J, double **spinMatrix){
	double mean_energy = 0;
	int L = size;
	for (int i = 0; i < L; i++){
		for (int j = 0; j < L; j++){

			int up = j+1;
			int down = j-1;
			int left = i-1;
			int right = i+1;

			if (i == L-1) right = 0;
			if (i == 0)   left = L-1;
			if (j == L-1) up = 0;
			if (j == 0)   down = L-1;

			mean_energy += spinMatrix[i][j]*spinMatrix[i][up] 
							+ spinMatrix[i][j]*spinMatrix[i][down]
							+ spinMatrix[i][j]*spinMatrix[left][j] 
							+ spinMatrix[i][j]*spinMatrix[right][j];
		}
	}
	return J*mean_energy/2.;
}

double calculateMagnetization(int L, double **spinMatrix){
	double magnetization = 0;
	for (int i = 0; i < L; i++){
		for (int j = 0; j < L; j++){
			magnetization += spinMatrix[i][j];
		}
	}
	return magnetization;
}

void createRandomSpins(int L, double **spins){
	for (int i = 0; i < L; i++){
		for (int j = 0; j < L; j++){
			int x = rand() % 2;
			
			if(x == 1) {
				spins[i][j] =  1;
			} else {
				spins[i][j] = -1;
			}
			
		}
	}
}

double** createRandomMatrix(int L){
	double **spins = new double*[L];
	for (int i = 0; i < L; i++){
		spins[i] = new double[L];
	}
	for (int i = 0; i < L; i++){
		for (int j = 0; j < L; j++){
			int x = rand() % 2;
			
			if(x == 1) {
				spins[i][j] =  1;
			} else {
				spins[i][j] = -1;
			}
		}
	}
	return spins;
}

double** createOrderedMatrix(int L){
	double **spins = new double*[L];
	for (int i = 0; i < L; i++){
		spins[i] = new double[L];
	}
	for (int i = 0; i < L; i++){
		for (int j = 0; j < L; j++){
			spins[i][j] = 1;
		}
	}
	return spins;
}

void printSpinMatrix(int L, double** spins) {
	for(int i= 0; i < L; i++) {
		for(int j = 0; j <L; j++) {
			cout << spins[i][j] << " ";
		}
		cout << endl;
	}
}

void metropolisAlgorithm(double T, double& E, double& M, double& E2, double& M2, double& cv, double& chi, int L, int N, double J, double** spinMatrix){
	// Wirte to file
	ofstream myfile; 
	myfile.open("test.dat");
	// Calculate current energy
	double energy = calculateEnergy(L,J,spinMatrix);
	double magnetizationSum = 0;
	double magnetization; //, E2, M2;
	double energySum = energy;
	double eSquaredSum = 0;
	double mSquaredSum = 0;
	int n = 0;
	double beta = 1./T;
	int accepted = 0;
	while (n < N){
		// Pick one random spin
		int i = rand() % L; 
		int j = rand() % L;
		// Flip this one and calculate new energy
		spinMatrix[i][j] *= (-1);
		double new_energy = calculateEnergy(L,J,spinMatrix);
		// Calculate dE
		double dE = new_energy - energy;
		if (dE <= 0){
			// Accept new energy
			energy = new_energy;
			magnetization = calculateMagnetization(L,spinMatrix);
			mSquaredSum += magnetization*magnetization;
			accepted += 1;
		} else { 
			double w = exp(-beta*dE);
			double max = RAND_MAX;
			double r = rand() / ((double) max);
			if (r < w){
				energy = new_energy;
				magnetization = calculateMagnetization(L,spinMatrix);
				accepted += 1;
			} else {
				spinMatrix[i][j] *= (-1);
			}
		}
		energySum += energy;
		eSquaredSum += energy*energy;
		magnetizationSum += magnetization;
		mSquaredSum += magnetization*magnetization;
		n += 1;

		//myfile << accepted << endl;
		myfile << energySum/((double)n*L*L) << " " << abs(magnetizationSum/((double) n*L*L)) << endl;
	}
	E = energySum;
	M = magnetizationSum;
	E2 = eSquaredSum;
	M2 = mSquaredSum;
	cv = (E2 - E*E)/(T*T);
	chi = (M2 - M*M)/T;

	myfile.close();
}

void printResults(double L, double T, double N, double energy, double magnetization, double E2, double M2, double cv, double chi){
	cout << endl;
	cout << "After " << N << " loops with temperature " << T <<", the results are:" << endl << endl;
	cout << "  o  Mean energy:               " << energy/(N*L*L) << endl;
	cout << "  o  Mean magnetization:        " << magnetization << endl;
	cout << "  o  Heat capacity:             " << cv << endl;
	cout << "  o  Magnetic susceptibility    " << chi << endl << endl;
	cout << "  o  Mean energy squared        " << E2 << endl;
	cout << "  o  Mean magnetization squared " << M2 << endl;
}

// void writeResultToFile(string myfile, double T, double E, double M, double E2, double M2, double cv, double chi){
// 	myfile << T << " " << E << " " << M << " " << E2 << " " << M2 << " " << cv << " " << chi << endl;
// }