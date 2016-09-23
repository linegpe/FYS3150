# Plotting the result from warmup1.cpp found in warmupresults.txt
import matplotlib.pyplot as plt 
from math import log

f = open("warmupresults.txt","r")
lines = f.readlines()
h = []
eps = []

for line in lines:
	h.append(line.split(' ')[0])
	eps.append(line.split(' ')[1])

f.close

plt.plot(h,eps)
plt.xlabel('log(steplength)')
plt.ylabel('log(error)')
plt.show()