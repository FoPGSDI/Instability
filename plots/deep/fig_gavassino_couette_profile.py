#!/usr/bin/env python3
"""
fig_gavassino_couette_profile.py
Plot Gavassino's exact Couette solution:
  u(x) = tan[ (2x/L) * arctan(v / sqrt(1-v^2)) ]
for v/c = 0.1, 0.5, 0.9, 0.99.
Compare with the Newtonian linear profile u = 2vx/L.

Reference: Gavassino, Niekamp, Schlichting & Denicol (2025), arXiv:2512.10420
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

x_over_L = np.linspace(-0.499, 0.499, 500)  # x/L in [-0.5, 0.5]

velocities = [0.1, 0.5, 0.9, 0.99]
colors = ['#2196F3', '#4CAF50', '#F44336', '#9C27B0']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Left panel: velocity profiles
for v, col in zip(velocities, colors):
    gamma_v = v / np.sqrt(1 - v**2)
    phi = np.arctan(gamma_v)
    u_exact = np.tan(2 * x_over_L * phi)
    u_newton = 2 * v * x_over_L

    ax1.plot(x_over_L, u_exact, color=col, linewidth=2.0,
             label=f'$v/c = {v}$ (Gavassino)')
    ax1.plot(x_over_L, u_newton, color=col, linewidth=1.2,
             linestyle='--', alpha=0.6)

ax1.set_xlabel('$x/L$')
ax1.set_ylabel('$u(x)$')
ax1.set_title('Gavassino exact Couette profile vs Newtonian linear')
ax1.legend(loc='upper left', fontsize=10)
ax1.set_xlim(-0.5, 0.5)
ax1.axhline(y=0, color='gray', linewidth=0.5)
ax1.axvline(x=0, color='gray', linewidth=0.5)

# Add annotation for dashed = Newtonian
ax1.text(0.35, -0.3, 'dashed = Newtonian', fontsize=9, color='gray',
         ha='center')

# Right panel: deviation from linearity (u_exact - u_linear) / v
for v, col in zip(velocities, colors):
    gamma_v = v / np.sqrt(1 - v**2)
    phi = np.arctan(gamma_v)
    u_exact = np.tan(2 * x_over_L * phi)
    u_newton = 2 * v * x_over_L
    deviation = (u_exact - u_newton)
    if v > 0:
        deviation /= v
    ax2.plot(x_over_L, deviation, color=col, linewidth=2.0,
             label=f'$v/c = {v}$')

ax2.set_xlabel('$x/L$')
ax2.set_ylabel('$(u_{\\mathrm{exact}} - u_{\\mathrm{Newton}})/v$')
ax2.set_title('Deviation from linear profile (normalized)')
ax2.legend(loc='upper left', fontsize=10)
ax2.set_xlim(-0.5, 0.5)
ax2.axhline(y=0, color='gray', linewidth=0.5)

plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), 'fig_gavassino_couette_profile.pdf'))
plt.savefig(os.path.join(os.path.dirname(__file__), 'fig_gavassino_couette_profile.png'))
print('Saved fig_gavassino_couette_profile.pdf')
