#!/usr/bin/env python3
"""
Agent 35: Toroidal B instabilities -- kink modes in neutron star magnetosphere.

Shows the relativistic kink/sausage stability criterion for toroidal
magnetic fields, comparing classical and relativistic thresholds for
the stabilising axial field required to suppress kink modes.

Produces: plots/ch9/fig_kink_modes_ns.pdf
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# Model: toroidal field H_theta(r) = H0 * (R1/r) (force-free-like)
# Stability requires: H_z^2 / (4 pi rho_eff) > critical threshold
# Relativistically: rho_eff = rho (1 + Xi + v_A^2/c^2)

r_ratio = np.linspace(1.0, 3.0, 300)  # r/R1

# Omega_H^2 profile for H_theta ~ 1/r
OmH2_class = 1.0 / r_ratio**4  # normalized

# Required stabilizing Hz^2 (proportional to integral of kink drive)
# For kink (m=1): need Hz^2 > Hz_crit^2
# Classical: Hz_crit depends on the toroidal field profile
# Relativistic: Hz_crit scales as rho_eff/rho * Hz_crit_class

Xi_values = [0.0, 0.1, 0.3, 0.5]  # p/(epsilon c^2)
vA_over_c = [0.0, 0.1, 0.2, 0.3]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

# Left panel: Kink growth rate vs axial wavenumber for different Xi
k_norm = np.linspace(0.01, 5, 500)  # kR1
colors = [COLORS['classical'], '#4CAF50', COLORS['accretion'], COLORS['relativistic']]

for i, Xi in enumerate(Xi_values):
    rho_eff_ratio = 1 + Xi
    # Simplified kink dispersion: sigma^2 ~ OmH^2 - k^2 v_A^2 / rho_eff_ratio
    # Assume OmH ~ 1, v_A_axial ~ 0.3
    vA_ax = 0.3
    sigma2 = 1.0 - k_norm**2 * vA_ax**2 / rho_eff_ratio
    sigma = np.sqrt(np.maximum(sigma2, 0))
    label = 'Classical' if Xi == 0 else rf'$\Xi = {Xi}$'
    ls = '-' if Xi == 0 else '--'
    ax1.plot(k_norm, sigma, color=colors[i], ls=ls, lw=2.0, label=label)

ax1.set_xlabel(r'Axial wavenumber $kR_1$')
ax1.set_ylabel(r'Kink growth rate $\sigma / \Omega_{H}$')
ax1.set_title('Kink mode growth rate')
ax1.legend(fontsize=10)
ax1.set_xlim(0, 5)
ax1.set_ylim(0, 1.2)

# Right panel: Critical Hz/Htheta for stabilisation vs Xi
Xi_arr = np.linspace(0, 0.6, 200)
vA_c_arr = np.linspace(0, 0.4, 200)

# Critical field ratio scales as sqrt(rho_eff / rho)
Hz_crit_class = 0.23  # representative value from Chandrasekhar Table XLI

XX, VV = np.meshgrid(Xi_arr, vA_c_arr)
rho_eff = 1 + XX + VV**2
Hz_crit_rel = Hz_crit_class * np.sqrt(rho_eff)

cs = ax2.contourf(XX, VV, Hz_crit_rel, levels=15, cmap='RdYlBu_r')
plt.colorbar(cs, ax=ax2, label=r'$H_{z,\mathrm{crit}} / H_{\theta,0}$')
ax2.set_xlabel(r'Pressure parameter $\Xi = p/(\varepsilon c^2)$')
ax2.set_ylabel(r'$v_A / c$')
ax2.set_title('Critical axial field for kink stabilisation')

# Mark NS magnetosphere regime
ax2.plot([0.1, 0.3], [0.05, 0.15], 'wo', markersize=8)
ax2.annotate('NS magnetosphere', xy=(0.2, 0.1), fontsize=9, color='white',
             ha='center', fontweight='bold')

fig.suptitle('Toroidal B Instabilities: Kink Modes in Neutron Star Magnetosphere',
             fontsize=13, y=1.02)
fig.tight_layout()
fig.savefig(os.path.join(os.path.dirname(__file__), 'fig_kink_modes_ns.pdf'))
fig.savefig(os.path.join(os.path.dirname(__file__), 'fig_kink_modes_ns.png'))
print("Saved plots/ch9/fig_kink_modes_ns.pdf")
