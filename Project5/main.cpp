#include <random>
#include <iostream>
#include <fstream>

// How to run from terminal:
// g++ -std=c++11 main.cpp

using namespace std;

void sum_money(double* money,int nr_agents);
void WriteToFile(double* money, int nr_agents);
int** CreateTransactionsMatrix(int nr_agents);
void PerformTransactions(int** transactions, double* money, int nr_transactions, double lambda, double gamma, double alpha);
double* CreateMoneyArray(int nr_agents, int initial_money);

int main(){
	int nr_agents = 500;		// Should be 500
	int nr_transactions = 1e7; 	// Should be at least 10^7
	int nr_simulations = 1e3; 	// Should be between 10^3 - 10^4

	int total_money = 0;
	//int max_initial_money = 100;
	double initial_money = 100;
	double lambda = 0.25;
	double alpha = 1.0;
	double gamma = 1.0;

	// Random number generators:
	random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> intRNG(0, nr_agents-1);
    uniform_real_distribution<double> doubleRNG(0,1);

	// Make matrix with transactions
	int** transactions = CreateTransactionsMatrix(nr_agents);

	// Make array with money
	double* money = CreateMoneyArray(nr_agents, initial_money);
	// double* money = new double[nr_agents];

	// // Initial random distribution of money
	// for (int i = 0; i < nr_agents; i++){
	// 	money[i] = initial_money;
	// }

	sum_money(money,nr_agents);

	PerformTransactions(transactions, money, nr_transactions, lambda, gamma, alpha);
	// // Metropolis algorithm for transactions
	// int completed_transactions = 0;
	// double probability = 0; 
	// while (completed_transactions < nr_transactions){
	// 	// Pick two random agents
	// 	int i = intRNG(gen);
	// 	int j = intRNG(gen);
	// 	if (i != j){

	// 		int c_ij = transactions[i][j];

	// 		probability = pow(fabs(money[i] - money[j]),-alpha)*(pow(c_ij+1,gamma));
	// 		double test_number = doubleRNG(gen);

	// 		if (test_number < probability){

	//     		double epsilon = doubleRNG(gen);
	//     		double sum_ij = money[i]+money[j];
	// 			money[i] = lambda*money[i] + epsilon*(1.0-lambda)*sum_ij;
	// 			money[j] = lambda*money[j] + (1.0-epsilon)*(1.0-lambda)*sum_ij;
	// 			completed_transactions += 1;
	// 			transactions[i][j] += 1;
	// 		}
	// 	} 
	// }

	WriteToFile(money,nr_agents);
}

void PerformTransactions(int** transactions, double* money, int nr_transactions, double lambda, double gamma, double alpha){
	// Metropolis algorithm for transactions
	int completed_transactions = 0;
	double probability = 0; 
	while (completed_transactions < nr_transactions){
		// Pick two random agents
		int i = intRNG(gen);
		int j = intRNG(gen);
		if (i != j){

			int c_ij = transactions[i][j];

			probability = pow(fabs(money[i] - money[j]),-alpha)*(pow(c_ij+1,gamma));
			double test_number = doubleRNG(gen);

			if (test_number < probability){

	    		double epsilon = doubleRNG(gen);
	    		double sum_ij = money[i]+money[j];
				money[i] = lambda*money[i] + epsilon*(1.0-lambda)*sum_ij;
				money[j] = lambda*money[j] + (1.0-epsilon)*(1.0-lambda)*sum_ij;
				completed_transactions += 1;
				transactions[i][j] += 1;
			}
		} 
	}	
}

void WriteToFile(double* money, int nr_agents){
	ofstream myfile;
	myfile.open("final_money.dat");
	for (int i = 0; i < nr_agents; i++){
		myfile << money[i] << endl;
	}
}

void sum_money(double* money,int nr_agents){
	double sum_money = 0;
	for (int i = 0; i < nr_agents; i++){
		sum_money += money[i];
	}
	cout << "SUM: " << sum_money << endl;
}

double* CreateMoneyArray(int nr_agents, int initial_money){
	double* money = new double[nr_agents];
	for (int i = 0; i < nr_agents; i++){
		money[i] = initial_money;
	}	
	return money;
}

int** CreateTransactionsMatrix(int nr_agents){
	int** transactions = new int*[nr_agents];
	for (int i = 0; i < nr_agents; i++){
		transactions[i] = new int[nr_agents];
	}
	for (int i = 0; i < nr_agents; i++){
		for (int j = 0; j < nr_agents; j++){
			transactions[i][j] = 0; 
		}
	}	
	return transactions;
}