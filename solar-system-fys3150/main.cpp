#include <iostream>
#include <cmath>
#include "examples.h"

int main(int, char**) {
    // Define constants
    double time = 1.0; 					// years
    double N = 1000; 					// Mesh points
    double h = time/N;              	// Step-size

    //double a_value = pow(velocity_x[0],2)/sqrt(x[0]*x[0] + y[0]*y[0]);

    Examples::twoBodyProblem();
    return 0;
}
