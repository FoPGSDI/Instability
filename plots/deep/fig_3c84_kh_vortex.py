"""
Stability map for the jet of 3C 84 with KH vortex parameters,
motivated by the 2025 direct imaging of KH vortices (Fuentes et al. 2025).

3C 84 parameters:
  Gamma_jet ~ 2-3 (mildly relativistic)
  Jet opening angle ~ 1-2 deg at sub-parsec scales
  Observed KH vortex structure at ~0.3 pc

Physics:
  - Relativistic Richardson number Ri_rel across the shear profile
  - Miles-Howard stability boundary Ri_rel = 1/4
  - Stability map in (Gamma, eta) space with 3C 84 position marked
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

setup_style()

# ---- 3C 84 parameters ----
Gamma_3c84 = 2.5  # observed Lorentz factor
eta_3c84 = 0.05   # approximate jet/ambient enthalpy ratio
d_shear_pc = 0.1  # shear layer width in parsec

# ---- Stability map computation ----
# Relativistic Richardson number: Ri_rel = Ri_class / Gamma^4
# For a tanh shear layer: Ri_class = g * d / U_0^2 * (Delta_rho/rho)
# Instability when Ri_rel < 1/4

Gamma_arr = np.linspace(1.01, 10, 200)
eta_arr = np.logspace(-3, 0, 200)
Gamma_grid, eta_grid = np.meshgrid(Gamma_arr, eta_arr)

# Compute Ri_rel across the parameter space
# For a jet with opening angle theta, the effective gravity is
#   g_eff ~ V_jet^2 / R_jet (centrifugal)
# and the shear rate is dU/dz ~ V_jet / d
# Ri_rel = (g_eff * d / V_jet^2) * (Delta_rho/rho) / Gamma^4
#        = (d/R_jet) * eta / Gamma^4

# Use d/R ~ 0.3 (shear layer is ~30% of jet radius) as typical
d_over_R = 0.3
beta_grid = np.sqrt(1 - 1/Gamma_grid**2)

# Richardson number (simplified, gravitational + inertial stratification)
Ri_rel = d_over_R * (1 - eta_grid) / (Gamma_grid**4 * eta_grid)

# Growth rate (normalised) where Ri_rel < 1/4
# sigma ~ (1/4 - Ri_rel)^{1/2} * k * V for unstable modes
sigma_norm = np.where(Ri_rel < 0.25,
                      np.sqrt(np.maximum(0.25 - Ri_rel, 0)),
                      0.0)

# ---- Compute Ri_rel profile across the shear layer for 3C 84 ----
z_d = np.linspace(-3, 3, 500)  # z/d
U_profile = np.tanh(z_d)  # normalised velocity
Gamma_local = 1.0 / np.sqrt(1 - (Gamma_3c84 - 1) / Gamma_3c84 * U_profile**2 /
                              (1 + (Gamma_3c84 - 1) * U_profile**2 / Gamma_3c84))
# Simpler: V(z) = V_0 * tanh(z/d), Gamma(z) accordingly
V0 = np.sqrt(1 - 1/Gamma_3c84**2)
V_z = V0 * np.tanh(z_d)
Gamma_z = 1.0 / np.sqrt(1 - V_z**2)

# dU/dz = V0/d * sech^2(z/d)
dU_dz = V0 * (1 - np.tanh(z_d)**2)

# Enthalpy gradient (exponential stratification)
beta_strat = 0.5  # stratification parameter (in units of 1/d)
w_profile = np.exp(-beta_strat * z_d)
dw_dz = -beta_strat * w_profile

# Ri_rel(z) = -g/(w * Gamma^4) * (dw/dz) / (dU/dz)^2
g_eff = V0**2 / (d_over_R * 10)  # effective g (normalised)
Ri_rel_profile = np.where(
    dU_dz > 0.01,
    -g_eff / (w_profile * Gamma_z**4) * dw_dz / (dU_dz**2 + 1e-10),
    np.nan
)

# ---- Plotting ----
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# Left panel: Stability map in (Gamma, eta) space
levels = np.linspace(0, 0.5, 50)
cf = ax1.contourf(Gamma_arr, eta_arr, sigma_norm, levels=levels,
                   cmap='RdYlBu_r', extend='max')
cb = plt.colorbar(cf, ax=ax1, label=r'Normalised growth rate $\tilde{\sigma}$')

# Mark the Ri_rel = 1/4 boundary
ax1.contour(Gamma_arr, eta_arr, Ri_rel, levels=[0.25],
            colors='white', linewidths=2.5, linestyles='--')
ax1.text(3.5, 0.4, r'$\mathrm{Ri}_{\rm rel} = 1/4$', color='white',
         fontsize=12, fontweight='bold')

# Mark 3C 84
ax1.plot(Gamma_3c84, eta_3c84, '*', ms=18, color='white', zorder=5,
         markeredgecolor='black', markeredgewidth=1.0)
ax1.annotate('3C 84\n(Fuentes+2025)', xy=(Gamma_3c84, eta_3c84),
             xytext=(Gamma_3c84 + 1.5, eta_3c84 * 2),
             fontsize=10, color='white', fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='white', lw=1.5))

# Mark M87
ax1.plot(6.0, 0.01, 'D', ms=12, color='cyan', zorder=5,
         markeredgecolor='black', markeredgewidth=1.0)
ax1.annotate('M87', xy=(6.0, 0.01),
             xytext=(7.0, 0.02),
             fontsize=10, color='cyan', fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='cyan', lw=1.5))

# Mark Cen A
ax1.plot(3.0, 0.1, 's', ms=10, color='yellow', zorder=5,
         markeredgecolor='black', markeredgewidth=1.0)
ax1.annotate('Cen A', xy=(3.0, 0.1),
             xytext=(4.5, 0.2),
             fontsize=10, color='yellow', fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='yellow', lw=1.5))

ax1.set_xlabel(r'Jet Lorentz factor $\Gamma$')
ax1.set_ylabel(r'Density ratio $\eta = \hat{\rho}_{\rm jet}/\hat{\rho}_{\rm amb}$')
ax1.set_title('KH stability map: relativistic jets')
ax1.set_yscale('log')
ax1.set_xlim(1, 10)
ax1.set_ylim(1e-3, 1)

# Right panel: Ri_rel profile across 3C 84 shear layer
ax2.plot(z_d, Ri_rel_profile, '-', lw=2.5, color=COLORS['jet'],
         label=rf'3C 84 ($\Gamma = {Gamma_3c84}$)')

# Miles-Howard threshold
ax2.axhline(y=0.25, ls='--', color='black', lw=1.5,
            label=r'Miles--Howard: $\mathrm{Ri}_{\rm rel} = 1/4$')

# Shade unstable region
ax2.fill_between(z_d, 0, 0.25, alpha=0.15, color='red',
                 label=r'Unstable ($\mathrm{Ri}_{\rm rel} < 1/4$)')

# Also plot classical Ri for comparison
Ri_class_profile = np.where(
    dU_dz > 0.01,
    -g_eff / w_profile * dw_dz / (dU_dz**2 + 1e-10),
    np.nan
)
ax2.plot(z_d, Ri_class_profile, '--', lw=1.8, color=COLORS['classical'],
         label=r'Classical $\mathrm{Ri}$')

# Mark the vortex location from Fuentes et al. (2025)
ax2.axvspan(-1.5, -0.5, alpha=0.1, color='purple')
ax2.text(-1.0, 0.05, 'Observed\nvortex', fontsize=9, color='purple',
         ha='center', va='bottom')

ax2.set_xlabel(r'$z/d$ (across shear layer)')
ax2.set_ylabel(r'Richardson number $\mathrm{Ri}_{\rm rel}$')
ax2.set_title('3C 84: Richardson number profile')
ax2.legend(loc='upper right', fontsize=9)
ax2.set_xlim(-3, 3)
ax2.set_ylim(-0.1, 1.5)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_3c84_kh_vortex.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_3c84_kh_vortex.png')
print("Saved fig_3c84_kh_vortex.pdf/png")
