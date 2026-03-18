"""
Deep Research 6: NS f-mode and g-mode frequencies for 3 EOSs,
with BDNK viscous damping (no IS relaxation artifacts),
and GW detectability with LIGO/Einstein Telescope.

References:
  - Radice & Bernuzzi, ApJ 869 (2018) 130
  - Duffell, ApJS 197 (2011) 15
  - Matsumoto et al., ApJ 914 (2021) 131
  - Andersson & Kokkotas (1998)
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, G_cgs, M_sun, pi
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# ============================================================
# EOS models for neutron stars
# ============================================================
# Three representative EOSs: soft (APR4), moderate (SLy4), stiff (H4)
# M-R relations (approximate analytic fits):

def MR_APR4(M_Msun):
    """APR4 EOS: soft, R ~ 11 km for 1.4 Msun."""
    return 11.0e5 * (M_Msun / 1.4)**(-0.15)  # cm

def MR_SLy4(M_Msun):
    """SLy4 EOS: moderate, R ~ 11.7 km for 1.4 Msun."""
    return 11.7e5 * (M_Msun / 1.4)**(-0.12)  # cm

def MR_H4(M_Msun):
    """H4 EOS: stiff, R ~ 13.5 km for 1.4 Msun."""
    return 13.5e5 * (M_Msun / 1.4)**(-0.08)  # cm

eos_models = [
    ('APR4 (soft)', MR_APR4, '#2196F3'),
    ('SLy4 (moderate)', MR_SLy4, '#4CAF50'),
    ('H4 (stiff)', MR_H4, '#F44336'),
]

# NS mass range
M_Msun = np.linspace(1.0, 2.4, 500)
M_g = M_Msun * M_sun

# ============================================================
# f-mode and g-mode frequencies
# ============================================================
# f-mode: sigma^2 = 2l(l-1)/(2l+1) * GM/R^3 * [1 + beta_l C]
# beta_2 = 2(5*4+10-3)/(5*3) - 3 = 29/15

l_f = 2
beta_2 = 29.0 / 15.0

# g-mode: approximate from Reisenegger & Goldreich (1992)
# f_g ~ 0.1 * sqrt(N_BV_max^2 / (G M / R^3)) * f_f
# where N_BV is the Brunt-Vaisala frequency
# For typical NS: f_g ~ 0.1-0.5 * f_f * sqrt(C)

# Viscous damping timescale (BDNK):
# tau_l = R^2 / ((l-1)(2l+1) nu)
# nu = eta / (w/c^2) with w = (epsilon + p)

# Nuclear matter viscosity
eta_shear = 1e18  # g/(cm s) -- fiducial shear viscosity

# ============================================================
# GW strain sensitivity curves
# ============================================================
# Approximate noise curves for LIGO O4, A+, and ET
f_gw = np.logspace(1, 4, 1000)  # Hz

# LIGO O4 (approximate)
def S_n_LIGO_O4(f):
    """Approximate LIGO O4 noise PSD sqrt(S_n) in 1/sqrt(Hz)."""
    # Simplified analytic fit
    f0 = 25.0
    S_low = 1e-21 * (f0 / f)**4
    S_mid = 3e-24
    S_high = 3e-24 * (f / 1000.0)**2
    return np.sqrt(S_low**2 + S_mid**2 + S_high**2)

# LIGO A+ (factor ~2 better)
def S_n_LIGO_Aplus(f):
    f0 = 20.0
    S_low = 5e-22 * (f0 / f)**4
    S_mid = 1.5e-24
    S_high = 1.5e-24 * (f / 1000.0)**2
    return np.sqrt(S_low**2 + S_mid**2 + S_high**2)

# Einstein Telescope (factor ~10 better at high f)
def S_n_ET(f):
    f0 = 5.0
    S_low = 1e-22 * (f0 / f)**4
    S_mid = 3e-25
    S_high = 3e-25 * (f / 2000.0)**1.5
    return np.sqrt(S_low**2 + S_mid**2 + S_high**2)

# GW strain from f-mode oscillation (order of magnitude):
# h ~ (G/c^4) * (M R^2 omega^2 epsilon) / d
# For a 1% excitation at 10 Mpc:
def gw_strain(f_mode_Hz, M_g, R_cm, d_Mpc=10.0, epsilon_exc=0.01):
    """Estimate GW strain from f-mode oscillation."""
    d_cm = d_Mpc * 3.086e24  # Mpc to cm
    omega = 2.0 * pi * f_mode_Hz
    # Quadrupole formula: h ~ (G/c^4) * I * omega^2 / d
    # I ~ epsilon * M R^2
    I_quad = epsilon_exc * M_g * R_cm**2
    h = G_cgs / c_cgs**4 * I_quad * omega**2 / d_cm
    return h

# ============================================================
# Figure: 2x2 layout
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 11))

# Panel (a): f-mode and g-mode frequencies vs NS mass
ax = axes[0, 0]

for name, MR_func, color in eos_models:
    R_cm = MR_func(M_Msun)
    C = G_cgs * M_g / (R_cm * c_cgs**2)

    # f-mode frequency
    sigma_K2_sq = 2.0 * l_f * (l_f - 1) / (2*l_f + 1) * G_cgs * M_g / R_cm**3
    correction_f = 1.0 + beta_2 * C
    freq_f_Hz = np.sqrt(sigma_K2_sq * np.maximum(correction_f, 0.01)) / (2 * pi)
    freq_f_kHz = freq_f_Hz / 1e3

    # g-mode frequency (approximate scaling)
    freq_g_kHz = 0.4 * np.sqrt(C / 0.15) * np.sqrt(G_cgs * M_g / R_cm**3) / (2 * pi) / 1e3

    ax.plot(M_Msun, freq_f_kHz, '-', color=color, lw=2.2, label=f'{name}: $f$-mode')
    ax.plot(M_Msun, freq_g_kHz, '--', color=color, lw=1.8, label=f'{name}: $g$-mode')

# Newtonian reference for comparison
R_ref = 12e5
sigma_Newt_sq = 2.0 * l_f * (l_f - 1) / (2*l_f + 1) * G_cgs * M_g / MR_SLy4(M_Msun)**3
freq_Newt_kHz = np.sqrt(sigma_Newt_sq) / (2 * pi) / 1e3
ax.plot(M_Msun, freq_Newt_kHz, 'k:', lw=1.2, alpha=0.5, label='Newtonian (SLy4)')

ax.set_xlabel(r'NS mass $M / M_\odot$')
ax.set_ylabel(r'Frequency [kHz]')
ax.set_title(r'(a) NS oscillation frequencies ($\ell = 2$)')
ax.legend(fontsize=8, loc='upper left', frameon=True, edgecolor='0.7', ncol=2)
ax.set_xlim(1.0, 2.4)
ax.set_ylim(0, 4.0)
ax.grid(True, ls=':', alpha=0.3)

# Panel (b): BDNK viscous damping timescale vs mass
ax = axes[0, 1]

for name, MR_func, color in eos_models:
    R_cm = MR_func(M_Msun)
    C = G_cgs * M_g / (R_cm * c_cgs**2)

    # Enthalpy density: w = rho c^2 (1 + xi)
    # For NS interior: rho ~ M / (4/3 pi R^3), xi ~ 0.1-0.2
    rho_avg = M_g / (4.0/3.0 * pi * R_cm**3)
    xi_ns = 0.15  # typical for NS core
    w_c2 = rho_avg * (1.0 + xi_ns)  # g/cm^3

    # BDNK kinematic viscosity
    nu_bdnk = eta_shear / w_c2

    # Damping timescale: tau_l = R^2 / ((l-1)(2l+1) nu)
    tau_f = R_cm**2 / ((l_f - 1) * (2*l_f + 1) * nu_bdnk)

    ax.semilogy(M_Msun, tau_f, '-', color=color, lw=2.0, label=f'{name}')

    # Also show IS prediction for comparison (with tau_pi = 10^{-4} s)
    tau_pi = 1e-4
    # IS effective viscosity reduces nu at the f-mode frequency
    # nu_IS = nu / (1 + tau_pi * sigma_f)
    sigma_K2_sq = 2.0 * l_f * (l_f - 1) / (2*l_f + 1) * G_cgs * M_g / R_cm**3
    sigma_f = np.sqrt(sigma_K2_sq * np.maximum(1.0 + beta_2 * C, 0.01))
    nu_IS = nu_bdnk / (1.0 + tau_pi * sigma_f)
    tau_f_IS = R_cm**2 / ((l_f - 1) * (2*l_f + 1) * nu_IS)

    ax.semilogy(M_Msun, tau_f_IS, '--', color=color, lw=1.5, alpha=0.6)

ax.plot([], [], 'k-', lw=2, label='BDNK')
ax.plot([], [], 'k--', lw=1.5, alpha=0.6, label=r'IS ($\tau_\pi = 10^{-4}$ s)')

ax.set_xlabel(r'NS mass $M / M_\odot$')
ax.set_ylabel(r'Damping timescale $\tau_f$ [s]')
ax.set_title(r'(b) $f$-mode viscous damping ($\eta = 10^{18}$ g/cm/s)')
ax.legend(fontsize=9, loc='upper right', frameon=True, edgecolor='0.7')
ax.set_xlim(1.0, 2.4)
ax.grid(True, ls=':', alpha=0.3, which='both')

# Panel (c): GW strain sensitivity
ax = axes[1, 0]

# Detector sensitivity curves
ax.loglog(f_gw, S_n_LIGO_O4(f_gw), '-', color='gray', lw=1.5, alpha=0.7,
          label='LIGO O4')
ax.loglog(f_gw, S_n_LIGO_Aplus(f_gw), '--', color='gray', lw=1.5, alpha=0.7,
          label='LIGO A+')
ax.loglog(f_gw, S_n_ET(f_gw), '-.', color='gray', lw=1.5, alpha=0.7,
          label='Einstein Telescope')

# f-mode and g-mode GW signals at 10 Mpc
distances = [10.0, 50.0]  # Mpc
markers_d = ['o', 's']

for name, MR_func, color in eos_models:
    # At M = 1.4 Msun
    M_14 = 1.4 * M_sun
    R_14 = MR_func(1.4)
    C_14 = G_cgs * M_14 / (R_14 * c_cgs**2)

    sigma_f_sq = 2.0 * l_f * (l_f - 1) / (2*l_f + 1) * G_cgs * M_14 / R_14**3
    sigma_f = np.sqrt(sigma_f_sq * (1.0 + beta_2 * C_14))
    f_f = sigma_f / (2 * pi)
    f_g = 0.4 * np.sqrt(C_14 / 0.15) * np.sqrt(G_cgs * M_14 / R_14**3) / (2 * pi)

    for d, marker in zip(distances, markers_d):
        h_f = gw_strain(f_f, M_14, R_14, d_Mpc=d)
        h_g = gw_strain(f_g, M_14, R_14, d_Mpc=d, epsilon_exc=0.001)

        ax.plot(f_f / 1e3 * 1e3, h_f, marker, color=color, ms=8, zorder=5)
        ax.plot(f_g / 1e3 * 1e3, h_g, marker, color=color, ms=6, mfc='none',
                mew=1.5, zorder=5)

# Legend entries for distances
ax.plot([], [], 'ko', ms=8, label='$f$-mode, 10 Mpc')
ax.plot([], [], 'ks', ms=8, label='$f$-mode, 50 Mpc')
ax.plot([], [], 'ko', ms=6, mfc='none', mew=1.5, label='$g$-mode, 10 Mpc')

# Color legend
for name, _, color in eos_models:
    ax.plot([], [], '-', color=color, lw=3, label=name)

ax.set_xlabel(r'Frequency [Hz]')
ax.set_ylabel(r'GW strain $h$ or $\sqrt{S_n}$ [Hz$^{-1/2}$]')
ax.set_title(r'(c) GW detectability of NS modes ($M = 1.4\,M_\odot$)')
ax.legend(fontsize=7, loc='upper right', frameon=True, edgecolor='0.7', ncol=2)
ax.set_xlim(10, 5000)
ax.set_ylim(1e-27, 1e-20)
ax.grid(True, ls=':', alpha=0.3, which='both')

# Panel (d): Relativistic correction to f-mode and damping vs compactness
ax = axes[1, 1]

C_range = np.linspace(0.01, 0.35, 500)

# f-mode correction factor
freq_ratio_f = np.sqrt(1.0 + beta_2 * C_range)

# Higher l modes
l_vals = [2, 3, 4]
colors_l = ['#F44336', '#4CAF50', '#2196F3']

for j, l_val in enumerate(l_vals):
    beta_l = 2.0 * (5*l_val**2 + 5*l_val - 3) / \
             ((2*l_val + 1) * (2*l_val - 1)) - 3.0 / (l_val - 1)
    corr = np.sqrt(np.maximum(1.0 + beta_l * C_range, 0.01))
    ax.plot(C_range, corr, '-', color=colors_l[j], lw=2.0,
            label=rf'$\ell = {l_val}$: $\beta_{l_val} = {beta_l:.2f}$')

    # Damping correction (tau_rel / tau_Newt = 1 / (1 + xi C))
    # Through nu = eta / (rho (1 + xi)), tau ~ 1/(1+xi)
    xi_typical = 0.15
    tau_ratio = 1.0 / (1.0 + xi_typical * np.ones_like(C_range))
    # Plus the correction from sigma_Kl change
    total_corr = tau_ratio / corr  # damping timescale is reduced
    ax.plot(C_range, total_corr, '--', color=colors_l[j], lw=1.5, alpha=0.6)

ax.axhline(y=1.0, color='gray', ls='--', lw=1, alpha=0.5)
ax.plot([], [], 'k-', lw=2, label='Frequency ratio')
ax.plot([], [], 'k--', lw=1.5, alpha=0.6, label='Damping ratio')

# Shade NS range
ax.axvspan(0.1, 0.25, alpha=0.08, color='blue')
ax.text(0.175, 0.65, 'Typical NS', fontsize=9, color='blue', ha='center',
        transform=ax.get_xaxis_transform())

ax.set_xlabel(r'Compactness $\mathcal{C} = GM/Rc^2$')
ax.set_ylabel(r'Ratio (relativistic / Newtonian)')
ax.set_title(r'(d) Relativistic corrections to mode properties')
ax.legend(fontsize=9, loc='upper left', frameon=True, edgecolor='0.7')
ax.set_xlim(0, 0.35)
ax.set_ylim(0.5, 2.0)
ax.grid(True, ls=':', alpha=0.3)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_ns_modes_gw.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_ns_modes_gw.png')
print("Saved fig_ns_modes_gw.pdf/png")
plt.close(fig)
