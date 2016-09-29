#include <iostream>
#include <cmath>
#include <algorithm>
#include <armadillo>
#include <iomanip>
#include "functions.h"

//using namespace std;

void printMatrix(double ** A, int N) 
{
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			std::cout << std::setw(12) << A[i][j] << " ";
		}
		std::cout << std::endl;
	}
	std::cout << std::endl;
	return; 
}

double* sort(double *v, int n, double** R){
	double* v_sorted = new double[n];
	double ** R_sorted = new double*[n];
	int i = 0;
	for (i=0;i<n;i++){
		R_sorted[i] = new double[n];
	}
	int j = 0;
	for (i=0;i<n+1;i++){
		double a1 = 0;
		double a2 = 0;
		double amax = 0;
		int max_no = 0;
		for(j=0;j<n;j++){
			if (v[j] > amax){
				amax = v[j];
				max_no = j;
			}
		}
		v[max_no] = 0;
		v_sorted[n-i] = amax;
		R_sorted[n-i] = R[max_no]; 
	}
	R = R_sorted;
	return v_sorted;
}

// double ** makeAmatrix(int N, double h, double *V, double nondiagonal_value)
// {
// 	double ** A = new double*[N];
// 	for (int i = 0; i < N; i++) 
// 	{
// 		A[i] = new double [N];
// 		for( int j = 0; j < N; j++)	
// 		{
// 			if (i == j){
// 				A[i][j] = 2.0/(h*h) + V[i+1];
// 			}
// 			else if (i == j+1){
// 				A[i][j] = nondiagonal_value;
// 			}
// 			else if (j == i+1){
// 				A[i][j] = nondiagonal_value;
// 			} else {
// 				A[i][j] = 0.0;
// 			}
// 		}
// 	}
// 	return;
// }

// double ** makeRmatrix(int N)
// {
// 	double ** R = new double*[N];
// 	for ( int i = 0; i < N; i++)
// 	{
// 		R[i] = new double [N];
// 		for (int j = 0; j < N; j++)
// 		{
// 			if (i == j) {R[i][j] = 1}
// 		}   else        {R[i][j] = 0}
// 	}
// 	return R;
// }



	// Make empty NxN matrices A and R
	
	// double ** A = new double*[N];
	// double ** R = new double*[N];
	// for (int i = 0; i < N; i++) {
	// 	A[i] = new double [N];
	// 	R[i] = new double [N];
	// }

	// for (int i = 0; i < N; i++){
	// 	for (int j = 0; j < N; j++){
	// 		if (i == j){
	// 			A[i][j] = 2.0/(h*h) + V[i+1];
	// 			R[i][j] = 1.0;
	// 		}
	// 		else if (i == j+1){
	// 			A[i][j] = nondiagonal_value;
	// 		}
	// 		else if (j == i+1){
	// 			A[i][j] = nondiagonal_value;
	// 		} else {
	// 			A[i][j] = 0.0;
	// 		}	
	// 	}
	// 	R[i][i] = 1.0;
	// }