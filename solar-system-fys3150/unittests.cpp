//#ifdef CATCH_CONFIG_MAIN

#include "unittests.h"
#include "catch.hpp"
#include "vec3.h"
#include "InitialConditions/twobody.h"
#include "Integrators/eulercromer.h"
#include "system.h"
#include "Integrators/velocityverlet.h"
#include "system.h"
#include "math.h"
#include <iostream>

using namespace std;
double norm(double*vec, int n);


unittests::unittests()
{}

TEST_CASE("Preservation of total energy"){
    System* solarSystem = new System;
    Particle* test__object =     new Particle(vec3(1,0,0), vec3(0,2*M_PI,0), 1E-4);
    Particle* large_object =     new Particle(vec3(0,0,0), vec3(0,0,0),      1.0);
    double dt = 0.0001;
    solarSystem->setIntegrator(new VelocityVerlet(solarSystem));
    int numTimesteps = 1000;
    double* kin_e = new double[1000];
    double* pot_e = new double[1000];
    for (int timestep = 0; timestep<numTimesteps; timestep++){
         solarSystem->integrate(1);
         kin_e[timestep] = solarSystem->computeKineticEnergy();
         //kin_e[timestep] = solarSystem.kineticEnergy();
         pot_e[timestep] = solarSystem->computeKineticEnergy();
         //pot_e[timestep] = solarSystem.kineticEnergy();
    }
    REQUIRE(abs(abs(kin_e[0] + pot_e[0]) - abs(kin_e[1000] + pot_e[1000])) < 0.001);
}



//#endif
