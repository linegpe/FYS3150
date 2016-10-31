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
void metropolisAlgorithm(double& E, double& M, double& cv, double& chi, int L, int N, double J, double** spinMatrix);
void printResults(double N, double energy, double magnetization, double cv, double chi);
double** createRandomMatrix(int L);


int main(){
	double temp = 1.0;
	int L = 20;
	int nr_spins = L*L;
	double nr_microstates = pow(2,nr_spins);
	double J = 1.0;
	int N = 1e5; // Number of Monte Carlo Cycles

	// Spin matrix
	double **spins = new double*[L];
	for (int i = 0; i < L; i++){
		spins[i] = new double[L];
	}

	for (int i = 0; i < L; i++){
		for (int j = 0; j < L; j++){
			spins[i][j] = 1;
		}
	}
	//createRandomSpins(L,spins);

	//double** spins = createRandomMatrix(L);

	//int total_spin = 0;
	srand (time(NULL));
	double E, M, cv, chi;
	metropolisAlgorithm(E, M, cv, chi, L, N, J, spins);
	printResults(N,E,M,cv,chi);
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
			if (i == 0) left = L-1;
			if (j == L-1) up = 0;
			if (j == 0) down = L-1;

			mean_energy += spinMatrix[i][j]*spinMatrix[i][up] 
							+ spinMatrix[i][j]*spinMatrix[i][down]
							+ spinMatrix[i][j]*spinMatrix[left][j] 
							+ spinMatrix[i][j]*spinMatrix[right][j];


/*			if((i+1) < L && (j+1) < L && (i-1) >= 0 && (j-1) >= 0) {
				cout << "uh oh" << endl;
				mean_energy += spinMatrix[i][j]*spinMatrix[i+1][j];
				mean_energy += spinMatrix[i][j]*spinMatrix[i][j+1];
				mean_energy += spinMatrix[i][j]*spinMatrix[i-1][j];
				mean_energy += spinMatrix[i][j]*spinMatrix[i][j-1];
			} else {

/*				if(i-1 < 0 && j-1 > 0) {
					mean_energy += spinMatrix[i][j]*spinMatrix[L-1][j];
					mean_energy += spinMatrix[i][j]*spinMatrix[i][j-1];
					mean_energy += spinMatrix[i][j]*spinMatrix[i+1][j];
					mean_energy += spinMatrix[i][j]*spinMatrix[i][j+1];
				}
				mean_energy += spinMatrix[i][j]*spinMatrix[1][j];
				mean_energy += spinMatrix[i][j]*spinMatrix[i][1];
				
				mean_energy += spinMatrix[i][j]*spinMatrix[i][L-1];
			// Corners:
			// Corner 1:
				if (i-1 < 0 && j-1 <0){
					mean_energy += spinMatrix[0][0]*spinMatrix[0][1];
					mean_energy += spinMatrix[0][0]*spinMatrix[1][0];
					mean_energy += spinMatrix[0][0]*spinMatrix[0][L-1];
					mean_energy += spinMatrix[0][0]*spinMatrix[L-1][0];
				}
			// Corner 2:
				else if (i-1 < 0 && j+1 > L-1){
					mean_energy += spinMatrix[0][L-1]*spinMatrix[0][0];
					mean_energy += spinMatrix[0][L-1]*spinMatrix[1][L-1];
					mean_energy += spinMatrix[0][L-1]*spinMatrix[L-1][L-1];
					mean_energy += spinMatrix[0][L-1]*spinMatrix[0][L-2];
				}
			// Corner 3:
				else if (i > L-2 && j-1 < 0){
					mean_energy += spinMatrix[L-1][0]*spinMatrix[L-2][0];
					mean_energy += spinMatrix[L-1][0]*spinMatrix[L-1][1];
					mean_energy += spinMatrix[L-1][0]*spinMatrix[L-1][L-1];
					mean_energy += spinMatrix[L-1][0]*spinMatrix[0][0];
				}
			// Corner 4:
				else if (i > L-2 && j > L-2){
					mean_energy += spinMatrix[L-1][L-1]*spinMatrix[L-1][L-2];
					mean_energy += spinMatrix[L-1][L-1]*spinMatrix[L-2][L-1];
					mean_energy += spinMatrix[L-1][L-1]*spinMatrix[L-1][0];
					mean_energy += spinMatrix[L-1][L-1]*spinMatrix[0][L-1];
				}
			} 
			//mean_energy *= (-J/2.0);*/
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
	return abs(magnetization);
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
	createRandomSpins(L,spins);
}

void printSpinMatrix(int L, double** spins) {
	for(int i= 0; i < L; i++) {
		for(int j = 0; j <L; j++) {
			cout << spins[i][j] << " ";
		}
		cout << endl;
	}
}

void metropolisAlgorithm(double& E, double& M, double& cv, double& chi, int L, int N, double J, double** spinMatrix){
	// Wirte to file
	ofstream myfile; 
	myfile.open("expect_T2_4.dat");
	// Calculate current energy
	double energy = calculateEnergy(L,J,spinMatrix);
	double magnetizationSum = 0;
	double magnetization, E2, M2;
	double energySum = energy;
	double eSquaredSum = 0;
	double mSquaredSum = 0;
	int n = 0;
	double T = 2.4;
	double beta = 1./T;
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
		} else { 
			double w = exp(-beta*dE);
			double max = RAND_MAX;
			double r = rand() / ((double) max);
			if (r < w){
				energy = new_energy;
				magnetization = calculateMagnetization(L,spinMatrix);
			} else {
				spinMatrix[i][j] *= (-1);
			}
		}
		energySum += energy;
		eSquaredSum += energy*energy;
		magnetizationSum += magnetization;
		mSquaredSum += magnetization*magnetization;
		n += 1;

		myfile << energySum/((double)n*L*L) << " " << abs(magnetizationSum/((double) n*L*L)) << endl;
	}
	E = energySum/N;
	M = magnetizationSum/N;
	E2 = eSquaredSum/N;
	M2 = mSquaredSum/N;
	cv = (E2 - E*E)/(T*T);
	chi = (M2 - M*M)/T;

	myfile.close();
}

void printResults(double N, double energy, double magnetization, double cv, double chi){
	cout << "After " << N << " loops, the results are:" << endl;
	cout << "  o  Mean energy:              " << energy << endl;
	cout << "  o  Mean magnetization:       " << magnetization << endl;
	cout << "  o  Heat capacity:            " << cv << endl;
	cout << "  o  Magnetic susceptibility   " << chi << endl;
}

//print "i = %-10.3d" % i