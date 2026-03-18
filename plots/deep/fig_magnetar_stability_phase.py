#!/usr/bin/env python3
"""
Deep Research 2, Plot 2:
Stability phase diagram for magnetar magneto-convection in (B, T_gradient) space.

For B = 10^{14}, 10^{15}, 10^{16} G, computes Q_rel for each,
determines Ra_c(Q_rel), and identifies when magnetic stabilization
overcomes relativistic destabilization.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, G_cgs, M_sun, pi, k_B, m_p
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

setup_style()

# ============================================================
# Magnetar parameters
# ============================================================
M_ns = 1.4 * M_sun
R_ns = 12e5                    # cm
g_ns = G_cgs * M_ns / R_ns**2  # ~1.3e14 cm/s^2
rho_nuc = 2.8e14               # g/cm^3
rho_core = 3.0 * rho_nuc      # ~8.4e14 g/cm^3

# SLy EOS parameters
xi_SLy = 1.28                  # w/(rho c^2) = (eps+p)/(rho c^2)
w_0 = rho_core * c_cgs**2 * xi_SLy  # enthalpy density

# Transport coefficients
nu_shear = 10.0                # cm^2/s (kinematic viscosity)
eta_shear = rho_core * nu_shear  # dynamic shear viscosity (g/cm/s)
kappa_T = 1e5                  # cm^2/s (thermal diffusivity)
eta_mag = 1e3                  # cm^2/s (magnetic diffusivity)
alpha_th = 1e-4                # K^{-1} (thermal expansion coeff)

# Layer depth
d = 1e4                       # cm (100 m)

# Effective kinematic viscosity
nu_eff = eta_shear * c_cgs**2 / w_0  # = nu / xi

# ============================================================
# Relativistic Chandrasekhar number
# ============================================================
def Q_rel(B_gauss, d_cm, w_enth, nu_eff_val, eta_m):
    """Q_rel = B^2 d^2 / (4 pi * (w/c^2) * nu_eff * eta)."""
    return B_gauss**2 * d_cm**2 / (4.0 * pi * (w_enth / c_cgs**2) * nu_eff_val * eta_m)

def Q_class(B_gauss, d_cm, rho, nu_val, eta_m):
    """Classical Q = mu H^2 d^2 / (4 pi rho nu eta)."""
    return B_gauss**2 * d_cm**2 / (4.0 * pi * rho * nu_val * eta_m)

# ============================================================
# Critical Ra (free boundaries, exact)
# ============================================================
def Ra_c_from_Q(Q_val):
    """Exact free-boundary: Ra = (pi^2+a^2)/a^2 * [(pi^2+a^2)^2 + pi^2*Q].
    Minimize over a. Use cubic: 2x^3 + 3x^2 = 1 + Q/pi^2."""
    Q1 = Q_val / pi**2
    coeffs = [2.0, 3.0, 0.0, -(1.0 + Q1)]
    roots = np.roots(coeffs)
    real_pos = [r.real for r in roots if abs(r.imag) < 1e-10 and r.real > 0]
    if not real_pos:
        return pi**2 * Q_val  # asymptotic
    x = max(real_pos)
    return pi**4 * (1 + x) / x * ((1 + x)**2 + Q1)

# ============================================================
# Critical temperature gradient
# ============================================================
def beta_c_rel(B_gauss):
    """Critical temperature gradient (K/cm) for relativistic case."""
    Qr = Q_rel(B_gauss, d, w_0, nu_eff, eta_mag)
    Ra_c = Ra_c_from_Q(Qr)
    return Ra_c * nu_eff * kappa_T / (g_ns * alpha_th * d**4)

def beta_c_class(B_gauss):
    """Classical critical temperature gradient."""
    Qc = Q_class(B_gauss, d, rho_core, nu_shear, eta_mag)
    Ra_c = Ra_c_from_Q(Qc)
    return Ra_c * nu_shear * kappa_T / (g_ns * alpha_th * d**4)

# ============================================================
# Phase diagram: (B, beta) space
# ============================================================
B_range = np.logspace(12, 17, 300)
beta_range = np.logspace(-8, 2, 300)

# Compute critical curves
beta_c_rel_curve = np.array([beta_c_rel(B) for B in B_range])
beta_c_class_curve = np.array([beta_c_class(B) for B in B_range])

# Also compute Q_rel values for annotation
B_marks = [1e14, 1e15, 1e16]
Q_rel_marks = [Q_rel(B, d, w_0, nu_eff, eta_mag) for B in B_marks]
Q_class_marks = [Q_class(B, d, rho_core, nu_shear, eta_mag) for B in B_marks]
Ra_c_rel_marks = [Ra_c_from_Q(Q) for Q in Q_rel_marks]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Panel (a): Stability phase diagram ---
ax1.loglog(B_range, beta_c_rel_curve, color=COLORS['relativistic'], lw=2.5,
           label=r'Relativistic ($\xi=1.28$, SLy)')
ax1.loglog(B_range, beta_c_class_curve, color=COLORS['classical'], lw=2.0,
           ls='--', label=r'Newtonian')

# Fill regions
ax1.fill_between(B_range, beta_c_rel_curve, 1e3, alpha=0.10, color='red',
                 label='Unstable (convection)')
ax1.fill_between(B_range, 1e-9, beta_c_rel_curve, alpha=0.10, color='blue',
                 label='Stable')

# Mark magnetar B values
for B_val, Q_r, Q_c in zip(B_marks, Q_rel_marks, Q_class_marks):
    ax1.axvline(B_val, color='grey', ls=':', lw=0.8, alpha=0.5)
    ax1.text(B_val * 1.3, 1e-7, f'$Q_{{\\rm rel}}={Q_r:.1e}$\n$Q_{{\\rm cl}}={Q_c:.1e}$',
             fontsize=7, color='grey')

# Typical temperature gradients
ax1.axhline(1e-1, color='green', ls='-.', lw=1.0, alpha=0.7,
            label=r'Proto-NS ($\beta\sim 0.1$ K/cm)')
ax1.axhline(1e-5, color='orange', ls='-.', lw=1.0, alpha=0.7,
            label=r'Mature NS ($\beta\sim 10^{-5}$ K/cm)')

ax1.set_xlabel(r'Magnetic field $B$ [G]', fontsize=14)
ax1.set_ylabel(r'Critical temperature gradient $\beta_c$ [K/cm]', fontsize=14)
ax1.set_title('(a) Stability phase diagram: magnetar magneto-convection', fontsize=12)
ax1.set_xlim(1e12, 1e17)
ax1.set_ylim(1e-8, 1e2)
ax1.legend(loc='upper left', fontsize=8, ncol=1)

# --- Panel (b): Ra_c vs Q_rel for three B values ---
Q_range = np.logspace(0, 12, 200)
Ra_c_curve = np.array([Ra_c_from_Q(Q) for Q in Q_range])

ax2.loglog(Q_range, Ra_c_curve, 'k-', lw=2.0, label=r'$\mathrm{Ra}_c(Q)$ (free bdry)')
ax2.loglog(Q_range, pi**2 * Q_range, 'k:', lw=1.0, alpha=0.5,
           label=r'$\pi^2 Q$ asymptote')

# Mark the three magnetar B values
colors_B = ['#4CAF50', '#FF9800', '#F44336']
for B_val, Q_r, color in zip(B_marks, Q_rel_marks, colors_B):
    Ra_val = Ra_c_from_Q(Q_r)
    ax2.plot(Q_r, Ra_val, 'o', color=color, ms=12, zorder=5,
             markeredgecolor='k', markeredgewidth=0.8,
             label=f'$B=10^{{{int(np.log10(B_val))}}}$ G: $Q_{{\\rm rel}}={Q_r:.1e}$')

# Also show where magnetic stabilization overcomes relativistic destabilization
# This happens when Q_rel is large enough that Ra_c(Q_rel) > Ra_c(Q=0) * xi^2
Ra_c_0 = Ra_c_from_Q(0)  # ~657.5 for free boundaries
Q_crossover = Ra_c_0 * (xi_SLy**2 - 1) / pi**2
ax2.axvline(Q_crossover, color='purple', ls='--', lw=1.5, alpha=0.7)
ax2.text(Q_crossover * 2, 1e3, f'$Q_{{\\rm cross}}={Q_crossover:.0f}$\n(magnetic > rel.)',
         fontsize=9, color='purple')

ax2.set_xlabel(r'Relativistic Chandrasekhar number $Q_{\rm rel}$', fontsize=14)
ax2.set_ylabel(r'Critical Rayleigh number $\mathrm{Ra}_c$', fontsize=14)
ax2.set_title('(b) $\\mathrm{Ra}_c$ vs $Q_{\\rm rel}$ with magnetar parameters', fontsize=12)
ax2.legend(loc='upper left', fontsize=9)
ax2.set_xlim(1e0, 1e12)
ax2.set_ylim(1e2, 1e14)

plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), 'fig_magnetar_stability_phase.pdf'))
plt.savefig(os.path.join(os.path.dirname(__file__), 'fig_magnetar_stability_phase.png'))
print("Saved fig_magnetar_stability_phase.pdf/png")

# Print quantitative results
for B_val, Q_r, Q_c, Ra_r in zip(B_marks, Q_rel_marks, Q_class_marks, Ra_c_rel_marks):
    print(f"B = {B_val:.0e} G: Q_rel = {Q_r:.3e}, Q_class = {Q_c:.3e}, "
          f"Ra_c = {Ra_r:.3e}, ratio Q_rel/Q_class = {Q_r/Q_c:.4f}")
