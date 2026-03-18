#!/usr/bin/env python3
"""
Jet capillary breakup: Rayleigh-Plateau timescale for GRB jets.

Computes the relativistic Rayleigh-Plateau capillary instability growth
rate and breakup timescale for gamma-ray burst (GRB) jets as a function
of the enthalpy ratio w/rho = (eps + p)/(rho c^2).

Application: GRB jet breakup into "internal shock" shells; the capillary
timescale sets a minimum variability timescale for prompt GRB emission.

Reference: rel_chapter_12_sec111-112.tex, eqs. (rel-111-dispersion),
           (rel-111-disp-m0), (rel-112-ideal-disp).
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.special import i0, i1, k0, k1

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

# ── Newtonian capillary dispersion: sigma^2 = (T/(rho R^3)) * f(x) ──
def f_capillary(x):
    """f(x) = x I1(x)/I0(x) * (1 - x^2) for axisymmetric mode."""
    if x < 1e-8:
        return 0.0
    if x >= 1.0:
        return (x * i1(x) / i0(x)) * (1.0 - x**2)
    return (x * i1(x) / i0(x)) * (1.0 - x**2)

x_arr = np.linspace(0.001, 1.2, 500)
f_arr = np.array([f_capillary(x) for x in x_arr])

# ── Left panel: growth rate vs enthalpy ratio ─────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
ax = axes[0]

# The relativistic correction: sigma^2 = (T / (w c^2 R^3)) * f(x)
# where w = (eps + p)/c^2 is the enthalpy density
# Ratio to Newtonian: sigma_rel / sigma_N = sqrt(rho / w) = 1/sqrt(w/rho)
# For ultra-rel: w/rho = (eps+p)/(rho c^2) ~ 4/3 * eps/(rho c^2)

# Maximum of f(x) occurs at x ~ 0.697
x_max = 0.697
f_max = f_capillary(x_max)

# Enthalpy ratio w/rho = (eps + p)/(rho c^2)
# Cold: w/rho = 1; hot: w/rho >> 1
w_over_rho = np.linspace(1.0, 20.0, 300)

# sigma_max_rel / sigma_max_N = sqrt(1 / (w/rho))
sigma_ratio = 1.0 / np.sqrt(w_over_rho)

# Breakup timescale ratio: tau_rel / tau_N = sqrt(w/rho)
tau_ratio = np.sqrt(w_over_rho)

ax.plot(w_over_rho, sigma_ratio, "-", color="#d62728", linewidth=2.5,
        label=r"$\sigma_{\max}^{\rm rel} / \sigma_{\max}^{\rm N}$")
ax.plot(w_over_rho, tau_ratio / tau_ratio[-1] * sigma_ratio[-1],
        "--", color="#1f77b4", linewidth=2.0, alpha=0.0)  # invisible spacer

ax2 = ax.twinx()
ax2.plot(w_over_rho, tau_ratio, "--", color="#1f77b4", linewidth=2.0,
         label=r"$\tau_{\rm breakup}^{\rm rel} / \tau_{\rm breakup}^{\rm N}$")

# Mark physical regimes
ax.axvspan(1.0, 1.3, alpha=0.1, color="blue")
ax.annotate("Cold jet\n(baryonic)", xy=(1.15, 0.85), fontsize=9,
            color="#1f77b4", ha="center")

ax.axvspan(1.33, 2.0, alpha=0.1, color="green")
ax.annotate("Warm\n(p~eps/3)", xy=(1.65, 0.65), fontsize=9,
            color="#2ca02c", ha="center")

ax.axvspan(4.0, 10.0, alpha=0.1, color="red")
ax.annotate("GRB fireball\n(radiation\ndominated)", xy=(6.5, 0.5),
            fontsize=9, color="#d62728", ha="center")

ax.axvspan(10.0, 20.0, alpha=0.08, color="purple")
ax.annotate("Pair\nplasma", xy=(14, 0.4), fontsize=9,
            color="#9467bd", ha="center")

ax.set_xlabel(r"Enthalpy ratio $w/\rho = (\varepsilon+p)/(\rho c^2)$")
ax.set_ylabel(r"Growth rate ratio $\sigma_{\rm rel}/\sigma_{\rm N}$", color="#d62728")
ax2.set_ylabel(r"Timescale ratio $\tau_{\rm rel}/\tau_{\rm N}$", color="#1f77b4")
ax.tick_params(axis="y", labelcolor="#d62728")
ax2.tick_params(axis="y", labelcolor="#1f77b4")
ax.set_title("Capillary breakup: relativistic suppression")

lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc="center right",
          frameon=True, edgecolor="0.7")
ax.set_xlim(1, 20)
ax.set_ylim(0, 1.1)
ax2.set_ylim(0, 5)
ax.grid(True, linestyle=":", alpha=0.5)

# ── Right panel: Breakup timescale for GRB jets ──────────────────────
ax = axes[1]

# Physical parameters for GRB jets
# R_jet ~ 10^7 cm (~ 100 km), T ~ effective surface tension from cocoon pressure
# rho ~ 10^{-10} g/cm^3 (fireball), Lorentz factor Gamma ~ 100-300
# Newtonian timescale: tau_N ~ sqrt(rho R^3 / T)
# For a pressure-confined jet: T ~ p_cocoon * R ~ 10^{20} erg/cm

Gamma_arr = np.linspace(10, 500, 300)

# In the jet comoving frame:
# eps ~ Gamma * n * m_p * c^2 (for initially cold jet boosted)
# but internal: eps ~ rho c^2 * (1 + e_int/c^2)
# For a fireball: w/rho ~ Gamma_internal ~ 1 + e_th/(rho c^2)

# Observed timescale = tau_comoving / Gamma (time dilation)
# tau_comoving ~ R/c * sqrt(w/rho) / sqrt(f_max * T/(w c^2 R^3) * R^2/c^2)

# Simplification: just show tau_obs vs Gamma for different internal temperatures
R_jet = 1e7  # cm
c_cgs = 3e10  # cm/s
rho_0 = 1e-10  # g/cm^3

# Effective surface tension from cocoon confinement: T ~ p_ext * R
p_ext = 1e18  # erg/cm^3  (cocoon pressure)
T_surf = p_ext

# Newtonian timescale
tau_N = np.sqrt(rho_0 * R_jet**3 / T_surf)  # seconds

# For different internal enthalpy ratios
w_rho_vals = [1.5, 4.0, 10.0, 50.0]
colors_tau = ["#2ca02c", "#ff7f0e", "#d62728", "#9467bd"]
labels_tau = [r"$w/\rho=1.5$ (warm)", r"$w/\rho=4$ (hot)",
              r"$w/\rho=10$ (fireball)", r"$w/\rho=50$ (pair)"]

for iw, wr in enumerate(w_rho_vals):
    tau_comoving = tau_N * np.sqrt(wr)
    tau_obs = tau_comoving / Gamma_arr * 1e3  # convert to ms
    ax.plot(Gamma_arr, tau_obs, "-", color=colors_tau[iw], linewidth=1.8,
            label=labels_tau[iw])

# Observed GRB variability timescale
ax.axhspan(0.5, 50, alpha=0.08, color="gray")
ax.annotate("Observed GRB\nvariability", xy=(350, 8), fontsize=10,
            color="0.4", ha="center")

ax.set_xlabel(r"Bulk Lorentz factor $\Gamma$")
ax.set_ylabel(r"Observer-frame breakup time [ms]")
ax.set_title("GRB jet capillary breakup timescale")
ax.legend(loc="upper right", frameon=True, edgecolor="0.7", fontsize=9)
ax.set_xlim(10, 500)
ax.set_yscale("log")
ax.set_ylim(0.01, 1e4)
ax.grid(True, linestyle=":", alpha=0.5)

fig.tight_layout()
fig.savefig("plots/ch12/fig_jet_capillary_breakup.pdf")
fig.savefig("plots/ch12/fig_jet_capillary_breakup.png")
print("Saved  plots/ch12/fig_jet_capillary_breakup.pdf  and .png")
plt.close(fig)
