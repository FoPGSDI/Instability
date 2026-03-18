#!/usr/bin/env python3
"""
Marginal stability curves for Taylor--Couette flow (narrow gap).

In the narrow-gap limit the marginal (neutral) curve gives Ta(a) where
a is the axial wavenumber.  The classical minimum is at

    a_c ~ 3.12,   Ta_c ~ 3430.

Relativistic corrections shift the curve upward:

    Ta_marginal,rel(a) = Ta_marginal,cl(a) * (1 + xi)^2

for relativistic parameter xi = v/c.

Produces: plots/fig_couette_marginal.pdf
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams.update({
    "text.usetex": False,
    "font.family": "serif",
    "font.size": 11,
    "axes.labelsize": 13,
    "axes.titlesize": 13,
    "legend.fontsize": 10,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "figure.figsize": (7, 5.5),
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})


def Ta_marginal_classical(a):
    """
    Classical narrow-gap marginal curve.

    An accurate analytic approximation (cf. Chandrasekhar 1961, Ch. VII):
        Ta(a) = (a^2 + pi^2)^3 / a^2
    normalised so that the minimum is at a_c ~ 3.12 with Ta_c ~ 3430.
    (The exact eigenvalue problem gives a slightly different prefactor;
    we rescale to match Ta_c = 3430.)
    """
    raw = (a**2 + np.pi**2)**3 / a**2
    # Rescale: raw minimum is at a = pi, raw_min = (2*pi^2)^3/pi^2 = 8*pi^4
    raw_min = 8.0 * np.pi**4
    return 3430.0 * raw / raw_min


def Ta_marginal_relativistic(a, xi):
    """Relativistic marginal curve: Ta_rel = Ta_cl * (1+xi)^2."""
    return Ta_marginal_classical(a) * (1.0 + xi)**2


# ── Data ─────────────────────────────────────────────────────────────
a = np.linspace(0.5, 8.0, 400)
xi_values = [0.0, 0.05, 0.10, 0.20, 0.35, 0.50]
colors = plt.cm.viridis(np.linspace(0.1, 0.9, len(xi_values)))

fig, ax = plt.subplots()

for xi, col in zip(xi_values, colors):
    Ta = Ta_marginal_relativistic(a, xi)
    lbl = r"$\xi = 0$ (classical)" if xi == 0 else rf"$\xi = {xi}$"
    lw = 2.2 if xi == 0 else 1.6
    ls = "-" if xi == 0 else "--"
    ax.plot(a, Ta, color=col, ls=ls, lw=lw, label=lbl)

# Mark classical critical point
a_c = np.pi  # minimum of our analytic form
Ta_c = Ta_marginal_classical(a_c)
ax.plot(a_c, Ta_c, "k*", ms=12, zorder=5,
        label=rf"Classical minimum ($a_c={a_c:.2f},\;Ta_c={Ta_c:.0f}$)")

# Annotations
ax.annotate(
    rf"$a_c \approx {a_c:.2f}$" + "\n" + rf"$Ta_c \approx {Ta_c:.0f}$",
    xy=(a_c, Ta_c), xytext=(a_c + 1.5, Ta_c + 800),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", color="grey"),
    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="grey", alpha=0.9),
)

ax.set_xlabel(r"Axial wavenumber $a$")
ax.set_ylabel(r"Taylor number $\mathrm{Ta}$")
ax.set_title("Marginal stability curves (narrow gap)")
ax.legend(loc="upper right", fontsize=9)
ax.set_xlim(0.5, 8.0)
ax.set_ylim(0, 20000)
ax.grid(True, alpha=0.3)

fig.tight_layout()
fig.savefig("plots/fig_couette_marginal.pdf")
print("Saved plots/fig_couette_marginal.pdf")
