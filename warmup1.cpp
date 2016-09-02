# include <iostream>
# include <vector>
# include <math.h>
# include <string>
# include <cmath>
# include <fstream>
using namespace std;

double f(double x);
double derivert(double x, double h);
double derivert_mfeil(double x, double h);
double totalfeil(double x, double h);


int main(){
	
	double x = sqrt(2);
	ofstream myfile;
	myfile.open("warmupresults.txt");
	for (int tall = 1; tall<20; ++tall){
		double h = 1./pow(10, tall);
		cout << "Steglengde " << h << " gir: " << endl;
		cout << "Uten feilledd: " << derivert(x,h) << endl;
		cout << "Med feilledd: " << derivert_mfeil(x,h) << endl;
		cout << "Absoluttfeil: " << totalfeil(x,h) << endl << endl;
		myfile << log10(h) << " " << log(totalfeil(x,h)) << endl;

	}
	myfile.close();


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
	return (f(x+h) - f(x-h))/(2*h);
}

double derivert_mfeil(double x, double h){
	return (f(x+h) - f(x-h))/(2*h) + o(h);
}

double totalfeil(double x, double h){
	return abs((1./3) - derivert_mfeil(x,h));
}