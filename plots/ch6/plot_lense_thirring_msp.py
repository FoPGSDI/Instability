#!/usr/bin/env python3
"""
Agent 23 -- Millisecond pulsar convection: Lense-Thirring correction
to effective rotation vs spin frequency.

Shows how frame-dragging reduces the effective Taylor number and
hence the rotational stabilisation of convection.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS, G_cgs, c_cgs, M_sun
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# Spin frequencies (Hz)
nu_spin = np.linspace(50, 716, 500)  # up to fastest known MSP (PSR J1748-2446ad)
Omega = 2 * np.pi * nu_spin

# NS parameters
M = 1.4 * M_sun
R = 1.0e6  # 10 km in cm
I_ns = 0.4 * M * R**2  # moment of inertia (approximate)
C_compact = G_cgs * M / (R * c_cgs**2)  # compactness ~ 0.21

# Lense-Thirring angular velocity at different radii
# omega_LT(r) = 2 G J / (c^2 r^3), J = I * Omega
# At the surface (r = R): omega_LT = 2 G I Omega / (c^2 R^3)
# Fractional correction: omega_LT / Omega = 2 G I / (c^2 R^3) ~ 2/5 * C
LT_frac_surface = 2 * G_cgs * I_ns / (c_cgs**2 * R**3)  # ~ 0.17

# At different fractional radii
r_fracs = [1.0, 0.7, 0.5]
colors_r = ['#2196F3', '#4CAF50', '#F44336']
styles_r = ['-', '--', '-.']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

# Left panel: Omega_eff / Omega vs spin frequency at different radii
for r_f, col, ls in zip(r_fracs, colors_r, styles_r):
    LT_frac = LT_frac_surface / r_f**3
    Omega_eff_ratio = 1 - LT_frac
    ax1.plot(nu_spin, np.full_like(nu_spin, Omega_eff_ratio), ls, color=col,
             linewidth=2.0, label=rf'$r/R = {r_f}$')

ax1.axhline(1.0, color='gray', linestyle=':', linewidth=1.0, label='No frame-dragging')
ax1.set_xlabel(r'Spin frequency $\nu$ (Hz)')
ax1.set_ylabel(r'$\Omega_{\mathrm{eff}} / \Omega$')
ax1.set_title('Frame-dragging reduction of effective rotation')
ax1.legend(loc='lower left')
ax1.set_ylim(0.5, 1.05)

# Right panel: Ta_rel / Ta_Newton vs spin frequency
# Ta_rel = 4 Omega_eff^2 R^4 / nu_rel^2
# Ta_Newton = 4 Omega^2 R^4 / nu^2
# Ratio = (Omega_eff / Omega)^2 = (1 - omega_LT/Omega)^2
# For different compactnesses
compactnesses = [0.10, 0.15, 0.20, 0.25]
colors_c = ['#2196F3', '#4CAF50', '#FF9800', '#F44336']
styles_c = ['-', '--', '-.', ':']

for C_val, col, ls in zip(compactnesses, colors_c, styles_c):
    # At center: omega_LT/Omega ~ (2/5)*C * (R/r)^3, use volume-averaged
    avg_LT_frac = 0.4 * C_val  # approximate
    Ta_ratio = (1 - avg_LT_frac)**2
    ax2.plot(nu_spin, np.full_like(nu_spin, Ta_ratio), ls, color=col,
             linewidth=2.0, label=rf'$\mathcal{{C}} = {C_val}$')

ax2.axhline(1.0, color='gray', linestyle=':', linewidth=1.0)
ax2.set_xlabel(r'Spin frequency $\nu$ (Hz)')
ax2.set_ylabel(r'$\mathrm{Ta}_{\mathrm{rel}} / \mathrm{Ta}_{\mathrm{Newton}}$')
ax2.set_title('Taylor number reduction by Lense-Thirring')
ax2.legend(loc='lower left')
ax2.set_ylim(0.6, 1.05)

# Mark known MSPs
for ax in [ax1, ax2]:
    ax.axvline(641, color='purple', linestyle=':', linewidth=0.8, alpha=0.5)
    ax.text(641, ax.get_ylim()[1]*0.98, 'PSR\nJ1748', fontsize=8,
            ha='right', va='top', color='purple')

fig.tight_layout()
outdir = os.path.dirname(__file__)
fig.savefig(os.path.join(outdir, 'fig_lense_thirring_msp.pdf'))
fig.savefig(os.path.join(outdir, 'fig_lense_thirring_msp.png'))
print('Saved plots/ch6/fig_lense_thirring_msp.pdf and .png')
plt.close(fig)
