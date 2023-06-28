import numpy as np 
import matplotlib.pyplot as plt
from scipy.constants import hbar
import os 
filepath = os.path.dirname(__file__)
ℏ = hbar
π = np.pi


def Ψ(x, t):
    n = 3; a = 1e-9; m = 0.511 # MeV / c^2
    return np.sqrt(2/a) * np.sin(n*π/a * x) * np.exp(-1j*((n**2*π**2*ℏ)/(2*m*a**2))*t)


x = np.linspace(0, π/16_000, 100)
t = 1e-14
fig, ax1 = plt.subplots(figsize = (16/2, 9/2))
plot1 = ax1.plot(x, Ψ(x, t).real, label = 'Re(Ψ)')
ax1.tick_params(labelcolor='blue')
ax2 = ax1.twinx()
plot2 = ax2.plot(x, Ψ(x, t).imag, label = 'Im(Ψ)', color = 'red')
ax2.tick_params(labelcolor='red')


ins = plot1 + plot2
labels = [l.get_label() for l in ins]
plt.legend(ins, labels, loc = 0)
plt.savefig(os.path.join(filepath, 'fig\\3.b.1.pdf'))
plt.show()

plt.figure(figsize = (16/2, 9/2))
plt.plot(x, np.abs(Ψ(x,t))**2, label = r'$|Ψ|^2$')
plt.savefig(os.path.join(filepath, 'fig\\3.b.2.pdf'))
plt.xlabel('x')
plt.ylabel('Sannsynlighet')
plt.legend()
plt.show()