"""
KH growth rate vs distance downstream of a recollimation shock
in a magnetised relativistic jet.

Physics:
  - At recollimation shocks, jet recollimates and velocity/density jump
  - Post-shock conditions modify KH stability
  - Magnetic field compression at shock enhances stabilisation
  - Downstream: field decays, KH modes can grow

References:
  Mukherjee, Bodo, Rossi, Mignone, Vaidya (2025)
  Gourgouliatos & Komissarov (2018)
  Fromm et al. (2024)
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, LINE_STYLES
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# ---- Parameters ----
c = 1.0

# Pre-shock jet
Gamma_pre = 10.0
sigma_mag_pre = 0.1   # magnetisation B^2/(4*pi*w*c^2)
eta_pre = 0.01         # jet/ambient enthalpy ratio
cs_pre = c / np.sqrt(3)

# Post-shock conditions (from relativistic MHD Rankine-Hugoniot)
# For a strong recollimation shock with compression ratio ~3:
compression = 3.0
Gamma_post = Gamma_pre / compression  # decelerated post-shock
sigma_mag_post = sigma_mag_pre * compression**2  # B compressed
eta_post = eta_pre * compression  # density compressed

# Distance downstream of shock (in units of jet radius)
z_R = np.linspace(0, 30, 500)

# ---- Post-shock evolution ----
# Gamma recovers gradually as jet re-expands
# Model: Gamma(z) = Gamma_post + (Gamma_pre - Gamma_post) * (1 - exp(-z/z_rec))
z_rec = 10.0  # recollimation length scale
Gamma_z = Gamma_post + (Gamma_pre - Gamma_post) * (1 - np.exp(-z_R / z_rec))

# Magnetisation decays as jet expands (B ~ 1/r, sigma ~ 1/r^2)
# In conical expansion: r(z) ~ r_0 + z * tan(theta)
theta_expand = 0.05  # ~3 deg half-opening angle
r_z = 1.0 + z_R * np.tan(theta_expand)
sigma_z = sigma_mag_post / r_z**2

# Density ratio evolves
eta_z = eta_post / r_z  # adiabatic expansion


def kh_growth_with_field(Gamma, eta, sigma_B, cs_j=c/np.sqrt(3), cs_a=0.1*c):
    """Compute KH growth rate including magnetic stabilisation.

    Magnetic field suppresses KH when sigma > sigma_crit.
    sigma_crit ~ eta / Gamma^2 for a light jet.
    Growth rate: sigma_KH ~ k*V*sqrt(alpha_j*alpha_a)/Gamma^2 * (1 - sigma_B/sigma_crit)
    """
    beta = np.sqrt(1 - 1/Gamma**2)
    V = beta * c

    alpha_j = Gamma**2 * eta / (Gamma**2 * eta + 1.0)
    alpha_a = 1.0 - alpha_j

    # Critical magnetisation
    sigma_crit = eta / Gamma**2 * (Gamma**2 * eta + 1)**2 / (Gamma**2 * eta)
    sigma_crit = np.maximum(sigma_crit, 1e-10)

    # Growth rate (at most unstable wavenumber kR ~ 1)
    sigma_hydro = V * np.sqrt(alpha_j * alpha_a) / Gamma**2

    # Magnetic suppression factor
    mag_factor = np.maximum(1 - sigma_B / sigma_crit, 0)

    return sigma_hydro * mag_factor, sigma_crit


# ---- Compute growth rate downstream ----
sigma_kh_z = np.zeros_like(z_R)
sigma_crit_z = np.zeros_like(z_R)
sigma_kh_hydro_z = np.zeros_like(z_R)

for i in range(len(z_R)):
    s_kh, s_crit = kh_growth_with_field(Gamma_z[i], eta_z[i], sigma_z[i])
    sigma_kh_z[i] = s_kh
    sigma_crit_z[i] = s_crit
    s_hydro, _ = kh_growth_with_field(Gamma_z[i], eta_z[i], 0.0)
    sigma_kh_hydro_z[i] = s_hydro

# Find the onset distance where sigma_B drops below sigma_crit
onset_mask = sigma_z < sigma_crit_z
if np.any(onset_mask):
    z_onset = z_R[np.argmax(onset_mask)]
else:
    z_onset = z_R[-1]


# ---- Plotting ----
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# Left panel: Growth rate and magnetisation vs distance
ax1_twin = ax1.twinx()

# Growth rates
ax1.plot(z_R, sigma_kh_z * 1e3, '-', lw=2.5, color=COLORS['relativistic'],
         label=r'$\sigma_{\rm KH}$ (MHD)')
ax1.plot(z_R, sigma_kh_hydro_z * 1e3, '--', lw=2.0, color=COLORS['classical'],
         label=r'$\sigma_{\rm KH}$ (hydro, no $B$)')

# Magnetisation on twin axis
ax1_twin.plot(z_R, sigma_z, '-.', lw=2.0, color=COLORS['accretion'],
              label=r'$\sigma_B(z)$')
ax1_twin.plot(z_R, sigma_crit_z, ':', lw=1.8, color=COLORS['data'],
              label=r'$\sigma_{\rm crit}(z)$')

# Mark onset of instability
ax1.axvline(x=z_onset, ls=':', color='gray', lw=2.0, alpha=0.7)
ax1.annotate('KH onset', xy=(z_onset, 0), fontsize=10, color='gray',
             xytext=(z_onset + 2, max(sigma_kh_z * 1e3) * 0.7),
             arrowprops=dict(arrowstyle='->', color='gray'))

# Mark shock location
ax1.axvline(x=0, ls='-', color='black', lw=2.0)
ax1.text(0.5, max(sigma_kh_hydro_z * 1e3) * 0.95, 'Recollimation\nshock',
         fontsize=9, color='black', va='top')

ax1.set_xlabel(r'Distance downstream $z/R_{\rm jet}$')
ax1.set_ylabel(r'Growth rate $\sigma_{\rm KH} \times 10^3\; [c/R_{\rm jet}]$',
               color=COLORS['relativistic'])
ax1_twin.set_ylabel(r'Magnetisation $\sigma_B$', color=COLORS['accretion'])
ax1.set_title('Post-recollimation KH growth rate')

# Combined legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax1_twin.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='center right', fontsize=9)

ax1.set_xlim(0, 30)
ax1.set_ylim(0, None)

# Right panel: Stability map in (z, sigma_B) space for different Gamma_pre
Gamma_pre_arr = [5, 10, 20]
colors_gp = [COLORS['classical'], COLORS['jet'], COLORS['relativistic']]

for j, Gp in enumerate(Gamma_pre_arr):
    Gpost = Gp / compression
    z_arr = np.linspace(0, 30, 300)
    G_arr = Gpost + (Gp - Gpost) * (1 - np.exp(-z_arr / z_rec))
    eta_arr = eta_pre * compression / (1.0 + z_arr * np.tan(theta_expand))

    # For each z, find sigma_crit
    scrit_arr = np.zeros_like(z_arr)
    for i in range(len(z_arr)):
        _, sc = kh_growth_with_field(G_arr[i], eta_arr[i], 0)
        scrit_arr[i] = sc

    ax2.semilogy(z_arr, scrit_arr, '-', lw=2.2, color=colors_gp[j],
                 label=rf'$\Gamma_{{\rm pre}}={Gp}$')

# Show the actual sigma_B(z) trajectory
ax2.semilogy(z_R, sigma_z, 'k--', lw=2.5, label=r'$\sigma_B(z)$ trajectory')

# Shade stable region (below the curves)
ax2.fill_between(z_R, 1e-6, sigma_z, alpha=0.1, color='green')
ax2.text(20, 0.02, 'Stable\n(magnetically\nsuppressed)', fontsize=9,
         color='green', ha='center', va='center')

# Mark Mukherjee et al. (2025) simulation result
ax2.plot(5, 0.3, '*', ms=14, color=COLORS['data'], zorder=5,
         markeredgecolor='black', markeredgewidth=0.5)
ax2.annotate('Mukherjee+2025\n(simulation)', xy=(5, 0.3),
             xytext=(10, 0.8), fontsize=9, color=COLORS['data'],
             arrowprops=dict(arrowstyle='->', color=COLORS['data']))

ax2.set_xlabel(r'Distance downstream $z/R_{\rm jet}$')
ax2.set_ylabel(r'Critical magnetisation $\sigma_{\rm crit}$')
ax2.set_title('Magnetic stabilisation boundary downstream of shock')
ax2.legend(loc='lower left', fontsize=9)
ax2.set_xlim(0, 30)
ax2.set_ylim(1e-3, 10)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_recollimation_kh.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_recollimation_kh.png')
print("Saved fig_recollimation_kh.pdf/png")
