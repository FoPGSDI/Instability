#!/usr/bin/env python3
"""
Magneto-rotational instability (MRI) dispersion relation.

For a Couette flow threaded by an axial magnetic field B_z, the MRI
growth rate sigma = Im(omega) depends on the axial wavenumber k.

Classical (incompressible):
    sigma^2 = -(kappa^2 + 2 (k v_A)^2) + sqrt(16 Omega^2 (k v_A)^2 + kappa^4)
                                          ─────────────────────────────────────────
                                                          2
where kappa^2 = (2 Omega/r) d(r^2 Omega)/dr  is the epicyclic frequency
and v_A = B/sqrt(4 pi rho) is the Alfven speed.

Relativistic: the Alfven speed is bounded, v_A -> v_A / sqrt(1 + v_A^2/c^2),
which caps the stabilising magnetic tension and modifies growth rates.

Produces: plots/fig_mri_dispersion.pdf
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
    "legend.fontsize": 9.5,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "figure.figsize": (7.5, 5),
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})


def mri_growth_rate(k, Omega, q, v_A):
    """
    Classical MRI growth rate.

    Parameters
    ----------
    k : array, axial wavenumber
    Omega : float, angular velocity
    q : float, shear parameter  q = -d ln Omega / d ln r  (q=3/2 for Keplerian)
    v_A : float, Alfven speed

    Returns
    -------
    sigma : array, growth rate (positive where unstable)
    """
    kappa2 = 2.0 * Omega**2 * (2.0 - q)   # epicyclic frequency squared
    kv = k * v_A
    discriminant = 16.0 * Omega**2 * kv**2 + kappa2**2
    sigma2 = 0.5 * (-kappa2 - 2.0 * kv**2 + np.sqrt(np.maximum(discriminant, 0.0)))
    return np.sqrt(np.maximum(sigma2, 0.0))


def mri_growth_rate_relativistic(k, Omega, q, v_A_over_c):
    """
    Relativistic MRI growth rate with bounded Alfven speed.

    v_A,rel = v_A / sqrt(1 + v_A^2/c^2),  so v_A,rel < c always.
    We parameterise by v_A/c.
    """
    # Relativistic Alfven speed (in units of c)
    v_A_rel = v_A_over_c / np.sqrt(1.0 + v_A_over_c**2)
    # Convert back to physical units: v_A_phys = v_A_rel * c.
    # For the dispersion relation we need v_A in the same units as Omega*r.
    # Set c = 1 for this calculation; Omega is already in code units.
    return mri_growth_rate(k, Omega, q, v_A_rel)


# ── Parameters ───────────────────────────────────────────────────────
Omega = 1.0
q = 1.5          # Keplerian shear
k = np.linspace(0.01, 5.0, 500)

# Various v_A/c ratios
va_ratios = [0.1, 0.3, 0.5, 1.0, 2.0]
colors_cl = plt.cm.Blues(np.linspace(0.4, 0.9, len(va_ratios)))
colors_rl = plt.cm.Reds(np.linspace(0.4, 0.9, len(va_ratios)))

fig, axes = plt.subplots(1, 2, figsize=(13, 5), sharey=True)

# ── Left panel: classical ────────────────────────────────────────────
ax = axes[0]
for i, va in enumerate(va_ratios):
    sigma = mri_growth_rate(k, Omega, q, va)
    ax.plot(k, sigma / Omega, color=colors_cl[i], lw=1.8,
            label=rf"$v_A/c = {va}$")

ax.set_xlabel(r"Wavenumber $k$  (units of $\Omega$)")
ax.set_ylabel(r"Growth rate $\sigma / \Omega$")
ax.set_title("Classical MRI")
ax.legend(loc="upper right", fontsize=9)
ax.set_xlim(0, 5)
ax.set_ylim(0, 1.0)
ax.grid(True, alpha=0.3)

# ── Right panel: relativistic (bounded v_A) ──────────────────────────
ax = axes[1]
for i, va in enumerate(va_ratios):
    sigma = mri_growth_rate_relativistic(k, Omega, q, va)
    ax.plot(k, sigma / Omega, color=colors_rl[i], lw=1.8,
            label=rf"$v_A/c = {va}$")

ax.set_xlabel(r"Wavenumber $k$  (units of $\Omega$)")
ax.set_title("Relativistic MRI (bounded Alfv\u00e9n speed)")
ax.legend(loc="upper right", fontsize=9)
ax.set_xlim(0, 5)
ax.grid(True, alpha=0.3)

fig.suptitle(r"MRI dispersion: Keplerian shear ($q = 3/2$)", fontsize=14, y=1.02)
fig.tight_layout()
fig.savefig("plots/fig_mri_dispersion.pdf")
print("Saved plots/fig_mri_dispersion.pdf")
