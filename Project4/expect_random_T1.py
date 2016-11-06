import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt("expect_random_T1.00.dat")
data2 = np.loadtxt("expect_ordered_T1.00.dat")
data3 = np.loadtxt("expect_random_T2.40.dat")
data4 = np.loadtxt("expect_ordered_T2.40.dat")
values1 = data1[0::1]
values2 = data2[0::1]
values3 = data3[0::1]
values4 = data4[0::1]

N1 = len(values1)
x1 = np.linspace(0,N1,N1)

N2 = len(values3)
x2 = np.linspace(0,N2,N2)

figure1 = plt.figure()

labels = figure1.add_subplot(111)

# Turn off axis lines and ticks of the big subplot
labels.spines['top'].set_color('none')
labels.spines['bottom'].set_color('none')
labels.spines['left'].set_color('none')
labels.spines['right'].set_color('none')
labels.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

plt.xlabel("Number of Monte Carlo cycles",fontsize=15)
plt.ylabel("Mean energy per spin",fontsize=15)

#figure1.yaxis.set_ticks_position(right)

#figure1.ylabel.set_ticks_position('left')

#figure1.yaxis.tick_right()

fig1 = figure1.add_subplot(211)

fig1.plot(x1,values1[:,0],label="Random initial spins, T=1")
fig1.plot(x1,values2[:,0],label="Ordered initial spins, T=1")
fig1.tick_params(axis='x', labelsize=15) #HOW TO PUT THIS ON THE RIGHT SIDE?
fig1.tick_params(axis='y', labelsize=15)
#plt.ylabel(r"$\langle E\rangle /L^2$",fontsize=17)
#plt.xlabel("Number of Monte Carlo cycles",fontsize=15)
plt.legend()
plt.axis([0,N1,-3,0])
#plt.show()




fig2 = figure1.add_subplot(212)
fig2.plot(x2,values3[:,0],label="Random initial spins, T=2.4")
fig2.plot(x2,values4[:,0],label="Ordered initial spins, T=2.4")
fig2.tick_params(axis='x', labelsize=15)
fig2.tick_params(axis='y', labelsize=15)
#plt.ylabel(r"$\langle E\rangle /L^2$",fontsize=15)
#plt.xlabel("Number of Monte Carlo cycles",fontsize=15)
plt.legend()
#plt.axis([0,8e6,-2.5,-0.5])
plt.show()



figure2 = plt.figure()



labels = figure2.add_subplot(111)
labels.spines['top'].set_color('none')
labels.spines['bottom'].set_color('none')
labels.spines['left'].set_color('none')
labels.spines['right'].set_color('none')
labels.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

plt.xlabel("Number of Monte Carlo cycles",fontsize=15)
plt.ylabel("Mean energy per spin",fontsize=15)


fig1 = figure2.add_subplot(211)
fig1.plot(x1,values1[:,1],label="Random initial spins, T=1")
fig1.plot(x1,values2[:,1],label="Ordered initial spins, T=1")
fig1.tick_params(axis='x', labelsize=15)
fig1.tick_params(axis='y', labelsize=15)
#fig2.ylabel(r"$abs(\langle M \rangle /L^2)$",fontsize=15)
#fig2.xlabel("Number of Monte Carlo cycles",fontsize=15)
plt.legend()
plt.axis([0,N1,0.2,1.6])
#plt.show()

fig2 = figure2.add_subplot(212)
fig2.plot(x2,values3[:,1],label="Random initial spins, T=2.4")
fig2.plot(x2,values4[:,1],label="Ordered initial spins, T=2.4")
fig2.tick_params(axis='x', labelsize=15)
fig2.tick_params(axis='y', labelsize=15)
#plt.ylabel(r"$abs(\langle M\rangle / L^2)$",fontsize=15)
#plt.xlabel("Number of Monte Carlo cycles",fontsize=15)
plt.legend()
#plt.axis([0,8e6,-0.1,1.4])
plt.show()