#!/usr/bin/env python3
"""
Viscous RT in neutron star mergers: damping timescales vs Reynolds number.

In binary NS mergers, the contact interface between the two stars is
subject to RT instability during and after coalescence. The viscous
damping timescale depends on the effective Reynolds number, which in
the BDNK first-order causal framework uses the relativistic kinematic
viscosity nu = eta / w, where w = (epsilon + p)/c^2.

Reference: Chandrasekhar Ch X §94 (relativistic extension).
"""
import sys; sys.path.insert(0, '/data/haiyangw/claude/Instability'); from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# --- Parameters ---
# Typical NS merger interface parameters
g_eff = 1e13  # effective gravity at contact (cm/s^2)
A_rel = 0.3   # relativistic Atwood number

# Reynolds number range (Re = g^{1/2} L^{3/2} / nu, with L = 1/k)
Re = np.logspace(0, 6, 500)

# Inviscid growth rate: sigma_0 = sqrt(g * k * A_rel)
# With k = g / (nu^2 Re^2)^{1/3} ... or more simply:
# sigma / sigma_0 as function of Re

# From the BDNK viscous dispersion: sigma^2 + nu k^2 sigma - g k A = 0
# sigma = (-nu k^2 + sqrt(nu^2 k^4 + 4 g k A)) / 2
# Non-dimensionalize: let sigma_0 = sqrt(g k A), define S = sigma/sigma_0
# Then: S^2 + (nu k^2 / sigma_0) S - 1 = 0
# nu k^2 / sigma_0 = nu k^{3/2} / sqrt(g A) = 1/sqrt(Re_eff)
# where Re_eff = g A / (nu^2 k^3)

# We parameterize by Re_eff = g * A / (nu^2 * k^3)
Re_eff = Re  # effective Reynolds number

# Normalized growth rate: S^2 + S/sqrt(Re_eff) - 1 = 0
# S = (-1/sqrt(Re) + sqrt(1/Re + 4)) / 2
S = (-1.0/np.sqrt(Re_eff) + np.sqrt(1.0/Re_eff + 4.0)) / 2.0

# Damping timescale relative to inviscid: tau_damp/tau_inviscid = 1/S
tau_ratio = 1.0 / S

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Left panel: Normalized growth rate vs Re ---
# Multiple Atwood numbers
A_vals = [0.1, 0.3, 0.5, 0.7, 0.9]
colors_A = ['#2196F3', '#4CAF50', '#FF9800', '#F44336', '#9C27B0']

for i, A in enumerate(A_vals):
    # The structure is the same for all A when normalized, but
    # let's show the actual growth rate sigma in units of sqrt(g/L)
    # sigma/sqrt(g/L) = sqrt(A) * S(Re)
    sigma_norm = np.sqrt(A) * S
    ax1.plot(Re_eff, sigma_norm, '-', color=colors_A[i], linewidth=2.0,
             label=rf'$\mathcal{{A}}_\mathrm{{rel}} = {A}$')

ax1.set_xscale('log')
ax1.set_xlabel(r'Effective Reynolds number $\mathrm{Re}_\mathrm{eff}$', fontsize=14)
ax1.set_ylabel(r'Growth rate $\sigma / \sqrt{g/L}$', fontsize=14)
ax1.set_title('RT growth rate with BDNK viscous damping', fontsize=14)
ax1.legend(loc='lower right', fontsize=10, frameon=True, edgecolor='0.7')
ax1.grid(True, linestyle=':', alpha=0.4, which='both')
ax1.axvline(x=100, color='gray', linestyle='--', alpha=0.4)
ax1.text(120, 0.1, 'NS merger\nregime', fontsize=9, color='gray')

# --- Right panel: Damping timescale vs Re ---
# For NS merger conditions, convert to physical timescales
# Typical values: L ~ 1 km, g ~ 10^13 cm/s^2
L_cm = 1e5  # 1 km
sigma_0_phys = np.sqrt(g_eff / L_cm)  # inviscid growth rate ~ 1/ms

# Physical timescales
tau_inviscid_ms = 1.0 / sigma_0_phys * 1e3  # ms
tau_damped_ms = tau_ratio * tau_inviscid_ms

ax2.plot(Re_eff, tau_ratio, '-', color=COLORS['relativistic'], linewidth=2.5,
         label=r'$\tau_\mathrm{damp} / \tau_\mathrm{inviscid}$')

# Also show the IS (Israel-Stewart) prediction for comparison
# In IS, effective viscosity is eta/(1 + tau_pi * sigma), which
# gives a different curve at high Re
tau_pi_over_tau_inv = 0.1  # representative ratio
# IS: S^2 + S/(sqrt(Re)*(1 + tau_pi*sigma_0*S)) - 1 = 0
# Approximate: at large Re, IS and BDNK agree; at small Re they differ
S_IS = np.zeros_like(Re_eff)
for idx in range(len(Re_eff)):
    # Iterate to solve IS dispersion
    s = S[idx]  # start from BDNK solution
    for _ in range(50):
        denom = np.sqrt(Re_eff[idx]) * (1.0 + tau_pi_over_tau_inv * s)
        s_new = (-1.0/denom + np.sqrt(1.0/denom**2 + 4.0)) / 2.0
        if abs(s_new - s) < 1e-10:
            break
        s = s_new
    S_IS[idx] = s

tau_ratio_IS = 1.0 / S_IS
ax2.plot(Re_eff, tau_ratio_IS, '--', color=COLORS['is'], linewidth=2.0,
         label=r'Israel--Stewart ($\tau_\pi/\tau_0 = 0.1$)')

ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.set_xlabel(r'Effective Reynolds number $\mathrm{Re}_\mathrm{eff}$', fontsize=14)
ax2.set_ylabel(r'Damping ratio $\tau_\mathrm{damp} / \tau_\mathrm{inviscid}$', fontsize=14)
ax2.set_title('Viscous damping timescale (NS merger)', fontsize=14)
ax2.legend(loc='upper right', fontsize=10, frameon=True, edgecolor='0.7')
ax2.grid(True, linestyle=':', alpha=0.4, which='both')
ax2.set_ylim(0.8, 100)
ax2.text(0.05, 0.05, rf'$\tau_\mathrm{{inviscid}} \approx {tau_inviscid_ms:.2f}$ ms',
         transform=ax2.transAxes, fontsize=10,
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

fig.tight_layout()
fig.savefig('/data/haiyangw/claude/Instability/plots/ch10/fig_viscous_RT_NS_merger.pdf')
fig.savefig('/data/haiyangw/claude/Instability/plots/ch10/fig_viscous_RT_NS_merger.png')
print("Saved fig_viscous_RT_NS_merger.pdf and fig_viscous_RT_NS_merger.png")
plt.close(fig)
