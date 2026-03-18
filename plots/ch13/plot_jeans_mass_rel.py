#!/usr/bin/env python3
"""
Plot relativistic Jeans mass M_J,rel vs equation of state parameter w = p/epsilon
for cosmological structure formation.

The relativistic Jeans mass:
    M_J,rel = (pi^(5/2) * c_s^3) / (6 * G^(3/2) * w_enth^(1/2) * A^(3/2))
where w_enth = (eps + p)/c^2, A = (1 + 3 c_s^2/c^2)/2

Compared with the classical M_J = pi^(5/2) c_s^3 / (6 G^(3/2) rho^(1/2))

Different EOS cases:
  - Non-relativistic: p << eps, c_s << c
  - Radiation: p = eps/3, c_s = c/sqrt(3)
  - Stiff (causal limit): p = eps, c_s = c
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, G_cgs, c_cgs, M_sun, m_p, k_B, pi
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

setup_style()

# Parameter: w = p/epsilon (equation of state parameter)
w_param = np.linspace(0.001, 1.0, 500)

# For a given w = p/eps:
#   c_s^2/c^2 = w  (for linear EOS p = w * eps)
#   enthalpy density: (eps + p)/c^2 = eps(1+w)/c^2
#   Active gravitational factor: A = (1 + 3w)/2
#
# Ratio M_J,rel / M_J,classical:
#   Classical: uses rho ~ eps/c^2, c_s^2 = w*c^2
#   M_J,cl ~ pi^(5/2)*(w*c^2)^(3/2) / (6*G^(3/2) * (eps/c^2)^(1/2))
#   M_J,rel ~ pi^(5/2)*(w*c^2)^(3/2) / (6*G^(3/2) * ((1+w)*eps/c^2)^(1/2) * ((1+3w)/2)^(3/2))
#
# Ratio = 1 / ((1+w)^(1/2) * ((1+3w)/2)^(3/2))

ratio_MJ = 1.0 / (np.sqrt(1.0 + w_param) * ((1.0 + 3.0*w_param)/2.0)**1.5)

# Also compute the Jeans wavenumber enhancement
# k_J,rel^2 / k_J,cl^2 = (1+w) * (1+3w)/2
# so k ratio = sqrt((1+w)*(1+3w)/2)
ratio_kJ = np.sqrt((1.0 + w_param) * (1.0 + 3.0*w_param) / 2.0)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# --- Left panel: M_J ratio ---
ax1.plot(w_param, ratio_MJ, '-', color='#F44336', lw=2.5,
         label=r'$M_{J,\mathrm{rel}} / M_{J,\mathrm{classical}}$')
ax1.axhline(1.0, color='gray', ls=':', lw=1.0)

# Mark key EOS points
special_w = [1.0/3.0, 1.0]
special_labels = [r'Radiation ($w=1/3$)', r'Stiff ($w=1$, causal limit)']
special_colors = ['#FF9800', '#9C27B0']
for ws, lbl, col in zip(special_w, special_labels, special_colors):
    r = 1.0 / (np.sqrt(1+ws) * ((1+3*ws)/2)**1.5)
    ax1.plot(ws, r, 'o', color=col, ms=10, zorder=5)
    ax1.annotate(lbl, xy=(ws, r), xytext=(ws+0.08, r+0.05),
                 fontsize=9, color=col,
                 arrowprops=dict(arrowstyle='->', color=col, lw=1.2))

# Shade cosmological regimes
ax1.axvspan(0, 0.05, alpha=0.08, color='#2196F3')
ax1.text(0.025, 0.85, 'Matter\ndom.', fontsize=8, ha='center',
         color='#2196F3')
ax1.axvspan(0.28, 0.38, alpha=0.08, color='#FF9800')
ax1.text(0.33, 0.85, 'Radiation\ndom.', fontsize=8, ha='center',
         color='#FF9800')

ax1.set_xlabel(r'EOS parameter $w = p/\varepsilon$')
ax1.set_ylabel(r'$M_{J,\mathrm{rel}} / M_{J,\mathrm{classical}}$')
ax1.set_title('Relativistic Jeans mass reduction')
ax1.legend(loc='upper right', fontsize=10)
ax1.set_xlim(0, 1.05)
ax1.set_ylim(0, 1.1)
ax1.grid(True, ls=':', alpha=0.3)

# --- Right panel: Jeans wavenumber enhancement ---
ax2.plot(w_param, ratio_kJ, '-', color='#2196F3', lw=2.5,
         label=r'$k_{J,\mathrm{rel}} / k_{J,\mathrm{classical}}$')
ax2.axhline(1.0, color='gray', ls=':', lw=1.0)

for ws, lbl, col in zip(special_w, special_labels, special_colors):
    r = np.sqrt((1+ws)*(1+3*ws)/2)
    ax2.plot(ws, r, 'o', color=col, ms=10, zorder=5)
    ax2.annotate(lbl, xy=(ws, r), xytext=(ws-0.15, r+0.3),
                 fontsize=9, color=col,
                 arrowprops=dict(arrowstyle='->', color=col, lw=1.2))

ax2.fill_between(w_param, 1.0, ratio_kJ, alpha=0.1, color='#2196F3')
ax2.text(0.6, 1.3, 'GR enhancement:\nmore modes unstable',
         fontsize=9, color='#2196F3', ha='center')

ax2.set_xlabel(r'EOS parameter $w = p/\varepsilon$')
ax2.set_ylabel(r'$k_{J,\mathrm{rel}} / k_{J,\mathrm{classical}}$')
ax2.set_title('Relativistic Jeans wavenumber enhancement')
ax2.legend(loc='upper left', fontsize=10)
ax2.set_xlim(0, 1.05)
ax2.set_ylim(0.5, 3.5)
ax2.grid(True, ls=':', alpha=0.3)

fig.tight_layout()
fig.savefig(os.path.join(os.path.dirname(__file__), 'fig_jeans_mass_rel.pdf'))
fig.savefig(os.path.join(os.path.dirname(__file__), 'fig_jeans_mass_rel.png'))
print("Saved plots/ch13/fig_jeans_mass_rel.pdf and .png")
plt.close(fig)
