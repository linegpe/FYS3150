import matplotlib.pyplot as plt 
from numpy import linspace

f = open("res2.txt","r")
lines = f.readlines()

u = []
f_exact = []
for line in lines:
	#i.append(line.split(' ')[0])
	u.append(line.split(' ')[1])
	f_exact.append(line.split(' ')[2])
f.close()
i = linspace(0,len(u),len(u))

print len(i)
print len(u)

plt.plot(i,u, label='U')
plt.plot(i,f_exact, label='Exact')
plt.legend()
plt.show()
