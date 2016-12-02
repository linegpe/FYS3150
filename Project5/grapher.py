import numpy as np 
import matplotlib.pyplot as plt 

# Pareto's distribution:
N = 100
alpha = np.linspace(1,2,N)
income  = 10
distribution = np.zeros(N)
for i in range(N):
	distribution[i] = income**(-1-alpha[i])

print len(alpha)
print len(distribution)

plt.plot(alpha,distribution,label="Theoretical distibution of income")
plt.xlabel("Agents",fontsize=17)
plt.ylabel("Income",fontsize=17)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
plt.legend(fontsize=15)
plt.show()

# Histogram distribution:
final_money = np.loadtxt("test.dat")
#final_money /= 50000

plt.hist(final_money,bins = 100,label="Distibution of money")
plt.xlabel("Money",fontsize=17)
plt.ylabel("Number of agents",fontsize=17)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
plt.legend(fontsize=15)
plt.show()

counts,bin_edges = np.histogram(final_money,50,normed=True)
bin_centers = (bin_edges[:-1] + bin_edges[1:])/2.0

plt.plot(bin_centers,counts,"--",label="lambda=0.0")
#plt.show()

alpha0lambda025 = np.loadtxt("alpha0lambda025.dat")
alpha0lambda05 = np.loadtxt("alpha0lambda05.dat")
alpha0lambda09 = np.loadtxt("alpha0lambda09.dat")

a0l025_counts, a0l025_edges = np.histogram(alpha0lambda025,50,normed=True) #alpha0lambda025[::-1]
a0l025_bin_centers = (a0l025_edges[:-1] + a0l025_edges[:1])/2.0

a0l05_counts, a0l05_edges = np.histogram(alpha0lambda05,50,normed=True) #alpha0lambda025[::-1]
a0l05_bin_centers = (a0l05_edges[:-1] + a0l05_edges[:1])/2.0

a0l09_counts, a0l09_edges = np.histogram(alpha0lambda09,50,normed=True) #alpha0lambda025[::-1]
a0l09_bin_centers = (a0l09_edges[:-1] + a0l09_edges[:1])/2.0


 #a0l05 = alpha0lambda05[::-1]
 #a0l09 = alpha0lambda09[::-1]

plt.plot(a0l025_bin_centers, a0l025_counts,'--',label="lambda=0.25")
plt.plot(a0l05_bin_centers, a0l05_counts,'--',label="lambda=0.5")
plt.plot(a0l09_bin_centers, a0l09_counts,'--',label="lambda=0.9")
plt.legend()

plt.show()

# N = 500

alpha05lambda0gamma1 = np.loadtxt("alpha05lambda0gamma0.dat")
alpha1lambda0gamma0 = np.loadtxt("alpha1lambda0gamma0.dat")
alpha15lambda0gamma0 = np.loadtxt("alpha15lambda0gamma0.dat")
alpha2lambda0gamma0 = np.loadtxt("alpha2lambda0gamma0.dat")

# New fre 16.12
alpha05lambda05gamma0 = np.loadtxt("alpha05lambda05gamma0.dat")
alpha1lambda05gamma0 = np.loadtxt("alpha1lambda05gamma0.dat")
alpha15lambda05gamma0 = np.loadtxt("alpha15lambda05gamma0.dat")
alpha2lambda05gamma0 = np.loadtxt("alpha2lambda05gamma0.dat")
#---

a05l0g0_counts, a05l0g0_edges = np.histogram(alpha05lambda0gamma0,50,normed=True) #alpha0lambda025[::-1]
a05l0g0_bin_centers = (a05l0g0_edges[:-1] + a05l0g0_edges[:1])/2.0

a1l0g0_counts, a1l0g0_edges = np.histogram(alpha1lambda0gamma0,50,normed=True) #alpha0lambda025[::-1]
a1l0g0_bin_centers = (a1l0g0_edges[:-1] + a1l0g0_edges[:1])/2.0

a15l0g0_counts, a15l0g0_edges = np.histogram(alpha15lambda0gamma0,50,normed=True) #alpha0lambda025[::-1]
a15l0g0_bin_centers = (a15l0g0_edges[:-1] + a15l0g0_edges[:1])/2.0

a2l0g0_counts, a2l0g0_edges = np.histogram(alpha2lambda0gamma0,50,normed=True) #alpha0lambda025[::-1]
a2l0g0_bin_centers = (a2l0g0_edges[:-1] + a2l0g0_edges[:1])/2.0

#New fre 16.14
a05l05g0_counts, a05l05g0_edges = np.histogram(alpha05lambda05gamma0,50,normed=True) #alpha0lambda025[::-1]
a05l05g0_bin_centers = (a05l05g0_edges[:-1] + a05l05g0_edges[:1])/2.0

a1l05g0_counts, a1l05g0_edges = np.histogram(alpha1lambda05gamma0,50,normed=True) #alpha0lambda025[::-1]
a1l05g0_bin_centers = (a1l05g0_edges[:-1] + a1l05g0_edges[:1])/2.0

