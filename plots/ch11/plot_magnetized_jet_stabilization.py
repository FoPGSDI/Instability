#!/usr/bin/env python3
"""
Magnetized jet stability: B-field stabilization threshold for the
relativistic Kelvin-Helmholtz instability.

From eq. (rel-11-R18), the KH instability is suppressed when:
    alpha1_rel * alpha2_rel * (U1 - U2)^2 <= (b1^2 + b2^2) / (4 pi (Gamma1^2 w1 + Gamma2^2 w2))

This defines a critical magnetic field strength (or equivalently a critical
magnetisation sigma = B^2/(4 pi w c^2)) above which the jet is stabilised.

References:
    - Mizuno, Hardee & Nishikawa (2007), ApJ 662, 835
    - Mizuno et al. (2011), ApJ 734, 19
    - Bodo et al. (2013), MNRAS 434, 3030
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Left panel: Critical magnetisation sigma_crit vs Gamma ---
Gamma = np.linspace(1.5, 50, 400)
beta_v = np.sqrt(1.0 - 1.0/Gamma**2)

# Density ratio eta = w_ambient / w_jet
eta_values = [0.01, 0.1, 0.5, 1.0]
labels = [r'$\eta = 0.01$', r'$\eta = 0.1$', r'$\eta = 0.5$', r'$\eta = 1.0$']
colors_list = [COLORS['jet'], COLORS['relativistic'], COLORS['bdnk'], COLORS['classical']]
lstyles = ['-', '--', '-.', ':']

for i, eta in enumerate(eta_values):
    # From stability criterion (rel-11-R18):
    # sigma_crit = alpha1_rel * alpha2_rel * V_rel^2 * (Gamma1^2 w1 + Gamma2^2 w2) / w
    # Simplified for jet (1) at rest, ambient (2) streaming:
    # With U1 = V_jet = beta*c, U2 = 0, w1 = w_jet, w2 = eta*w_jet
    # alpha1_rel = Gamma^2 / (Gamma^2 + eta), alpha2_rel = eta / (Gamma^2 + eta)
    # Stability when: alpha1 * alpha2 * beta^2 * c^2 <= v_A^2 (effective)
    # => sigma_crit = B^2/(4pi w c^2) = alpha1 * alpha2 * beta^2

    alpha1 = Gamma**2 / (Gamma**2 + eta)
    alpha2 = eta / (Gamma**2 + eta)

    sigma_crit = alpha1 * alpha2 * beta_v**2

    ax1.semilogy(Gamma, sigma_crit, lstyles[i], color=colors_list[i],
                 linewidth=2.0, label=labels[i])

# Mark typical magnetisation values
ax1.axhline(y=1.0, color='gray', ls=':', alpha=0.5)
ax1.text(45, 1.2, r'$\sigma = 1$', fontsize=10, color='gray')
ax1.axhline(y=0.01, color='gray', ls=':', alpha=0.5)
ax1.text(45, 0.012, r'$\sigma = 0.01$', fontsize=10, color='gray')

ax1.fill_between(Gamma, 0.001, 0.01, color=COLORS['jet'], alpha=0.08)
ax1.text(25, 0.004, 'Weakly\nmagnetised', fontsize=10, ha='center',
         color=COLORS['jet'], fontstyle='italic')

ax1.set_xlabel(r'Jet Lorentz factor $\Gamma_{\rm jet}$')
ax1.set_ylabel(r'Critical magnetisation $\sigma_{\rm crit}$')
ax1.set_title('B-field stabilisation threshold for KH modes')
ax1.legend(loc='lower right', frameon=True)
ax1.set_xlim(1.5, 50)
ax1.set_ylim(1e-4, 10)
ax1.grid(True, ls=':', alpha=0.4, which='both')

# --- Right panel: Growth rate vs sigma for fixed Gamma values ---
sigma_B = np.logspace(-4, 1, 400)  # magnetisation parameter

Gamma_fixed = [3, 10, 30]
colors_g = [COLORS['classical'], COLORS['relativistic'], COLORS['jet']]
lstyles_g = ['-', '--', '-.']
eta = 0.1  # fixed density ratio

for i, G in enumerate(Gamma_fixed):
    beta = np.sqrt(1.0 - 1.0/G**2)
    alpha1 = G**2 / (G**2 + eta)
    alpha2 = eta / (G**2 + eta)

    # Growth rate: sigma_growth ~ sqrt(alpha1 * alpha2 * beta^2 - sigma_B) / G^2
    # Normalised to k*c
    discriminant = alpha1 * alpha2 * beta**2 - sigma_B
    sigma_growth = np.sqrt(np.maximum(discriminant, 0)) / G**2

    ax2.loglog(sigma_B, sigma_growth + 1e-15, lstyles_g[i], color=colors_g[i],
               linewidth=2.0, label=r'$\Gamma = {:.0f}$'.format(G))

    # Mark critical sigma
    sig_c = alpha1 * alpha2 * beta**2
    ax2.axvline(x=sig_c, color=colors_g[i], ls=':', alpha=0.4)

ax2.set_xlabel(r'Magnetisation $\sigma = B^2 / (4\pi w c^2)$')
ax2.set_ylabel(r'Normalised growth rate $\sigma_{\rm KH} / (k\,c)$')
ax2.set_title(r'KH growth rate vs magnetic field strength ($\eta=0.1$)')
ax2.legend(loc='upper right', frameon=True)
ax2.set_xlim(1e-4, 10)
ax2.set_ylim(1e-8, 0.1)
ax2.grid(True, ls=':', alpha=0.4, which='both')

# Annotate stabilised region
ax2.axvspan(0.1, 10, color=COLORS['bdnk'], alpha=0.05)
ax2.text(1.0, 1e-7, 'Magnetically\nstabilised', fontsize=10,
         ha='center', color=COLORS['bdnk'], fontstyle='italic')

fig.tight_layout()
outdir = os.path.dirname(__file__)
fig.savefig(os.path.join(outdir, 'fig_magnetized_jet_stabilization.pdf'))
fig.savefig(os.path.join(outdir, 'fig_magnetized_jet_stabilization.png'))
print('Saved plots/ch11/fig_magnetized_jet_stabilization.pdf and .png')
plt.close(fig)
