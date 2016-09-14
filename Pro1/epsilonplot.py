from numpy import linspace
import matplotlib.pyplot as plt

epsilon = [-2.23297, -7.06964, -11.6932, -16.3003, -20.7334, -15.5917, -13.7288]
N = linspace(1,7,7)

plt.plot(N,epsilon)
plt.xlabel('ln(N)')
plt.ylabel('Error estimate $\epsilon$')
plt.show()