a15l05g0_counts, a15l05g0_edges = np.histogram(alpha15lambda05gamma0,50,normed=True) #alpha0lambda025[::-1]
a15l05g0_bin_centers = (a15l05g0_edges[:-1] + a15l05g0_edges[:1])/2.0

a2l05g0_counts, a2l05g0_edges = np.histogram(alpha2lambda05gamma0,50,normed=True) #alpha0lambda025[::-1]
a2l05g0_bin_centers = (a2l05g0_edges[:-1] + a2l05g0_edges[:1])/2.0
#---

plt.plot(np.log(a05l0g0_bin_centers), np.log(a05l0g0_counts),'-',label="alpha=0.5")
plt.plot(np.log(a1l0g0_bin_centers), np.log(a1l0g0_counts),'-',label="alpha=1.0")
plt.plot(np.log(a15l0g0_bin_centers), np.log(a15l0g0_counts),'-',label="alpha=1.5")
plt.plot(np.log(a2l0g0_bin_centers), np.log(a2l0g0_counts),'-',label="alpha=2.0")
plt.legend()

plt.show()


# Ny fre 16.19
plt.plot(np.log(a05l05g0_bin_centers), np.log(a05l05g0_counts),'-',label="alpha=0.5")
plt.plot(np.log(a1l05g0_bin_centers), np.log(a1l05g0_counts),'-',label="alpha=1.0")
plt.plot(np.log(a15l05g0_bin_centers), np.log(a15l05g0_counts),'-',label="alpha=1.5")
plt.plot(np.log(a2l05g0_bin_centers), np.log(a2l05g0_counts),'-',label="alpha=2.0")
plt.legend()

plt.show()

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
a05l0g0N1000_bin_centers = (a05l0g0N1000_edges[:-1] + a05l0g0N1000_edges[:1])/2.0

a1l0g0N1000_counts, a1l0g0N1000_edges = np.histogram(alpha1lambda0gamma0N1000,50,normed=True) #alpha0lambda025[::-1]
a1l0g0N1000_bin_centers = (a1l0g0N1000_edges[:-1] + a1l0g0N1000_edges[:1])/2.0

a15l0g0N1000_counts, a15l0g0N1000_edges = np.histogram(alpha15lambda0gamma0N1000,50,normed=True) #alpha0lambda025[::-1]
a15l0g0N1000_bin_centers = (a15l0g0N1000_edges[:-1] + a15l0g0N1000_edges[:1])/2.0

a2l0g0N1000_counts, a2l0g0N1000_edges = np.histogram(alpha2lambda0gamma0N1000,50,normed=True) #alpha0lambda025[::-1]
a2l0g0N1000_bin_centers = (a2l0g0N1000_edges[:-1] + a2l0g0N1000_edges[:1])/2.0

a05l05g0N1000_counts, a05l05g0N1000_edges = np.histogram(alpha05lambda05gamma0N1000,50,normed=True) #alpha0lambda025[::-1]
a05l05g0N1000_bin_centers = (a05l05g0N1000_edges[:-1] + a05l05g0N1000_edges[:1])/2.0

a1l05g0N1000_counts, a1l05g0N1000_edges = np.histogram(alpha1lambda05gamma0N1000,50,normed=True) #alpha0lambda025[::-1]
a1l05g0N1000_bin_centers = (a1l05g0N1000_edges[:-1] + a1l05g0N1000_edges[:1])/2.0

a15l05g0N1000_counts, a15l05g0N1000_edges = np.histogram(alpha15lambda05gamma0N1000,50,normed=True) #alpha0lambda025[::-1]
a15l05g0N1000_bin_centers = (a15l05g0N1000_edges[:-1] + a15l05g0N1000_edges[:1])/2.0

a2l05g0N1000_counts, a2l05g0N1000_edges = np.histogram(alpha2lambda05gamma0N1000,50,normed=True) #alpha0lambda025[::-1]
a2l05g0N1000_bin_centers = (a2l05g0N1000_edges[:-1] + a2l05g0N1000_edges[:1])/2.0

plt.plot(np.log(a05l0g0N1000_bin_centers), np.log(a05l0g0N1000_counts),'-',label="alpha=0.5")
plt.plot(np.log(a1l0g0N1000_bin_centers), np.log(a1l0g0N1000_counts),'-',label="alpha=1.0")
plt.plot(np.log(a15l0g0N1000_bin_centers), np.log(a15l0g0N1000_counts),'-',label="alpha=1.5")
plt.plot(np.log(a2l0g0N1000_bin_centers), np.log(a2l0g0N1000_counts),'-',label="alpha=2.0")
plt.legend()

plt.show()


plt.plot(np.log(a05l05g0N1000_bin_centers), np.log(a05l05g0N1000_counts),'-',label="alpha=0.5")
plt.plot(np.log(a1l05g0N1000_bin_centers), np.log(a1l05g0N1000_counts),'-',label="alpha=1.0")
plt.plot(np.log(a15l05g0N1000_bin_centers), np.log(a15l05g0N1000_counts),'-',label="alpha=1.5")
plt.plot(np.log(a2l05g0N1000_bin_centers), np.log(a2l05g0N1000_counts),'-',label="alpha=2.0")
plt.legend()

