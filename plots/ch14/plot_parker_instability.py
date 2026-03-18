#!/usr/bin/env python3
"""
Plot Parker (magnetic buoyancy) instability in relativistic galactic halos.

The Parker instability occurs when a magnetised, stratified atmosphere
becomes unstable to undular perturbations of the magnetic field lines.
In the relativistic regime, the growth rate is modified by:
  - Enthalpy density w = (eps + p)/c^2 replacing rho
  - Relativistic sound speed c_s^2 = dp/deps <= c^2
  - Bounded Alfven speed v_A < c

Growth rate: sigma^2 = g * k_x * (1/(1+beta/2) - k_z^2/k_x^2 * c_s^2/g*H)
where g = gravitational acceleration, H = scale height, beta = 8*pi*p/B^2
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, pi
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

setup_style()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# --- Left panel: Parker instability growth rate vs k_x*H ---

kxH = np.linspace(0.01, 5.0, 500)

# Parameters
beta_values = [0.5, 1.0, 2.0, 5.0]
colors = ['#F44336', '#FF9800', '#4CAF50', '#2196F3']

# Classical Parker growth rate (normalised by sqrt(g/H)):
# sigma^2 / (g/H) = k_x*H * (1/(1+beta/2)) - (k_x*H)^2 * cs^2/(g*H)
# For a fixed k_z = k_x (maximum growth angle)

cs2_over_gH = 0.5  # typical value

for beta_val, col in zip(beta_values, colors):
    sigma2_cl = kxH * (1.0 / (1.0 + beta_val/2.0)) - kxH**2 * cs2_over_gH
    sigma2_cl = np.maximum(sigma2_cl, -0.5)  # clip for plotting
    ax1.plot(kxH, sigma2_cl, '-', color=col, lw=2.0,
             label=r'$\beta = ' + f'{beta_val}' + '$ (classical)')

# Relativistic case: enhanced gravity due to pressure
# sigma^2_rel = sigma^2_cl * (1 + 3*cs^2/c^2)/2 * (1+w) - relativistic damping
# For a mildly relativistic halo (c_s/c = 0.3)
cs_over_c = 0.3
rel_enhance = (1.0 + 3.0*cs_over_c**2) / 2.0
w_eos = cs_over_c**2  # for linear EOS

for beta_val, col in zip([1.0, 2.0], ['#FF9800', '#4CAF50']):
    sigma2_rel = kxH * (1.0 / (1.0 + beta_val/2.0)) * rel_enhance * (1+w_eos) \
                 - kxH**2 * cs2_over_gH * (1 + w_eos)
    sigma2_rel = np.maximum(sigma2_rel, -0.5)
    ax1.plot(kxH, sigma2_rel, '--', color=col, lw=2.0,
             label=r'$\beta = ' + f'{beta_val}' + r'$ (rel., $c_s/c=0.3$)')

ax1.axhline(0, color='k', lw=0.8)
ax1.fill_between(kxH, -0.5, 0, alpha=0.04, color='green')
ax1.fill_between(kxH, 0, 1.0, alpha=0.04, color='red')
ax1.text(3.5, 0.15, 'UNSTABLE', fontsize=10, color='red', alpha=0.6,
         fontweight='bold')
ax1.text(3.5, -0.3, 'STABLE', fontsize=10, color='green', alpha=0.6,
         fontweight='bold')

ax1.set_xlabel(r'$k_x H$ (normalised wavenumber)')
ax1.set_ylabel(r'$\sigma^2 / (g/H)$ (normalised growth rate)')
ax1.set_title('Parker instability: growth rate')
ax1.legend(loc='upper right', fontsize=8, ncol=1)
ax1.set_xlim(0, 5)
ax1.set_ylim(-0.5, 0.6)
ax1.grid(True, ls=':', alpha=0.3)

# --- Right panel: Critical wavelength vs c_s/c ---

cs_c_arr = np.linspace(0.01, 0.7, 500)

# Classical critical wavelength: lambda_crit = 2*pi*H*sqrt(cs^2/(g*H) * (1+beta/2))
# Normalised: lambda_crit / H = 2*pi*sqrt(cs^2/(g*H) * (1+beta/2))

beta_fixed = 1.0
# Classical (independent of c)
lambda_cl = 2.0 * pi * np.sqrt(cs2_over_gH * (1 + beta_fixed/2.0))
lambda_cl_arr = np.ones_like(cs_c_arr) * lambda_cl

# Relativistic: effective gravity enhanced, effective cs^2 -> cs^2*w
# lambda_rel = lambda_cl / sqrt((1+3*cs^2/c^2)/2 * (1+w))
rel_factor = np.sqrt((1 + 3*cs_c_arr**2)/2.0 * (1 + cs_c_arr**2))
lambda_rel_arr = lambda_cl / rel_factor

# Maximum growth rate vs c_s/c
# sigma_max_cl = g/(4H) * 1/(1+beta/2)
sigma_max_cl = 0.25 / (1 + beta_fixed/2.0)
sigma_max_cl_arr = np.ones_like(cs_c_arr) * sigma_max_cl

sigma_max_rel = sigma_max_cl * (1 + 3*cs_c_arr**2)/2.0 * (1+cs_c_arr**2) \
                / (1 + cs_c_arr**2 * (1 + beta_fixed/2.0))
# Ensure bounded
sigma_max_rel = np.minimum(sigma_max_rel, 2.0)

ax2_twin = ax2.twinx()

l1, = ax2.plot(cs_c_arr, lambda_rel_arr / lambda_cl, '-', color='#2196F3', lw=2.5,
               label=r'$\lambda_{\mathrm{crit,rel}} / \lambda_{\mathrm{crit,cl}}$')
ax2.axhline(1.0, color='gray', ls=':', lw=1.0)

l2, = ax2_twin.plot(cs_c_arr, sigma_max_rel / sigma_max_cl, '--', color='#F44336',
                    lw=2.5,
                    label=r'$\sigma_{\max,\mathrm{rel}} / \sigma_{\max,\mathrm{cl}}$')

ax2.set_xlabel(r'$c_s / c$')
ax2.set_ylabel(r'$\lambda_{\mathrm{crit,rel}} / \lambda_{\mathrm{crit,cl}}$',
               color='#2196F3')
ax2_twin.set_ylabel(r'$\sigma_{\max,\mathrm{rel}} / \sigma_{\max,\mathrm{cl}}$',
                    color='#F44336')

ax2.set_title(r'Parker instability: relativistic corrections ($\beta=1$)')
lines = [l1, l2]
labels = [l.get_label() for l in lines]
ax2.legend(lines, labels, loc='center right', fontsize=9)

ax2.set_xlim(0, 0.7)
ax2.set_ylim(0.3, 1.1)
ax2_twin.set_ylim(0.8, 2.5)
ax2.grid(True, ls=':', alpha=0.3)

# Annotate physical regimes
ax2.annotate('Galactic halo\n(mildly relativistic)',
             xy=(0.2, 0.9), fontsize=9, color='#9C27B0',
             ha='center', style='italic')
ax2.annotate('AGN corona\n(strongly relativistic)',
             xy=(0.55, 0.55), fontsize=9, color='#9C27B0',
             ha='center', style='italic')

fig.tight_layout()
fig.savefig(os.path.join(os.path.dirname(__file__), 'fig_parker_instability.pdf'))
fig.savefig(os.path.join(os.path.dirname(__file__), 'fig_parker_instability.png'))
print("Saved plots/ch14/fig_parker_instability.pdf and .png")
plt.close(fig)
