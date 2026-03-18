"""
Plot: Cell pattern selection diagram for relativistic convection.
Shows how relativistic effects (xi, gd/c^2) can shift pattern preference.
"""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')); from SHARED_PLOT_STYLE import setup_style, COLORS
setup_style()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon, FancyArrowPatch

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# --- Panel (a): Pattern selection phase diagram ---
# Axes: gd/c^2 (gravitational redshift) vs cs^2/c^2 (compressibility)

gd_c2 = np.linspace(0, 0.1, 200)
cs2_c2 = np.linspace(0, 0.4, 200)
GD, CS2 = np.meshgrid(gd_c2, cs2_c2)

# Schematic pattern selection criterion:
# Rolls preferred when both gd/c^2 and cs^2/c^2 are small
# Hexagons preferred when non-Boussinesq effects are large
# The transition depends on the Landau coefficient h (resonant triad)
# h ~ gd/c^2 + (cs/c)^2 * f(Pr)
h_param = GD * 10 + CS2 * 0.5  # schematic amplitude of hexagonal tendency

# Regions
ax1.contourf(GD, CS2, h_param, levels=[0, 0.05, 0.15, 0.5, 2.0],
             colors=['#E3F2FD', '#BBDEFB', '#FFE0B2', '#FFCC80'], alpha=0.7)
ax1.contour(GD, CS2, h_param, levels=[0.05, 0.15], colors='black',
            linewidths=[1.5, 1.5], linestyles=['--', '-'])

# Labels
ax1.text(0.01, 0.05, 'Rolls\nstable', fontsize=12, fontweight='bold', color=COLORS['classical'])
ax1.text(0.04, 0.25, 'Hexagons\npreferred', fontsize=12, fontweight='bold', color=COLORS['jet'])
ax1.text(0.07, 0.35, 'Strong\nnon-Boussinesq', fontsize=10, color='brown')

# Mark astrophysical regimes
astro = {
    'Laboratory': (1e-18, 1e-10, COLORS['classical']),
    'NS crust': (0.01, 0.1, COLORS['neutron_star']),
    'NS core': (0.03, 0.25, COLORS['accretion']),
    'QGP': (0.001, 0.33, COLORS['qgp']),
}
for name, (x, y, c) in astro.items():
    if x > 0.001:
        ax1.plot(x, y, 'o', color=c, markersize=10, zorder=5, markeredgecolor='black')
        ax1.annotate(name, (x, y), textcoords="offset points", xytext=(8, 5), fontsize=9)

ax1.set_xlabel(r'Gravitational redshift $gd/c^2$', fontsize=13)
ax1.set_ylabel(r'Compressibility $c_s^2/c^2$', fontsize=13)
ax1.set_title('(a) Pattern selection phase diagram', fontsize=12)

# --- Panel (b): Schematic of roll vs hexagon aspect ratio ---
# Show how a_rel changes the cell dimensions

xi_vals = np.linspace(0, 0.5, 100)
gd_c2_val = 0.01  # typical NS

# Roll wavelength ratio
a_class = 3.117  # critical wavenumber for rigid-rigid
# a_rel^2 = a^2 * (1 + p/(e+p) * 2*Phi/c^2) ~ a^2 * (1 + xi*gd/c^2)
a_rel = a_class * np.sqrt(1 + xi_vals * 2 * gd_c2_val)
L_ratio = a_class / a_rel  # ratio of relativistic to classical cell size

ax2_twin = ax2

# Plot cell size ratio
ax2.plot(xi_vals, L_ratio, '-', color=COLORS['relativistic'], linewidth=2.5,
         label=r'Cell size ratio $L_{\mathrm{rel}}/L_{\mathrm{class}}$')

# Plot Landau coefficient enhancement
ell_ratio = 1 + xi_vals  # self-interaction enhanced by enthalpy
g_ratio = 1 + 1.5 * xi_vals  # cross-coupling more strongly enhanced
h_ratio = xi_vals * 10 * gd_c2_val  # hexagonal coefficient

ax2.plot(xi_vals, ell_ratio, '--', color=COLORS['bdnk'], linewidth=2,
         label=r'$\ell_{\mathrm{rel}}/\ell_{\mathrm{class}}$ (self-interaction)')
ax2.plot(xi_vals, g_ratio, '-.', color=COLORS['is'], linewidth=2,
         label=r'$g_{\mathrm{rel}}/g_{\mathrm{class}}$ (cross-coupling)')

ax2.set_xlabel(r'$\xi = p_0/(\varepsilon_0 c^2)$', fontsize=14)
ax2.set_ylabel('Ratio to classical value', fontsize=14)
ax2.set_title(r'(b) Landau coefficients vs $\xi$ ($gd/c^2=0.01$)', fontsize=12)
ax2.legend(fontsize=9)
ax2.set_ylim(0.95, 1.8)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/ch2/fig_cell_pattern_selection.pdf')
plt.close()
print("Saved fig_cell_pattern_selection.pdf")
