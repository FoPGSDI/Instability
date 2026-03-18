"""
MRI wavelength vs radius for Sgr A*: lambda_MRI/H vs r/r_g.

Model: M = 4e6 M_sun, Mdot ~ 1e-8 M_sun/yr (RIAF / ADAF model).
Computes the MRI characteristic wavelength lambda_MRI = 2*pi*v_A/Omega
and compares it to the disk scale height H(r) to assess whether the
MRI is resolved in the disk.

References:
  - Balbus & Hawley (1991), ApJ 376, 214
  - Balbus (2003), ARAA 41, 555
  - Narayan & Yi (1994), ApJ 428, L13
  - Wielgus et al. (2020), ApJ 901, 67
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, G_cgs, M_sun, pi, m_p, k_B
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# === Sgr A* parameters ===
M_bh = 4.0e6 * M_sun         # Black hole mass
Mdot = 1.0e-8 * M_sun / (365.25 * 86400)  # Accretion rate in g/s
r_g = G_cgs * M_bh / c_cgs**2  # Gravitational radius

# === Radial grid: from ISCO (6 r_g for Schwarzschild) outward ===
r_over_rg = np.linspace(6.5, 200, 500)
r = r_over_rg * r_g

# === Keplerian angular velocity ===
Omega_K = np.sqrt(G_cgs * M_bh / r**3)

# === ADAF / RIAF disk model (Narayan & Yi 1994) ===
# Scale height: H/r ~ c_s/v_K, for ADAF H/r ~ 0.3-1
# Temperature profile: T ~ T_virial * (r_g/r), ion temperature
# For ADAF: T_i ~ 10^12 (r_g/r) K
alpha_visc = 0.1  # viscosity parameter
T_ion = 1.0e12 * (r_g / r)  # ion temperature (K) - virial

# Sound speed
c_s = np.sqrt(k_B * T_ion / m_p)

# Scale height
H = c_s / Omega_K

# H/r ratio (should be ~0.3-1 for ADAF)
H_over_r = H / r

# === Magnetic field from beta parameter ===
# In ADAF: plasma beta ~ 1-10
# Density from mass conservation: rho ~ Mdot / (4*pi*r*H*v_r)
# v_r ~ alpha * c_s * (H/r)^2 for ADAF
v_r = alpha_visc * c_s * H_over_r**2
rho = Mdot / (4.0 * pi * r * H * np.abs(v_r))

# Magnetic field for different beta values
betas = [1, 10, 100]
colors_beta = ['#F44336', '#FF9800', '#2196F3']
labels_beta = [r'$\beta_{\rm pl} = 1$', r'$\beta_{\rm pl} = 10$',
               r'$\beta_{\rm pl} = 100$']

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# === Left panel: lambda_MRI / H vs r/r_g ===
ax1 = axes[0]
for i, beta in enumerate(betas):
    p_gas = rho * k_B * T_ion / m_p
    B = np.sqrt(8.0 * pi * p_gas / beta)

    # Relativistic enthalpy density
    epsilon = rho * c_cgs**2  # dominated by rest mass for this regime
    p_tot = p_gas
    w = (epsilon + p_tot) / c_cgs**2  # ~ rho for sub-relativistic

    # Alfven speed (relativistic)
    v_A2 = B**2 / (4.0 * pi * w + B**2 / c_cgs**2)
    v_A = np.sqrt(v_A2 * c_cgs**2 / c_cgs**2)  # normalize
    v_A = np.sqrt(B**2 * c_cgs**2 / (4.0 * pi * (epsilon + p_tot) + B**2))

    # MRI wavelength: lambda_MRI = 2*pi*v_A / Omega_K
    lambda_MRI = 2.0 * pi * v_A / Omega_K

    ratio = lambda_MRI / H

    ax1.semilogy(r_over_rg, ratio, color=colors_beta[i], lw=2,
                 label=labels_beta[i])

ax1.axhline(y=1.0, color='gray', ls='--', lw=1.2, alpha=0.7)
ax1.axhline(y=0.1, color='gray', ls=':', lw=1.0, alpha=0.5)
ax1.fill_between(r_over_rg, 0.01, 1.0, alpha=0.08, color='green',
                 label=r'$\lambda_{\rm MRI} < H$ (resolved)')

ax1.set_xlabel(r'$r\,/\,r_g$')
ax1.set_ylabel(r'$\lambda_{\rm MRI}\,/\,H$')
ax1.set_title(r'MRI wavelength vs. disk scale height (Sgr A$^*$)')
ax1.legend(loc='upper right', fontsize=10)
ax1.set_xlim(6, 200)
ax1.set_ylim(0.01, 100)
ax1.text(15, 40, r'MRI unresolved', fontsize=10, color='gray')
ax1.text(15, 0.3, r'MRI resolved in disk', fontsize=10, color='green',
         alpha=0.7)

# === Right panel: v_A/c and H/r vs r/r_g ===
ax2 = axes[1]

# Plot H/r
ax2.semilogy(r_over_rg, H_over_r, color=COLORS['classical'], lw=2,
             label=r'$H/r$ (ADAF)')

# Plot v_A/c for different betas
for i, beta in enumerate(betas):
    p_gas = rho * k_B * T_ion / m_p
    B = np.sqrt(8.0 * pi * p_gas / beta)
    epsilon = rho * c_cgs**2
    p_tot = p_gas
    v_A = np.sqrt(B**2 * c_cgs**2 / (4.0 * pi * (epsilon + p_tot) + B**2))
    ax2.semilogy(r_over_rg, v_A / c_cgs, color=colors_beta[i], lw=2,
                 ls='--', label=labels_beta[i] + r', $v_A/c$')

# Mark ISCO
ax2.axvline(x=6.0, color='black', ls=':', lw=1, alpha=0.5)
ax2.text(7, 0.002, 'ISCO', fontsize=9, rotation=90, va='bottom')

ax2.set_xlabel(r'$r\,/\,r_g$')
ax2.set_ylabel(r'Ratio')
ax2.set_title(r'Disk structure: Sgr A$^*$ ADAF model')
ax2.legend(loc='upper right', fontsize=9)
ax2.set_xlim(6, 200)
ax2.set_ylim(1e-4, 2)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_mri_sgra.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_mri_sgra.png')
print("Saved fig_mri_sgra.pdf and .png")
