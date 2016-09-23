// Expanded version of writetofile.cpp
# include <iostream>
# include <fstream>

using namespace std;

int sum(int a, int b);

int main(){
	int a = 2;
	int b = 3;
	int c = 7;
	int d = 8;
	ofstream myfile;
	myfile.open("resultoutput.txt");
	myfile << sum(a,b) << " " << sum(a,d) << "\n" << sum(c,d);
	myfile.close();
}

int sum(int a, int b){
	return a + b;
}
