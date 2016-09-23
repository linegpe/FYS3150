# include <iostream>
using namespace std;
int main(){
	int number = 5;
	int number2 = 4;
	cout << "Number: " << (long)&number << endl; // Changing between number and &number is changing between 5 and its adress
	cout << "Number2: " << (long)&number2 << endl;
	return 0;										// (long) makes the number not hexadecimal

}