import numpy as np
import matplotlib.pyplot as plt
import os 
filepath = os.path.dirname(__file__)
figpath = filepath + '\\fig\\'
π = np.pi


def ω(k, m):
    c = ℏ = 1
    return c*np.sqrt(k**2 + (m*c/ℏ)**2)

def sinus(x,t, A, k, ω):
    return A*np.sin(k*x + ω*t)

def fasehastighet(ω, k):
    return ω/k

def gruppehastighet(k):
    return k/(np.sqrt(k**2 + 1))

def A(k):
    return a/(k**2 + a**2)

def cosinus(x,t, A, k, ω):
    return A*np.cos(k*x + ω*t)


k1 = 0.7
k2 = 0.6
A = m = 1
ω1 = ω(k1, m)
ω2 = ω(k2, m)
x = np.linspace(0, 1000*π, 100)
t = np.linspace(0,100, 100)
y = sinus(x,t, A, k1, ω1) + sinus(x,t, A, k2, ω2)

# a)
def a():
    plt.plot(x,y)
    plt.title('Superponeringen av to sinus bølger', fontsize=16)
    plt.savefig(figpath + '5a.pdf')
    plt.show()
    
def b():
    vf1 = fasehastighet(ω1, k1)
    vf2 = fasehastighet(ω2, k2)
    vg1 = gruppehastighet(k1)
    vg2 = gruppehastighet(k2)
    vf = vf1 + vf2
    vg = vg1 + vg2
    print(f'Fasehastigheten: {vf: .2f}')
    print(f'Gruppehastigheten: {vg: .2f}')
    '''
    Fasehastigheten:  3.69
    Gruppehastigheten:  1.09
    '''
    
    
def c():
    def A(k):
        return a/(k**2 + a**2)

    t = 0
    m = 1
    a = 10000
    n = 1000
    k = np.linspace(-5, 5, n)
    x = np.linspace(-4*π, 4*π, n)
    y = 0
    for k_i in k:
        y += cosinus(x, t, A(k_i), k_i, ω(k_i, m))
    
    plt.plot(x,y)
    plt.title('Superponeringen av 1000 cosinus bølger', fontsize=16)
    plt.savefig(figpath + '5c.pdf')  
    plt.show()
    
    
if __name__ == '__main__':
    a()
    b()
    c()
