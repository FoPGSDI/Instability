"""
Thick disk (ADAF/torus) stability around Sgr A*.

Model a geometrically thick torus with H/R ~ 1 around Sgr A*
(M ~ 4 × 10^6 M☉), compute the critical Taylor number for the torus,
and map the stability boundary in parameter space.

The key physics: for thick disks (H/R ~ 1), the wide-gap Couette
analysis applies with η = R_in/R_out ~ 0.3-0.5. The relativistic
correction δ_rel reduces T_c, facilitating instability.

References:
  - Narayan & Yi (1994), ApJ 428, L13 (ADAF solution)
  - Abramowicz & Fragile (2013), Living Rev. Relativ. 16, 1
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, LINE_STYLES
from SHARED_PLOT_STYLE import c_cgs, G_cgs, M_sun, k_B, m_p, pi
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# --- Sgr A* parameters ---
M_bh = 4.0e6 * M_sun  # Sgr A* mass
r_g = G_cgs * M_bh / c_cgs**2  # gravitational radius

# ADAF parameters
alpha_visc = 0.1  # viscosity parameter
beta_mag = 0.5    # magnetic pressure / total pressure
f_adv = 0.5       # advection parameter

# --- Torus model ---
# For ADAF: H/R ~ c_s/v_K ~ (kT / m_p v_K²)^{1/2}
# Hot flow: T_ion ~ T_virial ~ GM m_p / (3kR)

def T_virial(r_rg):
    """Virial temperature at r (in units of r_g)."""
    return G_cgs * M_bh * m_p / (3 * k_B * r_rg * r_g)

def cs_over_vK(r_rg, T_ion=None):
    """Sound speed / Keplerian speed for ADAF."""
    if T_ion is None:
        T_ion = T_virial(r_rg)
    cs2 = k_B * T_ion / m_p
    vK2 = G_cgs * M_bh / (r_rg * r_g)
    return np.sqrt(cs2 / vK2)

def H_over_R(r_rg):
    """Disk aspect ratio for ADAF."""
    return cs_over_vK(r_rg)

# --- Critical Taylor number ---
# From the wide-gap analysis (§72-73):
# T_c^class depends on η = R_in/R_out and κ
# T_c^rel = T_c^class * (1 - δ_rel)
# δ_rel = p/(ρ₀c²) + (η_s²/(ρ₀²c²d²)) Φ_visc

def T_c_classical(eta, mu=0):
    """Approximate critical Taylor number for wide gap.
    Interpolation from Chandrasekhar Table XXXIV data.
    """
    # For μ = 0 (outer cylinder at rest):
    # T_c grows roughly as (1-η)^{-4} for narrow gap
    # and reaches ~10^5 for η ~ 0.3
    if np.isscalar(eta):
        eta = np.array([eta])
    Tc = np.zeros_like(eta)

    # Interpolation from known values:
    # η=0.95: T_c ≈ 1708, η=0.75: T_c ≈ 2530, η=0.5: T_c ≈ 15340
    # η=0.3: T_c ≈ 121000
    eta_data = np.array([0.95, 0.85, 0.75, 0.65, 0.5, 0.4, 0.3])
    Tc_data = np.array([1708, 1950, 2530, 5200, 15340, 42000, 121000])

    Tc = np.interp(eta, eta_data, Tc_data)
    return Tc

def delta_rel(r_rg, eta):
    """Relativistic correction δ_rel for thick disk."""
    T_ion = T_virial(r_rg)
    # p/(ρ₀c²): for hot ADAF, p = ρ kT / m_p
    p_over_rho_c2 = k_B * T_ion / (m_p * c_cgs**2)

    # Kinematic correction: Ω²R²/c² for Keplerian orbit
    v_over_c_sq = r_g / r_rg  # v²/c² ~ GM/(rc²) = r_g/r

    # Total correction
    return p_over_rho_c2 + v_over_c_sq


# --- PLOT ---
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# === Left panel: Stability boundary in (r/r_g, H/R) space ===
ax1 = axes[0]

r_rg = np.linspace(5, 200, 500)
HR = H_over_R(r_rg)

# Plot H/R profile
ax1.plot(r_rg, HR, color=COLORS['accretion'], lw=2.5,
         label=r'ADAF: $H/R = c_s/v_K$')

# For a thin disk comparison
HR_thin = 0.05 * np.ones_like(r_rg)
ax1.plot(r_rg, HR_thin, color=COLORS['classical'], lw=1.5, ls='--',
         label=r'Thin disk: $H/R = 0.05$')

# Shade the thick disk region
ax1.fill_between(r_rg, 0.5, 1.5, alpha=0.08, color='red')
ax1.annotate('Geometrically thick\n(wide-gap regime)',
             xy=(100, 1.1), fontsize=11, color='red', ha='center')
ax1.fill_between(r_rg, 0, 0.1, alpha=0.08, color='blue')
ax1.annotate('Thin disk\n(narrow-gap)',
             xy=(100, 0.03), fontsize=10, color='blue', ha='center')

# Mark ISCO
ax1.axvline(6, color='gray', ls=':', lw=1)
ax1.annotate('ISCO', xy=(6.5, 0.8), fontsize=10, color='gray')

ax1.set_xlabel(r'$r / r_g$')
ax1.set_ylabel(r'$H/R$')
ax1.set_title(r'Disk geometry: Sgr A* ($M = 4\times10^6\,M_\odot$)')
ax1.set_xlim(5, 200)
ax1.set_ylim(0, 1.5)
ax1.legend(loc='upper right', fontsize=10)

# === Right panel: Critical Taylor number with relativistic corrections ===
ax2 = axes[1]

eta_arr = np.linspace(0.25, 0.95, 200)

# Classical
Tc_cl = T_c_classical(eta_arr)

# Relativistic at different radii (which set δ_rel)
radii_for_delta = [10, 20, 50, 100]
colors_r = ['#F44336', '#FF9800', '#4CAF50', '#2196F3']

ax2.semilogy(eta_arr, Tc_cl, 'k-', lw=2.5, label='Classical (Newtonian)')

for i, r_val in enumerate(radii_for_delta):
    d_rel = delta_rel(r_val, eta_arr)
    Tc_rel = Tc_cl * (1 - d_rel)
    ax2.semilogy(eta_arr, Tc_rel, color=colors_r[i], lw=1.8,
                 ls=LINE_STYLES[(i+1) % len(LINE_STYLES)],
                 label=r'$r = {}\ r_g$, $\delta_{{\rm rel}} \approx {:.3f}$'.format(
                     r_val, float(delta_rel(r_val, 0.5))))

# Mark typical ADAF torus η range
ax2.axvspan(0.3, 0.55, alpha=0.1, color='orange')
ax2.annotate('Typical ADAF\ntorus range',
             xy=(0.42, 5e3), fontsize=10, color='#FF9800', ha='center',
             bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#FF9800'))

ax2.set_xlabel(r'$\eta = R_{\rm in}/R_{\rm out}$')
ax2.set_ylabel(r'$T_c$ (critical Taylor number)')
ax2.set_title('Stability boundary: classical vs relativistic')
ax2.legend(loc='upper left', fontsize=9)
ax2.set_xlim(0.25, 0.95)
ax2.set_ylim(1e3, 2e5)

fig.suptitle(
    r'Thick disk stability around Sgr A*: critical Taylor number for ADAF torus',
    fontsize=13, y=1.02)
plt.tight_layout()

for ext in ['pdf', 'png']:
    plt.savefig(f'/data/haiyangw/claude/Instability/plots/deep/fig_thick_disk_stability.{ext}',
                dpi=300, bbox_inches='tight')
print("Saved fig_thick_disk_stability.pdf/png")
plt.close()
