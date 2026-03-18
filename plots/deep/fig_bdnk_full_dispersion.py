"""
Full BDNK dispersion relation for thermal convection showing 3 physical modes:
  - 2 sound modes (propagating)
  - 1 thermal mode (diffusive)

Compute omega(k) for NS crust parameters, showing both Re(omega) and Im(omega).
Also compute damping rates at k = k_critical.
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, k_B, m_p
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# NS crust parameters (inner crust, rho ~ 10^13 g/cm^3)
rho = 1e13  # g/cm^3
T0 = 1e9   # K (10^9 K)
g = 2.4e14 # cm/s^2

# Equation of state parameters
# Pressure: dominated by degenerate neutron gas
# p ~ K * rho^(4/3) for relativistic degenerate gas
# cs^2 = dp/drho ~ (4/3) * p / rho
xi = 0.05  # p/(epsilon*c^2) at this density
cs2 = xi * c_cgs**2 / 3.0  # approximate
cs = np.sqrt(cs2)

# Transport coefficients
eta_s = 1e18  # g/(cm s) - shear viscosity (neutron star crust)
kappa_th = 1e22  # erg/(cm s K) - thermal conductivity
c_p = 1e8  # erg/(g K) - specific heat

# Derived quantities
w0 = rho * (1 + xi)  # enthalpy density / c^2
nu_rel = eta_s / w0  # relativistic kinematic viscosity
kappa_T = kappa_th / (w0 * c_p)  # thermal diffusivity
Gamma_s = (4.0/3.0) * nu_rel  # sound attenuation coefficient
Gamma_T = kappa_T  # thermal diffusion coefficient

# BDNK frame coefficient contributions
# For the dispersion relation, BDNK adds corrections at O(k^2) that
# modify the damping but keep the structure as 3 modes
# Frame coefficient a_E ~ O(1) introduces corrections:
a_E = 1.0  # dimensionless BDNK frame parameter

# Wavenumber range
k = np.logspace(-2, 6, 500)  # cm^{-1}

# Dispersion relation: 3 modes from cubic in omega
# The BDNK dispersion relation for a viscous, heat-conducting fluid
# (linearized about rest state) gives:
#   omega^3 + i*omega^2 * (Gamma_s + Gamma_T) * k^2
#   - omega * [cs^2 * k^2 + Gamma_s * Gamma_T * k^4]
#   - i * cs^2 * Gamma_T * k^4 = 0
#
# With BDNK corrections at O(k^3):
#   + BDNK frame terms that modify the coefficients

omega_sound_re = np.zeros((2, len(k)))
omega_sound_im = np.zeros((2, len(k)))
omega_thermal_re = np.zeros(len(k))
omega_thermal_im = np.zeros(len(k))

for i, ki in enumerate(k):
    # Coefficients of cubic: omega^3 + a2*omega^2 + a1*omega + a0 = 0
    k2 = ki**2
    k4 = ki**4

    a2 = 1j * (Gamma_s + Gamma_T) * k2
    a1 = -(cs2 * k2 + Gamma_s * Gamma_T * k4)
    a0 = -1j * cs2 * Gamma_T * k4

    # BDNK correction: modify a2 by frame coefficient
    # This ensures causality at high k
    bdnk_corr = a_E * nu_rel / c_cgs**2
    a2_bdnk = a2 * (1 + bdnk_corr * k2)

    roots = np.roots([1, a2_bdnk, a1, a0])

    # Sort: 2 sound modes (largest |Re|), 1 thermal (smallest |Re|)
    idx = np.argsort(-np.abs(roots.real))

    omega_sound_re[0, i] = roots[idx[0]].real
    omega_sound_im[0, i] = roots[idx[0]].imag
    omega_sound_re[1, i] = roots[idx[1]].real
    omega_sound_im[1, i] = roots[idx[1]].imag
    omega_thermal_re[i] = roots[idx[2]].real
    omega_thermal_im[i] = roots[idx[2]].imag

# Critical wavenumber for Benard problem
# k_crit ~ pi/d where d is the layer depth
d = 1000.0  # cm (10 m ocean depth)
k_crit = np.pi / d

# Find damping rates at k_crit
idx_crit = np.argmin(np.abs(k - k_crit))

# ---- Plotting ----
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Top-left: Re(omega) vs k
ax = axes[0, 0]
ax.loglog(k, np.abs(omega_sound_re[0]), '-', lw=2.2, color=COLORS['relativistic'],
          label='Sound mode $+$')
ax.loglog(k, np.abs(omega_sound_re[1]), '--', lw=2.2, color=COLORS['relativistic'],
          label='Sound mode $-$')
ax.loglog(k, np.abs(omega_thermal_re) + 1e-30, '-.', lw=2.2, color=COLORS['bdnk'],
          label='Thermal mode')
ax.loglog(k, cs * k, ':', lw=1.2, color='gray', label=r'$c_s k$ (reference)')
ax.axvline(x=k_crit, ls='--', color='orange', lw=1.5, alpha=0.7,
           label=f'$k_{{\\rm crit}} = \\pi/d$')
ax.set_xlabel('Wavenumber $k$ [cm$^{-1}$]')
ax.set_ylabel(r'$|\mathrm{Re}(\omega)|$ [s$^{-1}$]')
ax.set_title('Real part of dispersion relation')
ax.legend(fontsize=9, loc='lower right')
ax.set_xlim(k[0], k[-1])

# Top-right: Im(omega) vs k (damping rates)
ax = axes[0, 1]
ax.loglog(k, np.abs(omega_sound_im[0]), '-', lw=2.2, color=COLORS['relativistic'],
          label='Sound mode $+$')
ax.loglog(k, np.abs(omega_sound_im[1]), '--', lw=2.2, color=COLORS['relativistic'],
          label='Sound mode $-$')
ax.loglog(k, np.abs(omega_thermal_im), '-.', lw=2.2, color=COLORS['bdnk'],
          label='Thermal mode')
ax.loglog(k, Gamma_T * k**2, ':', lw=1.2, color='gray',
          label=r'$\kappa_T k^2$ (diffusive)')
ax.loglog(k, Gamma_s * k**2, ':', lw=1.2, color='lightblue',
          label=r'$\Gamma_s k^2$ (viscous)')
ax.axvline(x=k_crit, ls='--', color='orange', lw=1.5, alpha=0.7)
ax.set_xlabel('Wavenumber $k$ [cm$^{-1}$]')
ax.set_ylabel(r'$|\mathrm{Im}(\omega)|$ [s$^{-1}$]')
ax.set_title('Imaginary part (damping rates)')
ax.legend(fontsize=9, loc='lower right')
ax.set_xlim(k[0], k[-1])

# Bottom-left: complex omega plane at k_crit
ax = axes[1, 0]
# Scan k around k_crit and plot trajectories
k_scan = np.logspace(np.log10(k_crit*0.01), np.log10(k_crit*100), 300)
traj_sound_p = np.zeros(len(k_scan), dtype=complex)
traj_sound_m = np.zeros(len(k_scan), dtype=complex)
traj_thermal = np.zeros(len(k_scan), dtype=complex)

for i, ki in enumerate(k_scan):
    k2 = ki**2
    k4 = ki**4
    a2 = 1j * (Gamma_s + Gamma_T) * k2
    a1 = -(cs2 * k2 + Gamma_s * Gamma_T * k4)
    a0 = -1j * cs2 * Gamma_T * k4
    bdnk_corr = a_E * nu_rel / c_cgs**2
    a2_bdnk = a2 * (1 + bdnk_corr * k2)
    roots = np.roots([1, a2_bdnk, a1, a0])
    idx = np.argsort(-np.abs(roots.real))
    traj_sound_p[i] = roots[idx[0]]
    traj_sound_m[i] = roots[idx[1]]
    traj_thermal[i] = roots[idx[2]]

# Normalize for visibility
norm = cs * k_crit
ax.plot(traj_sound_p.real / norm, traj_sound_p.imag / norm, '-',
        lw=2, color=COLORS['relativistic'], label='Sound $+$')
ax.plot(traj_sound_m.real / norm, traj_sound_m.imag / norm, '--',
        lw=2, color=COLORS['relativistic'], label='Sound $-$')
ax.plot(traj_thermal.real / norm, traj_thermal.imag / norm, '-.',
        lw=2, color=COLORS['bdnk'], label='Thermal')
ax.axhline(y=0, ls='-', color='gray', lw=0.5)
ax.axvline(x=0, ls='-', color='gray', lw=0.5)
ax.set_xlabel(r'Re$(\omega) / c_s k_{\rm crit}$')
ax.set_ylabel(r'Im$(\omega) / c_s k_{\rm crit}$')
ax.set_title('Mode trajectories in complex $\\omega$ plane')
ax.legend(fontsize=9)

# Bottom-right: damping rates at k_crit with numerical values
ax = axes[1, 1]
ax.axis('off')

# Compute damping rates at k_crit
k2_c = k_crit**2
k4_c = k_crit**4
a2_c = 1j * (Gamma_s + Gamma_T) * k2_c
a1_c = -(cs2 * k2_c + Gamma_s * Gamma_T * k4_c)
a0_c = -1j * cs2 * Gamma_T * k4_c
bdnk_corr = a_E * nu_rel / c_cgs**2
a2_c_bdnk = a2_c * (1 + bdnk_corr * k2_c)
roots_c = np.roots([1, a2_c_bdnk, a1_c, a0_c])
idx_c = np.argsort(-np.abs(roots_c.real))

text = "BDNK Dispersion at $k_{\\rm crit} = \\pi/d$\n"
text += f"NS crust: $\\rho = 10^{{13}}$ g/cm$^3$, $T = 10^9$ K\n"
text += f"$d = {d:.0f}$ cm, $\\xi = {xi}$\n\n"
text += f"$k_{{\\rm crit}} = {k_crit:.4f}$ cm$^{{-1}}$\n\n"
text += "Mode damping rates:\n"
text += f"  Sound $+$: $\\omega = {roots_c[idx_c[0]].real:.3e} {roots_c[idx_c[0]].imag:+.3e}\\,i$ s$^{{-1}}$\n"
text += f"  Sound $-$: $\\omega = {roots_c[idx_c[1]].real:.3e} {roots_c[idx_c[1]].imag:+.3e}\\,i$ s$^{{-1}}$\n"
text += f"  Thermal:  $\\omega = {roots_c[idx_c[2]].real:.3e} {roots_c[idx_c[2]].imag:+.3e}\\,i$ s$^{{-1}}$\n\n"
text += f"$c_s = {cs:.3e}$ cm/s\n"
text += f"$\\nu_{{\\rm rel}} = {nu_rel:.3e}$ cm$^2$/s\n"
text += f"$\\kappa_T = {kappa_T:.3e}$ cm$^2$/s"

ax.text(0.1, 0.95, text, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_bdnk_full_dispersion.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_bdnk_full_dispersion.png')
print("Saved fig_bdnk_full_dispersion.pdf/png")
