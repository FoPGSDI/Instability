#!/usr/bin/env python3
"""
fig_bulk_viscosity_ns.py
Nuclear bulk viscosity zeta(T) from Urca processes: plot zeta vs T for
direct Urca, modified Urca, and electron capture.
Show Gavassino's telegraph relaxation time.

References:
- Gavassino, Antonelli & Haskell (2021), CQG 38, 075001 [arXiv:2003.04609]
- Gavassino (2023), PRD 107, 096023 [arXiv:2304.05455] (Burgers-type)
- Gavassino & Noronha (2023), PRD 108, 076006 [arXiv:2305.04119] (bulk rheology)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# === Left panel: Bulk viscosity vs temperature ===
ax1 = axes[0]

# Temperature range in units of 10^9 K
T9 = np.logspace(-1, 2, 300)  # 10^8 to 10^11 K
T = T9 * 1e9  # in K

# Bulk viscosity models (approximate scaling from Haensel+ and Alford+)
# Direct Urca: zeta ~ C_dU * T^{-4} for T < T_c (fast process)
# Modified Urca: zeta ~ C_mU * T^{-6} (slower, dominates at lower T)
# Electron capture: zeta ~ C_ec * T^{-2} (nuclear processes)

# Frequencies: omega = 2*pi * 1 kHz (typical NS oscillation)
omega = 2 * np.pi * 1e3  # rad/s

# Direct Urca (only above threshold density ~2 n_sat)
tau_dU = 1e-6 * (1e9 / T)**4  # relaxation time in seconds
zeta_dU = 1e30 * (1e9 / T)**4 * omega**2 * tau_dU / (1 + omega**2 * tau_dU**2)

# Modified Urca
tau_mU = 1e-2 * (1e9 / T)**6
zeta_mU = 1e28 * (1e9 / T)**6 * omega**2 * tau_mU / (1 + omega**2 * tau_mU**2)

# Electron capture (crust processes)
tau_ec = 1e-4 * (1e9 / T)**2
zeta_ec = 1e26 * (1e9 / T)**2 * omega**2 * tau_ec / (1 + omega**2 * tau_ec**2)

ax1.loglog(T9, zeta_dU, color='#F44336', linewidth=2.5,
           label='Direct Urca')
ax1.loglog(T9, zeta_mU, color='#2196F3', linewidth=2.5,
           label='Modified Urca')
ax1.loglog(T9, zeta_ec, color='#4CAF50', linewidth=2.5,
           label='Electron capture')

# Combined envelope
zeta_total = np.maximum(zeta_dU, np.maximum(zeta_mU, zeta_ec))
ax1.loglog(T9, zeta_total, color='black', linewidth=1.5, linestyle='--',
           label='Total (envelope)', alpha=0.6)

ax1.set_xlabel('$T$ [$10^9$ K]')
ax1.set_ylabel('$\\zeta$ [g cm$^{-1}$ s$^{-1}$]')
ax1.set_title('Nuclear bulk viscosity at $f = 1$ kHz')
ax1.legend(loc='upper right', fontsize=10)
ax1.set_xlim(0.1, 100)
ax1.set_ylim(1e20, 1e35)

# === Right panel: Telegraph relaxation (Gavassino) ===
ax2 = axes[1]

# Gavassino's telegraph relaxation for bulk viscosity:
# Pi_dot + Pi/tau = -zeta * theta_dot
# This gives effective viscosity zeta_eff(omega) = zeta * i*omega*tau / (1 + i*omega*tau)
# |zeta_eff| = zeta * omega*tau / sqrt(1 + omega^2*tau^2)

omega_range = np.logspace(-2, 4, 300)  # omega * tau_pi

# For different tau values
tau_values = [0.01, 0.1, 1.0, 10.0]
colors_tau = ['#2196F3', '#4CAF50', '#FF9800', '#F44336']

for tau, col in zip(tau_values, colors_tau):
    omega_tau = omega_range * tau
    # Normalized effective viscosity
    zeta_eff_norm = omega_tau / np.sqrt(1 + omega_tau**2)
    ax2.semilogx(omega_range, zeta_eff_norm, color=col, linewidth=2.0,
                 label=f'$\\tau_\\Pi = {tau}$ ms')

# Mark the transition omega*tau = 1
ax2.axvline(x=1.0, color='gray', linestyle=':', linewidth=1.5, alpha=0.7)
ax2.text(1.2, 0.15, '$\\omega\\tau_\\Pi = 1$', fontsize=11, color='gray')

# Asymptotic labels
ax2.text(0.02, 0.15, 'Navier--Stokes\nregime\n$\\zeta_{\\rm eff} \\propto \\omega\\tau$',
         fontsize=9, color='#37474F')
ax2.text(30, 0.85, 'Telegraph\nregime\n$\\zeta_{\\rm eff} \\to \\zeta$',
         fontsize=9, color='#37474F')

ax2.set_xlabel('Oscillation frequency $\\omega$ [kHz]')
ax2.set_ylabel('$|\\zeta_{\\rm eff}|/\\zeta$')
ax2.set_title("Gavassino's telegraph relaxation of bulk viscosity")
ax2.legend(loc='center right', fontsize=10)
ax2.set_xlim(0.01, 1e4)
ax2.set_ylim(0, 1.15)

plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), 'fig_bulk_viscosity_ns.pdf'))
plt.savefig(os.path.join(os.path.dirname(__file__), 'fig_bulk_viscosity_ns.png'))
print('Saved fig_bulk_viscosity_ns.pdf')
