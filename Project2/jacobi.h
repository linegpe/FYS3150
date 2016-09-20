#ifndef JACOBI_H
#define JACOBI_H

// Function to find the biggest offdiagonal value in a matrix
double biggest_offdiag_value( double ** A, int * k, int * l, int n);

// Function to rotate the matrix to use Jacobi's method
void rotate( double ** A, double ** R, int k, int l , int n);

// Function that performs Jacobi's algorithm
void jacobi_algorithm( double ** A, double ** R, int n);
#endif