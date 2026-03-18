#!/usr/bin/env python3
"""
Plot critical Rayleigh number Ra_c vs relativistic parameter xi = p/(eps c^2).

Classical values (two free boundaries):
    Ra_c = 27 pi^4 / 4  ~ 657.5   (free-free)
Rigid-rigid and rigid-free values from Chandrasekhar (1961), Table II.
Relativistic correction:
    Ra_{c,rel} = Ra_c / (1 + xi)

Reference: Chandrasekhar, Hydrodynamic and Hydromagnetic Stability (1961).
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
    "figure.figsize": (7, 5),
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})

# ── Classical critical Rayleigh numbers ───────────────────────────────
Ra_ff = 27.0 * np.pi**4 / 4.0          # free-free   ~ 657.5
Ra_rr = 1707.762                         # rigid-rigid (Chandrasekhar Table II)
Ra_rf = 1100.65                          # rigid-free  (Chandrasekhar Table II)

# ── Relativistic parameter ────────────────────────────────────────────
xi = np.linspace(0, 1, 500)

# ── Relativistic correction:  Ra_{c,rel} = Ra_c / (1 + xi) ──────────
Ra_ff_rel = Ra_ff / (1.0 + xi)
Ra_rr_rel = Ra_rr / (1.0 + xi)
Ra_rf_rel = Ra_rf / (1.0 + xi)

# ── Plot ──────────────────────────────────────────────────────────────
fig, ax = plt.subplots()

ax.plot(xi, Ra_rr_rel, "-",  color="#1f77b4", linewidth=2.0,
        label=r"Rigid-rigid  ($\mathrm{Ra}_{c}^{(0)}=1707.8$)")
ax.plot(xi, Ra_rf_rel, "--", color="#d62728", linewidth=2.0,
        label=r"Rigid-free   ($\mathrm{Ra}_{c}^{(0)}=1100.7$)")
ax.plot(xi, Ra_ff_rel, "-.", color="#2ca02c", linewidth=2.0,
        label=r"Free-free    ($\mathrm{Ra}_{c}^{(0)}=657.5$)")

# Mark the classical values at xi = 0
for Ra_val, marker, color in [(Ra_rr, "s", "#1f77b4"),
                                (Ra_rf, "D", "#d62728"),
                                (Ra_ff, "o", "#2ca02c")]:
    ax.plot(0, Ra_val, marker, color=color, markersize=8, zorder=5)

ax.set_xlabel(r"Relativistic parameter $\xi = p/(\varepsilon\, c^{2})$")
ax.set_ylabel(r"Critical Rayleigh number $\mathrm{Ra}_{c}$")
ax.set_title(r"B\'enard convection: $\mathrm{Ra}_{c}$ vs relativistic parameter")
ax.legend(loc="upper right", frameon=True, edgecolor="0.7")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1900)
ax.grid(True, linestyle=":", alpha=0.5)

fig.tight_layout()
fig.savefig("plots/fig_benard_Ra.pdf")
fig.savefig("plots/fig_benard_Ra.png")
print("Saved  plots/fig_benard_Ra.pdf  and  plots/fig_benard_Ra.png")
plt.close(fig)
