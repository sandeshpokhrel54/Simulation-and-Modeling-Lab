#economic system
import matplotlib.pyplot as plt

l_G = [30000, 40000, 50000, 60000, 70000, 80000, 90000]
Y_l = [0]
I_l = [40000]
T_l = [0]
C_l = [0]


for i in range(1,len(l_G)):
    Y = 45.45 +2.27*(I_l[i-1] + l_G[i-1])
    I = 2 + 0.1*Y_l[i-1]
    T = 0.2*Y_l[i-1]
    C = 20 + 0.7*(Y_l[i-1]-T_l[i-1])
    Y_l.append(Y)
    I_l.append(I)
    T_l.append(T)
    C_l.append(C)



plt.subplot(2,2,1)
# plt.scatter(l_G, Y_l)
plt.plot(l_G, Y_l, color='g')
plt.title('Gov exp vs National Income')

plt.subplot(2,2,2)
# plt.scatter(l_G, T_l)
plt.plot(l_G, T_l, color='red')
plt.title('Gov exp vs Taxes')

plt.subplot(2,2,3)
# plt.scatter(l_G,I_l)
plt.plot(l_G, I_l, color = 'purple')
plt.title('Gov exp vs Investment')

plt.subplot(2,2,4)
# plt.scatter(l_G,C_l)
plt.plot(l_G, C_l)
plt.title('Gov exp vs Consumption')
plt.show()


