#!/usr/bin/env python3
"""
Summary plot: all characteristic speeds bounded by the speed of light.

Characteristic speeds in relativistic MHD:
    - Sound speed:        c_s = sqrt(dp/depsilon)
    - Alfven speed:       v_A = B / sqrt(w mu_0 + B^2)   (relativistic)
    - Fast magnetosonic:  v_f^2 = c_s^2 + v_A^2 - c_s^2 v_A^2/c^2
    - Slow magnetosonic:  v_s^2 = c_s^2 v_A^2 / (c_s^2 + v_A^2 - c_s^2 v_A^2/c^2)

All speeds satisfy v <= c  (causal propagation).

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

# ── Parameters ────────────────────────────────────────────────────────
# Magnetic field strength parameter: sigma_B = B^2 / (w mu_0)
# where w = enthalpy density.  Range from 0 (hydro) to large (magnetically dominated).
sigma_B = np.linspace(0, 50, 1000)

# Sound speed: fixed for a given EOS.  Choose a few representative values.
cs2_values = [0.05, 1.0/6.0, 1.0/3.0]
cs_labels  = [r"$c_s^2/c^2 = 0.05$", r"$c_s^2/c^2 = 1/6$",
              r"$c_s^2/c^2 = 1/3$ (conformal)"]
color_sets = [("#a1d99b", "#31a354", "#006d2c"),    # greens
              ("#9ecae1", "#3182bd", "#08519c"),    # blues
              ("#fcbba1", "#e6550d", "#a63603")]    # oranges

fig, ax = plt.subplots(figsize=(9, 6))

for j, cs2 in enumerate(cs2_values):
    # Relativistic Alfven speed:  v_A^2 = sigma_B / (1 + sigma_B)
    vA2 = sigma_B / (1.0 + sigma_B)

    # Fast magnetosonic: v_f^2 = cs2 + vA2 - cs2 * vA2   (in c=1 units)
    vf2 = cs2 + vA2 - cs2 * vA2

    # Slow magnetosonic: v_s^2 = cs2 * vA2 / v_f^2
    vs2 = cs2 * vA2 / vf2

    c1, c2, c3 = color_sets[j]

    if j == 0:
        # Plot Alfven speed only once (same for all cs2)
        ax.plot(sigma_B, np.sqrt(vA2), "-.", color="0.4", linewidth=1.5,
                label=r"$v_A/c$ (Alfv\'en)", zorder=3)

    ax.plot(sigma_B, np.sqrt(vf2), "-", color=c3, linewidth=2.0,
            label=rf"$v_f/c$ ({cs_labels[j]})")
    ax.plot(sigma_B, np.sqrt(vs2), "--", color=c1, linewidth=1.5,
            label=rf"$v_s/c$ ({cs_labels[j]})")
    ax.plot(sigma_B, np.full_like(sigma_B, np.sqrt(cs2)), ":",
            color=c2, linewidth=1.0, alpha=0.5)

# Causal bound
ax.axhline(y=1.0, color="k", linestyle="--", linewidth=2.0, alpha=0.8,
           label=r"$v = c$ (causal limit)")

ax.set_xlabel(r"Magnetisation $\sigma_B = B^2/(\mu_0 w)$")
ax.set_ylabel(r"Characteristic speed $/\, c$")
ax.set_title("Characteristic speeds: all bounded by $c$")
ax.legend(loc="center right", frameon=True, edgecolor="0.7", fontsize=9)
ax.set_xlim(0, 50)
ax.set_ylim(0, 1.15)
ax.grid(True, linestyle=":", alpha=0.5)

# Annotate the causal region
ax.fill_between(sigma_B, 1.0, 1.15, color="red", alpha=0.05)
ax.annotate("Superluminal\n(forbidden)", xy=(25, 1.07),
            fontsize=11, ha="center", color="red", alpha=0.6, weight="bold")

fig.tight_layout()
fig.savefig("plots/fig_causality_speeds.pdf")
fig.savefig("plots/fig_causality_speeds.png")
print("Saved  plots/fig_causality_speeds.pdf  and  plots/fig_causality_speeds.png")
plt.close(fig)
