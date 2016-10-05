#include <iostream>
#include <cmath>
#include "eulercromer.h"
#include "../system.h"

EulerCromer::EulerCromer(System* system)
    : Integrator(system) {
}

void EulerCromer::integrateOneStep(std::vector<Particle*> particles) {
//void EulerCromer__integrateOneStep(std::vector<Earth*> particles){
    m_system->computeForces();
    for (int i=0; i<particles.size(); i++) {
        //std::cout << particles.size() << std::endl;
        Particle *p = particles.at(i);
//        vec3 v = p->getVelocity();
//        vec3 P = p->getPosition();
        vec3 F = p->getForce();
//        vec3 v = p->getVelocity();
        //std::cout << p->getPosition() << " particle p wha?" << std::endl;



        /*
         * This is where you need to update the positions and the velocities
         * and the velocities of each particle according to the Euler-Cromer
         * scheme.
         *
         * You can access the position of particle number i by
         *
         *      p->getPosition()
         *
         * Remember that the positions and velocities of all the particles are
         * vec3 vectors, which you can use the +=, -=, etc. operators on.
         */


        // Forward-Euler:


        //vec3 a = vec3 (dFx/m, dFy/m, dFz/m);
        p->getVelocity() += (vec3(m_dt*F(0)/p->getMass(),m_dt*F(1)/p->getMass(),0));
        p->getPosition() += m_dt*p->getVelocity();

    }
}

std::string EulerCromer::getName() {
    return "Euler-Cromer";
}
