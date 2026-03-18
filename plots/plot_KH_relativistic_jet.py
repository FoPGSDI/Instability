#!/usr/bin/env python3
"""
Kelvin-Helmholtz instability for relativistic jets.

The KH growth rate for a shear layer around a relativistic jet is suppressed
at high Lorentz factor:

    sigma / sigma_0 ~ Gamma_jet^{-2}

for the fundamental body mode in the ultrarelativistic limit.  For moderate
Lorentz factors, the full dispersion relation gives an intermediate behaviour.

Model dispersion (simplified):
    sigma(k) = sigma_0 * k / (1 + k^2 L^2) * Gamma^{-2} * (1 + alpha / Gamma)

where L is the shear layer width and alpha captures the transition from
non-relativistic to ultrarelativistic regimes.

Reference: Hardee (2007), Perucho et al. (2010), and Ch X-XIV of monograph.
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
k = np.linspace(0.01, 5, 500)   # wavenumber (normalised to jet radius)
L = 0.2                          # shear layer width / jet radius
sigma_0 = 1.0                    # normalisation

Gamma_values = [1, 2, 5, 10, 100]
colors = ["#2ca02c", "#1f77b4", "#ff7f0e", "#d62728", "#9467bd"]
styles = ["-", "-", "-", "-", "-"]

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# ── Left panel: Growth rate vs wavenumber for various Gamma ──────────
ax = axes[0]
for i, Gamma in enumerate(Gamma_values):
    beta = np.sqrt(1.0 - 1.0 / Gamma**2) if Gamma > 1 else 0.0
    # Growth rate: peaked function of k, suppressed by Gamma^{-2}
    sigma = sigma_0 * k / (1.0 + k**2 * L**2) / Gamma**2
    ax.plot(k, sigma, styles[i], color=colors[i], linewidth=2.0,
            label=rf"$\Gamma = {Gamma}$")

ax.set_xlabel(r"Wavenumber $kR_{\rm jet}$")
ax.set_ylabel(r"Growth rate $\sigma / \sigma_0$")
ax.set_title("KH growth rate for relativistic jets")
ax.legend(loc="upper right", frameon=True, edgecolor="0.7")
ax.set_xlim(0, 5)
ax.grid(True, linestyle=":", alpha=0.5)

# ── Right panel: Peak growth rate vs Gamma ───────────────────────────
ax = axes[1]
Gamma_arr = np.logspace(0, 2.5, 200)  # 1 to ~316

# Peak growth rate: max_k [k / (1 + k^2 L^2)] = 1/(2L) at k = 1/L
sigma_peak_0 = sigma_0 / (2.0 * L)
sigma_peak = sigma_peak_0 / Gamma_arr**2

# Reference power law
ax.loglog(Gamma_arr, sigma_peak, "-", color="#1f77b4", linewidth=2.5,
          label=r"$\sigma_{\rm peak} \propto \Gamma^{-2}$")

# Mark specific Gamma values
for i, Gamma in enumerate(Gamma_values):
    sp = sigma_peak_0 / Gamma**2
    ax.plot(Gamma, sp, "o", color=colors[i], markersize=10, zorder=5,
            markeredgecolor="k", markeredgewidth=0.5)
    ax.annotate(rf"$\Gamma={Gamma}$", (Gamma, sp),
                textcoords="offset points", xytext=(8, 5), fontsize=9)

# Reference line: Gamma^{-2}
Gamma_ref = np.array([1, 300])
ax.loglog(Gamma_ref, sigma_peak_0 * Gamma_ref**(-2.0), ":",
          color="gray", linewidth=1.0, alpha=0.7)

ax.set_xlabel(r"Jet Lorentz factor $\Gamma_{\rm jet}$")
ax.set_ylabel(r"Peak growth rate $\sigma_{\rm peak} / \sigma_0$")
ax.set_title(r"KH suppression: $\sigma \propto \Gamma^{-2}$")
ax.legend(loc="upper right", frameon=True, edgecolor="0.7")
ax.grid(True, linestyle=":", alpha=0.5, which="both")

fig.tight_layout()
fig.savefig("plots/fig_KH_jet.pdf")
fig.savefig("plots/fig_KH_jet.png")
print("Saved  plots/fig_KH_jet.pdf  and  plots/fig_KH_jet.png")
plt.close(fig)
