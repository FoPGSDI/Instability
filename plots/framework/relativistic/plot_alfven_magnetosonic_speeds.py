#!/usr/bin/env python3
"""
Agent 58: Alfven/magnetosonic speeds vs B-field for NS, magnetar, jet.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

log_B = np.linspace(10, 18, 1000)
B = 10.0**log_B

rho_ns = 2e14; w_ns = rho_ns * (2.998e10)**2; cs2_ns = 0.1
rho_mag = 5e14; w_mag = rho_mag * (2.998e10)**2; cs2_mag = 0.15
rho_jet = 1e-2; w_jet = 10.0 * rho_jet * (2.998e10)**2; cs2_jet = 1.0/3.0

def vA_rel(B, w, c_val=2.998e10):
    b2 = B**2
    return np.sqrt(b2 / (4*np.pi*w/c_val**2 + b2))

def vA_class(B, rho, c_val=2.998e10):
    return B / np.sqrt(4*np.pi*rho) / c_val

def vf_rel(B, w, cs2, c_val=2.998e10):
    va2 = vA_rel(B, w, c_val)**2
    return np.sqrt(cs2 + va2 - cs2*va2)

fig, axes = plt.subplots(1, 3, figsize=(16, 5), sharey=True)
environments = [
    ('(a) Neutron Star', vA_rel(B,w_ns), vA_class(B,rho_ns), vf_rel(B,w_ns,cs2_ns), cs2_ns, COLORS['neutron_star'], r'$\rho=2\times10^{14}$ g/cm$^3$'),
    ('(b) Magnetar', vA_rel(B,w_mag), vA_class(B,rho_mag), vf_rel(B,w_mag,cs2_mag), cs2_mag, COLORS['data'], r'$\rho=5\times10^{14}$ g/cm$^3$'),
    ('(c) Relativistic Jet', vA_rel(B,w_jet), vA_class(B,rho_jet), vf_rel(B,w_jet,cs2_jet), cs2_jet, COLORS['jet'], r'$w=10\,\rho c^2$'),
]
for ax, (title, va_r, va_c, vf_r, cs2, color, note) in zip(axes, environments):
    ax.axhline(y=1.0, color='gray', ls=':', lw=1.2, label=r'$c$')
    ax.fill_between(log_B, 1.0, 1.3, color='red', alpha=0.06)
    ax.plot(log_B, np.minimum(va_c, 1.3), color='gray', ls='--', lw=1.5, label=r'Classical $v_A$', alpha=0.7)
    ax.plot(log_B, va_r, color=color, lw=2.2, label=r'Rel. $v_A/c$')
    ax.plot(log_B, vf_r, color=COLORS['bdnk'], lw=2.0, ls='-.', label=r'Rel. $v_f/c$')
    ax.axhline(y=np.sqrt(cs2), color=COLORS['classical'], ls='--', lw=1.0, alpha=0.5, label=r'$c_s/c$')
    ax.set_xlabel(r'$\log_{10}(B$ [G]$)$'); ax.set_title(title)
    ax.set_xlim(10, 18); ax.set_ylim(0, 1.15)
    ax.legend(loc='lower right', fontsize=9)
    ax.text(10.3, 0.05, note, fontsize=8, style='italic', color='gray')
axes[0].set_ylabel(r'Speed / $c$')
fig.suptitle(r'Alfv\'en and Fast Magnetosonic Speeds vs $B$-field', fontsize=15, y=1.02)
plt.tight_layout()
outdir = os.path.dirname(os.path.abspath(__file__))
fig.savefig(f'{outdir}/fig_alfven_magnetosonic_speeds.pdf')
fig.savefig(f'{outdir}/fig_alfven_magnetosonic_speeds.png')
print('Saved fig_alfven_magnetosonic_speeds.pdf/.png')
plt.close()
