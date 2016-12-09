import numpy as np 
import matplotlib.pyplot as plt 
import scipy.special as sci

# Pareto's distribution:
N = 50
m_theoretical = np.linspace(2,8,N)
alpha = 1.2
income  = 10
distribution = np.zeros(N)
for i in range(N):
	distribution[i] = m_theoretical[i]**(-1-alpha)*20

x_money = np.linspace(2,8,N)



validation = np.loadtxt("validation.dat")
plt.hist(validation,bins=100, label="Distribution of money")


plt.plot(x_money,distribution,"--o",color="red",label="Theoretical distibution of income")
plt.xlabel("Wealth",fontsize=17)
plt.ylabel("Distribution",fontsize=17)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
plt.legend(fontsize=15)
#plt.axis([1,2,0,0.01])
plt.show()
#import sys; sys.exit("lol - line 27")
# Histogram distribution:
final_money = np.loadtxt("test.dat")
#final_money /= 50000

#import sys; sys.exit("lol - line 32")








plt.hist(final_money,bins = 100,label="Distibution of money")
plt.xlabel("Wealth",fontsize=17)
plt.ylabel("Distibution",fontsize=17)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
plt.legend(fontsize=15)
plt.show()

fm_counts, fm_edges = np.histogram(final_money,50,normed=True)
fm_bin_centers = (fm_edges[:-1] + fm_edges[:1])/2.0


plt.plot(np.log(fm_counts), label=r"$\log(\omega_m)$")
plt.xlabel("Wealth",fontsize=17)
plt.ylabel(r"$\log(\omega_m)$",fontsize=20)
plt.axis([0,35,-9,-4.5])
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
plt.legend(fontsize=20)
plt.show()



#import sys; sys.exit("lol - line 70")



varm0100 = np.loadtxt("variance_m0100.dat")
varm050 = np.loadtxt("variance_m050.dat")
varm010 = np.loadtxt("variance_m010.dat")
varm02 = np.loadtxt("variance_m02.dat")

m0100 = 100
m050 = 50
m010 = 10
m02 = 2
straightm0100 = np.zeros(len(varm0100))
straightm050 = np.zeros(len(varm050))
straightm010 = np.zeros(len(varm010))
straightm02 = np.zeros(len(varm02))

for i in range(0,len(varm0100)):
	straightm0100[i] = m0100**2

for i in range(0,len(varm050)):
	straightm050[i] = m050**2

for i in range(0,len(varm010)):
	straightm010[i] = m010**2

for i in range(0,len(varm02)):
	straightm02[i] = m02**2

cycles100 = np.linspace(0,len(varm0100),len(varm0100))
cycles50 = np.linspace(0,len(varm050),len(varm050))
cycles10 = np.linspace(0,len(varm010),len(varm010))
cycles2 = np.linspace(0,len(varm02),len(varm02))

plt.plot(cycles100,varm0100,label=r"$Variance$")
plt.plot(cycles100,straightm0100,"r--",linewidth=3,label=r"$m_0^2$")
plt.xlabel("Performed MC cycles", fontsize=24)
plt.ylabel("Variance", fontsize=24)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.legend(fontsize=24,loc="lower right")
plt.show()

plt.plot(cycles50,varm050,label=r"$Variance$")
plt.plot(cycles50,straightm050,"r--",linewidth=3,label=r"$m_0^2$")
plt.xlabel("Performed MC cycles", fontsize=24)
plt.ylabel("Variance", fontsize=24)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.legend(fontsize=24,loc="lower right")
plt.show()

plt.plot(cycles10,varm010,label=r"$Variance$")
plt.plot(cycles10,straightm010,"r--",linewidth=3,label=r"$m_0^2$")
plt.xlabel("Performed MC cycles", fontsize=24)
plt.ylabel("Variance", fontsize=24)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.legend(fontsize=24,loc="lower right")
plt.show()

