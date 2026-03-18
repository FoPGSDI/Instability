#!/usr/bin/env python3
"""
Agent 34: MRI in Keplerian disk with axial B: growth rate vs k for various B.

Shows the MRI dispersion relation sigma(k) for a Keplerian disk with
different magnetic field strengths, comparing classical and relativistic
(bounded Alfven speed) predictions.

Produces: plots/ch9/fig_mri_keplerian.pdf
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

Omega = 1.0
q = 1.5  # Keplerian shear
kappa2 = 2 * Omega**2 * (2 - q)  # = Omega^2

k = np.linspace(0.01, 8.0, 800)

def mri_growth(k, vA):
    """Classical MRI growth rate."""
    kv = k * vA
    disc = 16 * Omega**2 * kv**2 + kappa2**2
    sigma2 = 0.5 * (-kappa2 - 2 * kv**2 + np.sqrt(np.maximum(disc, 0)))
    return np.sqrt(np.maximum(sigma2, 0))

def mri_growth_rel(k, vA_over_c):
    """Relativistic MRI: v_A -> v_A / sqrt(1 + v_A^2/c^2)."""
    vA_rel = vA_over_c / np.sqrt(1 + vA_over_c**2)
    return mri_growth(k, vA_rel)

# Field strengths
vA_values = [0.05, 0.1, 0.3, 0.5, 1.0]
cmap_class = plt.cm.Blues(np.linspace(0.3, 0.9, len(vA_values)))
cmap_rel = plt.cm.Reds(np.linspace(0.3, 0.9, len(vA_values)))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5), sharey=True)

# Left: Classical
for i, vA in enumerate(vA_values):
    sigma = mri_growth(k, vA)
    ax1.plot(k, sigma / Omega, color=cmap_class[i], lw=1.8,
             label=rf'$v_A/c = {vA}$')

ax1.axhline(y=0.75, color='gray', ls=':', lw=0.8, alpha=0.5)
ax1.text(6, 0.76, r'$\sigma_{\max} = \frac{3}{4}\Omega$', fontsize=9,
         color='gray')
ax1.set_xlabel(r'Wavenumber $k$ (units of $\Omega/v_A$)')
ax1.set_ylabel(r'Growth rate $\sigma / \Omega$')
ax1.set_title('Classical MRI (Keplerian disk)')
ax1.legend(fontsize=9.5, loc='upper right')
ax1.set_xlim(0, 8)
ax1.set_ylim(0, 1.0)

# Right: Relativistic
for i, vA in enumerate(vA_values):
    sigma = mri_growth_rel(k, vA)
    ax2.plot(k, sigma / Omega, color=cmap_rel[i], lw=1.8,
             label=rf'$v_A/c = {vA}$')

ax2.axhline(y=0.75, color='gray', ls=':', lw=0.8, alpha=0.5)
ax2.set_xlabel(r'Wavenumber $k$ (units of $\Omega/v_A$)')
ax2.set_title('Relativistic MRI (bounded Alfv\u00e9n speed)')
ax2.legend(fontsize=9.5, loc='upper right')
ax2.set_xlim(0, 8)

# Highlight the cutoff difference
ax2.annotate('Relativistic cutoff\nlowers unstable band',
             xy=(3.5, 0.3), fontsize=9, color=COLORS['relativistic'],
             ha='center',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow',
                       alpha=0.8))

fig.suptitle('MRI Dispersion in Keplerian Disk: Growth Rate vs Wavenumber',
             fontsize=13, y=1.02)
fig.tight_layout()
fig.savefig(os.path.join(os.path.dirname(__file__), 'fig_mri_keplerian.pdf'))
fig.savefig(os.path.join(os.path.dirname(__file__), 'fig_mri_keplerian.png'))
print("Saved plots/ch9/fig_mri_keplerian.pdf")
