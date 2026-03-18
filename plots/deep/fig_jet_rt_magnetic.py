"""
Deep Research 6: Critical magnetic field vs jet Lorentz factor for
RT stabilisation at the jet-cocoon interface.

Model: Gamma = 10 jet with B_parallel stabilization.
Critical B for stability of jet-cocoon interface.

References:
  - Duffell, ApJS 197 (2011) 15
  - Matsumoto et al., ApJ 914 (2021) 131
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, pi
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# ============================================================
# Jet parameters
# ============================================================
# Jet Lorentz factors
Gamma_range = np.logspace(0.0, 2.5, 500)  # 1 to ~300

# Cocoon parameters
rho_cocoon = 1e-25     # g/cm^3 (typical cocoon density)
p_cocoon = 1e-5        # dyn/cm^2

# Jet parameters: hot, magnetised
# Internal energy: e_jet = rho_jet c^2 + thermal
# For a relativistic jet: w_jet = (e_jet + p_jet) depends on Gamma
# Enthalpy ratio parameterised by Gamma_jet

# In the jet comoving frame:
# w_jet = rho_jet c^2 (1 + epsilon + p/(rho c^2))
# For a hot jet: epsilon ~ 1, p/(rho c^2) ~ 0.3

xi_jet = 0.3  # p/(rho c^2) in jet frame (hot)
xi_cocoon = 0.01

# ============================================================
# Critical B-field from relativistic RT stability
# ============================================================
# From eq (rel97-kcrit): k_{x,crit}^2 = (w2 - w1) g k / (2 b^2) * (1 - vA^2/c^2)
# For complete stabilisation at all k_x: need b^2 > b^2_crit
# b^2_crit = (w2 - w1) g / (2 k) * (1 - vA^2/c^2)
#
# In terms of magnetisation sigma_B = b^2 / (rho c^2):
# sigma_B_crit depends on the Atwood number and effective g

# Effective deceleration of the jet:
# g_eff ~ c^2 / R_jet for a relativistic jet decelerating
# R_jet ~ Gamma^2 c t for the deceleration radius

# Lab-frame enthalpy densities:
# In the lab frame, the jet enthalpy is boosted by Gamma^2
# w_jet_lab ~ Gamma^2 * w_jet_comoving
# w_cocoon_lab ~ w_cocoon (cocoon is roughly at rest)

# Relativistic Atwood number in the lab frame:
def A_rel_lab(Gamma, xi_j, xi_c, rho_ratio=1.0):
    """Lab-frame relativistic Atwood number for jet-cocoon interface."""
    # Comoving enthalpy densities (normalised)
    w_jet_com = 1.0 + xi_j    # per rho_jet c^2
    w_coc_com = rho_ratio * (1.0 + xi_c)  # per rho_jet c^2
    # In the interface frame, effective inertia:
    w_jet_eff = Gamma**2 * w_jet_com
    w_coc_eff = w_coc_com
    return (w_jet_eff - w_coc_eff) / (w_jet_eff + w_coc_eff)


# ============================================================
# Critical magnetisation sigma_B vs Gamma
# ============================================================
# For stabilisation of the longest wavelength mode (k ~ 1/R_jet):
# sigma_B_crit ~ A_rel * (1 - vA^2/c^2) / 2
# where vA^2/c^2 = sigma_B / (1 + sigma_B) (when w includes B)

# Self-consistent: sigma_B_crit such that
# A_rel < 2 sigma_B / (1 - sigma_B/(1+sigma_B))
# = 2 sigma_B (1 + sigma_B)

# Simplified: for weak magnetisation (sigma_B << 1):
# sigma_B_crit ~ A_rel / 2

A_vals = A_rel_lab(Gamma_range, xi_jet, xi_cocoon)
sigma_B_crit_weak = np.abs(A_vals) / 2.0

# Strong field correction:
# sigma_B_crit satisfies: A_rel = 2 sigma_B (1 + sigma_B) / (1 + 2 sigma_B)
# Solve: A = 2s(1+s)/(1+2s) => 2s^2 + 2s - A(1+2s) = 0
# 2s^2 + (2-2A)s - A = 0
# s = [-(2-2A) + sqrt((2-2A)^2 + 8A)] / 4
sigma_B_crit = np.zeros_like(Gamma_range)
for i, A in enumerate(np.abs(A_vals)):
    A = min(A, 0.999)
    disc = (2.0 - 2.0*A)**2 + 8.0*A
    sigma_B_crit[i] = (-(2.0 - 2.0*A) + np.sqrt(disc)) / 4.0

# Also compute vA/c at the critical field
vA_over_c_crit = np.sqrt(sigma_B_crit / (1.0 + sigma_B_crit))

# ============================================================
# Figure: 2x2 layout
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 11))

# Panel (a): Critical sigma_B vs Gamma_jet
ax = axes[0, 0]

# Different density ratios rho_cocoon / rho_jet
rho_ratios = [0.1, 1.0, 10.0, 100.0]
colors_rho = ['#2196F3', '#4CAF50', '#FF9800', '#F44336']

for j, rr in enumerate(rho_ratios):
    A_j = A_rel_lab(Gamma_range, xi_jet, xi_cocoon, rho_ratio=rr)
    s_crit = np.zeros_like(Gamma_range)
    for i, A in enumerate(np.abs(A_j)):
        A = min(A, 0.999)
        disc = (2.0 - 2.0*A)**2 + 8.0*A
        s_crit[i] = (-(2.0 - 2.0*A) + np.sqrt(disc)) / 4.0

    ax.loglog(Gamma_range, s_crit, '-', color=colors_rho[j], lw=2.0,
              label=rf'$\rho_{{\rm coc}}/\rho_{{\rm jet}} = {rr}$')

ax.set_xlabel(r'Jet Lorentz factor $\Gamma_{\rm jet}$')
ax.set_ylabel(r'Critical magnetisation $\sigma_{B,\rm crit}$')
ax.set_title(r'(a) Critical $\sigma_B$ for RT stabilisation')
ax.legend(fontsize=9, loc='lower right', frameon=True, edgecolor='0.7')
ax.set_xlim(1, 300)
ax.grid(True, ls=':', alpha=0.3, which='both')

# Shade AGN vs GRB regimes
ax.axvspan(1, 10, alpha=0.06, color='blue')
ax.axvspan(100, 300, alpha=0.06, color='red')
ax.text(3, 0.01, 'AGN', fontsize=9, color='blue', ha='center')
ax.text(170, 0.01, 'GRB', fontsize=9, color='red', ha='center')

# Panel (b): Critical vA/c vs Gamma
ax = axes[0, 1]

for j, rr in enumerate(rho_ratios):
    A_j = A_rel_lab(Gamma_range, xi_jet, xi_cocoon, rho_ratio=rr)
    s_crit = np.zeros_like(Gamma_range)
    for i, A in enumerate(np.abs(A_j)):
        A = min(A, 0.999)
        disc = (2.0 - 2.0*A)**2 + 8.0*A
        s_crit[i] = (-(2.0 - 2.0*A) + np.sqrt(disc)) / 4.0
    vA_c = np.sqrt(s_crit / (1.0 + s_crit))

    ax.semilogx(Gamma_range, vA_c, '-', color=colors_rho[j], lw=2.0,
                label=rf'$\rho_{{\rm coc}}/\rho_{{\rm jet}} = {rr}$')

ax.axhline(y=1.0, color='gray', ls='--', lw=1, alpha=0.5)
ax.text(2, 1.01, '$c$ (causality limit)', fontsize=9, color='gray')

ax.set_xlabel(r'Jet Lorentz factor $\Gamma_{\rm jet}$')
ax.set_ylabel(r'Critical $v_A / c$')
ax.set_title(r'(b) Critical Alfv\'en speed for stabilisation')
ax.legend(fontsize=9, loc='upper left', frameon=True, edgecolor='0.7')
ax.set_xlim(1, 300)
ax.set_ylim(0, 1.1)
ax.grid(True, ls=':', alpha=0.3, which='both')

# Panel (c): Growth rate vs k for different B-field strengths at fixed Gamma=10
ax = axes[1, 0]

Gamma_fixed = 10.0
k_norm = np.linspace(0.01, 15.0, 500)

# Effective quantities at Gamma = 10
A_eff = A_rel_lab(Gamma_fixed, xi_jet, xi_cocoon, rho_ratio=1.0)
g_norm = 1.0  # normalised effective gravity

sigma_B_vals = [0.0, 0.1, 0.3, 0.5, 0.8]
colors_sB = ['#2196F3', '#26A69A', '#4CAF50', '#FF9800', '#F44336']

for j, sB in enumerate(sigma_B_vals):
    vA_c_sq = sB / (1.0 + sB) if sB > 0 else 0.0
    vA_c = np.sqrt(vA_c_sq) if sB > 0 else 0.0

    # Horizontal field dispersion (eq rel97-dispersion):
    # n^2 = g k [A_rel - 2 b^2 k_x^2 / ((w1+w2) k (1 - vA^2/c^2))]
    # With k_x = k (parallel propagation, worst case for stabilisation)
    # n^2 = g k [A_rel - factor * k]
    # where factor = 2 sB / (1 - vA_c_sq)
    if sB > 0:
        factor = 2.0 * sB / (1.0 - vA_c_sq)
    else:
        factor = 0.0

    n2 = g_norm * k_norm * (np.abs(A_eff) - factor * k_norm)
    n_growth = np.where(n2 > 0, np.sqrt(n2), 0.0)

    label = 'No B-field' if sB == 0 else rf'$\sigma_B = {sB}$'
    ls = '--' if sB == 0 else '-'
    ax.plot(k_norm, n_growth, ls, color=colors_sB[j], lw=2.0, label=label)

ax.set_xlabel(r'Normalised wavenumber $\hat{k}$')
ax.set_ylabel(r'Growth rate $\hat{n}$')
ax.set_title(rf'(c) RT growth with horizontal B ($\Gamma = {Gamma_fixed:.0f}$)')
ax.legend(fontsize=9, loc='upper right', frameon=True, edgecolor='0.7')
ax.set_xlim(0, 15)
ax.set_ylim(0, None)
ax.grid(True, ls=':', alpha=0.3)
ax.text(0.05, 0.75, 'Magnetic tension\nsuppresses short $\\lambda$',
        transform=ax.transAxes, fontsize=9,
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

# Panel (d): Vertical field -- growth rate saturation for different Gamma
ax = axes[1, 1]

k_plot = np.linspace(0.01, 15.0, 500)
Gamma_vals = [2.0, 5.0, 10.0, 50.0, 100.0]
colors_G = ['#2196F3', '#26A69A', '#4CAF50', '#FF9800', '#F44336']

# Fix sigma_B = 0.3
sigma_B_fixed = 0.3
vA_sq = sigma_B_fixed / (1.0 + sigma_B_fixed)
vA_c_factor = np.sqrt(1.0 - vA_sq)

for j, Gam in enumerate(Gamma_vals):
    A_j = np.abs(A_rel_lab(Gam, xi_jet, xi_cocoon, rho_ratio=1.0))

    # Lab-frame enthalpy fractions
    w_jet_eff = Gam**2 * (1.0 + xi_jet)
    w_coc_eff = 1.0 + xi_cocoon
    alpha1 = w_coc_eff / (w_jet_eff + w_coc_eff)
    alpha2 = w_jet_eff / (w_jet_eff + w_coc_eff)

    # Asymptotic limits from eq rel96-asymptotics:
    # k -> 0: n^2 -> g k (alpha2 - alpha1)
    # k -> inf: n -> (g/vA) * (sqrt(alpha2) - sqrt(alpha1)) * sqrt(1 - vA^2/c^2)
    g_n = 1.0
    vA_n = np.sqrt(vA_sq)

    n_low = np.sqrt(g_n * k_plot * (alpha2 - alpha1))
    n_high = (g_n / vA_n) * (np.sqrt(alpha2) - np.sqrt(alpha1)) * vA_c_factor

    # Smooth interpolation
    n_approx = n_low * n_high / np.sqrt(n_low**2 + n_high**2)

    ax.plot(k_plot, n_approx, '-', color=colors_G[j], lw=2.0,
            label=rf'$\Gamma = {Gam:.0f}$')
    ax.axhline(y=n_high, color=colors_G[j], ls=':', lw=0.8, alpha=0.4)

ax.set_xlabel(r'Normalised wavenumber $\hat{k}$')
ax.set_ylabel(r'Growth rate $\hat{n}$')
ax.set_title(rf'(d) Vertical B saturation ($\sigma_B = {sigma_B_fixed}$)')
ax.legend(fontsize=9, loc='upper left', frameon=True, edgecolor='0.7')
ax.set_xlim(0, 15)
ax.grid(True, ls=':', alpha=0.3)
ax.text(0.95, 0.05, 'Dotted: saturation levels\n'
        + r'$\propto(\sqrt{\alpha_2} - \sqrt{\alpha_1})\sqrt{1 - v_A^2/c^2}$',
        transform=ax.transAxes, fontsize=8, ha='right',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_jet_rt_magnetic.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_jet_rt_magnetic.png')
print("Saved fig_jet_rt_magnetic.pdf/png")
plt.close(fig)
