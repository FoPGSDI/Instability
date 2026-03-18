"""
Bar chart: relativistic corrections to critical Rayleigh number
for 6 astrophysical systems.

Systems:
1. Water (lab): xi ~ 10^{-10}
2. Mercury (lab): xi ~ 10^{-9}
3. Liquid metal reactor: xi ~ 10^{-8}
4. Neutron star crust: xi ~ 0.015
5. Neutron star core: xi ~ 0.14
6. Quark-gluon plasma: xi ~ 0.33

Ra_c,rel / Ra_c,class = 1 + xi
Correction magnitude = xi * 100%
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# System data
systems = [
    'Water\n(lab)',
    'Mercury\n(lab)',
    'Liquid metal\nreactor',
    'NS crust\n($\\rho \\sim 10^{10}$)',
    'NS core\n($\\rho \\sim 10^{14}$)',
    'QGP\n($T \\sim 200$ MeV)'
]

xi_values = [1e-10, 3e-9, 5e-8, 0.015, 0.14, 0.333]
Ra_class = 1707.762  # both rigid boundaries

# Compute corrections
Ra_rel = [Ra_class * (1 + xi) for xi in xi_values]
correction_pct = [xi * 100 for xi in xi_values]
ratio = [1 + xi for xi in xi_values]

# Colors
bar_colors = ['#2196F3', '#2196F3', '#2196F3', '#E91E63', '#F44336', '#795548']

# ---- Plotting ----
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Left panel: bar chart of Ra_c,rel / Ra_c,class
ax1 = axes[0]
x = np.arange(len(systems))
bars = ax1.bar(x, ratio, color=bar_colors, edgecolor='black', lw=0.8, alpha=0.85)

# Add value labels
for i, (bar, r, xi) in enumerate(zip(bars, ratio, xi_values)):
    if xi < 1e-3:
        label = f'$1 + {xi:.0e}$'
    else:
        label = f'{r:.3f}'
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
             label, ha='center', va='bottom', fontsize=9)

ax1.axhline(y=1.0, ls='--', color='gray', lw=1.0, alpha=0.7)
ax1.set_xticks(x)
ax1.set_xticklabels(systems, fontsize=9)
ax1.set_ylabel(r'$\mathrm{Ra}_{c}^{\rm rel} / \mathrm{Ra}_{c}^{\rm class}$')
ax1.set_title('Relativistic correction factor $(1+\\xi)$')
ax1.set_ylim(0.95, 1.45)

# Right panel: log-scale bar chart of xi
ax2 = axes[1]
bars2 = ax2.bar(x, xi_values, color=bar_colors, edgecolor='black', lw=0.8, alpha=0.85)
ax2.set_yscale('log')

# Add value labels
for i, (bar, xi) in enumerate(zip(bars2, xi_values)):
    if xi < 1e-3:
        label = f'$\\xi = {xi:.0e}$'
    else:
        label = f'$\\xi = {xi:.3f}$'
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() * 1.5,
             label, ha='center', va='bottom', fontsize=9)

ax2.axhline(y=0.01, ls=':', color='red', lw=1.5, alpha=0.7, label='1% correction threshold')
ax2.set_xticks(x)
ax2.set_xticklabels(systems, fontsize=9)
ax2.set_ylabel(r'$\xi = p_0 / (\varepsilon_0 c^2)$')
ax2.set_title('Compactness parameter $\\xi$ across systems')
ax2.set_ylim(1e-11, 2)
ax2.legend(loc='upper left', fontsize=10)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_Ra_correction_systems.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_Ra_correction_systems.png')
print("Saved fig_Ra_correction_systems.pdf/png")
