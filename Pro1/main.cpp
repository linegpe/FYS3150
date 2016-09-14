#include <iostream>
#include <cmath>
#include <fstream>
#include "armadillo"
#include "time.h"

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
    int n = 12;      // Length/size of vectors/matrices

    double h = 1./(n-1);
    double *a = new double[n];
    double *b = new double[n];
    double *c = new double[n];
    double *u = new double[n];
    double *f = new double[n];
    double *x = new double[n];
    double *u_exact = new double[n];
    double *b2 = new double[n];
    double *f2 = new double[n];
    double *u2 = new double[n];

    // Fill vectors with values
    for(int i = 0; i < n; i++){
        a[i] = -1;
        b[i] = 2;
        b2[i] = 2;
        c[i] = -1;
        f[i] = h*h*source_term(i*h);
        f2[i] = h*h*source_term(i*h);
    }

    // Dirichlet boundary conditions:
    a[n-1] = 0;

    b[0] = 1;
    b[n-1] = 1;
    
    c[0] = 0;
    
    f[0] = 0;
    f[n-1] = 0;

    b2[0] = 1;
    b2[n-1] = 1;

    f2[0] = 0;
    f2[n-1] = 0;

    // PART 1: EXACT SOLUTION

    // Fillling x with values
    for(int i = 0; i < n; i++){
        x[i] = i*h;
    }
    // Discretize exact solution to compare with approximations
    for(int i = n-1; i > 0; i--){
        u_exact[i] = exact_solution(x[i]);
    }

    // PART 2: GENERAL ALGORITHM

    clock_t start_general, finish_general; // Timing the algorithm
    start_general = clock();

    // Forward substitution
    for(int i = 1; i < n; i++){
        b[i] = b[i] - (c[i-1]*a[i])/b[i-1];
        f[i] = f[i] - (f[i-1]*a[i])/b[i-1]; 
    }
    // Backward substitution
    for(int i = n-2; i >= 0; i--){
        u[i] = (f[i] - c[i]*u[i+1])/b[i];
    }
    finish_general = clock();
    double time_general = ( double (finish_general - start_general)/CLOCKS_PER_SEC);
    cout << "Relative time, general algorithm: " << time_general << endl;

    // Calculating the error
    double *epsilon = new double[n];
    for (int i = 1; i < n-1; i++){
        epsilon[i] = log(fabs((u[i]-u_exact[i])/u[i]));
    } 
    cout << "Error estimate: " << epsilon[1] << endl; 

    // PART 3: SPECIAL CASE ALGORITHM

    clock_t start_special, finish_special; // Timing the algorithm
    start_special = clock();

    // Forward
    for(int i = 1; i < n; i++){
        b2[i] = double((i+1.0)/i);
        f2[i] = f2[i] + (f2[i-1])/b2[i-1];
    }

    // Backward
    for(int i = n-2; i > 0; i--){
        u2[i] = (f2[i] + u2[i+1])/b2[i];
    }

    finish_special = clock();
    double time_special = ( double (finish_special - start_special)/CLOCKS_PER_SEC);
    cout << "Relative time, special algorithm: " << time_special << endl;

    // PART 4: LU DECOMPOSITION

    // Check if n is too big for LU-decomposition
    int n_max = 1500; // Biggest value for n that does not crash computer
    int N = 0;
    if (n >= n_max){
        N = 0;
        cout << "n-value too big to perform LU-decomposition. " << endl; // Aborts
    }
    else{
        N = n;
    }

    // Define A as a matrix (armadillo syntax)
    mat A = zeros<mat>(N,N);
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
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

    // Special elements:
    A(0,0) = 1;
    A(0,1) = 0;
    A(n-1,N-1) = 1;
    A(n-1,N-2) = 0;

    // Define the f-vector
    vec f_vec = zeros<vec>(N);
    for (int i = 0; i< N; i++){
        f_vec(i) = h*h*source_term(x[i]);
    }
    f_vec(0) = 0;
    f_vec(N-1) = 0;

    clock_t start_LU, finish_LU;
    start_LU = clock();

    // LU decomposition
    mat L,U;
    lu(L,U,A);
    mat y_vec = solve(L,f_vec);
    vec v_vec = solve(U,y_vec);

    finish_LU = clock();
    double time_LU = ( double (finish_LU - start_LU)/CLOCKS_PER_SEC);
    cout << "Relative time, LU decomposition:  " << time_LU << endl;


    // Write result to file
    // Colons: 
    // 1: i, 2: general alg. solution, 3: exact solution, 4: LU solution, 5: error estimate, 6: special alg. solution
    ofstream myfile;
    myfile.open("res2.txt");
    for(int i = 0; i < n; i++){
        myfile << i << " " << u[i] << " " << u_exact[i] << " " << v_vec[i] <<  " " << epsilon[i] << " " << u2[i] << endl;
    }
    myfile.close();
    delete [] a;
    delete [] b;
    delete [] c;
    delete [] f;
    delete [] u;
    delete [] x; 
    delete [] f2;
    delete [] b2;

    cout << "Done!" << endl;

    return 0;
}