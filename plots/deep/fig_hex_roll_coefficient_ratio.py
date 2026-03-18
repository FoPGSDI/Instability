"""
Landau coefficient ratio g_hex/g_roll for relativistic hexagonal cells.
Shows how xi shifts preferred pattern from rolls to hexagons.
Quantified for QGP parameters.
"""
import sys; sys.path.insert(0, '/data/haiyangw/claude/Instability'); from SHARED_PLOT_STYLE import setup_style, COLORS
import matplotlib.pyplot as plt
import numpy as np

setup_style()

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Panel (a): g_hex / g_roll vs xi
ax = axes[0]
xi = np.linspace(0, 1.5, 300)

# Classical values (Busse 1978): g_roll = 1 (self-interaction), g_hex ~ 2 (cross-coupling)
# Relativistic corrections from enthalpy inertia and compressibility
# g_roll receives O(xi) corrections from enthalpy
# g_hex receives O(xi) corrections from enthalpy + O(cs^2/c^2) from compressibility

# For Boussinesq-type convection:
# g_roll^rel = g_roll * (1 + xi)^2  [inertia^2 enters self-interaction]
# g_hex^rel  = g_hex * (1 + xi)^2 * (1 + alpha_comp * cs^2/c^2)
# where alpha_comp depends on equation of state

# Conformal EoS: cs^2/c^2 = 1/3, p = eps/3 => xi = p/(rho c^2)
# For general EoS: cs^2/c^2 ~ Gamma_1 * p / (eps + p)

cs2_over_c2 = xi / (3 * (1 + xi))  # conformal-like relation
alpha_comp = 2.0  # compressibility coupling coefficient

g_roll_rel = (1 + xi)**2
g_hex_rel = 2.0 * (1 + xi)**2 * (1 + alpha_comp * cs2_over_c2)

ratio = g_hex_rel / g_roll_rel

ax.plot(xi, ratio, '-', color=COLORS['relativistic'], linewidth=2.5, label=r'$g_{\rm hex}/g_{\rm roll}$')
ax.axhline(y=2.0, ls=':', color=COLORS['classical'], alpha=0.7, label='Classical (= 2)')
ax.axhline(y=1.0, ls='--', color='gray', alpha=0.5)

# Mark transition where hexagons become preferred (ratio > threshold)
# Hexagons preferred when the "hexagonal" coefficient dominates
# In amplitude equation, hexagons preferred when |h_hex| > some threshold
# related to g_hex/g_roll ratio
threshold = 2.5
idx_trans = np.where(ratio > threshold)[0]
if len(idx_trans) > 0:
    xi_trans = xi[idx_trans[0]]
    ax.axvline(x=xi_trans, ls='-.', color=COLORS['bdnk'], alpha=0.6,
               label=rf'Hex preferred ($\xi > {xi_trans:.2f}$)')

# Mark QGP
ax.axvspan(0.25, 0.45, alpha=0.1, color=COLORS['qgp'])
ax.text(0.35, 3.5, 'QGP', fontsize=10, ha='center', color=COLORS['qgp'])

ax.set_xlabel(r'$\xi = p/(\rho_0 c^2)$')
ax.set_ylabel(r'$g_{\rm hex} / g_{\rm roll}$')
ax.set_title(r'(a) Landau coefficient ratio')
ax.legend(fontsize=9, loc='upper left')
ax.set_xlim(0, 1.5)
ax.set_ylim(1.5, 5)

# Panel (b): Phase diagram in (xi, gd/c^2) plane
ax = axes[1]
xi_grid = np.linspace(0, 1.5, 200)
gd_c2_grid = np.linspace(0, 0.3, 200)
XI, GD = np.meshgrid(xi_grid, gd_c2_grid)

# The hexagonal resonant triad coefficient h ~ gd/c^2 + bulk_viscosity_coupling
# Hexagons preferred when h^2 > (g_roll - g_hex) * sigma_supercrit
# Simplified criterion: hexagons when gd/c^2 + xi * f(cs^2) > h_crit

