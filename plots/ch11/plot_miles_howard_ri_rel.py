#!/usr/bin/env python3
"""
Relativistic Miles-Howard Richardson number for M87 and Cen A jets.

The relativistic Richardson number is J_rel = J_class / Gamma^4.
The Miles-Howard theorem requires J_rel >= 1/4 for stability.

This plot shows:
  Left: J_rel vs z/d across the shear layer for different Gamma_0
  Right: Critical shear layer width d_crit vs Gamma for M87 and Cen A parameters

References:
    - Hardee (2000), ApJ 533, 176
    - Lobanov & Zensus (2001), Science 294, 128
    - Perucho et al. (2005), A&A 443, 863
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Left panel: J_rel(z) across the shear layer ---
z_d = np.linspace(-3, 3, 500)  # z/d

# Velocity profile: U = U0 * tanh(z/d), so dU/dz = U0/d * sech^2(z/d)
# Density: w = w0 * exp(-beta z), so dw/dz = -beta * w
# Lorentz factor: Gamma(z) = 1/sqrt(1 - (U0 tanh(z/d))^2/c^2)

# J_rel = g * beta * d^2 / (Gamma^4 * U0^2) evaluated locally
# For the tanh profile with local Gamma:
# J_rel(z) = J_class * cosh^4(z/d) / Gamma(z)^4

# Parameters: beta*d = 0.3 (moderate stratification)
beta_d = 0.3  # beta * d

Gamma0_values = [1.0, 2.0, 5.0, 10.0]
colors_list = [COLORS['classical'], COLORS['bdnk'],
               COLORS['relativistic'], COLORS['jet']]
lstyles = ['-', '--', '-.', ':']

for i, G0 in enumerate(Gamma0_values):
    Ms = np.sqrt(1.0 - 1.0/G0**2) if G0 > 1 else 0.0
    U_profile = Ms * np.tanh(z_d)
    Gamma_local = 1.0 / np.sqrt(1.0 - U_profile**2 + 1e-15)

    # dU/dz normalised: (1/d) * Ms * sech^2(z/d)
    dUdz = Ms / np.cosh(z_d)**2

    # J_rel(z) = g * beta / (w * Gamma^4 * (dU/dz)^2)
    # In normalised form: J_rel = beta_d / (Gamma_local^4 * (Ms * sech^2)^2)
    # Avoid division by zero at edges
    with np.errstate(divide='ignore', invalid='ignore'):
        J_rel = beta_d * np.cosh(z_d)**4 / (Gamma_local**4 * Ms**2 + 1e-30)

    J_rel = np.clip(J_rel, 0, 5)

    label = r'$\Gamma_0 = {:.0f}$'.format(G0) if G0 > 1 else r'Classical ($\Gamma_0=1$)'
    ax1.plot(z_d, J_rel, lstyles[i], color=colors_list[i],
             linewidth=2.0, label=label)

ax1.axhline(y=0.25, color='k', ls='--', linewidth=1.5, alpha=0.7)
ax1.text(-2.8, 0.30, r'$J_{\rm rel} = 1/4$ (Miles-Howard)', fontsize=10,
         fontstyle='italic')
ax1.set_xlabel(r'$z / d$')
ax1.set_ylabel(r'$J_{\rm rel}(z)$')
ax1.set_title('Relativistic Richardson number across shear layer')
ax1.legend(loc='upper right', frameon=True)
ax1.set_xlim(-3, 3)
ax1.set_ylim(0, 3)
ax1.grid(True, ls=':', alpha=0.4)

# --- Right panel: Stability diagram for M87 and Cen A ---
Gamma_range = np.linspace(1.1, 30, 300)

# Critical condition: J_rel = 1/4 => d_crit = sqrt(Gamma^4 * U0^2 / (4 g beta))
# Normalise: d_crit / d_0 where d_0 = sqrt(U0^2 / (4 g beta)) at Gamma=1
# Then d_crit/d_0 = Gamma^2 * beta_jet(Gamma)
# where beta_jet = sqrt(1 - 1/Gamma^2)

beta_v = np.sqrt(1.0 - 1.0/Gamma_range**2)
d_crit_norm = Gamma_range**2 * beta_v

ax2.semilogy(Gamma_range, d_crit_norm, '-', color=COLORS['relativistic'],
             linewidth=2.5, label=r'$d_{\rm crit}/d_0 = \Gamma^2 \beta$')

# Fill stability regions
ax2.fill_between(Gamma_range, d_crit_norm, 1e4,
                 color=COLORS['bdnk'], alpha=0.1)
ax2.fill_between(Gamma_range, 0.01, d_crit_norm,
                 color=COLORS['jet'], alpha=0.1)
ax2.text(15, 1000, 'Stable\n' + r'($J_{\rm rel} > 1/4$)',
         fontsize=11, ha='center', color=COLORS['bdnk'])
ax2.text(5, 0.5, 'Unstable\n' + r'($J_{\rm rel} < 1/4$)',
         fontsize=11, ha='center', color=COLORS['jet'])

# Mark M87 and Cen A
# M87: Gamma ~ 6, observed shear layer width ~ 2-3 jet radii
# Cen A: Gamma ~ 3, broader shear layer
sources = {'M87': (6.0, 50), 'Cen A': (3.0, 8)}
for name, (G, d_obs) in sources.items():
    ax2.plot(G, d_obs, 'o', color=COLORS['data'], markersize=12,
             markeredgecolor='k', markeredgewidth=1.0, zorder=5)
    ax2.annotate(name, (G, d_obs), textcoords='offset points',
                 xytext=(10, 5), fontsize=11, fontweight='bold')

ax2.set_xlabel(r'Jet Lorentz factor $\Gamma$')
ax2.set_ylabel(r'$d_{\rm crit} / d_0$')
ax2.set_title('KH stability boundary for jet shear layers')
ax2.legend(loc='lower right', frameon=True)
ax2.set_xlim(1, 30)
ax2.set_ylim(0.1, 5000)
ax2.grid(True, ls=':', alpha=0.4, which='both')

fig.tight_layout()
outdir = os.path.dirname(__file__)
fig.savefig(os.path.join(outdir, 'fig_miles_howard_ri_rel.pdf'))
fig.savefig(os.path.join(outdir, 'fig_miles_howard_ri_rel.png'))
print('Saved plots/ch11/fig_miles_howard_ri_rel.pdf and .png')
plt.close(fig)
