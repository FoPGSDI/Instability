#!/usr/bin/env python3
"""
Jeans mass: classical vs relativistic (general-relativistic correction).

Classical:
    M_J propto c_s^3 / sqrt(G rho)

Relativistic (Tolman-Oppenheimer-Volkoff-type correction):
    In GR, pressure contributes to the gravitational source (active gravitational
    mass includes pressure).  This makes the relativistic Jeans mass SMALLER:

    M_J,rel / M_J = f(p/eps, c_s^2/c^2)

    Leading order:  M_J,rel / M_J ~ 1 - (3/2)(p/eps) * (1 + c_s^2/c^2)

Chandrasekhar's critical adiabatic index:
    gamma_c = 4/3 + K * (G M)/(R c^2)   where K = 38/21 for uniform density

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

# ── Parameters ────────────────────────────────────────────────────────
p_over_eps = np.linspace(0, 1.0/3.0, 500)   # p/eps from 0 to 1/3 (causal limit)

cs2_values = [0.01, 0.05, 0.1, 0.2, 1.0/3.0]  # c_s^2/c^2
colors = ["#2ca02c", "#1f77b4", "#ff7f0e", "#d62728", "#9467bd"]

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# ── Left panel: M_J,rel / M_J vs p/eps ──────────────────────────────
ax = axes[0]
for i, cs2 in enumerate(cs2_values):
    # Leading-order GR correction to Jeans mass
    # Pressure makes gravity stronger => M_J smaller
    ratio = 1.0 - 1.5 * p_over_eps * (1.0 + cs2) - 0.5 * p_over_eps**2
    ratio = np.maximum(ratio, 0.0)   # physical bound

    label = rf"$c_s^2/c^2 = {cs2:.2f}$"
    if cs2 == 1.0/3.0:
        label = r"$c_s^2/c^2 = 1/3$ (conformal)"
    ax.plot(p_over_eps, ratio, "-", color=colors[i], linewidth=2.0, label=label)

ax.axhline(y=1.0, color="k", linestyle="--", linewidth=0.8, alpha=0.5)
ax.set_xlabel(r"$p/\varepsilon$")
ax.set_ylabel(r"$M_{J,{\rm rel}} / M_J$")
ax.set_title("Jeans mass: GR correction")
ax.legend(loc="upper right", frameon=True, edgecolor="0.7")
ax.set_xlim(0, 1.0/3.0)
ax.set_ylim(0, 1.1)
ax.grid(True, linestyle=":", alpha=0.5)
ax.annotate("Pressure destabilises\nin GR", xy=(0.2, 0.4),
            fontsize=11, ha="center", style="italic", color="0.3")

# ── Right panel: Critical adiabatic index threshold ──────────────────
ax = axes[1]
# Compactness parameter: GM/(Rc^2)
compactness = np.linspace(0, 0.5, 500)

# Chandrasekhar limit:  gamma_c = 4/3 + (38/21) * GM/(Rc^2)
gamma_c = 4.0/3.0 + (38.0/21.0) * compactness

# Other estimates from literature
gamma_c_approx = 4.0/3.0 + 2.0 * compactness  # simplified coefficient

ax.plot(compactness, gamma_c, "-", color="#1f77b4", linewidth=2.5,
        label=r"$\gamma_c = 4/3 + (38/21)\,GM/(Rc^2)$")
ax.plot(compactness, gamma_c_approx, "--", color="#d62728", linewidth=1.5,
        label=r"$\gamma_c \approx 4/3 + 2\,GM/(Rc^2)$")

ax.axhline(y=4.0/3.0, color="k", linestyle=":", linewidth=1.0, alpha=0.6,
           label=r"Newtonian $\gamma_c = 4/3$")
ax.axhline(y=5.0/3.0, color="gray", linestyle="-.", linewidth=0.8, alpha=0.5,
           label=r"$\gamma = 5/3$ (non-rel. ideal gas)")

# Typical neutron star compactness
ax.axvline(x=0.2, color="#2ca02c", linestyle="--", linewidth=0.8, alpha=0.6)
ax.annotate("Neutron\nstar", xy=(0.21, 1.55), fontsize=10, color="#2ca02c")

# Black hole limit
ax.axvline(x=0.5, color="k", linestyle="-", linewidth=0.8, alpha=0.4)
ax.annotate("BH limit", xy=(0.42, 1.38), fontsize=10, color="0.3")

ax.set_xlabel(r"Compactness $GM/(Rc^2)$")
ax.set_ylabel(r"Critical adiabatic index $\gamma_c$")
ax.set_title("Chandrasekhar instability threshold")
ax.legend(loc="upper left", frameon=True, edgecolor="0.7", fontsize=10)
ax.set_xlim(0, 0.5)
ax.set_ylim(1.2, 2.2)
ax.grid(True, linestyle=":", alpha=0.5)

fig.tight_layout()
fig.savefig("plots/fig_jeans_mass.pdf")
fig.savefig("plots/fig_jeans_mass.png")
print("Saved  plots/fig_jeans_mass.pdf  and  plots/fig_jeans_mass.png")
plt.close(fig)
