#include <random>
#include <iostream>
#include <fstream>
#include <algorithm>

// How to run from terminal:
// g++ -std=c++11 main.cpp

using namespace std;

void sum_money(double* money,int nr_agents);
void WriteToFile(double* money, int nr_agents);
int** CreateTransactionsMatrix(int nr_agents);
double* PerformTransactions(int** transactions, double* money, int nr_agents, double lambda, double gamma, double alpha, int initial_money);
double* CreateMoneyArray(int nr_agents, int initial_money);

int main(int argc, char* argv[]){
//int main(){

	if (argc < 3){
		cerr << "Usage: " << argv[0] << " lambda" << " alpha" << " gamma" << endl;
	}

	int nr_agents = 1000; 

	double initial_money = 100;


	// double alpha = 0.5;
	// double lambda = 0.25;
	// double gamma = 0.0;

	double alpha = atof(argv[1]);
	double lambda = atof(argv[2]);
	double gamma = atof(argv[3]);

	int nr_simulations = 1e3; 	// Should be between 10^3 - 10^4

	int completed_simulations = 0; 

	double* final_money_distribution = CreateMoneyArray(nr_agents, initial_money);

	while (completed_simulations < nr_simulations){
		cout << "Simulation number " << completed_simulations << endl;

		int** transactions = CreateTransactionsMatrix(nr_agents);
		double* money = CreateMoneyArray(nr_agents, initial_money);
		//sum_money(money,nr_agents);
		cout << "Performing transactions... " << endl;
		double* new_money = PerformTransactions(transactions, money, nr_agents, lambda, gamma, alpha, initial_money);

		cout << "Summing all results... " << endl;
		for (int i = 0; i < nr_agents; i++){
			final_money_distribution[i] += new_money[i];
		}
		completed_simulations += 1; 
	}

	for (int i = 0; i < nr_agents; i++){
		final_money_distribution[i] /= nr_simulations;
	}


	WriteToFile(final_money_distribution,nr_agents);
}

double* PerformTransactions(int** transactions, double* money, int nr_agents, double lambda, double gamma, double alpha, int initial_money){
	// Metropolis algorithm for transactions
	//int nr_agents = 500;		// Should be 500
	int nr_transactions = 8*1e4; 	// Should be at least 10^7

	int completed_transactions = 0;	int completed_simulation = 0; 
	double probability; int i; int j; 
	
	// Random number generators:
	random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> intRNG(0, nr_agents-1);
    uniform_real_distribution<double> doubleRNG(0,1);
    ofstream myfile;
    //myfile.open("variance.dat");

		while (completed_transactions < nr_transactions){
			// Pick two random agents
			i = intRNG(gen);
			j = intRNG(gen);
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
					sum_money(money, nr_agents);
				}
			} 
			double var_sum = 0; 
			for (int i = 0; i < nr_agents; i++){
				var_sum += (money[i] - initial_money)*(money[i] - initial_money);
			}
			double variance_new = var_sum/nr_agents;
			//myfile << variance_new << endl;
			// //cout << var_sum << endl;
			// if (variance_new > initial_money*initial_money/2){
			// 	cout << i << endl;
			// 	cout << variance_old << "   " << variance_new << endl;
			// 	break;
			// }
			// if (completed_transactions > 2){
			// 	double variance_old = var_sum/nr_agents;
			// }
		}


		completed_simulation += 1; 
		sort(money, money + nr_agents);	
		//myfile.close();
		return money;
}

void WriteToFile(double* money, int nr_agents){
	ofstream myfile;
	myfile.open("alpha05lambda0gamma0N1000.dat");
	for (int i = 0; i < nr_agents; i++){
		myfile << money[i] << endl;
	}
	myfile.close();
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