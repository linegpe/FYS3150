#include <iostream>
#include <cmath>
#include "jacobi.h"
// #include <fstream>
// #include "armadillo"

using namespace std;
// using namespace arma;

int main(){
	int N = 10;
	double epsilon = pow(10,-8);
	double *rho = new double(N);
	double *V = new double(N);

	double rho0 = 0;
	double rhoN = 10;
	rho[0] = rho0;

	double h = (rhoN-rho0)/(N+1.0); // Steplength

	double nondiagonal_value = -1./(h*h);
	

	for (int i = 0; i < N; i++){
		rho[i] = rho0 + i*h;
		V[i] = rho[i]*rho[i];
		//nondiag1[i] = nondiagonal_value;
		//diagonal[i] = 2.0/(h*h) + V[i];
	}

	// Make empty NxN matrices A and R
	
	double ** A = new double*[N];
	double ** R = new double*[N];
	for (int i = 0; i < N; i++) {
		A[i] = new double [N];
		R[i] = new double [N];
	}

	// Define end values
	//A[0][0] = 0.0;
	//R[0][0] = 0.0;
	A[N-1][N-1] = 0.0;
	R[N-1][N-1] = 0.0;


	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++){
			if (i == j){
				A[i][j] = 2.0/(h*h) + V[i];
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

	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++){
			cout << R[i][j] << "  ";
		}
		cout << endl;
	}
	cout << endl;


	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++){
			cout << A[i][j] << "  ";
		}
		cout << endl;
	}
	cout << endl;

	// Jacobi's method:
	int k, l;
	double maxoffdiagonal = biggest_offdiag_value(A, &k, &l, N);
	int iterations = 0;

	int max_iterations = N * N * N;
	
	while (fabs(maxoffdiagonal) > epsilon && iterations < max_iterations){
		rotate(A,R,k,l,N);
		maxoffdiagonal = biggest_offdiag_value(A, &k, &l, N);
		iterations++;
	}

	cout << "Number of iterations: " << iterations << endl;


	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++){
			cout << R[i][j] << "  ";
		}
		cout << endl;
	}
	cout << endl;
	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++){
			cout << A[i][j] << "  ";
		}
		cout << endl;
	}
	cout << endl;


	return 0;
}