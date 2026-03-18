#!/usr/bin/env python3
"""
Plot critical Rayleigh number Ra_c vs Taylor number Ta for rotating
convection, comparing classical and relativistic cases.

Asymptotic laws (Chandrasekhar 1961):
  - Stationary convection:  Ra ~ (pi^2 / 6^{1/3}) Ta^{2/3}   (large Ta)
  - Overstable convection:  Ra ~ 3 (pi^2 Ta)^{1/3}            (large Ta)

Relativistic correction (BDNK framework):
  - Effective Taylor number:  Ta_rel = Ta / (1 + xi)^2
  - Effective Rayleigh number: Ra_rel = Ra / (1 + xi)
  where xi = p / (eps c^2).
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({
    "text.usetex": False,
    "font.family": "serif",
    "font.size": 12,
    "axes.labelsize": 14,
    "axes.titlesize": 14,
    "legend.fontsize": 10,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "figure.figsize": (7, 5),
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})

# ── Classical critical Ra(Ta) via asymptotic formulae ─────────────────
Ta = np.logspace(0, 10, 600)

# Stationary branch: Ra ~ (pi^2 / 6^{1/3}) Ta^{2/3}  (+  low-Ta offset)
Ra_stat_class = (np.pi**2 / 6.0**(1.0/3.0)) * Ta**(2.0/3.0) + 657.5

# Overstable branch: Ra ~ 3 (pi^2 Ta)^{1/3}  (+  low-Ta offset)
Ra_over_class = 3.0 * (np.pi**2 * Ta)**(1.0/3.0) + 657.5

# ── Relativistic curves for various xi ────────────────────────────────
xi_values = [0.0, 0.1, 0.33]
colors_stat = ["#1f77b4", "#ff7f0e", "#d62728"]
colors_over = ["#1f77b4", "#ff7f0e", "#d62728"]

fig, ax = plt.subplots()

for i, xi in enumerate(xi_values):
    factor = 1.0 + xi
    # Effective Taylor number seen by the fluid
    Ta_eff = Ta / factor**2
    # Critical Ra in the relativistic case
    Ra_stat_rel = ((np.pi**2 / 6.0**(1.0/3.0)) * Ta_eff**(2.0/3.0) + 657.5) / factor
    Ra_over_rel = (3.0 * (np.pi**2 * Ta_eff)**(1.0/3.0) + 657.5) / factor

    lbl_s = rf"Stationary, $\xi={xi}$"
    lbl_o = rf"Overstable, $\xi={xi}$"
    ls = "-" if xi == 0 else ("--" if xi == 0.1 else "-.")

    ax.loglog(Ta, Ra_stat_rel, ls, color=colors_stat[i], linewidth=1.8,
              label=lbl_s)
    ax.loglog(Ta, Ra_over_rel, ls, color=colors_over[i], linewidth=1.2,
              alpha=0.7, label=lbl_o)

# Reference slopes
ax.loglog([1e7, 1e10], [3e3, 3e3 * (1e10/1e7)**(2.0/3.0)],
          ":", color="gray", linewidth=1, label=r"$\sim\mathrm{Ta}^{2/3}$")
ax.loglog([1e7, 1e10], [1e3, 1e3 * (1e10/1e7)**(1.0/3.0)],
          ":", color="silver", linewidth=1, label=r"$\sim\mathrm{Ta}^{1/3}$")

ax.set_xlabel(r"Taylor number $\mathrm{Ta}$")
ax.set_ylabel(r"Critical Rayleigh number $\mathrm{Ra}_{c}$")
ax.set_title("Rotating convection: classical vs relativistic")
ax.legend(loc="upper left", fontsize=8, ncol=2, frameon=True, edgecolor="0.7")
ax.set_xlim(1, 1e10)
ax.set_ylim(1e2, 1e8)
ax.grid(True, which="both", linestyle=":", alpha=0.35)

fig.tight_layout()
fig.savefig("plots/fig_rotation_Ra_Ta.pdf")
fig.savefig("plots/fig_rotation_Ra_Ta.png")
print("Saved  plots/fig_rotation_Ra_Ta.pdf  and  plots/fig_rotation_Ra_Ta.png")
plt.close(fig)
