#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

// Exact solution we want to compare with
double source_term(double x){
    return 100*exp(-10*x);
}

int main()
{
    // Declaring variables and vectors
    int n = 10;
    double h = 1./(n+1);
    double *a = new double[n+2];
    double *b = new double[n+2];
    double *c = new double[n+2];
    double *u = new double[n+2];
    double *f = new double[n+2];
    double *x = new double[n+2];
    double *b_tilde = new double[n+2];
    double *c_tilde = new double[n+2];
    double *f_tilde1 = new double[n+2];
    double *f_tilde2 = new double[n+2];
    double *f_exact = new double[n+2];
    cout << "So far so good" << endl;
    // Fill vectors with values
    for(int i = 0; i < n+2; i++){
        a[i] = 2;
        b[i] = -1;
        c[i] = -1;
        f[i] = h*h*source_term(i*h);
    }
    // Forward substitution
    for(int i = 0; i < n+1; i++){
        b_tilde[i] = b[i] - (c[i-1]*a[i-1])/b_tilde[i-1];
        f_tilde1[i] = f[i] - (c[i-1]*a[i-1])/b_tilde[i-1];
    }
    // Backward substitution
    for(int i = n+1; i > 0; i--){
        c_tilde[i] = c[i] - c[i+1]/b_tilde[i+1];
        f_tilde2[i] = f_tilde1[i] - c[i+1]/b_tilde[i+1];
    }
    cout << "So far so good" << endl;
    // Then u is equal to f_tilde2
    for(int i = 0; i < n+2; i++){
        u[i] = f_tilde2[i];
    }
    // Fillling x with values
    for(int i = 0; i < n+2; i++){
        x[i] = i*h;
    }
    // Discretize exact solution to compare with approximation
    for(int i = n+1; i > 0; i--){
        f_exact[i] = source_term(x[i]);
    }
    // Write result to file
    ofstream myfile;
    cout << "We have openened a file!" << endl;
    myfile.open("res2.txt");
    for(int i = 0; i < n+2; i++){
        myfile << i << " " << u[i] << " " << f_exact[i] << endl;
    }
    myfile.close();
    cout << "File closed, deleting values..." << endl;
    delete [] a;
    delete [] b;
    delete [] c;
    delete [] f;
    delete [] u;
    delete [] x;
    delete [] f_tilde1;
    delete [] f_tilde2;
    delete [] b_tilde;
    delete [] c_tilde;
    delete [] f_exact;

    cout << "Done!" << endl;

    return 0;
}

