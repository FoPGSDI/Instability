#!/usr/bin/env python3
"""
Agent 17: Rotating magnetar convection — Ra(Ta, Q) 3D stability surface.
Shows the critical Rayleigh number as a function of both Taylor and
Chandrasekhar numbers for relativistic parameters.
"""
import sys; sys.path.insert(0, '/data/haiyangw/claude/Instability'); from SHARED_PLOT_STYLE import setup_style, COLORS, pi
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

setup_style()

def Ra_c_TQ(T_val, Q_val):
    """Critical Ra for two free boundaries with rotation+magnetic field.
    From eq (57): Ra = (pi^2+a^2) * {[(pi^2+a^2)^2 + Q*pi^2]^2 + T*pi^2*(pi^2+a^2)^2}
                       / {a^2 * [(pi^2+a^2)^2 + Q*pi^2]}
    Minimize over a (i.e. over x = a^2/pi^2)."""
    Q1 = Q_val / pi**2
    T1 = T_val / pi**4
    x_vals = np.linspace(0.1, 50, 2000)
    Ra_vals = []
    for x in x_vals:
        num = (1+x) * (((1+x)**2 + Q1)**2 + T1 * (1+x))
        den = x * ((1+x)**2 + Q1)
        Ra_vals.append(pi**4 * num / den)
    return min(Ra_vals)

# Create grid
log_T = np.linspace(0, 8, 40)
log_Q = np.linspace(0, 6, 40)
TT, QQ = np.meshgrid(log_T, log_Q)
log_Ra = np.zeros_like(TT)

for i in range(TT.shape[0]):
    for j in range(TT.shape[1]):
        Ra = Ra_c_TQ(10**TT[i,j], 10**QQ[i,j])
        log_Ra[i,j] = np.log10(max(Ra, 1))

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(TT, QQ, log_Ra, cmap='coolwarm', alpha=0.85,
                       edgecolor='k', linewidth=0.2)

ax.set_xlabel(r'$\log_{10} T_{\mathrm{rel}}$', labelpad=10)
ax.set_ylabel(r'$\log_{10} Q_{\mathrm{rel}}$', labelpad=10)
ax.set_zlabel(r'$\log_{10} \mathrm{Ra}_{c,\mathrm{rel}}$', labelpad=10)
ax.set_title('Rotating magnetar convection: stability surface', pad=15)

# Add colorbar
cbar = fig.colorbar(surf, shrink=0.5, aspect=15, pad=0.1)
cbar.set_label(r'$\log_{10} \mathrm{Ra}_{c,\mathrm{rel}}$')

ax.view_init(elev=25, azim=-55)

fig.tight_layout()
fig.savefig('/data/haiyangw/claude/Instability/plots/ch5/fig_rotating_magnetar_stability.pdf')
fig.savefig('/data/haiyangw/claude/Instability/plots/ch5/fig_rotating_magnetar_stability.png')
print("Saved fig_rotating_magnetar_stability.pdf/png")
