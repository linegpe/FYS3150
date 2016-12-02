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
final_money = np.loadtxt("final_money.dat")
plt.hist(final_money,bins = 100,label="Distibution of money")
plt.xlabel("Money",fontsize=17)
plt.ylabel("Number of agents",fontsize=17)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
plt.legend(fontsize=15)

plt.show()