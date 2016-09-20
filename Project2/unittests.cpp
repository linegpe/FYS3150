#include <iostream>
#include <stdlib.h>
#include "jacobi.h"

using namespace std;

int main(){
	// Test function to return largest non-diagonal element:
	int N = 5;

	double ** A = new double*[N];
	for (int i = 0; i < N; i++) {
		A[i] = new double [N];
	}

	for (int i=0; i<N; i++){
		for (int j=0; j<N; j++){
			A[i][j] = rand() % 50 + 1;
			cout << A[i][j] << "  ";
		}
		cout << endl;
	}

	int k, l;

	double maxoffdiagonal;
	maxoffdiagonal = biggest_offdiag_value(A, &k, &l, N);
	cout << "The biggest off-diagonal values is " << maxoffdiagonal << endl;

	return 0;
}