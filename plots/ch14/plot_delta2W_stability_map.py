#!/usr/bin/env python3
"""
Plot delta^2 W stability map for tokamak-like MHD configurations.

The MHD energy principle: stability requires delta^2 W > 0 for all
admissible displacements. We plot the stability boundary in the
(beta, q) parameter space, where:
  - beta = 8*pi*p / B^2 (plasma beta)
  - q = safety factor (related to field line pitch)

Relativistic corrections enter through:
  - Enthalpy density w = (eps + p)/c^2 replacing rho
  - Bounded Alfven speed v_A < c
  - Modified magnetic pressure balance
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, pi
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

setup_style()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# --- Left panel: delta^2 W stability map in (beta, q) space ---

beta = np.linspace(0.01, 2.0, 300)
q = np.linspace(0.5, 5.0, 300)
BETA, Q = np.meshgrid(beta, q)

# Simplified stability model for a tokamak-like equilibrium:
# Kink instability: unstable when q < 1 (m=1 kink)
# Ballooning instability: unstable when beta > beta_crit(q)
# Suydam criterion: local interchange stability

# Classical delta^2 W model (simplified):
# Stabilising: magnetic shear + compression
# Destabilising: pressure gradient + bad curvature
# Rough model: delta^2 W ~ A(q) - B(q)*beta

# For illustration: stability boundary is roughly beta_crit ~ alpha * (q - 1)
# for q > 1, and always unstable for q < 1
alpha_cl = 0.8
delta2W_classical = alpha_cl * (Q - 1.0) - BETA * 0.5
delta2W_classical[Q < 1.0] = -1.0  # kink unstable

# Relativistic correction: enthalpy effects reduce effective beta threshold
# by factor (1 + beta/(8*pi))^{-1} approximately
v_A_over_c = 0.3  # representative for compact objects
rel_correction = 1.0 / (1.0 + v_A_over_c**2)
delta2W_rel = alpha_cl * (Q - 1.0) * rel_correction - BETA * 0.5 * (1 + v_A_over_c**2)
delta2W_rel[Q < 1.0] = -1.0

# Custom colormap: red (unstable) to blue (stable)
cmap_stability = LinearSegmentedColormap.from_list(
    'stability', ['#F44336', '#FFEB3B', '#4CAF50', '#2196F3'], N=256)

# Classical
im1 = ax1.contourf(BETA, Q, delta2W_classical, levels=np.linspace(-1, 1, 21),
                    cmap=cmap_stability, extend='both')
ax1.contour(BETA, Q, delta2W_classical, levels=[0], colors='k', linewidths=2.5)

ax1.axhline(1.0, color='white', ls='--', lw=1.0, alpha=0.7)
ax1.text(1.5, 1.05, 'q = 1 (kink)', fontsize=9, color='white')

ax1.set_xlabel(r'Plasma $\beta = 8\pi p / B^2$')
ax1.set_ylabel(r'Safety factor $q$')
ax1.set_title(r'$\delta^2 W$ stability map (Newtonian)')
cb1 = fig.colorbar(im1, ax=ax1, shrink=0.85, label=r'$\delta^2 W$ (arb. units)')

# Mark stable/unstable regions
ax1.text(0.3, 3.5, 'STABLE', fontsize=12, color='white', fontweight='bold',
         ha='center')
ax1.text(1.5, 2.0, 'UNSTABLE', fontsize=12, color='white', fontweight='bold',
         ha='center')

# Relativistic
im2 = ax2.contourf(BETA, Q, delta2W_rel, levels=np.linspace(-1, 1, 21),
                    cmap=cmap_stability, extend='both')
ax2.contour(BETA, Q, delta2W_rel, levels=[0], colors='k', linewidths=2.5)
# Also show classical boundary for comparison
ax2.contour(BETA, Q, delta2W_classical, levels=[0], colors='white',
            linewidths=1.5, linestyles='--')

ax2.axhline(1.0, color='white', ls='--', lw=1.0, alpha=0.7)
ax2.text(1.5, 1.05, 'q = 1 (kink)', fontsize=9, color='white')

ax2.set_xlabel(r'Plasma $\beta = 8\pi p / B^2$')
ax2.set_ylabel(r'Safety factor $q$')
ax2.set_title(r'$\delta^2 W$ stability map (Relativistic, $v_A/c = 0.3$)')
cb2 = fig.colorbar(im2, ax=ax2, shrink=0.85, label=r'$\delta^2 W$ (arb. units)')

ax2.text(0.2, 3.5, 'STABLE', fontsize=12, color='white', fontweight='bold',
         ha='center')
ax2.text(1.2, 2.5, 'UNSTABLE', fontsize=12, color='white', fontweight='bold',
         ha='center')
ax2.text(1.0, 4.0, 'Dashed: classical\nboundary', fontsize=8, color='white',
         ha='center', style='italic')

fig.tight_layout()
fig.savefig(os.path.join(os.path.dirname(__file__), 'fig_delta2W_stability_map.pdf'))
fig.savefig(os.path.join(os.path.dirname(__file__), 'fig_delta2W_stability_map.png'))
print("Saved plots/ch14/fig_delta2W_stability_map.pdf and .png")
plt.close(fig)
