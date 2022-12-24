#economic system
import matplotlib.pyplot as plt
I = 2

l_G = [30000, 40000, 30000, 50000,60000,70000, 80000]
Y_l = []
I_l = []
T_l = []
C_l = []
for G in l_G:
    Y = 45.45 +2.27*(I+G)
    I = 2 + 0.1*Y
    T = 0.2*Y
    C = 20 + 0.7*(Y-T)
    Y_l.append(Y)
    I_l.append(I)
    T_l.append(T)
    C_l.append(C)

# print(Y_l)
# print(I_l)
# print(T_l)
# print(C_l)

plt.subplot(2,2,1)
plt.scatter(l_G, Y_l)
plt.title('Gov exp vs National Income')

plt.subplot(2,2,2)
plt.scatter(l_G, T_l)
plt.title('Gov exp vs Taxes')

plt.subplot(2,2,3)
plt.scatter(l_G,I_l)
plt.title('Gov exp vs Investment')

plt.subplot(2,2,4)
plt.scatter(l_G,C_l)
plt.title('Gov exp vs Consumption')
plt.show()


