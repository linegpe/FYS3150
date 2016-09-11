// Example of how to write to file 
# include <iostream>
# include <fstream>

using namespace std;

int main(){
	ofstream myfile;
	myfile.open(fileoutput.txt);
	myfile << "Writing this to file.\n";
	myfile.close();
	return 0;
}