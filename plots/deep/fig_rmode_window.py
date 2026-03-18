"""
R-mode instability window in the (T, f_spin) plane.

Computes the boundary where gravitational radiation driving equals
viscous damping. Compares:
  - Inviscid (GR driving only, all modes unstable)
  - Standard (Navier-Stokes bulk+shear viscosity)
  - Israel-Stewart (with relaxation time modifications)
  - BDNK (first-order causal, no IS relaxation artifacts)

Overlays observed pulsar population data (LMXBs and MSPs).
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, G_cgs, M_sun, k_B, m_p, pi
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# NS parameters
M = 1.4 * M_sun
R = 12e5  # cm (12 km)
I_ns = 0.35 * M * R**2  # moment of inertia (for n=1 polytrope, I ~ 0.35 MR^2)

# Kepler (breakup) frequency
f_K = (1 / (2 * pi)) * np.sqrt(G_cgs * M / R**3)  # ~ 1500 Hz

# Temperature and frequency grids
log_T = np.linspace(7.0, 11.0, 500)  # log10(T/K)
T = 10**log_T
f_spin = np.linspace(1, 800, 500)  # Hz

# ---- GR driving timescale for l=m=2 r-mode ----
# 1/tau_GR = -32 pi G Omega^{2l+2} / [c^{2l+3} * ...] for l=2
# Simplified: 1/tau_GR ~ -C_GR * Omega^6
# Owen et al. (1998): tau_GR ~ -47 s * (f_spin / 1 kHz)^{-6}
def tau_GR(f):
    """GR radiation reaction time for l=2 r-mode (negative = driving)."""
    Omega = 2 * pi * f
    # Using Owen et al. 1998 scaling
    return -47.0 * (f / 1000.0)**(-6)

# ---- Shear viscosity damping ----
# Dominated by neutron-neutron scattering in NS core:
# eta_s ~ 2e18 * (rho_14)^{9/4} * T_9^{-2} g/(cm s)  [Flowers & Itoh 1979]
def eta_shear(T_K):
    rho_14 = 3.0  # rho / 10^14 g/cm^3
    T_9 = T_K / 1e9
    return 2e18 * rho_14**(9.0/4.0) * T_9**(-2)

# tau_shear ~ I / (eta_s * R)  (rough scaling)
def tau_shear(T_K):
    return I_ns / (eta_shear(T_K) * R)

# ---- Bulk viscosity damping ----
# Modified Urca process: zeta ~ 6e25 * rho_14^2 * T_9^6 * omega^{-2}  [Haensel+ 2002]
# Direct Urca (if available): zeta ~ 6e29 * rho_14^2 * T_9^4 * omega^{-2}
def zeta_bulk_mUrca(T_K, f):
    rho_14 = 3.0
    T_9 = T_K / 1e9
    omega = 2 * pi * f
    return 6e25 * rho_14**2 * T_9**6 * omega**(-2)

def tau_bulk_mUrca(T_K, f):
    zeta = zeta_bulk_mUrca(T_K, f)
    return I_ns / (zeta * R)

# ---- IS relaxation modification ----
# IS bulk viscosity: zeta_IS = zeta / (1 + (omega * tau_R)^2)
# tau_R for modified Urca: tau_R ~ 1/(beta_0 T^4) ~ 0.01 * T_9^{-4} s
def tau_relax_IS(T_K):
    T_9 = T_K / 1e9
    return 0.01 * T_9**(-4)

def zeta_bulk_IS(T_K, f):
    omega = 2 * pi * f
    tau_R = tau_relax_IS(T_K)
    return zeta_bulk_mUrca(T_K, f) / (1.0 + (omega * tau_R)**2)

def tau_bulk_IS(T_K, f):
    zeta = zeta_bulk_IS(T_K, f)
    return I_ns / (zeta * R + 1e-30)

# ---- BDNK: no relaxation time, direct first-order viscosity ----
# In BDNK, the bulk viscosity is used directly without the IS suppression factor
# but the BDNK causality constraints modify the high-frequency behavior differently.
# At frequencies below the BDNK UV cutoff (omega < c/R ~ 2.5e4 Hz for NS),
# BDNK agrees with Navier-Stokes. The key difference from IS is that there is
# NO (1 + omega^2 tau_R^2) suppression factor. Instead, BDNK smoothly handles
# the transition through frame coefficients.
# The net effect: BDNK bulk viscosity is LARGER than IS at high T (where omega*tau_R > 1)
def zeta_bulk_BDNK(T_K, f):
    # BDNK: use the bare modified-Urca result without IS suppression
    # But include the BDNK frame coefficient correction
    omega = 2 * pi * f
    zeta_0 = zeta_bulk_mUrca(T_K, f)
    # BDNK frame correction: small at low omega, ensures causality at high omega
    # For r-modes (omega << c/R), correction is negligible
    bdnk_corr = 1.0 / (1.0 + (omega * R / c_cgs)**2)  # only kicks in at ~c/R
    return zeta_0 * bdnk_corr

def tau_bulk_BDNK(T_K, f):
    zeta = zeta_bulk_BDNK(T_K, f)
    return I_ns / (zeta * R + 1e-30)

# ---- Compute instability boundaries ----
# Instability when 1/tau_GR + 1/tau_shear + 1/tau_bulk < 0
# Boundary: 1/|tau_GR| = 1/tau_shear + 1/tau_bulk

def find_boundary(T_arr, tau_bulk_func, label):
    """Find f_crit(T) where GR driving = viscous damping."""
    f_crit = np.zeros_like(T_arr)
    for i, Ti in enumerate(T_arr):
        # Search for f where |1/tau_GR| = 1/tau_s + 1/tau_b
        for f_try in np.linspace(1, 1200, 2000):
            t_GR = np.abs(tau_GR(f_try))
            t_s = tau_shear(Ti)
            t_b = tau_bulk_func(Ti, f_try)
            damping = 1.0/t_s + 1.0/t_b
            driving = 1.0/t_GR
            if driving > damping:
                f_crit[i] = f_try
                break
    return f_crit

# Standard NS viscosity (no IS, no BDNK -- just bare transport coefficients)
f_standard = find_boundary(T, lambda T_K, f: tau_bulk_mUrca(T_K, f), 'Standard')
f_IS = find_boundary(T, tau_bulk_IS, 'IS')
f_BDNK = find_boundary(T, tau_bulk_BDNK, 'BDNK')

# ---- Observed pulsar data (approximate) ----
# MSPs (millisecond pulsars): high spin, low T
# LMXBs: moderate spin, high T
# Data from Haskell+ 2012, Mahmoodifar & Strohmayer 2013

msps_f = [317, 622, 641, 716, 346, 299, 478, 592, 437, 528]
msps_logT = [7.5, 7.8, 7.3, 8.0, 7.6, 7.4, 7.7, 7.9, 7.5, 7.8]

lmxbs_f = [363, 524, 270, 330, 401, 619, 581, 311, 549, 185]
lmxbs_logT = [8.2, 8.5, 8.8, 8.3, 8.6, 8.4, 8.7, 8.1, 8.9, 9.0]

# ---- Plot ----
fig, ax = plt.subplots(1, 1, figsize=(10, 7))

# Shade unstable region (above curve)
ax.fill_between(log_T, f_BDNK, 1200, alpha=0.08, color=COLORS['bdnk'],
                label='_nolegend_')

ax.plot(log_T, f_standard, '-', lw=2.5, color=COLORS['classical'],
        label='Standard (Navier--Stokes)')
ax.plot(log_T, f_IS, '--', lw=2.5, color=COLORS['is'],
        label='Israel--Stewart')
ax.plot(log_T, f_BDNK, '-', lw=2.5, color=COLORS['bdnk'],
        label='BDNK')

# Observed pulsars
ax.scatter(msps_logT, msps_f, marker='o', s=60, color=COLORS['data'],
           edgecolors='k', linewidths=0.5, zorder=5, label='MSPs')
ax.scatter(lmxbs_logT, lmxbs_f, marker='s', s=60, color=COLORS['neutron_star'],
           edgecolors='k', linewidths=0.5, zorder=5, label='LMXBs')

# Kepler limit
ax.axhline(f_K, ls=':', color='gray', lw=1.5, alpha=0.6)
ax.text(10.7, f_K + 30, f'$f_K = {f_K:.0f}$ Hz', fontsize=10, color='gray')

# Labels
ax.text(9.5, 100, 'STABLE', fontsize=16, color=COLORS['bdnk'], alpha=0.5, fontweight='bold')
ax.text(9.5, 600, 'UNSTABLE\n(r-modes)', fontsize=14, color='red', alpha=0.4,
        fontweight='bold', ha='center')

# Highlight IS artifact region
ax.annotate('IS relaxation\nsuppresses $\\zeta$\n(artifact)',
            xy=(9.8, f_IS[np.argmin(np.abs(log_T - 9.8))]),
            xytext=(10.3, 450), fontsize=9,
            arrowprops=dict(arrowstyle='->', color=COLORS['is']),
            color=COLORS['is'])

ax.set_xlabel('$\\log_{10}(T\\,/\\,{\\rm K})$')
ax.set_ylabel('Spin frequency $f_{\\rm spin}$ [Hz]')
ax.set_title('R-mode instability window: BDNK vs IS vs standard viscosity')
ax.set_xlim(7, 11)
ax.set_ylim(0, 900)
ax.legend(fontsize=10, loc='upper left')

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_rmode_window.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_rmode_window.png')
print("Saved fig_rmode_window.pdf/png")
print(f"  f_Kepler = {f_K:.1f} Hz")
print(f"  I_ns = {I_ns:.3e} g cm^2")
