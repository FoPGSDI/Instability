"""
Cosmological Jeans mass evolution M_J(z) from recombination to present.

Physics:
- M_J depends on sound speed c_s and density rho (or energy density epsilon)
- Three eras with different physics:
  (1) Radiation-dominated (z > z_eq ~ 3400): p = epsilon/3, c_s = c/sqrt(3)
      Relativistic Jeans mass: M_J ~ (c_s^3 / G^{3/2}) * (c^2 / (eps+p))^{1/2}
  (2) Matter-dominated (z_eq > z > ~1): c_s drops after decoupling, matter dominates
  (3) Dark energy era (z < ~1): Lambda-CDM, expansion accelerates

At recombination (z ~ 1100): baryons decouple from photons, c_s drops dramatically
  Before: c_s ~ c/sqrt(3) (radiation)
  After: c_s ~ sqrt(k_B T / m_p) ~ 5 km/s (thermal baryon gas)

Relativistic corrections at high z: use (eps + p)(1 + 3*cs^2/c^2)/2 for gravity source.

References:
  Lifshitz (1946) JETP 16, 587
  Weinberg (1971) ApJ 168, 175
  Weinberg (1972) Gravitation and Cosmology, Ch. 15
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, G_cgs, M_sun, k_B, m_p, pi, hbar, sigma_SB
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

setup_style()

# === Cosmological parameters (Planck 2018) ===
H0 = 67.4e5 / (3.086e24)  # Hubble constant in s^{-1} (67.4 km/s/Mpc)
Omega_m = 0.315
Omega_r = 9.1e-5  # radiation (photons + neutrinos)
Omega_Lambda = 1.0 - Omega_m - Omega_r
T_CMB_0 = 2.725  # K, CMB temperature today

# Key redshifts
z_eq = Omega_m / Omega_r - 1   # matter-radiation equality ~3400
z_rec = 1100.0                  # recombination
z_dec = 1090.0                  # decoupling (photon last scattering)

# === Redshift array ===
z = np.logspace(-1, np.log10(5000), 2000)
z_sorted = np.sort(z)[::-1]  # high z to low z

# === Temperature evolution ===
T_CMB = T_CMB_0 * (1 + z)  # CMB temperature

# === Energy densities ===
# Critical density today
rho_crit_0 = 3 * H0**2 / (8 * pi * G_cgs)  # g/cm^3

# Matter density
rho_m = Omega_m * rho_crit_0 * (1 + z)**3  # g/cm^3
eps_m = rho_m * c_cgs**2  # erg/cm^3

# Radiation energy density
# eps_r = a_rad * T^4 where a_rad = 4*sigma_SB/c
a_rad = 4 * sigma_SB / c_cgs
eps_r = a_rad * T_CMB**4  # erg/cm^3
p_r = eps_r / 3.0

# Total
eps_total = eps_m + eps_r
p_total = p_r  # matter pressure negligible on cosmological scales (before decoupling)

# === Sound speed ===
# Before decoupling (z > z_dec): tightly coupled baryon-photon fluid
# c_s^2 = c^2/3 * 1/(1 + R) where R = 3*rho_b/(4*eps_r/c^2)
# rho_b = Omega_b * rho_crit_0 * (1+z)^3
Omega_b = 0.0493
rho_b = Omega_b * rho_crit_0 * (1 + z)**3
R_bp = 3 * rho_b * c_cgs**2 / (4 * eps_r)  # baryon-to-photon ratio

cs2_coupled = (c_cgs**2 / 3.0) / (1.0 + R_bp)

# After decoupling: baryon sound speed
# c_s = sqrt(5/3 * k_B T / m_p) for monatomic ideal gas
# T_gas ~ T_CMB for z > ~200 (Compton coupling), then T_gas ~ (1+z)^2
T_gas = np.where(z > 200, T_CMB, T_CMB_0 * (1 + 200) * ((1 + z) / (1 + 200))**2)
cs2_baryon = (5.0/3.0) * k_B * T_gas / m_p

# Smooth transition at decoupling
sigma_dec = 50.0  # width of transition in z
transition = 1.0 / (1.0 + np.exp(-(z - z_dec) / sigma_dec))
cs2 = cs2_coupled * transition + cs2_baryon * (1.0 - transition)

cs = np.sqrt(cs2)

# === Jeans mass ===
# Classical (Newtonian): M_J = (pi/6) * rho * lambda_J^3
# lambda_J = c_s * sqrt(pi / (G * rho))
# M_J = (pi^{5/2} / 6) * c_s^3 / (G^{3/2} * rho^{1/2})

# Use total matter density for gravitating mass
rho_grav = rho_m + eps_r / c_cgs**2  # total gravitating density

# Newtonian Jeans mass
M_J_newton = (pi**(5.0/2.0) / 6.0) * cs**3 / (G_cgs**1.5 * rho_grav**0.5)

# Relativistic Jeans mass:
# From sec119: gravity source is (eps + p)(1 + 3*cs^2/c^2)/2
# Enthalpy density: w = (eps + p)/c^2
w = (eps_total + p_total) / c_cgs**2  # g/cm^3
A_factor = (1.0 + 3.0 * cs2 / c_cgs**2) / 2.0

# Relativistic Jeans wavenumber:
# k_J_rel^2 = 4*pi*G * w * A / cs^2
k_J_rel2 = 4 * pi * G_cgs * w * A_factor / cs2

# Relativistic Jeans mass
lambda_J_rel = 2 * pi / np.sqrt(k_J_rel2)
M_J_rel = (4 * pi / 3.0) * w * (lambda_J_rel / 2.0)**3

# === Plotting ===
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# --- Left panel: M_J(z) ---
ax1.loglog(1 + z, M_J_newton / M_sun, '-', lw=2.5, color=COLORS['classical'],
           label='Newtonian $M_J$')
ax1.loglog(1 + z, M_J_rel / M_sun, '-', lw=2.5, color=COLORS['relativistic'],
           label='Relativistic $M_J$')

# Mark key epochs
for z_mark, label, color in [(z_eq, '$z_{\\rm eq}$', '#9C27B0'),
                               (z_rec, '$z_{\\rm rec}$', '#E91E63'),
                               (z_dec, '$z_{\\rm dec}$', '#FF5722')]:
    ax1.axvline(1 + z_mark, ls='--', color=color, lw=1.0, alpha=0.6)
    ax1.text(1 + z_mark, 1e20, label, fontsize=9, color=color,
             rotation=90, va='bottom', ha='right')

# Shade eras
ax1.axvspan(1 + z_eq, 6000, alpha=0.05, color='#FF9800')
ax1.text(4000, 3e5, 'Radiation\ndominated', fontsize=8, color='#FF9800',
         ha='center', fontweight='bold')

ax1.axvspan(2, 1 + z_eq, alpha=0.05, color='#2196F3')
ax1.text(50, 3e5, 'Matter\ndominated', fontsize=8, color='#2196F3',
         ha='center', fontweight='bold')

ax1.axvspan(1, 2, alpha=0.05, color='#4CAF50')
ax1.text(1.3, 3e5, r'$\Lambda$', fontsize=8, color='#4CAF50',
         ha='center', fontweight='bold')

# Mark characteristic masses
ax1.axhline(1e12, ls=':', color='gray', lw=0.8, alpha=0.5)
ax1.text(1.2, 1.5e12, r'$10^{12}\,M_\odot$ (galaxy cluster)', fontsize=8, color='gray')

ax1.axhline(1e6, ls=':', color='gray', lw=0.8, alpha=0.5)
ax1.text(1.2, 1.5e6, r'$10^{6}\,M_\odot$ (dwarf galaxy)', fontsize=8, color='gray')

ax1.set_xlabel(r'$1 + z$')
ax1.set_ylabel(r'Jeans mass $M_J / M_\odot$')
ax1.set_title('Cosmological Jeans mass evolution')
ax1.set_xlim(1, 6000)
ax1.set_ylim(1e3, 1e20)
ax1.legend(loc='upper left', fontsize=10)
ax1.invert_xaxis()

# --- Right panel: Ratio M_J_rel / M_J_newton and c_s/c ---
ax2_twin = ax2.twinx()

ratio = M_J_rel / M_J_newton
ax2.semilogx(1 + z, ratio, '-', lw=2.5, color=COLORS['relativistic'],
             label=r'$M_{J,\rm rel} / M_{J,\rm Newton}$')
ax2.axhline(1.0, ls=':', color='gray', lw=1.0, alpha=0.5)

# Sound speed ratio on twin axis
cs_over_c = cs / c_cgs
ax2_twin.loglog(1 + z, cs_over_c, '--', lw=2.0, color=COLORS['bdnk'],
                label=r'$c_s / c$')
ax2_twin.axhline(1.0 / np.sqrt(3), ls=':', color=COLORS['bdnk'], lw=0.8, alpha=0.5)
ax2_twin.text(4000, 0.65, r'$c/\sqrt{3}$', fontsize=8, color=COLORS['bdnk'])

# Mark decoupling
ax2.axvline(1 + z_dec, ls='--', color='#E91E63', lw=1.0, alpha=0.6)
ax2.text(1 + z_dec, 0.55, '$z_{\\rm dec}$', fontsize=9, color='#E91E63',
         rotation=90, va='bottom', ha='right')

ax2.axvline(1 + z_eq, ls='--', color='#9C27B0', lw=1.0, alpha=0.6)
ax2.text(1 + z_eq, 0.55, '$z_{\\rm eq}$', fontsize=9, color='#9C27B0',
         rotation=90, va='bottom', ha='right')

ax2.set_xlabel(r'$1 + z$')
ax2.set_ylabel(r'$M_{J,\rm rel} / M_{J,\rm Newton}$', color=COLORS['relativistic'])
ax2_twin.set_ylabel(r'$c_s / c$', color=COLORS['bdnk'])
ax2.set_title('Relativistic correction and sound speed')
ax2.set_xlim(1, 6000)
ax2.set_ylim(0.3, 1.1)
ax2_twin.set_ylim(1e-6, 1)
ax2.invert_xaxis()

# Combined legend
lines1, labels1 = ax2.get_legend_handles_labels()
lines2, labels2 = ax2_twin.get_legend_handles_labels()
ax2.legend(lines1 + lines2, labels1 + labels2, loc='lower left', fontsize=9)

fig.tight_layout()
fig.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_jeans_mass_cosmic.pdf')
fig.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_jeans_mass_cosmic.png')
print("Saved fig_jeans_mass_cosmic.pdf/png")
plt.close(fig)
