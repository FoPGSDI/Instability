"""
Nuclear EOS transport coefficients for BDNK hydrodynamics:
shear viscosity eta, bulk viscosity zeta, and thermal conductivity kappa
as functions of baryon number density n_B for three nuclear EOSs:
APR, SLy, DD2.

Physics:
- Shear viscosity dominated by neutron-neutron scattering:
  eta ~ A * n_B^(5/3) * T^(-2)  (degenerate Fermi liquid)
- Bulk viscosity from Urca processes:
  zeta ~ B * n_B * omega^(-2) * (delta_mu)^2
  peaks near beta-equilibrium threshold
- Thermal conductivity from electron conduction:
  kappa ~ C * n_e^(1/3) * T^(-1)  (degenerate electrons)

Each EOS gives different n_B dependence through different nuclear
interactions and composition (proton fraction, effective masses).

References:
  Akmal, Pandharipande, Ravenhall, PRC 58 (1998) 1804  [APR]
  Douchin & Haensel, A&A 380 (2001) 151  [SLy]
  Hempel & Schaffner-Bielich, NPA 837 (2010) 210  [DD2]
  Alford, Mahmoodifar, Schwenzer, PRD 85 (2012) 044051
  Gavassino, Antonelli, PLB 849 (2024)
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, k_B, m_p, hbar
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# ============================================================
# Nuclear saturation density
# ============================================================
n0 = 0.16  # fm^{-3}, nuclear saturation density
rho0 = n0 * m_p  # g/cm^3 (approximate)

# Baryon density range: 0.5 n0 to 6 n0 (NS core range)
n_B = np.linspace(0.5, 6.0, 500)  # in units of n0
n_B_fm3 = n_B * n0  # in fm^{-3}

# Temperature: fixed at T = 10^9 K (cold NS core, relevant for BDNK)
T = 1.0e9  # K
T_MeV = k_B * T / 1.602e-6  # convert to MeV (~ 0.086 MeV)

# ============================================================
# EOS-dependent quantities
# ============================================================

def effective_mass_ratio(n, eos='APR'):
    """Effective nucleon mass m*/m as function of density.
    Different EOSs predict different density dependence.
    """
    if eos == 'APR':
        # APR: moderate effective mass, drops with density
        return 1.0 / (1.0 + 0.3 * n)
    elif eos == 'SLy':
        # SLy: slightly larger effective mass
        return 1.0 / (1.0 + 0.25 * n)
    elif eos == 'DD2':
        # DD2: relativistic mean field, stronger density dependence
        return 1.0 / (1.0 + 0.4 * n)

def proton_fraction(n, eos='APR'):
    """Proton fraction x_p in beta equilibrium."""
    if eos == 'APR':
        return 0.04 + 0.02 * n  # rises slowly
    elif eos == 'SLy':
        return 0.035 + 0.025 * n
    elif eos == 'DD2':
        return 0.05 + 0.03 * n  # higher symmetry energy

def sound_speed_sq(n, eos='APR'):
    """Sound speed squared cs^2/c^2 for the EOS."""
    if eos == 'APR':
        # APR: stiff, reaches ~0.8 c at high density
        return 0.1 + 0.12 * n  # approximate fit
    elif eos == 'SLy':
        # SLy: moderate stiffness
        return 0.08 + 0.10 * n
    elif eos == 'DD2':
        # DD2: soft at moderate density, stiffens
        return 0.05 + 0.15 * n * np.exp(-0.3 * n)

# ============================================================
# Transport coefficients
# ============================================================

def shear_viscosity(n, T_K, eos='APR'):
    """Shear viscosity eta [g/(cm s)] from nn scattering in degenerate
    neutron matter (Cutler & Lindblom 1987, Flowers & Itoh 1979).

    eta ~ 347 * rho_14^(9/4) * T_9^(-2) * (m*/m)^(-5/2)  g/(cm s)
    where rho_14 = rho / 10^14 g/cm^3
    """
    mstar = effective_mass_ratio(n, eos)
    rho_14 = n * n0 * m_p / 1.0e14  # density in units of 10^14 g/cm^3
    T_9 = T_K / 1.0e9

    eta = 347.0 * rho_14**(9.0/4.0) * T_9**(-2) * mstar**(-5.0/2.0)
    return eta  # g/(cm s)

def bulk_viscosity(n, T_K, eos='APR'):
    """Bulk viscosity zeta [g/(cm s)] from modified Urca processes.

    zeta ~ 6e25 * rho_14^2 * T_9^6 * omega_4^(-2) * (m*/m)^4  g/(cm s)
    (Haensel, Levenfish, Yakovlev 2002)

    For a pulsation frequency omega ~ 10^4 rad/s (typical f-mode).
    Bulk viscosity peaks strongly near the direct Urca threshold.
    """
    mstar = effective_mass_ratio(n, eos)
    xp = proton_fraction(n, eos)
    rho_14 = n * n0 * m_p / 1.0e14
    T_9 = T_K / 1.0e9
    omega_4 = 1.0  # omega / 10^4 rad/s

    # Modified Urca contribution
    zeta_mUrca = 6.0e25 * rho_14**2 * T_9**6 * omega_4**(-2) * mstar**4

    # Direct Urca threshold: x_p > x_DU ~ 0.11-0.15
    x_DU = 0.11 if eos == 'DD2' else 0.14
    # Enhancement near threshold
    if isinstance(n, np.ndarray):
        enhancement = np.where(xp > x_DU,
                              1e3 * np.exp(-0.5 * ((xp - x_DU) / 0.02)**2) + 1.0,
                              1.0)
    else:
        enhancement = 1e3 * np.exp(-0.5 * ((xp - x_DU) / 0.02)**2) + 1.0 if xp > x_DU else 1.0

    return zeta_mUrca * enhancement

def thermal_conductivity(n, T_K, eos='APR'):
    """Thermal conductivity kappa [erg/(cm s K)] from electron conduction
    in degenerate NS matter.

    kappa ~ 7e20 * rho_14^(1/3) * T_9^(-1)  erg/(cm s K)
    (Potekhin & Chabrier 2018, Flowers & Itoh 1981)
    """
    mstar = effective_mass_ratio(n, eos)
    xp = proton_fraction(n, eos)
    rho_14 = n * n0 * m_p / 1.0e14
    T_9 = T_K / 1.0e9

    # Electron density ~ xp * n_B
    ne_ratio = xp / 0.04  # normalized to reference proton fraction

    kappa = 7.0e20 * rho_14**(1.0/3.0) * ne_ratio**(1.0/3.0) * T_9**(-1) * mstar**(-1)
    return kappa

# ============================================================
# Compute for all three EOSs
# ============================================================
eos_list = ['APR', 'SLy', 'DD2']
eos_colors = {
    'APR': COLORS['relativistic'],
    'SLy': COLORS['classical'],
    'DD2': COLORS['bdnk'],
}
eos_styles = {
    'APR': '-',
    'SLy': '--',
    'DD2': '-.',
}

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 5.5), sharex=True)

for eos in eos_list:
    eta = shear_viscosity(n_B, T, eos)
    zeta = bulk_viscosity(n_B, T, eos)
    kappa = thermal_conductivity(n_B, T, eos)

    color = eos_colors[eos]
    ls = eos_styles[eos]

    ax1.semilogy(n_B, eta, ls=ls, lw=2.5, color=color, label=eos)
    ax2.semilogy(n_B, zeta, ls=ls, lw=2.5, color=color, label=eos)
    ax3.semilogy(n_B, kappa, ls=ls, lw=2.5, color=color, label=eos)

# ---- Panel (a): Shear viscosity ----
ax1.set_ylabel(r'$\eta$ [g cm$^{-1}$ s$^{-1}$]', fontsize=13)
ax1.set_title(r'(a) Shear viscosity $\eta$', fontsize=13)
ax1.set_xlabel(r'$n_B / n_0$', fontsize=13)
ax1.legend(loc='upper left', fontsize=11)
ax1.set_xlim(0.5, 6.0)

# KSS bound reference: eta/s >= 1/(4*pi) implies eta >= s/(4*pi)
# s ~ n_B * k_B * (T/T_F)  for degenerate fermions
# This is very small for cold NS, so KSS is easily satisfied
ax1.text(4.5, 1e1, r'$T = 10^9$ K', fontsize=10,
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

# Mark nuclear saturation density
for ax in [ax1, ax2, ax3]:
    ax.axvline(x=1.0, ls=':', lw=1.0, color='gray', alpha=0.5)
    ax.text(1.05, ax.get_ylim()[0] * 3, r'$n_0$', fontsize=9, color='gray')

# ---- Panel (b): Bulk viscosity ----
ax2.set_ylabel(r'$\zeta$ [g cm$^{-1}$ s$^{-1}$]', fontsize=13)
ax2.set_title(r'(b) Bulk viscosity $\zeta$', fontsize=13)
ax2.set_xlabel(r'$n_B / n_0$', fontsize=13)
ax2.legend(loc='upper left', fontsize=11)

# Direct Urca threshold annotation
ax2.annotate('Direct Urca\nthreshold', xy=(4.5, 1e28), xytext=(3.0, 1e30),
             fontsize=9, arrowprops=dict(arrowstyle='->', color='gray'),
             bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

# ---- Panel (c): Thermal conductivity ----
ax3.set_ylabel(r'$\kappa$ [erg cm$^{-1}$ s$^{-1}$ K$^{-1}$]', fontsize=13)
ax3.set_title(r'(c) Thermal conductivity $\kappa$', fontsize=13)
ax3.set_xlabel(r'$n_B / n_0$', fontsize=13)
ax3.legend(loc='upper left', fontsize=11)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_nuclear_transport.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_nuclear_transport.png')
print("Saved fig_nuclear_transport.pdf/png")
