#!/usr/bin/env python3
"""
Plot dispersion relations for thermal modes: classical (Navier-Stokes)
vs BDNK relativistic, verifying causality (group velocity < c).

Classical Navier-Stokes (incompressible, linearised):
  - Two sound modes:   omega = +/- c_s k   (isentropic)
  - Thermal diffusion: omega = -i kappa k^2

BDNK relativistic (Israel-Stewart-like causal theory):
  - Same three mode structure, but:
    * Sound speed c_s < c  (bounded by c/sqrt{3} for conformal fluid)
    * Thermal diffusion acquires a relaxation time tau_q
      so that  omega_thermal  ->  -i/tau_q  at large k  (causal)
    * Group velocity  d(Re omega)/dk  <  c  for all k

Parameters are chosen for a representative relativistic fluid
with xi = p/(eps c^2) = 0.1.
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
    "legend.fontsize": 10,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "figure.figsize": (9, 8),
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})

# ── Physical parameters (dimensionless, c = 1) ───────────────────────
c = 1.0
cs_class = 0.4 * c          # classical sound speed
kappa = 0.05                 # thermal diffusivity
xi = 0.1                     # relativistic parameter
cs_rel = cs_class / np.sqrt(1.0 + xi)   # relativistic sound speed
tau_q = 0.02                 # BDNK thermal relaxation time

k = np.linspace(0, 50, 2000)

# ── Classical modes ───────────────────────────────────────────────────
omega_sound_class = cs_class * k               # Re(omega)  for + sound mode
gamma_sound_class = -0.5 * kappa * k**2        # Im(omega)  attenuation
omega_thermal_class_im = -kappa * k**2          # Im(omega)  thermal diffusion (acausal!)

# ── BDNK relativistic modes ──────────────────────────────────────────
# Sound modes:  omega^2 = cs_rel^2 k^2  -  i omega Gamma k^2
# Approximate Re and Im parts
Gamma_rel = kappa / (1.0 + xi)
omega_sound_rel = cs_rel * k
gamma_sound_rel = -0.5 * Gamma_rel * k**2 / (1.0 + tau_q * cs_rel * k)

# Thermal mode (BDNK causal):
#   omega = -i kappa_eff k^2 / (1 + i tau_q omega)
# -> omega_im = -kappa_eff k^2 / (1 + tau_q kappa_eff k^2)  (saturates at -1/tau_q)
kappa_eff = kappa / (1.0 + xi)
omega_thermal_rel_im = -kappa_eff * k**2 / (1.0 + tau_q * kappa_eff * k**2)

# ── Group velocity check ─────────────────────────────────────────────
# d(Re omega)/dk  for sound modes
vg_class = np.gradient(omega_sound_class, k)
vg_rel   = np.gradient(omega_sound_rel, k)

# ── Plotting ──────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# (a) Re(omega) — sound modes
ax = axes[0, 0]
ax.plot(k, omega_sound_class, "-", color="#1f77b4", linewidth=1.8,
        label="Classical sound")
ax.plot(k, omega_sound_rel, "--", color="#d62728", linewidth=1.8,
        label="BDNK sound")
ax.plot(k, c * k, ":", color="gray", linewidth=1,
        label=r"Light cone $\omega = c\,k$")
ax.set_xlabel(r"Wavenumber $k$")
ax.set_ylabel(r"Re$(\omega)$")
ax.set_title("(a) Sound mode dispersion")
ax.legend(loc="upper left", fontsize=9)
ax.set_xlim(0, 50)
ax.grid(True, linestyle=":", alpha=0.4)

# (b) Im(omega) — thermal diffusion mode
ax = axes[0, 1]
ax.plot(k, omega_thermal_class_im, "-", color="#1f77b4", linewidth=1.8,
        label="Classical (acausal)")
ax.plot(k, omega_thermal_rel_im, "--", color="#d62728", linewidth=1.8,
        label="BDNK (causal)")
ax.axhline(-1.0/tau_q, color="gray", linestyle=":", linewidth=1,
           label=rf"$-1/\tau_q = {-1.0/tau_q:.0f}$")
ax.set_xlabel(r"Wavenumber $k$")
ax.set_ylabel(r"Im$(\omega)$")
ax.set_title("(b) Thermal diffusion mode")
ax.legend(loc="lower left", fontsize=9)
ax.set_xlim(0, 50)
ax.grid(True, linestyle=":", alpha=0.4)

# (c) Im(omega) — sound mode attenuation
ax = axes[1, 0]
ax.plot(k, gamma_sound_class, "-", color="#1f77b4", linewidth=1.8,
        label="Classical")
ax.plot(k, gamma_sound_rel, "--", color="#d62728", linewidth=1.8,
        label="BDNK")
ax.set_xlabel(r"Wavenumber $k$")
ax.set_ylabel(r"Im$(\omega)$")
ax.set_title("(c) Sound mode attenuation")
ax.legend(loc="lower left", fontsize=9)
ax.set_xlim(0, 50)
ax.grid(True, linestyle=":", alpha=0.4)

# (d) Group velocity
ax = axes[1, 1]
ax.plot(k[1:], vg_class[1:], "-", color="#1f77b4", linewidth=1.8,
        label="Classical")
ax.plot(k[1:], vg_rel[1:], "--", color="#d62728", linewidth=1.8,
        label="BDNK")
ax.axhline(c, color="gray", linestyle=":", linewidth=1, label=r"$c$")
ax.set_xlabel(r"Wavenumber $k$")
ax.set_ylabel(r"Group velocity $v_g = d\,\mathrm{Re}(\omega)/dk$")
ax.set_title("(d) Causality check: $v_g < c$")
ax.legend(loc="center right", fontsize=9)
ax.set_xlim(0, 50)
ax.set_ylim(0, 1.2)
ax.grid(True, linestyle=":", alpha=0.4)

fig.suptitle("Dispersion relations: classical vs BDNK relativistic",
             fontsize=14, y=1.01)
fig.tight_layout()
fig.savefig("plots/fig_dispersion_thermal.pdf")
fig.savefig("plots/fig_dispersion_thermal.png")
print("Saved  plots/fig_dispersion_thermal.pdf  and  plots/fig_dispersion_thermal.png")
plt.close(fig)
