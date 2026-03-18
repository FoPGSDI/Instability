#!/usr/bin/env python3
"""
Deep Research 2, Plot 1:
Critical Rayleigh number Ra_c(Ta) for realistic millisecond pulsar parameters.

Uses PSR J1748-2446ad (f_spin = 716 Hz), M = 1.4 M_sun, R = 12 km,
SLy nuclear EOS for enthalpy ratio xi = w/(rho c^2).
Compares Newtonian vs relativistic predictions.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, G_cgs, M_sun, pi
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

setup_style()

# ============================================================
# Physical parameters for PSR J1748-2446ad
# ============================================================
M_ns = 1.4 * M_sun            # g
R_ns = 12e5                    # cm (12 km)
f_spin = 716.0                 # Hz
Omega = 2 * pi * f_spin        # rad/s  ~4498 rad/s

# Surface gravity
g_ns = G_cgs * M_ns / R_ns**2  # cm/s^2  ~1.3e14

# SLy EOS at rho ~ 3 rho_nuc: enthalpy ratio
# xi = (epsilon + p) / (rho c^2) for nuclear matter
xi_SLy = 1.28                  # SLy at ~3 rho_nuc (Douchin & Haensel 2001)

# Transport coefficients (Flowers & Itoh 1976; Shternin & Yakovlev 2006)
nu_values = [1.0, 10.0, 100.0]  # cm^2/s  (range)
kappa_T = 1e5                   # cm^2/s  (thermal diffusivity)

# Convective layer depth
d_values = [1e3, 1e4, 1e5]     # cm (10m, 100m, 1km)
d_ref = 1e4                    # reference: 100 m

# ============================================================
# Newtonian and relativistic Taylor numbers
# ============================================================
def Ta_Newt(Omega, d, nu):
    """Classical Taylor number."""
    return 4.0 * Omega**2 * d**4 / nu**2

def Ta_rel(Omega, d, nu, xi):
    """Relativistic Taylor number: Ta_N * xi^2."""
    nu_eff = nu / xi  # nu_eff = eta_shear * c^2 / w = nu / xi
    return 4.0 * Omega**2 * d**4 / nu_eff**2

# ============================================================
# Critical Rayleigh number: asymptotic Ra_c ~ 8.6956 * Ta^{2/3}
# and exact solution from 2x^3 + 3x^2 = 1 + Ta/pi^4
# ============================================================
def Ra_c_exact(Ta_val):
    """Solve the exact free-boundary critical Ra(Ta) from
    2x^3 + 3x^2 = 1 + Ta/pi^4, then Ra = pi^4*(1+x)^3/x + pi^4*Ta/(pi^4*x).
    """
    T1 = Ta_val / pi**4
    # Solve 2x^3 + 3x^2 - 1 - T1 = 0 for x > 0
    coeffs = [2.0, 3.0, 0.0, -(1.0 + T1)]
    roots = np.roots(coeffs)
    # Pick the positive real root
    real_roots = [r.real for r in roots if abs(r.imag) < 1e-10 and r.real > 0]
    if len(real_roots) == 0:
        # fallback to asymptotic
        return 8.6956 * Ta_val**(2./3.)
    x = max(real_roots)
    Ra = pi**4 * (1 + x)**3 / x + Ta_val / x
    return Ra

def Ra_c_asymptotic(Ta_val):
    """Asymptotic formula: Ra_c = 3*(pi^2*Ta/2)^{2/3}."""
    return 3.0 * (0.5 * pi**2 * Ta_val)**(2./3.)

# ============================================================
# Generate curves
# ============================================================
Ta_range = np.logspace(0, 28, 500)

# Newtonian exact curve
Ra_Newt_exact = np.array([Ra_c_exact(T) for T in Ta_range])

# Relativistic exact curve (xi = 1.28 SLy)
# The curve shape is the same, just evaluated at Ta_rel instead of Ta_Newt
# But we plot both as functions of the PHYSICAL Taylor number Ta_phys = 4 Omega^2 d^4 / nu^2
# The relativistic curve uses Ta_rel = Ta_phys * xi^2
Ra_rel_exact = np.array([Ra_c_exact(T * xi_SLy**2) for T in Ta_range])

# Also show xi = 1.0 (Newtonian), 1.15 (APR soft), 1.28 (SLy), 1.45 (stiff)
xi_values = [1.0, 1.15, 1.28, 1.45]
xi_labels = [r'$\xi=1.00$ (Newtonian)',
             r'$\xi=1.15$ (APR)',
             r'$\xi=1.28$ (SLy)',
             r'$\xi=1.45$ (stiff EOS)']
xi_colors = [COLORS['classical'], '#8BC34A', COLORS['relativistic'], '#9C27B0']

fig, ax = plt.subplots(figsize=(10, 7))

for xi_val, label, color in zip(xi_values, xi_labels, xi_colors):
    Ra_curve = np.array([Ra_c_exact(T * xi_val**2) for T in Ta_range])
    lw = 2.5 if xi_val == 1.28 else 1.5
    ls = '-' if xi_val == 1.28 or xi_val == 1.0 else '--'
    ax.loglog(Ta_range, Ra_curve, color=color, lw=lw, ls=ls, label=label)

# Mark realistic MSP parameters
for nu_val, marker, ms in zip([1.0, 10.0, 100.0], ['o', 's', 'D'], [10, 9, 8]):
    Ta_phys = Ta_Newt(Omega, d_ref, nu_val)
    Ra_N = Ra_c_exact(Ta_phys)
    Ra_R = Ra_c_exact(Ta_phys * xi_SLy**2)

    ax.plot(Ta_phys, Ra_N, marker=marker, color=COLORS['classical'],
            ms=ms, zorder=5, markeredgecolor='k', markeredgewidth=0.5)
    ax.plot(Ta_phys, Ra_R, marker=marker, color=COLORS['relativistic'],
            ms=ms, zorder=5, markeredgecolor='k', markeredgewidth=0.5)

# Annotate the PSR J1748-2446ad region
Ta_msp_low = Ta_Newt(Omega, d_ref, 100.0)
Ta_msp_high = Ta_Newt(Omega, d_ref, 1.0)
ax.axvspan(Ta_msp_low, Ta_msp_high, alpha=0.08, color='grey',
           label=r'PSR J1748$-$2446ad ($d=100$ m)')

# Asymptotic line
ax.loglog(Ta_range, 8.6956 * Ta_range**(2./3.), 'k:', lw=0.8, alpha=0.5,
          label=r'$8.70\,\mathrm{Ta}^{2/3}$ asymptote')

# Add secondary x-axis: Omega for d=100m, nu=10
ax2 = ax.twiny()
ax2.set_xscale('log')
Ta_ticks = np.array([1e8, 1e12, 1e16, 1e20, 1e24, 1e28])
Omega_ticks = np.sqrt(Ta_ticks * 10.0**2 / (4.0 * (1e4)**4))
Omega_labels = [f'{O:.0e}' for O in Omega_ticks]
ax2.set_xlim(ax.get_xlim())
ax2.set_xlabel(r'$\Omega$ [rad/s] ($\nu=10$ cm$^2$/s, $d=100$ m)', fontsize=12)

# Quantify the correction
Ta_ref = Ta_Newt(Omega, d_ref, 10.0)
Ra_N_ref = Ra_c_exact(Ta_ref)
Ra_R_ref = Ra_c_exact(Ta_ref * xi_SLy**2)
correction_pct = (Ra_R_ref - Ra_N_ref) / Ra_N_ref * 100

ax.set_xlabel(r'Physical Taylor number $\mathrm{Ta} = 4\Omega^2 d^4/\nu^2$', fontsize=14)
ax.set_ylabel(r'Critical Rayleigh number $\mathrm{Ra}_c$', fontsize=14)
ax.set_title(r'Rotating convection: $\mathrm{Ra}_c(\mathrm{Ta})$ for realistic MSP (PSR J1748$-$2446ad)',
             fontsize=13)
ax.legend(loc='upper left', fontsize=10, framealpha=0.9)
ax.set_xlim(1e0, 1e28)
ax.set_ylim(1e1, 1e20)

# Add annotation for correction magnitude
ax.text(0.98, 0.15,
        f'Relativistic correction (SLy, $\\xi=1.28$):\n'
        f'$\\Delta\\mathrm{{Ra}}_c / \\mathrm{{Ra}}_c = {correction_pct:.1f}\\%$\n'
        f'at $\\mathrm{{Ta}} = {Ta_ref:.1e}$',
        transform=ax.transAxes, fontsize=10, ha='right', va='bottom',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), 'fig_msp_critical_Ra_realistic.pdf'))
plt.savefig(os.path.join(os.path.dirname(__file__), 'fig_msp_critical_Ra_realistic.png'))
print(f"Saved fig_msp_critical_Ra_realistic.pdf/png")
print(f"Reference Ta = {Ta_ref:.3e}, Ra_N = {Ra_N_ref:.3e}, Ra_R = {Ra_R_ref:.3e}")
print(f"Relativistic correction: {correction_pct:.1f}%")