plt.plot(cycles2,varm02,label=r"$Variance$")
plt.plot(cycles2,straightm02,"r--",linewidth=3,label=r"$m_0^2$")
plt.xlabel("Performed MC cycles", fontsize=24)
plt.ylabel("Variance", fontsize=24)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.legend(fontsize=24,loc="lower right")
plt.show()




counts,bin_edges = np.histogram(final_money,50,normed=True)
bin_centers = (bin_edges[:-1] + bin_edges[1:])/2.0

plt.plot(bin_centers,counts,"--",label=r"$\lambda=0.0$")
plt.show()

alpha0lambda025 = np.loadtxt("alpha0lambda025.dat")
alpha0lambda05 = np.loadtxt("alpha0lambda05.dat")
alpha0lambda09 = np.loadtxt("alpha0lambda09.dat")


a0l025_counts, a0l025_edges = np.histogram(alpha0lambda025,50,normed=True) #alpha0lambda025[::-1]
a0l025_bin_centers = (a0l025_edges[:-1] + a0l025_edges[1:])/2.0

a0l05_counts, a0l05_edges = np.histogram(alpha0lambda05,50,normed=True) #alpha0lambda025[::-1]
a0l05_bin_centers = (a0l05_edges[:-1] + a0l05_edges[1:])/2.0

a0l09_counts, a0l09_edges = np.histogram(alpha0lambda09,50,normed=True) #alpha0lambda025[::-1]
a0l09_bin_centers = (a0l09_edges[:-1] + a0l09_edges[1:])/2.0

print sci.gamma(2)

plt.show()

NN = 10
lillem2 = np.linspace(130,180,NN)
lambda1 = 0.9
X = np.zeros(NN)
for i in range(0,NN):
	X[i] = lillem2[i]/100
n = 1 + 3*lambda1/(1-lambda1)
an = np.zeros(NN)
pofn = np.zeros(NN)
for i in range(0,NN):
	an[i] = n**n/sci.gamma(X[i])
	pofn[i] = an[i] * X[i]**(n-1)*np.exp(-n*X[i])*1e-30



plt.plot(a0l09_bin_centers, a0l09_counts,'--',label=r"$\lambda=0.9$")
#plt.plot(bin_centers,counts,"--",label=r"$\lambda=0.0$")
plt.plot(lillem2,pofn,'ro',label=r"$Theoretical$")
plt.legend(fontsize=17)
plt.xlabel("Wealth",fontsize=17)
plt.ylabel("Distribution",fontsize=17)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
plt.show()


#plt.plot(a0l09_bin_centers, a0l09_counts,'--',label=r"$\lambda=0.9$")
#plt.show()
 #a0l05 = alpha0lambda05[::-1]
 #a0l09 = alpha0lambda09[::-1]

plt.plot(a0l025_bin_centers, a0l025_counts,'--',label=r"$\lambda=0.25$")
plt.plot(a0l05_bin_centers, a0l05_counts,'--',label=r"$\lambda=0.5$")
plt.plot(a0l09_bin_centers, a0l09_counts,'--',label=r"$\lambda=0.9$")
plt.legend()
plt.xlabel("Wealth",fontsize=15)
plt.ylabel("Distribution",fontsize=15)

plt.axis([0,300,0,0.025])

plt.show()

# N = 500

alpha05lambda0gamma0 = np.loadtxt("alpha05lambda0gamma0.dat")
alpha1lambda0gamma0 = np.loadtxt("alpha1lambda0gamma0.dat")
alpha15lambda0gamma0 = np.loadtxt("alpha15lambda0gamma0.dat")
alpha2lambda0gamma0 = np.loadtxt("alpha2lambda0gamma0.dat")
# plt.text(1,-4,"Gamma = 0.0",fontsize=15)
# plt.xlabel("Income [log(m)]",fontsize=15)
# plt.ylabel("Probability [log(P(m))]",fontsize=15)
# plt.show()

plt.hist(alpha05lambda0gamma0,50,normed=True)
#plt.show()
plt.hist(alpha2lambda0gamma0,50,normed=True)
#plt.show()

