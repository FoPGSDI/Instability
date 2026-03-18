#!/usr/bin/env python3
"""
BDNK vs Israel-Stewart dispersion relations for thermal (diffusion) mode.

Israel-Stewart (IS): 2nd-order theory with relaxation time tau_pi.
    Dispersion relation is 5th-order in omega (3 hydro + 2 relaxation modes).

BDNK: 1st-order causal theory (Bemfica-Disconzi-Noronha-Kovtun).
    Dispersion relation is 3rd-order in omega (only physical modes).

Both agree at long wavelengths (small k), diverge at short wavelengths (large k).

Model dispersion relations (longitudinal sector):

IS:  tau_pi omega^2 - i omega - D_th k^2 = 0   (thermal / shear sector)
     Plus additional relaxation modes at omega ~ -i/tau_pi.

BDNK: -i omega - D_th k^2 / (1 + i tau_bdnk omega) = 0
       => omega^2 + i omega / tau_bdnk - D_th k^2 / tau_bdnk = 0

Reference: Chapters X-XIV of the relativistic instability monograph.
"""

import warnings
import numpy as np
warnings.filterwarnings("ignore", category=RuntimeWarning)
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
D_th = 1.0        # thermal diffusivity (normalised)
tau_is = 0.5      # IS relaxation time
tau_bdnk = 0.3    # BDNK characteristic time scale
cs = 0.5          # sound speed (c = 1)

k = np.linspace(0.01, 8, 1000)

# ── IS dispersion: thermal/diffusion mode ─────────────────────────────
# Shear/diffusion sector:  tau omega^2 - i omega - D k^2 = 0
# omega = (i +/- sqrt(-1 + 4 tau D k^2)) / (2 tau)
# The physical (hydrodynamic) mode at small k: omega ~ -i D k^2
disc_is = -1.0 + 4.0 * tau_is * D_th * k**2
omega_is_im = np.where(disc_is < 0,
                       (1.0 - np.sqrt(-disc_is)) / (2.0 * tau_is),
                       1.0 / (2.0 * tau_is))
omega_is_re = np.where(disc_is >= 0,
                       np.sqrt(disc_is) / (2.0 * tau_is),
                       0.0)
# Non-hydrodynamic (relaxation) mode
omega_is_nh_im = np.where(disc_is < 0,
                          (1.0 + np.sqrt(-disc_is)) / (2.0 * tau_is),
                          1.0 / (2.0 * tau_is))
omega_is_nh_re = np.where(disc_is >= 0,
                          -np.sqrt(disc_is) / (2.0 * tau_is),
                          0.0)

# ── BDNK dispersion: thermal mode ────────────────────────────────────
# omega^2 + (i / tau_bdnk) omega - D k^2 / tau_bdnk = 0
disc_bdnk = -1.0 / tau_bdnk**2 + 4.0 * D_th * k**2 / tau_bdnk
omega_bdnk_im = np.where(disc_bdnk < 0,
                         (1.0 / tau_bdnk - np.sqrt(-disc_bdnk)) / 2.0,
                         1.0 / (2.0 * tau_bdnk))
omega_bdnk_re = np.where(disc_bdnk >= 0,
                          np.sqrt(disc_bdnk) / 2.0,
                          0.0)

# ── Sound mode (for reference): omega = +/- cs k ─────────────────────
omega_sound_re = cs * k

