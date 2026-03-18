#!/usr/bin/env python3
"""
AGN jet Kelvin-Helmholtz instability: critical velocity for jet disruption
vs jet Lorentz factor Gamma_jet.

From eq. (rel-11-25), the critical relative velocity for KH onset is:
    V_rel^2 > (g/k) * (rho1 - rho2)(rho1 + gamma_rel^2 rho2) / (rho1 gamma_rel^2 rho2)

For ultra-relativistic jets the lab-frame growth rate scales as Gamma^{-2},
so there is a critical Gamma above which the jet survives disruption over
a given propagation length.

References:
    - Perucho et al. (2004), A&A 427, 415
    - Hardee (2007), ApJ 664, 26
    - Bodo et al. (2004), Phys. Rev. E 70, 036304
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# --- Parameters ---
Gamma_jet = np.linspace(1.01, 50, 500)
beta_jet = np.sqrt(1.0 - 1.0 / Gamma_jet**2)

# Density ratio eta = rho_ambient / rho_jet (enthalpy densities)
eta_values = [0.01, 0.1, 0.5, 1.0]
labels = [r'$\eta = 0.01$ (light jet)', r'$\eta = 0.1$',
          r'$\eta = 0.5$', r'$\eta = 1.0$ (matched)']
colors_list = [COLORS['jet'], COLORS['relativistic'],
               COLORS['bdnk'], COLORS['classical']]
lstyles = ['-', '--', '-.', ':']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Left panel: Critical velocity V_crit/c vs Gamma_jet ---
for i, eta in enumerate(eta_values):
    # From eq. (rel-11-25) in rest frame of ambient (U1=0):
    # V_crit^2 = (g/k) * (1 - eta)(1 + gamma_rel^2 eta) / (gamma_rel^2 eta)
    # Normalise to (g/k)=1, plot V_crit/c
    # For the jet: gamma_rel = Gamma_jet, rhohat1=1 (ambient), rhohat2=eta
    gamma_rel = Gamma_jet
    numerator = (1.0 - eta) * (1.0 + gamma_rel**2 * eta)
    denominator = gamma_rel**2 * eta
    V_crit_sq = numerator / denominator  # in units of g/k
    # Normalise so V_crit/c = sqrt(V_crit_sq) * sqrt(g/(k c^2))
    # For a dimensionless plot, show V_crit / sqrt(g/k)
    V_crit_norm = np.sqrt(np.clip(V_crit_sq, 0, None))

    ax1.semilogy(Gamma_jet, V_crit_norm, lstyles[i], color=colors_list[i],
                 linewidth=2.0, label=labels[i])

ax1.axhline(y=1.0, color='gray', ls=':', alpha=0.5, linewidth=1)
ax1.set_xlabel(r'Jet Lorentz factor $\Gamma_{\rm jet}$')
ax1.set_ylabel(r'$V_{\rm crit} / \sqrt{g/k}$')
ax1.set_title('Critical KH velocity vs jet Lorentz factor')
ax1.legend(loc='upper right', frameon=True)
ax1.set_xlim(1, 50)
ax1.set_ylim(0.01, 100)
ax1.grid(True, ls=':', alpha=0.4, which='both')

# --- Right panel: Lab-frame growth rate suppression ---
# sigma_lab ~ sigma_0 * Gamma^{-2} for the fundamental KH body mode
Gamma_arr = np.logspace(0, 2, 300)
sigma_norm = 1.0 / Gamma_arr**2  # normalised to classical value

ax2.loglog(Gamma_arr, sigma_norm, '-', color=COLORS['relativistic'],
           linewidth=2.5, label=r'$\sigma_{\rm lab}/\sigma_0 \propto \Gamma^{-2}$')

# Mark typical AGN jet values
agn_sources = {
    'M87': 6.0,
    '3C 273': 15.0,
    '3C 279': 30.0,
}
markers = ['o', 's', 'D']
for (name, G), mk in zip(agn_sources.items(), markers):
    sig = 1.0 / G**2
    ax2.plot(G, sig, mk, color=COLORS['data'], markersize=10,
             markeredgecolor='k', markeredgewidth=0.8, zorder=5)
    ax2.annotate(name, (G, sig), textcoords='offset points',
                 xytext=(8, 5), fontsize=10)

# Shaded disruption zone
ax2.axhspan(0.1, 2.0, color=COLORS['classical'], alpha=0.08)
ax2.text(1.2, 0.3, 'Disruption\nregime', fontsize=10, color=COLORS['classical'],
         fontstyle='italic')
ax2.axhspan(1e-4, 0.01, color=COLORS['bdnk'], alpha=0.08)
ax2.text(20, 0.002, 'Stable\npropagation', fontsize=10, color=COLORS['bdnk'],
         fontstyle='italic')

ax2.set_xlabel(r'Jet Lorentz factor $\Gamma_{\rm jet}$')
ax2.set_ylabel(r'$\sigma_{\rm lab} / \sigma_0$')
ax2.set_title(r'KH growth rate suppression: $\sigma \propto \Gamma^{-2}$')
ax2.legend(loc='upper right', frameon=True)
ax2.grid(True, ls=':', alpha=0.4, which='both')

fig.tight_layout()
outdir = os.path.dirname(__file__)
fig.savefig(os.path.join(outdir, 'fig_agn_jet_kh_critical.pdf'))
fig.savefig(os.path.join(outdir, 'fig_agn_jet_kh_critical.png'))
print('Saved plots/ch11/fig_agn_jet_kh_critical.pdf and .png')
plt.close(fig)
