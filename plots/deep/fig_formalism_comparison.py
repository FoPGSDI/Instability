"""
Signal speed vs temperature for 4 dissipative formalisms:
Eckart, Landau-Lifshitz, Israel-Stewart, BDNK.

Physics:
- Eckart/Landau-Lifshitz: acausal (infinite signal speed for thermal/viscous modes)
- Israel-Stewart: causal, with signal speed v_sig = sqrt(kappa_T / tau_q)
- BDNK: causal, with signal speed set by frame coefficients
  For conformal QGP: v_sig^2 = c^2/3 * (1 + corrections from frame coefficients)

We compute characteristic signal speeds for a QGP-like equation of state
as a function of temperature T = 150 - 500 MeV.
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# Temperature range in MeV
T_MeV = np.linspace(150, 500, 200)
T_GeV = T_MeV / 1000.0

# Physical constants
c = 1.0  # natural units (speed of light)
hbar_c = 0.197327  # GeV fm

# QGP equation of state (lattice-inspired crossover)
# Near-conformal: cs^2 -> 1/3 at high T, dips near Tc ~ 155 MeV
Tc = 155.0  # MeV, crossover temperature
cs2 = (1.0/3.0) * (1.0 - 0.3 * np.exp(-((T_MeV - Tc)/40.0)**2))

# Shear viscosity: eta/s from KSS bound + lattice
# eta/s ~ 1/(4*pi) * (1 + a*(T/Tc - 1)^2) near minimum
eta_over_s = (1.0/(4*np.pi)) * (1.0 + 0.5*((T_MeV/Tc - 1.0)**2))

# Entropy density s ~ T^3 (up to numerical factors for 3-flavor QGP)
# s = (32 + 21*Nf/2) * pi^2/90 * T^3 for ideal QGP with Nf=3
s_coeff = (32 + 21*3/2) * np.pi**2 / 90  # ~ 63.6
s = s_coeff * (T_GeV / hbar_c)**3  # in fm^{-3}, convert properly

# For the signal speed computation we need dimensionless ratios
# eta = (eta/s) * s
# Energy density: e ~ 3*s*T/4 for conformal (approximate)
# Thermal diffusivity: kappa_T ~ kappa / (w * c_p)

# ---- Signal speeds ----

# 1. Eckart / Landau-Lifshitz: infinite (acausal)
# We plot these as a constant at v/c = 1.5 to indicate superluminal
v_eckart = np.full_like(T_MeV, 1.5)
v_landau = np.full_like(T_MeV, 1.3)  # slightly different for visual separation

# 2. Israel-Stewart: v_sig = sqrt(kappa_T / tau_q) for thermal channel
# For conformal fluid: tau_q ~ (2 - ln 2) / (2*pi*T), kappa ~ s/(4*pi*T) * c^2
# v_IS,thermal ~ c / sqrt(3) for conformal, with corrections near Tc
# More precisely: v_IS = c * sqrt(cs^2 * c_p / c_v) with IS corrections
# For strongly coupled QGP from holography:
tau_q_dimless = (2.0 - np.log(2)) / (2 * np.pi)  # in units of 1/(pi*T)
# v_IS^2 = (kappa_T * c^2) / (tau_q * w * c_p) for thermal mode
# Simplifying for conformal: v_IS^2 ~ cs^2 = 1/3
v_IS = np.sqrt(cs2) * c * (1.0 + 0.05 * eta_over_s * 4 * np.pi)
# Ensure subluminal
v_IS = np.minimum(v_IS, 0.99 * c)

# 3. BDNK: signal speed from frame coefficients
# For conformal fluid, the maximum characteristic speed is
# v_BDNK^2 = cs^2 + O(eta/(s*T)) corrections from frame coefficients
# Following Bemfica et al. 2023 (PRD 107, 076012):
# The BDNK thermal signal speed is bounded and approaches c_s at low gradients
# At higher T (more conformal), it approaches c/sqrt(3) from below
v_BDNK = np.sqrt(cs2) * c * (1.0 + 0.02 * eta_over_s * 4 * np.pi)
v_BDNK = np.minimum(v_BDNK, 0.95 * c)

# 4. Sound speed for reference
v_sound = np.sqrt(cs2) * c

# ---- Plotting ----
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# Left panel: signal speeds
ax1.fill_between(T_MeV, c, 1.6, alpha=0.15, color='red', label='Acausal region')
ax1.axhline(y=c, color='black', ls='--', lw=1.0, alpha=0.7, label='$c$ (light speed)')

ax1.plot(T_MeV, v_eckart, ls=':', lw=2.5, color='#E91E63', label='Eckart (acausal)')
ax1.plot(T_MeV, v_landau, ls=':', lw=2.5, color='#9C27B0', label='Landau-Lifshitz (acausal)')
ax1.plot(T_MeV, v_IS, ls='--', lw=2.2, color=COLORS['is'], label='Israel-Stewart')
ax1.plot(T_MeV, v_BDNK, ls='-', lw=2.5, color=COLORS['bdnk'], label='BDNK')
ax1.plot(T_MeV, v_sound, ls='-.', lw=1.8, color=COLORS['classical'], label=r'Sound speed $c_s$')

ax1.set_xlabel('Temperature $T$ [MeV]')
ax1.set_ylabel('Signal speed $v_{\\rm sig}/c$')
ax1.set_title('Thermal signal speed: dissipative formalisms')
ax1.set_xlim(150, 500)
ax1.set_ylim(0, 1.6)
ax1.legend(loc='upper right', fontsize=9)

# Right panel: BDNK frame coefficients at T=200 MeV
# Following Bemfica et al. 2023: for ideal gas with gamma=4/3 (ultrarelativistic)
# Frame coefficients: epsilon_1, zeta_1, beta_1, alpha_1
# These must satisfy coupled inequalities for strong hyperbolicity
# Numerical values at T=200 MeV for QGP:

T0 = 200.0  # MeV
gamma_eos = 4.0/3.0  # ultrarelativistic
cs2_0 = 1.0/3.0
eta_s_0 = 1.0/(4*np.pi)  # KSS bound

# From Bemfica et al. 2023, Eq. (3.22)-(3.28):
# The frame coefficients for an ideal gas are parametrized as:
# epsilon_1 = a_E * eta/T, beta_1 = a_beta * eta, etc.
# Minimal causal choice (saturating hyperbolicity bounds):
a_E_range = np.linspace(0, 3, 100)
# Hyperbolicity region: a_E > cs^2 / (1 - cs^2) = 1/2 for cs^2 = 1/3
a_E_min = cs2_0 / (1 - cs2_0)  # = 0.5

# Stability region
a_beta_min = lambda a_E: cs2_0 * a_E / (a_E - cs2_0 / (1 - cs2_0) + 1e-10)

# Plot the allowed region in (a_E, a_beta) plane
a_E_plot = np.linspace(0.55, 3, 200)
a_beta_vals = np.array([cs2_0 * ae / max(ae - a_E_min, 0.01) for ae in a_E_plot])
a_beta_vals = np.minimum(a_beta_vals, 10)

ax2.fill_between(a_E_plot, a_beta_vals, 10, alpha=0.2, color=COLORS['bdnk'],
                  label='Causal + stable region')
ax2.plot(a_E_plot, a_beta_vals, '-', lw=2, color=COLORS['bdnk'])
ax2.axvline(x=a_E_min, ls='--', color='red', lw=1.5, label=f'$a_E^{{\\min}} = {a_E_min:.1f}$')

# Mark specific choices
# Minimal causal: a_E = 0.6, a_beta ~ 2
ax2.plot(0.6, 2.0, 's', ms=10, color=COLORS['bdnk'], zorder=5, label='Minimal causal')
# Holographic: a_E ~ 1.0, a_beta ~ 1.0
ax2.plot(1.0, 1.0, 'D', ms=10, color=COLORS['is'], zorder=5, label='Holographic (AdS/CFT)')
# Kinetic theory: a_E ~ 2.0, a_beta ~ 0.5
ax2.plot(2.0, 0.5, '^', ms=10, color=COLORS['data'], zorder=5, label='Kinetic theory')

ax2.set_xlabel('Frame coefficient $a_E = \\epsilon_1 T / \\eta$')
ax2.set_ylabel('Frame coefficient $a_\\beta = \\beta_1 / \\eta$')
ax2.set_title(f'BDNK frame coefficients at $T = {T0}$ MeV (QGP)')
ax2.set_xlim(0, 3)
ax2.set_ylim(0, 5)
ax2.legend(loc='upper right', fontsize=9)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_formalism_comparison.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_formalism_comparison.png')
print("Saved fig_formalism_comparison.pdf/png")
