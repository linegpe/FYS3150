import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt("threebody_euler.dat")
data2 = np.loadtxt("threebody_verlet.dat")

euler_earth    = data1[0::3]
euler_sun      = data1[1::3]
euler_jupiter  = data1[2::3]

verlet_earth   = data2[0::3]
verlet_sun     = data2[1::3]
verlet_jupiter = data2[2::3]

fig = plt.figure()
fig1 = fig.add_subplot(121)
fig1.plot(euler_earth[:,0],euler_earth[:,1],label="Earth")
fig1.plot(euler_sun[:,0], euler_sun[:,1],"yo",label="Sun")
fig1.plot(euler_jupiter[:,0],euler_jupiter[:,1],label="Jupiter")
plt.legend(numpoints=1)
plt.axis("equal")
plt.title("Forward Euler",fontsize=18)
plt.xlabel("Position in x direction [AU]",fontsize=18)
plt.ylabel("Position in y direction [AU]",fontsize=18)

fig2 = fig.add_subplot(122)
fig2.plot(verlet_earth[:,0],verlet_earth[:,1])
fig2.plot(verlet_sun[:,0],verlet_sun[:,1],"yo")
fig2.plot(verlet_jupiter[:,0],verlet_jupiter[:,1])
plt.axis("equal")
plt.xlabel("Position in x direction [AU]",fontsize=18)
plt.title("Velocity Verlet",fontsize=18)

plt.show()

# plt.plot(earth[:,0],earth[:,1],label="Earth")
# plt.plot(sun[:,0],sun[:,1],'o',label="Sun")
# plt.plot(jupiter[:,0],jupiter[:,1],label="Jupiter")
# plt.legend()
# plt.xlabel("Position in x-direction [AU]",fontsize=15)
# plt.ylabel("Position in y-direction [AU]",fontsize=15)
# plt.show()



# earth = data[0::3]
# sun = data[1::3]
# jupiter = data[2::3]