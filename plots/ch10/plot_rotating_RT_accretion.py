#!/usr/bin/env python3
"""
Rotating RT in accretion disks: centrifugal stabilization.

In relativistic accretion disks around black holes, the Rayleigh-Taylor
instability at density interfaces is modified by rotation. The
relativistic Coriolis effect (enhanced by gamma^2) provides stronger
stabilization than in the Newtonian case.

Reference: Chandrasekhar Ch X §95 (relativistic extension).
"""
import sys; sys.path.insert(0, '/data/haiyangw/claude/Instability'); from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# --- Parameters ---
# Normalized: g = 1, k ranges, Omega varies
g_eff = 1.0
A_rel = 0.5  # relativistic Atwood number

# Non-rotating RT growth rate (squared)
k = np.linspace(0.01, 5.0, 500)
n0_sq = g_eff * k * A_rel  # inviscid, no surface tension

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Left panel: Growth rate vs k for different Omega ---
# From eq: n^2 = -2*Omega_rel^2 + sqrt(4*Omega_rel^4 + n0^4)
Omega_values = [0.0, 0.2, 0.5, 1.0, 2.0, 5.0]
colors_Om = ['#2196F3', '#4CAF50', '#FF9800', '#F44336', '#9C27B0', '#795548']

for i, Om in enumerate(Omega_values):
    if Om == 0:
        n2 = n0_sq
    else:
        n2 = -2.0 * Om**2 + np.sqrt(4.0 * Om**4 + n0_sq**2)

    # Growth rate (real part, for unstable modes)
    n_growth = np.sqrt(np.maximum(n2, 0))

    label = r'No rotation' if Om == 0 else rf'$\Omega_\mathrm{{rel}} = {Om}$'
    ax1.plot(k, n_growth, '-', color=colors_Om[i], linewidth=2.0, label=label)

ax1.set_xlabel(r'Wavenumber $k$', fontsize=14)
ax1.set_ylabel(r'Growth rate $n$', fontsize=14)
ax1.set_title(r'RT growth rate with rotation ($\mathcal{A}_\mathrm{rel} = 0.5$)', fontsize=14)
ax1.legend(loc='upper left', fontsize=9, frameon=True, edgecolor='0.7')
ax1.set_xlim(0, 5)
ax1.grid(True, linestyle=':', alpha=0.4)

# --- Right panel: Centrifugal stabilization factor ---
# Ratio n(Omega) / n(0) vs Omega R / c for fixed k
k_fixed_values = [0.5, 1.0, 2.0, 5.0]
colors_k = ['#2196F3', '#4CAF50', '#FF9800', '#F44336']

# Omega*R/c range
v_over_c = np.linspace(0.01, 0.95, 500)

# Lorentz factor
gamma_sq = 1.0 / (1.0 - v_over_c**2)
# Omega_rel = Omega * gamma^2
# For comparison, we normalize: let Omega be such that Omega*R/c = v/c
# Then Omega_rel = Omega * gamma^2

for j, k_f in enumerate(k_fixed_values):
    n0_sq_f = g_eff * k_f * A_rel

    ratio_newt = np.zeros_like(v_over_c)
    ratio_rel = np.zeros_like(v_over_c)

    for idx, vc in enumerate(v_over_c):
        # Newtonian: Omega_N ~ vc (in natural units with R=1, c=1)
        Om_N = vc
        n2_N = -2.0 * Om_N**2 + np.sqrt(4.0 * Om_N**4 + n0_sq_f**2)
        ratio_newt[idx] = np.sqrt(max(n2_N, 0)) / np.sqrt(n0_sq_f) if n0_sq_f > 0 else 0

        # Relativistic: Omega_rel = Omega * gamma^2
        Om_rel = vc * gamma_sq[idx]
        n2_rel = -2.0 * Om_rel**2 + np.sqrt(4.0 * Om_rel**4 + n0_sq_f**2)
        ratio_rel[idx] = np.sqrt(max(n2_rel, 0)) / np.sqrt(n0_sq_f) if n0_sq_f > 0 else 0

    ax2.plot(v_over_c, ratio_newt, '--', color=colors_k[j], linewidth=1.5, alpha=0.5)
    ax2.plot(v_over_c, ratio_rel, '-', color=colors_k[j], linewidth=2.0,
             label=rf'$k = {k_f}$')

# Add a legend entry for the line styles
ax2.plot([], [], '--', color='gray', linewidth=1.5, alpha=0.5, label='Newtonian')
ax2.plot([], [], '-', color='gray', linewidth=2.0, label='Relativistic')

ax2.set_xlabel(r'Co-rotation speed $\Omega R / c$', fontsize=14)
ax2.set_ylabel(r'$n(\Omega) / n(0)$', fontsize=14)
ax2.set_title('Centrifugal stabilization: Newtonian vs relativistic', fontsize=14)
ax2.legend(loc='upper right', fontsize=9, frameon=True, edgecolor='0.7', ncol=2)
ax2.set_xlim(0, 0.95)
ax2.set_ylim(0, 1.05)
ax2.grid(True, linestyle=':', alpha=0.4)
ax2.text(0.05, 0.05, 'Dashed: Newtonian\nSolid: Relativistic',
         transform=ax2.transAxes, fontsize=9,
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

fig.tight_layout()
fig.savefig('/data/haiyangw/claude/Instability/plots/ch10/fig_rotating_RT_accretion.pdf')
fig.savefig('/data/haiyangw/claude/Instability/plots/ch10/fig_rotating_RT_accretion.png')
print("Saved fig_rotating_RT_accretion.pdf and fig_rotating_RT_accretion.png")
plt.close(fig)
