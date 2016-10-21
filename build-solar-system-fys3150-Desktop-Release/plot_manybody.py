import matplotlib.pyplot as plt 
import numpy as np 

nrPlanets = 10

data = np.loadtxt("planetary.dat") #manybody.dat

sun = data[0::nrPlanets]
mercury = data[1::nrPlanets]
venus = data[2::nrPlanets]
earth = data[3::nrPlanets]
mars = data[4::nrPlanets]
jupiter = data[5::nrPlanets]
saturn = data[6::nrPlanets]
uranus = data[7::nrPlanets]
neptune = data[8::nrPlanets]
luna = data[9::nrPlanets]


plt.plot(sun[:,0],sun[:,1],'o',label="Sun")
plt.plot(mercury[:,0],mercury[:,1],label="Mercury")
plt.plot(venus[:,0],venus[:,1],label="Venus")
plt.plot(earth[:,0],earth[:,1],label="Earth")
plt.plot(mars[:,0],mars[:,1],label="Mars")
plt.plot(jupiter[:,0],jupiter[:,1],label="Jupiter")
plt.plot(saturn[:,0],saturn[:,1],label="Saturn")
plt.plot(uranus[:,0],uranus[:,1],label="Uranus")
plt.plot(neptune[:,0],neptune[:,1],label="Neptune")
# plt.plot(luna[:,0],luna[:,1],label="Luna")

plt.xlabel("Position in x-direction",fontsize=15)
plt.ylabel("Position in y-direction",fontsize=15)
plt.axis([-35,60,-35,35])

plt.legend()
plt.show()