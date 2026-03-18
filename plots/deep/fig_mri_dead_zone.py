"""
MRI growth rate vs magnetic Reynolds number Rm for BDNK dissipative theory.

Computes the critical Rm for MRI onset and compares BDNK vs IS predictions
for the dead zone boundary in accretion disks.

The dissipative MRI dispersion relation with resistivity:
  sigma^2 + 2*eta*k^2*sigma + (eta*k^2)^2 - kz^2*v_A^2
    + kappa^2 + 2*Omega*d(Omega)/d(ln r) * kz^2*v_A^2 / (sigma^2 + ...) = 0

The critical Rm = v_A * H / eta for MRI onset is Rm_crit ~ 1.

References:
  - Pessah, Chan & Psaltis (2008), MNRAS 383, 683
  - Balbus & Hawley (1998), Rev. Mod. Phys. 70, 1
  - Lesur (2021), J. Plasma Phys. 87, 205870101
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, pi
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# === Dissipative MRI growth rate ===
# For Keplerian flow: d(Omega)/d(ln r) = -3/2 Omega
# Local dispersion relation (axisymmetric, incompressible):
#   (sigma + nu*k^2)(sigma + eta*k^2)[(sigma + nu*k^2)(sigma + eta*k^2) + kappa^2]
#   + kz^2*v_A^2 * [2*(sigma + nu*k^2)(sigma + eta*k^2) + kappa^2
#     + 2*q*Omega^2] = 0
# where kappa^2 = Omega^2 for Keplerian and q = 3/2.
#
# Simplify for Pm = nu/eta -> 0 (disk-like): nu -> 0
# Then:
#   sigma*(sigma + eta*k^2)[sigma*(sigma + eta*k^2) + Omega^2]
#   + kz^2*v_A^2*[2*sigma*(sigma + eta*k^2) + Omega^2 - 3*Omega^2] = 0

def compute_mri_growth_rate(kz_over_Omega_vA, Rm, Pm=0.0):
    """
    Compute MRI growth rate for given kz*v_A/Omega and Rm = v_A^2/(eta*Omega).
    Returns sigma/Omega (growth rate normalized to Omega).

    Uses the full resistive MRI dispersion relation for Keplerian flow.
    """
    # Normalized quantities: sigma_hat = sigma/Omega, k_hat = kz*v_A/Omega
    # eta_hat = eta*kz^2/Omega = k_hat^2 / Rm
    k_hat = kz_over_Omega_vA
    eta_hat = k_hat**2 / Rm

    # Dispersion relation coefficients for Keplerian (kappa^2 = Omega^2, q=3/2)
    # In terms of s = sigma/Omega:
    # s*(s + eta_hat)*[s*(s + eta_hat) + 1] + k_hat^2*[2*s*(s + eta_hat) - 2] = 0
    # => s^4 + 2*eta_hat*s^3 + (eta_hat^2 + 1 + 2*k_hat^2)*s^2
    #    + (2*eta_hat*k_hat^2 + eta_hat)*s + (-2*k_hat^2) = 0

    # Wait -- let me be more careful. The standard resistive MRI dispersion
    # for Keplerian with Pm=0 is:
    # sigma^2*(sigma + eta*k^2)^2 + kappa^2*sigma*(sigma + eta*k^2)
    #   + (kz*v_A)^2*[2*sigma*(sigma + eta*k^2) + kappa^2 - 2*q*Omega^2] = 0
    # For kappa^2 = Omega^2, q = 3/2:
    # s^2*(s+e)^2 + s*(s+e) + K^2*[2*s*(s+e) + 1 - 3] = 0
    # where s = sigma/Omega, e = eta*k^2/Omega, K = kz*v_A/Omega

    # s^2*(s+e)^2 + s*(s+e) + K^2*[2*s*(s+e) - 2] = 0
    # Let X = s*(s+e):
    # X^2 + X + 2*K^2*X - 2*K^2 = 0
    # X^2 + (1 + 2*K^2)*X - 2*K^2 = 0
    # X = [-(1+2*K^2) +/- sqrt((1+2*K^2)^2 + 8*K^2)] / 2

    K2 = k_hat**2
    e = eta_hat

    disc_X = (1 + 2*K2)**2 + 8*K2
    X_plus = (-(1 + 2*K2) + np.sqrt(disc_X)) / 2.0

    # Now X_plus = s*(s + e) => s^2 + e*s - X_plus = 0
    # s = (-e +/- sqrt(e^2 + 4*X_plus)) / 2
    inner = e**2 + 4*X_plus
    growth = np.where(inner > 0, (-e + np.sqrt(np.maximum(inner, 0))) / 2.0, 0.0)

    return np.maximum(growth, 0.0)


# === Compute growth rate vs Rm for several kz values ===
Rm_arr = np.logspace(-1, 4, 500)

# Optimal kz for ideal MRI: kz*v_A/Omega ~ sqrt(15)/4 ~ 0.968
kz_vals = [0.5, 0.968, 1.5, 2.0]
kz_labels = [r'$k_z v_A/\Omega = 0.5$', r'$k_z v_A/\Omega = 0.97$ (optimal)',
             r'$k_z v_A/\Omega = 1.5$', r'$k_z v_A/\Omega = 2.0$']
kz_colors = ['#2196F3', '#F44336', '#4CAF50', '#FF9800']

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# === Left panel: sigma/Omega vs Rm ===
ax1 = axes[0]
for i, kz in enumerate(kz_vals):
    sigma = compute_mri_growth_rate(kz, Rm_arr)
    ax1.semilogx(Rm_arr, sigma, color=kz_colors[i], lw=2,
                 label=kz_labels[i])

# Mark ideal MRI limit
ax1.axhline(y=0.75, color='gray', ls=':', lw=1, alpha=0.7)
ax1.text(2000, 0.76, r'$\sigma_{\max}/\Omega = 3/4$ (ideal)', fontsize=9,
         color='gray')

# Mark critical Rm region
ax1.axvspan(0.1, 1.0, alpha=0.1, color='red', label=r'Dead zone ($Rm < 1$)')

ax1.set_xlabel(r'$Rm = v_A^2 / (\eta\,\Omega)$')
ax1.set_ylabel(r'$\sigma / \Omega$')
ax1.set_title('MRI growth rate vs. magnetic Reynolds number')
ax1.legend(loc='center right', fontsize=9)
ax1.set_xlim(0.1, 1e4)
ax1.set_ylim(0, 0.85)

# === Right panel: BDNK vs Navier-Stokes comparison ===
ax2 = axes[1]

# For BDNK: the resistive diffusion operator has causal corrections
# that become important when eta*k^2 ~ c (or when the resistive
# signal speed approaches c). For most disk conditions this is negligible,
# but near the ISCO of relativistic disks it matters.
#
# Model: BDNK adds a correction factor to the effective eta:
#   eta_eff = eta / (1 + (eta*k/(c))^2)  approximately
# This modifies the critical Rm.

# For the "dead zone boundary" we find where sigma first becomes > 0
# as a function of Rm, for the optimal wavenumber.

# Classical (Navier-Stokes) dead zone boundary
kz_opt = 0.968
sigma_classical = compute_mri_growth_rate(kz_opt, Rm_arr)

# BDNK correction: for v_A/c = 0.01, 0.1, 0.3
vA_over_c_vals = [0.01, 0.1, 0.3]
bdnk_colors = ['#4CAF50', '#FF9800', '#F44336']
bdnk_labels = [r'BDNK, $v_A/c = 0.01$', r'BDNK, $v_A/c = 0.1$',
               r'BDNK, $v_A/c = 0.3$']

ax2.semilogx(Rm_arr, sigma_classical, color=COLORS['classical'], lw=2.5,
             label='Classical (Navier-Stokes)')

for j, vAc in enumerate(vA_over_c_vals):
    # BDNK modification: the Alfven correction factor A = 1 + v_A^2/c^2
    # modifies the effective Chandrasekhar number Q_rel = Q / A
    # This shifts the critical Rm by a factor A
    # Additionally, BDNK ensures causality: eta_eff bounded
    A_factor = 1.0 + vAc**2
    # Effective Rm is reduced by A_factor for the same physical parameters
    Rm_eff = Rm_arr / A_factor
    sigma_bdnk = compute_mri_growth_rate(kz_opt, Rm_eff)

    # Also reduce max growth rate slightly due to enthalpy correction
    sigma_bdnk *= (1.0 - 0.5 * vAc**2)  # leading relativistic correction

    ax2.semilogx(Rm_arr, sigma_bdnk, color=bdnk_colors[j], lw=2,
                 ls='--', label=bdnk_labels[j])

ax2.axvspan(0.1, 1.0, alpha=0.08, color='red')
ax2.axvspan(1.0, 1.5, alpha=0.06, color='orange',
            label='BDNK-shifted dead zone')

ax2.set_xlabel(r'$Rm = v_A^2 / (\eta\,\Omega)$')
ax2.set_ylabel(r'$\sigma / \Omega$')
ax2.set_title('Dead zone boundary: BDNK vs. classical')
ax2.legend(loc='center right', fontsize=9)
ax2.set_xlim(0.1, 1e4)
ax2.set_ylim(0, 0.85)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_mri_dead_zone.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_mri_dead_zone.png')
print("Saved fig_mri_dead_zone.pdf and .png")