# New fre 16.12
alpha05lambda05gamma0 = np.loadtxt("alpha05lambda05gamma0.dat")
alpha1lambda05gamma0 = np.loadtxt("alpha1lambda05gamma0.dat")
alpha15lambda05gamma0 = np.loadtxt("alpha15lambda05gamma0.dat")
alpha2lambda05gamma0 = np.loadtxt("alpha2lambda05gamma0.dat")
# plt.text(1,-4,"Gamma = 0.5",fontsize=15)
# plt.xlabel("Income [log(m)]",fontsize=15)
# plt.ylabel("Probability [log(P(m))]",fontsize=15)
# plt.show()
#---

a05l0g0_counts, a05l0g0_edges = np.histogram(alpha05lambda0gamma0,50,normed=True) #alpha0lambda025[::-1]
a05l0g0_bin_centers = (a05l0g0_edges[:-1] + a05l0g0_edges[1:])/2.0

a1l0g0_counts, a1l0g0_edges = np.histogram(alpha1lambda0gamma0,50,normed=True) #alpha0lambda025[::-1]
a1l0g0_bin_centers = (a1l0g0_edges[:-1] + a1l0g0_edges[1:])/2.0

a15l0g0_counts, a15l0g0_edges = np.histogram(alpha15lambda0gamma0,50,normed=True) #alpha0lambda025[::-1]
a15l0g0_bin_centers = (a15l0g0_edges[:-1] + a15l0g0_edges[1:])/2.0

a2l0g0_counts, a2l0g0_edges = np.histogram(alpha2lambda0gamma0,50,normed=True) #alpha0lambda025[::-1]
a2l0g0_bin_centers = (a2l0g0_edges[:-1] + a2l0g0_edges[1:])/2.0

#New fre 16.14
a05l05g0_counts, a05l05g0_edges = np.histogram(alpha05lambda05gamma0,50,normed=True) #alpha0lambda025[::-1]
a05l05g0_bin_centers = (a05l05g0_edges[:-1] + a05l05g0_edges[1:])/2.0

a1l05g0_counts, a1l05g0_edges = np.histogram(alpha1lambda05gamma0,50,normed=True) #alpha0lambda025[::-1]
a1l05g0_bin_centers = (a1l05g0_edges[:-1] + a1l05g0_edges[1:])/2.0

a15l05g0_counts, a15l05g0_edges = np.histogram(alpha15lambda05gamma0,50,normed=True) #alpha0lambda025[::-1]
a15l05g0_bin_centers = (a15l05g0_edges[:-1] + a15l05g0_edges[1:])/2.0

a2l05g0_counts, a2l05g0_edges = np.histogram(alpha2lambda05gamma0,50,normed=True) #alpha0lambda025[::-1]
a2l05g0_bin_centers = (a2l05g0_edges[:-1] + a2l05g0_edges[1:])/2.0
#---

plt.plot(np.log(a05l0g0_bin_centers), np.log(a05l0g0_counts),'-',label=r"$\alpha=0.5$")
plt.plot(np.log(a1l0g0_bin_centers), np.log(a1l0g0_counts),'-',label=r"$\alpha=1.0$")
plt.plot(np.log(a15l0g0_bin_centers), np.log(a15l0g0_counts),'-',label=r"$\alpha=1.5$")
plt.plot(np.log(a2l0g0_bin_centers), np.log(a2l0g0_counts),'-',label=r"$\alpha=2.0$")
plt.legend(fontsize=17)
#plt.text(-2,-8,r"$\gamma = 0.0$",fontsize=17)
plt.xlabel("Wealth [log(m)]",fontsize=17)
plt.ylabel("Probability [log(P(m))]",fontsize=17)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
plt.show()

