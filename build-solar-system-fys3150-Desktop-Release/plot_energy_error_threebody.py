import numpy as np
import matplotlib.pyplot as plt

Euler_EtotN = np.array([0.00517, 0.00517, 0.00517, 0.00520, 0.00543])
Euler_Etot0 = np.array([0.00518, 0.00518, 0.00518, 0.00515, 0.00521])

Verlet_EtotN = np.array([0.00517, 0.00517, 0.00517, 0.00517, 0.00514])
Verlet_Etot0 = np.array([0.00518, 0.00518, 0.00517, 0.00517, 0.00511])

x = np.linspace(-5,-1,5)
one = np.ones(5)

plt.plot(x,Euler_EtotN/Euler_Etot0,label="Euler")
plt.plot(x,Verlet_EtotN/Verlet_Etot0,label="Verlet")
plt.plot(x,one,"--")
plt.legend()
plt.xlabel(r"$\log_{10} (dt)$",fontsize=15)
plt.ylabel(r"$E_tot (N) / E_tot (0)$",fontsize=15)
plt.show()