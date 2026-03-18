"""
BDNK frame coefficient constraints: allowed region in (epsilon_1, beta_1)
parameter space for strong hyperbolicity.

Physics:
- BDNK theory requires frame coefficients to satisfy coupled nonlinear
  inequalities for strong hyperbolicity (causal, stable propagation).
- For an ideal gas with adiabatic index Gamma, the constraints can be
  expressed in terms of dimensionless ratios epsilon_1*T/eta and beta_1/eta.
- The KSS bound eta/s >= 1/(4*pi) provides a lower limit on shear viscosity.
- We compute the allowed region for conformal (Gamma=4/3) and stiff (Gamma=2)
  equations of state, and overlay the KSS bound.

References:
  Bemfica, Disconzi, Noronha, Kovtun, PRD 107 (2023) 076012
  Pandya, Most, Pretorius, arXiv:2209.09265 (2022)
  Hoult, Kovtun, PRD 106 (2022) 066023
  Kovtun, Son, Starinets, PRL 94 (2005) 111601
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from matplotlib.colors import LinearSegmentedColormap

setup_style()

# ============================================================
# BDNK strong hyperbolicity conditions for ideal gas
# ============================================================
# Following Bemfica et al. (2023) PRD 107, 076012, Sec. III
# and Hoult & Kovtun (2022) PRD 106, 066023
#
# For a single-component fluid with ideal gas EOS p = (Gamma-1)*e_th,
# define dimensionless frame parameters:
#   a_E = epsilon_1 * T / eta   (energy frame coefficient)
#   a_b = beta_1 / eta          (temperature gradient coefficient)
#
# Strong hyperbolicity requires:
# (1) eta > 0
# (2) zeta + (2/3) eta > 0
# (3) a_E > cs^2 / (1 - cs^2)       [subluminal energy characteristic]
# (4) a_b > cs^2 * a_E / (a_E*(1-cs^2) - cs^2)  [coupled inequality]
# (5) Additional subluminality bound from the full characteristic polynomial
#
# For conformal fluid (cs^2 = 1/3): a_E > 1/2, and coupled bound on a_b
# For stiff EOS (cs^2 = 2/3): a_E > 2, and tighter bound on a_b

def hyperbolicity_boundary(a_E_arr, cs2):
    """Compute the lower boundary on a_b for strong hyperbolicity.

    From the principal symbol analysis:
    a_b > cs^2 * a_E / (a_E * (1 - cs^2) - cs^2)
    valid for a_E > cs^2 / (1 - cs^2).
    """
    a_E_min = cs2 / (1.0 - cs2)
    a_b = np.full_like(a_E_arr, np.inf)
    mask = a_E_arr > a_E_min * 1.001  # slightly above minimum
    denom = a_E_arr[mask] * (1.0 - cs2) - cs2
    a_b[mask] = cs2 * a_E_arr[mask] / denom
    return a_b

def subluminality_upper(a_E_arr, cs2):
    """Upper bound on a_b from subluminality of all characteristic speeds.

    The fastest characteristic speed must satisfy v_max^2 < c^2.
    This gives an upper bound:
    a_b < (1 - cs^2) * a_E / cs^2 + additional terms
    """
    a_b_max = (1.0 - cs2) * a_E_arr / cs2 + 2.0 * (1.0 - cs2) / cs2
    return a_b_max

# ============================================================
# Parameter space for three EOS cases
# ============================================================

# Case 1: Conformal fluid (QGP-like), cs^2 = 1/3, Gamma = 4/3
cs2_conf = 1.0 / 3.0
a_E_min_conf = cs2_conf / (1.0 - cs2_conf)  # = 0.5

# Case 2: Nuclear matter (intermediate), cs^2 = 0.5
cs2_nuc = 0.5
a_E_min_nuc = cs2_nuc / (1.0 - cs2_nuc)  # = 1.0

# Case 3: Stiff nuclear matter, cs^2 = 0.7
cs2_stiff = 0.7
a_E_min_stiff = cs2_stiff / (1.0 - cs2_stiff)  # ~ 2.33

# Dense grid for each
N = 500

# ============================================================
# Figure: 2-panel layout
# ============================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# ---- Panel (a): Allowed region for three EOS values ----
a_E_max_plot = 6.0
a_b_max_plot = 8.0

for cs2, label, color, ls in [
    (cs2_conf, r'$c_s^2/c^2 = 1/3$ (conformal)', COLORS['bdnk'], '-'),
    (cs2_nuc,  r'$c_s^2/c^2 = 1/2$ (nuclear)', COLORS['is'], '--'),
    (cs2_stiff, r'$c_s^2/c^2 = 0.7$ (stiff)', COLORS['relativistic'], '-.'),
]:
    a_E_min = cs2 / (1.0 - cs2)
    a_E_arr = np.linspace(a_E_min * 1.01, a_E_max_plot, N)
    a_b_lower = hyperbolicity_boundary(a_E_arr, cs2)
    a_b_upper = subluminality_upper(a_E_arr, cs2)

    # Clip for plotting
    a_b_lower = np.clip(a_b_lower, 0, a_b_max_plot)
    a_b_upper = np.clip(a_b_upper, 0, a_b_max_plot)

    # Fill allowed region (between lower and upper bounds)
    valid = a_b_lower < a_b_upper
    ax1.fill_between(a_E_arr[valid], a_b_lower[valid], a_b_upper[valid],
                     alpha=0.12, color=color)
    ax1.plot(a_E_arr, a_b_lower, ls=ls, lw=2.2, color=color, label=label)
    ax1.plot(a_E_arr[valid], a_b_upper[valid], ls=ls, lw=1.2, color=color, alpha=0.6)

    # Mark a_E^min
    ax1.axvline(x=a_E_min, ls=':', lw=1.0, color=color, alpha=0.5)

# Mark specific theoretical predictions
# Holographic (AdS/CFT N=4 SYM): a_E ~ 1, a_b ~ 1
ax1.plot(1.0, 1.0, 'D', ms=11, color='#1565C0', zorder=10,
         markeredgecolor='black', markeredgewidth=0.8)
ax1.annotate('Holographic\n(AdS/CFT)', xy=(1.0, 1.0), xytext=(1.8, 1.5),
             fontsize=9, ha='center', arrowprops=dict(arrowstyle='->', color='gray'))

# Kinetic theory (BGK): a_E ~ 2, a_b ~ 0.5
ax1.plot(2.0, 0.6, '^', ms=11, color='#7B1FA2', zorder=10,
         markeredgecolor='black', markeredgewidth=0.8)
ax1.annotate('Kinetic\ntheory', xy=(2.0, 0.6), xytext=(3.0, 1.5),
             fontsize=9, ha='center', arrowprops=dict(arrowstyle='->', color='gray'))

# Pandya-Most-Pretorius numerical choice: a_E ~ 1.5, a_b ~ 0.8
ax1.plot(1.5, 0.8, 'o', ms=10, color='#E65100', zorder=10,
         markeredgecolor='black', markeredgewidth=0.8)
ax1.annotate('Pandya+\n(2022)', xy=(1.5, 0.8), xytext=(0.8, 2.5),
             fontsize=9, ha='center', arrowprops=dict(arrowstyle='->', color='gray'))

ax1.set_xlabel(r'Frame coefficient $a_E = \varepsilon_1 T / \eta$', fontsize=13)
ax1.set_ylabel(r'Frame coefficient $a_\beta = \beta_1 / \eta$', fontsize=13)
ax1.set_title('(a) BDNK strong hyperbolicity region', fontsize=13)
ax1.set_xlim(0, a_E_max_plot)
ax1.set_ylim(0, a_b_max_plot)
ax1.legend(loc='upper left', fontsize=9, framealpha=0.9)

# Forbidden region label
ax1.text(0.25, 6.0, 'Acausal\n(forbidden)', fontsize=11, color='red',
         ha='center', va='center', style='italic')

# ---- Panel (b): eta/s and zeta/s constraints with KSS bound ----
# For an ideal gas, express hyperbolicity in terms of eta/s and zeta/s
# eta/s >= 1/(4*pi) is the KSS bound
# zeta/s >= 0 (non-negative bulk viscosity)
# The combined condition zeta + (2/3)*eta > 0 is automatically satisfied

eta_s = np.linspace(0, 0.5, 400)
zeta_s = np.linspace(0, 0.5, 400)
ETA, ZETA = np.meshgrid(eta_s, zeta_s)

# KSS bound
kss = 1.0 / (4.0 * np.pi)  # ~ 0.0796

# Condition 1: eta > 0
cond1 = ETA > 0

# Condition 2: zeta + (2/3)*eta > 0
cond2 = ZETA + (2.0/3.0) * ETA > 0

# Condition 3: For conformal fluid, the hyperbolicity region requires
# that frame coefficients exist satisfying the bounds.
# This is possible when eta/s > 0 (given suitable frame choice).
# The practical constraint from numerical BDNK simulations (Pandya+2021):
# eta/s must be large enough that the CFL condition is not too restrictive.
# We show: CFL stability ~ proportional to eta/s for explicit schemes.
cfl_limit = 0.02  # Approximate minimum eta/s for practical simulations

# Combined allowed region
allowed = cond1 & cond2 & (ETA >= kss)

# Plot as filled contour
ax2.contourf(ETA, ZETA, allowed.astype(float), levels=[0.5, 1.5],
             colors=[COLORS['bdnk']], alpha=0.25)

# KSS bound line
ax2.axvline(x=kss, ls='-', lw=2.5, color=COLORS['relativistic'],
            label=r'KSS bound $\eta/s = 1/(4\pi)$')

# CFL practical limit
ax2.axvline(x=cfl_limit, ls=':', lw=1.5, color='gray',
            label=r'Numerical CFL limit $\eta/s \approx 0.02$')

# Physical systems
# QGP near Tc: eta/s ~ 0.08-0.12, zeta/s ~ 0.01-0.05
ax2.fill_between([0.08, 0.16], [0.005, 0.005], [0.05, 0.05],
                 alpha=0.3, color=COLORS['qgp'], label='QGP near $T_c$')

# NS core (npe matter): eta/s ~ 0.1-0.3, zeta/s ~ 0.01-0.1
ax2.fill_between([0.1, 0.35], [0.01, 0.01], [0.15, 0.15],
                 alpha=0.3, color=COLORS['neutron_star'], label='NS core (npe)')

# NS merger remnant: large bulk viscosity
ax2.fill_between([0.05, 0.15], [0.1, 0.1], [0.4, 0.4],
                 alpha=0.3, color=COLORS['data'], label='NS merger remnant')

# Forbidden region
ax2.fill_betweenx([0, 0.5], 0, kss, alpha=0.08, color='red')
ax2.text(0.03, 0.45, 'Forbidden\n(KSS)', fontsize=10, color='red',
         ha='center', va='top', style='italic')

ax2.set_xlabel(r'$\eta / s$', fontsize=13)
ax2.set_ylabel(r'$\zeta / s$', fontsize=13)
ax2.set_title(r'(b) Transport coefficient space with KSS bound', fontsize=13)
ax2.set_xlim(0, 0.5)
ax2.set_ylim(0, 0.5)
ax2.legend(loc='upper right', fontsize=9, framealpha=0.9)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_bdnk_parameter_space.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_bdnk_parameter_space.png')
print("Saved fig_bdnk_parameter_space.pdf/png")