# Ny fre 16.19
plt.plot(np.log(a05l05g0_bin_centers), np.log(a05l05g0_counts),'-',label=r"$\alpha=0.5$")
plt.plot(np.log(a1l05g0_bin_centers), np.log(a1l05g0_counts),'-',label=r"$\alpha=1.0$")
plt.plot(np.log(a15l05g0_bin_centers), np.log(a15l05g0_counts),'-',label=r"$\alpha=1.5$")
plt.plot(np.log(a2l05g0_bin_centers), np.log(a2l05g0_counts),'-',label=r"$\alpha=2.0$")
plt.legend(fontsize=17)
#plt.text(0,-8,r"$\gamma = 0.5$",fontsize=17)
plt.xlabel("Wealth [log(m)]",fontsize=17)
plt.ylabel("Probability [log(P(m))]",fontsize=17)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
plt.show()

#plt.show()

#----


# N = 1000


alpha05lambda0gamma0N1000 = np.loadtxt("alpha05lambda0gamma0N1000.dat")
alpha1lambda0gamma0N1000 = np.loadtxt("alpha1lambda0gamma0N1000.dat")
alpha15lambda0gamma0N1000 = np.loadtxt("alpha15lambda0gamma0N1000.dat")
alpha2lambda0gamma0N1000 = np.loadtxt("alpha2lambda0gamma0N1000.dat")

alpha05lambda05gamma0N1000 = np.loadtxt("alpha05lambda05gamma0N1000.dat")
alpha1lambda05gamma0N1000 = np.loadtxt("alpha1lambda05gamma0N1000.dat")
alpha15lambda05gamma0N1000 = np.loadtxt("alpha15lambda05gamma0N1000.dat")
alpha2lambda05gamma0N1000 = np.loadtxt("alpha2lambda05gamma0N1000.dat")


a05l0g0N1000_counts, a05l0g0N1000_edges = np.histogram(alpha05lambda0gamma0N1000,50,normed=True) #alpha0lambda025[::-1]
a05l0g0N1000_bin_centers = (a05l0g0N1000_edges[:-1] + a05l0g0N1000_edges[1:])/2.0

a1l0g0N1000_counts, a1l0g0N1000_edges = np.histogram(alpha1lambda0gamma0N1000,50,normed=True) #alpha0lambda025[::-1]
a1l0g0N1000_bin_centers = (a1l0g0N1000_edges[:-1] + a1l0g0N1000_edges[1:])/2.0

a15l0g0N1000_counts, a15l0g0N1000_edges = np.histogram(alpha15lambda0gamma0N1000,50,normed=True) #alpha0lambda025[::-1]
a15l0g0N1000_bin_centers = (a15l0g0N1000_edges[:-1] + a15l0g0N1000_edges[1:])/2.0

a2l0g0N1000_counts, a2l0g0N1000_edges = np.histogram(alpha2lambda0gamma0N1000,50,normed=True) #alpha0lambda025[::-1]
a2l0g0N1000_bin_centers = (a2l0g0N1000_edges[:-1] + a2l0g0N1000_edges[1:])/2.0

a05l05g0N1000_counts, a05l05g0N1000_edges = np.histogram(alpha05lambda05gamma0N1000,50,normed=True) #alpha0lambda025[::-1]
a05l05g0N1000_bin_centers = (a05l05g0N1000_edges[:-1] + a05l05g0N1000_edges[1:])/2.0

a1l05g0N1000_counts, a1l05g0N1000_edges = np.histogram(alpha1lambda05gamma0N1000,50,normed=True) #alpha0lambda025[::-1]
a1l05g0N1000_bin_centers = (a1l05g0N1000_edges[:-1] + a1l05g0N1000_edges[1:])/2.0

a15l05g0N1000_counts, a15l05g0N1000_edges = np.histogram(alpha15lambda05gamma0N1000,50,normed=True) #alpha0lambda025[::-1]
a15l05g0N1000_bin_centers = (a15l05g0N1000_edges[:-1] + a15l05g0N1000_edges[1:])/2.0

