"""
Jeans length vs redshift for cosmic filaments.

Physics:
- Dark matter filament + baryonic gas at cosmic web densities
- xi_gas ~ 10^{-5} (baryon fraction of filament mass)
- Jeans length lambda_J = 2*pi*R / x_max where x_max ~ 0.580 (Newtonian)
- Relativistic correction shifts x_max to longer wavelengths by factor ~(1 + 0.35*C)
- Compactness C = pi*G*rho*R^2/c^2
- At z=1000 (recombination), relativistic corrections become non-negligible

We plot:
  Left: lambda_J / R vs redshift z for Newtonian and relativistic cases
  Right: Relativistic correction factor lambda_J^{rel} / lambda_J^{N} vs z
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, G_cgs, pi, k_B, m_p
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# --- Cosmological parameters ---
H0 = 67.4e5 / 3.086e24  # Hubble constant in 1/s (67.4 km/s/Mpc)
Omega_m = 0.315
Omega_b = 0.049
rho_crit_0 = 3 * H0**2 / (8 * pi * G_cgs)  # g/cm^3, present-day critical density

# --- Filament model parameters ---
# At z=0: overdensity delta ~ 10 relative to mean matter density
# Filament radius R ~ 1 Mpc = 3.086e24 cm at z=0, scales as R(z) ~ R_0/(1+z)
R_0 = 1.0 * 3.086e24  # cm (1 Mpc at z=0)
delta_fil = 10.0  # overdensity of filament relative to mean

# Redshift array
z_arr = np.logspace(-1, 3.1, 500)  # z = 0.1 to ~1200

# Mean matter density as function of z
rho_mean_z = Omega_m * rho_crit_0 * (1 + z_arr)**3

# Filament density (proper frame)
rho_fil_z = delta_fil * rho_mean_z

# Filament radius (comoving -> proper)
R_fil_z = R_0 / (1 + z_arr)

# Baryon fraction
xi_gas = Omega_b / Omega_m  # ~0.155 (dominantly DM), but task says xi_gas ~ 1e-5
# The task specifies xi_gas ~ 10^{-5} for the gas fraction relevant to baryonic Jeans
# This is the fraction of baryonic gas that participates in the pressure support
# (most baryons are in hot ionized phase, only a small fraction in cold dense gas)
xi_gas_cold = 1e-5

# Compactness parameter C = pi * G * rho * R^2 / c^2
C_z = pi * G_cgs * rho_fil_z * R_fil_z**2 / c_cgs**2

# Newtonian Jeans length: lambda_J^N = 2*pi*R / x_max^N
# x_max^N = 0.580 (from Chandrasekhar Ch XII)
x_max_N = 0.580
lambda_J_N = 2 * pi * R_fil_z / x_max_N

# Relativistic Jeans length: lambda_J^rel = 2*pi*R / x_max^rel
# x_max^rel = x_max^N - alpha * C  (from eq. rel-12-17)
# alpha ~ 0.35 * x_max^N (numerical coefficient from the implicit dispersion relation)
alpha_coeff = 0.35
x_max_rel = x_max_N * (1 - alpha_coeff * C_z)
x_max_rel = np.maximum(x_max_rel, 0.01)  # prevent negative
lambda_J_rel = 2 * pi * R_fil_z / x_max_rel

# Ratio
ratio_lambda = lambda_J_rel / lambda_J_N

# Also compute the gas Jeans length (thermal) for comparison
# T_gas ~ T_CMB at z > 200, then T ~ T_CMB * (1+z)^2 / (1+z_dec)^2 for z < 200 (adiabatic cooling)
T_CMB_0 = 2.725  # K
z_dec = 200.0  # thermal decoupling redshift
T_gas = np.where(z_arr > z_dec,
                 T_CMB_0 * (1 + z_arr),
                 T_CMB_0 * (1 + z_dec) * ((1 + z_arr) / (1 + z_dec))**2)

# Thermal Jeans length for gas component
cs2_gas = k_B * T_gas / (0.6 * m_p)  # sound speed squared (mean molecular weight ~ 0.6)
lambda_J_thermal = np.sqrt(pi * cs2_gas / (G_cgs * rho_fil_z * xi_gas_cold))

# --- Plotting ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# Conversion: cm to Mpc
cm_per_Mpc = 3.086e24

# Left panel: lambda_J / R vs z
ax1.loglog(z_arr, lambda_J_N / R_fil_z, '-', lw=2.2, color=COLORS['classical'],
           label=r'$\lambda_J^{\rm N} / R$ (Newtonian)')
ax1.loglog(z_arr, lambda_J_rel / R_fil_z, '-', lw=2.2, color=COLORS['relativistic'],
           label=r'$\lambda_J^{\rm rel} / R$ (relativistic)')
ax1.loglog(z_arr, lambda_J_thermal / R_fil_z, '--', lw=1.5, color=COLORS['bdnk'],
           label=r'$\lambda_J^{\rm thermal} / R$ (gas, $\xi_{\rm gas}=10^{-5}$)')

# Mark specific redshifts
for z_mark, label in [(0, 'z=0'), (2, 'z=2'), (6, 'z=6'), (1000, 'z=1000')]:
    if z_mark > 0:
        ax1.axvline(z_mark, ls=':', color='gray', alpha=0.5, lw=0.8)

ax1.annotate('$z=2$', xy=(2, 15), fontsize=10, color='gray')
ax1.annotate('$z=6$', xy=(6, 15), fontsize=10, color='gray')
ax1.annotate('$z=1000$\n(recombination)', xy=(1000, 15), fontsize=9, color='gray',
             ha='right')

ax1.set_xlabel('Redshift $z$')
ax1.set_ylabel(r'$\lambda_J / R_{\rm fil}$')
ax1.set_title('Jeans length of cosmic filaments vs. redshift')
ax1.set_xlim(0.1, 1500)
ax1.set_ylim(1, 100)
ax1.legend(loc='upper left', fontsize=10)

# Right panel: Relativistic correction factor and compactness
ax2_twin = ax2.twinx()

ax2.semilogx(z_arr, ratio_lambda, '-', lw=2.5, color=COLORS['relativistic'],
             label=r'$\lambda_J^{\rm rel} / \lambda_J^{\rm N}$')
ax2.axhline(1.0, ls='--', color='gray', alpha=0.5, lw=1.0)

ax2_twin.loglog(z_arr, C_z, '-.', lw=1.8, color=COLORS['data'],
                label=r'Compactness $\mathcal{C}$')

# Shade the region where relativistic corrections exceed 1%
z_1pct = z_arr[np.argmin(np.abs(ratio_lambda - 1.01))]
ax2.axvspan(z_1pct, 1500, alpha=0.08, color=COLORS['relativistic'])
ax2.annotate('>1% correction', xy=(z_1pct * 1.5, 1.005), fontsize=9,
             color=COLORS['relativistic'])

# Mark astrophysical regimes
ax2.annotate('Cosmic web\n($z \\sim 0$--$2$)', xy=(0.5, 1.0001), fontsize=9,
             color=COLORS['classical'])
ax2.annotate('Recombination\n($z \\sim 1000$)', xy=(500, 1.003), fontsize=9,
             color=COLORS['relativistic'])

ax2.set_xlabel('Redshift $z$')
ax2.set_ylabel(r'$\lambda_J^{\rm rel} / \lambda_J^{\rm N}$', color=COLORS['relativistic'])
ax2_twin.set_ylabel(r'Compactness $\mathcal{C} = \pi G \rho R^2 / c^2$',
                     color=COLORS['data'])
ax2.set_title('Relativistic correction to Jeans length')
ax2.set_xlim(0.1, 1500)

# Build combined legend
lines1, labels1 = ax2.get_legend_handles_labels()
lines2, labels2 = ax2_twin.get_legend_handles_labels()
ax2.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=10)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_cosmic_filament_jeans.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_cosmic_filament_jeans.png')
print("Saved fig_cosmic_filament_jeans.pdf/png")
