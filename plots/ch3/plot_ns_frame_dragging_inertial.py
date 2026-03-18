#!/usr/bin/env python3
"""
Agent 8: Frame-dragging effect on inertial waves in rotating neutron stars.

Plots the inertial-wave frequency as a function of wavevector angle theta,
comparing:
  - Classical: sigma = 2*Omega*cos(theta)
  - With frame-dragging: sigma = 2*(Omega - Omega_LT)*cos(theta)
for several NS compactness values (Omega_LT/Omega ratios).

Also shows the relativistic enthalpy correction to the damping rate.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS
setup_style()

import numpy as np
import matplotlib.pyplot as plt

# --- Physical parameters ---
# Millisecond pulsar: Omega ~ 4000 rad/s, R ~ 10 km, M ~ 1.4 Msun
# Frame-dragging fraction Omega_LT / Omega for various compactness
compactness_labels = [
    (0.0,   r'Classical ($\Omega_{\rm LT}/\Omega = 0$)'),
    (0.02,  r'$\mathcal{C}=0.10$, $\Omega_{\rm LT}/\Omega=0.02$'),
    (0.05,  r'$\mathcal{C}=0.15$, $\Omega_{\rm LT}/\Omega=0.05$'),
    (0.10,  r'$\mathcal{C}=0.20$, $\Omega_{\rm LT}/\Omega=0.10$'),
    (0.20,  r'$\mathcal{C}=0.25$, $\Omega_{\rm LT}/\Omega=0.20$'),
]

theta = np.linspace(0, np.pi, 500)
Omega = 4000.0  # rad/s, representative millisecond pulsar

color_list = [COLORS['classical'], COLORS['relativistic'],
              COLORS['bdnk'], COLORS['is'], COLORS['neutron_star']]
ls_list = ['-', '--', '-.', ':', (0, (3, 1, 1, 1))]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# --- Panel (a): Inertial wave frequency vs angle ---
for i, (frac, label) in enumerate(compactness_labels):
    Omega_eff = Omega * (1.0 - frac)
    sigma = 2.0 * Omega_eff * np.abs(np.cos(theta))
    ax1.plot(np.degrees(theta), sigma, color=color_list[i],
             ls=ls_list[i], linewidth=2.0, label=label)

ax1.set_xlabel(r'Angle $\vartheta$ between $\mathbf{k}$ and $\Omega$ (deg)')
ax1.set_ylabel(r'Inertial wave frequency $|\sigma|$ (rad/s)')
ax1.set_title('(a) Frame-dragging effect on inertial waves')
ax1.legend(fontsize=9, loc='upper right')
ax1.set_xlim(0, 180)
ax1.set_ylim(0, 9000)

# --- Panel (b): Relative frequency shift vs compactness ---
C_vals = np.linspace(0.05, 0.30, 200)
# Approximate Omega_LT/Omega ~ 0.4 * C^2 / (1 - 2C) for slowly rotating NS
# (simplified Hartle model)
I_NS = 0.35  # I/(MR^2) typical
frac_LT = 2.0 * C_vals * I_NS / (1.0 - 2.0 * C_vals)
frac_LT = np.clip(frac_LT, 0, 0.5)

# Also enthalpy correction: h/rho*c^2 ~ 1/(1-2C) approximately
h_over_rho = 1.0 / (1.0 - 2.0 * C_vals)

# Total frequency shift: delta_sigma/sigma = -frac_LT (frame dragging)
# plus enthalpy suppression of damping: factor (rho*c^2/h)
delta_freq = -frac_LT * 100  # percent
delta_damp = (1.0 / h_over_rho - 1.0) * 100  # percent change in damping

ax2.plot(C_vals, delta_freq, color=COLORS['relativistic'], linewidth=2.0,
         label=r'Frequency shift $\Delta\sigma/\sigma$ (frame-dragging)')
ax2.plot(C_vals, delta_damp, color=COLORS['bdnk'], linewidth=2.0, ls='--',
         label=r'Damping rate change $\Delta\gamma/\gamma$ (enthalpy)')

ax2.axhline(0, color='gray', linewidth=0.5)
ax2.axvline(0.20, color='gray', ls=':', alpha=0.5, label=r'Typical NS ($\mathcal{C}=0.2$)')

ax2.set_xlabel(r'Compactness $\mathcal{C} = GM/(Rc^2)$')
ax2.set_ylabel('Relative change (%)')
ax2.set_title('(b) Relativistic corrections vs compactness')
ax2.legend(fontsize=9, loc='lower left')
ax2.set_xlim(0.05, 0.30)

fig.tight_layout()
outdir = os.path.join(os.path.dirname(__file__), '..')
fig.savefig(os.path.join(outdir, 'ch3', 'fig_ns_frame_dragging_inertial.pdf'))
fig.savefig(os.path.join(outdir, 'ch3', 'fig_ns_frame_dragging_inertial.png'))
print("Saved plots/ch3/fig_ns_frame_dragging_inertial.pdf and .png")
plt.close(fig)
