import numpy as np 
import matplotlib.pyplot as plt
import os
filepath = os.path.dirname(__file__)

def Ψ(x, λ):
    return λ*np.exp(-2*λ*abs(x))

λ = 1
σ = 1/(np.sqrt(2)*λ)
x = np.linspace(-5,5,1000)
plt.figure(figsize=(16,9))
plt.plot(x,Ψ(x,λ), label = r'$|Ψ(x)|^2$')
plt.vlines(σ, 0, 1, linestyles='--', colors = 'black', label = r'$<x> + σ$')
plt.vlines(-σ, 0, 1, linestyles='--', colors = 'black', label = r'$<x> - σ$')
font_size = 20
plt.xlabel('x', fontsize=font_size)
plt.ylabel(r'$\left|Ψ(x)\right|^2$    ', fontsize=font_size, rotation=0)
plt.title('Sannsynligheten for å finne et objekt i en posisjon x', fontsize=font_size)
plt.xticks([-4, -2, -σ, 0, σ, 2, 4], [-4, -2, r'$<x> - σ$', 0, r'$<x> + σ$', 2, 4], fontsize=font_size/1.5)
plt.legend(fontsize=font_size)
plt.savefig(os.path.join(filepath, '4.c.pdf'))
# plt.show()