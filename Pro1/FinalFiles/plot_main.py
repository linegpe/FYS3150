import matplotlib.pyplot as plt 
from numpy import linspace

f = open("res2.txt","r")
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

print epsilon[1]

plt.plot(i,u, label='General algorithm')
plt.plot(i,f_exact, label='Exact')
plt.plot(i,v, label='LU decomposition')
plt.plot(i,u2, label='Special case algorithm')
plt.legend()
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.show()

plt.figure()
plt.plot(i,epsilon,'--')
plt.xlabel('$x$')
plt.ylabel('Relative error, logarithmic scale')
plt.show()