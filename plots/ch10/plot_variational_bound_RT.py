#!/usr/bin/env python3
"""
Variational bound on RT growth rate: maximum growth rate vs wavenumber.

The variational principle (§93, relativistic) provides an upper bound
on the growth rate n^2 for a given trial function. We compare the exact
growth rate with variational bounds from simple trial functions for
the exponentially stratified case.

Reference: Chandrasekhar Ch X §93 (relativistic extension).
"""
import sys; sys.path.insert(0, '/data/haiyangw/claude/Instability'); from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# --- Parameters for exponentially stratified fluid ---
g = 1.0       # normalized gravity
beta = 1.0    # stratification parameter (enthalpy gradient)
d = np.pi     # layer thickness

# Wavenumber range
k = np.linspace(0.1, 8.0, 500)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Left panel: Exact growth rates for different modes ---
colors_m = ['#2196F3', '#F44336', '#4CAF50', '#FF9800', '#9C27B0']
for m_idx, m in enumerate([1, 2, 3]):
    # Exact dispersion: g*beta/n^2 = 1 + (beta^2 d^2/4 + m^2 pi^2) / (k^2 d^2)
    factor = (0.25 * beta**2 * d**2 + m**2 * np.pi**2) / (k**2 * d**2)
    n2_exact = g * beta / (1.0 + factor)
    n_exact = np.sqrt(np.maximum(n2_exact, 0))

    ax1.plot(k, n_exact, '-', color=colors_m[m_idx], linewidth=2.0,
             label=rf'$m = {m}$ (exact)')

# Variational upper bound using trial function w_hat = sin(pi z / d)
# This corresponds to m=1 exactly, but we can compute the bound for all k
m_trial = 1
factor_trial = (0.25 * beta**2 * d**2 + m_trial**2 * np.pi**2) / (k**2 * d**2)
n2_bound = g * beta / (1.0 + factor_trial)
n_bound = np.sqrt(np.maximum(n2_bound, 0))

# A cruder trial function: w_hat = z(d-z) (parabolic)
# For this: I1 ~ integral of w * [z(d-z)]^2 + w * [d-2z]^2/k^2
# I2 ~ integral of Dw * [z(d-z)]^2
# Compute numerically
z_grid = np.linspace(0, d, 1000)
dz = z_grid[1] - z_grid[0]
w0 = np.exp(beta * z_grid)
Dw0 = beta * np.exp(beta * z_grid)
psi = z_grid * (d - z_grid)
Dpsi = d - 2 * z_grid

n2_parabolic = np.zeros_like(k)
for ik, kk in enumerate(k):
    I1 = np.trapz(w0 * (psi**2 + Dpsi**2 / kk**2), z_grid)
    I2 = np.trapz(Dw0 * psi**2, z_grid)
    n2_parabolic[ik] = g * I2 / I1

n_parabolic = np.sqrt(np.maximum(n2_parabolic, 0))

ax1.plot(k, n_parabolic, ':', color='#795548', linewidth=2.5,
         label=r'Parabolic trial (upper bound)')

# Asymptotic bound: n^2 <= g * beta (the k -> infinity limit)
ax1.axhline(y=np.sqrt(g * beta), color='gray', linestyle='--', alpha=0.5,
            label=r'$n_{\max} = \sqrt{g\beta}$')

ax1.set_xlabel(r'Wavenumber $k$', fontsize=14)
ax1.set_ylabel(r'Growth rate $n$', fontsize=14)
ax1.set_title(r'RT growth: exact modes and variational bounds', fontsize=14)
ax1.legend(loc='lower right', fontsize=10, frameon=True, edgecolor='0.7')
ax1.set_xlim(0, 8)
ax1.grid(True, linestyle=':', alpha=0.4)
ax1.text(0.05, 0.95, rf'$\beta = {beta}$, $d = \pi$',
         transform=ax1.transAxes, fontsize=11, va='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# --- Right panel: Ratio of variational bound to exact (measure of bound tightness) ---
# For the parabolic trial vs exact m=1
n2_exact_m1 = g * beta / (1.0 + (0.25 * beta**2 * d**2 + np.pi**2) / (k**2 * d**2))
ratio_parabolic = n2_parabolic / n2_exact_m1

# Classical vs relativistic comparison for the upper bound
# Relativistic: w = rho c^2 (1 + xi), so the bound is modified
xi_values = [0.0, 0.1, 0.3, 0.5]
rel_labels = [
    r'Classical ($\xi=0$)',
    r'$\xi = 0.1$',
    r'$\xi = 0.3$',
    r'$\xi = 0.5$',
]
rel_colors = ['#2196F3', '#4CAF50', '#FF9800', '#F44336']

for j, xi in enumerate(xi_values):
    # With relativistic correction: w = rho(1+xi), Dw = beta*w
    # The variational bound formula is the same structurally,
    # but the effective growth rate scales as n ~ sqrt(g*beta/(1+xi))
    # because the denominator I1 scales with (1+xi)
    n2_rel = g * beta / ((1.0 + xi) * (1.0 + (0.25 * beta**2 * d**2 + np.pi**2) / (k**2 * d**2)))
    n_rel = np.sqrt(np.maximum(n2_rel, 0))
    ax2.plot(k, n_rel, '-', color=rel_colors[j], linewidth=2.0, label=rel_labels[j])

ax2.set_xlabel(r'Wavenumber $k$', fontsize=14)
ax2.set_ylabel(r'Maximum growth rate $n_{\max}$', fontsize=14)
ax2.set_title(r'Variational bound: relativistic correction', fontsize=14)
ax2.legend(loc='lower right', fontsize=10, frameon=True, edgecolor='0.7')
ax2.set_xlim(0, 8)
ax2.grid(True, linestyle=':', alpha=0.4)
ax2.text(0.05, 0.95, r'$m=1$ mode, $\beta=1$',
         transform=ax2.transAxes, fontsize=11, va='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

fig.tight_layout()
fig.savefig('/data/haiyangw/claude/Instability/plots/ch10/fig_variational_bound_RT.pdf')
fig.savefig('/data/haiyangw/claude/Instability/plots/ch10/fig_variational_bound_RT.png')
print("Saved fig_variational_bound_RT.pdf and fig_variational_bound_RT.png")
plt.close(fig)
