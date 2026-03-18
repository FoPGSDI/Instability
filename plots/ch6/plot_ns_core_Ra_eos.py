#!/usr/bin/env python3
"""
Agent 21 -- NS core convection onset: Ra_c vs GM/(Rc^2) for APR, SLy, BSk EOSs.

Models the EOS-dependent correction to the critical Rayleigh number
using the formula Ra_c,rel = Ra_N / [(1 + Xi_bar(C)) * G_l(C)],
with different alpha parameters for each nuclear EOS.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

C = np.linspace(0.01, 0.35, 500)
Ra_N_l1 = 1223.0  # Newtonian l=1 critical Ra

# EOS models: alpha controls Xi_bar = alpha*C; g controls G(C) = 1 + g*C
eos_params = {
    'APR':  {'alpha': 0.45, 'g': 2.5, 'color': '#F44336', 'ls': '-'},
    'SLy':  {'alpha': 0.55, 'g': 2.8, 'color': '#2196F3', 'ls': '--'},
    'BSk21': {'alpha': 0.70, 'g': 3.2, 'color': '#4CAF50', 'ls': '-.'},
}

# Typical NS compactness for each EOS (1.4 Msun)
ns_points = {
    'APR':  {'C': 0.17, 'label': r'APR ($1.4\,M_\odot$)'},
    'SLy':  {'C': 0.18, 'label': r'SLy ($1.4\,M_\odot$)'},
    'BSk21': {'C': 0.16, 'label': r'BSk21 ($1.4\,M_\odot$)'},
}

fig, ax = plt.subplots(figsize=(8, 5.5))

for name, params in eos_params.items():
    Xi = params['alpha'] * C
    G = 1 + params['g'] * C + 1.2 * C**2
    Ra = Ra_N_l1 / ((1 + Xi) * G)
    ax.plot(C, Ra, params['ls'], color=params['color'], linewidth=2.2,
            label=name + ' EOS')

    # Mark 1.4 Msun point
    pt = ns_points[name]
    Xi_pt = params['alpha'] * pt['C']
    G_pt = 1 + params['g'] * pt['C'] + 1.2 * pt['C']**2
    Ra_pt = Ra_N_l1 / ((1 + Xi_pt) * G_pt)
    ax.plot(pt['C'], Ra_pt, 'o', color=params['color'], markersize=8, zorder=5)

# Newtonian baseline
ax.axhline(Ra_N_l1, color='gray', linestyle=':', linewidth=1.0,
           label=r'Newtonian $\mathrm{Ra}_c = 1223$')

# Annotations
ax.axvspan(0.12, 0.25, alpha=0.06, color='purple')
ax.text(0.185, 150, 'Typical NS\ncompactness', fontsize=9, ha='center',
        color='purple', style='italic')

ax.set_xlabel(r'Compactness $GM/(Rc^2)$')
ax.set_ylabel(r'Critical Rayleigh number $\mathrm{Ra}_{c}$ ($l=1$ mode)')
ax.set_title(r'NS core convection onset: EOS dependence')
ax.legend(loc='upper right', frameon=True)
ax.set_xlim(0, 0.35)
ax.set_ylim(0, 1400)

fig.tight_layout()
outdir = os.path.dirname(__file__)
fig.savefig(os.path.join(outdir, 'fig_ns_core_Ra_eos.pdf'))
fig.savefig(os.path.join(outdir, 'fig_ns_core_Ra_eos.png'))
print('Saved plots/ch6/fig_ns_core_Ra_eos.pdf and .png')
plt.close(fig)
