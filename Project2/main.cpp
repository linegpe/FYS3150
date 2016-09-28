#include <iostream>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include "jacobi.h"
#include "functions.h"

using namespace std;
using namespace arma;

int main(){
	// Declaring constants and variables
	int N = 200;

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
		V[i] = rho[i]*rho[i];
	}

	cout << endl;
	
	// Make matrices A and R
	double ** A = new double*[N];
	double ** R = new double*[N];
	for (int i = 0; i < N; i++) {
		A[i] = new double [N];
		R[i] = new double [N];
	}

	// Fill A and R with values
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
	
	// Running the algorithm
	while (fabs(maxoffdiagonal) > epsilon && iterations < max_iterations){
		rotate(A,R,k,l,N);
		maxoffdiagonal = biggest_offdiag_value(A, &k, &l, N);
		iterations++;
	}

	// Timing finished
    finish = clock();
    double time = ( double (finish - start)/CLOCKS_PER_SEC);
    
    // Print results to terminal
    cout << endl << "Run time: " << time << " sec." << endl << endl;
	cout << endl << "Number of iterations: " << iterations << endl << endl;

	// Sorting eigenvalues
	double *neweigvals = new double[N];
	double *eigenvalues = new double [N];
	for (int i = 0; i < N; i++){
		eigenvalues[i] = A[i][i];
		neweigvals[i] = A[i][i];
	}

	double *eigenvalues_sorted = new double[N];
	eigenvalues_sorted = sort(eigenvalues, N, R);

	cout << "Eigenvalues: " << endl;
	for (int i = 1; i < 4; i++) // First element 0
	{
		cout << eigenvalues_sorted[i] << endl;
	}

	//Find index of eigenvalues
	int index0;
	int index1;
	int index2;
	double eps2 = 0.1;
	for (int i = 0; i < N; i++){
		if (fabs(neweigvals[i] - eigenvalues_sorted[1]) < epsilon) {index0 = i;}
		if (fabs(neweigvals[i] - eigenvalues_sorted[2]) < epsilon) {index1 = i;}
		if (fabs(neweigvals[i] - eigenvalues_sorted[3]) < epsilon) {index2 = i;}
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
		myfile << "  " << eigenvalues_sorted[1] << "    " << time << "    " << iterations << endl;
		myfile << "  " << eigenvalues_sorted[2] << endl << "  " << eigenvalues_sorted[3];

		myfile.close();
		cout << "Results saved in " << filename << endl << endl;
	} else {
		cout << "Data not stored in file. " << endl << endl;
	}

	// Write eigenvectors to file
	ofstream myfile;
	myfile.open("eigvecs.txt");
	for (int i = 0; i < N; i++){
		myfile << pow(R[i][index0],2) << "   " << pow(R[i][index1],2) << "   " << pow(R[i][index2],2) << endl;
	}
	myfile.close();
	return 0;
}