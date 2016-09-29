#ifndef __TESTPROGRAM_H_INCLUDED__
#define __TESTPROGRAM_H_INCLUDED__

double* sort(double *v, int n, double** R);
void test_highest_element(double** A, int n, double amax);
//double* test_armadillo(double** A, int n);
void test_orthogonality(double**A, int n);
double mean(double*v, int n);
void test_sort(double*v, int n);
void run_all_tests(int a);
//double** conv_to_arma(double** A, int n);
#endif
