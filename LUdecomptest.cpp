#include <iostream>
#include "armadillo"

using namespace std;
using namespace arma;

int main(){
	mat A = randu<mat>(5,5); // Random matrix
	vec b = randu<vec>(5);   // Random vector

	A.print("A =");
	b.print("b =");

	// Solve Ax = b:
	vec x = solve(A,b);
	x.print("x =");

	// LU decompostiion:
	mat L,U;
	lu(L,U,A);

	L.print("L =");
	U.print("U =");

	// Check that A = LU
	(A - L*U).print("Test of LU decompostiion");
	return 0;
}