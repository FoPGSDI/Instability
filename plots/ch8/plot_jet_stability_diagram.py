#!/usr/bin/env python3
"""
Agent 32: Jet axial flow + rotation stability diagram.

Shows the relativistic stability boundary in the (k, Omega) plane for
combined axial and rotational flow in astrophysical jets, illustrating
the relativistic Rayleigh criterion with the Lorentz-factor weighting.

Produces: plots/ch8/fig_jet_stability_diagram.pdf
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# Relativistic stability criterion: d/dr(r^2 Gamma^2 Omega) > 0
# For a jet with W(r) axial flow and V(r) = r Omega rotational flow
# Gamma^2 = 1/(1 - (V^2 + W^2)/c^2)

# Model: jet with Gaussian axial velocity W(r) = W0 * exp(-r^2/R_j^2)
# and rotation Omega(r) = Omega0 * (R_j/r)^q for r > R_j

r = np.linspace(0.1, 5.0, 500)  # in units of R_j
W0_over_c = [0.0, 0.3, 0.6, 0.9]  # jet axial speed

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

# Left panel: Psi_rel(r) for pure axial flow stability
colors = [COLORS['classical'], '#4CAF50', COLORS['accretion'], COLORS['relativistic']]

for i, W0c in enumerate(W0_over_c):
    W = W0c * np.exp(-r**2)
    Gamma2 = 1.0 / (1.0 - W**2)
    # Psi_rel = r d/dr [1/r d(Gamma^2 W)/dr]
    Gamma2W = Gamma2 * W
    dGamma2W_dr = np.gradient(Gamma2W, r)
    Psi_inner = dGamma2W_dr / r
    Psi_rel = r * np.gradient(Psi_inner, r)

    label = 'Classical ($W_0 = 0$)' if W0c == 0 else rf'$W_0/c = {W0c}$'
    ls = '-' if W0c == 0 else '--'
    ax1.plot(r, Psi_rel, color=colors[i], ls=ls, lw=2.0, label=label)

ax1.axhline(y=0, color='gray', ls=':', lw=0.8)
ax1.set_xlabel(r'$r / R_j$')
ax1.set_ylabel(r'$\Psi_{\mathrm{rel}}(r)$')
ax1.set_title('Axial flow: inflexion-point criterion')
ax1.legend(fontsize=10)
ax1.set_xlim(0.1, 4)
ax1.set_ylim(-5, 3)
ax1.fill_between(r, -5, 0, alpha=0.05, color='red')
ax1.text(2.5, -3, 'UNSTABLE', fontsize=10, color='red', alpha=0.5)
ax1.text(2.5, 1.5, 'STABLE', fontsize=10, color='blue', alpha=0.5)

# Right panel: Combined rotation + axial flow stability boundary
# Phi_rel > 0 for stability
q_vals = [1.5, 2.0, 2.5]  # shear parameters
W0c_fixed = 0.5

for j, q_val in enumerate(q_vals):
    Omega_profile = 1.0 / r**q_val
    V = r * Omega_profile
    W = W0c_fixed * np.exp(-r**2)
    speed2 = np.minimum(V**2 + W**2, 0.99)
    Gamma2 = 1.0 / (1.0 - speed2)

    # Phi_rel = (Gamma^2 Omega / r) d/dr(r^2 Gamma^2 Omega)
    ell = r**2 * Gamma2 * Omega_profile
    dell_dr = np.gradient(ell, r)
    Phi_rel = Gamma2 * Omega_profile / r * dell_dr

    ax2.plot(r, Phi_rel, color=plt.cm.plasma(j / 3), lw=2.0,
             label=rf'$q = {q_val}$, $W_0/c = {W0c_fixed}$')

ax2.axhline(y=0, color='gray', ls=':', lw=0.8)
ax2.set_xlabel(r'$r / R_j$')
ax2.set_ylabel(r'$\Phi_{\mathrm{rel}}(r)$')
ax2.set_title(r'Rotation + axial flow: relativistic Rayleigh criterion')
ax2.legend(fontsize=10)
ax2.set_xlim(0.5, 4)
ax2.set_ylim(-5, 5)
ax2.fill_between(r, -5, 0, alpha=0.05, color='red')
ax2.text(3, -3, 'UNSTABLE', fontsize=10, color='red', alpha=0.5)
ax2.text(3, 3, 'STABLE', fontsize=10, color='blue', alpha=0.5)

fig.suptitle('Astrophysical Jet Stability: Axial Flow + Rotation',
             fontsize=13, y=1.02)
fig.tight_layout()
fig.savefig(os.path.join(os.path.dirname(__file__), 'fig_jet_stability_diagram.pdf'))
fig.savefig(os.path.join(os.path.dirname(__file__), 'fig_jet_stability_diagram.png'))
print("Saved plots/ch8/fig_jet_stability_diagram.pdf")
