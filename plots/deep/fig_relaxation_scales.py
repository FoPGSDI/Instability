"""
Comparison of BDNK and IS thermal relaxation length scales
for neutron star ocean parameters.

l_BDNK = kappa / (c^2 * rho * c_p)   [BDNK thermal relaxation scale]
l_IS   = sqrt(kappa * tau_q / (rho * c_p))  [IS relaxation scale]

Both agree at leading order but differ at O(l/lambda)^2.
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, k_B, m_p
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# Neutron star ocean parameters
# Temperature range: 10^7 - 10^10 K (accreting NS ocean)
T = np.logspace(7, 10, 300)  # K

# Density: ~10^6 - 10^10 g/cm^3 for ocean
# Use a representative density for each T regime
# For simplicity, fix rho and vary T
rho = 1e9  # g/cm^3 (representative NS ocean density)

# Specific heat at constant pressure (degenerate electron gas)
# c_p ~ (pi^2 / 3) * (k_B^2 * T) / (E_F * m_e)
# For NS ocean with Z/A ~ 0.5, E_F ~ 5 MeV at rho=10^9
E_F = 5.0 * 1.602e-6  # erg (5 MeV in erg)
m_e = 9.109e-28  # g
c_p = (np.pi**2 / 3.0) * k_B**2 * T / E_F  # erg/(g K) per electron
# Per gram: multiply by n_e/rho ~ Z/(A*m_p) ~ 0.5/m_p
c_p_per_gram = c_p * 0.5 / m_p  # erg/(g K)

# Thermal conductivity (electron conduction in NS ocean)
# kappa ~ 10^{20} * (T/10^8)^{-1} * (rho/10^9)^{1/3} erg/(cm s K)
# Following Potekhin & Chabrier 2018
kappa = 1e20 * (T / 1e8)**(-1) * (rho / 1e9)**(1.0/3.0)  # erg/(cm s K)

# Thermal diffusivity
kappa_T = kappa / (rho * c_p_per_gram)  # cm^2/s

# BDNK relaxation length scale
# l_BDNK = kappa / (c^2 * rho * c_p) = kappa_T / c^2
l_BDNK = kappa_T / c_cgs**2  # cm

# IS relaxation time (from kinetic theory)
# tau_q ~ l_mfp / v_th where v_th ~ sqrt(k_B T / m_ion)
# For NS ocean: tau_q ~ 10^{-18} * (T/10^8)^{-2} s (electron scattering)
tau_q = 1e-18 * (T / 1e8)**(-2)  # s

# IS relaxation length scale
# l_IS = sqrt(kappa * tau_q / (rho * c_p))
l_IS = np.sqrt(kappa_T * tau_q)  # cm

# Mean free path (for comparison)
# l_mfp ~ v_F * tau_q where v_F ~ c (relativistic electrons)
l_mfp = c_cgs * tau_q  # cm

# Difference at O(l/lambda)^2
# The BDNK and IS scales agree at leading order when tau_q ~ kappa_T / c^2
# The fractional difference is:
# (l_IS - l_BDNK) / l_BDNK ~ O(l_BDNK / lambda)^2
# where lambda is the macroscopic scale

# ---- Plotting ----
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# Left panel: relaxation length scales vs T
ax1.loglog(T, l_BDNK, '-', lw=2.5, color=COLORS['bdnk'], label=r'$\ell_{\rm BDNK} = \kappa_T / c^2$')
ax1.loglog(T, l_IS, '--', lw=2.5, color=COLORS['is'], label=r'$\ell_{\rm IS} = \sqrt{\kappa_T \tau_q}$')
ax1.loglog(T, l_mfp, ':', lw=1.8, color=COLORS['data'], label=r'$\ell_{\rm mfp} = v_F \tau_q$')

# Mark the regime where they agree
# They agree when tau_q ~ kappa_T / c^2, i.e., l_IS ~ l_BDNK
ratio = l_IS / l_BDNK
agree_mask = (ratio > 0.5) & (ratio < 2.0)

ax1.set_xlabel('Temperature $T$ [K]')
ax1.set_ylabel('Relaxation length scale [cm]')
ax1.set_title(r'Thermal relaxation: NS ocean ($\rho = 10^9$ g/cm$^3$)')
ax1.legend(loc='best', fontsize=10)
ax1.set_xlim(1e7, 1e10)

# Right panel: ratio l_IS / l_BDNK and O(l/lambda)^2 correction
ax2.semilogx(T, l_IS / l_BDNK, '-', lw=2.5, color=COLORS['relativistic'],
             label=r'$\ell_{\rm IS} / \ell_{\rm BDNK}$')
ax2.axhline(y=1.0, ls='--', color='gray', lw=1.0)

# Compute the O(l/lambda)^2 correction
# For a macroscopic scale lambda ~ 10 m = 1000 cm (ocean depth)
lam = 1000.0  # cm
correction = 1.0 + 0.5 * (l_BDNK / lam)**2
ax2.semilogx(T, correction, '--', lw=2.0, color=COLORS['bdnk'],
             label=r'$1 + \frac{1}{2}(\ell_{\rm BDNK}/\lambda)^2$')

ax2.set_xlabel('Temperature $T$ [K]')
ax2.set_ylabel('Ratio')
ax2.set_title(r'Leading-order agreement and $\mathcal{O}(\ell/\lambda)^2$ difference')
ax2.legend(loc='best', fontsize=10)
ax2.set_xlim(1e7, 1e10)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_relaxation_scales.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_relaxation_scales.png')
print("Saved fig_relaxation_scales.pdf/png")
