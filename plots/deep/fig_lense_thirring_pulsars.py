#!/usr/bin/env python3
"""
Deep Research Agent 3 -- Lense-Thirring quantification for specific pulsars.

Plots Omega_LT / Omega vs spin frequency for specific pulsars:
  - PSR J0737-3039A (double pulsar): f=44.05 Hz, M=1.338 Msun, C~0.18
  - PSR J1748-2446ad (fastest spinner): f=716 Hz, M~2.0 Msun, C~0.25
  - PSR J0437-4715 (nearby MSP): f=173.7 Hz, M=1.44 Msun, C~0.20
  - PSR B1937+21 (classic MSP): f=641.9 Hz, M~1.4 Msun, C~0.20
  - PSR J1614-2230 (massive): f=317.4 Hz, M=1.97 Msun, C~0.26

Also computes the frame-dragging reduction of Ta_rel for each pulsar.

References:
  - Hartle (1967), slow rotation formalism
  - Paschalidis & Stergioulas (2017), Living Rev. Relativ. 20, 7
  - Hessels et al. (2006), fastest pulsar
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS, G_cgs, c_cgs, M_sun
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# --- Pulsar data ---
pulsars = {
    'J0737-3039A': {
        'f': 44.05, 'M': 1.338, 'R_km': 11.8, 'C': 0.167,
        'color': '#E91E63', 'marker': 'p', 'label': 'J0737-3039A\n(double pulsar)',
    },
    'J0437-4715': {
        'f': 173.7, 'M': 1.44, 'R_km': 11.5, 'C': 0.185,
        'color': '#9C27B0', 'marker': 'h', 'label': 'J0437-4715',
    },
    'J1614-2230': {
        'f': 317.4, 'M': 1.97, 'R_km': 11.0, 'C': 0.264,
        'color': '#FF9800', 'marker': 'D', 'label': 'J1614-2230\n(massive)',
    },
    'B1937+21': {
        'f': 641.9, 'M': 1.4, 'R_km': 10.5, 'C': 0.197,
        'color': '#4CAF50', 'marker': '^', 'label': 'B1937+21',
    },
    'J1748-2446ad': {
        'f': 716.0, 'M': 2.0, 'R_km': 11.0, 'C': 0.268,
        'color': '#F44336', 'marker': '*', 'label': 'J1748-2446ad\n(716 Hz)',
    },
}

# --- Compute Lense-Thirring correction ---
# Omega_LT / Omega at surface for uniform density:
#   omega_LT(R) / Omega = 2GI/(c^2 R^3), I = (2/5)MR^2
#   = (4/5) GM/(Rc^2) = (4/5) C
# At arbitrary radius r inside star (uniform density, Hartle 1967):
#   omega_LT(r)/Omega ~ (2/5) C * (R/r)^3 * f(r/R)
# Volume-averaged: <omega_LT/Omega> ~ (2/5) C (approximately)

def LT_frac_surface(C):
    """Omega_LT / Omega at the stellar surface."""
    return 4.0 / 5.0 * C

def LT_frac_volume_avg(C):
    """Volume-averaged Omega_LT / Omega (approximate for uniform density)."""
    return 2.0 / 5.0 * C

def Ta_reduction(C):
    """Ta_rel / Ta_Newton = (1 - <omega_LT/Omega>)^2"""
    return (1.0 - LT_frac_volume_avg(C))**2

# --- Background curves ---
f_spin = np.linspace(10, 800, 500)
C_values = [0.10, 0.15, 0.20, 0.25, 0.30]
C_colors = ['#90CAF9', '#64B5F6', '#42A5F5', '#1E88E5', '#1565C0']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Left panel: Omega_LT/Omega vs f_spin ---
# Background: contours of constant compactness
for C_val, cc in zip(C_values, C_colors):
    LT_surf = LT_frac_surface(C_val)
    ax1.axhline(LT_surf, color=cc, linestyle='--', linewidth=0.8, alpha=0.5)
    ax1.text(805, LT_surf, rf'$\mathcal{{C}}={C_val:.2f}$',
             fontsize=7.5, color=cc, va='center')

# Plot each pulsar as a point
for name, p in pulsars.items():
    LT = LT_frac_surface(p['C'])
    ax1.scatter(p['f'], LT, color=p['color'], marker=p['marker'],
                s=120, zorder=5, edgecolors='black', linewidths=0.5)
    # Annotation offset depends on position
    dx, dy = 10, 0.005
    if p['f'] > 600:
        dx = -80
    if name == 'J0437-4715':
        dy = 0.008
    ax1.annotate(p['label'], (p['f'], LT),
                 textcoords='offset points',
                 xytext=(dx, dy * 1000), fontsize=7.5,
                 color=p['color'], weight='bold',
                 arrowprops=dict(arrowstyle='->', color=p['color'],
                                 lw=0.8) if abs(dx) > 50 else None)

ax1.set_xlabel(r'Spin frequency $\nu$ (Hz)')
ax1.set_ylabel(r'$\omega_{\mathrm{LT}}(R) / \Omega$ (surface)')
ax1.set_title(r'Lense-Thirring frame-dragging: specific pulsars')
ax1.set_xlim(0, 850)
ax1.set_ylim(0, 0.30)

# --- Right panel: Ta_rel / Ta_Newton vs f_spin ---
# Background curves
for C_val, cc in zip(C_values, C_colors):
    Ta_r = Ta_reduction(C_val)
    ax2.axhline(Ta_r, color=cc, linestyle='--', linewidth=0.8, alpha=0.5)
    ax2.text(805, Ta_r, rf'$\mathcal{{C}}={C_val:.2f}$',
             fontsize=7.5, color=cc, va='center')

# Pulsar points
for name, p in pulsars.items():
    Ta_r = Ta_reduction(p['C'])
    ax2.scatter(p['f'], Ta_r, color=p['color'], marker=p['marker'],
                s=120, zorder=5, edgecolors='black', linewidths=0.5)
    # Label
    dx = 10
    if p['f'] > 600:
        dx = -80
    ax2.annotate(name, (p['f'], Ta_r),
                 textcoords='offset points',
                 xytext=(dx, 8), fontsize=7.5,
                 color=p['color'], weight='bold')

ax2.axhline(1.0, color='gray', linestyle=':', linewidth=1.0,
            label='No frame-dragging')

ax2.set_xlabel(r'Spin frequency $\nu$ (Hz)')
ax2.set_ylabel(r'$\mathrm{Ta}_{\mathrm{rel}} / \mathrm{Ta}_{\mathrm{Newton}}$')
ax2.set_title(r'Taylor number reduction by frame-dragging')
ax2.set_xlim(0, 850)
ax2.set_ylim(0.70, 1.05)

# Add table of computed values
table_lines = []
for name, p in pulsars.items():
    LT = LT_frac_surface(p['C'])
    Ta_r = Ta_reduction(p['C'])
    table_lines.append(f'{name}: LT={LT:.3f}, Ta_r={Ta_r:.3f}')

table_text = '\n'.join(table_lines)
ax2.text(0.02, 0.35, table_text, transform=ax2.transAxes,
         fontsize=6.5, ha='left', va='top', family='monospace',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.8))

fig.tight_layout()
outdir = os.path.dirname(__file__)
fig.savefig(os.path.join(outdir, 'fig_lense_thirring_pulsars.pdf'))
fig.savefig(os.path.join(outdir, 'fig_lense_thirring_pulsars.png'))
print('Saved plots/deep/fig_lense_thirring_pulsars.pdf and .png')
plt.close(fig)
