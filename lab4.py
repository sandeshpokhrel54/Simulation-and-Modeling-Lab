#damping in spring system
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

k=5 #spring coefficient
m=30
D = 1.5 #damper coefficient
F = 15
# angular_freq = math.sqrt(k/m)
# damping_ratio = D/2*m*angular_fre
t = np.linspace(0,20,2001)

#separate the second order diff eqn to system of single order diff eqns and solve
def spring(y, t, F, m, D):
    x2, x1 = y
    dydt = [x1, F/m-D/m*x1-k/m*x2]
    return dydt

y0 = [0.0, 0.0]


for d in [1.5, 2.4, -3.3, 0.4]:

    sol = odeint(spring, y0, t, args=(F, m, d))

    # print(sol)
    plt.plot(t, sol[:,0], label = 'displacement') 
    plt.plot(t, sol[:,1],label = 'velocity')
    plt.legend(loc='lower right')
    plt.show()

# plt.show()

