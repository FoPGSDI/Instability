#!/usr/bin/env python3
"""
Agent 20 -- Variational Ra_c vs compactness C for l=1,2,3 modes
in a self-gravitating relativistic sphere.

Uses the model from sec57-58: C_rel = C / [(1 + Xi_bar) * G(C)]
where G(C) = 1 + g_l * C + ... and Xi_bar ~ alpha_eos * C.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

C = np.linspace(0, 0.42, 500)

# Newtonian critical Ra values (from Chandrasekhar Table XX, free boundary)
Ra_N = {1: 1223.0, 2: 1704.0, 3: 2432.0}

# Model parameters per l-mode
# g_l: curvature coefficient; Xi_bar ~ 0.6*C (moderate EOS)
g_l = {1: 2.8, 2: 2.5, 3: 2.3}

def Ra_rel(C_val, l):
    Xi_bar = 0.6 * C_val
    G_C = 1 + g_l[l] * C_val + 1.5 * C_val**2
    ratio = 1.0 / ((1 + Xi_bar) * G_C)
    return Ra_N[l] * ratio

colors_l = {1: '#F44336', 2: '#2196F3', 3: '#4CAF50'}
styles_l = {1: '-', 2: '--', 3: '-.'}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

# Left: Ra_c,rel vs C for each l
for l in [1, 2, 3]:
    Ra_vals = Ra_rel(C, l)
    ax1.plot(C, Ra_vals, styles_l[l], color=colors_l[l], linewidth=2.0,
             label=rf'$l={l}$')
    ax1.axhline(Ra_N[l], color=colors_l[l], linestyle=':', linewidth=0.8, alpha=0.4)

ax1.axvspan(0.1, 0.25, alpha=0.07, color='blue')
ax1.text(0.175, 100, 'NS range', fontsize=9, ha='center', color='#1f77b4', style='italic')
ax1.set_xlabel(r'Compactness $\mathcal{C} = GM/(Rc^2)$')
ax1.set_ylabel(r'$\mathrm{Ra}_{c,\mathrm{rel}}$')
ax1.set_title(r'Critical Ra vs compactness (variational, free boundary)')
ax1.legend(loc='upper right')
ax1.set_xlim(0, 0.42)
ax1.set_ylim(0, 2600)

# Right: ratio Ra_rel / Ra_N vs C
for l in [1, 2, 3]:
    ratio = Ra_rel(C, l) / Ra_N[l]
    ax2.plot(C, ratio, styles_l[l], color=colors_l[l], linewidth=2.0,
             label=rf'$l={l}$')

ax2.axhline(1.0, color='gray', linestyle=':', linewidth=1.0)
ax2.axvspan(0.1, 0.25, alpha=0.07, color='blue')
ax2.set_xlabel(r'Compactness $\mathcal{C} = GM/(Rc^2)$')
ax2.set_ylabel(r'$\mathrm{Ra}_{c,\mathrm{rel}} / \mathrm{Ra}_{c}^{(N)}$')
ax2.set_title(r'Ratio to Newtonian critical Ra')
ax2.legend(loc='lower left')
ax2.set_xlim(0, 0.42)
ax2.set_ylim(0, 1.1)

fig.tight_layout()
outdir = os.path.dirname(__file__)
fig.savefig(os.path.join(outdir, 'fig_variational_Ra_compactness.pdf'))
fig.savefig(os.path.join(outdir, 'fig_variational_Ra_compactness.png'))
print('Saved plots/ch6/fig_variational_Ra_compactness.pdf and .png')
plt.close(fig)
