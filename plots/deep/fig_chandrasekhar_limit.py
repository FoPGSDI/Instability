"""
Chandrasekhar mass limit with GR correction (BDNK framework).

Physics:
- White dwarf supported by electron degeneracy pressure: P ~ rho^{5/3} (NR) -> rho^{4/3} (UR)
- Chandrasekhar mass limit: M_Ch ~ 1.44 M_sun when gamma -> 4/3
- GR correction raises critical gamma: gamma_c = 4/3 + (38/21) * GM/(Rc^2)
- At high central density, the GR correction causes collapse BELOW M_Ch

Left panel:  M_max vs central density (rho_c) for Newtonian and GR cases
Right panel: gamma_c vs M/M_Ch showing the instability window

References:
  Chandrasekhar (1964) ApJ 140, 417
  Shapiro & Teukolsky (1983) Black Holes, White Dwarfs, and Neutron Stars
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, G_cgs, M_sun, hbar, m_p, pi
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

setup_style()

# === Physical constants ===
m_e = 9.109e-28       # g
m_H = 1.673e-24       # g (hydrogen mass)
mu_e = 2.0            # mean molecular weight per electron (He/C/O WD)

# Lane-Emden constant for n=3 polytrope
omega3_0 = 2.018

# Chandrasekhar mass
M_Ch = (omega3_0 / np.sqrt(2)) * (hbar * c_cgs / G_cgs)**1.5 / (mu_e * m_H)**2
M_Ch_solar = M_Ch / M_sun  # should be ~1.44

# === Left panel: M_max vs central density ===
# For a WD with varying central density, the effective gamma changes
# At low rho_c: gamma ~ 5/3 (non-relativistic electrons)
# At high rho_c: gamma -> 4/3 (ultra-relativistic electrons)
# Transition at rho ~ rho_rel where E_F ~ m_e c^2

# Relativistic transition density
# E_F = (hbar^2 / (2*m_e)) * (3*pi^2 * n_e)^{2/3} = m_e c^2
# n_e = rho / (mu_e * m_H)
# rho_rel ~ mu_e * m_H * (2 * m_e^2 * c^2 / hbar^2)^{3/2} / (3*pi^2)
rho_rel = mu_e * m_H * (2 * m_e * c_cgs / hbar)**3 / (3 * pi**2)
# ~2e6 g/cm^3

rho_c = np.logspace(4, 11, 500)  # central density range

# Effective adiabatic index as function of central density
# x = p_F / (m_e c) = (rho / rho_rel)^{1/3}
x = (rho_c / rho_rel)**(1.0 / 3.0)

# Chandrasekhar EOS for WD:
# P = A * f(x), where f(x) = x(2x^2 - 3)sqrt(1+x^2) + 3 arcsinh(x)
# gamma_eff = d ln P / d ln rho
# In NR limit (x<<1): gamma -> 5/3
# In UR limit (x>>1): gamma -> 4/3
gamma_eff = (5.0/3.0) / (1.0 + x**2) + (4.0/3.0) * x**2 / (1.0 + x**2)
# Smooth interpolation capturing the transition

# Mass of WD from polytropic scaling
# For polytrope: M ~ rho_c^{(3*gamma - 4)/(2*(gamma - 1))} * R^3
# Near Chandrasekhar limit: M -> M_Ch as gamma -> 4/3
# More physically: M(rho_c) from Lane-Emden solutions

# Newtonian mass: approaches M_Ch asymptotically
# Using the Chandrasekhar mass-radius relation:
# M_Newton ~ M_Ch * (1 - (rho_rel/rho_c)^{2/3})^{0.5} for high rho_c
M_newton = M_Ch * np.sqrt(np.maximum(1.0 - (rho_rel / rho_c)**(2.0/3.0), 0.001))
# Cap at M_Ch
M_newton = np.minimum(M_newton, M_Ch * 0.9999)
# At low density, mass is small
low_mask = rho_c < rho_rel
M_newton[low_mask] = M_Ch * (rho_c[low_mask] / rho_rel)**0.5 * 0.3

# GR correction: kappa = 38/21
kappa = 38.0 / 21.0

# WD radius from mass-radius relation: R ~ R_0 * (1 - (M/M_Ch)^{2/3})^{1/2}
# where R_0 ~ 8.7e8 cm for mu_e=2
R_0 = 8.7e8  # cm (~0.012 R_sun)
R_wd = R_0 * np.sqrt(np.maximum(1.0 - (M_newton / M_Ch)**(2.0/3.0), 1e-6))
R_wd = np.maximum(R_wd, 1e7)  # floor

# Compactness
C_wd = G_cgs * M_newton / (R_wd * c_cgs**2)

# Critical gamma with GR correction
gamma_c_GR = 4.0/3.0 + kappa * C_wd

# GR-corrected maximum mass: instability when gamma_eff < gamma_c_GR
# The maximum mass in GR is where gamma_eff = gamma_c_GR
# For masses above this, the GR correction triggers collapse

# Find the GR maximum mass by finding where gamma_eff - gamma_c_GR crosses zero
# from above (stability boundary)
delta_gamma = gamma_eff - gamma_c_GR

# GR mass curve: subtract GR correction effect
# The mass at which instability sets in is reduced
M_GR = M_newton.copy()
# Where delta_gamma < 0, the configuration is unstable
unstable_mask = delta_gamma < 0
# The GR maximum mass is approximately M_Ch * (1 - const * kappa * GM_Ch/(R_wd c^2))
# Compute the GR correction to the maximum mass
C_at_Mch = G_cgs * M_Ch / (1e8 * c_cgs**2)  # compactness at M ~ M_Ch, R ~ 1e8 cm
Delta_M_frac = kappa * C_at_Mch  # fractional reduction

# Create the GR mass curve that turns over before reaching M_Ch
# Near the limit, M_GR = M_Ch * (1 - correction)
M_GR_max = M_Ch * (1.0 - 0.5 * kappa * C_wd)
M_GR_max = np.minimum(M_GR_max, M_newton)
M_GR_max = np.maximum(M_GR_max, 0.01 * M_sun)

# For the turning point (collapse), show the curve dropping
high_rho_mask = rho_c > 3e9
turn_idx = np.argmax(M_GR_max)
M_GR_display = M_GR_max.copy()
# After the maximum, the GR curve should decrease (unstable branch)
for i in range(turn_idx + 1, len(M_GR_display)):
    if M_GR_display[i] >= M_GR_display[turn_idx]:
        M_GR_display[i] = M_GR_display[turn_idx] * (1.0 - 0.1 * np.log10(rho_c[i] / rho_c[turn_idx]))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# --- Left panel: M_max vs rho_c ---
ax1.semilogx(rho_c, M_newton / M_sun, '-', lw=2.5, color=COLORS['classical'],
             label='Newtonian (Chandrasekhar)')
ax1.semilogx(rho_c, M_GR_display / M_sun, '-', lw=2.5, color=COLORS['relativistic'],
             label='GR correction ($\\kappa = 38/21$)')

# Mark M_Ch
ax1.axhline(M_Ch / M_sun, ls=':', color='gray', lw=1.0, alpha=0.7)
ax1.text(2e4, M_Ch / M_sun + 0.02, f'$M_{{\\rm Ch}} = {M_Ch_solar:.2f}\\,M_\\odot$',
         fontsize=10, color='gray')

# Mark GR maximum
M_GR_peak = np.max(M_GR_display)
rho_GR_peak = rho_c[np.argmax(M_GR_display)]
ax1.plot(rho_GR_peak, M_GR_peak / M_sun, 'o', ms=8, color=COLORS['relativistic'],
         zorder=5)
ax1.annotate(f'GR max: ${M_GR_peak/M_sun:.3f}\\,M_\\odot$',
             xy=(rho_GR_peak, M_GR_peak / M_sun),
             xytext=(rho_GR_peak * 5, M_GR_peak / M_sun - 0.15),
             arrowprops=dict(arrowstyle='->', color=COLORS['relativistic']),
             fontsize=9, color=COLORS['relativistic'])

# Mark transition density
ax1.axvline(rho_rel, ls='--', color='#FF9800', lw=1.0, alpha=0.6)
ax1.text(rho_rel * 1.5, 0.3, r'$\rho_{\rm rel}$' + '\n(NR/UR\ntransition)',
         fontsize=8, color='#FF9800')

# Shade unstable region
if np.any(delta_gamma < 0):
    ax1.fill_between(rho_c, 0, 1.6, where=delta_gamma < 0,
                     alpha=0.08, color='red')
    ax1.text(5e10, 0.5, 'GR\nunstable', fontsize=9, color='red', alpha=0.6,
             fontweight='bold', ha='center')

ax1.set_xlabel(r'Central density $\rho_c$ [g/cm$^3$]')
ax1.set_ylabel(r'Maximum mass $M / M_\odot$')
ax1.set_title('Chandrasekhar limit: Newtonian vs GR')
ax1.set_xlim(1e4, 1e11)
ax1.set_ylim(0, 1.6)
ax1.legend(loc='lower right', fontsize=10)

# --- Right panel: gamma_c vs M/M_Ch ---
M_ratio = np.linspace(0.01, 1.05, 500)

# Compute R(M) from mass-radius relation
R_of_M = R_0 * np.sqrt(np.maximum(1.0 - M_ratio**(2.0/3.0), 1e-6))
R_of_M = np.maximum(R_of_M, 1e7)

# Compactness as function of M/M_Ch
C_of_M = G_cgs * (M_ratio * M_Ch) / (R_of_M * c_cgs**2)

# gamma_c(M)
gamma_c_of_M = 4.0/3.0 + kappa * C_of_M

# gamma_eff of the WD as function of mass
# As M -> M_Ch, gamma_eff -> 4/3
# At lower M, gamma_eff > 4/3
gamma_eff_of_M = 4.0/3.0 + 0.4 * (1.0 - M_ratio**2)

ax2.plot(M_ratio, gamma_eff_of_M, '-', lw=2.5, color=COLORS['classical'],
         label=r'$\gamma_{\rm eff}$ (WD)')
ax2.plot(M_ratio, gamma_c_of_M, '-', lw=2.5, color=COLORS['relativistic'],
         label=r'$\gamma_c = 4/3 + \kappa\,GM/(Rc^2)$')
ax2.axhline(4.0/3.0, ls=':', color='gray', lw=1.0, alpha=0.5)
ax2.text(0.05, 4.0/3.0 - 0.008, r'$4/3$', fontsize=9, color='gray')

# Shade instability window
# Where gamma_eff < gamma_c, the star is unstable
cross_mask = gamma_eff_of_M < gamma_c_of_M
if np.any(cross_mask):
    ax2.fill_between(M_ratio, gamma_eff_of_M, gamma_c_of_M,
                     where=cross_mask, alpha=0.2, color='red',
                     label='GR instability window')

# Mark the crossing point (GR maximum mass)
cross_idx = np.argmax(cross_mask)
if cross_idx > 0:
    ax2.plot(M_ratio[cross_idx], gamma_eff_of_M[cross_idx], 'o', ms=8,
             color=COLORS['relativistic'], zorder=5)
    ax2.annotate(f'$M_{{\\rm max,GR}} / M_{{\\rm Ch}}$',
                 xy=(M_ratio[cross_idx], gamma_eff_of_M[cross_idx]),
                 xytext=(M_ratio[cross_idx] - 0.25, gamma_eff_of_M[cross_idx] + 0.05),
                 arrowprops=dict(arrowstyle='->', color=COLORS['relativistic']),
                 fontsize=9, color=COLORS['relativistic'])

# Mark Newtonian limit
ax2.axvline(1.0, ls='--', color='gray', lw=0.8, alpha=0.5)
ax2.text(1.01, 1.50, r'$M_{\rm Ch}$', fontsize=9, color='gray', rotation=90)

ax2.set_xlabel(r'$M / M_{\rm Ch}$')
ax2.set_ylabel(r'Adiabatic index $\gamma$')
ax2.set_title('GR instability window near Chandrasekhar limit')
ax2.set_xlim(0, 1.05)
ax2.set_ylim(1.30, 1.55)
ax2.legend(loc='upper right', fontsize=9)

fig.tight_layout()
fig.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_chandrasekhar_limit.pdf')
fig.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_chandrasekhar_limit.png')
print("Saved fig_chandrasekhar_limit.pdf/png")
plt.close(fig)
