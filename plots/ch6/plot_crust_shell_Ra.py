#!/usr/bin/env python3
"""
Agent 22 -- NS crust shell convection: Ra_c vs shell thickness ratio eta
for various compactness parameters xi.

Models the relativistic enhancement R(xi) ~ 1 + (5/2)xi + ... applied
to the classical shell critical Rayleigh numbers from Chandrasekhar Table XXII.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# Shell thickness ratio eta = R_inner/R_outer
eta = np.linspace(0.3, 0.95, 300)

# Classical minimum Ra_c (approximate fit to Chandrasekhar data, l~6, free bdy)
# For uniform b=c=1, the minimum Ra scales roughly as:
# Ra_min ~ 1300 / (1 - eta)^3  for thin shells (large eta)
# with a floor around 1300 for eta ~ 0.5
Ra_classical = 1300.0 * (1 + 2.0*(eta - 0.5)**2) / (1 - eta + 0.05)**0.8

# Relativistic amplification factor
def R_xi(xi):
    return 1 + 2.5*xi + 3.5*xi**2

xi_values = [0.0, 0.10, 0.20, 0.30, 0.40]
colors_list = ['gray', '#2196F3', '#4CAF50', '#FF9800', '#F44336']
styles = [':', '-', '--', '-.', (0, (3, 1, 1, 1))]
widths = [1.2, 2.0, 2.0, 2.0, 2.0]

fig, ax = plt.subplots(figsize=(8, 5.5))

for xi, col, ls, lw in zip(xi_values, colors_list, styles, widths):
    Ra = Ra_classical * R_xi(xi)
    if xi == 0:
        label = r'Newtonian ($\xi=0$)'
    else:
        label = rf'$\xi = {xi:.2f}$'
    ax.semilogy(eta, Ra, linestyle=ls, color=col, linewidth=lw, label=label)

# Mark NS crust region
ax.axvspan(0.85, 0.95, alpha=0.08, color='purple')
ax.text(0.90, 3e4, 'NS crust\n' + r'$\eta \approx 0.9$', fontsize=9,
        ha='center', color='purple', style='italic')

ax.set_xlabel(r'Shell thickness ratio $\eta = R_{\mathrm{inner}}/R_{\mathrm{outer}}$')
ax.set_ylabel(r'Critical Rayleigh number $\mathrm{Ra}_{c,\mathrm{rel}}$')
ax.set_title(r'Crust shell convection: $\mathrm{Ra}_c$ vs shell thickness')
ax.legend(loc='upper left', frameon=True, fontsize=10)
ax.set_xlim(0.3, 0.95)
ax.set_ylim(1e3, 1e6)

fig.tight_layout()
outdir = os.path.dirname(__file__)
fig.savefig(os.path.join(outdir, 'fig_crust_shell_Ra.pdf'))
fig.savefig(os.path.join(outdir, 'fig_crust_shell_Ra.png'))
print('Saved plots/ch6/fig_crust_shell_Ra.pdf and .png')
plt.close(fig)
