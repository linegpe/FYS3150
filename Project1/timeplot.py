from numpy import linspace
import matplotlib.pyplot as plt
#import plotly.plotly as py

N = linspace(1,3,3)
#general = [4*10**(-6), 10**(-5), 7.5*10**(-5)]
#special = [10**(-6), 8*10**(-6), 6.6*10**(-5)]
#LUdecom = [0.000286, 0.004641, 2.6906]

general = [6*10**(-5),
3.4*10**(-5),
7*10**(-5),
0.000143,
0.000378,
0.000756]

special = [9*10**(-6),
3.1*10**(-5),
9*10**(-5),
0.000133,
0.00034,
0.000689]

LUdecom = [
0.0049,
0.341752,
2.78691,
26.023,
437.288,
3400.77]

N = [100,
500,
1000,
2000,
5000,
10000]

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.plot(N,general,'--o', label='General algorithm')


#plt.plot(N,general,'--o', label='General algorithm')
ax1.plot(N,special,'--o', label='Special algorithm')
plt.xlabel('ln(N)')
plt.ylabel('Time [s]')
plt.legend()

ax2 = fig.add_subplot(212)
ax2.plot(N,LUdecom,'--o', label='LU decomposition')

plt.show()

#plt.figure()
#plt.plot(N,general, label='General algorithm')
#plt.plot(N,special, label='Special algorithm')
#plt.show()

#plt.tight_layout()
#fig = plt.gcf(())