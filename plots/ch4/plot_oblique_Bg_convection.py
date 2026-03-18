#!/usr/bin/env python3
"""
Agent 15: Magnetar interior — oblique B+g thermal convection.
Plot effective Q_rel vs angle theta for different v_A^2/c^2,
and overstable frequency shift.
"""
import sys; sys.path.insert(0, '/data/haiyangw/claude/Instability'); from SHARED_PLOT_STYLE import setup_style, COLORS, pi
import matplotlib.pyplot as plt
import numpy as np

setup_style()

theta = np.linspace(0, pi/2, 200)  # angle between B and g

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Left: Q_rel/Q_class vs theta for various v_A^2/c^2
Q_class_ratio = np.cos(theta)**2  # Q depends on cos^2(theta)

for vA2_c2, color, lbl in [
    (0.0, COLORS['classical'], 'Classical'),
    (0.01, '#4CAF50', r'$v_A^2/c^2 = 0.01$'),
    (0.05, '#FF9800', r'$v_A^2/c^2 = 0.05$'),
    (0.1, '#F44336', r'$v_A^2/c^2 = 0.1$'),
    (0.3, '#9C27B0', r'$v_A^2/c^2 = 0.3$'),
]:
    Q_ratio = np.cos(theta)**2 / (1 + vA2_c2)
    ls = '-' if vA2_c2 == 0 else '--'
    ax1.plot(np.degrees(theta), Q_ratio, ls, color=color, lw=2, label=lbl)

ax1.set_xlabel(r'Angle $\vartheta$ between $\mathbf{B}$ and $\mathbf{g}$ (degrees)')
ax1.set_ylabel(r'$Q_{\mathrm{rel}} / Q_{\mathrm{class}}(\vartheta=0)$')
ax1.set_title(r'Effective Chandrasekhar number vs field inclination')
ax1.legend(fontsize=9)
ax1.set_xlim(0, 90)
ax1.set_ylim(0, 1.05)

# Right: Overstable frequency shift
Q_rel_values = np.array([10, 100, 1000])
vA2_c2_range = np.linspace(0, 0.3, 200)

for Q_val, color in zip(Q_rel_values, ['#2196F3', '#F44336', '#4CAF50']):
    theta_45 = pi/4
    freq_ratio = np.sqrt(1 - vA2_c2_range * Q_val * np.cos(theta_45)**2 /
                         (Q_val * np.cos(theta_45)**2 + pi**2))
    freq_ratio = np.maximum(freq_ratio, 0)
    ax2.plot(vA2_c2_range, freq_ratio, '-', color=color, lw=2,
             label=r'$Q_{\mathrm{rel}} = %d$' % Q_val)

ax2.set_xlabel(r'$v_A^2 / c^2$')
ax2.set_ylabel(r'$\sigma_{\mathrm{rel}} / \sigma_{\mathrm{class}}$')
ax2.set_title(r'Overstable frequency shift ($\vartheta = 45^\circ$)')
ax2.legend(fontsize=10)
ax2.set_xlim(0, 0.3)
ax2.set_ylim(0, 1.05)

fig.tight_layout()
fig.savefig('/data/haiyangw/claude/Instability/plots/ch4/fig_oblique_Bg_convection.pdf')
fig.savefig('/data/haiyangw/claude/Instability/plots/ch4/fig_oblique_Bg_convection.png')
print("Saved fig_oblique_Bg_convection.pdf/png")
