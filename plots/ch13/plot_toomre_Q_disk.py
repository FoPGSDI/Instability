#!/usr/bin/env python3
"""
Plot Toomre Q parameter for galactic disk stability with rotation and
magnetic field in spiral arms.

The relativistic Toomre parameter:
    Q_rel = c_s * kappa_rel / (pi * G * Sigma_rel)

We plot Q as a function of radius in a model spiral galaxy,
showing how rotation and magnetic field modify the stability boundary.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, G_cgs, c_cgs, M_sun, pi
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

setup_style()

# Model galactic disk parameters
# Radii in kpc
r_kpc = np.linspace(1.0, 20.0, 500)
r_cm = r_kpc * 3.086e21  # kpc to cm

# Rotation curve: flat at V_c ~ 220 km/s
V_c = 2.2e7  # cm/s (220 km/s)
Omega = V_c / r_cm  # angular velocity
# Epicyclic frequency for flat rotation curve: kappa = sqrt(2) * Omega
kappa = np.sqrt(2.0) * Omega

# Surface density: exponential disk with Sigma_0 = 50 Msun/pc^2
R_d = 3.0  # scale length in kpc
Sigma_0 = 50.0 * M_sun / (3.086e18)**2  # g/cm^2
Sigma = Sigma_0 * np.exp(-r_kpc / R_d)

# Sound speed: thermal (10 km/s) + turbulent
cs_thermal = 1.0e6  # 10 km/s in cm/s

# Magnetic field: B ~ 5 muG in spiral arms
B_arm = 5e-6  # Gauss
# Effective sound speed with magnetic support: c_eff^2 = c_s^2 + v_A^2
rho_midplane = Sigma / (2.0 * 300 * 3.086e18)  # rough midplane density
v_A = B_arm / np.sqrt(4.0 * pi * rho_midplane)

c_eff_no_B = cs_thermal
c_eff_with_B = np.sqrt(cs_thermal**2 + v_A**2)

# Toomre Q
Q_no_B = c_eff_no_B * kappa / (pi * G_cgs * Sigma)
Q_with_B = c_eff_with_B * kappa / (pi * G_cgs * Sigma)

# Relativistic correction (very small for galactic disks, but show for principle)
# w = p/eps, for galactic gas w ~ 1e-6, so correction is negligible
# But for illustration, show with exaggerated c_s/c ratio
w_param = (cs_thermal / c_cgs)**2
rel_factor = np.sqrt((1.0 + w_param) * (1.0 + 3.0*w_param) / 2.0)
# For a hypothetical relativistic disk (e.g., near SMBH)
cs_rel = 0.1 * c_cgs  # 10% of c
w_rel = (cs_rel / c_cgs)**2
Sigma_rel = Sigma * (1.0 + w_rel)  # enthalpy correction
kappa_rel = kappa  # same for illustration
Q_rel_disk = cs_rel * kappa_rel / (pi * G_cgs * Sigma_rel * (1 + 3*w_rel)/2)
# Normalise to same scale
Q_rel_norm = Q_rel_disk / Q_rel_disk[0] * Q_no_B[0]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# --- Left panel: Q vs radius for galactic disk ---
ax1.plot(r_kpc, Q_no_B, '-', color='#2196F3', lw=2.2,
         label=r'Thermal only ($c_s = 10$ km/s)')
ax1.plot(r_kpc, Q_with_B, '-', color='#4CAF50', lw=2.2,
         label=r'Thermal + B ($B = 5\,\mu$G)')

# Spiral arm enhancement: reduce Q locally
r_arm1, r_arm2 = 5.0, 10.0  # spiral arm locations
for r_arm in [r_arm1, r_arm2]:
    ax1.axvspan(r_arm - 0.5, r_arm + 0.5, alpha=0.08, color='#FF9800')

ax1.axhline(1.0, color='red', ls='--', lw=1.5, alpha=0.7,
            label=r'$Q = 1$ (instability threshold)')
ax1.axhline(2.0, color='orange', ls=':', lw=1.0, alpha=0.5,
            label=r'$Q = 2$ (marginal for non-axisymmetric)')

ax1.fill_between(r_kpc, 0, 1.0, alpha=0.05, color='red')
ax1.text(15, 0.5, 'UNSTABLE', fontsize=10, color='red', alpha=0.6,
         fontweight='bold')

ax1.set_xlabel('Galactocentric radius [kpc]')
ax1.set_ylabel(r'Toomre $Q$ parameter')
ax1.set_title('Disk stability: Toomre Q with rotation + B field')
ax1.legend(loc='upper right', fontsize=9)
ax1.set_xlim(1, 20)
ax1.set_ylim(0, 5)
ax1.grid(True, ls=':', alpha=0.3)
ax1.text(5, 4.5, 'Spiral\narm', fontsize=8, ha='center', color='#FF9800')
ax1.text(10, 4.5, 'Spiral\narm', fontsize=8, ha='center', color='#FF9800')

# --- Right panel: Q_rel vs c_s/c for different B strengths ---
cs_over_c = np.linspace(0.001, 0.5, 500)
cs_vals = cs_over_c * c_cgs

# Fixed parameters for a compact disk (near SMBH)
Sigma_fixed = 1e4 * M_sun / (3.086e18)**2  # high surface density
kappa_fixed = 1.0e-4  # s^-1

B_values = [0, 1e-3, 1e-2, 1e-1]  # in Gauss (strong fields near SMBH)
B_labels = [r'$B = 0$', r'$B = 1$ mG', r'$B = 10$ mG', r'$B = 100$ mG']
B_colors = ['#F44336', '#FF9800', '#4CAF50', '#2196F3']

for Bval, lbl, col in zip(B_values, B_labels, B_colors):
    rho_est = Sigma_fixed / (2.0 * 1e15)
    enthalpy = rho_est * (1 + cs_over_c**2)
    if Bval > 0:
        vA2 = Bval**2 / (4 * pi * enthalpy)
        cs_eff = np.sqrt(cs_vals**2 + vA2)
    else:
        cs_eff = cs_vals

    A_factor = (1 + 3*cs_over_c**2) / 2.0
    Sigma_enth = Sigma_fixed * (1 + cs_over_c**2)
    Q_vals = cs_eff * kappa_fixed / (pi * G_cgs * Sigma_enth * A_factor)
    Q_norm = Q_vals / Q_vals[0]  # normalise to show relative effect
    ax2.plot(cs_over_c, Q_norm, '-', color=col, lw=2.0, label=lbl)

ax2.axhline(1.0, color='gray', ls=':', lw=1.0)
ax2.set_xlabel(r'$c_s / c$')
ax2.set_ylabel(r'Normalised $Q_{\mathrm{rel}}$')
ax2.set_title(r'Relativistic $Q$ vs sound speed (compact disk)')
ax2.legend(loc='upper right', fontsize=9)
ax2.set_xlim(0, 0.5)
ax2.grid(True, ls=':', alpha=0.3)

# Annotate relativistic regime
ax2.annotate('Relativistic\ncorrections\nsignificant',
             xy=(0.3, 0.6), fontsize=9, color='#9C27B0',
             ha='center', style='italic')

fig.tight_layout()
fig.savefig(os.path.join(os.path.dirname(__file__), 'fig_toomre_Q_disk.pdf'))
fig.savefig(os.path.join(os.path.dirname(__file__), 'fig_toomre_Q_disk.png'))
print("Saved plots/ch13/fig_toomre_Q_disk.pdf and .png")
plt.close(fig)
