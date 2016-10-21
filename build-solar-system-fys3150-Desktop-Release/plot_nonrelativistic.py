import matplotlib.pyplot as plt 
import numpy as np 

nrPlanets = 2

data = np.loadtxt("nonrel.dat")

sun = data[0::nrPlanets]
mercury = data[1::nrPlanets]
theta = []

N = len(mercury)
r = np.zeros(N)

year_count = 0
for i in range(N):
	r[i] = np.sqrt((mercury[i,0])**2 + (mercury[i,1])**2)

for i in range(1,N-1):
	if r[i] < r[i-1] and r[i] < r[i+1]:
		year_count += 1
		theta.append(np.arctan2(mercury[i,1],mercury[i,0]))

print len(theta)

x = np.linspace(0,year_count,year_count)

print len(x)

plt.plot(x,theta)
plt.xlabel("X")
plt.ylabel("theta")

plt.show()