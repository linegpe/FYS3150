import matplotlib.pyplot as plt 
from numpy import linspace
import sys


user_filename = raw_input("Please state filename of results: ")


f = open(user_filename,"r")
lines = f.readlines()

u = []
f_exact = []
v = []
epsilon = []
u2 = []
for line in lines:
	u.append(line.split(' ')[1])
	f_exact.append(line.split(' ')[2])
	v.append(line.split(' ')[3])
	epsilon.append(line.split(' ')[4])
	u2.append(line.split(' ')[5])
f.close()
i = linspace(0,1,len(u))


plt.plot(i,u,'r-', label='Gaussian',)
plt.plot(i,f_exact, 'k-', label='Exact', )
plt.legend()
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.legend()
plt.show()

plt.figure()
plt.plot(i,epsilon,'--')
plt.xlabel('$x$')
plt.ylabel('Relative error, logarithmic scale')
plt.xlim([-0.1,1.1])
plt.show()