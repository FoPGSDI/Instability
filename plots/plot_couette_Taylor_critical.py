#!/usr/bin/env python3
"""
Critical Taylor number vs gap ratio eta and relativistic parameter xi.

Ta_rel = Ta_classical * (1 + xi)^2, where xi = v/c characterises the
relativistic correction.  The classical critical Taylor number for
co-rotating cylinders depends on the radius ratio eta = R_inner/R_outer.

Reference values (narrow-gap limit): Ta_c ~ 3430 (eta -> 1).

Produces: plots/fig_couette_Taylor.pdf
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import rcParams

# ── Publication styling ──────────────────────────────────────────────
rcParams.update({
    "text.usetex": False,
    "font.family": "serif",
    "font.size": 11,
    "axes.labelsize": 13,
    "axes.titlesize": 13,
    "legend.fontsize": 10,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "figure.figsize": (7, 5),
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})

# ── Classical critical Taylor number vs eta ──────────────────────────
# Approximate analytic fit (Esser & Grossmann 1996-style):
#   Ta_c(eta) ~ 3430 * f(eta)
# where f(eta) -> 1 as eta -> 1 (narrow gap) and grows for wider gaps.
# A convenient rational approximation:
#   f(eta) = (1 + eta) / (2 * eta)  (captures leading-order trend)

def Ta_critical_classical(eta):
    """Classical critical Taylor number as a function of radius ratio."""
    # Narrow-gap value 3430; widen correction factor
    f = (1.0 + eta) / (2.0 * eta)
    return 3430.0 * f


def Ta_critical_relativistic(eta, xi):
    """Relativistic critical Taylor number: Ta_rel = Ta_cl * (1+xi)^2."""
    return Ta_critical_classical(eta) * (1.0 + xi) ** 2


# ── Data ─────────────────────────────────────────────────────────────
xi_vals = np.linspace(0.0, 0.5, 200)
etas = [0.5, 0.8, 0.95]
colors = ["#1b9e77", "#d95f02", "#7570b3"]
linestyles = ["-", "--", "-."]

fig, ax = plt.subplots()

for eta, col, ls in zip(etas, colors, linestyles):
    Ta = Ta_critical_relativistic(eta, xi_vals)
    ax.plot(xi_vals, Ta, color=col, ls=ls, lw=2.0,
            label=rf"$\eta = {eta}$")

# Mark classical values at xi = 0
for eta, col in zip(etas, colors):
    ax.plot(0.0, Ta_critical_classical(eta), "o", color=col, ms=6,
            zorder=5)

ax.set_xlabel(r"Relativistic parameter $\xi = v/c$")
ax.set_ylabel(r"Critical Taylor number $\mathrm{Ta}_c$")
ax.set_title("Relativistic stabilisation of Taylor--Couette flow")
ax.legend(title=r"Radius ratio $\eta$", loc="upper left")
ax.set_xlim(0, 0.5)
ax.set_ylim(bottom=0)
ax.grid(True, alpha=0.3)

fig.tight_layout()
fig.savefig("plots/fig_couette_Taylor.pdf")
print("Saved plots/fig_couette_Taylor.pdf")
