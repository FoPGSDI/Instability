"""
KH growth rate sigma(k) for spine-sheath jet model vs uniform jet.

Spine-sheath model:
  Fast spine: Gamma_spine ~ 10, narrow core
  Slow sheath: Gamma_sheath ~ 2, broader envelope

Comparison with single-component uniform jet at matched parameters.

Physics:
  - Two-interface KH problem: spine-sheath and sheath-ambient
  - Growth rates from relativistic vortex-sheet dispersion
  - Coupling between modes at the two interfaces

References: Hardee (2007), Mizuno et al. (2007, 2011)
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, LINE_STYLES
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# ---- Jet parameters ----
c = 1.0

# Spine-sheath model
Gamma_spine = 10.0
Gamma_sheath = 2.0
eta_spine = 0.001   # spine enthalpy / ambient enthalpy
eta_sheath = 0.05   # sheath enthalpy / ambient enthalpy
R_spine = 0.3       # spine radius (normalised to jet radius)
R_jet = 1.0         # total jet radius

# Uniform jet for comparison
Gamma_uniform = 6.0  # average
eta_uniform = 0.01

# Sound speeds
cs_spine = c / np.sqrt(3)    # hot spine
cs_sheath = 0.3 * c          # warm sheath
cs_amb = 0.1 * c             # cool ambient
cs_uniform = c / np.sqrt(3)  # hot uniform jet

# Wavenumber range
kR = np.linspace(0.01, 8.0, 600)


def vortex_sheet_growth(kR, Gamma, eta, cs_int, cs_ext):
    """Compute KH growth rate for a relativistic vortex sheet.

    Returns sigma * R / c (normalised growth rate in lab frame).
    """
    beta = np.sqrt(1 - 1/Gamma**2)
    V = beta * c

    # Density fractions (relativistic)
    alpha_j = Gamma**2 * eta / (Gamma**2 * eta + 1.0)
    alpha_e = 1.0 - alpha_j

    # Incompressible growth rate
    sigma_incomp = kR * V * np.sqrt(alpha_j * alpha_e)

    # Compressibility: cut off modes with k > k_sonic
    # k_sonic determined by relative Mach number
    M_rel = Gamma * V / cs_ext
    k_sonic = M_rel * Gamma  # approximate
    compress = 1.0 / np.sqrt(1 + (kR / k_sonic)**2)

    # Lab-frame time dilation
    sigma_lab = sigma_incomp * compress / Gamma**2

    return sigma_lab


# ---- Compute growth rates ----

# 1. Spine-sheath interface
sigma_ss = vortex_sheet_growth(kR / R_spine, Gamma_spine / Gamma_sheath,
                                eta_spine / eta_sheath,
                                cs_spine, cs_sheath)
# Scale to jet radius units
sigma_ss *= R_spine

# 2. Sheath-ambient interface
sigma_sa = vortex_sheet_growth(kR, Gamma_sheath, eta_sheath,
                                cs_sheath, cs_amb)

# 3. Combined: the faster-growing mode dominates
sigma_combined = np.maximum(sigma_ss, sigma_sa)

# 4. Coupling enhancement: when both interfaces are excited,
#    constructive interference boosts growth by ~20-50%
coupling_factor = 1.0 + 0.3 * np.exp(-(kR - 2.0)**2 / 2.0)
sigma_coupled = sigma_combined * coupling_factor

# 5. Uniform jet for comparison
sigma_uniform = vortex_sheet_growth(kR, Gamma_uniform, eta_uniform,
                                     cs_uniform, cs_amb)


# ---- Plotting ----
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# Left panel: Growth rate comparison
ax1.plot(kR, sigma_uniform, '-', lw=2.5, color=COLORS['classical'],
         label=rf'Uniform jet ($\Gamma={Gamma_uniform:.0f}$)')
ax1.plot(kR, sigma_ss, '--', lw=2.0, color=COLORS['jet'],
         label=rf'Spine-sheath interface ($\Gamma_s={Gamma_spine:.0f}$)')
ax1.plot(kR, sigma_sa, '-.', lw=2.0, color=COLORS['accretion'],
         label=rf'Sheath-ambient interface ($\Gamma_{{sh}}={Gamma_sheath:.0f}$)')
ax1.plot(kR, sigma_coupled, '-', lw=2.8, color=COLORS['relativistic'],
         label='Coupled spine-sheath')

# Mark the most unstable wavenumber for each
k_max_uniform = kR[np.argmax(sigma_uniform)]
k_max_coupled = kR[np.argmax(sigma_coupled)]
ax1.axvline(x=k_max_uniform, ls=':', color=COLORS['classical'], alpha=0.5, lw=1.0)
ax1.axvline(x=k_max_coupled, ls=':', color=COLORS['relativistic'], alpha=0.5, lw=1.0)

ax1.set_xlabel(r'Normalised wavenumber $k R_{\rm jet}$')
ax1.set_ylabel(r'Growth rate $\sigma R_{\rm jet}/c$')
ax1.set_title(r'KH growth rate: spine-sheath vs uniform jet')
ax1.legend(loc='upper right', fontsize=9)
ax1.set_xlim(0, 8)
ax1.set_ylim(0, None)

# Right panel: Growth rate ratio spine-sheath / uniform
# and schematic of the jet structure
ax2_top = fig.add_axes([0.58, 0.55, 0.35, 0.35])  # inset for jet cross-section

# Main right panel: ratio
ratio = sigma_coupled / np.maximum(sigma_uniform, 1e-10)
ax2.plot(kR, ratio, '-', lw=2.5, color=COLORS['relativistic'])
ax2.axhline(y=1.0, ls='--', color='gray', lw=1.0)
ax2.fill_between(kR, 1.0, ratio, where=ratio > 1, alpha=0.2,
                 color=COLORS['relativistic'], label='Spine-sheath more unstable')
ax2.fill_between(kR, ratio, 1.0, where=ratio < 1, alpha=0.2,
                 color=COLORS['classical'], label='Uniform jet more unstable')

ax2.set_xlabel(r'Normalised wavenumber $k R_{\rm jet}$')
ax2.set_ylabel(r'$\sigma_{\rm spine-sheath} / \sigma_{\rm uniform}$')
ax2.set_title('Growth rate ratio')
ax2.legend(loc='upper right', fontsize=9)
ax2.set_xlim(0, 8)
ax2.set_ylim(0, 5)

# Inset: jet cross-section schematic
theta = np.linspace(0, 2*np.pi, 100)
# Spine
ax2_top.fill(R_spine * np.cos(theta), R_spine * np.sin(theta),
             color=COLORS['relativistic'], alpha=0.4, label='Spine')
# Sheath
ax2_top.fill(R_jet * np.cos(theta), R_jet * np.sin(theta),
             color=COLORS['accretion'], alpha=0.2, label='Sheath')
ax2_top.fill(R_spine * np.cos(theta), R_spine * np.sin(theta),
             color=COLORS['relativistic'], alpha=0.4)

ax2_top.annotate(rf'$\Gamma={Gamma_spine:.0f}$', xy=(0, 0), fontsize=9,
                 ha='center', va='center', color=COLORS['relativistic'],
                 fontweight='bold')
ax2_top.annotate(rf'$\Gamma={Gamma_sheath:.0f}$', xy=(0.65, 0.0), fontsize=9,
                 ha='center', va='center', color=COLORS['accretion'],
                 fontweight='bold')
ax2_top.annotate('Ambient', xy=(0, -1.3), fontsize=9,
                 ha='center', va='center', color='gray')

ax2_top.set_xlim(-1.5, 1.5)
ax2_top.set_ylim(-1.5, 1.5)
ax2_top.set_aspect('equal')
ax2_top.set_title('Jet cross-section', fontsize=10)
ax2_top.set_xticks([])
ax2_top.set_yticks([])

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_spine_sheath_kh.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_spine_sheath_kh.png')
print("Saved fig_spine_sheath_kh.pdf/png")
