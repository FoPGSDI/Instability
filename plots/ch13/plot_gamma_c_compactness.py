#!/usr/bin/env python3
"""
Plot critical adiabatic index gamma_c vs compactness C = GM/(Rc^2)
for white dwarfs, neutron stars, and supermassive stars.

The Chandrasekhar (1964) result:
    gamma_c = 4/3 + kappa * GM/(Rc^2)
with kappa ~ 1.81 for a uniform-density sphere (kappa = 38/21).

Different stellar objects occupy different compactness ranges:
  - White dwarfs:       C ~ 1e-4 to 1e-3
  - Neutron stars:      C ~ 0.1 to 0.35
  - Supermassive stars: C ~ 1e-6 to 1e-3

The plot also shows the effective gamma for each class, illustrating
how GR destabilises marginally stable Newtonian configurations.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, G_cgs, M_sun, R_sun
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

setup_style()

# Compactness parameter
C_full = np.linspace(0, 0.44, 1000)
C_log = np.logspace(-6, np.log10(0.44), 1000)

kappa_uniform = 38.0 / 21.0  # ~1.81 for uniform density

# Different structure-dependent kappa values
kappas = {
    'Uniform density': (kappa_uniform, '-', '#2196F3'),
    'Polytrope n=3 (WD)': (2.25, '--', '#4CAF50'),
    'Realistic NS EOS': (1.5, '-.', '#F44336'),
}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# --- Left panel: gamma_c vs compactness (linear scale) ---
ax1.axhline(4.0/3.0, color='gray', ls=':', lw=1.2,
            label=r'Newtonian $\gamma_c = 4/3$')

for label, (kap, ls, col) in kappas.items():
    gamma_c = 4.0/3.0 + kap * C_full
    ax1.plot(C_full, gamma_c, ls=ls, color=col, lw=2.0, label=label)

# Shade stellar compactness ranges
ax1.axvspan(1e-4, 2e-3, alpha=0.10, color='#4CAF50')
ax1.text(1e-3, 1.80, 'WD', fontsize=10, ha='center', color='#4CAF50',
         fontweight='bold')

ax1.axvspan(0.10, 0.35, alpha=0.10, color='#F44336')
ax1.text(0.225, 1.80, 'NS', fontsize=10, ha='center', color='#F44336',
         fontweight='bold')

# Effective gamma for radiation-dominated SMS
ax1.axhline(4.0/3.0, color='#FF9800', ls='--', lw=1.0, alpha=0.5)
ax1.annotate('SMS: radiation-dominated\n' + r'$\gamma_{\rm eff} \approx 4/3$',
             xy=(0.005, 4.0/3.0), xytext=(0.08, 1.40),
             arrowprops=dict(arrowstyle='->', color='#FF9800'),
             fontsize=9, color='#FF9800')

# Buchdahl limit
ax1.axvline(4.0/9.0, color='k', ls='--', lw=0.8, alpha=0.4)
ax1.text(4.0/9.0 - 0.01, 1.82, 'Buchdahl', fontsize=8, ha='right',
         color='0.4', rotation=90)

ax1.set_xlabel(r'Compactness $\mathcal{C} = GM/(Rc^2)$')
ax1.set_ylabel(r'Critical adiabatic index $\gamma_c$')
ax1.set_title(r'GR destabilisation: $\gamma_c$ vs compactness')
ax1.legend(loc='upper left', fontsize=9)
ax1.set_xlim(0, 0.44)
ax1.set_ylim(1.30, 1.85)
ax1.grid(True, ls=':', alpha=0.3)

# --- Right panel: Critical mass as function of gamma for different compactness ---
# For a star near marginal stability, M_max ~ (gamma - 4/3)^alpha * f(EOS)
# Show schematic mass-radius trajectories

gamma_arr = np.linspace(1.334, 2.5, 500)

# Newtonian: stable for gamma > 4/3, M_max = Chandrasekhar limit when gamma=4/3
# GR: stable for gamma > gamma_c(C)

compactness_vals = [0.0, 0.001, 0.01, 0.1, 0.2, 0.3]
colors_right = plt.cm.plasma(np.linspace(0.1, 0.9, len(compactness_vals)))

for Cval, col in zip(compactness_vals, colors_right):
    gc = 4.0/3.0 + kappa_uniform * Cval
    # Schematic: omega^2 proportional to (gamma - gamma_c)
    omega2 = (gamma_arr - gc)
    omega2_norm = omega2 / np.max(np.abs(omega2))
    lbl = r'$\mathcal{C}=' + f'{Cval:.3f}' + '$' if Cval > 0 else 'Newtonian'
    ax2.plot(gamma_arr, omega2_norm, color=col, lw=1.8, label=lbl)

ax2.axhline(0, color='k', lw=0.8)
ax2.axvline(4.0/3.0, color='gray', ls=':', lw=1.0, alpha=0.5)
ax2.text(4.0/3.0 + 0.01, -0.8, r'$\gamma = 4/3$', fontsize=9, color='gray')

ax2.fill_between(gamma_arr, -1.1, 0, alpha=0.05, color='red')
ax2.text(1.40, -0.5, 'UNSTABLE', fontsize=10, color='red', alpha=0.6,
         fontweight='bold')
ax2.text(2.0, 0.5, 'STABLE', fontsize=10, color='green', alpha=0.6,
         fontweight='bold')

ax2.set_xlabel(r'Adiabatic index $\gamma$')
ax2.set_ylabel(r'Normalised $\omega^2$ (stability parameter)')
ax2.set_title(r'Stability boundary shift with compactness')
ax2.legend(loc='lower right', fontsize=8, ncol=2)
ax2.set_xlim(1.334, 2.5)
ax2.set_ylim(-1.1, 1.1)
ax2.grid(True, ls=':', alpha=0.3)

fig.tight_layout()
fig.savefig(os.path.join(os.path.dirname(__file__), 'fig_gamma_c_compactness.pdf'))
fig.savefig(os.path.join(os.path.dirname(__file__), 'fig_gamma_c_compactness.png'))
print("Saved plots/ch13/fig_gamma_c_compactness.pdf and .png")
plt.close(fig)
