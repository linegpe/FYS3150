# This program plots the time used by the different algorithms

from numpy import linspace, log10
import matplotlib.pyplot as plt



# Lists that holds the time used by different methods
general = [6*10**(-5), 3.4*10**(-5), 7*10**(-5), 0.000143, 0.000378, 0.000756]
special = [9*10**(-6), 3.1*10**(-5), 9*10**(-5), 0.000133, 0.00034, 0.000689]
LUdecom = [ 0.0049, 0.341752, 2.78691, 26.023, 437.288, 3400.77]

# N-values the methods are tested for. 
N = [100, 500, 1000, 2000, 5000, 10000]

# Ploting 
fig = plt.figure()


ax1 = fig.add_subplot(211)
ax1.plot(N,general,'--o', label='General algorithm')
ax1.plot(N,special,'--o', label='Special algorithm')
plt.xlabel('N')
plt.ylabel('Time [s]')
plt.legend(loc = 'upper left')
axes1 = plt.gca()
axes1.set_xlim([0,N[-1]+100])
axes1.set_ylim([0,1.5*max(special)])
axes1.grid('on')

ax2 = fig.add_subplot(212)
ax2.plot(N,LUdecom,'r--o', label='LU decomposition')
plt.xlabel('N')
plt.ylabel('Time [s]')
plt.legend(loc = 'upper left')
axes2 = plt.gca()
axes2.set_xlim([0,N[-1]+100])
axes2.set_ylim([-100, max(LUdecom)+100])
axes2.grid('on')

plt.show()

