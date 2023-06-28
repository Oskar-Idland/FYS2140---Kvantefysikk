import numpy as np 
import matplotlib.pyplot as plt
import os 
filepath = os.path.dirname(__file__)
π = np.pi
e = np.exp

# [nm]       [nm]        [nm]     [nm]              [nm]
a = π; ε = 0.01*a; x0 = 0.5*a; k = π/a; A = np.sqrt(2/a);

def ψ(x):
    return 1/(np.sqrt(ε)) * e(-abs(x-x0)/ε)

def ψ_1(x):
    return A*np.sin(1*π/a * x)


x = np.linspace(0,a, 10_000) # [nm]

fontsize = 20
fig, ax1 = plt.subplots(figsize=(14, 8))
plot1 = ax1.plot(x, ψ(x), linewidth=4, label = r'$Ψ_{x_0}(x)$')
ax1.set_xlabel('x [nm]', fontsize=fontsize)
ax1.set_ylabel(r'[$nm^{-1/2}$]', fontsize=fontsize, color='blue')
# ax1.yaxis.set_label_coords(-0.2,.45)
ax1.set_xticks([0, 0.25*a, 0.5*a, 0.75*a, a], ['0', r'$\frac{1}{4} a$', r'$\frac{1}{2} a$', r'$\frac{3}{4} a$', 'a'], fontsize=fontsize-2)
ax1.tick_params(axis='y', labelcolor='blue', labelsize=fontsize)


ax2 = ax1.twinx()
plot2 = ax2.plot(x, ψ_1(x), linestyle='--' , color = 'red', linewidth=4, label = r'$ψ_1(x)$')
ax2.tick_params(axis='y', labelcolor='red', labelsize=fontsize)
ax2.set_ylabel(r'[$nm^{-1/2}$]', fontsize=fontsize, color='red')
# ax2.yaxis.set_label_coords(1.25,.475)

plt.title('Bølgefunksjonen til elektronet samt dets laveste energinivå ved t=0', fontsize=fontsize)
plot = plot1 + plot2
labels = [l.get_label() for l in plot]
plt.legend(plot, labels, fontsize=fontsize)

plt.tight_layout()
plt.savefig(os.path.join(filepath, 'Midtveis.pdf'))
plt.show()