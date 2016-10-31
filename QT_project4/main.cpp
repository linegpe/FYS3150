#include <iostream>
#include <cmath>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

using namespace std;

int main(){
    double temp = 1.0;
    int L = 2;
    int nr_spins = L*L;
    double nr_microstates = pow(2,nr_spins);
    double J = 1.0;

    // Spin matrix
    double **spins = new double*[L];
    for (int i = 0; i < L; i++){
        spins[i] = new double[L];
    }

    int N = 10; // Number of Monte Carlo cycles

    int total_spin = 0;

    srand (time(NULL));

    // Fill grid with spins
    for (int i = 0; i < L; i++){
        for (int j = 0; j < L; j++){
            spins[i][j] = rand() % 2;
        }
    }

    // Calculate energy
    double energy_i = 0;
    double mean_energy = 0;
    for (int i = 0; i < L; i++){
        for (int j = 0; j < L; j++){
            if (i == 0) {
                mean_energy += spins[i][j]*spins[L][j];
            }
            else if (j == 0) {
                mean_energy += spins[i][j]*spins[i][L];
            }
            cout << i << " " << j << endl;
            mean_energy += spins[i][j]*spins[i+1][j];
            mean_energy += spins[i][j]*spins[i][j+1];
        }
    }

    cout << mean_energy << endl;

    return 0;
}
