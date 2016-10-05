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
        std::cout << particles.size() << std::endl;
        Particle *p = particles.at(i);
        vec3 v = p->getVelocity();
        p->getPosition();
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


        // Euler-Cromer: (Forward-Euler)

        //a(i) =
        //x(i+1) = x(i) + h*v(i);
        //v(i+1) = v(i) + h*a(i);
        double dFx = 1.0;
        double dFy = 1.0;
        double dFz = 1.0;
        double dt = pow(10,-3);
//        Earth->addForce(dFx, dFy, dFz);
        //int N = 100;
        //particles.at(i)->addForce();
        vec3 a = p->addForce(dFx,dFy,dFz);
        p(i+1) = p(i) + v(i)*dt;
        v(i+1) = v(i) + a(i)*dt;


    }
}

std::string EulerCromer::getName() {
    return "Euler-Cromer";
}
