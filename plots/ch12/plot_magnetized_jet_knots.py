#!/usr/bin/env python3
"""
Magnetized jet knots: B-field vs fragmentation wavelength.

Computes the critical wavenumber x_a and maximum growth rate as functions
of the axial magnetic field strength H/H_{0,rel} for a relativistic
self-gravitating cylinder with axial B-field.

Application: knot spacing in AGN jets (M87, 3C 273) interpreted as
gravitational fragmentation modulated by the axial magnetic field.

Reference: rel_chapter_12_sec110.tex, eqs. (rel-12-110-17)--(rel-12-110-24).
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.special import i0, i1, k0, k1
from scipy.optimize import brentq

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

# ── Dispersion relation functions ─────────────────────────────────────

def grav_term(x):
    """Gravitational part: x I1(x)/I0(x) * [K0(x) I0(x) - 1/2]."""
    if x < 1e-8:
        return 0.0
    return (x * i1(x) / i0(x)) * (k0(x) * i0(x) - 0.5)

def mag_term(x):
    """Magnetic stabilizing part: x^2 I1(x) K0(x) / (I0(x) K1(x))."""
    if x < 1e-8:
        return 0.0
    return x**2 * i1(x) * k0(x) / (i0(x) * k1(x))

def sigma2_magnetized(x, H_ratio):
    """sigma^2 / (4 pi G rho_G) for magnetized cylinder."""
    return grav_term(x) - H_ratio**2 * mag_term(x)


# ── Left panel: Dispersion curves for different B-field strengths ─────
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
ax = axes[0]

x_arr = np.linspace(0.001, 1.2, 500)
H_ratios = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
colors_disp = ["#1f77b4", "#2ca02c", "#ff7f0e", "#d62728", "#9467bd", "#8c564b"]

for ih, Hr in enumerate(H_ratios):
    s2 = np.array([sigma2_magnetized(x, Hr) for x in x_arr])
    ax.plot(x_arr, s2, "-", color=colors_disp[ih], linewidth=1.8,
            label=rf"$H/H_{{0,\mathrm{{rel}}}} = {Hr}$")

ax.axhline(y=0, color="k", linewidth=0.5)
ax.set_xlabel(r"$x = kR$")
ax.set_ylabel(r"$\sigma^2 / (4\pi G\rho_G)$")
ax.set_title("Dispersion relation: axial B-field effect")
ax.legend(loc="upper left", frameon=True, edgecolor="0.7", fontsize=9)
ax.set_xlim(0, 1.2)
ax.set_ylim(-0.04, 0.12)
ax.grid(True, linestyle=":", alpha=0.5)

# ── Right panel: Critical x_a and sigma_max vs H/H0 ──────────────────
ax = axes[1]

H_range = np.linspace(0.01, 2.0, 200)
x_a_vals = []
sigma_max_vals = []

for Hr in H_range:
    # Find critical x_a where sigma^2 = 0
    # For small H, x_a is near 1.0668; for large H, it decreases exponentially
    # Use strong-field asymptotic: x_a ~ 0.6811 exp(-2 (H/H0)^2)
    x_a_approx = 0.6811 * np.exp(-2.0 * Hr**2)

    # More precisely, find root of sigma2 = 0
    try:
        def f_root(x):
            return sigma2_magnetized(x, Hr)
        # Search near the approx
        x_lo = max(x_a_approx * 0.5, 1e-6)
        x_hi = min(1.0668, x_a_approx * 2.0 + 0.1)
        x_a = brentq(f_root, x_lo, x_hi)
    except (ValueError, RuntimeError):
        x_a = x_a_approx
    x_a_vals.append(x_a)

    # Find maximum growth rate
    x_test = np.linspace(0.001, max(x_a - 0.001, 0.002), 300)
    s2_test = np.array([sigma2_magnetized(x, Hr) for x in x_test])
    sigma_max_vals.append(np.sqrt(max(np.max(s2_test), 0.0)))

x_a_vals = np.array(x_a_vals)
sigma_max_vals = np.array(sigma_max_vals)

# Fragmentation wavelength = 2 pi R / x_a  (in units of R)
lambda_frag = 2 * np.pi / np.maximum(x_a_vals, 1e-6)

color1 = "#d62728"
color2 = "#1f77b4"

ax.plot(H_range, lambda_frag / (2 * np.pi), "-", color=color1, linewidth=2.5,
        label=r"$\lambda_{\min}/(2\pi R)$")

ax2 = ax.twinx()
ax2.plot(H_range, sigma_max_vals, "--", color=color2, linewidth=2.0,
         label=r"$\sigma_{\max}/\sqrt{4\pi G\rho_G}$")

# Mark astrophysical jet regimes
ax.axvspan(0.3, 0.7, alpha=0.08, color="green")
ax.annotate("M87-like\njets", xy=(0.5, 3.5), fontsize=10, color="#2ca02c",
            ha="center")

ax.axvspan(1.0, 1.5, alpha=0.08, color="orange")
ax.annotate("Cygnus A\n(smooth)", xy=(1.25, 6), fontsize=10, color="#ff7f0e",
            ha="center")

ax.set_xlabel(r"$H / H_{0,\mathrm{rel}}$")
ax.set_ylabel(r"$\lambda_{\min} / (2\pi R)$", color=color1)
ax2.set_ylabel(r"$\sigma_{\max} / \sqrt{4\pi G\rho_G}$", color=color2)
ax.tick_params(axis="y", labelcolor=color1)
ax2.tick_params(axis="y", labelcolor=color2)
ax.set_title("Fragmentation scale vs axial B-field")
ax.set_xlim(0, 2.0)
ax.set_ylim(0.9, 50)
ax.set_yscale("log")
ax2.set_ylim(0, 0.35)

# Combine legends
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc="upper left",
          frameon=True, edgecolor="0.7", fontsize=10)
ax.grid(True, linestyle=":", alpha=0.5)

fig.tight_layout()
fig.savefig("plots/ch12/fig_magnetized_jet_knots.pdf")
fig.savefig("plots/ch12/fig_magnetized_jet_knots.png")
print("Saved  plots/ch12/fig_magnetized_jet_knots.pdf  and .png")
plt.close(fig)