a2l05g0N1000_counts, a2l05g0N1000_edges = np.histogram(alpha2lambda05gamma0N1000,50,normed=True) #alpha0lambda025[::-1]
a2l05g0N1000_bin_centers = (a2l05g0N1000_edges[:-1] + a2l05g0N1000_edges[1:])/2.0

plt.plot(np.log(a05l0g0N1000_bin_centers), np.log(a05l0g0N1000_counts),'-',label=r"$\alpha=0.5$")
plt.plot(np.log(a1l0g0N1000_bin_centers), np.log(a1l0g0N1000_counts),'-',label=r"$\alpha=1.0$")
plt.plot(np.log(a15l0g0N1000_bin_centers), np.log(a15l0g0N1000_counts),'-',label=r"$\alpha=1.5$")
plt.plot(np.log(a2l0g0N1000_bin_centers), np.log(a2l0g0N1000_counts),'-',label=r"$\alpha=2.0$")
plt.legend(fontsize=17)
#plt.text(0,-8,r"$\gamma = 0.0$",fontsize=17)
#plt.text(0,-8.5,r"$N = 1000$", fontsize=17)
plt.xlabel("Wealth [log(m)]",fontsize=17)
plt.ylabel("Probability [log(P(m))]",fontsize=17)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
plt.show()

plt.show()

N2 = 10
pofm = np.zeros(N2)
nr_agents = 1000.0
total_money = 500*100.0*3.2
T = total_money/nr_agents
lillem = np.linspace(500,800,N2)
for i in range(0,N2):
	pofm[i] = (1.0/T)*np.exp(-lillem[i]/T)

plt.plot(np.log(lillem), np.log(pofm),'ro',label=r"$Theoretical$")


plt.plot(np.log(a05l05g0N1000_bin_centers), np.log(a05l05g0N1000_counts),'-',label=r"$\alpha=0.5$")
plt.plot(np.log(a1l05g0N1000_bin_centers), np.log(a1l05g0N1000_counts),'-',label=r"$\alpha=1.0$")
plt.plot(np.log(a15l05g0N1000_bin_centers), np.log(a15l05g0N1000_counts),'-',label=r"$\alpha=1.5$")
plt.plot(np.log(a2l05g0N1000_bin_centers), np.log(a2l05g0N1000_counts),'-',label=r"$\alpha=2.0$")
plt.legend(fontsize=17)
#plt.text(0,-8,r"$\gamma = 0.5$",fontsize=17)
#plt.text(0,-8.5,r"$N = 1000$", fontsize=17)
plt.xlabel("Wealth [log(m)]",fontsize=17)
plt.ylabel("Probability [log(P(m))]",fontsize=17)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
plt.show()

plt.show()

import sys; sys.exit("LOL")





# N = 1000, alpha = 1, gamma = 0.0, 1.0, 2.0, 3.0, 4.0


#plt.show()

# lambda = 0
alpha1lambda0gamma0 = np.loadtxt("alpha1lambda0gamma0N1000.dat")
alpha1lambda0gamma1 = np.loadtxt("alpha1lambda0gamma1N1000.dat")
alpha1lambda0gamma2 = np.loadtxt("alpha1lambda0gamma2N1000.dat")
alpha1lambda0gamma3 = np.loadtxt("alpha1lambda0gamma3N1000.dat")
alpha1lambda0gamma4 = np.loadtxt("alpha1lambda0gamma4N1000.dat")

# lambda = 0.5
alpha1lambda05gamma0 = np.loadtxt("alpha1lambda05gamma0N1000.dat")
alpha1lambda05gamma1 = np.loadtxt("alpha1lambda05gamma1N1000.dat")
alpha1lambda05gamma2 = np.loadtxt("alpha1lambda05gamma2N1000.dat")
alpha1lambda05gamma3 = np.loadtxt("alpha1lambda05gamma3N1000.dat")
alpha1lambda05gamma4 = np.loadtxt("alpha1lambda05gamma4N1000.dat")

# N = 1000, alpha = 2, gamma = 0.0, 1.0, 2.0, 3.0, 4.0

