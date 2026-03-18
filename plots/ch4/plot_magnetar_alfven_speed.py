#!/usr/bin/env python3
"""
Agent 12: Magnetar B-field — Alfven speed vs c.
Plot v_A/c for B = 10^{14}--10^{16} G at various NS densities.
"""
import sys; sys.path.insert(0, '/data/haiyangw/claude/Instability'); from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, pi
import matplotlib.pyplot as plt
import numpy as np

setup_style()

B = np.logspace(14, 16.5, 500)  # Gauss

# Densities typical of NS layers (g/cm^3)
densities = {
    r'Outer crust ($\rho = 10^{10}$ g/cm$^3$)': 1e10,
    r'Inner crust ($\rho = 10^{13}$ g/cm$^3$)': 1e13,
    r'Outer core ($\rho = 10^{14}$ g/cm$^3$)': 1e14,
    r'Inner core ($\rho = 10^{15}$ g/cm$^3$)': 1e15,
}

colors = ['#E91E63', '#F44336', '#FF9800', '#2196F3']

fig, ax = plt.subplots(figsize=(8, 5.5))

for (label, rho), color in zip(densities.items(), colors):
    # Relativistic Alfven speed: v_A = B*c / sqrt(4pi*w + B^2)
    # For cold NS matter, w ~ rho*c^2, so enthalpy ~ rho*c^2
    w = rho * c_cgs**2  # enthalpy density (erg/cm^3)
    b2 = B**2 / (4 * pi)  # magnetic pressure (erg/cm^3)
    vA_over_c = np.sqrt(b2 / (w / c_cgs**2 + b2 / c_cgs**2)) / c_cgs
    # Equivalently: vA/c = B/sqrt(4pi) / sqrt(w/c^2 + B^2/(4pi*c^2))
    # = c * sqrt(b2) / sqrt(w + b2)
    vA_rel = c_cgs * np.sqrt(b2) / np.sqrt(w + b2)
    vA_over_c = vA_rel / c_cgs

    # Classical (no saturation)
    vA_class = B / np.sqrt(4 * pi * rho) / c_cgs

    ax.loglog(B, vA_over_c, '-', color=color, lw=2, label=label)
    ax.loglog(B, vA_class, '--', color=color, lw=1, alpha=0.5)

ax.axhline(1.0, color='k', ls=':', lw=1.5, label=r'$v_A/c = 1$ (causal limit)')
ax.fill_between([1e14, 4e16], 1.0, 10, color='gray', alpha=0.1)

ax.set_xlabel(r'Magnetic field $B$ (G)')
ax.set_ylabel(r'$v_A / c$')
ax.set_title(r'Relativistic Alfv\'en speed in neutron star interiors')
ax.set_xlim(1e14, 3e16)
ax.set_ylim(1e-4, 3)
ax.legend(loc='lower right', fontsize=9.5)

# Annotate
ax.annotate('Relativistic (solid)\nvs Classical (dashed)',
            xy=(2e15, 0.3), fontsize=9, style='italic',
            bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='gray', alpha=0.8))

fig.tight_layout()
fig.savefig('/data/haiyangw/claude/Instability/plots/ch4/fig_magnetar_alfven_speed.pdf')
fig.savefig('/data/haiyangw/claude/Instability/plots/ch4/fig_magnetar_alfven_speed.png')
print("Saved fig_magnetar_alfven_speed.pdf/png")
