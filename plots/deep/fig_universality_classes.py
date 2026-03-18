#!/usr/bin/env python3
"""
fig_universality_classes.py
Schematic showing IS, BDNK, GENERIC as different representations of the same
universality class, with identical linear spectrum.

Reference: Gavassino, Disconzi & Noronha (2023),
  PRL 130, 162302 [arXiv:2302.03478]
  PRD 108, 076003 [arXiv:2302.05332]
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

setup_style()

fig, axes = plt.subplots(1, 2, figsize=(15, 6.5))

# === Left panel: Schematic of universality classes ===
ax = axes[0]

# Draw three boxes for the three formalisms
box_props = dict(boxstyle='round,pad=0.6', linewidth=2.5)

# IS box
is_box = FancyBboxPatch((0.05, 0.65), 0.25, 0.20, **box_props,
                          facecolor='#FFE0B2', edgecolor='#E65100')
ax.add_patch(is_box)
ax.text(0.175, 0.75, 'Israel--Stewart\n(2nd order, 14 DOFs)\n$\\tau_\\pi, \\tau_q, \\tau_\\Pi$',
        ha='center', va='center', fontsize=10, fontweight='bold',
        color='#BF360C')

# BDNK box
bdnk_box = FancyBboxPatch((0.37, 0.65), 0.25, 0.20, **box_props,
                           facecolor='#C8E6C9', edgecolor='#2E7D32')
ax.add_patch(bdnk_box)
ax.text(0.495, 0.75, 'BDNK\n(1st order, 5 DOFs)\nFrame coefficients',
        ha='center', va='center', fontsize=10, fontweight='bold',
        color='#1B5E20')

# GENERIC box
gen_box = FancyBboxPatch((0.69, 0.65), 0.25, 0.20, **box_props,
                          facecolor='#D1C4E9', edgecolor='#4527A0')
ax.add_patch(gen_box)
ax.text(0.815, 0.75, 'GENERIC\n(multifluid, Carter)\nEntrainment matrix',
        ha='center', va='center', fontsize=10, fontweight='bold',
        color='#311B92')

# Central universality class box
univ_box = FancyBboxPatch((0.20, 0.15), 0.60, 0.25, **box_props,
                           facecolor='#BBDEFB', edgecolor='#0D47A1')
ax.add_patch(univ_box)
ax.text(0.50, 0.275, 'SAME UNIVERSALITY CLASS\n'
        'Identical linearized spectrum\n'
        'Same critical parameters (Ra$_c$, Ta$_c$, $Q_c$)',
        ha='center', va='center', fontsize=11, fontweight='bold',
        color='#0D47A1')

# Arrows from each formalism to universality class
for x_start in [0.175, 0.495, 0.815]:
    ax.annotate('', xy=(0.50, 0.42), xytext=(x_start, 0.63),
                arrowprops=dict(arrowstyle='->', color='#37474F',
                              lw=2.0, connectionstyle='arc3,rad=0'))

# Label for arrows
ax.text(0.50, 0.52, 'Change of variables\n(gauge transformation)',
        ha='center', va='center', fontsize=10, color='#37474F',
        style='italic')

ax.set_xlim(0, 1)
ax.set_ylim(0.05, 0.95)
ax.set_title('Universality classes of relativistic fluid dynamics',
             fontsize=13, fontweight='bold')
ax.axis('off')

# === Right panel: Shared dispersion relation ===
ax2 = axes[1]

k = np.linspace(0, 5, 300)

# Sound mode (real part of omega)
cs2 = 1.0/3.0  # conformal
cs = np.sqrt(cs2)
omega_sound_re = cs * k

# Damping rate (imaginary part, common to all formalisms at low k)
eta_over_w = 0.1  # eta_s / (epsilon+p)
omega_sound_im = 0.5 * (4.0/3.0 * eta_over_w) * k**2

# IS non-hydro mode (extra)
tau_pi = 0.5
omega_is_nonhydro = 1.0/tau_pi * np.ones_like(k) + 0.02 * k**2

# BDNK UV mode (frame-dependent)
omega_bdnk_uv = 0.8 * k  # asymptotically propagating

ax2.plot(k, omega_sound_re, 'b-', linewidth=2.5,
         label='Sound mode Re($\\omega$) [shared]')
ax2.plot(k, omega_sound_im, 'b--', linewidth=2.0,
         label='Sound mode Im($\\omega$) [shared]')

# Shear mode
omega_shear = eta_over_w * k**2
ax2.plot(k, omega_shear, 'g-', linewidth=2.0,
         label='Shear diffusion [shared]')

# Non-hydro modes (different between formalisms but OUTSIDE hydro regime)
ax2.plot(k, omega_is_nonhydro, color='#FF9800', linewidth=1.5,
         linestyle=':', label='IS non-hydro (relaxation)')
ax2.plot(k, omega_bdnk_uv, color='#4CAF50', linewidth=1.5,
         linestyle=':', label='BDNK UV mode (frame)')

# Shade the hydrodynamic regime
ax2.axvspan(0, 2.0, alpha=0.08, color='blue')
ax2.text(1.0, 3.8, 'Hydrodynamic\nregime\n(shared spectrum)',
         ha='center', fontsize=10, color='#0D47A1',
         fontweight='bold')

# Shade the non-hydro regime
ax2.axvspan(2.0, 5.0, alpha=0.05, color='red')
ax2.text(3.5, 3.8, 'Non-hydro regime\n(formalism-dependent)',
         ha='center', fontsize=10, color='#B71C1C')

ax2.set_xlabel('Wavenumber $k$ [arb. units]')
ax2.set_ylabel('Frequency $\\omega$ [arb. units]')
ax2.set_title('Dispersion relations: shared vs. formalism-dependent',
              fontsize=13, fontweight='bold')
ax2.legend(loc='upper left', fontsize=9, framealpha=0.9)
ax2.set_xlim(0, 5)
ax2.set_ylim(0, 4.5)

plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), 'fig_universality_classes.pdf'))
plt.savefig(os.path.join(os.path.dirname(__file__), 'fig_universality_classes.png'))
print('Saved fig_universality_classes.pdf')
