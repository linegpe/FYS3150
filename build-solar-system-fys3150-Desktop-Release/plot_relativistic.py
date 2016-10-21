import matplotlib.pyplot as plt 
import numpy as np 

nrPlanets = 2


print "Retreaving data from file one"
data = np.loadtxt("relativistic_update.dat")


sun = data[0::2*nrPlanets]
mercury = data[1::2*nrPlanets]
theta = []


print "Retreaving data from file two"
data2 = np.loadtxt("nonrel_update.dat")

sun2 = data2[0::nrPlanets]
mercury2 = data2[1::nrPlanets]
theta2 = []

N = len(mercury)
r = np.zeros(N)

print "First for-loop"
year_count = 0
for i in range(N):
	r[i] = np.sqrt((mercury[i,0])**2 + (mercury[i,1])**2)

print "Second for-loop"
for i in range(1,N-1):
	if r[i] < r[i-1] and r[i] < r[i+1]:
		year_count += 1
		theta.append(np.arctan2(mercury[i,1],mercury[i,0]))

x = np.linspace(0,year_count,year_count)

print len(x)
print len(theta)

plt.plot(x,theta,label="Non-relativistic")
plt.xlabel("X")
plt.ylabel("theta")


r2 = np.zeros(N)

print "Third for-loop"

year_count2 = 0
for i in range(N):
	r2[i] = np.sqrt((mercury2[i,0])**2 + (mercury2[i,1])**2)

print "Last fo-loop now! =D"
for i in range(1,N-1):
	if r2[i] < r2[i-1] and r2[i] < r2[i+1]:
		print i
		year_count2 += 1
		theta2.append(np.arctan2(mercury2[i,1],mercury2[i,0]))

print len(theta2)
x2 = np.linspace(0,year_count2,year_count2)


print "Plotting..."
#plt.figure(2)
plt.plot(x2,theta2,label="Relativistic")
plt.legend()
plt.show()