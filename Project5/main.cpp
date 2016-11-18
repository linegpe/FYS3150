#include <random>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// How to run from terminal:
// g++ -std=c++11 main.cpp

using namespace std;

int main(){
	int nr_agents = 500;
	int nr_transactions = 1e3; 	// Should be at least 10^7
	int nr_simulations = 100; 	// Should be between 10^3 - 10^4

	int total_money = 0;
	int max_initial_money = 100;

	// Make array with agents
	double* agents = new double[nr_agents];
	for (int i = 0; i < nr_agents; i++){
		agents[i] = i;
	}

	// Make array with money
	double* money = new double[nr_agents];

	// Initial random distribution of money

	//random_device epsilon();
	//mt19937 gen(epsilon());
	//uniform_int_distribution<> dis(0,nr_agents);
	
	for (int i = 0; i < total_money; i++){
		money[i] = rand() % max_initial_money;
		total_money += money[i];
	}

	// Metropolis algorithm for transactions
	int completed_transactions = 0;
	while (completed_transactions < nr_transactions){
		// Pick two random agents
		int i = rand() % nr_agents;
		int j = rand() % nr_agents;
		// Make sure i =/= j
		while (i == j){
			j = rand() % nr_agents;
		}
		double max = RAND_MAX;
		double epsilon = rand() / ((double) max);
		int new_money_i = epsilon*(money[i] + money[j]);
		int new_money_j = (1-epsilon)*(money[i] + money[j]);
		completed_transactions += 1;
	}
}