//Testing the program for the Jacobi method

#include "jacobi.h"
#include <vector>
#include <iostream>
#include "armadillo"


using namespace arma;
using namespace std;
double* sort_2(double *v, int n, double** R);
void test_highest_element(double** A, int n, double amax);
//double* test_armadillo(double** A, int n);
void test_orthogonality(double**A, int n);
double mean(double*v, int n);
void test_sort(double*v, int n);
void run_all_tests(int a);
//double** conv_to_arma(double** A, int n);


void run_all_tests(int a){
	int i; int j;
	int n = 20;
	double** A = new double*[n];
	double* v = new double[n];
for (i=0;i<n;i++){
	A[i] = new double[n];
	A[i][i] = 1;
	A[i][i+1] = 2;
	A[i][i-1] = 2;
	v[i] = i;
}

double amax = 2;
test_orthogonality(A, n);
test_highest_element(A, n, amax);
test_sort(v, n);
	return;
}


void test_orthogonality(double** A, int n){
	int i;int j; int k;
	//A has to be an orthogonal matrix!
	double** eigvecs = new double*[n];
	for (i=0;i<n;i++){
		eigvecs[i] = new double[n];
	}
	jacobi_method(A, eigvecs, n);
	//Calculating inner product:
	double inner_product = 0;
	int b;
	double inner_product_ij;
	//If the vectors are not orthogonal, the "inner product" will be much larger than zero
	cout << "checking orthogonality" << endl;
	for (i=0;i<n;i++){
		for (j=0; j<n; j++){
			if (i != j){
				for (k=0;k<n;k++){
					inner_product_ij += eigvecs[i][k]*eigvecs[j][k];
				}
				if (inner_product_ij < 1E-10){
					inner_product_ij = 0;
				}
				else{
					b = 0;
				}
				inner_product += inner_product_ij;
		}
		else{
			b = 0;
		}	

		}
	}
	if (inner_product < 1E-8){
		cout << "The Jacobi method preserves orthogonality" << endl;
	}
	else{
		cout << "The Jacobi method does not preserve orthogonality :o :( :'( " << endl;
	}
	return;
}

void test_sort(double*v, int n){
	int i; double a;
	double** R = new double*[n];
	double* v_sorted = new double[n];
	for (i=0;i<n;i++){
		R[i] = new double[n];
	}
	int check = 0;
	v_sorted = sort_2(v, n, R);
	for (i=0;i<n;i++){
	}
	for (i=0;i<n-1;i++){
		a = v_sorted[i] - v_sorted[i+1];
		if (a < 0){
			check += 0;
		}
		else if (a == 0){
			check += 0;
		}
		else{
			check += 1;
		}
	}
	if (check == 0){
		cout << "The sorting function works! "<< endl;
	}
	else{
		cout << "The sorting function does not work.." << endl;
	}
}




void test_highest_element(double** A, int n, double amax){
	int k; int l;
	double amax_jacobi = maxoffdiag(A, &k, &l, n);
	cout << amax_jacobi << endl;
	cout << abs(amax - amax_jacobi) << endl;
	if (abs(amax - amax_jacobi) < 1E-5){
		cout << "Maxoffdiag works" << endl;
	}
	else{
		cout << "Maxoffdiag does not work" << endl;
	}
	return;
}


double mean(double*v, int n){
	int i;
	double sum = 0;
	for (i=0;i<n;i++){
		sum += v[i];
	}
	return sum/double(n);
}

double* sort_2(double *v, int n, double** R){
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
		//int count = 0; 
		for(j=0;j<n;j++){
			if (v[j] > amax){
				amax = v[j];
				max_no = j;
				//cout << v[j] << endl;
				//count++;
			}
		}
		v[max_no] = 0;
		v_sorted[n-i] = amax;
		R_sorted[n-i] = R[max_no]; 

		//cout << v_sorted[n-i] << endl;
	}
	//v = v_sorted;
	R = R_sorted;
	return v_sorted;}






