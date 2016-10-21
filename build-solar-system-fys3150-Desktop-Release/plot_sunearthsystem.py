import matplotlib.pyplot as plt 
import numpy as np 

x_earth = []
y_earth = []

x_sun = []
y_sun = []

f = open("twobody.dat","r")
lines = f.readlines()

line_number = 1

for line in lines:
	if line_number % 2 == 0:
		x_sun.append(line.split(" ")[0])
		y_sun.append(line.split(" ")[1])
	else:
		x_earth.append(line.split(" ")[0])
		y_earth.append(line.split(" ")[1])

	line_number += 1
f.close()

N = len(x_earth)

plt.plot(x_earth,y_earth,label="Earth")
plt.plot(x_sun, y_sun,'o',label="Sun")
plt.legend()
#plt.axis([-1.1,1.1,-1.1,1.1])
plt.show()

