import numpy as np
import matplotlib.pyplot as plt

noint = []
omega01 = []
omega05 = []
omega1 = []
omega5 = []
noint1 = []
nonint0_01 = []


f = open("eigvecs.txt")
lines = f.readlines()
for line in lines:
	noint.append(line.split('   ')[0])
f.close()

f01 = open("eigvecs2_omega_0_01.txt","r")
lines = f01.readlines()
for line in lines:
	omega01.append(line.split('   ')[0])
f01.close()

f05 = open("eigvecs2_omega_0_05.txt","r")
lines = f05.readlines()
for line in lines:
	omega05.append(line.split('   ')[0])
f05.close()

f1 = open("eigvecs2_omega_1.txt","r")
lines = f1.readlines()
for line in lines:
	omega1.append(line.split('   ')[0])
f1.close()

f5 = open("eigvecs2_omega_5.txt","r")
lines = f5.readlines()
for line in lines:
	omega5.append(line.split('   ')[0])
f5.close()

fn1 = open("nonint_omega_1.txt","r")
lines = fn1.readlines()
for line in lines:
	noint1.append(line.split('   ')[0])
fn1.close()

fn0_01 = open("nonint_omega_0_01.txt","r")
lines = fn0_01.readlines()
for line in lines:
	nonint0_01.append(line.split('   ')[0])
fn0_01.close()

N = len(noint)
rho = np.linspace(0,40,N)

#plt.plot(rho,noint,label="No interaction")
plt.plot(rho,omega01,label=r"Interacting case, $\omega$ = 0.01")
plt.plot(rho,nonint0_01,label=r"Non-interacting, $\omega$ = 0.01")
#plt.plot(rho,noint1,label=r"Non-interacting, $\omega$ = 1")
#plt.plot(rho,omega05,label=r"$\omega$ = 0.5")
#plt.plot(rho,omega1,label=r"Interacting case, $\omega$ = 1")
#plt.plot(rho,omega5,label=r"$\omega$ = 5")
plt.xlabel(r"Distance $\rho$",fontsize=17)
plt.ylabel(r"$|\psi(\rho)|^2$",fontsize=15)
plt.legend()
plt.show()


