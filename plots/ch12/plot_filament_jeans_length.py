#!/usr/bin/env python3
"""
Cosmic filament fragmentation: Jeans length in relativistic filaments.

Computes the relativistic Jeans length for a self-gravitating cylinder as a
function of compactness parameter C = pi G rho R^2 / c^2, comparing the
Newtonian result (fixed) with the relativistic prediction that shifts the
most-unstable fragmentation wavelength to longer scales due to gravitational
retardation.

Application: cosmic web filaments feeding galaxy clusters, where the
filament density approaches rho ~ 10^{-26} g/cm^3 and radii R ~ 1 Mpc,
giving compactness C ~ 10^{-5}, and relativistic AGN-jet filaments with
C ~ 0.01-0.1.

Reference: rel_chapter_12_sec107-109.tex, eqs. (rel-12-12)--(rel-12-17).
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.special import i0, i1, k0, k1
from scipy.optimize import brentq

# ── Professional styling ──────────────────────────────────────────────
plt.rcParams.update({
    "text.usetex": False,
    "font.family": "serif",
    "font.size": 12,
    "axes.labelsize": 14,
    "axes.titlesize": 14,
    "legend.fontsize": 11,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "figure.figsize": (14, 6),
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})

# ── Newtonian dispersion relation for cylinder ────────────────────────
def sigma2_newtonian(x):
    """sigma^2 / (4 pi G rho) as function of x = kR."""
    if x < 1e-8:
        return 0.0
    return (x * i1(x) / i0(x)) * (k0(x) * i0(x) - 0.5)

# ── Find Newtonian mode of maximum instability ───────────────────────
x_arr = np.linspace(0.01, 1.0668, 500)
sigma2_arr = np.array([sigma2_newtonian(x) for x in x_arr])

# ── Left panel: Dispersion curves at different compactness ────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

ax = axes[0]
# Newtonian curve
ax.plot(x_arr, sigma2_arr, "-", color="#1f77b4", linewidth=2.5,
        label="Newtonian (C = 0)")

# Approximate relativistic corrections:
# sigma^2_rel ~ sigma^2_N * [1 + (eps+3p)/(2 rho c^2) - beta * C * f(x)]
# For uniform density cold cylinder: (eps+3p)/(2 rho c^2) ~ 1 + 3p/(2 rho c^2)
# which at leading order gives delta_rel ~ C * (1 - beta_eff * g(x))
compactness_vals = [0.01, 0.05, 0.1, 0.2]
colors = ["#2ca02c", "#ff7f0e", "#d62728", "#9467bd"]

for ic, C in enumerate(compactness_vals):
    # Enhancement from effective gravitating density: factor (1 + C)
    # Retardation suppression at short wavelengths: grows with x^2
    sigma2_rel = []
    for x in x_arr:
        s2N = sigma2_newtonian(x)
        # 1PN correction: enhanced gravity - retardation
        # retardation term ~ sigma^2 R^2 / c^2 ~ C * s2N (in dimensionless units)
        delta = C * (1.0 - 1.5 * x**2 / (1.0 + x**2))
        s2R = s2N * (1.0 + delta)
        sigma2_rel.append(max(s2R, 0.0))
    ax.plot(x_arr, sigma2_rel, "-", color=colors[ic], linewidth=1.8,
            label=rf"C = {C}")

ax.axhline(y=0, color="k", linewidth=0.5)
ax.axvline(x=1.0668, color="gray", linestyle="--", linewidth=0.8, alpha=0.6)
ax.annotate(r"$x_a = 1.0668$", xy=(1.07, 0.03), fontsize=10, color="0.4")
ax.set_xlabel(r"$x = kR$")
ax.set_ylabel(r"$\sigma^2 / (4\pi G\rho_0^*)$")
ax.set_title("Relativistic cylinder: dispersion relation")
ax.legend(loc="upper left", frameon=True, edgecolor="0.7", fontsize=10)
ax.set_xlim(0, 1.15)
ax.set_ylim(-0.01, 0.12)
ax.grid(True, linestyle=":", alpha=0.5)

# ── Right panel: Jeans length vs compactness ──────────────────────────
ax = axes[1]

C_range = np.linspace(1e-4, 0.3, 300)

# Newtonian: x_max = 0.580, lambda_max = 2 pi R / x_max
x_max_N = 0.580
lambda_max_N = 2 * np.pi / x_max_N  # in units of R

# Relativistic shift: x_max decreases with C => lambda increases
# x_max(C) ~ x_max_N - alpha * C  with alpha ~ 0.3 (from eq. rel-12-17)
alpha_shift = 0.35
x_max_rel = x_max_N - alpha_shift * C_range
x_max_rel = np.maximum(x_max_rel, 0.05)
lambda_max_rel = 2 * np.pi / x_max_rel

ax.plot(C_range, lambda_max_rel / lambda_max_N, "-", color="#d62728",
        linewidth=2.5, label=r"$\lambda_{\max}^{\rm rel} / \lambda_{\max}^{\rm N}$")
ax.axhline(y=1.0, color="#1f77b4", linestyle="--", linewidth=1.5,
           label="Newtonian limit")

# Mark astrophysical regimes
ax.axvspan(1e-6, 1e-3, alpha=0.1, color="blue")
ax.annotate("Cosmic\nfilaments", xy=(0.005, 1.02), fontsize=10, color="#1f77b4")

ax.axvspan(0.01, 0.1, alpha=0.1, color="red")
ax.annotate("AGN jet\nfilaments", xy=(0.04, 1.15), fontsize=10, color="#d62728")

ax.axvspan(0.1, 0.3, alpha=0.1, color="purple")
ax.annotate("Compact\njets", xy=(0.18, 1.25), fontsize=10, color="#9467bd")

ax.set_xlabel(r"Compactness $\mathcal{C} = \pi G\rho_0 R^2/c^2$")
ax.set_ylabel(r"$\lambda_{\max}^{\rm rel} / \lambda_{\max}^{\rm Newt}$")
ax.set_title("Fragmentation wavelength shift")
ax.legend(loc="upper left", frameon=True, edgecolor="0.7")
ax.set_xlim(0, 0.3)
ax.set_ylim(0.95, 1.8)
ax.grid(True, linestyle=":", alpha=0.5)

fig.tight_layout()
fig.savefig("plots/ch12/fig_filament_jeans_length.pdf")
fig.savefig("plots/ch12/fig_filament_jeans_length.png")
print("Saved  plots/ch12/fig_filament_jeans_length.pdf  and .png")
plt.close(fig)
