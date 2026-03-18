"""
Deep Research 6: Mixing length vs time post-merger for NS merger ejecta
with BDNK viscosity from nuclear transport coefficients.

Model: merger ejecta with rho ~ 10^{10} g/cm^3, v_exp ~ 0.1c
BDNK viscosity from nuclear transport coefficients.
Fastest-growing wavelength and mixing length.

References:
  - Radice & Bernuzzi, ApJ 869 (2018) 130
  - Duffell, ApJS 197 (2011) 15
  - Matsumoto et al., ApJ 914 (2021) 131
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, G_cgs, M_sun, m_p, k_B, pi
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# ============================================================
# NS merger ejecta parameters
# ============================================================
rho_0 = 1e10          # g/cm^3 -- initial contact density
v_exp = 0.1 * c_cgs   # expansion velocity ~ 0.1c
T_nuc = 3e10           # K (~ 3 MeV nuclear temperature)

# Nuclear transport coefficients (Alford+ 2018, Schmitt & Shternin 2018)
# Shear viscosity of dense nuclear matter:
# eta ~ 10^{15} - 10^{18} g/(cm s) depending on T and rho
eta_low = 1e15         # g/(cm s) -- high-T, low-density limit
eta_high = 1e18        # g/(cm s) -- low-T, high-density limit
eta_fiducial = 1e16    # fiducial value

# Bulk viscosity (modified Urca process):
# zeta ~ 10^{25} (T/10^9 K)^{-2} (omega/1 kHz)^{-2} g/(cm s)
# but for the slow RT modes, bulk viscosity is typically subdominant

# EOS parameter
xi = 0.08              # p/(rho c^2) for merger ejecta
Gamma_eos = 2.0        # polytropic index for nuclear matter

# Enthalpy density
w = rho_0 * c_cgs**2 * (1.0 + xi)  # erg/cm^3
w_cgs = w / c_cgs**2  # g/cm^3 (enthalpy per c^2)

# BDNK kinematic viscosity
nu_bdnk = eta_fiducial / w_cgs

# Effective gravity at contact interface
# g_eff ~ GM_remnant / R_contact^2 + centrifugal
M_rem = 2.5 * M_sun
R_contact = 2e6  # cm (20 km)
g_eff_0 = G_cgs * M_rem / R_contact**2  # ~ 5.5e13 cm/s^2

# Atwood number (density contrast across contact)
rho_ratio = 2.0  # moderate contrast
A_rel = (rho_ratio * (1 + xi) - 1.0 * (1 + 0.01)) / \
        (rho_ratio * (1 + xi) + 1.0 * (1 + 0.01))

# ============================================================
# Time evolution post-merger
# ============================================================
t_ms = np.logspace(-1, 3, 500)  # ms post-merger
t_s = t_ms * 1e-3                # seconds

# Effective gravity decays as remnant settles
# g_eff(t) ~ g_eff_0 * exp(-t/tau_settle) + g_eff_residual
tau_settle = 0.01  # 10 ms settling time
g_eff_residual = 1e12  # residual gravitational gradient
g_eff_t = g_eff_0 * np.exp(-t_s / tau_settle) + g_eff_residual

# Density also evolves as ejecta expand
rho_t = rho_0 * np.exp(-t_s / (R_contact / v_exp))

# BDNK kinematic viscosity evolves with density
eta_t = eta_fiducial * (rho_t / rho_0)**0.5  # rough scaling
w_t = rho_t * c_cgs**2 * (1.0 + xi)
nu_t = eta_t / (w_t / c_cgs**2)

# ============================================================
# Fastest-growing wavelength
# ============================================================
# From viscous RT: sigma(k) = (-nu k^2 + sqrt(nu^2 k^4 + 4gAk)) / 2
# Maximum at d(sigma)/dk = 0:
# k_max ~ (g A / (3 nu^2))^{1/3}  (viscous regime)
# lambda_max = 2 pi / k_max

k_max_t = (g_eff_t * np.abs(A_rel) / (3.0 * nu_t**2))**(1.0/3.0)
lambda_max_t = 2.0 * pi / k_max_t  # cm
lambda_max_km = lambda_max_t / 1e5  # km

# Maximum growth rate at k_max
sigma_max_t = np.sqrt(g_eff_t * k_max_t * np.abs(A_rel))

# ============================================================
# Mixing length evolution
# ============================================================
# RT mixing length grows as h(t) ~ alpha * A * g * t^2 (self-similar)
# alpha ~ 0.05 (RT mixing coefficient from simulations)
alpha_RT = 0.05

# Compute cumulative mixing length
# dh/dt ~ alpha * A * g * t => h ~ alpha * A * integral(g(t') * t' dt')
# For early times use numerical integration
h_mix = np.zeros_like(t_s)
dt = np.diff(t_s)
for i in range(1, len(t_s)):
    # Self-similar growth rate
    dh = alpha_RT * np.abs(A_rel) * g_eff_t[i] * t_s[i] * (t_s[i] - t_s[i-1])
    h_mix[i] = h_mix[i-1] + dh
    # Cap at the system size
    h_mix[i] = min(h_mix[i], R_contact)

h_mix_km = h_mix / 1e5  # convert to km

# ============================================================
# Viscous cutoff mixing length (BDNK)
# ============================================================
# Viscous cutoff scale: l_visc ~ (nu^2 / (g A))^{1/3}
l_visc_t = (nu_t**2 / (g_eff_t * np.abs(A_rel)))**(1.0/3.0)
l_visc_km = l_visc_t / 1e5

# ============================================================
# Figure: 2x2 layout
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 11))

# Panel (a): Mixing length vs time for different viscosities
ax = axes[0, 0]

eta_range = [1e15, 1e16, 1e17, 1e18]
colors_eta = ['#2196F3', '#4CAF50', '#FF9800', '#F44336']

for j, eta_val in enumerate(eta_range):
    eta_t_j = eta_val * (rho_t / rho_0)**0.5
    nu_t_j = eta_t_j / (w_t / c_cgs**2)

    h_j = np.zeros_like(t_s)
    for i in range(1, len(t_s)):
        # Include viscous damping: effective growth reduced by viscosity
        k_max_j = (g_eff_t[i] * np.abs(A_rel) / (3.0 * nu_t_j[i]**2 + 1e-30))**(1.0/3.0)
        sigma_j = np.sqrt(g_eff_t[i] * k_max_j * np.abs(A_rel)) \
                  / (1.0 + nu_t_j[i] * k_max_j**2 / (np.sqrt(g_eff_t[i] * k_max_j * np.abs(A_rel)) + 1e-30))
        dh = alpha_RT * np.abs(A_rel) * g_eff_t[i] * t_s[i] * (t_s[i] - t_s[i-1])
        # Viscous suppression factor
        visc_factor = np.exp(-nu_t_j[i] * k_max_j**2 * (t_s[i] - t_s[i-1]))
        h_j[i] = h_j[i-1] + dh * visc_factor
        h_j[i] = min(h_j[i], R_contact)

    ax.loglog(t_ms, h_j / 1e5, '-', color=colors_eta[j], lw=2.0,
              label=rf'$\eta = 10^{{{int(np.log10(eta_val))}}}$ g/cm/s')

# System size
ax.axhline(y=R_contact / 1e5, color='gray', ls='--', lw=1.2, alpha=0.5)
ax.text(0.15, R_contact / 1e5 * 1.1, r'$R_{\rm contact}$', fontsize=10, color='gray')

ax.set_xlabel(r'Time post-merger $t$ [ms]')
ax.set_ylabel(r'Mixing length $h_{\rm mix}$ [km]')
ax.set_title(r'(a) RT mixing length vs time (BDNK viscosity)')
ax.legend(fontsize=9, loc='lower right', frameon=True, edgecolor='0.7')
ax.set_xlim(t_ms[0], t_ms[-1])
ax.set_ylim(1e-5, 50)
ax.grid(True, ls=':', alpha=0.3, which='both')

# Panel (b): Fastest-growing wavelength vs time
ax = axes[0, 1]

for j, eta_val in enumerate(eta_range):
    eta_t_j = eta_val * (rho_t / rho_0)**0.5
    nu_t_j = eta_t_j / (w_t / c_cgs**2)
    k_max_j = (g_eff_t * np.abs(A_rel) / (3.0 * nu_t_j**2 + 1e-30))**(1.0/3.0)
    lam_j = 2.0 * pi / k_max_j / 1e5  # km

    ax.loglog(t_ms, lam_j, '-', color=colors_eta[j], lw=2.0,
              label=rf'$\eta = 10^{{{int(np.log10(eta_val))}}}$')

# Viscous cutoff scale
ax.loglog(t_ms, l_visc_km, 'k:', lw=1.5, alpha=0.6, label=r'$\ell_{\rm visc}$ (fiducial)')

ax.set_xlabel(r'Time post-merger $t$ [ms]')
ax.set_ylabel(r'Fastest-growing wavelength $\lambda_{\rm max}$ [km]')
ax.set_title(r'(b) Fastest-growing wavelength')
ax.legend(fontsize=9, loc='upper left', frameon=True, edgecolor='0.7')
ax.set_xlim(t_ms[0], t_ms[-1])
ax.grid(True, ls=':', alpha=0.3, which='both')
ax.text(0.95, 0.05, r'Radice \& Bernuzzi (2018)', fontsize=9,
        transform=ax.transAxes, ha='right',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

# Panel (c): Growth rate sigma(k) at t=1 ms for different eta
ax = axes[1, 0]

k_plot = np.logspace(-8, -2, 1000)
t_snap = 1e-3  # 1 ms

for j, eta_val in enumerate(eta_range):
    w_snap = rho_0 * c_cgs**2 * (1.0 + xi)
    nu_snap = eta_val / (w_snap / c_cgs**2)

    # Viscous RT dispersion: sigma = (-nu k^2 + sqrt(nu^2 k^4 + 4gAk)) / 2
    discriminant = nu_snap**2 * k_plot**4 + 4.0 * g_eff_0 * np.abs(A_rel) * k_plot
    sigma_visc = (-nu_snap * k_plot**2 + np.sqrt(discriminant)) / 2.0
    sigma_visc = np.maximum(sigma_visc, 0)

    ax.loglog(k_plot, sigma_visc * 1e-3, '-', color=colors_eta[j], lw=2.0,
              label=rf'$\eta = 10^{{{int(np.log10(eta_val))}}}$')

# Inviscid reference
sigma_inv = np.sqrt(g_eff_0 * k_plot * np.abs(A_rel))
ax.loglog(k_plot, sigma_inv * 1e-3, 'k--', lw=1.5, alpha=0.5, label='Inviscid')

ax.set_xlabel(r'Wavenumber $k$ [cm$^{-1}$]')
ax.set_ylabel(r'Growth rate $\sigma$ [ms$^{-1}$]')
ax.set_title(r'(c) Viscous RT dispersion at $t = 1$ ms')
ax.legend(fontsize=9, loc='lower right', frameon=True, edgecolor='0.7')
ax.set_xlim(k_plot[0], k_plot[-1])
ax.grid(True, ls=':', alpha=0.3, which='both')

# Panel (d): BDNK vs Israel-Stewart comparison for mixing
ax = axes[1, 1]

# At a fixed k, compare growth rate in BDNK vs IS
k_fixed = 1e-5  # representative wavenumber
sigma_range = np.logspace(-2, 5, 500)

# BDNK: sigma^2 + nu k^2 sigma - g A k = 0
# IS: sigma^2 + nu_eff k^2 sigma - g A k = 0
#     where nu_eff = nu / (1 + tau_pi * sigma)

tau_pi_values = [0.0, 1e-5, 1e-4, 1e-3]  # s (relaxation times)
colors_tau = ['#4CAF50', '#2196F3', '#FF9800', '#F44336']

k_sweep = np.logspace(-8, -2, 500)
eta_comp = 1e17  # comparison viscosity
nu_comp = eta_comp / w_cgs

for j, tau_pi in enumerate(tau_pi_values):
    sigma_is = np.zeros_like(k_sweep)
    for ik, kk in enumerate(k_sweep):
        # Solve IS dispersion iteratively
        # sigma^2 + (nu/(1+tau_pi*sigma)) * k^2 * sigma - g*A*k = 0
        s = np.sqrt(g_eff_0 * kk * np.abs(A_rel))  # start from inviscid
        for _ in range(100):
            if tau_pi > 0:
                nu_eff = nu_comp / (1.0 + tau_pi * np.abs(s))
            else:
                nu_eff = nu_comp
            disc = nu_eff**2 * kk**4 + 4.0 * g_eff_0 * np.abs(A_rel) * kk
            s_new = (-nu_eff * kk**2 + np.sqrt(disc)) / 2.0
            if abs(s_new - s) / (abs(s) + 1e-30) < 1e-8:
                break
            s = s_new
        sigma_is[ik] = max(s, 0)

    label = 'BDNK (no $\\tau_\\pi$)' if tau_pi == 0 else rf'IS: $\tau_\pi = 10^{{{int(np.log10(tau_pi))}}}$ s'
    ls = '-' if tau_pi == 0 else '--'
    ax.loglog(k_sweep, sigma_is * 1e-3, ls, color=colors_tau[j], lw=2.0, label=label)

ax.set_xlabel(r'Wavenumber $k$ [cm$^{-1}$]')
ax.set_ylabel(r'Growth rate $\sigma$ [ms$^{-1}$]')
ax.set_title(r'(d) BDNK vs Israel--Stewart ($\eta = 10^{17}$)')
ax.legend(fontsize=9, loc='lower right', frameon=True, edgecolor='0.7')
ax.set_xlim(k_sweep[0], k_sweep[-1])
ax.grid(True, ls=':', alpha=0.3, which='both')
ax.text(0.03, 0.95, 'BDNK has no relaxation\nartifacts at high $k$',
        transform=ax.transAxes, fontsize=9, va='top',
        bbox=dict(boxstyle='round', facecolor='lightcyan', alpha=0.7))

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_ns_merger_mixing.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_ns_merger_mixing.png')
print("Saved fig_ns_merger_mixing.pdf/png")
plt.close(fig)
