#include <iostream>
#include <cmath>
#include "jacobi.h"
#include <algorithm>
#include "armadillo"

#include <iomanip>

using namespace std;
using namespace arma;

void printMatrix(double ** A, int N) {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cout << setw(12) << A[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
	return; 
}

int main(){
	int N = 200;

	// Declaring constants:
	double mass = 0.5e6;	//eV/c^2
	double hbar = 1240;		//eVnm/c^2
	double beta_e2 = 1.44; 	//eVnm
	double alpha = hbar*hbar/(mass*beta_e2);
	double omega2 = 0.25; 	//(1.0/4.0) * (m*k/hbar) * pow(alpha,4);
	double konst = mass*omega2;

	double epsilon = pow(10,-8);
	double *rho = new double[N+1];
	double *V = new double[N+1];

	double rho0 = 0.0;
	double rhoN = 5.0;
	rho[0] = rho0;

	double h = (rhoN-rho0)/(N+1.0); // Steplength

	double nondiagonal_value = -1.0/(h*h);
	

	for (int i = 0; i < N+1; i++){
		rho[i] = rho0 + i*h;
		V[i] = rho[i]*rho[i]*omega2 + 1.0/rho[i];
	}

	cout << endl;


	// Make empty NxN matrices A and R
	
	double ** A = new double*[N];
	double ** R = new double*[N];
	for (int i = 0; i < N; i++) {
		A[i] = new double [N];
		R[i] = new double [N];
	}

	// Define end values
	A[N-1][N-1] = 2.0/(h*h) + V[N];

	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++){
			if (i == j){
				A[i][j] = 2.0/(h*h) + V[i+1];
				R[i][j] = 1.0;
			}
			else if (i == j+1){
				A[i][j] = nondiagonal_value;
			}
			else if (j == i+1){
				A[i][j] = nondiagonal_value;
			} else {
				A[i][j] = 0.0;
			}	
		}
		R[i][i] = 1.0;
	}

	// Jacobi's method:
	int k, l;
	double maxoffdiagonal = biggest_offdiag_value(A, &k, &l, N);
	int iterations = 0;

	int max_iterations = N * N * N;

	// Timing the algorithm
    clock_t start, finish; 
    start = clock();
	
	while (fabs(maxoffdiagonal) > epsilon && iterations < max_iterations){
		rotate(A,R,k,l,N);
		maxoffdiagonal = biggest_offdiag_value(A, &k, &l, N);
		iterations++;
	}

	// Timing finished
    finish = clock();
    double time = ( double (finish - start)/CLOCKS_PER_SEC);
    cout << endl << "Run time: " << time << " sec." << endl << endl;

	cout << endl << "Number of iterations: " << iterations << endl << endl;


	// Sort eigenvalues:
	double *eigenvalues = new double [N];
	for (int i = 0; i < N; i++){
		eigenvalues[i] = A[i][i];
	}


	vec eigval2 = zeros<vec>(N);

	// Print 3 first eigenvalues
	cout << "Eigenvalues" << endl;
	for (int i = 0; i < N; i++){
		eigval2(i) = eigenvalues[i];
	}
	eigval2 = sort(eigval2);
	cout << eigval2(0) << endl;
	cout << eigval2(1) << endl;
	cout << eigval2(2) << endl;


	//Find index of eigenvalues
	int index0;
	int index1;
	int index2;
	for (int i = 0; i < N; i++){
		if (fabs(eigenvalues[i] - eigval2(0)) < epsilon) {index0 = i;}
		if (fabs(eigenvalues[i] - eigval2(1)) < epsilon) {index1 = i;}
		if (fabs(eigenvalues[i] - eigval2(2)) < epsilon) {index2 = i;}
	}


	// Write results to file if wanted
	cout << "Do you wish to save the eigenvalues and runtime? [y/n] ";
	string answer;
	cin >> answer;
	if (answer == "y"){

		cout << "Where do you want to save the results? ";
		string filename;
		cin >> filename;

		ofstream myfile;
		myfile.open(filename.c_str());

		myfile << "Eigenvalues" << "    " << "Time" << "    " << "Iterations" << endl;
		myfile << "  " << eigval2(0) << "    " << time << "    " << iterations << endl;
		myfile << "  " << eigval2(1) << endl << "  " << eigval2(2);

		myfile.close();
		cout << "Results saved in " << filename << endl << endl;
	} else {
		cout << "Data not stored in file. " << endl << endl;
	}

	ofstream myfile;
	myfile.open("eigvecs2.txt");
	for (int i = 0; i < N; i++){
		myfile << pow(R[i][index0],2) << "   " << pow(R[i][index1],2) << "   " << pow(R[i][index2],2) << endl;
	}
	myfile.close();
	return 0;

}