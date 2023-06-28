import numpy as np
import matplotlib.pyplot as plt 
from scipy.constants import hbar, pi 

ℏ, π, e = hbar, pi, np.exp

#  kg   J*s/kg   J^2s^2/kg
m = 1; ω = ℏ/m; k = m*ω**2;
def ψ_0(x):
    return ((m*ω)/(π*ℏ))**(1/4) * e(-m*ω*x**2/(2*ℏ))

def ψ_1(x):
    return ((2*m*ω)/(ħ))**(1/2) * x*ψ_0(x)

def ψ_2(x):
    return 1/2**(1/2) * ((3*m*ω)/(2*ħ)*x**2 - 1)*ψ_0(x)

def V(x):
    return 1/2 * k * x**2

lim = 5
x = np.linspace(-lim, lim, 1001)

fig, ax1 = plt.subplots(figsize=(10, 6))
plot1 = ax1.plot(x,ψ_0(x), label= r'ψ_0', color='navy')\
      + ax1.plot(x,ψ_1(x), label= r'ψ_1', color='blue')\
      + ax1.plot(x,ψ_2(x), label= r'ψ_2', color='deepskyblue')
      
ax1.set_ylabel(r'$[nm^{-2}]$', color = 'blue')
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
plot2 = ax2.plot(x,V(x), label= r'V(x)', color = 'red')
ax2.set_ylabel(r'[eVnm]', color = 'red')
ax2.tick_params(axis='y', labelcolor='red')

plots = plot1 + plot2
labels = [p.get_label() for p in plots]
plt.xlabel('x [nm]')
plt.grid()
plt.legend(plots, labels)
plt.savefig('4b.pdf')
plt.show()