#lamba = 0
alpha2lambda0gamma0 = np.loadtxt("alpha2lambda0gamma0N1000.dat")
alpha2lambda0gamma1 = np.loadtxt("alpha2lambda0gamma1N1000.dat")
alpha2lambda0gamma2 = np.loadtxt("alpha2lambda0gamma2N1000.dat")
alpha2lambda0gamma3 = np.loadtxt("alpha2lambda0gamma3N1000.dat")
alpha2lambda0gamma4 = np.loadtxt("alpha2lambda0gamma4N1000.dat")

#lamba = 0.5
alpha2lambda05gamma0 = np.loadtxt("alpha2lambda05gamma0N1000.dat")
alpha2lambda05gamma1 = np.loadtxt("alpha2lambda05gamma1N1000.dat")
alpha2lambda05gamma2 = np.loadtxt("alpha2lambda05gamma2N1000.dat")
alpha2lambda05gamma3 = np.loadtxt("alpha2lambda05gamma3N1000.dat")
alpha2lambda05gamma4 = np.loadtxt("alpha2lambda05gamma4N1000.dat")


# Plotting alpha = 1: 

a1l0g0_counts, a1l0g0_edges = np.histogram(alpha1lambda0gamma0,50,normed=True) #alpha0lambda025[::-1]
a1l0g0_bin_centers = (a1l0g0_edges[:-1] + a1l0g0_edges[1:])/2.0

a1l0g1_counts, a1l0g1_edges = np.histogram(alpha1lambda0gamma1,50,normed=True) #alpha0lambda025[::-1]
a1l0g1_bin_centers = (a1l0g1_edges[:-1] + a1l0g1_edges[1:])/2.0

a1l0g2_counts, a1l0g2_edges = np.histogram(alpha1lambda0gamma2,50,normed=True) #alpha0lambda025[::-1]
a1l0g2_bin_centers = (a1l0g2_edges[:-1] + a1l0g2_edges[1:])/2.0

a1l0g3_counts, a1l0g3_edges = np.histogram(alpha1lambda0gamma3,50,normed=True) #alpha0lambda025[::-1]
a1l0g3_bin_centers = (a1l0g3_edges[:-1] + a1l0g3_edges[1:])/2.0

a1l0g4_counts, a1l0g4_edges = np.histogram(alpha1lambda0gamma4,50,normed=True) #alpha0lambda025[::-1]
a1l0g4_bin_centers = (a1l0g4_edges[:-1] + a1l0g4_edges[1:])/2.0

# Plotting alpha = 2: 

a2l0g0_counts, a2l0g0_edges = np.histogram(alpha2lambda0gamma0,50,normed=True) #alpha0lambda025[::-1]
a2l0g0_bin_centers = (a2l0g0_edges[:-1] + a2l0g0_edges[1:])/2.0

a2l0g1_counts, a2l0g1_edges = np.histogram(alpha2lambda0gamma1,50,normed=True) #alpha0lambda025[::-1]
a2l0g1_bin_centers = (a2l0g1_edges[:-1] + a2l0g1_edges[1:])/2.0

a2l0g2_counts, a2l0g2_edges = np.histogram(alpha2lambda0gamma2,50,normed=True) #alpha0lambda025[::-1]
a2l0g2_bin_centers = (a2l0g2_edges[:-1] + a2l0g2_edges[1:])/2.0

a2l0g3_counts, a2l0g3_edges = np.histogram(alpha2lambda0gamma3,50,normed=True) #alpha0lambda025[::-1]
a2l0g3_bin_centers = (a2l0g3_edges[:-1] + a2l0g3_edges[1:])/2.0

a2l0g4_counts, a2l0g4_edges = np.histogram(alpha2lambda0gamma4,50,normed=True) #alpha0lambda025[::-1]
a2l0g4_bin_centers = (a2l0g4_edges[:-1] + a2l0g4_edges[1:])/2.0

plt.show()