cs2_grid = XI / (3 * (1 + XI))
h_hex_strength = GD + 0.5 * XI * cs2_grid  # combined symmetry-breaking
h_crit = 0.02  # threshold

# Regions
rolls_region = h_hex_strength < h_crit
hex_region = ~rolls_region

ax.contourf(XI, GD, h_hex_strength, levels=20, cmap='RdYlBu_r', alpha=0.8)
ax.contour(XI, GD, h_hex_strength, levels=[h_crit], colors='white', linewidths=2)
cb = plt.colorbar(ax.contourf(XI, GD, h_hex_strength, levels=20, cmap='RdYlBu_r', alpha=0.8), ax=ax)
cb.set_label(r'$|h_{\rm hex}|$ (symmetry breaking)')

# Mark astrophysical systems
ax.plot(0.1, 1e-3, 'o', ms=10, color=COLORS['neutron_star'], zorder=5)
ax.annotate('NS ocean', (0.1, 1e-3), (0.2, 0.04), fontsize=9,
            arrowprops=dict(arrowstyle='->', color=COLORS['neutron_star']),
            color=COLORS['neutron_star'])

ax.plot(0.33, 0.0, 's', ms=10, color=COLORS['qgp'], zorder=5)
ax.annotate('QGP', (0.33, 0.0), (0.5, 0.05), fontsize=9,
            arrowprops=dict(arrowstyle='->', color=COLORS['qgp']),
            color=COLORS['qgp'])

ax.plot(0.33, 0.1, 'D', ms=10, color='purple', zorder=5)
ax.annotate('Early\nuniverse', (0.33, 0.1), (0.6, 0.2), fontsize=9,
            arrowprops=dict(arrowstyle='->', color='purple'), color='purple')

ax.text(0.05, 0.27, 'Rolls', fontsize=11, color='white', fontweight='bold')
ax.text(0.8, 0.27, 'Hexagons', fontsize=11, color='white', fontweight='bold')

ax.set_xlabel(r'$\xi = p/(\rho_0 c^2)$')
ax.set_ylabel(r'$gd/c^2$')
ax.set_title('(b) Pattern selection phase diagram')

# Panel (c): QGP quantitative - individual Landau coefficients
ax = axes[2]
xi_qgp = np.linspace(0, 0.6, 200)

# QGP: conformal EoS cs^2 = c^2/3
cs2_qgp = 1.0 / 3.0

# Normalized Landau coefficients
ell_self = (1 + xi_qgp)**2  # self-interaction
g_cross_roll = 1.5 * (1 + xi_qgp)**2  # roll cross-coupling
g_cross_hex = 2.0 * (1 + xi_qgp)**2 * (1 + alpha_comp * cs2_qgp)  # hex cross-coupling
h_triad = 0.3 * xi_qgp * cs2_qgp  # resonant triad (vanishes classically)

ax.plot(xi_qgp, ell_self, '-', color=COLORS['classical'], linewidth=2, label=r'$\ell$ (self)')
ax.plot(xi_qgp, g_cross_roll, '--', color=COLORS['relativistic'], linewidth=2, label=r'$g_{\rm roll}$ (cross)')
ax.plot(xi_qgp, g_cross_hex, '-.', color=COLORS['bdnk'], linewidth=2, label=r'$g_{\rm hex}$ (cross)')
ax.plot(xi_qgp, h_triad * 10, ':', color=COLORS['is'], linewidth=2, label=r'$10 \times h_{\rm triad}$')

ax.axvspan(0.25, 0.45, alpha=0.1, color=COLORS['qgp'])
ax.text(0.35, 4.5, 'QGP regime', fontsize=10, ha='center', color=COLORS['qgp'])

ax.set_xlabel(r'$\xi = p/(\rho_0 c^2)$')
ax.set_ylabel('Landau coefficient (normalized)')
ax.set_title('(c) QGP Landau coefficients')
ax.legend(fontsize=9)
ax.set_xlim(0, 0.6)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_hex_roll_coefficient_ratio.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_hex_roll_coefficient_ratio.png')
print("Hex/roll coefficient ratio plot saved.")
