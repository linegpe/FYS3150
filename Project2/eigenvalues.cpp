#include <iostream>
#include <cmath>
#include "armadillo"

using namespace std;
using namespace arma;

int main(){

	// Declare constants
	int N = 400;
	double rho0 = 0.0;
	double rhomax = 10.0;
	double h = (rhomax - rho0)/(N+1);
	double evalue = -1.0/(h*h);
	double diagconst = 2.0/(h*h);

	// Make rho vector
	vec rho = zeros<vec>(N+1);{
	for (int i = 0; i < N+1; i++)
		rho(i) = rho0 + i*h;
	}

	// Make V vector
	vec V = zeros<vec>(N+1);
	for (int i = 0; i < N+1; i++){
		V(i) = rho(i)*rho(i);
	}

	// Declare NxN matrix A
	mat A = zeros<mat>(N,N);
	for (int i = 0; i < N-1; i++){
		A(i,i) = diagconst + V(i+1);
		A(i,i+1) = evalue;
		A(i+1,i) = evalue;
	}
	A(N-1,N-1) = -2*evalue + V(N);

	// Timing the algorithm
    clock_t start, finish; 
    start = clock();

	// Find the eigenvectors and eigenvalues
	mat eigvec;
	vec eigval;
	eig_sym(eigval, eigvec, A);

	// Timing finished
    finish = clock();
    double time = ( double (finish - start)/CLOCKS_PER_SEC);
    cout << endl << "Run time: " << time << " sec." << endl << endl;

    // Write eigenvalues in terminal
	cout << "Eigenvalues: " << endl;
	for (int i = 0; i < 3; i++){
		cout << eigval(i) << endl;
	}
	cout << endl;

	// Write results to file if wanted
	cout << "Do you wish to save these results? [y/n] ";
	string answer;
	cin >> answer;
	if (answer == "y"){

		cout << "Where do you want to save the results? ";
		string filename;
		cin >> filename;

		ofstream myfile;
		myfile.open(filename.c_str());

		myfile << "Eigenvalues" << "    " << "Time" << endl;
		myfile << "  " << eigval(0) << "    " << time << endl;
		myfile << "  " << eigval(1) << endl << "  " << eigval(2);

		myfile.close();
		cout << "Results saved in " << filename << endl << endl;
	} else {
		cout << "Data not stored in file. " << endl << endl;
	}

	return 0;
}