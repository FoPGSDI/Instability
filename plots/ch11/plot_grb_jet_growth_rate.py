#!/usr/bin/env python3
"""
GRB jet stability: KH growth rate sigma vs Lorentz factor Gamma
for structured jets with angular profiles.

For a structured GRB jet, the growth rate of KH modes depends on the
local Lorentz factor and the jet structure (top-hat vs Gaussian).

Key results:
  - Incompressible growth rate: sigma = k V0 Gamma_0 (in jet frame)
  - Lab-frame growth rate: sigma_lab ~ k c_s / Gamma^2
  - Compressible stabilisation at V0 > c_s / sqrt(1 + c_s^2/c^2)

References:
    - Aloy et al. (2000), ApJ 528, L85
    - Zhang, Woosley & MacFadyen (2003), ApJ 586, 356
    - Morsony, Lazzati & Begelman (2007), ApJ 665, 569
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Left panel: Growth rate vs Gamma for different jet structures ---
Gamma = np.logspace(0.3, 3, 400)  # 2 to 1000

# Sound speed in units of c
cs_hot = 1.0/np.sqrt(3)  # ultra-relativistic gas (Gamma_ad = 4/3)
cs_cold = 0.1  # cold jet

# Lab-frame KH growth rate (normalised): sigma_lab / (k c) ~ cs/c / Gamma^2
# with compressible stabilisation cutoff at Gamma > Gamma_stab

def sigma_lab(Gamma, cs):
    """Lab-frame KH growth rate normalised to k*c."""
    beta = np.sqrt(1.0 - 1.0/Gamma**2)
    # Compressible stabilisation: V0 > cs / sqrt(1 + cs^2)
    V0 = beta  # in units of c
    V_stab = cs / np.sqrt(1.0 + cs**2)
    # Growth rate with smooth cutoff
    sigma = cs * np.ones_like(Gamma) / Gamma**2
    # Apply compressible suppression
    suppression = np.exp(-((V0 - V_stab)/0.1)**2 * (V0 > V_stab).astype(float))
    sigma *= np.where(V0 < V_stab, 1.0, suppression)
    return sigma

# Top-hat jet
sig_hot = sigma_lab(Gamma, cs_hot)
sig_cold = sigma_lab(Gamma, cs_cold)

ax1.loglog(Gamma, sig_hot, '-', color=COLORS['jet'], linewidth=2.5,
           label=r'Hot jet ($c_s = c/\sqrt{3}$)')
ax1.loglog(Gamma, sig_cold, '--', color=COLORS['classical'], linewidth=2.5,
           label=r'Cold jet ($c_s = 0.1\,c$)')

# Gaussian structured jet: effective Gamma varies, weight by structure
# sigma_eff ~ integral of sigma(Gamma(theta)) * f(theta) dtheta
theta_c = 0.1  # core angle
theta = np.linspace(0, 0.5, 100)
for Gcore, ls, clr, lbl in [(100, '-.', COLORS['relativistic'],
                               r'Structured ($\Gamma_{\rm core}=100$)'),
                              (300, ':', COLORS['bdnk'],
                               r'Structured ($\Gamma_{\rm core}=300$)')]:
    # Gaussian structure: Gamma(theta) = 1 + (Gcore-1) * exp(-theta^2/(2*theta_c^2))
    Gamma_struct = 1.0 + (Gcore - 1.0) * np.exp(-theta**2 / (2*theta_c**2))
    sig_struct = sigma_lab(Gamma_struct, cs_hot)
    ax1.loglog(Gamma_struct, sig_struct, ls, color=clr, linewidth=2.0,
               label=lbl)

# Reference slopes
Gamma_ref = np.array([10, 300])
ax1.loglog(Gamma_ref, 0.3 * Gamma_ref**(-2.0), ':', color='gray',
           linewidth=1, alpha=0.6)
ax1.text(50, 3e-4, r'$\propto \Gamma^{-2}$', fontsize=11, color='gray',
         rotation=-35)

# Mark GRB regime
ax1.axvspan(100, 1000, color=COLORS['data'], alpha=0.06)
ax1.text(200, 0.02, 'GRB\nregime', fontsize=11, color=COLORS['data'],
         ha='center', fontstyle='italic')

ax1.set_xlabel(r'Lorentz factor $\Gamma$')
ax1.set_ylabel(r'$\sigma_{\rm lab} / (k\,c)$')
ax1.set_title('KH growth rate for GRB jet structures')
ax1.legend(loc='upper right', frameon=True, fontsize=10)
ax1.set_xlim(2, 1000)
ax1.set_ylim(1e-7, 1)
ax1.grid(True, ls=':', alpha=0.4, which='both')

# --- Right panel: Stability map in (Gamma, cs/c) plane ---
Gamma_2d = np.logspace(0.3, 3, 300)
cs_2d = np.linspace(0.01, 0.9, 300)
GG, CC = np.meshgrid(Gamma_2d, cs_2d)

# Compressible stabilisation boundary: beta = cs / sqrt(1 + cs^2)
beta_2d = np.sqrt(1.0 - 1.0/GG**2)
V_stab_2d = CC / np.sqrt(1.0 + CC**2)

# Growth rate proxy: sigma ~ cs / Gamma^2 * (1 if beta < V_stab else exp(-...))
sigma_2d = CC / GG**2
sigma_2d[beta_2d > V_stab_2d] *= 0.01  # strong suppression

im = ax2.pcolormesh(GG, CC, np.log10(sigma_2d + 1e-10),
                    cmap='inferno_r', shading='auto', vmin=-7, vmax=0)
cbar = fig.colorbar(im, ax=ax2, label=r'$\log_{10}(\sigma_{\rm lab}/kc)$')

# Stability boundary curve
Gamma_bnd = np.logspace(0.3, 3, 500)
for cs_val, clr, lbl in [(1/np.sqrt(3), 'cyan', r'$c_s = c/\sqrt{3}$'),
                           (0.1, 'lime', r'$c_s = 0.1\,c$')]:
    # beta(Gamma) = V_stab => Gamma_stab
    V_s = cs_val / np.sqrt(1.0 + cs_val**2)
    Gamma_stab = 1.0 / np.sqrt(1.0 - V_s**2)
    ax2.axvline(x=Gamma_stab, color=clr, ls='--', linewidth=1.5, alpha=0.8)
    ax2.text(Gamma_stab * 1.1, 0.85, lbl, fontsize=9, color=clr, rotation=90)

ax2.set_xlabel(r'Lorentz factor $\Gamma$')
ax2.set_ylabel(r'$c_s / c$')
ax2.set_title('KH stability map: structured GRB jets')
ax2.set_xscale('log')
ax2.set_xlim(2, 1000)
ax2.set_ylim(0.01, 0.9)
ax2.grid(True, ls=':', alpha=0.3, which='both')

fig.tight_layout()
outdir = os.path.dirname(__file__)
fig.savefig(os.path.join(outdir, 'fig_grb_jet_growth_rate.pdf'))
fig.savefig(os.path.join(outdir, 'fig_grb_jet_growth_rate.png'))
print('Saved plots/ch11/fig_grb_jet_growth_rate.pdf and .png')
plt.close(fig)
