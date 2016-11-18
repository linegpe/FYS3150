#include <random>
#include <iostream>
#include <fstream>

// How to run from terminal:
// g++ -std=c++11 main.cpp

using namespace std;

void sum_money(double* money,int nr_agents);

int main(){
	int nr_agents = 500;			// Should be 500
	int nr_transactions = 1e7; 	// Should be at least 10^7
	int nr_simulations = 1e3; 	// Should be between 10^3 - 10^4

	int total_money = 0;
	//int max_initial_money = 100;
	double initial_money = 100;
	double lambda = 0.25;

	// Make array with agents
	double* agents = new double[nr_agents];
	for (int i = 0; i < nr_agents; i++){
		agents[i] = i;
	}

	// Make array with money
	double* money = new double[nr_agents];

	// Initial random distribution of money
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> intRNG(0, nr_agents-1);
    uniform_real_distribution<double> doubleRNG(0,1);

	//cout << "100 to everyone: " << endl;
	for (int i = 0; i < nr_agents; i++){
		money[i] = initial_money;
		//cout << money[i] << endl;
	}

	sum_money(money,nr_agents);

	// Metropolis algorithm for transactions
	int completed_transactions = 0;
	while (completed_transactions < nr_transactions){
		// Pick two random agents
		int i = intRNG(gen);
		int j = intRNG(gen);
		if (i != j){

    		double epsilon = doubleRNG(gen);
    		double sum_ij = money[i]+money[j];
			money[i] = lambda*money[i] + epsilon*(1.0-lambda)*sum_ij;
			money[j] = lambda*money[j] + (1.0-epsilon)*(1.0-lambda)*sum_ij;
			completed_transactions += 1;
		} 
	}


	ofstream myfile;
	myfile.open("final_money.dat");
	for (int i = 0; i < nr_agents; i++){
		myfile << money[i] << endl;
	}


	// cout << "Random distribution: " << endl;
	// for (int i = 0; i < nr_agents; i++){
	// 	//cout << money[i] << endl;
	// }
}

void sum_money(double* money,int nr_agents){
	double sum_money = 0;
	for (int i = 0; i < nr_agents; i++){
		sum_money += money[i];
	}
	cout << "SUM: " << sum_money << endl;
}