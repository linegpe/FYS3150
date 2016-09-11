#include <iostream>
#include <cmath>
#include <fstream>
#include "armadillo"

using namespace std;
using namespace arma;

// Exact solution we want to compare with
double source_term(double x){
    return 100*exp(-10*x);
   }

double exact_solution(double x){
    return 1 - (1 - exp(-10))*x - exp(-10*x);
}

int main()
{
    // Declaring variables and vectors
    int n = 102;
    double h = 1./(n-1);
    double *a = new double[n];
    double *b = new double[n];
    double *c = new double[n];
    double *u = new double[n];
    double *f = new double[n];
    double *x = new double[n];
    double *u_exact = new double[n];
    //double *b2 = new double[n]; // Make new vectors to use in special algorithm
    //double *

    // Fill vectors with values
    for(int i = 0; i < n; i++){
        a[i] = -1;
        b[i] = 2;
        c[i] = -1;
        f[i] = h*h*source_term(i*h);
    }
    b[0] = 1;
    c[0] = 0;
    f[0] = 0;
    a[n-1] = 0;
    b[n-1] = 1;
    f[n-1] = 0;

    // PART 1: EXACT SOLUTION

    // Fillling x with values
    for(int i = 0; i < n; i++){
        x[i] = i*h;
    }
    // Discretize exact solution to compare with approximation
    for(int i = n-1; i > 0; i--){
        u_exact[i] = exact_solution(x[i]);
    }

    // PART 2: GENERAL ALGORITHM

    // Forward substitution
    for(int i = 1; i < n; i++){
        b[i] = b[i] - (c[i-1]*a[i])/b[i-1];
        f[i] = f[i] - (f[i-1]*a[i])/b[i-1];
    }
    //u[n-1] = f[n-1]/b[n-1]; What happened here? If not needed, delete.
    // Backward substitution
    for(int i = n-2; i >= 0; i--){
        u[i] = (f[i] - c[i]*u[i+1])/b[i];
    }

    // Calculating the error
    double *epsilon = new double[n];
    for (int i = 1; i < n-1; i++){
         epsilon[i] = log(fabs((u[i]-u_exact[i])/u[i]));
    } // Something wrong here. Every element in epsilon are the same.


    // PART 3: LU DECOMPOSITION

    // Define A as a matrix and rest as vectors (armadillo syntax)
    mat A = zeros<mat>(n,n);
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if (i==j){
                A(i,j) = 2;
            }
            else if (i == j-1){
                A(i,j) = -1;
            }
            else if (i == j+1){
                A(i,j) = -1;
            }
            else {
                A(i,j) = 0;
            }
        }
    }

    // Special cases:
    A(0,0) = 1;
    A(0,1) = 0;
    A(n-1,n-1) = 1;
    A(n-1,n-2) = 0;

    A.print("A = ");
    vec f_vec = zeros<vec>(n);
    for (int i = 0; i< n; i++){
        f_vec(i) = h*h*source_term(x[i]);
    }
    f_vec(0) = 0;
    f_vec(n-1) = 0;

    // LU decomposition
    mat L,U;
    lu(L,U,A);
    L.print("L = ");
    U.print("U = ");
    mat y_vec = solve(L,f_vec);
    vec v_vec = solve(U,y_vec);
    cout << v_vec << endl;


    // Write result to file 1 (General alorithm) and LU v in last column
    ofstream myfile;
    myfile.open("res2.txt");
    for(int i = 0; i < n; i++){
        myfile << i << " " << u[i] << " " << u_exact[i] << " " << v_vec[i] <<  " " << epsilon[i] << endl;
    }
    myfile.close();
    delete [] a;
    delete [] b;
    delete [] c;
    delete [] f;
    delete [] u;
    delete [] x;

    cout << "Done!" << endl;

    return 0;
}