N2 = 10
pofm = np.zeros(N2)
nr_agents = 1000.0
total_money = 500*100.0*10
T = total_money/nr_agents
lillem = np.linspace(500,900,N2)
for i in range(0,N2):
	pofm[i] = (1.0/T)*np.exp(-lillem[i]/T)

#plt.plot(np.log(lillem),np.log(pofm),"ro")

plt.plot(np.log(a1l0g0_bin_centers), np.log(a1l0g0_counts),'-',label=r"$\gamma=0$")
plt.plot(np.log(a1l0g1_bin_centers), np.log(a1l0g1_counts),'-',label=r"$\gamma=1$")
plt.plot(np.log(a1l0g2_bin_centers), np.log(a1l0g2_counts),'-',label=r"$\gamma=2$")
plt.plot(np.log(a1l0g3_bin_centers), np.log(a1l0g3_counts),'-',label=r"$\gamma=3$")
plt.plot(np.log(a1l0g4_bin_centers), np.log(a1l0g4_counts),'-',label=r"$\gamma=4$")
plt.plot(np.log(lillem),np.log(pofm),"ro",label=r"$Theoretical$")
plt.legend(fontsize=17)
plt.xlabel("Wealth [log(m)]",fontsize=17)
plt.ylabel("Probability [log(P(m))]",fontsize=17)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
plt.show()

#import sys; sys.exit("lol - line 430")

N2 = 10
pofm = np.zeros(N2)
nr_agents = 1000.0
total_money = 500*100.0*3.2
T = total_money/nr_agents
lillem = np.linspace(500,800,N2)
for i in range(0,N2):
	pofm[i] = (1.0/T)*np.exp(-lillem[i]/T)




plt.plot(np.log(a2l0g0_bin_centers), np.log(a2l0g0_counts),'-',label=r"$\gamma=0$")
plt.plot(np.log(a2l0g1_bin_centers), np.log(a2l0g1_counts),'-',label=r"$\gamma=1$")
plt.plot(np.log(a2l0g2_bin_centers), np.log(a2l0g2_counts),'-',label=r"$\gamma=2$")
plt.plot(np.log(a2l0g3_bin_centers), np.log(a2l0g3_counts),'-',label=r"$\gamma=3$")
plt.plot(np.log(a2l0g4_bin_centers), np.log(a2l0g4_counts),'-',label=r"$\gamma=4$")
plt.plot(np.log(lillem),np.log(pofm),"ro",label=r"$Theoretical$")
plt.legend(fontsize=17)
plt.xlabel("Wealth [log(m)]",fontsize=17)
plt.ylabel("Probability [log(P(m))]",fontsize=17)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
plt.show()

# Plotting alpha = 1: 
# LAMBDA = 0.5

a1l05g0_counts, a1l05g0_edges = np.histogram(alpha1lambda05gamma0,50,normed=True) #alpha0lambda025[::-1]
a1l05g0_bin_centers = (a1l05g0_edges[:-1] + a1l05g0_edges[1:])/2.0

a1l05g1_counts, a1l05g1_edges = np.histogram(alpha1lambda05gamma1,50,normed=True) #alpha0lambda025[::-1]
a1l05g1_bin_centers = (a1l05g1_edges[:-1] + a1l05g1_edges[1:])/2.0

a1l05g2_counts, a1l05g2_edges = np.histogram(alpha1lambda05gamma2,50,normed=True) #alpha0lambda025[::-1]
a1l05g2_bin_centers = (a1l05g2_edges[:-1] + a1l05g2_edges[1:])/2.0

a1l05g3_counts, a1l05g3_edges = np.histogram(alpha1lambda05gamma3,50,normed=True) #alpha0lambda025[::-1]
a1l05g3_bin_centers = (a1l05g3_edges[:-1] + a1l05g3_edges[1:])/2.0

a1l05g4_counts, a1l05g4_edges = np.histogram(alpha1lambda05gamma4,50,normed=True) #alpha0lambda025[::-1]
a1l05g4_bin_centers = (a1l05g4_edges[:-1] + a1l05g4_edges[1:])/2.0

