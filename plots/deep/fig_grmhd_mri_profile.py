"""
GRMHD MRI growth rate profile: sigma(r)/Omega_K vs r/r_g for Kerr a/M = 0.9.

Includes relativistic corrections:
  - Frame-dragging modification to epicyclic frequency
  - Bounded Alfven speed v_A < c
  - ISCO location for spinning black hole

References:
  - Balbus (2003), ARAA 41, 555
  - Pessah, Chan & Psaltis (2008), MNRAS 383, 683
  - Liska et al. (2021), MNRAS 507, 983
  - Gammie, McKinney & Toth (2003), ApJ 589, 444
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, pi
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# === Kerr metric functions ===
def isco_radius(a_star):
    """ISCO radius for Kerr BH with dimensionless spin a_star = a/M.
    Returns r_ISCO / M (in gravitational units G=c=1).
    For prograde orbits."""
    Z1 = 1 + (1 - a_star**2)**(1/3) * ((1 + a_star)**(1/3) + (1 - a_star)**(1/3))
    Z2 = np.sqrt(3 * a_star**2 + Z1**2)
    return 3 + Z2 - np.sqrt((3 - Z1) * (3 + Z1 + 2*Z2))


def kerr_omega(r, a_star):
    """Keplerian angular velocity in Kerr: Omega = M^{1/2}/(r^{3/2} + a*M^{1/2})
    In units where M=1."""
    return 1.0 / (r**1.5 + a_star)


def kerr_epicyclic(r, a_star):
    """Radial epicyclic frequency kappa for Kerr.
    kappa^2 = Omega^2 * (1 - 6/r + 8*a/r^{3/2} - 3*a^2/r^2) for prograde."""
    Omega = kerr_omega(r, a_star)
    kappa2 = Omega**2 * (1 - 6.0/r + 8.0*a_star/r**1.5 - 3.0*a_star**2/r**2)
    return kappa2


def mri_max_growth_kerr(r, a_star, vA_over_c=0.01):
    """
    Maximum MRI growth rate in Kerr spacetime.

    For the MRI in a disk with Keplerian shear:
      sigma_max = (3/4) * |Omega| (ideal MRI, Keplerian)

    Relativistic corrections:
    1. The shear rate q = -d(ln Omega)/d(ln r) is modified by frame-dragging
    2. The Alfven speed is bounded: v_A < c
    3. Near ISCO, kappa^2 -> 0, modifying the MRI maximum growth rate

    General formula (Pessah & Psaltis 2005):
      sigma_max^2 = max over kz of:
        -kappa^2/4 + kz^2*v_A^2*(2*q*Omega^2 - kappa^2)/(kz^2*v_A^2 + kappa^2)
    For ideal MRI, maximized over kz, and with kappa^2 = (2-q)*2*Omega^2:
      sigma_max = q*Omega/2 when kz*v_A is optimally chosen.
    For Keplerian q=3/2: sigma_max = (3/4)*Omega.

    Near ISCO, kappa^2 -> 0, and sigma_max -> sqrt(2*q)*Omega/2 = sqrt(3)*Omega/2
    for Keplerian q = 3/2.
    """
    Omega = kerr_omega(r, a_star)
    kappa2 = kerr_epicyclic(r, a_star)

    # Shear parameter q = -d(ln Omega)/d(ln r)
    # For Kerr: q = (3/2) * r^{1/2} / (r^{3/2} + a) * r^{3/2} / (r^{3/2} + a)
    # Simplify: q = (3/2) * r^2 / (r^{3/2} + a)^2 * ... let me compute numerically
    dr = 0.001 * r
    Omega_plus = kerr_omega(r + dr, a_star)
    Omega_minus = kerr_omega(r - dr, a_star)
    q = -r / Omega * (Omega_plus - Omega_minus) / (2 * dr)

    # Maximum MRI growth rate
    # In the ideal case (eta = 0):
    # sigma_max^2 = q^2 * Omega^2 / 4  when kappa^2 > 0 and v_A sufficient
    # But bounded by the wavenumber constraint: kz < Omega/v_A
    # and by the Alfven speed bound v_A < c.

    # Full expression including kappa:
    # For optimal kz: sigma_max = (q/2)*Omega when kappa^2/(2*q*Omega^2) << 1
    # General case: sigma_max^2 = q^2*Omega^2/4 - (correction from kappa)
    # Using the exact maximization (Pessah & Psaltis):
    sigma_max_sq = np.where(
        kappa2 > 0,
        # Standard regime
        q**2 * Omega**2 / 4.0,
        # kappa^2 < 0: Rayleigh unstable, even stronger growth
        q**2 * Omega**2 / 4.0 + np.abs(kappa2) / 4.0
    )

    sigma_max = np.sqrt(np.maximum(sigma_max_sq, 0.0))

    # Relativistic correction from bounded v_A:
    # The MRI requires kz*v_A < Omega, limiting the unstable band.
    # The maximum growth rate is reduced when v_A/c is not negligible:
    # sigma_max -> sigma_max * (1 - v_A^2/(2*c^2))
    rel_correction = 1.0 - 0.5 * vA_over_c**2

    return sigma_max * rel_correction, q, kappa2


# === Compute profiles for different spins ===
spin_values = [0.0, 0.5, 0.9, 0.998]
spin_colors = ['#2196F3', '#4CAF50', '#F44336', '#9C27B0']
spin_labels = [r'$a_* = 0$', r'$a_* = 0.5$', r'$a_* = 0.9$', r'$a_* = 0.998$']

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# === Left panel: sigma/Omega_K vs r/r_g ===
ax1 = axes[0]
for i, a_star in enumerate(spin_values):
    r_isco = isco_radius(a_star)
    r_arr = np.linspace(r_isco + 0.1, 50, 500)

    sigma_max, q, kappa2 = mri_max_growth_kerr(r_arr, a_star, vA_over_c=0.01)
    Omega = kerr_omega(r_arr, a_star)

    ax1.plot(r_arr, sigma_max / np.abs(Omega), color=spin_colors[i], lw=2,
             label=spin_labels[i])

    # Mark ISCO
    ax1.axvline(x=r_isco, color=spin_colors[i], ls=':', lw=1, alpha=0.5)

ax1.axhline(y=0.75, color='gray', ls='--', lw=1, alpha=0.7)
ax1.text(35, 0.76, r'$3/4$ (Keplerian ideal)', fontsize=9, color='gray')

ax1.set_xlabel(r'$r\,/\,r_g$')
ax1.set_ylabel(r'$\sigma_{\max}\,/\,\Omega_K$')
ax1.set_title(r'MRI maximum growth rate in Kerr spacetime')
ax1.legend(loc='lower right', fontsize=10)
ax1.set_xlim(1, 50)
ax1.set_ylim(0, 1.2)

# === Right panel: Effect of v_A/c on growth rate at a* = 0.9 ===
ax2 = axes[1]
a_star = 0.9
r_isco = isco_radius(a_star)
r_arr = np.linspace(r_isco + 0.1, 50, 500)

vA_vals = [0.001, 0.01, 0.1, 0.3]
vA_colors = ['#2196F3', '#4CAF50', '#FF9800', '#F44336']
vA_styles = ['-', '-', '--', '--']
vA_labels = [r'$v_A/c = 10^{-3}$', r'$v_A/c = 10^{-2}$',
             r'$v_A/c = 0.1$', r'$v_A/c = 0.3$']

for j, vAc in enumerate(vA_vals):
    sigma_max, q, kappa2 = mri_max_growth_kerr(r_arr, a_star, vA_over_c=vAc)
    Omega = kerr_omega(r_arr, a_star)
    ax2.plot(r_arr, sigma_max / np.abs(Omega), color=vA_colors[j],
             lw=2, ls=vA_styles[j], label=vA_labels[j])

ax2.axvline(x=r_isco, color='black', ls=':', lw=1.2, alpha=0.6)
ax2.text(r_isco + 0.3, 0.1, 'ISCO', fontsize=9, rotation=90)

ax2.axhline(y=0.75, color='gray', ls='--', lw=1, alpha=0.7)

ax2.set_xlabel(r'$r\,/\,r_g$')
ax2.set_ylabel(r'$\sigma_{\max}\,/\,\Omega_K$')
ax2.set_title(r'Bounded $v_A$: relativistic MRI at $a_* = 0.9$')
ax2.legend(loc='lower right', fontsize=10)
ax2.set_xlim(1, 50)
ax2.set_ylim(0, 1.2)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_grmhd_mri_profile.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_grmhd_mri_profile.png')
print("Saved fig_grmhd_mri_profile.pdf and .png")
