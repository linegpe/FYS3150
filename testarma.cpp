# include <armadillo>
# include <iostream>

using namespace std;
using namespace arma;

int main(int argc, char** argv){
	mat A = randu<mat>(5,5);
	mat B = randu<mat>(5,5);
	cout << A*B << endl;
	retrun 0;
}