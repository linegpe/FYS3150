import numpy as np
import matplotlib.pyplot as plt

EtotN = np.array([0.01099, 0.11068, 1.35284, 11.02949])
Etot0 = np.array([0.01100, 0.10857, 1.10135, 13.09287])

x = np.linspace(1,4,4)
one = np.ones(4)

plt.plot(x,abs(EtotN-Etot0)/Etot0)
plt.plot(x,one,"--")
plt.legend()
plt.xlabel(r"$\log_{10} (N)$",fontsize=15)
plt.ylabel(r"$E_tot (N) / E_tot (0)$",fontsize=15)
plt.show()