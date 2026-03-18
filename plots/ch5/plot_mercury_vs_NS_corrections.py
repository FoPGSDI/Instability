#!/usr/bin/env python3
"""
Agent 18: Mercury lab vs NS — comparison table + correction magnitude plot.
Shows the magnitude of relativistic corrections across environments.
"""
import sys; sys.path.insert(0, '/data/haiyangw/claude/Instability'); from SHARED_PLOT_STYLE import setup_style, COLORS, pi, c_cgs
import matplotlib.pyplot as plt
import numpy as np

setup_style()

# Systems and their characteristic parameters
systems = [
    'Mercury\n(lab)',
    'Solar\ninterior',
    'White\ndwarf',
    'NS\nouter crust',
    'NS\ncore',
    'Magnetar\ninterior',
]
vA2_c2 = [1e-20, 1e-13, 1e-9, 1e-5, 1e-2, 1e-1]
Omega_d_c2 = [1e-20, 1e-18, 1e-15, 1e-10, 1e-8, 1e-8]
p_rho_c2 = [1e-15, 1e-5, 1e-4, 1e-3, 0.1, 0.3]

x = np.arange(len(systems))

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Top panel: individual corrections
width = 0.25
bars1 = ax1.bar(x - width, vA2_c2, width, color=COLORS['relativistic'],
                label=r'$v_A^2/c^2$ (magnetic)', log=True)
bars2 = ax1.bar(x, Omega_d_c2, width, color=COLORS['classical'],
                label=r'$\Omega^2 d^2/c^2$ (rotation)', log=True)
bars3 = ax1.bar(x + width, p_rho_c2, width, color=COLORS['bdnk'],
                label=r'$p/(\rho c^2)$ (thermal)', log=True)

ax1.set_ylabel('Correction magnitude')
ax1.set_title('Magnitude of relativistic corrections across astrophysical systems')
ax1.legend(fontsize=10)
ax1.set_ylim(1e-22, 1)
ax1.axhline(1e-2, color='gray', ls='--', lw=1, alpha=0.5)
ax1.text(5.5, 2e-2, '1% level', fontsize=9, color='gray')

# Bottom panel: total fractional correction to Ra_c
total_correction = [max(a, b, c) for a, b, c in zip(vA2_c2, Omega_d_c2, p_rho_c2)]
colors_bar = ['#2196F3' if tc < 1e-6 else '#FF9800' if tc < 1e-2 else '#F44336'
              for tc in total_correction]

ax2.bar(x, total_correction, 0.6, color=colors_bar, log=True, edgecolor='k', lw=0.5)
ax2.set_ylabel(r'$|\Delta \mathrm{Ra}_c / \mathrm{Ra}_c|$ (leading order)')
ax2.set_xlabel('Astrophysical system')
ax2.set_xticks(x)
ax2.set_xticklabels(systems, fontsize=10)
ax2.set_ylim(1e-22, 1)

ax2.axhline(1e-2, color='gray', ls='--', lw=1, alpha=0.5)
ax2.text(5.5, 2e-2, '1% threshold', fontsize=9, color='gray')

# Color legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#2196F3', label='Negligible (<$10^{-6}$)'),
    Patch(facecolor='#FF9800', label='Small ($10^{-6}$--$10^{-2}$)'),
    Patch(facecolor='#F44336', label='Significant (>$10^{-2}$)'),
]
ax2.legend(handles=legend_elements, fontsize=9.5, loc='upper left')

fig.tight_layout()
fig.savefig('/data/haiyangw/claude/Instability/plots/ch5/fig_mercury_vs_NS_corrections.pdf')
fig.savefig('/data/haiyangw/claude/Instability/plots/ch5/fig_mercury_vs_NS_corrections.png')
print("Saved fig_mercury_vs_NS_corrections.pdf/png")
