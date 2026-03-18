#!/usr/bin/env python3
"""
Agent 31: Stability map for disk with radial pressure gradient.

Shows the critical Taylor number T_c as a function of the transverse
velocity parameter lambda for several values of the relativistic
pressure parameter Xi = p/(epsilon c^2), illustrating stabilisation
by relativistic inertia in accretion disk coronae.

Produces: plots/ch8/fig_disk_stability_map.pdf
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# Classical T_c(lambda) from Chandrasekhar Table XXXIX approximation
# Using the approximate formula: T_c ~ 3416 / (1 + lambda/3) for |lambda| < 1
# and T_c ~ 9.3e4 * (1-mu) / lambda^2 for large |lambda|
lam = np.linspace(-6, 6, 600)
lam_safe = np.where(np.abs(lam) < 0.01, 0.01, lam)

# Piecewise approximation to classical T_c(lambda)
Tc_class = np.where(
    np.abs(lam) < 1.5,
    3416.0 / np.maximum(1 + lam / 3.0, 0.05),
    9.3e4 / lam_safe**2
)
# Cap at the sharp maximum near lambda ~ -3.5
Tc_class = np.minimum(Tc_class, 5e5)
Tc_class = np.maximum(Tc_class, 100)

Xi_values = [0.0, 0.1, 0.3, 0.5]
colors = [COLORS['classical'], '#4CAF50', COLORS['accretion'], COLORS['relativistic']]
labels = ['Classical ($\\Xi = 0$)',
          r'$\Xi = 0.1$ (NS interior)',
          r'$\Xi = 0.3$ (QGP/rad. corona)',
          r'$\Xi = 0.5$ (ultra-rel.)']

fig, ax = plt.subplots(figsize=(9, 6))

for i, Xi in enumerate(Xi_values):
    Tc_rel = Tc_class * (1 + Xi)**2
    ls = '-' if Xi == 0 else '--'
    ax.semilogy(lam, Tc_rel, color=colors[i], ls=ls, lw=2.0, label=labels[i])

ax.set_xlabel(r'Transverse velocity parameter $\lambda = 6V_m / (R_1 \Omega_1)$')
ax.set_ylabel(r'Critical Taylor number $T_c^{\mathrm{(rel)}}$')
ax.set_title('Stability Map: Disk with Radial Pressure Gradient')
ax.legend(fontsize=10, loc='upper right')
ax.set_xlim(-6, 6)
ax.set_ylim(1e2, 1e6)

# Annotate astrophysical regimes
ax.annotate('Rayleigh\nstable', xy=(3, 5e2), fontsize=9, ha='center',
            color='gray')
ax.annotate('Centrifugal\nunstable', xy=(-4, 5e2), fontsize=9, ha='center',
            color='gray')
ax.axvline(x=0, color='gray', ls=':', lw=0.8)

fig.tight_layout()
fig.savefig(os.path.join(os.path.dirname(__file__), 'fig_disk_stability_map.pdf'))
fig.savefig(os.path.join(os.path.dirname(__file__), 'fig_disk_stability_map.png'))
print("Saved plots/ch8/fig_disk_stability_map.pdf")
