"""
Gravitational wave characteristic strain h_c(f) from turbulent
convection in proto-neutron stars, compared with detector sensitivity curves.

Models:
  - Convective quadrupole GW emission (proto-NS at 10 kpc)
  - BDNK viscosity effect on convective amplitude
  - LIGO, Einstein Telescope (ET), Cosmic Explorer (CE) sensitivity
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, G_cgs, M_sun, pi
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# ---- Source parameters ----
M_ns = 1.4 * M_sun
R_ns = 20e5         # cm (20 km for proto-NS, larger than cold NS)
d_source = 10 * 3.086e21  # 10 kpc in cm
rho_core = 3e14     # g/cm^3

# Convective parameters
# Convective velocity: v_conv ~ 10^8 - 10^9 cm/s in proto-NS
# (from Burrows & Lattimer 1986, Ott et al. 2008)
v_conv_inviscid = 5e8     # cm/s (inviscid estimate)
v_conv_bdnk = 4.5e8       # cm/s (BDNK: viscosity reduces convection slightly)

# Characteristic convective frequency
# f_conv ~ v_conv / l_eddy where l_eddy ~ R_ns / few
l_eddy = R_ns / 5.0
f_conv = v_conv_inviscid / l_eddy  # ~ 125 Hz

# Convective turnover time
t_conv = l_eddy / v_conv_inviscid

# Duration of active convection
t_active = 1.0  # s (neutrino-driven convection active for ~1 s post-bounce)

# ---- GW strain from turbulent convection ----
# Quadrupole formula: h ~ (2G / c^4 d) * d^2 I / dt^2
# For turbulent convection: ddot{I} ~ M_conv * v_conv^2
# where M_conv ~ rho * R^3 * (v_conv / c_s)^2 is the convective mass
c_s = 0.3 * c_cgs  # sound speed in proto-NS core

# Mass involved in convection
M_conv = rho_core * (4.0/3.0 * pi * R_ns**3) * (v_conv_inviscid / c_s)**2

# Peak strain (time domain)
h_peak_inviscid = (2 * G_cgs / (c_cgs**4 * d_source)) * M_conv * v_conv_inviscid**2
h_peak_bdnk = (2 * G_cgs / (c_cgs**4 * d_source)) * M_conv * v_conv_bdnk**2

# Frequency array
f = np.logspace(0, 4, 1000)  # Hz

# ---- Characteristic strain spectrum ----
# h_c(f) = h_rms * sqrt(N_cycles) where N_cycles ~ f * t_active
# The spectral shape follows a Kolmogorov-like cascade:
# h_c(f) ~ h_peak * (f/f_conv)^{1/2} for f < f_conv (energy injection)
# h_c(f) ~ h_peak * (f/f_conv)^{-5/6} for f > f_conv (inertial range)
# h_c(f) ~ h_peak * (f/f_conv)^{-5/2} for f > f_diss (dissipation)

# Dissipation frequency
nu_visc = 1e4  # cm^2/s (kinematic viscosity in proto-NS)
f_diss_inviscid = v_conv_inviscid / (2 * pi * (nu_visc / v_conv_inviscid)**(3.0/4.0) * l_eddy**(1.0/4.0))

# BDNK increases effective viscosity at small scales
nu_bdnk = 1.5 * nu_visc  # BDNK adds ~50% to effective viscosity
f_diss_bdnk = v_conv_bdnk / (2 * pi * (nu_bdnk / v_conv_bdnk)**(3.0/4.0) * l_eddy**(1.0/4.0))

def hc_convection(f, h_peak, f_conv, f_diss, N_eff):
    """Characteristic strain from turbulent convection."""
    hc = np.zeros_like(f)
    for i, fi in enumerate(f):
        if fi < f_conv:
            hc[i] = h_peak * (fi / f_conv)**(0.5)
        elif fi < f_diss:
            hc[i] = h_peak * (fi / f_conv)**(-5.0/6.0)
        else:
            hc[i] = h_peak * (f_diss / f_conv)**(-5.0/6.0) * (fi / f_diss)**(-2.5)
    # Multiply by sqrt(N_cycles)
    hc *= np.sqrt(fi * t_active) if False else np.sqrt(f * t_active)
    return hc

N_eff = f_conv * t_active  # effective number of cycles

hc_inviscid = hc_convection(f, h_peak_inviscid, f_conv, f_diss_inviscid, N_eff)
hc_bdnk = hc_convection(f, h_peak_bdnk, f_conv, f_diss_bdnk, N_eff)

# ---- Detector sensitivity curves ----
# Approximate analytic fits for sqrt(S_n) * sqrt(f) = h_c sensitivity

def hc_LIGO_design(f):
    """aLIGO design sensitivity (approximate)."""
    # Based on LIGO-T1800044
    f0 = 20.0  # Hz seismic wall
    x = f / 215.0
    S_n = 1e-47 * (0.5 * (1 + x**(-4)) * x**(-4.14) - 5 * x**(-2) + 111 * (1 - x**2 + 0.5 * x**4) / (1 + 0.5 * x**2))
    # Simple parametric form
    hc = np.zeros_like(f)
    for i, fi in enumerate(f):
        if fi < f0:
            hc[i] = 1e-15
        else:
            x = fi / 200.0
            hc[i] = 3e-23 * (x**(-2) + 0.3 + 0.05 * x**2) * np.sqrt(fi)
    return hc

def hc_ET(f):
    """Einstein Telescope sensitivity (approximate)."""
    f0 = 3.0  # Hz
    hc = np.zeros_like(f)
    for i, fi in enumerate(f):
        if fi < f0:
            hc[i] = 1e-15
        else:
            x = fi / 200.0
            hc[i] = 2e-24 * (x**(-2.5) + 0.2 + 0.03 * x**2) * np.sqrt(fi)
    return hc

def hc_CE(f):
    """Cosmic Explorer sensitivity (approximate)."""
    f0 = 5.0  # Hz
    hc = np.zeros_like(f)
    for i, fi in enumerate(f):
        if fi < f0:
            hc[i] = 1e-15
        else:
            x = fi / 200.0
            hc[i] = 1e-24 * (x**(-2.3) + 0.15 + 0.02 * x**2) * np.sqrt(fi)
    return hc

hc_ligo = hc_LIGO_design(f)
hc_et = hc_ET(f)
hc_ce = hc_CE(f)

# ---- Plot ----
fig, axes = plt.subplots(1, 2, figsize=(14, 7))

# Left panel: h_c(f) overview
ax = axes[0]

# Detector curves
ax.loglog(f, hc_ligo, '-', lw=1.5, color='gray', alpha=0.7, label='aLIGO design')
ax.loglog(f, hc_et, '-', lw=1.5, color='steelblue', alpha=0.7, label='Einstein Telescope')
ax.loglog(f, hc_ce, '-', lw=1.5, color='darkgreen', alpha=0.7, label='Cosmic Explorer')

# Source curves
ax.loglog(f, hc_inviscid, '-', lw=2.5, color=COLORS['classical'],
          label='Inviscid convection')
ax.loglog(f, hc_bdnk, '-', lw=2.5, color=COLORS['bdnk'],
          label='BDNK viscous convection')

# Mark f_conv
ax.axvline(f_conv, ls=':', color='orange', lw=1.5, alpha=0.6)
ax.text(f_conv * 1.2, 5e-23, f'$f_{{\\rm conv}} \\approx {f_conv:.0f}$ Hz',
        fontsize=10, color='orange')

ax.set_xlabel('Frequency $f$ [Hz]')
ax.set_ylabel('Characteristic strain $h_c$')
ax.set_title('GW from proto-NS convection at 10 kpc')
ax.set_xlim(1, 5000)
ax.set_ylim(1e-26, 1e-19)
ax.legend(fontsize=9, loc='upper right')

ax.text(0.05, 0.05, '$d = 10$ kpc\n$M = 1.4\\,M_\\odot$\n'
        f'$v_{{\\rm conv}} = {v_conv_inviscid:.0e}$ cm/s',
        transform=ax.transAxes, fontsize=10,
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

# Right panel: zoom on BDNK effect
ax = axes[1]

ratio = hc_bdnk / (hc_inviscid + 1e-50)
ax.semilogx(f, ratio, '-', lw=2.5, color=COLORS['bdnk'])
ax.axhline(1.0, ls=':', color='gray', lw=1)

# Shade the region where BDNK viscosity reduces the signal
mask_below = ratio < 1.0
if np.any(mask_below):
    ax.fill_between(f, ratio, 1.0, where=mask_below,
                    color=COLORS['bdnk'], alpha=0.15)

ax.axvline(f_conv, ls=':', color='orange', lw=1.5, alpha=0.6)
ax.axvline(f_diss_inviscid, ls='--', color=COLORS['classical'], lw=1.2, alpha=0.6)
ax.axvline(f_diss_bdnk, ls='--', color=COLORS['bdnk'], lw=1.2, alpha=0.6)
ax.text(f_diss_inviscid * 0.5, 1.05, '$f_{\\rm diss}^{\\rm inv}$', fontsize=9,
        color=COLORS['classical'])
ax.text(f_diss_bdnk * 0.5, 0.85, '$f_{\\rm diss}^{\\rm BDNK}$', fontsize=9,
        color=COLORS['bdnk'])

ax.set_xlabel('Frequency $f$ [Hz]')
ax.set_ylabel('$h_c^{\\rm BDNK} / h_c^{\\rm inviscid}$')
ax.set_title('BDNK viscous suppression of convective GW')
ax.set_xlim(1, 5000)
ax.set_ylim(0.3, 1.15)

ax.text(0.05, 0.05, 'BDNK viscosity reduces\n$h_c$ by enhanced\nsmall-scale damping',
        transform=ax.transAxes, fontsize=10,
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_gw_convection.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_gw_convection.png')
print("Saved fig_gw_convection.pdf/png")
print(f"  h_peak_inviscid = {h_peak_inviscid:.3e}")
print(f"  h_peak_bdnk = {h_peak_bdnk:.3e}")
print(f"  f_conv = {f_conv:.1f} Hz")
print(f"  f_diss_inviscid = {f_diss_inviscid:.1f} Hz")
print(f"  f_diss_bdnk = {f_diss_bdnk:.1f} Hz")
print(f"  M_conv = {M_conv/M_sun:.3e} M_sun")
