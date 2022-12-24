#chemical reaction; concentration of reactants and products simulation
import numpy as np
import matplotlib.pyplot as plt

k1 = 0.4
k2 = 0.8

dt = 0.002
t_total = 5
t = np.arange(0,t_total,dt)

l = int(t_total/dt)
c1 = np.zeros(l,)
c2 = np.zeros(l,)
c3 = np.zeros(l,)

# for i in range(l):
c1[0] = 5
c2[0] = 5
c3[0] = 0.2

i = 0

for i in range(l-1):
    c1[i+1] = c1[i] + (k2*c3[i] - k1*c1[i]*c2[i])*dt
    c2[i+1] = c2[i] + (k2*c3[i] - k1*c1[i]*c2[i])*dt
    c3[i+1] = c3[i] + (2*k1*c1[i]*c2[i] - 2*k2*c3[i])*dt


plt.subplot(2,2,1)
plt.title('c1')
plt.plot(t,c1)

plt.subplot(2,2,2)
plt.title('c2')
plt.plot(t,c2)

plt.subplot(2,2,3)
plt.title('c3')
plt.plot(t,c3)

plt.show()