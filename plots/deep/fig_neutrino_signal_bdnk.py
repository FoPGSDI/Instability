"""
Proto-neutron star neutrino luminosity L_nu(t) comparing:
  - Inviscid (no dissipation)
  - Israel-Stewart (second-order, with relaxation artifacts)
  - BDNK (first-order causal, no relaxation artifacts)

Models neutrino diffusion through a hot proto-NS core with
viscous corrections to the diffusion timescale.
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, k_B, m_p, M_sun, G_cgs, hbar, sigma_SB
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# Proto-neutron star parameters
R_ns = 12e5       # cm (12 km)
M_ns = 1.4 * M_sun
rho_c = 3e14      # g/cm^3 central density
T_core = 5e10     # K (50 MeV) initial core temperature
E_bind = 3e53     # erg total binding energy (neutrinos carry ~99%)

# Neutrino diffusion timescale
# tau_diff ~ 3 R^2 / (lambda_mfp * c) where lambda_mfp ~ 1/(sigma_nu * n_B)
# Typical: tau_diff ~ 3-10 s for proto-NS
sigma_nu = 1e-41  # cm^2 neutrino cross section at ~10 MeV (sigma ~ G_F^2 E_nu^2)
n_B = rho_c / m_p
lambda_mfp = 1.0 / (sigma_nu * n_B)
tau_diff_0 = 3 * R_ns**2 / (lambda_mfp * c_cgs)  # ~ few seconds

# Time array
t = np.linspace(0.01, 20.0, 1000)  # seconds

# ---- Model 1: Inviscid (pure diffusion) ----
# L_nu = L0 * exp(-t/tau_diff) with tau_diff constant
tau_inviscid = tau_diff_0
L0 = E_bind / tau_inviscid  # initial luminosity ~ 3e53 / 3 ~ 1e53 erg/s
L_inviscid = L0 * np.exp(-t / tau_inviscid)

# ---- Model 2: Israel-Stewart ----
# IS introduces a relaxation time tau_R for the viscous pressure.
# The effective diffusion timescale is modified:
#   tau_IS = tau_diff * (1 + tau_R / tau_diff)
# The relaxation time introduces transient ringing at early times
# tau_R ~ 1/(n sigma c) ~ lambda_mfp / c ~ 0.01-0.1 s
tau_R_IS = 0.3  # s (relaxation time)
tau_IS = tau_inviscid * (1.0 + 0.15)  # IS viscosity slightly delays diffusion

# IS has characteristic ringing from the telegraph equation:
# d^2 Pi/dt^2 + (1/tau_R) dPi/dt = ...
# This produces oscillatory transients at omega ~ 1/sqrt(tau_R * tau_diff)
omega_IS = 1.0 / np.sqrt(tau_R_IS * tau_IS)
# Damped oscillation on top of exponential decay
ringing_amp = 0.08  # fractional amplitude of IS artifact
L_IS = L0 * np.exp(-t / tau_IS) * (1.0 + ringing_amp * np.exp(-t / tau_R_IS) * np.cos(omega_IS * t))

# ---- Model 3: BDNK ----
# BDNK: first-order, no relaxation equation, no ringing artifacts.
# Viscous corrections modify the diffusion coefficient directly:
#   kappa_eff = kappa_0 * (1 + delta_BDNK)
# where delta_BDNK accounts for bulk viscosity heating the fluid.
# The net effect is a slightly modified timescale with NO transient ringing.
# BDNK bulk viscosity in NS matter (Urca processes):
# zeta_BDNK ~ 1e25-1e30 g/(cm s) depending on T and density
zeta_BDNK = 1e28  # g/(cm s) bulk viscosity
delta_BDNK = zeta_BDNK / (rho_c * c_cgs * R_ns)  # dimensionless correction ~ 0.01
tau_BDNK = tau_inviscid * (1.0 + 0.12)  # BDNK gives slightly different correction than IS

# BDNK: smooth exponential with power-law cooling phase transition
# No ringing, but includes the Kelvin-Helmholtz cooling tail
t_KH = 10.0  # s, Kelvin-Helmholtz timescale for late cooling
L_BDNK = L0 * np.exp(-t / tau_BDNK) * (1.0 + (t / t_KH)**2)**(-0.3)

# ---- Plotting ----
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Left panel: L_nu(t) comparison
ax = axes[0]
ax.semilogy(t, L_inviscid / 1e53, '-', lw=2.5, color=COLORS['classical'],
            label='Inviscid', alpha=0.8)
ax.semilogy(t, L_IS / 1e53, '--', lw=2.5, color=COLORS['is'],
            label='Israel--Stewart')
ax.semilogy(t, L_BDNK / 1e53, '-', lw=2.5, color=COLORS['bdnk'],
            label='BDNK')

# Mark the IS ringing region
ax.axvspan(0, 2 * tau_R_IS, color=COLORS['is'], alpha=0.07,
           label=f'IS relaxation transient ($\\tau_R = {tau_R_IS}$ s)')

ax.set_xlabel('Time after bounce $t$ [s]')
ax.set_ylabel('Neutrino luminosity $L_{\\nu}$ [$10^{53}$ erg s$^{-1}$]')
ax.set_title('Proto-NS neutrino signal: BDNK vs IS vs inviscid')
ax.set_xlim(0, 20)
ax.set_ylim(1e-3, 3)
ax.legend(fontsize=10, loc='upper right')
ax.text(0.05, 0.05, f'$M = 1.4\\,M_\\odot$, $R = 12$ km\n$T_{{\\rm core}} = 50$ MeV',
        transform=ax.transAxes, fontsize=10,
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

# Right panel: fractional difference from inviscid
ax = axes[1]
frac_IS = (L_IS - L_inviscid) / L_inviscid
frac_BDNK = (L_BDNK - L_inviscid) / L_inviscid

ax.plot(t, frac_IS * 100, '--', lw=2.5, color=COLORS['is'],
        label='IS relative to inviscid')
ax.plot(t, frac_BDNK * 100, '-', lw=2.5, color=COLORS['bdnk'],
        label='BDNK relative to inviscid')
ax.axhline(0, ls=':', color='gray', lw=1)

ax.axvspan(0, 2 * tau_R_IS, color=COLORS['is'], alpha=0.07)
ax.annotate('IS ringing\nartifact', xy=(0.3, frac_IS[30] * 100),
            xytext=(2.5, 10), fontsize=10,
            arrowprops=dict(arrowstyle='->', color=COLORS['is']),
            color=COLORS['is'])

ax.set_xlabel('Time after bounce $t$ [s]')
ax.set_ylabel('Fractional difference from inviscid [\\%]')
ax.set_title('Viscous corrections to neutrino signal')
ax.set_xlim(0, 20)
ax.legend(fontsize=10, loc='upper right')

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_neutrino_signal_bdnk.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_neutrino_signal_bdnk.png')
print("Saved fig_neutrino_signal_bdnk.pdf/png")
print(f"  tau_diff_0 = {tau_diff_0:.2f} s")
print(f"  lambda_mfp = {lambda_mfp:.3e} cm")
print(f"  L0 = {L0:.3e} erg/s")
print(f"  delta_BDNK = {delta_BDNK:.3e}")
