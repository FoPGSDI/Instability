#!/usr/bin/env python3
"""
Z-pinch in magnetar flares: Kruskal-Shafranov critical B.

Computes the relativistic Kruskal-Shafranov stability boundary for the
kink (m=-1) mode of a Z-pinch, showing how the critical ratio
B_z/B_phi depends on the bulk Lorentz factor.

Application: magnetar giant flares produce relativistic plasma columns
(fireballs confined by the dipolar field) where kink stability determines
whether the trapped fireball can expand coherently or fragments via
current-driven instabilities.

Reference: rel_chapter_12_sec113-115.tex, eqs. (rel-115-KS),
           (rel-115-DR), (rel-115-stab-crit).
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
    "figure.figsize": (14, 6),
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})

# ── Left panel: Kruskal-Shafranov critical ratio vs Lorentz factor ────
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
ax = axes[0]

# Relativistic KS criterion (eq. rel-115-KS):
# B_z / B_phi > kR / (1 + Gamma^2 V^2 / (2 c^2))
# For the most dangerous mode kR ~ 1 (longest wavelength fitting in the column)
# V/c = sqrt(1 - 1/Gamma^2)

Gamma_arr = np.linspace(1.0, 30.0, 500)
V_over_c = np.sqrt(1.0 - 1.0 / Gamma_arr**2)

# Different kR values (axial wavenumber * radius)
kR_vals = [0.5, 1.0, 2.0, 3.0]
colors_kR = ["#2ca02c", "#1f77b4", "#ff7f0e", "#d62728"]

for ikR, kR in enumerate(kR_vals):
    # Classical KS: B_z/B_phi > kR
    # Relativistic: B_z/B_phi > kR / (1 + Gamma^2 V^2 / (2 c^2))
    denom = 1.0 + Gamma_arr**2 * V_over_c**2 / 2.0
    critical_ratio = kR / denom
    ax.plot(Gamma_arr, critical_ratio, "-", color=colors_kR[ikR],
            linewidth=2.0, label=rf"$kR_1 = {kR}$")
    # Classical limit (horizontal dashed)
    ax.axhline(y=kR, color=colors_kR[ikR], linestyle=":", linewidth=0.8,
               alpha=0.4)

ax.set_xlabel(r"Bulk Lorentz factor $\Gamma$")
ax.set_ylabel(r"Critical $B_{z,\mathrm{int}} / B_\varphi(R_1)$")
ax.set_title("Relativistic Kruskal-Shafranov criterion")
ax.legend(loc="upper right", frameon=True, edgecolor="0.7")
ax.set_xlim(1, 30)
ax.set_ylim(0, 3.5)
ax.set_yscale("linear")
ax.grid(True, linestyle=":", alpha=0.5)

ax.annotate("Classical KS\n(dotted lines)", xy=(20, 2.5), fontsize=10,
            color="0.4", ha="center")
ax.annotate(r"Relativistic $\Gamma$ stabilises $\rightarrow$",
            xy=(8, 0.15), fontsize=10, color="0.3", ha="center")

# ── Right panel: Magnetar flare application ───────────────────────────
ax = axes[1]

# Magnetar surface field: B ~ 10^{14} - 10^{15} G
# Flare fireball: R ~ 10^6 cm, Gamma ~ 1-100 (mildly to highly relativistic)
# Internal B_z from the dipole: B_z ~ B_surface * (R_NS / R)^3

# B_surface in units of 10^15 G
B_surface_15 = np.array([0.1, 0.3, 1.0, 3.0, 10.0])

# Fireball radius in units of R_NS = 10 km
r_over_rns = np.linspace(1.0, 50.0, 300)

# B_z at radius r: dipole falloff
# B_z(r) ~ B_surface * (R_NS / r)^3
# B_phi at surface of flux tube (from current): B_phi ~ B_surface * (R_NS / r)

# The ratio B_z / B_phi ~ (R_NS / r)^2 for a twisted dipole
bz_over_bphi = 1.0 / r_over_rns**2  # simplified dipole ratio at fireball surface

# For the m=-1 kink mode with kR = 1, classical KS requires B_z/B_phi > 1
# Relativistic: need B_z/B_phi > 1 / (1 + Gamma^2/2)

Gamma_flare = [1.0, 2.0, 5.0, 10.0, 30.0]
colors_G = ["#1f77b4", "#2ca02c", "#ff7f0e", "#d62728", "#9467bd"]

for ig, Gf in enumerate(Gamma_flare):
    Vf = np.sqrt(1.0 - 1.0 / Gf**2) if Gf > 1 else 0.0
    crit = 1.0 / (1.0 + Gf**2 * Vf**2 / 2.0)

    # Find where B_z/B_phi = crit  =>  1/r^2 = crit  =>  r = 1/sqrt(crit)
    r_stable_max = 1.0 / np.sqrt(crit) if crit > 0 else 50.0

    ax.axhline(y=crit, color=colors_G[ig], linestyle="--", linewidth=1.0,
               alpha=0.6)
    ax.annotate(rf"$\Gamma={Gf:.0f}$", xy=(48, crit * 1.05),
                fontsize=9, color=colors_G[ig], ha="right")

# Plot the dipole B_z/B_phi ratio
ax.plot(r_over_rns, bz_over_bphi, "-", color="black", linewidth=2.5,
        label=r"$B_z/B_\varphi \propto (R_{\rm NS}/r)^2$")

ax.fill_between(r_over_rns, bz_over_bphi, 2.0,
                where=(bz_over_bphi < 2.0), alpha=0.08, color="red",
                label="Kink unstable (classical)")

ax.set_xlabel(r"Fireball radius $r / R_{\rm NS}$")
ax.set_ylabel(r"$B_z / B_\varphi$")
ax.set_title("Magnetar flare: kink stability of trapped fireball")
ax.legend(loc="upper right", frameon=True, edgecolor="0.7", fontsize=9)
ax.set_xlim(1, 50)
ax.set_ylim(0, 1.2)
ax.set_yscale("linear")
ax.grid(True, linestyle=":", alpha=0.5)

ax.annotate("Stable\n(strong B_z)", xy=(3, 0.8), fontsize=11,
            color="#2ca02c", ha="center", style="italic")
ax.annotate("Unstable\n(kink)", xy=(20, 0.15), fontsize=11,
            color="#d62728", ha="center", style="italic")

fig.tight_layout()
fig.savefig("plots/ch12/fig_zpinch_magnetar.pdf")
fig.savefig("plots/ch12/fig_zpinch_magnetar.png")
print("Saved  plots/ch12/fig_zpinch_magnetar.pdf  and .png")
plt.close(fig)
