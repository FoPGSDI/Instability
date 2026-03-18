#!/usr/bin/env python3
"""
Agent 19 -- Plot TOV equilibrium profiles for a neutron star:
  energy density epsilon(r), pressure p(r), metric potential Phi(r).

Uses the Schwarzschild interior (uniform-density) exact solution for
several compactness values C = GM/(Rc^2).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, G_cgs, M_sun
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# --- Schwarzschild interior exact solution (uniform density) ---
# p(r)/epsilon = [sqrt(1 - 2C r^2/R^2) - sqrt(1 - 2C)] /
#                [3 sqrt(1 - 2C) - sqrt(1 - 2C r^2/R^2)]
# Phi(r)/c^2 = (1/2) ln[ (3 sqrt(1-2C) - sqrt(1-2C r^2/R^2)) / 2 ]
# (with Phi matched at surface to Schwarzschild exterior)

r_frac = np.linspace(1e-3, 1.0, 500)  # r/R

compactnesses = [0.05, 0.10, 0.20, 0.30]
colors_list = ['#2196F3', '#4CAF50', '#FF9800', '#F44336']
styles = ['-', '--', '-.', ':']

fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

for C, col, ls in zip(compactnesses, colors_list, styles):
    x2 = r_frac**2
    sq_r = np.sqrt(1 - 2*C*x2)
    sq_R = np.sqrt(1 - 2*C)

    # Pressure profile (normalised to central epsilon)
    p_over_eps = (sq_r - sq_R) / (3*sq_R - sq_r)

    # Energy density is constant = 1 (uniform density)
    eps_norm = np.ones_like(r_frac)

    # Metric potential Phi/c^2 (shifted so Phi(R)=0 matches exterior)
    # e^{2Phi/c^2} = [(3 sqrt(1-2C) - sqrt(1-2C r^2/R^2))/2]^2
    # Phi/c^2 = ln[ (3 sq_R - sq_r) / 2 ]
    Phi_over_c2 = np.log((3*sq_R - sq_r) / 2.0)

    label = rf'$\mathcal{{C}}={C:.2f}$'

    axes[0].plot(r_frac, eps_norm, ls, color=col, linewidth=1.8, label=label)
    axes[0].plot(r_frac, 1 + p_over_eps, ls, color=col, linewidth=1.8, alpha=0.5)

    axes[1].plot(r_frac, p_over_eps, ls, color=col, linewidth=1.8, label=label)

    axes[2].plot(r_frac, Phi_over_c2, ls, color=col, linewidth=1.8, label=label)

# --- Axis labels and formatting ---
axes[0].set_xlabel(r'$r/R$')
axes[0].set_ylabel(r'$\varepsilon/\varepsilon_c$ and $({\varepsilon+p})/{\varepsilon_c}$')
axes[0].set_title(r'Energy density & enthalpy')
axes[0].legend(fontsize=9)
axes[0].set_ylim(0.8, 2.5)
axes[0].text(0.5, 2.3, r'$(\varepsilon+p)/\varepsilon_c$', fontsize=9, color='gray')
axes[0].text(0.5, 1.05, r'$\varepsilon/\varepsilon_c = 1$', fontsize=9, color='gray')

axes[1].set_xlabel(r'$r/R$')
axes[1].set_ylabel(r'$p(r)/\varepsilon_c$')
axes[1].set_title(r'Pressure profile')
axes[1].legend(fontsize=9)

axes[2].set_xlabel(r'$r/R$')
axes[2].set_ylabel(r'$\Phi(r)/c^2$')
axes[2].set_title(r'Metric potential $\Phi$')
axes[2].legend(fontsize=9)

fig.suptitle('TOV equilibrium profiles (Schwarzschild interior)', fontsize=13, y=1.02)
fig.tight_layout()

outdir = os.path.join(os.path.dirname(__file__))
fig.savefig(os.path.join(outdir, 'fig_tov_profiles.pdf'))
fig.savefig(os.path.join(outdir, 'fig_tov_profiles.png'))
print('Saved plots/ch6/fig_tov_profiles.pdf and .png')
plt.close(fig)
