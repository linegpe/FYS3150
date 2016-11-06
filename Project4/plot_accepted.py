import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt("accepted_random_T1.dat")
data2 = np.loadtxt("accepted_ordered_T1.dat")
data3 = np.loadtxt("accepted_random_T2_4.dat")
data4 = np.loadtxt("accepted_ordered_T2_4.dat")

randomT1 = data1[0::1]
orederedT1 = data2[0::1]
randomT24 = data3[0::1]
orederedT24 = data4[0::1]

N = len(randomT1)
x = np.linspace(0,N,N)

plt.plot(x,randomT1,label="Random, T=1")
plt.plot(x,orederedT1,label="Ordered, T=1")
plt.ylabel("Total number of accepted configurations",fontsize=15)
plt.xlabel("Number of Monte Carlo cycles",fontsize=15)
plt.legend()
plt.axis([-10000,1e6,0,3000])
plt.show()

plt.plot(x,randomT24,label="Random, T=2.4")
plt.plot(x,orederedT24,label="Ordered, T=2.4")
plt.ylabel("Total number of accepted configurations",fontsize=15)
plt.xlabel("Number of Monte Carlo cycles",fontsize=15)
plt.legend()
#plt.axis([-10000,1e6,0,50000])
plt.show()