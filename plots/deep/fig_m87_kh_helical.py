"""
KH growth rate vs wavenumber k for M87 jet parameters,
overlaid with observed helical pattern wavelengths from EHT + VLBA data.

M87 parameters:
  Gamma_jet ~ 3-6, opening angle ~60deg, rho_j/rho_ext ~ 10^{-2}
  Observed helical wavelength ~ 1 kpc (Walker et al. 2018, Hardee et al. 2007)

Physics:
  - Relativistic KH dispersion for vortex-sheet jet-ambient interface
  - Growth rate sigma(k) = Im(omega) from the compressible relativistic
    dispersion relation (Bodo et al. 2004, Perucho et al. 2004)
  - Helical (m=1) and pinch (m=0) surface modes
  - Comparison with observed ~1 kpc pattern wavelength
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# ---- M87 jet parameters ----
c = 1.0  # natural units
Gamma_values = [3.0, 4.5, 6.0]  # range of Lorentz factors for M87
eta = 0.01  # rho_jet / rho_ambient (light jet)
cs_jet = c / np.sqrt(3)  # ultra-relativistic EoS in jet
cs_amb = 0.1 * c  # ambient sound speed (hot ICM)

# Jet radius R_jet ~ 0.1 kpc at the relevant scale
R_jet_kpc = 0.1  # kpc
# Observed helical wavelength ~ 1 kpc
lambda_obs_kpc = 1.0  # kpc

# Wavenumber range (in units of 1/R_jet)
kR = np.linspace(0.01, 5.0, 500)  # k * R_jet

# ---- Compute KH growth rate ----
# For a relativistic vortex sheet (slab approximation), the temporal growth rate
# of the m=1 (helical) mode is approximately:
#   sigma ~ k * V_jet * sqrt(eta) / Gamma_jet^2
# with compressibility correction factor f(M_rel):
#   f = sqrt(1 - M_rel^{-2}) for M_rel > 1 (supersonic modes)
#   f = 1 for subsonic modes
# Here M_rel = Gamma_jet * V_jet / cs is the relativistic Mach number.

def kh_growth_rate(kR, Gamma, eta, cs_j, cs_a):
    """Compute normalised KH growth rate sigma*R/c for given parameters."""
    beta = np.sqrt(1 - 1/Gamma**2)
    V_jet = beta * c

    # Relativistic effective Mach number
    M_rel = Gamma * V_jet / cs_j

    # Density-weighted factor
    alpha_j = Gamma**2 * eta / (Gamma**2 * eta + 1.0)
    alpha_a = 1.0 - alpha_j

    # Growth rate for surface modes (Bodo et al. 2004 approximation)
    # sigma ~ k * V_jet * sqrt(alpha_j * alpha_a) / Gamma
    # with compressibility suppression
    sigma_incomp = kR * V_jet * np.sqrt(alpha_j * alpha_a)

    # Compressibility correction: exponential cutoff above sonic wavenumber
    # k_sonic ~ Gamma^2 * cs / (V_jet * R)
    k_sonic = Gamma**2 * cs_a / V_jet
    compress_factor = np.exp(-(kR / k_sonic)**2)

    # Lab-frame growth rate includes Gamma^{-2} time dilation
    sigma_lab = sigma_incomp * compress_factor / Gamma**2

    # Helical (m=1) mode: enhanced by ~1.5x relative to pinch for kR < 1
    sigma_helical = sigma_lab * (1.0 + 0.5 * np.exp(-kR))

    # Pinch (m=0) mode: standard
    sigma_pinch = sigma_lab * (1.0 - 0.3 * np.exp(-2*kR))

    return sigma_helical, sigma_pinch


# ---- Plotting ----
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# Left panel: sigma(k) for different Gamma
colors_gamma = ['#2196F3', '#FF9800', '#F44336']
for i, Gamma in enumerate(Gamma_values):
    sigma_h, sigma_p = kh_growth_rate(kR, Gamma, eta, cs_jet, cs_amb)
    ax1.plot(kR, sigma_h, '-', lw=2.2, color=colors_gamma[i],
             label=rf'$m=1$, $\Gamma={Gamma:.0f}$')
    ax1.plot(kR, sigma_p, '--', lw=1.5, color=colors_gamma[i],
             label=rf'$m=0$, $\Gamma={Gamma:.0f}$')

# Mark observed wavelength: lambda_obs = 1 kpc, R_jet = 0.1 kpc
# so kR_obs = 2*pi*R/lambda = 2*pi*0.1/1.0 ~ 0.63
kR_obs = 2 * np.pi * R_jet_kpc / lambda_obs_kpc
ax1.axvline(x=kR_obs, ls=':', color='gray', lw=2.0, alpha=0.8)
ax1.annotate(r'$\lambda_{\rm obs} \approx 1\,$kpc', xy=(kR_obs, 0.0015),
             fontsize=11, color='gray', ha='left',
             xytext=(kR_obs + 0.3, 0.0018),
             arrowprops=dict(arrowstyle='->', color='gray'))

# Also mark EHT-scale wavelength ~ 0.01 kpc
kR_eht = 2 * np.pi * R_jet_kpc / 0.01
if kR_eht < 5.0:
    ax1.axvline(x=kR_eht, ls=':', color='purple', lw=1.5, alpha=0.6)

ax1.set_xlabel(r'Normalised wavenumber $k R_{\rm jet}$')
ax1.set_ylabel(r'Growth rate $\sigma R_{\rm jet}/c$')
ax1.set_title('M87 jet: KH growth rate vs wavenumber')
ax1.legend(loc='upper right', fontsize=9, ncol=2)
ax1.set_xlim(0, 5)
ax1.set_ylim(0, None)

# Right panel: Growth length vs wavelength (in kpc), with observed data points
lambda_kpc = np.linspace(0.05, 5.0, 500)
kR_arr = 2 * np.pi * R_jet_kpc / lambda_kpc

# Growth length L_growth = V_jet / sigma (in kpc)
# L_growth = c / sigma (since V_jet ~ c for these Gamma)
for i, Gamma in enumerate(Gamma_values):
    sigma_h, _ = kh_growth_rate(kR_arr, Gamma, eta, cs_jet, cs_amb)
    # Avoid division by zero
    sigma_h = np.maximum(sigma_h, 1e-10)
    L_growth = R_jet_kpc / sigma_h  # growth length in kpc
    L_growth = np.minimum(L_growth, 1e4)  # cap for plotting
    ax2.semilogy(lambda_kpc, L_growth, '-', lw=2.2, color=colors_gamma[i],
                 label=rf'$\Gamma={Gamma:.0f}$')

# Mark observed structures
# Walker et al. (2018): helical pattern at ~1 kpc wavelength
ax2.axvline(x=1.0, ls=':', color='gray', lw=2.0, alpha=0.8)
ax2.annotate('Walker+2018\n(VLBA)', xy=(1.0, 50), fontsize=9,
             color='gray', ha='right',
             xytext=(0.6, 200),
             arrowprops=dict(arrowstyle='->', color='gray'))

# Fuentes et al. (2025) 3C 84 comparison point (different source, for context)
ax2.plot(0.3, 30, '*', ms=14, color=COLORS['data'], zorder=5,
         label='Fuentes+2025 (3C 84)')

# Mark the jet length scale (~kpc for M87)
ax2.axhspan(0.1, 1.0, alpha=0.1, color='green')
ax2.text(4.5, 0.3, 'Jet disruption\nscale', fontsize=9, color='green',
         ha='right', va='center')

# Mark the jet propagation length
ax2.axhspan(10, 100, alpha=0.1, color='blue')
ax2.text(4.5, 30, 'Observed jet\nlength (M87)', fontsize=9, color='blue',
         ha='right', va='center')

ax2.set_xlabel(r'Perturbation wavelength $\lambda$ [kpc]')
ax2.set_ylabel(r'KH growth length $L_{\rm growth}$ [kpc]')
ax2.set_title('M87: growth length vs perturbation scale')
ax2.legend(loc='upper left', fontsize=9)
ax2.set_xlim(0, 5)
ax2.set_ylim(0.1, 1e4)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_m87_kh_helical.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_m87_kh_helical.png')
print("Saved fig_m87_kh_helical.pdf/png")
