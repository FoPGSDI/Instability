"""
Deep Research 6: RT instability growth rate sigma(k) for core-collapse supernovae
with nuclear equation of state.

Model: shock at r=200 km, rho_post/rho_pre = 7 (strong shock), g_eff = GM/r^2
Compute relativistic Atwood number A_rel for nuclear matter EOS.
Growth timescale vs convective overturn timescale.

References:
  - Duffell, ApJS 197 (2011) 15
  - Matsumoto et al., ApJ 914 (2021) 131
  - Couch & Ott (2015), Mueller+ (2012)
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, G_cgs, M_sun, pi
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# ============================================================
# Physical parameters for CCSN
# ============================================================
R_shock = 2.0e7       # cm (200 km)
M_PNS = 1.4 * M_sun   # proto-neutron star mass
g_eff = G_cgs * M_PNS / R_shock**2  # ~ 6.6e11 cm/s^2

# Nuclear EOS parameters
# Pre-shock (infalling Si/O): cold, non-relativistic
rho_pre = 1e9          # g/cm^3 (pre-shock density)
T_pre = 1e9            # K (~ 0.1 MeV)
xi_pre = 0.001         # p/(rho c^2) -- essentially zero

# Post-shock: hot nuclear matter, density compression ratio ~7
rho_post = 7.0 * rho_pre  # strong shock compression
T_post = 8e10          # K (~ 7 MeV)

# Nuclear matter EOS: p = p_deg + p_thermal
# For hot nuclear matter at these densities:
# xi = p/(rho c^2) depends on temperature
# At T ~ 5-10 MeV, xi ~ 0.02-0.15 for nuclear matter
xi_values_nuc = [0.0, 0.02, 0.05, 0.10, 0.15]

# Convective overturn timescale: tau_conv ~ R_gain / v_conv
# v_conv ~ (g_eff * R_gain * A)^{1/3} for turbulent convection
R_gain = 1.5e7  # gain radius ~ 150 km
v_conv = 1e8    # ~ 1000 km/s typical convective velocity
tau_conv = R_gain / v_conv  # ~ 0.15 s

# ============================================================
# Wavenumber range
# ============================================================
# l_min ~ 1 (fundamental), l_max ~ 100 (small scale)
l_modes = np.arange(1, 101)
k_from_l = l_modes / R_shock  # k ~ l/R
k = np.logspace(-8, -4, 1000)  # cm^{-1}

# ============================================================
# Figure: 2x2 layout
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 11))

# ------------------------------------------------------------
# Panel (a): sigma(k) for CCSN with nuclear EOS
# ------------------------------------------------------------
ax = axes[0, 0]

density_ratio = rho_post / rho_pre  # = 7

for i, xi in enumerate(xi_values_nuc):
    # Enthalpy densities (w = rho(1 + xi) in units where c=1 effectively)
    w_post = rho_post * c_cgs**2 * (1.0 + xi)   # erg/cm^3
    w_pre = rho_pre * c_cgs**2 * (1.0 + xi_pre)  # erg/cm^3

    # Relativistic Atwood number
    A_rel = (w_post - w_pre) / (w_post + w_pre)

    # Inviscid RT growth rate: sigma = sqrt(g * k * A_rel)
    sigma = np.sqrt(g_eff * k * np.abs(A_rel))

    # Convert to 1/ms
    sigma_ms = sigma * 1e-3

    colors = ['#2196F3', '#26A69A', '#4CAF50', '#FF9800', '#F44336']
    ls_list = ['-', '--', '-.', ':', (0, (3, 1, 1, 1))]
    label = 'Classical' if xi == 0.0 else rf'$\xi = {xi}$ (nuclear)'
    ax.loglog(k, sigma_ms, ls=ls_list[i], color=colors[i], lw=2.0, label=label)

# Mark convective overturn timescale
sigma_conv = 1.0 / tau_conv * 1e-3
ax.axhline(y=sigma_conv, color='gray', ls='--', lw=1.2, alpha=0.6)
ax.text(k[10], sigma_conv * 1.3, r'$\tau_{\rm conv}^{-1}$',
        fontsize=10, color='gray')

# Mark l=1 and l=10 modes
k_l1 = 1.0 / R_shock
k_l10 = 10.0 / R_shock
ax.axvline(x=k_l1, color='purple', ls=':', lw=1, alpha=0.5)
ax.axvline(x=k_l10, color='purple', ls=':', lw=1, alpha=0.5)
ax.text(k_l1 * 1.2, 0.2, '$\\ell=1$', fontsize=9, color='purple')
ax.text(k_l10 * 1.2, 0.2, '$\\ell=10$', fontsize=9, color='purple')

ax.set_xlabel(r'Wavenumber $k$ [cm$^{-1}$]')
ax.set_ylabel(r'Growth rate $\sigma$ [ms$^{-1}$]')
ax.set_title(r'(a) RT growth rate $\sigma(k)$ in CCSN')
ax.legend(fontsize=9, loc='lower right', frameon=True, edgecolor='0.7')
ax.set_xlim(k[0], k[-1])
ax.grid(True, ls=':', alpha=0.3, which='both')
ax.text(0.03, 0.95, r'$R_{\rm shock} = 200\,\mathrm{km}$, $\rho_2/\rho_1 = 7$',
        transform=ax.transAxes, fontsize=9, va='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# ------------------------------------------------------------
# Panel (b): Relativistic Atwood number vs xi for nuclear EOS
# ------------------------------------------------------------
ax = axes[0, 1]

xi_range = np.linspace(0.0, 0.25, 500)
compression_ratios = [3.0, 5.0, 7.0, 10.0]
colors_cr = ['#2196F3', '#4CAF50', '#FF9800', '#F44336']

for i, cr in enumerate(compression_ratios):
    # A_class = (cr - 1) / (cr + 1)
    A_class = (cr - 1.0) / (cr + 1.0)

    # A_rel(xi): post-shock has xi, pre-shock has xi_pre ~ 0
    w2 = cr * (1.0 + xi_range)
    w1 = 1.0 * (1.0 + xi_pre)
    A_rel = (w2 - w1) / (w2 + w1)

    # Fractional change
    delta_A = (A_rel - A_class) / A_class * 100

    ax.plot(xi_range, A_rel, '-', color=colors_cr[i], lw=2.0,
            label=rf'$\rho_2/\rho_1 = {cr:.0f}$')
    # Classical limit as horizontal dashed
    ax.axhline(y=A_class, color=colors_cr[i], ls='--', lw=0.8, alpha=0.4)

# Shade typical CCSN range
ax.axvspan(0.02, 0.15, alpha=0.08, color='orange')
ax.text(0.085, 0.45, 'CCSN\npost-shock', fontsize=9, ha='center',
        color='darkorange', style='italic')

ax.set_xlabel(r'Relativistic parameter $\xi = p/(\rho c^2)$')
ax.set_ylabel(r'Atwood number $\mathcal{A}_{\rm rel}$')
ax.set_title(r'(b) Relativistic Atwood number (nuclear EOS)')
ax.legend(fontsize=9, loc='lower right', frameon=True, edgecolor='0.7')
ax.set_xlim(0, 0.25)
ax.set_ylim(0.3, 1.0)
ax.grid(True, ls=':', alpha=0.3)

# ------------------------------------------------------------
# Panel (c): Growth timescale vs convective overturn timescale
# ------------------------------------------------------------
ax = axes[1, 0]

l_modes_plot = np.arange(1, 51)
k_modes = l_modes_plot / R_shock

# Growth timescale for different xi
for i, xi in enumerate([0.0, 0.05, 0.10, 0.15]):
    w_post = rho_post * (1.0 + xi)
    w_pre = rho_pre * (1.0 + xi_pre)
    A_rel = (w_post - w_pre) / (w_post + w_pre)

    sigma_modes = np.sqrt(g_eff * k_modes * np.abs(A_rel))
    tau_growth = 1.0 / sigma_modes  # seconds

    colors = ['#2196F3', '#4CAF50', '#FF9800', '#F44336']
    ls_list = ['-', '--', '-.', ':']
    label = 'Classical' if xi == 0.0 else rf'$\xi = {xi}$'
    ax.semilogy(l_modes_plot, tau_growth * 1e3, ls=ls_list[i],
                color=colors[i], lw=2.0, label=label)

# Convective overturn timescale
ax.axhline(y=tau_conv * 1e3, color='gray', ls='--', lw=1.5, alpha=0.6)
ax.text(40, tau_conv * 1e3 * 1.3, r'$\tau_{\rm conv}$',
        fontsize=10, color='gray')

# Advection timescale through gain region
tau_adv = R_gain / 1e9  # ~ 15 ms (freefall through gain region)
ax.axhline(y=tau_adv * 1e3, color='red', ls=':', lw=1.2, alpha=0.5)
ax.text(40, tau_adv * 1e3 * 1.3, r'$\tau_{\rm adv}$',
        fontsize=10, color='red')

ax.set_xlabel(r'Spherical harmonic order $\ell$')
ax.set_ylabel(r'Growth timescale $\tau_{\rm growth}$ [ms]')
ax.set_title(r'(c) Growth vs overturn timescale')
ax.legend(fontsize=9, loc='upper right', frameon=True, edgecolor='0.7')
ax.set_xlim(1, 50)
ax.set_ylim(0.1, 1e3)
ax.grid(True, ls=':', alpha=0.3, which='both')

# Shade where RT grows faster than convection turns over
ax.fill_between(l_modes_plot, 0.1, tau_conv * 1e3,
                alpha=0.05, color='green')
ax.text(25, 5, 'RT dominates', fontsize=9, color='green', ha='center')

# ------------------------------------------------------------
# Panel (d): sigma(k) comparison: Duffell vs analytic
# ------------------------------------------------------------
ax = axes[1, 1]

# Compare the analytic RT growth rate with compressibility corrections
# Duffell (2011) moving-mesh method captures the nonlinear RT
# Compressible correction: sigma_comp = sigma_inc * (1 - k^2 cs^2 / (g * A * k + ...))

# Sound speed in post-shock nuclear matter
# cs^2 ~ Gamma * p / rho where Gamma ~ 4/3 for radiation-dominated
Gamma_eos = 4.0 / 3.0
xi_ccsn = 0.10
cs2 = Gamma_eos * xi_ccsn * c_cgs**2  # ~ 0.13 c^2
cs = np.sqrt(cs2)

# Enthalpy-based quantities
w_post = rho_post * (1.0 + xi_ccsn)
w_pre = rho_pre * (1.0 + xi_pre)
A_rel = (w_post - w_pre) / (w_post + w_pre)

# Incompressible RT growth rate
sigma_inc = np.sqrt(g_eff * k * np.abs(A_rel))

# Compressible correction (Duffell 2011 approach):
# At high k, compressibility suppresses growth when k > k_J ~ g*A/cs^2
k_J = g_eff * np.abs(A_rel) / cs2
sigma_comp = sigma_inc * np.sqrt(1.0 / (1.0 + (k / k_J)**2))

# Matsumoto et al. (2021) Richtmyer-Meshkov + RT coupling
# Additional impulsive growth from shock passage
# sigma_RM ~ A_rel * Delta_v * k where Delta_v ~ post-shock velocity jump
Delta_v = 1e9  # cm/s (shock velocity jump)
sigma_RM = np.abs(A_rel) * Delta_v * k  # RM growth rate (linear in k)

# Combined RT + RM
sigma_combined = np.sqrt(sigma_inc**2 + sigma_RM**2)

ax.loglog(k, sigma_inc * 1e-3, '-', color=COLORS['classical'], lw=2.0,
          label='Incompressible RT (analytic)')
ax.loglog(k, sigma_comp * 1e-3, '--', color=COLORS['relativistic'], lw=2.0,
          label='Compressible RT (Duffell 2011)')
ax.loglog(k, sigma_RM * 1e-3, ':', color=COLORS['bdnk'], lw=1.8,
          label='Richtmyer--Meshkov (Matsumoto+ 2021)')
ax.loglog(k, sigma_combined * 1e-3, '-', color=COLORS['jet'], lw=2.0,
          alpha=0.7, label='Combined RT + RM')

# Mark Jeans-like scale
ax.axvline(x=k_J, color='gray', ls='--', lw=1, alpha=0.5)
ax.text(k_J * 0.5, 100, r'$k_J$', fontsize=10, color='gray')

ax.set_xlabel(r'Wavenumber $k$ [cm$^{-1}$]')
ax.set_ylabel(r'Growth rate $\sigma$ [ms$^{-1}$]')
ax.set_title(r'(d) Compressible + RM corrections ($\xi = 0.10$)')
ax.legend(fontsize=9, loc='lower right', frameon=True, edgecolor='0.7')
ax.set_xlim(k[0], k[-1])
ax.grid(True, ls=':', alpha=0.3, which='both')

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_ccsn_RT_growth.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_ccsn_RT_growth.png')
print("Saved fig_ccsn_RT_growth.pdf/png")
plt.close(fig)
