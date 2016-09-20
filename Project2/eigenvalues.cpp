#include <iostream>
#include <cmath>
#include "armadillo"

using namespace std;
using namespace arma;

int main(){
	int N = 5;
	double rho0 = 0;
	double rhomax = 100;
	double h = (rhomax - rho0)/(N+1);
	double evalue = -1.0/(h*h);


	// Make rho vector
	vec rho = zeros<vec>(N);{
	for (int i = 0; i < N; i++)
		rho(i) = rho0 + i*h;
	}

	// Make V vector
	vec V = zeros<vec>(N);
	for (int i = 0; i < N; i++){
		V(i) = rho(i)*rho(i);
	}

	// Declare NxN matrix A
	mat A = zeros<mat>(N,N);
	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++){
			if (i==j){
				A(i,j) = 2.0/(h*h) + V(i)*V(i);
			}
			else if (i==j+1){
				A(i,j) = evalue;
			}
			else if (i==j-1){
				A(i,j) = evalue;
			}
			else{
				A(i,j) = 0.0;
			}
		}
	}
	A(0,0) = 0.0;
	A(N-1,N-1) = 0.0;

	A.print("Matrix A: ");

	// Find the eigenvectors and eigenvalues
	mat eigvec;
	vec eigval;
	eig_sym(eigval, eigvec, A);

	eigval.print("Eigenvalues: ");



	return 0;
}