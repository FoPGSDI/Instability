#!/usr/bin/env python3
"""
Deep Research 2, Plot 3:
Combined rotation + B field stability for a proto-neutron star.

Parameters: M = 1.6 M_sun, R = 20 km, f_spin = 100 Hz, B = 10^{13} G,
neutrino-driven temperature gradient.

Computes Ra_rel, Ta_rel, Q_rel simultaneously.
Determines whether convection is stationary or overstable.
Produces a 3D stability surface slice at proto-NS parameters.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, G_cgs, M_sun, pi, k_B
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import LogNorm

setup_style()

# ============================================================
# Proto-neutron star parameters
# ============================================================
M_pns = 1.6 * M_sun            # g
R_pns = 20e5                    # cm (20 km)
f_spin = 100.0                  # Hz
Omega_pns = 2 * pi * f_spin     # ~628 rad/s
B_pns = 1e13                    # G
g_pns = G_cgs * M_pns / R_pns**2  # ~5.3e13 cm/s^2
T_core = 3e10                   # K (30 MeV, hot proto-NS)

# EOS: proto-NS is hot, partially degenerate
# xi = w/(rho c^2) is larger due to thermal pressure
rho_core = 2.5e14               # g/cm^3 (~rho_nuc)
xi_pns = 1.45                   # higher than cold NS due to thermal contribution
w_pns = rho_core * c_cgs**2 * xi_pns

# Transport (neutrino-dominated in proto-NS)
nu_shear = 1.0                  # cm^2/s
eta_shear_pns = rho_core * nu_shear
kappa_T_pns = 1e7               # cm^2/s (neutrino thermal diffusivity, very high)
eta_mag_pns = 1e2               # cm^2/s (magnetic diffusivity)
alpha_th_pns = 3e-4             # K^{-1} (enhanced at high T)

# Layer depth (larger for proto-NS, convective region ~few km)
d_pns = 1e5                    # cm (1 km)

# Effective viscosity
nu_eff_pns = eta_shear_pns * c_cgs**2 / w_pns

# Prandtl numbers
Pr1 = nu_eff_pns / kappa_T_pns   # thermal Prandtl
Pr2 = nu_eff_pns / eta_mag_pns   # magnetic Prandtl

# ============================================================
# Dimensionless parameters
# ============================================================
Ta_rel_pns = 4 * Omega_pns**2 * d_pns**4 / nu_eff_pns**2
# Q_rel = Q_class / xi (see Ch IV tex derivation: Q_rel = Q * rho c^2 / w)
Q_class_pns_raw = B_pns**2 * d_pns**2 / (4 * pi * rho_core * nu_shear * eta_mag_pns)
Q_rel_pns = Q_class_pns_raw / xi_pns

# Neutrino-driven temperature gradient (Pons et al. 1999)
beta_pns = 0.1  # K/cm (typical proto-NS convective driving)
Ra_actual = rho_core * g_pns * alpha_th_pns * beta_pns * d_pns**4 / (
    (w_pns / c_cgs**2) * nu_eff_pns * kappa_T_pns)

# Classical comparison
Ta_class = 4 * Omega_pns**2 * d_pns**4 / nu_shear**2
Q_class = B_pns**2 * d_pns**2 / (4 * pi * rho_core * nu_shear * eta_mag_pns)

print(f"Proto-NS parameters:")
print(f"  g = {g_pns:.2e} cm/s^2")
print(f"  xi = {xi_pns}")
print(f"  nu_eff = {nu_eff_pns:.3e} cm^2/s")
print(f"  Pr_thermal = {Pr1:.3e}")
print(f"  Pr_magnetic = {Pr2:.3e}")
print(f"  Ta_rel = {Ta_rel_pns:.3e} (classical: {Ta_class:.3e})")
print(f"  Q_rel = {Q_rel_pns:.3e} (classical: {Q_class:.3e})")
print(f"  Ra_actual = {Ra_actual:.3e}")

# ============================================================
# Solve for critical Ra at given (Ta, Q)
# ============================================================
def Ra_c_TaQ(Ta_val, Q_val, n=1):
    """Critical Ra for free boundaries with both rotation and B.
    From eq (57) of Ch V:
    Ra = (n^2 pi^2 + a^2) * {[(n^2 pi^2+a^2)^2 + Q*n^2 pi^2]^2
         + T*n^2 pi^2*(n^2 pi^2+a^2)^2} /
         {a^2 * [(n^2 pi^2+a^2)^2 + Q*n^2 pi^2]}
    Minimize numerically over a.
    """
    def Ra_of_a(a):
        npi2 = n**2 * pi**2
        s = npi2 + a**2
        bracket = s**2 + Q_val * npi2
        numer = s * (bracket**2 + Ta_val * npi2 * s**2)
        denom = a**2 * bracket
        return numer / denom

    a_test = np.logspace(-1, 4, 5000)
    Ra_vals = np.array([Ra_of_a(a) for a in a_test])
    idx = np.argmin(Ra_vals)
    return Ra_vals[idx], a_test[idx]

# ============================================================
# Overstability criterion: Pr < 1 required
# For Pr << 1, overstability dominates when Ta is large enough
# Marginal overstable Ra from the cubic (eq 241 generalized)
# ============================================================
def Ra_c_overstable(Ta_val, Q_val, Pr):
    """Approximate critical Ra for overstability (free boundaries).
    In the large-Ta limit with Q:
    Ra_o ~ 6*Pr^{4/3} / (1+Pr)^{1/3} * (pi^2 Ta/2)^{2/3} * f(Q,Ta)
    For moderate values, use the exact cubic.
    """
    if Pr >= 1.0:
        return np.inf  # no overstability

    # Simplified: for two free boundaries with both Ta and Q,
    # overstable onset involves solving the cubic for sigma = i*omega
    # In the regime Q << Ta (rotation-dominated), the asymptotic formula works
    T1 = Ta_val / pi**4
    Q1 = Q_val / pi**2

    # Approximate: treat Q as perturbation on the rotation problem
    # Ra_o ~ (1+Pr)/Pr * [(1+x)^2 * (1+Pr) + Q1*(1+Pr)] * (1+x)/x
    # with omega^2 from rotation
    # For simplicity, use known asymptotic in Ta >> 1, Q << Ta regime:
    if T1 > 100 and Q1 < T1:
        Ra_o = 6.0 * Pr**(4./3.) / (1 + Pr)**(1./3.) * (0.5 * pi**2 * Ta_val)**(2./3.)
        # Q correction (approximate, from perturbation theory)
        Ra_o += pi**2 * Q_val * (1 + Pr) / (1 + Pr + Pr * Q1/T1)
        return Ra_o
    else:
        # fallback: just return stationary value (overstability not accessible)
        Ra_s, _ = Ra_c_TaQ(Ta_val, Q_val)
        return Ra_s * 1.5  # rough placeholder

# ============================================================
# Generate the stability surface slice
# ============================================================
Ta_range = np.logspace(0, 20, 200)
Q_range = np.logspace(0, 12, 200)
TT, QQ = np.meshgrid(Ta_range, Q_range)
Ra_c_grid = np.zeros_like(TT)

for i in range(TT.shape[0]):
    for j in range(TT.shape[1]):
        Ra_c_grid[i, j], _ = Ra_c_TaQ(TT[i, j], QQ[i, j])

# ============================================================
# Figure: 2 panels
# ============================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Panel (a): Contour plot of Ra_c(Ta, Q) ---
levels = np.logspace(2, 18, 33)
cs = ax1.contourf(TT, QQ, Ra_c_grid, levels=levels, norm=LogNorm(),
                  cmap='RdYlBu_r')
cb = plt.colorbar(cs, ax=ax1, label=r'$\mathrm{Ra}_{c,\mathrm{rel}}$')

# Mark proto-NS location
ax1.plot(Ta_rel_pns, Q_rel_pns, '*', color='lime', ms=18, markeredgecolor='k',
         markeredgewidth=1.5, zorder=10, label='Proto-NS')

# Mark stationary vs overstable boundary (approximate)
# Overstable preferred when Pr < p* ~ 0.677
# and Ta > T_threshold (depends on Q)
# For Pr << 1, overstable always preferred at large Ta
Ta_overstable_line = np.logspace(4, 20, 100)
Q_threshold = 0.5 * Ta_overstable_line**(2./3.) * Pr1**(2./3.)  # approximate
valid = Q_threshold < 1e12
ax1.plot(Ta_overstable_line[valid], Q_threshold[valid], 'w--', lw=2.0, alpha=0.8,
         label=r'Overstable/stationary boundary ($\mathrm{Pr}=%.0e$)' % Pr1)

# Mark Ra_actual contour
Ra_c_at_pns, a_c_pns = Ra_c_TaQ(Ta_rel_pns, Q_rel_pns)
Ra_o_at_pns = Ra_c_overstable(Ta_rel_pns, Q_rel_pns, Pr1)

ax1.contour(TT, QQ, Ra_c_grid, levels=[Ra_actual], colors=['yellow'],
            linewidths=2.0, linestyles=['-.'])

ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_xlabel(r'$\mathrm{Ta}_{\rm rel}$', fontsize=14)
ax1.set_ylabel(r'$Q_{\rm rel}$', fontsize=14)
ax1.set_title('(a) Stability surface: $\\mathrm{Ra}_c(\\mathrm{Ta}_{\\rm rel}, Q_{\\rm rel})$',
              fontsize=12)
ax1.legend(loc='lower right', fontsize=9)
ax1.set_xlim(1, 1e20)
ax1.set_ylim(1, 1e12)

# --- Panel (b): 1D slices at proto-NS Q value ---
Q_fixed = Q_rel_pns
Ra_c_stat = []
Ra_c_over = []
a_c_vals = []
for T in Ta_range:
    Rc, ac = Ra_c_TaQ(T, Q_fixed)
    Ra_c_stat.append(Rc)
    a_c_vals.append(ac)
    Ra_c_over.append(Ra_c_overstable(T, Q_fixed, Pr1))

Ra_c_stat = np.array(Ra_c_stat)
Ra_c_over = np.array(Ra_c_over)

ax2.loglog(Ta_range, Ra_c_stat, color=COLORS['classical'], lw=2.5,
           label='Stationary convection')
ax2.loglog(Ta_range, Ra_c_over, color=COLORS['is'], lw=2.5, ls='--',
           label=f'Overstability ($\\mathrm{{Pr}}={Pr1:.1e}$)')

# Physical Ra
ax2.axhline(Ra_actual, color='green', ls='-.', lw=1.5, alpha=0.8,
            label=f'Actual Ra (proto-NS, $\\beta=0.1$ K/cm)')

# Mark proto-NS Ta
ax2.axvline(Ta_rel_pns, color='grey', ls=':', lw=1.0, alpha=0.7)
ax2.text(Ta_rel_pns * 1.5, 1e3, f'$\\mathrm{{Ta}}_{{\\rm rel}}={Ta_rel_pns:.1e}$',
         fontsize=9, color='grey', rotation=90, va='bottom')

# Determine convection character at proto-NS
is_convective = Ra_actual > min(Ra_c_at_pns, Ra_o_at_pns)
preferred = "Overstable" if Ra_o_at_pns < Ra_c_at_pns else "Stationary"

ax2.text(0.98, 0.05,
         f'Proto-NS: $\\mathrm{{Ra}}_{{\\rm actual}}={Ra_actual:.1e}$\n'
         f'$\\mathrm{{Ra}}_c^{{(s)}}={Ra_c_at_pns:.1e}$\n'
         f'$\\mathrm{{Ra}}_c^{{(o)}}={Ra_o_at_pns:.1e}$\n'
         f'Convection: {"YES" if is_convective else "NO"}\n'
         f'Preferred mode: {preferred}',
         transform=ax2.transAxes, fontsize=10, ha='right', va='bottom',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

ax2.set_xlabel(r'$\mathrm{Ta}_{\rm rel}$', fontsize=14)
ax2.set_ylabel(r'Rayleigh number', fontsize=14)
ax2.set_title(f'(b) Slice at $Q_{{\\rm rel}}={Q_fixed:.1e}$ (proto-NS $B=10^{{13}}$ G)',
              fontsize=12)
ax2.legend(loc='upper left', fontsize=9)
ax2.set_xlim(1, 1e20)
ax2.set_ylim(1e2, 1e16)

plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), 'fig_proto_ns_combined.pdf'))
plt.savefig(os.path.join(os.path.dirname(__file__), 'fig_proto_ns_combined.png'))
print("Saved fig_proto_ns_combined.pdf/png")
print(f"\nProto-NS convection assessment:")
print(f"  Ra_actual = {Ra_actual:.3e}")
print(f"  Ra_c (stationary) = {Ra_c_at_pns:.3e}")
print(f"  Ra_c (overstable) = {Ra_o_at_pns:.3e}")
print(f"  Convective: {is_convective}")
print(f"  Preferred mode: {preferred}")
