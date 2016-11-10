import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt("accepted_random_T1.dat")
#data1 = np.loadtxt("accepted.dat")
data2 = np.loadtxt("accepted_ordered_T1.dat")
data3 = np.loadtxt("accepted_random_T2_4.dat")
data4 = np.loadtxt("accepted_ordered_T2_4.dat")

randomT1 = data1[0::5]
orederedT1 = data2[0::5]
randomT24 = data3[0::5]
orederedT24 = data4[0::5]

N1 = len(randomT1)
N2 = len(orederedT1)
x1 = np.linspace(0,N1,N1)
x2 = np.linspace(0,N2,N2)

fig = plt.figure()

labels = fig.add_subplot(111)
labels.spines['top'].set_color('none')
labels.spines['bottom'].set_color('none')
labels.spines['left'].set_color('none')
labels.spines['right'].set_color('none')
labels.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

plt.ylabel("Total number of accepted configurations",fontsize=15)

#fig.axes[0].get_yaxis()
#ax = gca()
#labels.yaxis.set_label_position("right")
plt.xlabel("Number of Monte Carlo cycles",fontsize=15)

fig1 = fig.add_subplot(211)
fig1.plot(x1,randomT1,label="Random, T=1")
fig1.plot(x2,orederedT1,label="Ordered, T=1")
fig1.tick_params(axis='x', labelsize=12)
fig1.tick_params(axis='y', labelsize=12)


fig1.yaxis.tick_right()
#plt.ylabel("Total number of accepted configurations",fontsize=15)
#plt.xlabel("Number of Monte Carlo cycles",fontsize=15)
plt.legend(loc="lower right")
#plt.axis([-10000,1e6,0,3000])
#plt.show()

fig2 = fig.add_subplot(212)
fig2.plot(x2,randomT24,label="Random, T=2.4")
fig2.plot(x2,orederedT24,label="Ordered, T=2.4")
fig2.yaxis.tick_right()
fig2.tick_params(axis='x', labelsize=12)
fig2.tick_params(axis='y', labelsize=12)
#plt.ylabel("Total number of accepted configurations",fontsize=15)
#plt.xlabel("Number of Monte Carlo cycles",fontsize=15)
plt.legend(loc="lower right")#,bbox_transform=plt.gcf().transFigure)
#plt.axis([-10000,1e6,0,50000])
plt.show()


#plt.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)