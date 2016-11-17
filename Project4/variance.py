import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt("random_T1.dat")
data2 = np.loadtxt("random_T2_4.dat")
#data3 = np.loadtxt("expect_random_T2_4.dat")
#data4 = np.loadtxt("expect_T2_4.dat")

stable = 100000

values1 = data1[stable::1]/400
values2 = data2[stable::1]/400
#values3 = data3[stable::1]
#values4 = data4[stable::1]

print values1

N = len(values1)

fig = plt.figure()

print np.var(values1)
print np.var(values2)

labels = fig.add_subplot(111)
labels.spines['top'].set_color('none')
labels.spines['bottom'].set_color('none')
labels.spines['left'].set_color('none')
labels.spines['right'].set_color('none')
labels.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')
plt.ylabel("Frequency",fontsize=17)
#labels.yaxis.set_label_position("right")
plt.xlabel("Energy per spin",fontsize=17)


fig1 = fig.add_subplot(121)
fig1.hist(values1,label="T=1.0")
fig1.tick_params(axis='x', labelsize=15) #HOW TO PUT THIS ON THE RIGHT SIDE?
fig1.tick_params(axis='y', labelsize=15)
fig1.yaxis.tick_right()
plt.legend()

fig2 = fig.add_subplot(122)
fig2.hist(values2,color="black",bins=1000,label="T=2.4")

fig2.tick_params(axis='x', labelsize=15) #HOW TO PUT THIS ON THE RIGHT SIDE?
fig2.tick_params(axis='y', labelsize=15)
fig2.yaxis.tick_right()
plt.legend()
plt.show()

# range1 = 0
# range2 = 0
# range3 = 0
# range4 = 0
# range5 = 0
# range6 = 0
# range7 = 0
# range8 = 0
# range9 = 0

# test = 0

# outofrange = 0

# for i in range(0,N):
# 	if values1[i,0] <= -1.99622 and values1[i,0] > -1.99623:
# 		range1 += 1
# 	if values1[i,0] <= -1.99623 and values1[i,0] > -1.99624:
# 		range2 += 1
# 	elif values1[i,0] <= -1.99624 and values1[i,0] > -1.99625:
# 		range3 += 1
# 	elif values1[i,0] <= -1.99625 and values1[i,0] > -1.99626:
# 		range4 += 1
# 	elif values1[i,0] <= -1.99626 and values1[i,0] > -1.99627:
# 		range5 += 1
# 	elif values1[i,0] <= -1.99627 and values1[i,0] > -1.99628:
# 		#print values1[i,0]
# 		range6 += 1
# 	elif values1[i,0] <= -1.99628 and values1[i,0] > -1.99629:
# 		range7 += 1
# 	elif values1[i,0] <= -1.99629 and values1[i,0] > -1.99630:
# 		range8 += 1
# 	elif values1[i,0] <= -1.99630 and values1[i,0] > -1.99631:
# 		range9 += 1
# 	else:
# 		print values1[i,0]
# 		outofrange += 1


# print "Range 1: " + str(range1)
# print "Range 2: " + str(range2)
# print "Range 3: " + str(range3)
# print "Range 4: " + str(range4)
# print "Range 5: " + str(range5)
# print "Range 6: " + str(range6)
# print "Range 7: " + str(range7)
# print "Range 8: " + str(range8)
# print "Range 9: " + str(range9)
# print "Out of range: " + str(outofrange)

# ranges = [30, 205, 114, 153, 187, 130, 136, 37]
# x = np.linspace(1,8,8)



#plt.plot(x, ranges)
#plt.show()