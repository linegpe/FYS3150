import matplotlib.pyplot as plt 
from numpy import linspace

f = open("res2.txt","r")
lines = f.readlines()

u = []
f_exact = []
v = []
for line in lines:
	#i.append(line.split(' ')[0])
	u.append(line.split(' ')[1])
	f_exact.append(line.split(' ')[2])
	v.append(line.split(' ')[3])
f.close()
i = linspace(0,len(u),len(u))

print len(i)
print len(u)

plt.plot(i,u, label='General algorithm')
plt.plot(i,f_exact, label='Exact')
plt.plot(i,v, label='LU decomposition')
plt.legend()
plt.show()
