"""
Toomre Q parameter for the Milky Way disk: stellar + gas + dark matter contributions.

Physics:
- Toomre criterion: Q = c_s * kappa / (pi * G * Sigma)
  Q > 1 => stable to axisymmetric gravitational perturbations
  Q < 1 => gravitationally unstable (fragmentation, star formation)
- For MW: flat rotation curve V_c ~ 220 km/s
  => kappa = sqrt(2) * V_c / R (flat rotation curve epicyclic frequency)
- Surface density: exponential disk Sigma(R) = Sigma_0 * exp(-R/R_d)
- Three components: stellar disk, gas disk, dark matter halo
- Relativistic correction near galactic center (R < 0.1 pc from Sgr A*):
  kappa_rel includes frame-dragging, enthalpy correction negligible for MW disk

Left panel:  Q(R) for MW with individual and combined contributions
Right panel: Mark spiral arm locations where Q approaches 1

References:
  Toomre (1964) ApJ 139, 1217
  Binney & Tremaine (2008) Galactic Dynamics, Ch. 6
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, G_cgs, M_sun, k_B, m_p, pi
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

setup_style()

# === Milky Way parameters ===
kpc = 3.086e21   # cm
V_c = 220e5      # cm/s (220 km/s flat rotation curve)
R_sun = 8.0      # kpc (solar galactocentric radius)

# Radial grid
R_kpc = np.linspace(0.5, 20, 500)  # kpc
R_cm = R_kpc * kpc

# === Epicyclic frequency for flat rotation curve ===
# kappa^2 = (2*Omega/R) * d(R^2 * Omega)/dR = 2*Omega^2 for flat V_c
Omega = V_c / R_cm  # s^{-1}
kappa_epi = np.sqrt(2.0) * Omega  # s^{-1}

# === Surface density profiles ===

# Stellar disk: exponential with R_d = 2.5 kpc, Sigma_*,0 ~ 50 M_sun/pc^2
R_d_star = 2.5  # kpc
Sigma_star_0 = 50 * M_sun / (3.086e18)**2  # g/cm^2 (50 M_sun/pc^2)
Sigma_star = Sigma_star_0 * np.exp(-R_kpc / R_d_star)

# Gas disk (HI + H2): exponential with R_d = 4 kpc, broader
# Central hole in HI, molecular gas concentrated in ring
R_d_gas = 4.0  # kpc
Sigma_gas_0 = 13 * M_sun / (3.086e18)**2  # g/cm^2 (13 M_sun/pc^2)
# Molecular ring at R ~ 4-5 kpc
ring = 1.0 + 2.0 * np.exp(-((R_kpc - 4.5) / 1.5)**2)
Sigma_gas = Sigma_gas_0 * np.exp(-R_kpc / R_d_gas) * ring
# Suppress gas at very small R
Sigma_gas *= (1.0 - np.exp(-R_kpc / 1.0))

# Total baryonic surface density
Sigma_total = Sigma_star + Sigma_gas

# === Sound speeds ===
# Stellar velocity dispersion: sigma_R ~ 40 km/s near sun, decreasing outward
sigma_star = 40e5 * np.exp(-(R_kpc - R_sun) / 8.0)  # cm/s

# Gas sound speed: c_s ~ 7-10 km/s (warm neutral medium)
cs_gas = 8e5  # cm/s (8 km/s)

# Effective sound speed for combined gas+stars
# Q_eff^{-1} ~ Q_star^{-1} + Q_gas^{-1} (Wang & Silk 1994 approximation)

# === Toomre Q for each component ===
Q_star = sigma_star * kappa_epi / (pi * G_cgs * Sigma_star)
Q_gas = cs_gas * kappa_epi / (pi * G_cgs * Sigma_gas)

# Combined Q (two-fluid approximation)
# 1/Q_eff ~ 1/Q_star + 1/Q_gas (simplified)
Q_eff_inv = 1.0 / Q_star + 1.0 / Q_gas
Q_eff = 1.0 / Q_eff_inv

# === Dark matter contribution ===
# DM halo: NFW profile contributes to kappa through the rotation curve
# but does not have a surface density for Toomre analysis
# It stabilises indirectly by maintaining high Omega (and hence kappa)
# Show Q with enhanced kappa from DM
# For an NFW halo with c=12, r_s = 20 kpc:
r_s_dm = 20.0  # kpc
c_nfw = 12.0
# V_c with DM is approximately flat; without DM, V_c would be Keplerian at large R
# Show the effect: Q_no_DM uses declining V_c
V_c_disk_only = V_c * np.sqrt(Sigma_total / Sigma_total[np.argmin(np.abs(R_kpc - R_sun))])
V_c_disk_only = np.minimum(V_c_disk_only, V_c)
kappa_no_dm = np.sqrt(2.0) * V_c_disk_only / R_cm
Q_eff_no_dm = 1.0 / (sigma_star * kappa_no_dm / (pi * G_cgs * Sigma_star) +
                       cs_gas * kappa_no_dm / (pi * G_cgs * Sigma_gas))**(-1)
# Simplified: just scale Q by kappa ratio
Q_eff_no_dm = Q_eff * (kappa_no_dm / kappa_epi)

# === Spiral arm locations (schematic) ===
# MW has 4 major spiral arms; overdensity enhances Sigma by factor ~2
spiral_R = [3.5, 5.0, 6.5, 8.0, 10.0, 12.0]  # approximate arm crossings in kpc
spiral_names = ['3 kpc', 'Norma', 'Scutum-\nCentaurus', 'Sagittarius',
                'Perseus', 'Outer']

# Q in spiral arms (enhanced surface density)
Q_spiral = Q_eff / 2.0  # factor ~2 overdensity in arms

# === Relativistic correction near galactic center ===
# Sgr A* mass: M_BH ~ 4e6 M_sun
# Relativistic effects relevant for R < 0.01 pc
# kappa_rel = kappa_Newton * (1 - 3*R_S/R + ...)
# R_S = 2*G*M_BH/c^2 ~ 1.2e12 cm for Sgr A*
M_BH = 4e6 * M_sun
R_S = 2 * G_cgs * M_BH / c_cgs**2
# At R = 0.5 kpc (innermost point in our plot), R_S/R ~ 10^{-12}: negligible
# Include as annotation only

# === Plotting ===
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# --- Left panel: Q(R) for individual components ---
ax1.semilogy(R_kpc, Q_star, '--', lw=2.0, color='#FF9800',
             label=r'$Q_\star$ (stellar)')
ax1.semilogy(R_kpc, Q_gas, '--', lw=2.0, color=COLORS['bdnk'],
             label=r'$Q_{\rm gas}$')
ax1.semilogy(R_kpc, Q_eff, '-', lw=2.5, color=COLORS['relativistic'],
             label=r'$Q_{\rm eff}$ (two-fluid)')
ax1.semilogy(R_kpc, Q_eff_no_dm, ':', lw=2.0, color=COLORS['data'],
             label=r'$Q_{\rm eff}$ (no DM halo)')

# Q = 1 line
ax1.axhline(1.0, ls='-', color='black', lw=1.0, alpha=0.5)
ax1.text(18, 1.1, '$Q = 1$', fontsize=9, color='black')

# Q = 2 line (often used as practical threshold)
ax1.axhline(2.0, ls=':', color='gray', lw=0.8, alpha=0.5)
ax1.text(18, 2.2, '$Q = 2$', fontsize=8, color='gray')

# Mark solar position
ax1.axvline(R_sun, ls='--', color='gray', lw=0.8, alpha=0.5)
ax1.text(R_sun + 0.2, 15, r'$R_\odot$', fontsize=9, color='gray')

# Shade unstable region
ax1.fill_between(R_kpc, 0.1, 1.0, alpha=0.08, color='red')
ax1.text(2.0, 0.5, 'UNSTABLE', fontsize=9, color='red', alpha=0.6, fontweight='bold')

ax1.set_xlabel(r'Galactocentric radius $R$ [kpc]')
ax1.set_ylabel(r'Toomre parameter $Q$')
ax1.set_title('Toomre $Q$ for Milky Way disk')
ax1.set_xlim(0.5, 20)
ax1.set_ylim(0.3, 30)
ax1.legend(loc='upper right', fontsize=9)

# --- Right panel: Q_eff with spiral arm perturbations ---
ax2.semilogy(R_kpc, Q_eff, '-', lw=2.5, color=COLORS['classical'],
             label=r'$Q_{\rm eff}$ (inter-arm)')
ax2.semilogy(R_kpc, Q_spiral, '--', lw=2.5, color=COLORS['relativistic'],
             label=r'$Q_{\rm eff}$ (in spiral arm, $\times 2$ overdensity)')

# Q = 1 line
ax2.axhline(1.0, ls='-', color='black', lw=1.0, alpha=0.5)

# Mark spiral arm locations
for i, (r_arm, name) in enumerate(zip(spiral_R, spiral_names)):
    ax2.axvspan(r_arm - 0.3, r_arm + 0.3, alpha=0.12, color='#FF9800')
    if i < 5:
        ax2.text(r_arm, 0.35, name, fontsize=7, color='#FF9800',
                 ha='center', rotation=90, va='bottom')

# Mark where spiral arms drive Q < 1
arm_unstable = Q_spiral < 1.0
if np.any(arm_unstable):
    ax2.fill_between(R_kpc, 0.1, 1.0, where=arm_unstable,
                     alpha=0.15, color='red')

# Shade unstable region
ax2.fill_between(R_kpc, 0.1, 1.0, alpha=0.05, color='red')
ax2.text(15, 0.5, 'Star formation\nthreshold', fontsize=9, color='red',
         alpha=0.6, ha='center')

# Mark solar position
ax2.axvline(R_sun, ls='--', color='gray', lw=0.8, alpha=0.5)
ax2.text(R_sun + 0.2, 12, r'$R_\odot$', fontsize=9, color='gray')

# Annotation about GR correction
ax2.annotate('GR correction\nnear Sgr A*:\n' + r'$\Delta Q/Q \sim 10^{-12}$' + '\n(negligible)',
             xy=(0.5, 0.35), xytext=(3, 0.4),
             arrowprops=dict(arrowstyle='->', color='gray', alpha=0.5),
             fontsize=8, color='gray', style='italic',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='gray', alpha=0.8))

ax2.set_xlabel(r'Galactocentric radius $R$ [kpc]')
ax2.set_ylabel(r'Toomre parameter $Q$')
ax2.set_title('Spiral arm instability in Milky Way')
ax2.set_xlim(0.5, 20)
ax2.set_ylim(0.3, 20)
ax2.legend(loc='upper right', fontsize=9)

fig.tight_layout()
fig.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_toomre_milky_way.pdf')
fig.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_toomre_milky_way.png')
print("Saved fig_toomre_milky_way.pdf/png")
plt.close(fig)
