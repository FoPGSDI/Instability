#!/usr/bin/env python3
"""
fig_stability_causality_theorem.py
Conceptual diagram: stability region is a subset of causality region,
illustrating Gavassino's theorem that thermodynamic stability implies causality.

Reference: Gavassino (2022), Phys. Rev. X 12, 041001 [arXiv:2105.14621]
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch

setup_style()

fig, ax = plt.subplots(figsize=(10, 7))

# Draw the outer region: "All hydrodynamic theories"
outer = Ellipse((0.5, 0.5), 0.9, 0.75, angle=0, facecolor='#FFCDD2',
                edgecolor='#D32F2F', linewidth=2.5, alpha=0.4)
ax.add_patch(outer)
ax.text(0.5, 0.88, 'All relativistic hydrodynamic theories',
        ha='center', va='center', fontsize=13, fontweight='bold',
        color='#B71C1C')

# Draw the causal region
causal = Ellipse((0.5, 0.47), 0.72, 0.55, angle=0, facecolor='#BBDEFB',
                 edgecolor='#1565C0', linewidth=2.5, alpha=0.5)
ax.add_patch(causal)
ax.text(0.82, 0.60, 'Causal\n(signal $\\leq c$)',
        ha='center', va='center', fontsize=12, color='#0D47A1',
        fontweight='bold')

# Draw the stable region (inside causal)
stable = Ellipse((0.48, 0.43), 0.48, 0.35, angle=-5, facecolor='#C8E6C9',
                 edgecolor='#2E7D32', linewidth=2.5, alpha=0.6)
ax.add_patch(stable)
ax.text(0.48, 0.43, 'Thermodynamically\nstable\n($E^0_{AB} > 0$)',
        ha='center', va='center', fontsize=12, color='#1B5E20',
        fontweight='bold')

# Arrow showing the implication
ax.annotate('', xy=(0.68, 0.55), xytext=(0.58, 0.48),
            arrowprops=dict(arrowstyle='->', color='#1565C0',
                          lw=2.5, connectionstyle='arc3,rad=0.2'))
ax.text(0.66, 0.50, 'Gavassino\nTheorem',
        ha='center', va='center', fontsize=11,
        fontweight='bold', color='#1565C0',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                 edgecolor='#1565C0', alpha=0.9))

# Place example theories
# Eckart (unstable, acausal)
ax.plot(0.15, 0.78, 'x', markersize=14, color='#D32F2F', markeredgewidth=3)
ax.text(0.15, 0.72, 'Eckart', ha='center', fontsize=10, color='#D32F2F')

# Landau-Lifshitz (unstable, acausal)
ax.plot(0.30, 0.80, 'x', markersize=14, color='#D32F2F', markeredgewidth=3)
ax.text(0.30, 0.74, 'Landau-\nLifshitz', ha='center', fontsize=9,
        color='#D32F2F')

# IS (stable, causal)
ax.plot(0.38, 0.38, 'o', markersize=10, color='#2E7D32',
        markeredgecolor='#1B5E20', markeredgewidth=2)
ax.text(0.38, 0.32, 'IS', ha='center', fontsize=11, fontweight='bold',
        color='#2E7D32')

# BDNK (stable, causal)
ax.plot(0.55, 0.40, 's', markersize=10, color='#2E7D32',
        markeredgecolor='#1B5E20', markeredgewidth=2)
ax.text(0.55, 0.34, 'BDNK', ha='center', fontsize=11, fontweight='bold',
        color='#2E7D32')

# GENERIC (stable, causal)
ax.plot(0.48, 0.50, 'D', markersize=9, color='#2E7D32',
        markeredgecolor='#1B5E20', markeredgewidth=2)
ax.text(0.48, 0.55, 'GENERIC', ha='center', fontsize=10, fontweight='bold',
        color='#2E7D32')

# Title
ax.set_title("Gavassino's Theorem: Thermodynamic Stability $\\Rightarrow$ Causality",
             fontsize=15, fontweight='bold', pad=15)

ax.set_xlim(0, 1)
ax.set_ylim(0.1, 0.95)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), 'fig_stability_causality_theorem.pdf'))
plt.savefig(os.path.join(os.path.dirname(__file__), 'fig_stability_causality_theorem.png'))
print('Saved fig_stability_causality_theorem.pdf')
