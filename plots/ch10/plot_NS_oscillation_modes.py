#!/usr/bin/env python3
"""
Neutron star oscillation modes: f-mode and g-mode frequencies vs compactness.

The relativistic Kelvin modes (§98) describe oscillations of a
self-gravitating fluid globe. For neutron stars, the compactness
parameter C = GM/(Rc^2) introduces significant corrections to the
classical oscillation frequencies. The f-mode (fundamental) and
g-mode (gravity) frequencies shift with compactness.

Reference: Chandrasekhar Ch X §§98-99, Thorne & Campolattaro (1967),
           Andersson & Kokkotas (1998).
"""
import sys; sys.path.insert(0, '/data/haiyangw/claude/Instability'); from SHARED_PLOT_STYLE import setup_style, COLORS, G_cgs, M_sun, c_cgs
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# --- Parameters ---
# Compactness range: C = GM/(Rc^2)
# Typical NS: M ~ 1.4 Msun, R ~ 10-14 km => C ~ 0.1-0.3
# Maximum (Buchdahl): C = 4/9 ~ 0.44
C = np.linspace(0.001, 0.35, 500)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Left panel: Kelvin mode frequencies vs compactness ---
# sigma_Kl^2 = 2l(l-1)/(2l+1) * GM/R^3 * [1 + beta_l * C + O(C^2)]
# Normalized: sigma / sigma_Newt where sigma_Newt = sqrt(2l(l-1)/(2l+1) * GM/R^3)

l_values = [2, 3, 4, 5]
colors_l = ['#2196F3', '#F44336', '#4CAF50', '#FF9800']

for j, l in enumerate(l_values):
    # beta_l = 2(5l^2 + 5l - 3)/((2l+1)(2l-1)) - 3/(l-1)
    beta_l = 2.0 * (5*l**2 + 5*l - 3) / ((2*l + 1) * (2*l - 1)) - 3.0 / (l - 1)

    # Relativistic correction (to first order in C)
    correction = 1.0 + beta_l * C

    # For higher order, use a Pade-like approximation to stay physical
    # sigma_rel / sigma_Newt = sqrt(1 + beta_l C)
    freq_ratio = np.sqrt(np.maximum(correction, 0.01))

    ax1.plot(C, freq_ratio, '-', color=colors_l[j], linewidth=2.0,
             label=rf'$\ell = {l}$ ($\beta_{l} = {beta_l:.2f}$)')

ax1.axhline(y=1.0, color='gray', linestyle='--', alpha=0.5, label='Newtonian')
ax1.set_xlabel(r'Compactness $\mathcal{C} = GM/Rc^2$', fontsize=14)
ax1.set_ylabel(r'$\sigma_\mathrm{rel} / \sigma_\mathrm{Newt}$', fontsize=14)
ax1.set_title('Kelvin mode frequency: relativistic correction', fontsize=14)
ax1.legend(loc='upper left', fontsize=10, frameon=True, edgecolor='0.7')
ax1.set_xlim(0, 0.35)
ax1.grid(True, linestyle=':', alpha=0.4)

# Shade the typical NS range
ax1.axvspan(0.1, 0.25, alpha=0.08, color='blue')
ax1.text(0.175, 0.55, 'Typical NS', fontsize=9, color='blue', ha='center',
         transform=ax1.get_xaxis_transform())

# --- Right panel: Physical f-mode and g-mode frequencies for NS ---
# f-mode: use the l=2 Kelvin formula with realistic NS parameters
# M ranges, fix R or use an EOS-inspired M-R relation

M_Msun = np.linspace(1.0, 2.5, 500)
M_g = M_Msun * M_sun

# Simple M-R relation inspired by nuclear EOS: R ~ 12 km * (M/1.4 Msun)^{-0.1}
R_cm = 12e5 * (M_Msun / 1.4)**(-0.1)

C_phys = G_cgs * M_g / (R_cm * c_cgs**2)

# f-mode frequency (l=2)
l_f = 2
beta_2 = 2.0 * (5*4 + 10 - 3) / (5 * 3) - 3.0  # = 74/15 - 3 = 29/15
sigma_K2_sq = 2.0 * l_f * (l_f - 1) / (2*l_f + 1) * G_cgs * M_g / R_cm**3
correction_f = 1.0 + beta_2 * C_phys
freq_f_Hz = np.sqrt(sigma_K2_sq * np.maximum(correction_f, 0.01)) / (2 * np.pi)
freq_f_kHz = freq_f_Hz / 1e3

# g-mode (rough estimate): f_g ~ f_f * sqrt(C) * N/omega_0
# A simple scaling: f_g ~ 0.5 * sqrt(C/0.15) kHz for l=2
freq_g_kHz = 0.5 * np.sqrt(C_phys / 0.15)

# Newtonian f-mode for comparison
freq_f_Newt_Hz = np.sqrt(sigma_K2_sq) / (2 * np.pi)
freq_f_Newt_kHz = freq_f_Newt_Hz / 1e3

ax2.plot(M_Msun, freq_f_kHz, '-', color=COLORS['relativistic'], linewidth=2.5,
         label=r'$f$-mode (relativistic, $\ell=2$)')
ax2.plot(M_Msun, freq_f_Newt_kHz, '--', color=COLORS['classical'], linewidth=2.0,
         label=r'$f$-mode (Newtonian)')
ax2.plot(M_Msun, freq_g_kHz, '-', color=COLORS['neutron_star'], linewidth=2.0,
         label=r'$g$-mode estimate')

# Viscous damping time scale (from eq rel-10-291R)
# tau_l = R^2 / ((l-1)(2l+1) nu)
# For NS: eta ~ 10^{18} g/(cm s), rho ~ 10^{14.5} g/cm^3
# nu ~ eta / (w/c^2) ~ 10^{18} / (10^{14.5} * 1.3) ~ 2000 cm^2/s
# tau_2 ~ (12e5)^2 / (1 * 5 * 2000) ~ 1.4e7 s ... very long

ax2.set_xlabel(r'Neutron star mass $M / M_\odot$', fontsize=14)
ax2.set_ylabel(r'Frequency [kHz]', fontsize=14)
ax2.set_title(r'NS oscillation frequencies ($\ell = 2$)', fontsize=14)
ax2.legend(loc='upper left', fontsize=10, frameon=True, edgecolor='0.7')
ax2.set_xlim(1.0, 2.5)
ax2.set_ylim(0, 4.0)
ax2.grid(True, linestyle=':', alpha=0.4)
ax2.text(0.95, 0.95, r'$R \approx 12\,(M/1.4M_\odot)^{-0.1}$ km',
         transform=ax2.transAxes, fontsize=10, va='top', ha='right',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

fig.tight_layout()
fig.savefig('/data/haiyangw/claude/Instability/plots/ch10/fig_NS_oscillation_modes.pdf')
fig.savefig('/data/haiyangw/claude/Instability/plots/ch10/fig_NS_oscillation_modes.png')
print("Saved fig_NS_oscillation_modes.pdf and fig_NS_oscillation_modes.png")
plt.close(fig)
