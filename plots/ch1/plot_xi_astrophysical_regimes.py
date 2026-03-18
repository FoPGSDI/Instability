"""
Plot: Relativistic parameter xi = p/(epsilon*c^2) across astrophysical regimes.
Shows where relativistic corrections become significant for various systems.
"""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')); from SHARED_PLOT_STYLE import setup_style, COLORS
setup_style()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(10, 6))

# Define astrophysical regimes with their xi ranges and characteristic temperatures/densities
regimes = {
    'Laboratory water': {'xi_min': 1e-21, 'xi_max': 1e-19, 'color': COLORS['classical'], 'y': 0.5},
    'Liquid metals': {'xi_min': 1e-12, 'xi_max': 1e-9, 'color': COLORS['classical'], 'y': 1.5},
    'White dwarf': {'xi_min': 1e-7, 'xi_max': 1e-5, 'color': COLORS['data'], 'y': 2.5},
    'NS crust': {'xi_min': 5e-4, 'xi_max': 5e-2, 'color': COLORS['neutron_star'], 'y': 3.5},
    'NS core': {'xi_min': 0.05, 'xi_max': 0.3, 'color': COLORS['neutron_star'], 'y': 4.5},
    'Accretion disk\n(inner)': {'xi_min': 0.1, 'xi_max': 0.35, 'color': COLORS['accretion'], 'y': 5.5},
    'QGP\n(T~200 MeV)': {'xi_min': 0.25, 'xi_max': 0.4, 'color': COLORS['qgp'], 'y': 6.5},
    'Early universe\n(radiation era)': {'xi_min': 0.3, 'xi_max': 0.35, 'color': COLORS['jet'], 'y': 7.5},
}

for name, props in regimes.items():
    ax.barh(props['y'], np.log10(props['xi_max']) - np.log10(props['xi_min']),
            left=np.log10(props['xi_min']), height=0.7, color=props['color'],
            alpha=0.7, edgecolor='black', linewidth=0.8)
    # Label on left
    ax.text(np.log10(props['xi_min']) - 0.3, props['y'], name,
            ha='right', va='center', fontsize=10)

# Mark where corrections become significant (1% level)
xi_1pct = np.log10(0.01)
ax.axvline(xi_1pct, color='red', linestyle='--', linewidth=2, alpha=0.8)
ax.text(xi_1pct + 0.1, 8.2, r'1% correction ($\xi = 0.01$)',
        color='red', fontsize=11, ha='left')

# Mark where corrections are order unity
xi_unity = np.log10(1.0/3)
ax.axvline(xi_unity, color='darkred', linestyle='-.', linewidth=2, alpha=0.8)
ax.text(xi_unity + 0.1, 8.6, r'$\mathcal{O}(1)$ correction ($\xi = 1/3$)',
        color='darkred', fontsize=11, ha='left')

# Secondary axis showing Ra_rel/Ra = 1 + xi
ax2 = ax.twiny()
xi_vals = np.array([1e-20, 1e-15, 1e-10, 1e-5, 1e-3, 0.01, 0.1, 1.0/3])
correction_pct = xi_vals * 100
ax2.set_xlim(ax.get_xlim())
tick_positions = np.log10(xi_vals)
tick_labels = [f'{c:.0e}%' if c < 0.1 else f'{c:.1f}%' if c < 10 else f'{c:.0f}%' for c in correction_pct]
ax2.set_xticks(tick_positions)
ax2.set_xticklabels(tick_labels, fontsize=8)
ax2.set_xlabel(r'Relativistic correction to $\mathrm{Ra}_c$: $\Delta\mathrm{Ra}/\mathrm{Ra} \approx \xi$', fontsize=12)

ax.set_xlim(-22, 1)
ax.set_ylim(-0.3, 9.2)
ax.set_xlabel(r'$\log_{10}\,\xi$ where $\xi = p_0 / (\varepsilon_0 c^2)$', fontsize=14)
ax.set_yticks([])
ax.set_title(r'Relativistic Compactness Parameter $\xi$ Across Astrophysical Regimes', fontsize=14, pad=40)

# Shaded regions
ax.axvspan(-22, xi_1pct, alpha=0.05, color='blue', label='Classical regime')
ax.axvspan(xi_1pct, 1, alpha=0.08, color='red', label='Relativistic regime')

ax.legend(loc='lower right', fontsize=10)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/ch1/fig_xi_astrophysical_regimes.pdf')
plt.close()
print("Saved fig_xi_astrophysical_regimes.pdf")
