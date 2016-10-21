#include <iostream>
#include <stdlib.h>
#include "jacobi.h"

using namespace std;

int main(){
	// Test function to return largest non-diagonal element:
	int N = 5;
	cout << "Matrix with random numbers from 1 to (insert highest number): ";
	int max;
	cin >> max;

	double ** A = new double*[N];
	for (int i = 0; i < N; i++) {
		A[i] = new double [N];
	}

	cout << endl << "A before rotation: " << endl << endl;
	for (int i=0; i<N; i++){
		for (int j=0; j<N; j++){
			A[i][j] = rand() % max;
			cout << A[i][j] << "  ";
		}
		cout << endl;
	}

	int k, l;

	double maxoffdiagonal;
	maxoffdiagonal = biggest_offdiag_value(A, &k, &l, N);
	cout << endl << "The biggest off-diagonal values is " << maxoffdiagonal << endl << endl;

	// Test rotate function:

	// Create random symmetric matrix B
	double ** B = new double*[N];
	for (int i = 0; i < N; i++){
		B[i] = new double [N];
		for (int j = 0; j < N; j++){
			B[i][j] = rand() % max;
		}
	}
	cout << endl << "B before rotation: " << endl << endl;
	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++){
			B[j][i] = B[i][j]; // Make it symmetric
			cout << B[i][j] << "  ";
		}
		cout << endl;
	}

	double ** R = new double*[N];
	for (int i = 0; i < N; i++){
		R[i] = new double [N];
		R[i][i] = 1.0;
	}

	cout << "R before rotation: " << endl << endl;
	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++){
			cout << R[i][j] << "  ";
		}
		cout << endl;
	}

	//int k, l;
	rotate(A, R, k, l, N);

	cout << endl << "B after 1 rotation: " << endl << endl;

	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++){
			cout << B[i][j] << "  ";
		}
		cout << endl;
	}

	cout << endl << "R after 1 rotation: " << endl << endl;

	for (int i = 0; i < N; i++){
		for ( int j = 0; j < N; j++){
			cout << R[i][j] << "  ";
		}
		cout << endl;
	}

	return 0;
}