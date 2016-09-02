# include <iostream>
# include <vector>
# include <math.h>
# include <string>
# include <cmath>

using namespace std;

double f(double x);
double derivert(double x, double h);
double derivert_mfeil(double x, double h);
double totalfeil(double x, double h);


int main(){
	
	double x = sqrt(2);
	double h = 0.001; // Step length
	cout << "Uten feilledd: " << derivert(x,h) << endl;
	cout << "Med feilledd: " << derivert_mfeil(x,h) << endl;
	cout << "Absoluttfeil: " << totalfeil(x,h) << endl;

	return 0;
}

double f(double x){
	return atan(x);
}

double o(double h){
	return h*h;
}

double likn1(double x, double h){
	double f2c = (f(x+h) - f(x))/h + o(h);
	return f2c;
}

double likn2(double x, double h) {
	double f3c = (f(x+h) - f(x-h))/(2*h) + o(h*h);
	return f3c;
}

double derivert(double x, double h){
	return (f(x+h) - f(x-h))/(2*h); // + o(h*h);
}

double derivert_mfeil(double x, double h){
	return (f(x+h) - f(x-h))/(2*h) + o(h); // + o(h*h);
}

double totalfeil(double x, double h){
	return 1/3 - abs(derivert_mfeil(x,h));
}