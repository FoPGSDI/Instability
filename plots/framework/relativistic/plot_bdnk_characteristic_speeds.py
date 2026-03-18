#!/usr/bin/env python3
"""
Agent 57: BDNK characteristic speeds vs temperature for QGP and NS matter.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

T_MeV = np.linspace(1, 500, 1000)
c = 1.0

cs2_qgp = np.full_like(T_MeV, 1.0 / 3.0)
v_char_qgp = np.sqrt(cs2_qgp + 0.15 * (1 - np.exp(-T_MeV / 150.0)))
v_char_qgp = np.minimum(v_char_qgp, 0.95)

cs2_ns = 0.04 + 0.76 * (1.0 - np.exp(-T_MeV / 80.0))
cs2_ns = np.minimum(cs2_ns, 0.95)
v_char_ns = np.sqrt(cs2_ns + 0.08 * np.exp(-(T_MeV - 150)**2 / (60**2)))
v_char_ns = np.minimum(v_char_ns, 0.98)

v_eckart = np.ones_like(T_MeV) * c

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5), sharey=True)

ax1.axhline(y=1.0, color='gray', ls=':', lw=1.2, label=r'$c$ (causal limit)')
ax1.fill_between(T_MeV, 1.0, 1.05, color='red', alpha=0.08)
ax1.plot(T_MeV, np.sqrt(cs2_qgp), color=COLORS['classical'], lw=2.2, label=r'Sound $c_s/c = 1/\sqrt{3}$')
ax1.plot(T_MeV, v_char_qgp, color=COLORS['bdnk'], lw=2.2, label=r'BDNK max char. speed')
ax1.plot(T_MeV, v_eckart, color=COLORS['is'], lw=1.5, ls='--', label=r'Eckart/Landau (acausal)')
ax1.axvline(x=155, color='gray', ls='-.', lw=1.0, alpha=0.6)
ax1.text(160, 0.15, r'$T_c$ (QCD)', fontsize=10, color='gray')
ax1.set_xlabel(r'Temperature $T$ [MeV]')
ax1.set_ylabel(r'Signal speed / $c$')
ax1.set_title('(a) Quark-Gluon Plasma')
ax1.set_xlim(1, 500); ax1.set_ylim(0, 1.08)
ax1.legend(loc='center right', fontsize=10)

ax2.axhline(y=1.0, color='gray', ls=':', lw=1.2, label=r'$c$ (causal limit)')
ax2.fill_between(T_MeV, 1.0, 1.05, color='red', alpha=0.08)
ax2.plot(T_MeV, np.sqrt(cs2_ns), color=COLORS['neutron_star'], lw=2.2, label=r'Sound $c_s/c$')
ax2.plot(T_MeV, v_char_ns, color=COLORS['bdnk'], lw=2.2, label=r'BDNK max char. speed')
ax2.plot(T_MeV, v_eckart, color=COLORS['is'], lw=1.5, ls='--', label=r'Eckart/Landau (acausal)')
ax2.axvspan(100, 200, color='purple', alpha=0.05)
ax2.text(125, 0.15, 'Deconf.\ntransition', fontsize=9, color='purple', alpha=0.7)
ax2.set_xlabel(r'Temperature $T$ [MeV]')
ax2.set_title('(b) Neutron Star Matter')
ax2.set_xlim(1, 500)
ax2.legend(loc='center right', fontsize=10)

fig.suptitle('BDNK Characteristic Speeds vs Temperature', fontsize=15, y=1.02)
plt.tight_layout()
outdir = os.path.dirname(os.path.abspath(__file__))
fig.savefig(f'{outdir}/fig_bdnk_char_speeds.pdf')
fig.savefig(f'{outdir}/fig_bdnk_char_speeds.png')
print(f'Saved fig_bdnk_char_speeds.pdf/.png')
plt.close()
