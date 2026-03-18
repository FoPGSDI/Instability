#!/usr/bin/env python3
"""
Agent 36: Dissipative MRI -- critical Ta(Q) for conducting/insulating boundaries.

Shows the marginal stability curves Ta_c(Q) for dissipative MHD Couette
flow, comparing conducting and non-conducting wall boundary conditions,
and illustrating the relativistic correction Q -> Q_rel.

Produces: plots/ch9/fig_dissipative_mri_TaQ.pdf
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

Q = np.logspace(0, 5, 500)

# Classical asymptotic relations from Chandrasekhar:
# Non-conducting walls: Ta ~ 107.2 * Q for large Q, Ta(0) = 1715
# Conducting walls: Ta ~ 451.2 * Q for large Q, Ta(0) = 1715

# Approximate full curves (interpolation of Tables XLII, XLIII)
Ta_nonconduct = 1715 + 107.2 * Q
Ta_conduct = 1715 + 451.2 * Q

# Counter-rotating (mu = -1):
# Non-conducting: Ta ~ 726 * Q; Ta(0) ~ 3400
# Conducting: Ta ~ 6203 * Q; Ta(0) ~ 3400
Ta_nc_counter = 3400 + 726 * Q
Ta_c_counter = 3400 + 6203 * Q

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

# Left panel: mu > 0 (co-rotating)
ax1.loglog(Q, Ta_nonconduct, color=COLORS['classical'], lw=2.0, ls='-',
           label='Non-conducting walls (class.)')
ax1.loglog(Q, Ta_conduct, color=COLORS['accretion'], lw=2.0, ls='-',
           label='Conducting walls (class.)')

# Relativistic: Q_rel = Q * (1 - Xi - v_A^2/c^2)
# For v_A/c = 0.1, Xi = 0.1: Q_rel/Q = 0.98
frac = 0.98
Q_rel = Q * frac
Ta_nc_rel = 1715 + 107.2 * Q_rel
Ta_c_rel = 1715 + 451.2 * Q_rel

ax1.loglog(Q, Ta_nc_rel, color=COLORS['classical'], lw=1.5, ls='--',
           label=rf'Non-cond. (rel., $v_A/c = 0.1$)')
ax1.loglog(Q, Ta_c_rel, color=COLORS['accretion'], lw=1.5, ls='--',
           label=rf'Conducting (rel., $v_A/c = 0.1$)')

ax1.fill_between(Q, Ta_nonconduct, 1e10, alpha=0.03, color='red')
ax1.fill_between(Q, 1, Ta_nonconduct, alpha=0.03, color='green')
ax1.text(10, 5e6, 'UNSTABLE', fontsize=10, color='red', alpha=0.5)
ax1.text(10, 500, 'STABLE', fontsize=10, color='green', alpha=0.5)

ax1.set_xlabel(r'Chandrasekhar number $Q$')
ax1.set_ylabel(r'Critical Taylor number $\mathscr{T}_c$')
ax1.set_title(r'Co-rotating cylinders ($\mu > 0$)')
ax1.legend(fontsize=8.5, loc='upper left')
ax1.set_xlim(1, 1e5)
ax1.set_ylim(1e3, 1e10)

# Right panel: mu = -1 (counter-rotating)
ax2.loglog(Q, Ta_nc_counter, color=COLORS['classical'], lw=2.0, ls='-',
           label='Non-conducting walls')
ax2.loglog(Q, Ta_c_counter, color=COLORS['accretion'], lw=2.0, ls='-',
           label='Conducting walls')

# Relativistic versions
Ta_nc_counter_rel = 3400 + 726 * Q_rel
Ta_c_counter_rel = 3400 + 6203 * Q_rel
ax2.loglog(Q, Ta_nc_counter_rel, color=COLORS['classical'], lw=1.5, ls='--',
           label='Non-cond. (relativistic)')
ax2.loglog(Q, Ta_c_counter_rel, color=COLORS['accretion'], lw=1.5, ls='--',
           label='Conducting (relativistic)')

ax2.set_xlabel(r'Chandrasekhar number $Q$')
ax2.set_ylabel(r'Critical Taylor number $\mathscr{T}_c$')
ax2.set_title(r'Counter-rotating cylinders ($\mu = -1$)')
ax2.legend(fontsize=8.5, loc='upper left')
ax2.set_xlim(1, 1e5)
ax2.set_ylim(1e3, 1e10)

# Annotate the boundary condition effect
ax2.annotate('Conducting walls\nmuch more stable',
             xy=(1e3, 1e7), fontsize=9, color=COLORS['accretion'],
             ha='center')

fig.suptitle(r'Dissipative MRI: Critical $\mathscr{T}_c(Q)$ for Conducting/Insulating Boundaries',
             fontsize=13, y=1.02)
fig.tight_layout()
fig.savefig(os.path.join(os.path.dirname(__file__), 'fig_dissipative_mri_TaQ.pdf'))
fig.savefig(os.path.join(os.path.dirname(__file__), 'fig_dissipative_mri_TaQ.png'))
print("Saved plots/ch9/fig_dissipative_mri_TaQ.pdf")
