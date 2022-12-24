#random number generator
#ri+1 = (ri*a +b ) mod P

#test for random number

import matplotlib.pyplot as plt
seed = 19
P = 100
a = 17
b= 31
rand_num = (seed * a + b ) % P

#generate 1000 random numbers in range 0 to 100
classes = [0,0,0,0,0]
Num_of_Obs = 1000
num_classes = len(classes)
rand_list = [rand_num]
for i in range(Num_of_Obs):

    rand_num = (rand_list[i] * a + b) % P
    if(rand_num<20):
        classes[0] += 1
    if(rand_num>=20 and rand_num<40):
        classes[1] += 1
    if(rand_num>=40 and rand_num<60):
        classes[2] += 1
    if(rand_num>=60 and rand_num<80):
        classes[3] += 1
    if(rand_num>=80 and rand_num<100):
        classes[4] += 1
    
    rand_list.append(rand_num)

# print(rand_list)
Ei = Num_of_Obs/num_classes
print(classes)
print(Ei)
Xi = sum([(c-Ei)*(c-Ei)/Ei for c in classes])

print(Xi)

plt.scatter(rand_list, [0]*len(rand_list))
plt.show()


