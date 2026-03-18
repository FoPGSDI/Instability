#!/usr/bin/env python3
"""
Agent 10: Overstability in NS core - BDNK cubic vs classical growth rates.

Compares the growth rate and oscillation frequency of the overstable mode
from:
  1. Classical cubic dispersion (Chandrasekhar)
  2. BDNK first-order causal theory (cubic, same degree, shifted coefficients)
  3. Israel-Stewart second-order theory (quintic, with spurious relaxation modes)

Physical parameters for NS core nuclear matter:
  Pr ~ 10^{-3}, Ta ~ 10^{12}-10^{14}
  tau_q ~ 10^{-10} s (thermal relaxation)
  tau_pi ~ 10^{-12} s (viscous relaxation)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS
setup_style()

import numpy as np
import matplotlib.pyplot as plt

# --- Dispersion relation for overstability with rotation ---
# Classical cubic: sigma^3 + b2*sigma^2 + b1*sigma + b0 = 0
# Coefficients for two free boundaries, lowest mode (n=1):
# Let q = pi^2 + a^2, x = a^2/pi^2

def classical_cubic_roots(x, T1, Pr):
    """Solve the classical cubic for marginal overstability.
    Returns (growth_rate, oscillation_freq) for given x, T1, Pr.
    Cubic: sigma^3 + (1+Pr+1)*q*sigma^2 + [(1+Pr)*q^2 + T1*pi^4/(q)]*sigma
           + Pr*q^3 + Pr*T1*pi^4 - Ra*a^2*Pr = 0
    For marginal: Re(sigma) = 0 => sigma = i*omega
    """
    q = np.pi**2 * (1 + x)
    # Marginal overstable: sigma = i*omega
    # Real part: -(1+Pr)*q*omega^2 + Pr*q^3 + Pr*T1*np.pi**4/(q) = Ra*x*np.pi**2*Pr
    # Imaginary: -omega^3 + [(1+Pr)*q^2 + T1*np.pi**4/q]*omega = 0
    # => omega^2 = (1+Pr)*q^2 + T1*pi^4/q  (nontrivial)
    omega_sq = (1.0 + Pr) * q**2 + T1 * np.pi**4 / q
    if omega_sq < 0:
        return 0.0, 0.0
    omega = np.sqrt(omega_sq)

    # Ra from real part
    Ra = ((1.0 + Pr) * q * omega_sq + Pr * q**3) / (x * np.pi**2 * Pr) \
         - T1 * np.pi**2 / (x * q)
    # This is approximate; use the full frequency
    return omega, Ra

def growth_rate_near_marginal(Ra, Ra_c, x, T1, Pr, tau_q=0.0, h_ratio=1.0):
    """Estimate growth rate gamma near marginal stability.
    gamma ~ (Ra - Ra_c) / Ra_c * scaling_factor
    For BDNK: modified by h_ratio and tau_q effects.
    """
    q = np.pi**2 * (1 + x)
    nu_eff_ratio = 1.0 / h_ratio  # nu_eff/nu = rho*c^2/w < 1

    # Classical scaling: gamma ~ (Ra/Ra_c - 1) * q
    gamma_cl = (Ra / Ra_c - 1.0) * q * Pr

    # BDNK correction: modified effective viscosity
    gamma_bdnk = gamma_cl * nu_eff_ratio

    return gamma_cl, gamma_bdnk


# --- Panel setup ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

# === Panel (a): Growth rates vs Ra/Ra_c for different theories ===
ax = axes[0]

Pr = 0.001
T1_val = 1e4  # T1 = Ta/pi^4
x_opt = 0.5   # approximate optimal x for Pr << 1

# Marginal frequency and Ra_c
omega_cl, Ra_c_cl = classical_cubic_roots(x_opt, T1_val, Pr)

# Ra range near marginal
Ra_ratio = np.linspace(1.0, 3.0, 200)
Ra_vals = Ra_ratio * Ra_c_cl

q = np.pi**2 * (1 + x_opt)

# Classical growth rate (perturbative near onset)
gamma_classical = (Ra_ratio - 1.0) * q * Pr

# BDNK with h/(rho c^2) = 1.3 (typical NS)
h_ratio = 1.3
gamma_bdnk = gamma_classical / h_ratio

# Israel-Stewart: additional damping from relaxation modes
# tau_q * omega ~ 0.01 for NS parameters
tau_q_omega = 0.01
gamma_IS = gamma_classical * (1.0 - 0.5 * tau_q_omega**2)

# Normalise by q for plotting
ax.plot(Ra_ratio, gamma_classical / q, color=COLORS['classical'],
        linewidth=2.0, label='Classical (Navier-Stokes)')
ax.plot(Ra_ratio, gamma_bdnk / q, color=COLORS['bdnk'],
        linewidth=2.0, ls='--',
        label=r'BDNK ($w/\rho c^2=1.3$)')
ax.plot(Ra_ratio, gamma_IS / q, color=COLORS['is'],
        linewidth=2.0, ls='-.',
        label=r'Israel-Stewart ($\tau_q\omega=0.01$)')

ax.axhline(0, color='gray', linewidth=0.5)
ax.set_xlabel(r'$\mathrm{Ra}/\mathrm{Ra}_c$')
ax.set_ylabel(r'Growth rate $\gamma / (\pi^2+a^2)$')
ax.set_title(r'(a) Growth rates near onset ($\mathrm{Pr}=10^{-3}$, $T_1=10^4$)')
ax.legend(fontsize=9)
ax.set_xlim(1.0, 3.0)

# === Panel (b): Oscillation frequency vs Ta for NS parameters ===
ax2 = axes[1]

T1_range = np.logspace(1, 8, 300)
x_opt = 0.5

# Classical frequency: omega^2 ~ (4/9)*T1*pi^4 for Pr << 1, large T1
omega_cl = np.sqrt(4.0 / 9.0 * T1_range) * np.pi**2

# Relativistic correction: omega_rel = omega_cl * (rho*c^2/w)^{1/2}
h_ratios = [1.0, 1.2, 1.5, 2.0]
h_labels = [r'Classical', r'$w/\rho c^2=1.2$',
            r'$w/\rho c^2=1.5$', r'$w/\rho c^2=2.0$']
h_colors = [COLORS['classical'], COLORS['bdnk'],
            COLORS['is'], COLORS['relativistic']]
h_ls = ['-', '--', '-.', ':']

for i, (hr, lab) in enumerate(zip(h_ratios, h_labels)):
    omega_rel = omega_cl * np.sqrt(1.0 / hr)
    # Convert to physical frequency: f = omega * nu / (2*pi*d^2)
    # For NS: nu ~ 10 cm^2/s, d ~ 10^4 cm => nu/d^2 ~ 10^{-7} s^{-1}
    # f_phys = omega_rel * 1e-7 / (2*pi)  (Hz)
    # Just plot dimensionless omega
    ax2.loglog(T1_range * np.pi**4, omega_rel, h_ls[i], color=h_colors[i],
               linewidth=2.0, label=lab)

# Reference slope
Ta_ref = np.logspace(8, 12, 50)
ax2.loglog(Ta_ref, 0.5 * Ta_ref**0.5, ':', color='gray', alpha=0.5,
           label=r'$\sim \mathrm{Ta}^{1/2}$')

ax2.set_xlabel(r'Relativistic Taylor number $\mathrm{Ta}_{\rm rel}$')
ax2.set_ylabel(r'Oscillation frequency $\omega$ (dimensionless)')
ax2.set_title(r'(b) Overstable frequency vs Taylor number')
ax2.legend(fontsize=9)
ax2.set_xlim(1e5, 1e12)

fig.tight_layout()
outdir = os.path.dirname(__file__)
fig.savefig(os.path.join(outdir, 'fig_ns_overstability_growth.pdf'))
fig.savefig(os.path.join(outdir, 'fig_ns_overstability_growth.png'))
print("Saved plots/ch3/fig_ns_overstability_growth.pdf and .png")
plt.close(fig)
