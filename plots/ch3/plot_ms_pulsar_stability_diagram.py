#!/usr/bin/env python3
"""
Agent 9: Critical Ra(Ta) stability diagram for millisecond pulsars.

Plots the stability boundary in the (Ta, Ra) plane with:
  - Classical stationary convection curve
  - Classical overstable curve (Pr = 0.001)
  - Relativistic corrections for NS enthalpy ratios h/(rho*c^2) = 1.2, 1.5, 2.0
  - Marks the regime Ta ~ 10^12 relevant to millisecond pulsars

Quantitative estimates:
  Omega = 2*pi*716 Hz (fastest known pulsar, PSR J1748-2446ad)
  d ~ 1 km (convective layer depth)
  nu_eff ~ 1 cm^2/s (nuclear viscosity)
  => Ta = 4*Omega^2*d^4/nu^2 ~ 8e25 (extremely large)

For realistic nuclear matter: nu ~ 1-100 cm^2/s, kappa ~ 10^4-10^6 cm^2/s
  => Ta ~ 10^12 - 10^18 depending on assumptions
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS
setup_style()

import numpy as np
import matplotlib.pyplot as plt

# --- Exact solution for two free boundaries (Chandrasekhar) ---
def Ra_stationary_free(Ta, n=1):
    """Critical Ra for stationary convection, two free boundaries.
    Ra = min_a [(n^2 pi^2 + a^2)^3 + n^2 pi^2 Ta] / a^2
    """
    # For large Ta, a_min ~ (pi^2 Ta / 2)^{1/6}
    # Numerically minimise over a
    a2_vals = np.logspace(-1, 6, 5000)
    Ra_best = np.full_like(Ta, np.inf)
    for a2 in a2_vals:
        Ra_trial = ((n**2 * np.pi**2 + a2)**3 + n**2 * np.pi**2 * Ta) / a2
        Ra_best = np.minimum(Ra_best, Ra_trial)
    return Ra_best

def Ra_overstable_free(Ta, Pr=0.001):
    """Critical Ra for overstability, two free boundaries, asymptotic formula.
    For Pr << 1: Ra_over ~ 2*pi^4*(1+x)^3/x with modified x.
    Large-Ta asymptote: Ra ~ 6*Pr^{4/3}/(1+Pr)^{1/3} * (pi^2*Ta/2)^{2/3}
    """
    # Asymptotic for large Ta
    Ra_asymp = 6.0 * Pr**(4.0/3.0) / (1.0 + Pr)**(1.0/3.0) * \
               (0.5 * np.pi**2 * Ta)**(2.0/3.0)
    # Low-Ta floor: need Ta > some threshold for overstability
    # Threshold: Ta_min ~ pi^4 * (1+Pr)^3 / (1-Pr)
    Ta_thresh = np.pi**4 * (1.0 + Pr)**3 / max(1.0 - Pr, 1e-10)
    Ra_asymp[Ta < Ta_thresh] = np.nan
    return Ra_asymp

# --- Taylor number range ---
Ta = np.logspace(4, 18, 1000)

# Classical curves
Ra_stat_cl = Ra_stationary_free(Ta)
Ra_over_cl = Ra_overstable_free(Ta, Pr=0.001)

# --- Relativistic curves ---
h_ratios = [1.0, 1.2, 1.5, 2.0]
labels_h = [r'Classical ($w/\rho c^2=1$)',
            r'$w/\rho c^2=1.2$',
            r'$w/\rho c^2=1.5$',
            r'$w/\rho c^2=2.0$ (core)']
colors_h = [COLORS['classical'], COLORS['bdnk'],
            COLORS['is'], COLORS['relativistic']]
ls_h = ['-', '--', '-.', ':']

fig, ax = plt.subplots(figsize=(10, 7))

for i, h_r in enumerate(h_ratios):
    # Relativistic Ta_rel = Ta * h_r^2 (enhanced effective Taylor number)
    Ta_rel = Ta * h_r**2
    # But we plot vs physical Ta on x-axis
    # Ra_stat uses Ta_rel in the formula
    Ra_stat_rel = Ra_stationary_free(Ta_rel)
    Ra_over_rel = Ra_overstable_free(Ta_rel, Pr=0.001)

    ax.loglog(Ta, Ra_stat_rel, ls_h[i], color=colors_h[i],
              linewidth=2.0, label=labels_h[i] + ' (stat.)')
    if i == 0 or i == 3:  # Only show overstable for classical and extreme
        ax.loglog(Ta, Ra_over_rel, ls_h[i], color=colors_h[i],
                  linewidth=1.2, alpha=0.6,
                  label=labels_h[i] + ' (overstab.)')

# --- Mark millisecond pulsar regime ---
# PSR J1748-2446ad: f = 716 Hz, Omega = 4498 rad/s
# With nu ~ 10 cm^2/s, d ~ 5e4 cm: Ta ~ 4*4498^2*(5e4)^4/10^2 ~ 5e26
# More conservative: nu ~ 100, d ~ 1e4: Ta ~ 4*4498^2*(1e4)^4/100^2 ~ 8e17
# Nuclear matter estimates span Ta ~ 10^12 to 10^18

ax.axvspan(1e12, 1e18, alpha=0.08, color=COLORS['neutron_star'],
           label='MS pulsar regime')
ax.axvline(1e14, color=COLORS['neutron_star'], ls=':', alpha=0.4)
ax.annotate('Millisecond\npulsar\nregime', xy=(3e14, 5e6),
            fontsize=11, color=COLORS['neutron_star'],
            ha='center', style='italic')

# Reference slopes
Ta_ref = np.logspace(12, 18, 100)
ax.loglog(Ta_ref, 8.696 * Ta_ref**(2.0/3.0), ':', color='gray',
          linewidth=1.0, alpha=0.5, label=r'$8.70\,\mathrm{Ta}^{2/3}$')

ax.set_xlabel(r'Physical Taylor number $\mathrm{Ta}$')
ax.set_ylabel(r'Critical Rayleigh number $\mathrm{Ra}_c$')
ax.set_title(r'Stability diagram: rotating convection in millisecond pulsars')
ax.legend(fontsize=8.5, loc='upper left', ncol=2, frameon=True)
ax.set_xlim(1e4, 1e18)
ax.set_ylim(1e3, 1e14)

# Add secondary axis with physical rotation rate
ax_top = ax.twiny()
nu_eff = 10.0  # cm^2/s representative
d = 1e4  # cm = 100 m
Ta_to_Omega = lambda Ta_val: np.sqrt(Ta_val) * nu_eff / (2.0 * d**2)
Omega_ticks = [1, 10, 100, 1e3, 1e4]
Ta_ticks_top = [(2.0 * Om * d**2 / nu_eff)**2 for Om in Omega_ticks]
ax_top.set_xscale('log')
ax_top.set_xlim(ax.get_xlim())
ax_top.set_xticks(Ta_ticks_top)
ax_top.set_xticklabels([f'{int(Om)}' for Om in Omega_ticks])
ax_top.set_xlabel(r'$\Omega$ (rad/s) for $\nu=10\,{\rm cm^2/s}$, $d=100\,{\rm m}$')

fig.tight_layout()
outdir = os.path.join(os.path.dirname(__file__))
fig.savefig(os.path.join(outdir, 'fig_ms_pulsar_stability.pdf'))
fig.savefig(os.path.join(outdir, 'fig_ms_pulsar_stability.png'))
print("Saved plots/ch3/fig_ms_pulsar_stability.pdf and .png")
plt.close(fig)
