#voltage in a circuit simulation

import matplotlib.pyplot as plt

A11 = -50.0
A21 = -19000.0
A22 = -21.5
ein = 1.5

def func1(v10):
    return A11 * v10 - A11*ein

def func2(v10, v20):
    return (A21*v10 + A22*v20 -A21*ein)


if __name__=='__main__':
    #m11, m12, m13, m14, m21, m22, m23, m24, v11, v21, v10=0.0, v20=0.0, t
    v10 = 0.0
    v20 = 0.0
    h = 0.0002
    t_l = [0]
    v10_l = [v10]
    v20_l = [v20]

    for i in range(800):
        m11 = func1(v10)
        m12 = func1(v10 + m11*h/2)
        m13 = func1(v10 + m12*h/2)
        m14 = func1(v10 + m13*h)
        v11 = v10 + ((m11 + 2*m12 + 2*m13 + m14)/6) * h
        
        m21 = func2(v10, v20)
        m22 = func2(v10 + h/2, v20+m21*h/2)
        m23 = func2(v10 + h/2, v20+m22*h/2)
        m24 = func2(v10 +h, v20+m23*h)
        v21 = v20+((m21+2*m22+2*m23 +m24)/6)*h

        v10 = v11
        v20 = v21
        t = h*i
        # print(v10, v20)
        v10_l.append(v10)
        v20_l.append(v20)

        t_l.append(t)

    # print(t_l)
    # print(v10_l)
    # print(v20_l)
    
    plt.subplot(1,2,1)
    plt.title('v10')
    plt.plot(t_l,v10_l)

    plt.subplot(1,2,2)
    plt.title('v20')
    plt.plot(t_l,v20_l)

    plt.show()