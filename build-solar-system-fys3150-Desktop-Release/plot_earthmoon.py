import matplotlib.pyplot as plt 
import numpy as np 

nrPlanets = 3

data = np.loadtxt("earthmoon.dat")

sun = data[0::nrPlanets]
earth = data[1::nrPlanets]
luna = data[2::nrPlanets]

print sun 
print earth
print luna 

#plt.plot(sun[:,0],sun[:,1],'o',label="Sun")
#plt.plot(earth[:,0],earth[:,1],label="Earth")
#plt.plot(luna[:,0],luna[:,1],label="Luna")
plt.plot(luna[:,0]-earth[:,0],luna[:,1]-earth[:,1])
plt.xlabel("Distance, x-direction [AU]", fontsize=15)
plt.ylabel("Distance, y-direction [AU]", fontsize=15)
plt.legend()
plt.show()