# Plotting alpha = 2: 

a2l05g0_counts, a2l05g0_edges = np.histogram(alpha2lambda05gamma0,50,normed=True) #alpha0lambda025[::-1]
a2l05g0_bin_centers = (a2l05g0_edges[:-1] + a2l05g0_edges[1:])/2.0

a2l05g1_counts, a2l05g1_edges = np.histogram(alpha2lambda05gamma1,50,normed=True) #alpha0lambda025[::-1]
a2l05g1_bin_centers = (a2l05g1_edges[:-1] + a2l05g1_edges[1:])/2.0

a2l05g2_counts, a2l05g2_edges = np.histogram(alpha2lambda05gamma2,50,normed=True) #alpha0lambda025[::-1]
a2l05g2_bin_centers = (a2l05g2_edges[:-1] + a2l05g2_edges[1:])/2.0

a2l05g3_counts, a2l05g3_edges = np.histogram(alpha2lambda05gamma3,50,normed=True) #alpha0lambda025[::-1]
a2l05g3_bin_centers = (a2l05g3_edges[:-1] + a2l05g3_edges[1:])/2.0

a2l05g4_counts, a2l05g4_edges = np.histogram(alpha2lambda05gamma4,50,normed=True) #alpha0lambda025[::-1]
a2l05g4_bin_centers = (a2l05g4_edges[:-1] + a2l05g4_edges[1:])/2.0

N2 = 100
pofm = np.zeros(N2)
nr_agents = 1000.0
total_money = 500*100.0
T = total_money/nr_agents
lillem = np.linspace(200,300,N2)
for i in range(0,N2):
	pofm[i] = (1.0/T)*np.exp(-lillem[i]/T)

#plt.plot(np.log(lillem),np.log(pofm),"ro")

plt.plot(np.log(a1l05g0_bin_centers), np.log(a1l05g0_counts),'-',label=r"$\gamma=0$")
plt.plot(np.log(a1l05g1_bin_centers), np.log(a1l05g1_counts),'-',label=r"$\gamma=1$")
plt.plot(np.log(a1l05g2_bin_centers), np.log(a1l05g2_counts),'-',label=r"$\gamma=2$")
plt.plot(np.log(a1l05g3_bin_centers), np.log(a1l05g3_counts),'-',label=r"$\gamma=3$")
plt.plot(np.log(a1l05g4_bin_centers), np.log(a1l05g4_counts),'-',label=r"$\gamma=4$")
plt.legend(fontsize=17)
plt.xlabel("Wealth [log(m)]",fontsize=17)
plt.ylabel("Probability [log(P(m))]",fontsize=17)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
plt.show()

N2 = 100
pofm = np.zeros(N2)
nr_agents = 1000.0
total_money = 500*100.0
T = total_money/nr_agents
lillem = np.linspace(100,400,N2)
for i in range(0,N2):
	pofm[i] = (1.0/T)*np.exp(-lillem[i]/T)

#plt.plot(np.log(lillem),np.log(pofm),"ro")

plt.plot(np.log(a2l05g0_bin_centers), np.log(a2l05g0_counts),'-',label=r"$\gamma=0$")
plt.plot(np.log(a2l05g1_bin_centers), np.log(a2l05g1_counts),'-',label=r"$\gamma=1$")
plt.plot(np.log(a2l05g2_bin_centers), np.log(a2l05g2_counts),'-',label=r"$\gamma=2$")
plt.plot(np.log(a2l05g3_bin_centers), np.log(a2l05g3_counts),'-',label=r"$\gamma=3$")
plt.plot(np.log(a2l05g4_bin_centers), np.log(a2l05g4_counts),'-',label=r"$\gamma=4$")
plt.legend(fontsize=17)
plt.xlabel("Wealth [log(m)]",fontsize=17)
plt.ylabel("Probability [log(P(m))]",fontsize=17)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
plt.show()
