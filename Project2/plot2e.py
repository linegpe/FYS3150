import numpy as np 
import matplotlib.pyplot as plt 

r1 = []
r2 = []
r3 = []

f = open("eigvecs2.txt","r")
lines = f.readlines()

for line in lines:
	r1.append(line.split('   ')[0])
	r2.append(line.split('   ')[1])
	r3.append(line.split('   ')[2])
f.close()

N = len(r1)
rho = np.linspace(0,5,N)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig = plt.figure()

fig1 = fig.add_subplot(311)
fig1.plot(rho,r1,label='1st eigenvector', color='indigo')
plt.legend()

fig2 = fig.add_subplot(312)
fig2.plot(rho,r2,label='2nd eigenvector', color='fuchsia')
plt.legend()
plt.ylabel('Probability $|R(r)|$', fontsize=15)

fig3 = fig.add_subplot(313)
fig3.plot(rho,r3,label='3rd eigenvector', color='violet')
plt.legend()
plt.xlabel('Distance $ \\rho $', fontsize=15)


show = raw_input("Show figure now? [y/n] ")
if show == "y":
	plt.show(block=False)

save = raw_input("Do you wish to save the figure? [y/n] ")
if save == "y":
	filename = raw_input("Filename (with .png, .jpg etc): ")
	plt.savefig(filename)

plt.show()