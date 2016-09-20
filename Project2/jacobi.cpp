#include <iostream>
#include <cmath>
#include "jacobi.h"

using namespace std;

double biggest_offdiag_value( double ** A, int * k, int * l, int n);
void rotate( double ** A, double ** R, int k, int l , int n);

void jacobi_algorithm( double ** A, double ** R, int n){
	double epsilon = pow(10,-8);
	int k, l;

	// Make eigenvector matrix
	for (int i = 0; i < n; i++){
		for (int j = 0; j < n; j++){
			if (i==j){
				R[i][j] = 0.0;
			}
		}
	}

	double max_iterations = (double) n * (double) n * (double) n;
	int iterations = 0;
	double maxoffdiagonal = biggest_offdiag_value(A, &k, &l, n);

	while (fabs(maxoffdiagonal) > epsilon && (double) iterations < max_iterations){
		maxoffdiagonal = biggest_offdiag_value(A, &k, &l, n);
		rotate(A,R,k,l,n);
		iterations ++;
	}

	cout << "Number of iterations = " << iterations << endl;
	return;
}


// Function to find the maximum matrix element:
double biggest_offdiag_value( double ** A, int * k, int * l, int n){
	double max = 0.0;
	for (int i = 0; i < n; i++){
		for (int j = 0; j < n; j++){
			if (fabs(A[i][j]) > max){
				max = fabs(A[i][j]);
				*l = i;
				*k = j;
			}
		}
	}
	return max;
}

// Funtion to find the values of cos and sin:
void rotate( double ** A, double ** R, int k, int l , int n){
	double s, c; // Shortened for sin and cos
	if (A[k][l] != 0.0){
		double t, tau;
		tau = (A[l][l] - A[k][k])/(2*A[k][l]);
		if (tau > 0){
			t = 1.0/(tau + sqrt(1.0 + tau*tau));
		} else {
			t = -1.0/(-tau + sqrt(1.0 + tau*tau));
		}
		c = 1.0/(1+t*t);
		s = t*c;
	} else {
		c = 1.0;
		s = 0.0;
	}
	// Define elements with indices l and k
	double a_kk, a_ll, a_ik, a_il, r_ik, r_il;
	a_kk = A[k][k];
	a_ll = A[l][l];

	// Changing matrix elements with indices k and l
	A[k][k] = c*c*a_kk - 2.0*c*s*A[k][l] + s*s*a_ll;
	A[l][l] = s*s*a_kk + 2.0*c*s*A[k][l] + c*c*a_ll;
	A[k][l] = 0.0;
	A[l][k] = 0.0;

	// Change remaining elements
	for (int i = 0; i < n; i++){
		if (i != k && i != l){
			a_ik = A[i][k];
			a_il = A[i][l];
			A[i][k] = c*a_ik - s*a_il;
			A[k][i] = A[i][k];
			A[i][l] = c*a_il + s*a_ik;
			A[l][i] = A[i][l];
		}
		// Compute new eigenvectors
		r_ik = R[i][k];
		r_il = R[i][l];
		R[i][k] = c*r_ik - s*r_il;
		R[i][l] = c*r_il + s*r_ik;
	}
	return;
}
