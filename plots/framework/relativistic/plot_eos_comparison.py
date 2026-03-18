#!/usr/bin/env python3
"""
Agent 59: EOS comparison -- c_s^2/c^2 vs energy density.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

eps = np.linspace(0.01, 20.0, 2000)

Gamma_eff = 5.0/3.0 - (5.0/3.0 - 4.0/3.0)*(1-np.exp(-eps/2.0))
p_over_eps_ideal = (Gamma_eff-1.0)*(1.0-np.exp(-eps/1.5))
cs2_ideal = Gamma_eff * p_over_eps_ideal / (1.0 + p_over_eps_ideal)

smooth = 1.0/(1.0+np.exp(-(eps-0.5)/0.1))
cs2_qgp_low = 0.15*eps/0.5
cs2_qgp_high = (1.0/3.0)*(1.0 - 0.6*np.exp(-(eps-1.0)**2/0.3**2))
cs2_qgp = (1-smooth)*cs2_qgp_low + smooth*cs2_qgp_high
cs2_qgp = np.maximum(cs2_qgp, 0.01)

cs2_nuclear = 0.04 + 0.85*(1.0-np.exp(-eps/3.0))
cs2_nuclear += 0.08*np.exp(-(eps-0.5)**2/0.15)
cs2_nuclear = np.minimum(cs2_nuclear, 0.95)

fig, ax = plt.subplots(figsize=(9, 6))
ax.axhline(y=1.0, color='red', ls='-', lw=1.5, alpha=0.4, label=r'Causality: $c_s^2=c^2$')
ax.fill_between(eps, 1.0, 1.1, color='red', alpha=0.08)
ax.axhline(y=1.0/3.0, color='gray', ls=':', lw=1.2, label=r'Conformal: $c_s^2/c^2=1/3$')
ax.plot(eps, cs2_ideal, color=COLORS['classical'], lw=2.5, label=r'Ideal gas ($\Gamma$-law)')
ax.plot(eps, cs2_qgp, color=COLORS['qgp'], lw=2.5, label=r'QGP (lattice-inspired)')
ax.plot(eps, cs2_nuclear, color=COLORS['neutron_star'], lw=2.5, label=r'Nuclear matter (APR-like)')
ax.annotate(r'QCD crossover', xy=(1.0, cs2_qgp[np.argmin(np.abs(eps-1.0))]),
            xytext=(3.0, 0.08), fontsize=10, color=COLORS['qgp'],
            arrowprops=dict(arrowstyle='->', color=COLORS['qgp'], lw=1.2))
ax.annotate(r'Stiffening', xy=(3.5, cs2_nuclear[np.argmin(np.abs(eps-3.5))]),
            xytext=(6.0, 0.6), fontsize=10, color=COLORS['neutron_star'],
            arrowprops=dict(arrowstyle='->', color=COLORS['neutron_star'], lw=1.2))
ax.axvspan(0, 1.0, color='blue', alpha=0.03)
ax.axvspan(1.0, 5.0, color='green', alpha=0.03)
ax.axvspan(5.0, 20.0, color='orange', alpha=0.03)
ax.text(0.3, 0.92, 'Hadronic', fontsize=9, color='gray', ha='center')
ax.text(2.5, 0.92, 'Transition', fontsize=9, color='gray', ha='center')
ax.text(12.0, 0.92, 'Dense QCD', fontsize=9, color='gray', ha='center')
ax.set_xlabel(r'Energy density $\varepsilon / \varepsilon_{\mathrm{nuc}}$')
ax.set_ylabel(r'$c_s^2 / c^2$')
ax.set_title(r'Equation of State Comparison: $c_s^2/c^2$ vs $\varepsilon$')
ax.set_xlim(0, 20); ax.set_ylim(0, 1.05)
ax.legend(loc='right', fontsize=11)
plt.tight_layout()
outdir = os.path.dirname(os.path.abspath(__file__))
fig.savefig(f'{outdir}/fig_eos_comparison.pdf')
fig.savefig(f'{outdir}/fig_eos_comparison.png')
print('Saved fig_eos_comparison.pdf/.png')
plt.close()
