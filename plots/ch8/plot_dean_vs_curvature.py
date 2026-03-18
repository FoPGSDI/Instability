#!/usr/bin/env python3
"""
Agent 30: Dean number vs disk curvature for accretion stream curved channel.

Shows how the relativistic critical Dean number Lambda_rel,c varies with
the curvature ratio d/R_1 for several values of V_m/c, illustrating the
relativistic enhancement of centrifugal instability in accretion tori.

Produces: plots/ch8/fig_dean_vs_curvature.pdf
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# Parameters
d_over_R1 = np.linspace(0.001, 0.3, 300)  # curvature ratio
Vm_over_c = [0.0, 0.01, 0.1, 0.3, 0.5]   # relativistic Mach numbers

# Classical critical Dean parameter (fourth Galerkin approximation)
Lambda_cl_base = 92975.0
A_coeff = 3.8  # relativistic correction coefficient from eq (rel-8-Acoeff)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

# Left panel: Critical Reynolds number vs d/R1
colors = [COLORS['classical'], '#4CAF50', COLORS['accretion'],
          COLORS['jet'], COLORS['relativistic']]
for i, beta in enumerate(Vm_over_c):
    Lambda_rel = Lambda_cl_base * (1 + A_coeff * beta**2)
    Re_c = 35.94 * np.sqrt(1.0 / d_over_R1) * (1 - A_coeff / 2 * beta**2)
    label = 'Classical' if beta == 0 else rf'$V_m/c = {beta}$'
    ls = '-' if beta == 0 else '--'
    ax1.plot(d_over_R1, Re_c, color=colors[i], ls=ls, lw=2.0, label=label)

ax1.set_xlabel(r'Curvature ratio $d/R_1$')
ax1.set_ylabel(r'Critical Reynolds number $\mathrm{Re}_c \sqrt{d/R_1}$')
ax1.set_title('Critical Re for Dean instability')
ax1.legend(fontsize=10)
ax1.set_xlim(0, 0.3)
ax1.set_ylim(0, 60)

# Right panel: Critical Dean number vs V_m/c for fixed curvatures
Vm_c_arr = np.linspace(0, 0.6, 200)
curvatures = [0.01, 0.05, 0.1, 0.2]
cmap = plt.cm.viridis(np.linspace(0.2, 0.9, len(curvatures)))

for j, dR in enumerate(curvatures):
    Lambda_crit = Lambda_cl_base * (1 + A_coeff * Vm_c_arr**2)
    ax2.plot(Vm_c_arr, Lambda_crit / 1e3, color=cmap[j], lw=2.0,
             label=rf'$d/R_1 = {dR}$')

ax2.set_xlabel(r'Relativistic Mach number $V_m/c$')
ax2.set_ylabel(r'$\Lambda_{\mathrm{rel},c}$ ($\times 10^3$)')
ax2.set_title('Relativistic Dean parameter vs flow speed')
ax2.legend(fontsize=10)
ax2.set_xlim(0, 0.6)

# Add astrophysical annotations
ax2.axvspan(0.1, 0.3, alpha=0.1, color=COLORS['accretion'],
            label='Accretion torus')
ax2.axvspan(0.3, 0.6, alpha=0.1, color=COLORS['jet'],
            label='Inner disk')

fig.suptitle('Accretion Stream Curved Channel: Dean Number vs Disk Curvature',
             fontsize=13, y=1.02)
fig.tight_layout()
os.makedirs(os.path.dirname(__file__), exist_ok=True)
fig.savefig(os.path.join(os.path.dirname(__file__), 'fig_dean_vs_curvature.pdf'))
fig.savefig(os.path.join(os.path.dirname(__file__), 'fig_dean_vs_curvature.png'))
print("Saved plots/ch8/fig_dean_vs_curvature.pdf")
