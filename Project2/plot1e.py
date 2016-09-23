import numpy as np 
import matplotlib.pyplot as plt 

r1 = []
r2 = []
r3 = []

f = open("eigvecs.txt","r")
lines = f.readlines()

for line in lines:
	r1.append(line.split('   ')[0])
	r2.append(line.split('   ')[1])
	r3.append(line.split('   ')[2])
f.close()

N = len(r1)
rho = np.linspace(0,5,N)
plt.show(block=False)
plt.plot(rho,r1,label='1st eigenvector')
plt.plot(rho,r2,label='2nd eigenvector')
plt.plot(rho,r3,label='3rd eigenvector')
plt.legend()
plt.xlabel('Distance $r$')
plt.ylabel('Probability $|R(r)|$')

show = raw_input("Show figure now? [y/n] ")
print type(show)
if show == "y":
	plt.show(block=False)

save = raw_input("Do you wish to save the figure? [y/n] ")
if save == "y":
	filename = raw_input("Filename (with .png, .jpg etc): ")
	plt.savefig(filename)
#plt.show()