# ── IS: 5th-order polynomial (sound + thermal + 2 relaxation) ────────
# Sound modes in IS:  tau omega^3 + i omega^2 - (cs^2 + D/tau) k^2 omega - i cs^2 k^2 = 0
# We solve numerically for the full sound sector
omega_is_sound_re = np.zeros_like(k)
omega_is_sound_im = np.zeros_like(k)
for idx, kk in enumerate(k):
    # Coefficients: tau * w^3 + i w^2 - (cs^2 + D/tau)*k^2 * w - i cs^2 k^2 = 0
    # Let w = -i * z  => solve in z
    # tau * (-i)^3 z^3 + i (-i)^2 z^2 - (cs^2 + D/tau) k^2 (-i z) - i cs^2 k^2 = 0
    # i tau z^3 - i z^2 + i (cs^2 + D/tau) k^2 z - i cs^2 k^2 = 0
    # tau z^3 - z^2 + (cs^2 + D/tau) k^2 z - cs^2 k^2 = 0
    coeffs = [tau_is,
              -1.0,
              (cs**2 + D_th / tau_is) * kk**2,
              -cs**2 * kk**2]
    roots = np.roots(coeffs)
    # omega = -i z  => Im(omega) = -Re(z), Re(omega) = Im(z)
    # Pick the mode closest to cs * k in Re(omega)
    omega_roots = 1j * roots  # omega = -i * z => but easier: omega = i * Im(z) - Re(z) ...
    # Actually omega = -i * z, so Re(omega) = Im(z), Im(omega) = -Re(z)
    re_parts = np.imag(roots)   # Re(omega)
    im_parts = -np.real(roots)  # Im(omega) (should be negative for damped)
    # Pick mode with largest |Re(omega)|
    idx_sound = np.argmax(np.abs(re_parts))
    omega_is_sound_re[idx] = np.abs(re_parts[idx_sound])
    omega_is_sound_im[idx] = im_parts[idx_sound]

# ── Plot ──────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Left panel: Real part of omega (propagation)
ax = axes[0]
ax.plot(k, omega_sound_re, ":", color="0.5", linewidth=1.0,
        label=r"$\omega = c_s k$ (ideal)")
ax.plot(k, omega_is_re, "-", color="#1f77b4", linewidth=2.0,
        label="IS: thermal mode (Re)")
ax.plot(k, omega_bdnk_re, "--", color="#d62728", linewidth=2.0,
        label="BDNK: thermal mode (Re)")
ax.plot(k, np.abs(omega_is_nh_re), "-.", color="#1f77b4", linewidth=1.0, alpha=0.5,
        label="IS: non-hydro mode (Re)")
ax.plot(k, omega_is_sound_re, "-", color="#2ca02c", linewidth=1.5,
        label="IS: sound mode (Re)")

ax.set_xlabel(r"Wavenumber $k$")
ax.set_ylabel(r"Re$(\omega)$")
ax.set_title("Dispersion: propagation")
ax.legend(loc="upper left", frameon=True, edgecolor="0.7", fontsize=9)
ax.set_xlim(0, 8)
ax.grid(True, linestyle=":", alpha=0.5)

# Right panel: Imaginary part (damping)
ax = axes[1]
ax.plot(k, -D_th * k**2, ":", color="0.5", linewidth=1.0,
        label=r"$-D_{\rm th} k^2$ (Navier-Stokes)")
ax.plot(k, -omega_is_im, "-", color="#1f77b4", linewidth=2.0,
        label="IS: thermal mode (Im)")
ax.plot(k, -omega_bdnk_im, "--", color="#d62728", linewidth=2.0,
        label="BDNK: thermal mode (Im)")
ax.plot(k, -omega_is_nh_im, "-.", color="#1f77b4", linewidth=1.0, alpha=0.5,
        label="IS: non-hydro mode (Im)")
ax.plot(k, omega_is_sound_im, "-", color="#2ca02c", linewidth=1.5,
        label="IS: sound mode (Im)")

ax.set_xlabel(r"Wavenumber $k$")
ax.set_ylabel(r"$-$Im$(\omega)$ [damping rate]")
ax.set_title("Dispersion: damping")
ax.legend(loc="upper left", frameon=True, edgecolor="0.7", fontsize=9)
ax.set_xlim(0, 8)
ax.grid(True, linestyle=":", alpha=0.5)

# Annotate agreement region
for a in axes:
    a.axvspan(0, 1.5, color="green", alpha=0.03)
    a.annotate("Low-$k$:\nagree", xy=(0.5, 0.85), xycoords=("data", "axes fraction"),
               fontsize=9, color="#2ca02c", ha="center")

fig.tight_layout()
fig.savefig("plots/fig_bdnk_vs_is.pdf")
fig.savefig("plots/fig_bdnk_vs_is.png")
print("Saved  plots/fig_bdnk_vs_is.pdf  and  plots/fig_bdnk_vs_is.png")
plt.close(fig)
