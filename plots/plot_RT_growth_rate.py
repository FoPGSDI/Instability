#!/usr/bin/env python3
"""
Rayleigh-Taylor instability growth rate: classical vs relativistic.

Classical:  sigma^2 = g k A,  where A = (rho2 - rho1)/(rho2 + rho1)  (Atwood number)
Relativistic:  sigma^2 = g k A_rel,  where A_rel = (w2 - w1)/(w2 + w1),
               w = (epsilon + p)/c^2  (enthalpy density / c^2)

Viscous damping (BDNK first-order):
    sigma^2 = g k A_rel - nu k^2 sigma   =>  cubic in sigma

Reference: Chapters X-XIV of the relativistic instability monograph.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ── Professional styling ──────────────────────────────────────────────
plt.rcParams.update({
    "text.usetex": False,
    "font.family": "serif",
    "font.size": 12,
    "axes.labelsize": 14,
    "axes.titlesize": 14,
    "legend.fontsize": 10,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "figure.figsize": (8, 6),
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})

# ── Parameters ────────────────────────────────────────────────────────
g = 1.0          # gravitational acceleration (normalised)
c = 1.0          # speed of light (natural units)
k = np.linspace(0.01, 10, 500)

# Atwood numbers (classical and relativistic)
A_values = [0.1, 0.3, 0.5, 0.7, 0.9]
colors_class = ["#a6cee3", "#6baed6", "#3182bd", "#08519c", "#08306b"]
colors_rel   = ["#fdae6b", "#f16913", "#d94801", "#a63603", "#7f2704"]

# Relativistic correction: A_rel < A for hot matter because enthalpy > rest mass
# Model:  w = rho c^2 (1 + xi),  xi = p/(rho c^2)
# So A_rel = A * (1 + xi1)(1 + xi2)^{-1}  ... simplified model below
xi_heavy = 0.3   # relativistic parameter for heavy fluid
xi_light = 0.05  # relativistic parameter for light fluid

# ── Figure 1: sigma(k) for various Atwood numbers ────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Left panel: Classical vs Relativistic (inviscid)
ax = axes[0]
for i, A in enumerate(A_values):
    # Classical
    sigma_class = np.sqrt(g * k * A)
    ax.plot(k, sigma_class, "-", color=colors_class[i], linewidth=1.8,
            label=rf"$A = {A}$ (classical)")

    # Relativistic: A_rel < A due to enthalpy contribution
    # Model: heavy fluid has xi_h, light has xi_l
    # rho2/rho1 = (1+A)/(1-A), so A_rel = ((1+xi_l)*rho2 - (1+xi_h)*rho1)/...
    rho_ratio = (1.0 + A) / (1.0 - A)
    w2 = rho_ratio * (1.0 + xi_heavy)
    w1 = 1.0 * (1.0 + xi_light)
    A_rel = (w2 - w1) / (w2 + w1)

    sigma_rel = np.sqrt(g * k * A_rel)
    ax.plot(k, sigma_rel, "--", color=colors_rel[i], linewidth=1.8,
            label=rf"$A_{{rel}} = {A_rel:.2f}$")

ax.set_xlabel(r"Wavenumber $k$")
ax.set_ylabel(r"Growth rate $\sigma$")
ax.set_title("RT growth rate: classical vs relativistic")
ax.legend(loc="upper left", fontsize=8, ncol=2, frameon=True, edgecolor="0.7")
ax.set_xlim(0, 10)
ax.grid(True, linestyle=":", alpha=0.5)

# Right panel: Viscous damping (BDNK first-order)
ax = axes[1]
A_fixed = 0.5
nu_values = [0.0, 0.05, 0.1, 0.2, 0.5]
visc_colors = ["#2ca02c", "#1f77b4", "#ff7f0e", "#d62728", "#9467bd"]

for j, nu in enumerate(nu_values):
    # Dispersion: sigma^2 + nu k^2 sigma - g k A = 0  (quadratic in sigma)
    # sigma = (-nu k^2 + sqrt(nu^2 k^4 + 4 g k A)) / 2
    discriminant = nu**2 * k**4 + 4.0 * g * k * A_fixed
    sigma_visc = (-nu * k**2 + np.sqrt(discriminant)) / 2.0
    label = rf"$\nu = {nu}$" if nu > 0 else r"Inviscid ($\nu = 0$)"
    ax.plot(k, sigma_visc, "-", color=visc_colors[j], linewidth=1.8, label=label)

ax.set_xlabel(r"Wavenumber $k$")
ax.set_ylabel(r"Growth rate $\sigma$")
ax.set_title(r"RT with BDNK viscous damping ($A = 0.5$)")
ax.legend(loc="upper left", frameon=True, edgecolor="0.7")
ax.set_xlim(0, 10)
ax.grid(True, linestyle=":", alpha=0.5)

fig.tight_layout()
fig.savefig("plots/fig_RT_growth.pdf")
fig.savefig("plots/fig_RT_growth.png")
print("Saved  plots/fig_RT_growth.pdf  and  plots/fig_RT_growth.png")
plt.close(fig)
