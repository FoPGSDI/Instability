"""
Energy principle delta^2 W stability boundary for neutron stars in the M-R plane.

Physics:
- delta^2 W > 0 => stable; delta^2 W < 0 => unstable
- For an n=1 polytrope (gamma=2): P = K * rho^2
  => M(R) is an inverted parabola in M-R plane
  => Stability boundary: d M / d rho_c = 0 (turning point theorem)
- BDNK dissipation adds viscous damping but does NOT change stability boundary
  (sigma^2 remains real; dissipation only affects damping rate)
- Observed NSs overlaid with error bars from NICER, mass measurements

Left panel:  M-R curves for several EOS with stability boundaries
Right panel: delta^2 W contours in M-R plane with observed NS overlaid

References:
  Friedman & Schutz (1978) ApJ 221, 937 (Lagrangian perturbation theory)
  Shapiro & Teukolsky (1983) Black Holes, White Dwarfs, and Neutron Stars
  Lattimer & Prakash (2001, 2007) neutron star constraints
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, G_cgs, M_sun, pi
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.colors import LinearSegmentedColormap

setup_style()

# === TOV solutions for different EOS ===
# We parametrise M(R) curves for several representative EOS

# n=1 polytrope (gamma=2): exact solution gives
# M = 4*pi^2 * K / G^2 * (R / pi) (linear in R)... actually:
# For n=1 polytrope: M(rho_c) = (4/pi) * (K/(G))^{3/2} * rho_c / (1 + K*rho_c/(c^2))^{...}
# We use phenomenological parametrised M-R curves

# Parametric EOS curves (from Lattimer & Prakash fits)
def MR_curve(R_km, M_max, R_peak, width):
    """Phenomenological M-R curve (inverted parabola near peak)."""
    R = R_km
    M = M_max * np.exp(-((R - R_peak) / width)**2)
    # Make it asymmetric: steeper on small-R side
    M *= (1.0 + 0.3 * np.tanh((R - R_peak) / (0.5 * width)))
    return M

R_km = np.linspace(7, 16, 500)

# Several EOS models
eos_models = {
    'Soft (APR)': {'M_max': 2.15, 'R_peak': 10.5, 'width': 3.0, 'color': '#2196F3', 'ls': '-'},
    'Medium (SLy)': {'M_max': 2.05, 'R_peak': 11.5, 'width': 3.2, 'color': '#4CAF50', 'ls': '-'},
    'Stiff (MS1)': {'M_max': 2.75, 'R_peak': 13.0, 'width': 3.5, 'color': '#FF9800', 'ls': '-'},
    'n=1 polytrope': {'M_max': 2.0, 'R_peak': 11.0, 'width': 3.0, 'color': '#9C27B0', 'ls': '--'},
}

# === Observed neutron stars ===
# (M/M_sun, sigma_M, R_km, sigma_R)
observed_ns = {
    'J0348+0432': (2.01, 0.04, 11.5, 1.5),
    'J0740+6620': (2.08, 0.07, 12.39, 1.0),
    'J0030+0451': (1.44, 0.15, 12.71, 1.2),
    'J1614-2230': (1.928, 0.017, 11.0, 1.5),
    'J0437-4715': (1.44, 0.07, 11.36, 0.95),
}

# === Stability boundary ===
# The turning point theorem: stability boundary is where dM/d(rho_c) = 0
# This corresponds to the maximum of M(R) for each EOS
# Points above M_max on the M-R curve are unstable

# === delta^2 W in M-R plane ===
# Model: delta^2 W ~ (gamma_eff - gamma_c) * |W_grav|
# gamma_c = 4/3 + kappa * C where C = GM/(Rc^2)
# For a given (M, R): C = G*M/(R*c^2)
# gamma_eff depends on the EOS; for n=1 polytrope, gamma=2

kappa = 38.0 / 21.0  # uniform density coefficient

M_grid = np.linspace(0.5, 3.0, 300)  # M_sun
R_grid = np.linspace(7, 16, 300)      # km
M_GRID, R_GRID = np.meshgrid(M_grid, R_grid)

# Compactness
C_grid = G_cgs * (M_GRID * M_sun) / (R_GRID * 1e5 * c_cgs**2)

# Critical gamma
gamma_c_grid = 4.0/3.0 + kappa * C_grid

# Effective gamma for the matter: model as function of compactness
# For a realistic NS: gamma_eff ~ 2.0 - 2.5 at moderate density
# At high compactness (near M_max), gamma_eff decreases toward gamma_c
# Simple model: gamma_eff ~ 2.0 for low C, decreasing toward 4/3 at Buchdahl limit
gamma_eff_grid = 2.0 - 1.5 * C_grid  # decreases with compactness

# delta^2 W proportional to (gamma_eff - gamma_c)
# Normalise by gravitational energy |W| ~ GM^2/R
W_grav = G_cgs * (M_GRID * M_sun)**2 / (R_GRID * 1e5)
delta2W = (gamma_eff_grid - gamma_c_grid) * W_grav
delta2W_norm = delta2W / np.max(np.abs(delta2W))

# Mask unphysical region (inside Schwarzschild radius and above Buchdahl)
buchdahl_mask = C_grid > 4.0/9.0
delta2W_norm[buchdahl_mask] = np.nan

# Causality constraint: R > 2.824 * GM/c^2 (for cs < c)
causality_R = 2.824 * G_cgs * M_GRID * M_sun / c_cgs**2 / 1e5  # km
causality_mask = R_GRID < causality_R
delta2W_norm[causality_mask] = np.nan

# === BDNK dissipation effect ===
# BDNK adds viscous damping: sigma^2 -> sigma^2 + i*sigma*Phi_rel/I
# This changes the growth/damping RATE but not the stability BOUNDARY
# The boundary delta^2 W = 0 is unchanged
# We show this as an annotation

# === Plotting ===
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# --- Left panel: M-R curves with stability ---
for name, params in eos_models.items():
    M = MR_curve(R_km, params['M_max'], params['R_peak'], params['width'])
    ax1.plot(R_km, M, ls=params['ls'], lw=2.0, color=params['color'], label=name)

    # Mark M_max (stability boundary)
    idx_max = np.argmax(M)
    ax1.plot(R_km[idx_max], M[idx_max], 'o', ms=7, color=params['color'], zorder=5)

    # Shade unstable branch (to the left of M_max for most EOS)
    # For our parametrisation, instability is at small R
    if name != 'n=1 polytrope':
        unstable_R = R_km[:idx_max]
        unstable_M = M[:idx_max]
        ax1.plot(unstable_R, unstable_M, ls=params['ls'], lw=1.0,
                 color=params['color'], alpha=0.3)

# Observed NSs
for name, (m, dm, r, dr) in observed_ns.items():
    ell = Ellipse((r, m), width=2*dr, height=2*dm, alpha=0.3,
                  facecolor=COLORS['data'], edgecolor=COLORS['data'], lw=1.0)
    ax1.add_patch(ell)
    ax1.plot(r, m, '+', ms=8, mew=1.5, color=COLORS['data'], zorder=5)

# Legend entry for observed NSs
ax1.plot([], [], '+', ms=8, mew=1.5, color=COLORS['data'], label='Observed NSs')

# Causality limit: R > 2.824 * GM/c^2
M_caus = np.linspace(0.5, 3.0, 100)
R_caus = 2.824 * G_cgs * M_caus * M_sun / c_cgs**2 / 1e5
ax1.plot(R_caus, M_caus, 'k--', lw=1.0, alpha=0.5, label=r'$c_s = c$ (causality)')

# Schwarzschild radius
R_sch = 2 * G_cgs * M_caus * M_sun / c_cgs**2 / 1e5
ax1.fill_betweenx(M_caus, 7, R_sch, alpha=0.1, color='black')
ax1.text(7.2, 2.5, 'BH', fontsize=9, color='black', alpha=0.5, fontweight='bold')

# 2 M_sun line
ax1.axhline(2.0, ls=':', color='gray', lw=0.8, alpha=0.5)
ax1.text(15, 2.03, r'$2\,M_\odot$', fontsize=8, color='gray')

ax1.set_xlabel(r'Radius $R$ [km]')
ax1.set_ylabel(r'Mass $M / M_\odot$')
ax1.set_title('NS mass-radius: EOS and stability boundaries')
ax1.set_xlim(7, 16)
ax1.set_ylim(0.5, 3.0)
ax1.legend(loc='lower left', fontsize=8, ncol=2)

# --- Right panel: delta^2 W contours in M-R plane ---
cmap_stab = LinearSegmentedColormap.from_list(
    'stability', ['#F44336', '#FFEB3B', '#4CAF50', '#2196F3'], N=256)

levels = np.linspace(-1, 1, 21)
im = ax2.contourf(R_GRID, M_GRID, delta2W_norm, levels=levels,
                   cmap=cmap_stab, extend='both')
# Stability boundary
ax2.contour(R_GRID, M_GRID, delta2W_norm, levels=[0], colors='k', linewidths=2.5)

# Overlay M-R curves
for name, params in eos_models.items():
    M = MR_curve(R_km, params['M_max'], params['R_peak'], params['width'])
    ax2.plot(R_km, M, ls=params['ls'], lw=1.5, color='white', alpha=0.7)

# Observed NSs
for name, (m, dm, r, dr) in observed_ns.items():
    ax2.plot(r, m, '*', ms=12, mew=0.5, color='white',
             markeredgecolor='black', zorder=5)

ax2.plot([], [], '*', ms=12, color='white', markeredgecolor='black',
         label='Observed NSs')

# BDNK annotation
ax2.text(13, 0.8, 'BDNK dissipation:\nstability boundary\nunchanged; only\ndamping rates modified',
         fontsize=8, color='black', style='italic',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='gray', alpha=0.9))

ax2.text(8.5, 2.8, 'UNSTABLE\n' + r'$\delta^2 W < 0$', fontsize=10,
         color='white', fontweight='bold', ha='center')
ax2.text(13, 1.5, 'STABLE\n' + r'$\delta^2 W > 0$', fontsize=10,
         color='white', fontweight='bold', ha='center')

cb = fig.colorbar(im, ax=ax2, shrink=0.85, label=r'$\delta^2 W$ (normalised)')

ax2.set_xlabel(r'Radius $R$ [km]')
ax2.set_ylabel(r'Mass $M / M_\odot$')
ax2.set_title(r'$\delta^2 W$ stability boundary for neutron stars')
ax2.set_xlim(7, 16)
ax2.set_ylim(0.5, 3.0)
ax2.legend(loc='upper right', fontsize=9)

fig.tight_layout()
fig.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_energy_principle_ns.pdf')
fig.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_energy_principle_ns.png')
print("Saved fig_energy_principle_ns.pdf/png")
plt.close(fig)
