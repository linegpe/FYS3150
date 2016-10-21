#include <iostream>
#include "functions.h"

using namespace std;

int main(){
	int N = 2;
	double **A = new double*[N];
	for (int i=0; i<N; i++){
		A[i] = new double[N];
	}
	A[0][0] = 3;
	A[0][1] = 1;
	A[1][0] = 5;
	A[1][1] = 4;

	printMatrix(A,N);

	return 0;
}