#!/usr/bin/env python3
"""
Agent 33: Viscous spiral flow in accretion: Re-Ta parameter space.

Shows the stability boundary in the (Re, Ta) parameter space for
spiral Poiseuille-Couette flow, comparing classical and relativistic
(BDNK causal) predictions relevant to accretion column flows.

Produces: plots/ch8/fig_spiral_Re_Ta.pdf
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# Classical critical Taylor number vs Reynolds number (from Table XL)
# T_c increases with Re; approximate functional form
Re_vals = np.array([0, 5, 10, 20, 40, 60, 80, 100])
Tc_class = np.array([1715, 1748, 1793, 2078, 3881, 6424, 8750, 10876])

# Interpolate for smooth curves
Re_fine = np.linspace(0, 120, 500)
from numpy.polynomial import polynomial as P
coeffs = np.polyfit(Re_vals, Tc_class, 4)
Tc_interp = np.polyval(coeffs, Re_fine)
Tc_interp = np.maximum(Tc_interp, 1700)

# BDNK causality parameter values
T_vals = [0, 1e-4, 1e-2, 1e-1]
labels = [r'Classical ($\mathcal{T} = 0$)',
          r'$\mathcal{T} = 10^{-4}$',
          r'$\mathcal{T} = 10^{-2}$',
          r'$\mathcal{T} = 10^{-1}$ (rel. accretion)']
colors = [COLORS['classical'], '#66BB6A', COLORS['accretion'], COLORS['relativistic']]
styles = ['-', '-.', '--', ':']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

# Left panel: Stability boundaries in Re-Ta space
for i, T_bdnk in enumerate(T_vals):
    # BDNK correction: T_c increases with T_bdnk
    correction = 1.0 + T_bdnk * (np.pi**2 + 9.87)**2 * 0.01
    Tc_rel = Tc_interp * correction
    ax1.plot(Re_fine, Tc_rel, color=colors[i], ls=styles[i], lw=2.0,
             label=labels[i])

ax1.fill_between(Re_fine, Tc_interp, 2e4, alpha=0.05, color='green')
ax1.fill_between(Re_fine, 0, Tc_interp, alpha=0.05, color='red')
ax1.text(60, 2000, 'STABLE', fontsize=11, color='green', alpha=0.6)
ax1.text(60, 12000, 'UNSTABLE', fontsize=11, color='red', alpha=0.6)

ax1.set_xlabel(r'Reynolds number Re $= V_m d / \nu$')
ax1.set_ylabel(r'Taylor number $\mathscr{T}$')
ax1.set_title(r'Spiral Poiseuille--Couette stability ($\mu > 0$)')
ax1.legend(fontsize=9.5, loc='upper left')
ax1.set_xlim(0, 120)
ax1.set_ylim(0, 15000)

# Right panel: Critical Ta vs BDNK parameter for fixed Re
T_bdnk_arr = np.logspace(-6, 0, 300)
Re_fixed = [0, 10, 40, 100]
cmap = plt.cm.copper(np.linspace(0.2, 0.9, len(Re_fixed)))

for j, Re_val in enumerate(Re_fixed):
    Tc0 = np.polyval(coeffs, Re_val)
    Tc0 = max(Tc0, 1700)
    # T_c(T_bdnk) ~ T_c0 * (1 + T_bdnk * delta)
    delta = (np.pi**2 + 9.87)**2 * 0.01
    Tc_bdnk = Tc0 * (1 + T_bdnk_arr * delta)
    ax2.loglog(T_bdnk_arr, Tc_bdnk, color=cmap[j], lw=2.0,
               label=rf'Re $= {Re_val}$')

ax2.set_xlabel(r'BDNK causality parameter $\mathcal{T}$')
ax2.set_ylabel(r'Critical $\mathscr{T}_c$')
ax2.set_title('Effect of causal viscosity on stability')
ax2.legend(fontsize=10)
ax2.set_xlim(1e-6, 1)
ax2.set_ylim(1e3, 1e6)

# Annotate astrophysical regimes
ax2.axvspan(1e-2, 1, alpha=0.1, color=COLORS['accretion'])
ax2.text(0.1, 2e3, 'Relativistic\naccretion', fontsize=9,
         color=COLORS['accretion'], ha='center')

fig.suptitle('Viscous Spiral Flow in Accretion: Re--Ta Parameter Space',
             fontsize=13, y=1.02)
fig.tight_layout()
fig.savefig(os.path.join(os.path.dirname(__file__), 'fig_spiral_Re_Ta.pdf'))
fig.savefig(os.path.join(os.path.dirname(__file__), 'fig_spiral_Re_Ta.png'))
print("Saved plots/ch8/fig_spiral_Re_Ta.pdf")
