import matplotlib.pyplot as plt 
import numpy as np 

nrPlanets = 3

data = np.loadtxt("threebody.dat")

earth = data[0::3]
sun = data[1::3]
jupiter = data[2::3]


print earth[:,0]

plt.plot(earth[:,0],earth[:,1],label="Earth")
plt.plot(sun[:,0],sun[:,1],'yo',label="Sun")
plt.plot(jupiter[:,0],jupiter[:,1],label="Jupiter")
plt.legend(numpoints=1)
plt.xlabel("Position in x-direction [AU]",fontsize=15)
plt.ylabel("Position in y-direction [AU]",fontsize=15)
plt.axis("equal")
plt.show()


# LONG: N = 100 000 