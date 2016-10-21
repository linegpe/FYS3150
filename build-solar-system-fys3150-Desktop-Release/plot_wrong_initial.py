import matplotlib.pyplot as plt 
import numpy as np 

nrPlanets = 2

data = np.loadtxt("toolow.dat")

earth = data[0::nrPlanets]
sun = data[1::nrPlanets]

data2 = np.loadtxt("toohigh.dat")
earth2 = data2[0::nrPlanets]

#plt.plot(earth[:,0],earth[:,1],label="Too low velocity")
plt.plot(earth2[:,0],earth2[:,1],label="Earth")
plt.plot(sun[:,0],sun[:,1],'o',label="Sun")
#plt.plot(jupiter[:,0],jupiter[:,1],label="Jupiter")
plt.legend()
plt.xlabel("Position in x-direction [AU]",fontsize=15)
plt.ylabel("Position in y-direction [AU]",fontsize=15)
plt.axis([-7,1,-1,7])
plt.show()