"""Exercise 14."""
import numpy as np
import neurolab as nl
import matplotlib.pyplot as plt

purelin = nl.trans.PureLin()
logsig = nl.trans.LogSig()

alpha = 0.1

epochs = 1000
x=np.array([2, 5, 4, 5, 3, 2, 3, 2])
y=np.array([1, 3, 4, 2, 2, 3, 6, 4])

p = np.array([x,y])
p = p.T

s = 1
t = np.array([1, 1, 1, 1, -1, -1, -1, -1])

w1=np.random.rand(3,2)
b1=np.random.rand(3,1)
w2=np.random.rand(1,3)
b2=np.random.rand(1,1)

ea = np.zeros(p.shape[0])

for epoch in range(epochs):
    for id_p in range(p.shape[0]):
        pn=np.random.rand(2,1)
        pn[0][0] = p[id_p][0]
        pn[1][0] = p[id_p][1]
        a1 = logsig(np.dot(w1,pn)+b1)
        a2 = purelin(np.dot(w2,a1)+b2)
        e = t[id_p] - a2
        f1= (1-a1)*a1
        f2 = 1
        f11 = f1[0]
        f12 = f1[1]
        f13 = f1[2]
        fd1 = np.append(np.array([0, 0]), f11)
        fd2 = np.append(np.array([0]), f12)
        fd2 = np.append(fd2, np.array([0]))
        fd3 = np.append(f13, np.array([0, 0]))
        fd = np.array([fd1, fd2, fd3])
        fd2 = 1
        s2 = -2*fd2*e
        s1 = np.dot(fd,np.dot((w2).T,s2))
        w2 = w2 - alpha*s2*a1.T
        b2 = b2 - alpha*s2
        w1 = w1 - alpha*s1*pn.T
        b1 = b1 - alpha*s1
        ea[id_p] = a2[0][0]

plt.figure()

pn=np.random.rand(2,1)
for x in range(60):
    x *= 0.1
    for j in range(60):
        j *= 0.1
        pn[0][0] = x
        pn[1][0] = j
        a1=logsig(np.dot(w1,pn) + b1)
        a2=purelin(np.dot(w2,a1) + b2)
        if (a2[0][0]>=0):
            plt.plot([x], [j], 'bo')
        if (a2[0][0]<0):
            plt.plot([x], [j], 'ro')

plt.plot([2, 5, 4, 5], [1, 3, 4, 2], 'w*')
plt.plot([3, 2, 3, 2], [2, 3, 6, 4], 'k*')
plt.show()
