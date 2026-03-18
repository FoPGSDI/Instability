"""
Plot: Experimental/observational parameter space for relativistic thermal instability.
Shows where different astrophysical systems fall in the (Ra, xi) plane.
"""
import sys; sys.path.insert(0, '../..'); from SHARED_PLOT_STYLE import setup_style, COLORS
setup_style()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))

# --- Panel (a): Parameter space: Ra vs xi ---
# Astrophysical systems with estimated Ra ranges

systems = {
    'Proto-NS\nconvection': {
        'Ra_min': 1e6, 'Ra_max': 1e10,
        'xi_min': 0.05, 'xi_max': 0.2,
        'color': COLORS['neutron_star']
    },
    'NS ocean\n(accreting)': {
        'Ra_min': 1e4, 'Ra_max': 1e8,
        'xi_min': 0.005, 'xi_max': 0.03,
        'color': '#E91E63'
    },
    'Accretion disk\n(inner, rad.-dom.)': {
        'Ra_min': 1e8, 'Ra_max': 1e14,
        'xi_min': 0.2, 'xi_max': 0.35,
        'color': COLORS['accretion']
    },
    'QGP fireball': {
        'Ra_min': 1, 'Ra_max': 1e3,
        'xi_min': 0.25, 'xi_max': 0.4,
        'color': COLORS['qgp']
    },
    'Early universe\n(sub-horizon)': {
        'Ra_min': 1e2, 'Ra_max': 1e6,
        'xi_min': 0.30, 'xi_max': 0.35,
        'color': COLORS['jet']
    },
    'White dwarf\nenvelope': {
        'Ra_min': 1e6, 'Ra_max': 1e12,
        'xi_min': 1e-6, 'xi_max': 1e-4,
        'color': COLORS['data']
    },
}

for name, props in systems.items():
    width = np.log10(props['xi_max']) - np.log10(props['xi_min'])
    height = np.log10(props['Ra_max']) - np.log10(props['Ra_min'])
    x = np.log10(props['xi_min'])
    y = np.log10(props['Ra_min'])

    rect = plt.Rectangle((x, y), width, height, facecolor=props['color'],
                          alpha=0.4, edgecolor=props['color'], linewidth=2)
    ax1.add_patch(rect)
    ax1.text(x + width/2, y + height/2, name, ha='center', va='center',
             fontsize=8, fontweight='bold')

# Critical Ra lines
for bc_name, Ra_c in [('Both free', 657.511), ('Both rigid', 1707.762)]:
    xi_line = np.logspace(-6, 0, 100)
    Ra_crit_line = Ra_c * (1 + xi_line)
    ax1.plot(np.log10(xi_line), np.log10(Ra_crit_line), '--',
             color='black', linewidth=1.5, alpha=0.7)
    ax1.text(-0.5, np.log10(Ra_c) + 0.1, f'{bc_name}\n$R_c={Ra_c:.0f}$',
             fontsize=8, color='black')

# Shade stable region
xi_fill = np.logspace(-6, 0, 100)
ax1.fill_between(np.log10(xi_fill), 0, np.log10(657.511 * (1 + xi_fill)),
                  alpha=0.05, color='blue')
ax1.text(-4, 1.5, 'STABLE', fontsize=14, color='blue', alpha=0.3, fontweight='bold')

ax1.set_xlim(-6, 0.5)
ax1.set_ylim(0, 15)
ax1.set_xlabel(r'$\log_{10}\,\xi$', fontsize=14)
ax1.set_ylabel(r'$\log_{10}\,\mathrm{Ra}$', fontsize=14)
ax1.set_title('(a) Astrophysical parameter space', fontsize=12)

# --- Panel (b): Observational signatures ---
# Show how relativistic corrections affect observable quantities

xi = np.linspace(0, 0.5, 200)

# Convective heat flux enhancement
# F_conv ~ (Ra - Ra_c)^gamma, gamma ~ 1/3 near onset
# Relativistic: Ra_c increases by (1+xi), so F_conv decreases for same DeltaT
F_ratio = 1.0 / (1 + xi)**0.33  # heat flux suppression

# Convective velocity (for same supercriticality)
# v_conv ~ sqrt(alpha * g * DeltaT * d / (1 + xi))
v_ratio = 1.0 / np.sqrt(1 + xi)

# Cell size (critical wavenumber unchanged)
cell_ratio = np.ones_like(xi)  # a_c unchanged, cell size unchanged

# Frequency of oscillatory modes (if any)
# Near onset, frequency ~ 0 (exchange of stabilities)
# But for overstable modes: omega ~ sqrt(Ra - Ra_c) * (1 + xi)^{-1/2}

ax2.plot(xi, F_ratio, '-', color=COLORS['relativistic'], linewidth=2.5,
         label=r'$F_{\mathrm{conv}}^{\mathrm{rel}}/F_{\mathrm{conv}}^{\mathrm{class}}$')
ax2.plot(xi, v_ratio, '--', color=COLORS['bdnk'], linewidth=2.5,
         label=r'$v_{\mathrm{conv}}^{\mathrm{rel}}/v_{\mathrm{conv}}^{\mathrm{class}}$')
ax2.plot(xi, cell_ratio, ':', color=COLORS['classical'], linewidth=2,
         label='Cell size (unchanged)')

# Mark specific systems
for xi_val, name, color in [(0.015, 'NS crust', COLORS['neutron_star']),
                              (0.15, 'NS core', COLORS['accretion']),
                              (1./3, 'QGP', COLORS['qgp'])]:
    ax2.axvline(xi_val, color=color, linestyle=':', alpha=0.3)
    ax2.text(xi_val + 0.01, 1.02, name, fontsize=9, color=color, rotation=90, va='bottom')

ax2.set_xlabel(r'$\xi = p_0/(\varepsilon_0 c^2)$', fontsize=14)
ax2.set_ylabel('Ratio to classical value', fontsize=14)
ax2.set_title('(b) Observable signatures of relativistic convection', fontsize=12)
ax2.legend(fontsize=10, loc='lower left')
ax2.set_ylim(0.6, 1.1)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/ch2/fig_observational_parameter_space.pdf')
plt.close()
print("Saved fig_observational_parameter_space.pdf")
