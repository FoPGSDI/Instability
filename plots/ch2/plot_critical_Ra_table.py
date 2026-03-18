"""
Plot: Critical Ra comparison table - classical vs relativistic for NS and QGP.
Bar chart and parameter space showing how xi shifts the onset condition.
"""
import sys; sys.path.insert(0, '../..'); from SHARED_PLOT_STYLE import setup_style, COLORS
setup_style()

import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# --- Panel (a): Bar chart of critical Ra for different regimes ---
boundary_types = ['Both free', 'Mixed', 'Both rigid']
Ra_class = np.array([657.511, 1100.65, 1707.762])

regimes = {
    'Classical': {'xi': 0, 'color': COLORS['classical']},
    'NS crust ($\\xi=0.015$)': {'xi': 0.015, 'color': COLORS['neutron_star']},
    'NS core ($\\xi=0.15$)': {'xi': 0.15, 'color': COLORS['accretion']},
    'QGP ($\\xi=1/3$)': {'xi': 1./3, 'color': COLORS['qgp']},
}

x = np.arange(len(boundary_types))
width = 0.18
multiplier = 0

for regime_name, props in regimes.items():
    Ra_rel = Ra_class * (1 + props['xi'])
    offset = width * multiplier
    bars = ax1.bar(x + offset, Ra_rel, width, label=regime_name,
                   color=props['color'], edgecolor='black', linewidth=0.5, alpha=0.85)
    multiplier += 1

ax1.set_xlabel('Boundary configuration', fontsize=13)
ax1.set_ylabel(r'$R_c^{\mathrm{rel}} = R_c^{\mathrm{class}}(1+\xi)$', fontsize=13)
ax1.set_title('(a) Critical Rayleigh numbers', fontsize=12)
ax1.set_xticks(x + 1.5 * width)
ax1.set_xticklabels(boundary_types, fontsize=10)
ax1.legend(fontsize=9, loc='upper left')

# Add percentage annotations for QGP case
for i, ra in enumerate(Ra_class):
    pct = 100 * (1./3)
    ax1.annotate(f'+{pct:.0f}%', (x[i] + 3*width, ra * (1 + 1./3)),
                 textcoords="offset points", xytext=(0, 5), fontsize=8,
                 ha='center', color=COLORS['qgp'])

# --- Panel (b): Ra_c(a) curves for classical and relativistic ---
a = np.linspace(0.5, 8, 500)

# Both-free: Ra = (pi^2 + a^2)^3 / a^2
Ra_a_free = (np.pi**2 + a**2)**3 / a**2

xi_values = [0, 0.015, 0.15, 1./3]
labels = ['Classical', r'NS crust ($\xi=0.015$)', r'NS core ($\xi=0.15$)', r'QGP ($\xi=1/3$)']
colors = [COLORS['classical'], COLORS['neutron_star'], COLORS['accretion'], COLORS['qgp']]

for xi_val, label, color in zip(xi_values, labels, colors):
    Ra_rel_a = Ra_a_free * (1 + xi_val)
    ax2.semilogy(a, Ra_rel_a, '-', color=color, linewidth=2, label=label)
    # Mark minimum
    a_min = np.pi / np.sqrt(2)
    Ra_min = 27 * np.pi**4 / 4 * (1 + xi_val)
    ax2.plot(a_min, Ra_min, 'o', color=color, markersize=6, zorder=5)

ax2.set_xlabel(r'Horizontal wavenumber $a = kd$', fontsize=14)
ax2.set_ylabel(r'$R_c^{\mathrm{rel}}(a)$', fontsize=14)
ax2.set_title('(b) Marginal stability curves (both free)', fontsize=12)
ax2.set_xlim(0.5, 8)
ax2.set_ylim(400, 1e5)
ax2.legend(fontsize=9)

# Mark critical wavenumber
ax2.axvline(np.pi/np.sqrt(2), color='gray', linestyle=':', alpha=0.5)
ax2.text(np.pi/np.sqrt(2) + 0.1, 500, r'$a_c = \pi/\sqrt{2}$', fontsize=9, color='gray')

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/ch2/fig_critical_Ra_table.pdf')
plt.close()
print("Saved fig_critical_Ra_table.pdf")
