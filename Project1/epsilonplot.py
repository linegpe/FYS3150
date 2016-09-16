# This program plots the value of the relaive error against 
# the corresponding N-values

from numpy import linspace, log10
import matplotlib.pyplot as plt


epsilon = [-2.33482, - 7.06964,  -11.6933, -16.3003, -20.7334, -15.5917]
N = [10, 100, 1000, 10000, 100000, 1000000]

plt.plot(log10(N),epsilon, 'o--')
plt.xlabel('log(N)')
plt.ylabel('Error estimate $\epsilon$')


plt.show()