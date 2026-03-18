#!/usr/bin/env python3
"""
Rayleigh stability diagram for Taylor--Couette flow.

Classical criterion:  d(r^2 Omega)^2 / dr > 0  =>  stability.
Relativistic:        d(gamma^2 r^2 Omega)^2 / dr > 0  =>  stability,
where gamma = 1/sqrt(1 - (r Omega / c)^2).

The plot shows the stability boundary in the (Omega_inner, Omega_outer)
plane for a fixed geometry, comparing classical and relativistic cases.

Produces: plots/fig_rayleigh_criterion.pdf
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

# ── Geometry ─────────────────────────────────────────────────────────
eta = 0.8          # radius ratio R1/R2
R1 = 1.0
R2 = R1 / eta

# ── Classical Rayleigh line ──────────────────────────────────────────
# For Couette profile Omega(r) = A + B/r^2 with inner/outer angular
# velocities Omega_1, Omega_2.  The classical Rayleigh criterion
# (marginal) in the (mu, 1) plane where mu = Omega_2/Omega_1 is:
#   mu_crit = eta^2   (classical)
mu_classical = eta ** 2

# ── Relativistic Rayleigh boundary ───────────────────────────────────
# With Lorentz factor gamma(r) the effective angular momentum
# is L = gamma * r^2 * Omega.  The relativistic correction shifts the
# stability boundary to higher mu (outer rotation must be relatively
# faster).  For a velocity parameter beta_1 = R1*Omega_1/c we compute
# the marginal mu numerically.

def rayleigh_marginal_relativistic(beta1, eta, N=500):
    """Return marginal mu = Omega2/Omega1 for given beta1 = R1*Omega1/c."""
    R1_loc = 1.0
    R2_loc = R1_loc / eta
    # Couette profile: Omega(r) = A + B/r^2
    # boundary conditions Omega(R1)=Omega1, Omega(R2)=mu*Omega1
    # We sweep mu and find where d/dr[gamma^2 r^2 Omega]^2 = 0
    # at some r in [R1, R2].
    # Simplify: set Omega1 = 1 (absorbed in beta1).
    Omega1 = 1.0
    r = np.linspace(R1_loc, R2_loc, N)

    def check_stability(mu):
        Omega2 = mu * Omega1
        # Couette coefficients
        A = (Omega2 * R2_loc**2 - Omega1 * R1_loc**2) / (R2_loc**2 - R1_loc**2)
        B = (Omega1 - Omega2) * R1_loc**2 * R2_loc**2 / (R2_loc**2 - R1_loc**2)
        Omega_r = A + B / r**2
        v_r = r * Omega_r * beta1  # actual v/c = r*Omega * (beta1/R1*Omega1) but Omega1=1, R1=1
        gamma_r = 1.0 / np.sqrt(np.clip(1.0 - v_r**2, 1e-12, None))
        L = gamma_r * r**2 * Omega_r
        L2 = L**2
        dL2 = np.diff(L2) / np.diff(r)
        return np.all(dL2 > 0)

    # Binary search for marginal mu
    mu_lo, mu_hi = 0.0, 1.5
    for _ in range(80):
        mu_mid = 0.5 * (mu_lo + mu_hi)
        if check_stability(mu_mid):
            mu_hi = mu_mid
        else:
            mu_lo = mu_mid
    return 0.5 * (mu_lo + mu_hi)


# ── Compute curves ───────────────────────────────────────────────────
beta1_values = np.linspace(0.01, 0.70, 60)
mu_rel = np.array([rayleigh_marginal_relativistic(b, eta) for b in beta1_values])

fig, ax = plt.subplots()

# Classical line (independent of beta)
ax.axhline(mu_classical, color="k", ls="--", lw=1.5,
           label=rf"Classical: $\mu_c = \eta^2 = {mu_classical:.2f}$")

# Relativistic curve
ax.plot(beta1_values, mu_rel, "-", color="#d62728", lw=2.0,
        label=r"Relativistic boundary ($\gamma$-corrected)")

# Shade stable / unstable
ax.fill_between(beta1_values, mu_rel, 1.5, alpha=0.12, color="green")
ax.fill_between(beta1_values, 0, mu_rel, alpha=0.08, color="red")
ax.text(0.50, 1.10, "STABLE", fontsize=12, ha="center", color="green",
        fontweight="bold", alpha=0.7)
ax.text(0.15, 0.15, "UNSTABLE", fontsize=12, ha="center", color="red",
        fontweight="bold", alpha=0.7)

ax.set_xlabel(r"Inner-cylinder velocity parameter $\beta_1 = R_1\Omega_1/c$")
ax.set_ylabel(r"Rotation ratio $\mu = \Omega_2/\Omega_1$")
ax.set_title(r"Rayleigh stability boundary ($\eta = 0.8$)")
ax.legend(loc="lower right")
ax.set_xlim(0, 0.72)
ax.set_ylim(0, 1.4)
ax.grid(True, alpha=0.3)

fig.tight_layout()
fig.savefig("plots/fig_rayleigh_criterion.pdf")
print("Saved plots/fig_rayleigh_criterion.pdf")
