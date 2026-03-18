#!/usr/bin/env python3
"""
Kelvin-Helmholtz critical velocity: classical vs relativistic.

Classical:
    V_crit^2 = (sigma k / rho1 rho2) (rho1 + rho2)
             + g (rho2^2 - rho1^2) / (rho1 rho2 k)
    For pure density contrast (no gravity, no surface tension):
    V_crit^2 ~ sigma_surf * k * (rho1 + rho2)^2 / (rho1 rho2 (rho1 + rho2))

Relativistic correction:
    Lorentz factor gamma^2 enhancement of effective inertia:
    V_crit,rel > V_crit,class  because relativistic inertia stabilises.

    V_crit,rel = V_crit,class * sqrt(1 + V_crit^2/c^2)  (leading order)

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
    "legend.fontsize": 11,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "figure.figsize": (8, 6),
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})

c = 1.0  # speed of light

# ── Density ratio ─────────────────────────────────────────────────────
eta = np.linspace(0.01, 0.99, 500)   # eta = rho1/rho2  (< 1)

# Surface tension parameter: sigma_surf * k  (dimensionless, normalised to rho2 c^2)
Sigma_values = [0.001, 0.01, 0.05, 0.1, 0.2]
colors = ["#2ca02c", "#1f77b4", "#ff7f0e", "#d62728", "#9467bd"]

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# ── Left panel: Classical V_crit/c vs density ratio ──────────────────
ax = axes[0]
for i, Sigma in enumerate(Sigma_values):
    # V_crit^2 / c^2 = Sigma * (1 + eta)^2 / (eta * (1 + eta))
    #                 = Sigma * (1 + eta) / eta
    # (simplified model: dominant k mode, no gravity)
    V2_class = Sigma * (1.0 + eta) / eta
    V_class = np.sqrt(np.minimum(V2_class, 0.999**2))  # cap below c
    ax.plot(eta, V_class, "-", color=colors[i], linewidth=1.8,
            label=rf"$\Sigma = {Sigma}$")

ax.set_xlabel(r"Density ratio $\eta = \rho_1/\rho_2$")
ax.set_ylabel(r"$V_{\rm crit}/c$")
ax.set_title("Classical KH critical velocity")
ax.axhline(y=1.0, color="k", linestyle="--", linewidth=1.0, alpha=0.6, label=r"$v = c$")
ax.legend(loc="upper right", frameon=True, edgecolor="0.7")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.1)
ax.grid(True, linestyle=":", alpha=0.5)

# ── Right panel: Relativistic V_crit/c vs density ratio ──────────────
ax = axes[1]
for i, Sigma in enumerate(Sigma_values):
    V2_class = Sigma * (1.0 + eta) / eta

    # Relativistic: solve V_rel from
    # V_rel^2 * gamma_rel^2 = V_class^2   where gamma = 1/sqrt(1 - V^2/c^2)
    # => V_rel^2 / (1 - V_rel^2) = V_class^2
    # => V_rel^2 = V_class^2 / (1 + V_class^2)
    V2_rel = V2_class / (1.0 + V2_class)
    V_rel = np.sqrt(V2_rel)

    ax.plot(eta, V_rel, "-", color=colors[i], linewidth=1.8,
            label=rf"$\Sigma = {Sigma}$")

    # Also show classical for comparison (thin dashed)
    V_class = np.sqrt(np.minimum(V2_class, 0.999**2))
    ax.plot(eta, V_class, "--", color=colors[i], linewidth=0.8, alpha=0.5)

ax.set_xlabel(r"Density ratio $\eta = \rho_1/\rho_2$")
ax.set_ylabel(r"$V_{\rm crit}/c$")
ax.set_title(r"Relativistic KH critical velocity ($\gamma^2$ correction)")
ax.axhline(y=1.0, color="k", linestyle="--", linewidth=1.0, alpha=0.6, label=r"$v = c$ (causal bound)")
ax.legend(loc="upper right", frameon=True, edgecolor="0.7",
          title="Solid = rel., dashed = class.")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.1)
ax.grid(True, linestyle=":", alpha=0.5)

fig.tight_layout()
fig.savefig("plots/fig_KH_critical.pdf")
fig.savefig("plots/fig_KH_critical.png")
print("Saved  plots/fig_KH_critical.pdf  and  plots/fig_KH_critical.png")
plt.close(fig)
