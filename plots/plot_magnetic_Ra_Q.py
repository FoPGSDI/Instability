#!/usr/bin/env python3
"""
Plot critical Rayleigh number Ra_c vs Chandrasekhar number Q for
magneto-convection, comparing classical and relativistic cases.

Classical result (Chandrasekhar 1961, Chapter IV):
    Ra_c  ->  pi^2 Q   for  Q >> 1   (free-free boundaries)
    Exact:  Ra_c(a, Q)  minimised over wavenumber a.

Relativistic correction:
    Q_rel = Q / (1 + v_A^2 / c^2)
    Ra_{c,rel} = Ra_c(Q_rel) / (1 + xi)
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

# ── Chandrasekhar number range ────────────────────────────────────────
Q = np.logspace(0, 6, 600)

# Classical critical Ra(Q) for free-free boundaries (exact Chandrasekhar):
#   Ra_c = min_a [ (pi^2 + a^2)^3 / a^2  +  pi^2 Q (pi^2 + a^2) / a^2 ]
# Numerically minimise over the wavenumber a for each Q.
def Ra_critical_classical(Q_val):
    a = np.linspace(0.5, 30, 2000)
    pi2 = np.pi**2
    pa2 = pi2 + a**2
    Ra = pa2**3 / a**2 + pi2 * Q_val * pa2 / a**2
    return Ra.min()

Ra_class = np.array([Ra_critical_classical(q) for q in Q])

# Asymptote pi^2 Q
Ra_asymp = np.pi**2 * Q

# ── Relativistic curves ───────────────────────────────────────────────
# v_A^2 / c^2 parametrises magnetic-relativistic correction
vA2_c2_values = [0.0, 0.05, 0.20]
xi = 0.1  # fixed relativistic enthalpy parameter

colors = ["#1f77b4", "#ff7f0e", "#d62728"]
styles = ["-", "--", "-."]

fig, ax = plt.subplots()

for i, vA2 in enumerate(vA2_c2_values):
    Q_eff = Q / (1.0 + vA2)
    Ra_rel = np.array([Ra_critical_classical(q) for q in Q_eff]) / (1.0 + xi)
    lbl = (rf"$v_A^2/c^2={vA2}$, $\xi={xi}$" if vA2 > 0
           else r"Classical ($v_A^2/c^2=0$, $\xi=0$)")
    if vA2 == 0:
        Ra_rel = Ra_class  # pure classical
    ax.loglog(Q, Ra_rel, styles[i], color=colors[i], linewidth=2.0,
              label=lbl)

# pi^2 Q asymptote
ax.loglog(Q, Ra_asymp, ":", color="gray", linewidth=1.2,
          label=r"$\pi^{2}\,Q$ asymptote")

ax.set_xlabel(r"Chandrasekhar number $Q$")
ax.set_ylabel(r"Critical Rayleigh number $\mathrm{Ra}_{c}$")
ax.set_title("Magneto-convection: classical vs relativistic")
ax.legend(loc="upper left", frameon=True, edgecolor="0.7")
ax.set_xlim(1, 1e6)
ax.set_ylim(1e2, 1e9)
ax.grid(True, which="both", linestyle=":", alpha=0.35)

fig.tight_layout()
fig.savefig("plots/fig_magnetic_Ra_Q.pdf")
fig.savefig("plots/fig_magnetic_Ra_Q.png")
print("Saved  plots/fig_magnetic_Ra_Q.pdf  and  plots/fig_magnetic_Ra_Q.png")
plt.close(fig)