plt.show()




# N = 1000, alpha = 1, gamma = 0.0, 1.0, 2.0, 3.0, 4.0

# lambda = 0
alpha1lambda0gamma0 = np.loadtxt("alpha1lambda0gamma0.dat")
alpha1lambda0gamma1 = np.loadtxt("alpha1lambda0gamma1.dat")
alpha1lambda0gamma2 = np.loadtxt("alpha1lambda0gamma2.dat")
alpha1lambda0gamma3 = np.loadtxt("alpha1lambda0gamma3.dat")
alpha1lambda0gamma4 = np.loadtxt("alpha1lambda0gamma4.dat")

# lambda = 0.5
alpha1lambda0gamma0 = np.loadtxt("alpha1lambda0gamma0.dat")
alpha1lambda0gamma1 = np.loadtxt("alpha1lambda0gamma1.dat")
alpha1lambda0gamma2 = np.loadtxt("alpha1lambda0gamma2.dat")
alpha1lambda0gamma3 = np.loadtxt("alpha1lambda0gamma3.dat")
alpha1lambda0gamma4 = np.loadtxt("alpha1lambda0gamma4.dat")

# N = 1000, alpha = 2, gamma = 0.0, 1.0, 2.0, 3.0, 4.0

#lamba = 0
alpha2lambda0gamma0 = np.loadtxt("alpha2lambda0gamma0.dat")
alpha2lambda0gamma1 = np.loadtxt("alpha2lambda0gamma1.dat")
alpha2lambda0gamma2 = np.loadtxt("alpha2lambda0gamma2.dat")
alpha2lambda0gamma3 = np.loadtxt("alpha2lambda0gamma3.dat")
alpha2lambda0gamma4 = np.loadtxt("alpha2lambda0gamma4.dat")

#lamba = 0.5
alpha2lambda0gamma0 = np.loadtxt("alpha2lambda0gamma0.dat")
alpha2lambda0gamma1 = np.loadtxt("alpha2lambda0gamma1.dat")
alpha2lambda0gamma2 = np.loadtxt("alpha2lambda0gamma2.dat")
alpha2lambda0gamma3 = np.loadtxt("alpha2lambda0gamma3.dat")
alpha2lambda0gamma4 = np.loadtxt("alpha2lambda0gamma4.dat")


# Plotting alpha = 1: 

a1l0g0_counts, a1l0g0_edges = np.histogram(alpha1lambda0gamma0,50,normed=True) #alpha0lambda025[::-1]
a1l0g0_bin_centers = (a1l0g0_edges[:-1] + a1l0g0_edges[:1])/2.0

a1l0g1_counts, a1l0g1_edges = np.histogram(alpha1lambda0gamma1,50,normed=True) #alpha0lambda025[::-1]
a1l0g1_bin_centers = (a1l0g1_edges[:-1] + a1l0g1_edges[:1])/2.0

a1l0g2_counts, a1l0g2_edges = np.histogram(alpha1lambda0gamma2,50,normed=True) #alpha0lambda025[::-1]
a1l0g2_bin_centers = (a1l0g2_edges[:-1] + a1l0g2_edges[:1])/2.0

a1l0g3_counts, a1l0g3_edges = np.histogram(alpha1lambda0gamma3,50,normed=True) #alpha0lambda025[::-1]
a1l0g3_bin_centers = (a1l0g3_edges[:-1] + a1l0g3_edges[:1])/2.0

a1l0g4_counts, a1l0g4_edges = np.histogram(alpha1lambda0gamma4,50,normed=True) #alpha0lambda025[::-1]
a1l0g4_bin_centers = (a1l0g4_edges[:-1] + a1l0g4_edges[:1])/2.0

# Plotting alpha = 2: 

a2l0g0_counts, a2l0g0_edges = np.histogram(alpha2lambda0gamma0,50,normed=True) #alpha0lambda025[::-1]
a2l0g0_bin_centers = (a2l0g0_edges[:-1] + a2l0g0_edges[:1])/2.0

a2l0g1_counts, a2l0g1_edges = np.histogram(alpha2lambda0gamma1,50,normed=True) #alpha0lambda025[::-1]
a2l0g1_bin_centers = (a2l0g1_edges[:-1] + a2l0g1_edges[:1])/2.0

a2l0g2_counts, a2l0g2_edges = np.histogram(alpha2lambda0gamma2,50,normed=True) #alpha0lambda025[::-1]
a2l0g2_bin_centers = (a2l0g2_edges[:-1] + a2l0g2_edges[:1])/2.0

a2l0g3_counts, a2l0g3_edges = np.histogram(alpha2lambda0gamma3,50,normed=True) #alpha0lambda025[::-1]
a2l0g3_bin_centers = (a2l0g3_edges[:-1] + a2l0g3_edges[:1])/2.0

a2l0g4_counts, a2l0g4_edges = np.histogram(alpha2lambda0gamma4,50,normed=True) #alpha0lambda025[::-1]
a2l0g4_bin_centers = (a2l0g4_edges[:-1] + a2l0g4_edges[:1])/2.0


