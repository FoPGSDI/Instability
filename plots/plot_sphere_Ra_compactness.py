#!/usr/bin/env python3
"""
Plot critical Rayleigh number Ra_c vs stellar compactness C = GM/(Rc^2)
for convection onset in a self-gravitating sphere.

Newtonian limit (C -> 0):
    Ra_c ~ 3091  (l=1 mode, rigid boundaries, Chandrasekhar approximation)

General-relativistic correction (Tolman-Oppenheimer-Volkoff background):
    Ra_{c,rel}(C) = Ra_c^{(N)} * f(C)
where
    f(C) = (1 - 2C)^{-1/2} / (1 + xi(C))
accounts for:
  - Metric (redshift) factor (1 - 2C)^{-1/2}
  - Relativistic enthalpy correction 1/(1 + xi)
  - xi grows roughly as 3C for moderate equations of state

The plot shows that Ra_c first decreases (enthalpy softening) then
increases sharply near the Buchdahl limit C -> 4/9.
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
    "legend.fontsize": 11,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "figure.figsize": (7, 5),
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})

# ── Compactness range ─────────────────────────────────────────────────
C = np.linspace(0, 0.43, 800)   # up to near Buchdahl limit 4/9 ~ 0.444

# Newtonian critical Ra (l = 1 mode, rigid sphere)
Ra_N = 3091.0

# ── Relativistic correction factor ────────────────────────────────────
# Model: xi(C) = alpha * C   with alpha ~ 3 for a polytropic EOS
# f(C) = (1 - 2C)^{-1/2} / (1 + alpha C)

alphas = [1.0, 3.0, 6.0]
labels = [
    r"Stiff EOS ($\alpha=1$)",
    r"Moderate EOS ($\alpha=3$)",
    r"Soft EOS ($\alpha=6$)",
]
colors = ["#2ca02c", "#1f77b4", "#d62728"]
styles = ["-.", "-", "--"]

fig, ax = plt.subplots()

# Newtonian baseline
ax.axhline(Ra_N, color="gray", linestyle=":", linewidth=1.2,
           label=r"Newtonian $\mathrm{Ra}_{c}^{(N)}=3091$")

for alpha, lbl, col, ls in zip(alphas, labels, colors, styles):
    xi_C = alpha * C
    f_C = 1.0 / (np.sqrt(1.0 - 2.0 * C) * (1.0 + xi_C))
    Ra_rel = Ra_N * f_C
    ax.plot(C, Ra_rel, ls, color=col, linewidth=2.0, label=lbl)

# Mark Buchdahl limit
ax.axvline(4.0/9.0, color="k", linestyle="--", linewidth=0.8, alpha=0.5)
ax.text(4.0/9.0 - 0.015, 500, "Buchdahl\nlimit", fontsize=9,
        ha="right", va="bottom", color="0.3")

# Neutron-star compactness band
ax.axvspan(0.1, 0.25, alpha=0.08, color="blue")
ax.text(0.175, 400, "Neutron\nstars", fontsize=9, ha="center",
        va="bottom", color="#1f77b4", style="italic")

ax.set_xlabel(r"Compactness $\mathcal{C} = GM/(Rc^{2})$")
ax.set_ylabel(r"Critical Rayleigh number $\mathrm{Ra}_{c}$")
ax.set_title("Spherical convection onset vs compactness")
ax.legend(loc="upper left", frameon=True, edgecolor="0.7")
ax.set_xlim(0, 0.44)
ax.set_ylim(0, 12000)
ax.grid(True, linestyle=":", alpha=0.4)

fig.tight_layout()
fig.savefig("plots/fig_sphere_Ra.pdf")
fig.savefig("plots/fig_sphere_Ra.png")
print("Saved  plots/fig_sphere_Ra.pdf  and  plots/fig_sphere_Ra.png")
plt.close(fig)
