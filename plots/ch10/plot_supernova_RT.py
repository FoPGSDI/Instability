#!/usr/bin/env python3
"""
Supernova RT instability: shock-driven RT in core-collapse supernovae.
Growth rate vs density ratio for various relativistic corrections.

Application: In core-collapse supernovae, the stalled accretion shock
decelerates through composition interfaces (Si/O, O/He), creating
conditions for RT instability. The relativistic enthalpy correction
modifies the effective Atwood number when the post-shock matter is hot.

Reference: Couch & Ott (2015), Muller+ (2012), Chandrasekhar Ch X §90-92.
"""
import sys; sys.path.insert(0, '/data/haiyangw/claude/Instability'); from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, G_cgs, M_sun
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# --- Parameters ---
# Density ratios across the shock / composition interface
density_ratio = np.linspace(1.01, 10.0, 500)  # rho_2 / rho_1

# Gravitational acceleration at shock radius ~150 km in a CCSN
R_shock = 1.5e7  # cm (150 km)
M_PNS = 1.4 * M_sun
g = G_cgs * M_PNS / R_shock**2  # ~ 1.2e12 cm/s^2

# Representative wavenumber (l~10 mode, k ~ l/R)
l_mode = 10
k = l_mode / R_shock

# Classical Atwood number
A_class = (density_ratio - 1.0) / (density_ratio + 1.0)

# Relativistic corrections for different post-shock temperatures
# xi = p / (rho c^2), the relativistic parameter
xi_values = [0.0, 0.05, 0.10, 0.20]
labels = [
    r'Classical ($\xi = 0$)',
    r'$\xi = 0.05$ (mild)',
    r'$\xi = 0.10$ (moderate)',
    r'$\xi = 0.20$ (hot post-shock)',
]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Left panel: Growth rate vs density ratio ---
for i, xi in enumerate(xi_values):
    # w = rho c^2 (1 + xi) for each fluid
    # Heavy fluid (post-shock, hot): w2 = rho2 * c^2 * (1 + xi)
    # Light fluid (pre-shock, cold): w1 = rho1 * c^2 * (1 + 0)
    # A_rel = (w2 - w1) / (w2 + w1)
    w2 = density_ratio * (1.0 + xi)
    w1 = 1.0
    A_rel = (w2 - w1) / (w2 + w1)

    sigma = np.sqrt(g * k * np.abs(A_rel))
    # Convert to per-millisecond for astrophysical relevance
    sigma_ms = sigma * 1e-3  # per ms

    color = ['#2196F3', '#4CAF50', '#FF9800', '#F44336'][i]
    ls = ['-', '--', '-.', ':'][i]
    ax1.plot(density_ratio, sigma_ms, ls, color=color, linewidth=2.0, label=labels[i])

ax1.set_xlabel(r'Density ratio $\rho_2 / \rho_1$', fontsize=14)
ax1.set_ylabel(r'Growth rate $\sigma$ [ms$^{-1}$]', fontsize=14)
ax1.set_title('RT growth rate in core-collapse supernovae', fontsize=14)
ax1.legend(loc='lower right', fontsize=10, frameon=True, edgecolor='0.7')
ax1.set_xlim(1, 10)
ax1.grid(True, linestyle=':', alpha=0.4)
ax1.text(0.05, 0.95, r'$R_{\rm shock} = 150\,\mathrm{km}$, $M_{\rm PNS} = 1.4\,M_\odot$',
         transform=ax1.transAxes, fontsize=10, va='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# --- Right panel: Atwood number comparison ---
for i, xi in enumerate(xi_values):
    w2 = density_ratio * (1.0 + xi)
    w1 = 1.0
    A_rel = (w2 - w1) / (w2 + w1)

    color = ['#2196F3', '#4CAF50', '#FF9800', '#F44336'][i]
    ls = ['-', '--', '-.', ':'][i]
    ax2.plot(density_ratio, A_rel, ls, color=color, linewidth=2.0, label=labels[i])

ax2.plot(density_ratio, A_class, 'k-', linewidth=1.0, alpha=0.3, label='Classical limit')
ax2.set_xlabel(r'Density ratio $\rho_2 / \rho_1$', fontsize=14)
ax2.set_ylabel(r'Atwood number $\mathcal{A}$', fontsize=14)
ax2.set_title('Classical vs relativistic Atwood number', fontsize=14)
ax2.legend(loc='lower right', fontsize=10, frameon=True, edgecolor='0.7')
ax2.set_xlim(1, 10)
ax2.set_ylim(0, 1)
ax2.grid(True, linestyle=':', alpha=0.4)

fig.tight_layout()
fig.savefig('/data/haiyangw/claude/Instability/plots/ch10/fig_supernova_RT.pdf')
fig.savefig('/data/haiyangw/claude/Instability/plots/ch10/fig_supernova_RT.png')
print("Saved fig_supernova_RT.pdf and fig_supernova_RT.png")
plt.close(fig)
