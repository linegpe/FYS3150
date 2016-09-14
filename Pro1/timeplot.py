from numpy import linspace
import matplotlib.pyplot as plt

N = linspace(1,3,3)
general = [4*10**(-6), 10**(-5), 7.5*10**(-5)]
special = [10**(-6), 8*10**(-6), 6.6*10**(-5)]
LUdecom = [0.000286, 0.004641, 2.6906]

plt.plot(N,general, label='General algorithm')
plt.plot(N,special, label='Special algorithm')
plt.plot(N,LUdecom, label='LU decomposition')
plt.xlabel('ln(N)')
plt.ylabel('Time [s]')
plt.legend()
plt.show()