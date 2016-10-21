#include <iostream>

using namespace std;

double* sort(double *vec, int N)
{
	double max = 0.0;
	for (int i = N-1; i = 0; i--)
	{
		
		for (int j = N-1; j = 0; i--)
		{
			if (vec[j] > max) {max = vec[j];}	
		}
		vec[i] = max;
	}
	return vec;
}

int main(){
	int N = 9;
	double *vec = new double[N];
	double *newvec = new double[N];

	for (int i = 0; i < N; i++)
	{
		vec[i] = N*N-i;
		cout << vec[i] << endl;
	}
	newvec = sort(vec,N);
	for (int i = 0; i < N; i++)
	{
		cout << newvec[i] << endl;
	}
}