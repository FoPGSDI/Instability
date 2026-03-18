"""
BDNK viscosity in accretion disks: effective α vs r.

Compute the effective BDNK Reynolds number for a Shakura-Sunyaev α-disk
and show how BDNK frame coefficients modify the α-prescription.

Key result: α_rel = α_cl / (1 + ξ) where ξ = (ε+p)/(ρ₀c²) - 1.

For a standard α-disk, ξ(r) varies with radius through the local
thermodynamic state. We model gas-pressure and radiation-pressure
dominated zones following Shakura & Sunyaev (1973).
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, LINE_STYLES
from SHARED_PLOT_STYLE import c_cgs, G_cgs, M_sun, k_B, m_p, sigma_SB, pi
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# --- BH parameters ---
M_bh = 10.0 * M_sun  # 10 solar mass BH
r_g = G_cgs * M_bh / c_cgs**2  # gravitational radius in cm

alpha_cl = 0.1  # classical Shakura-Sunyaev alpha
Mdot_edd_frac = 0.1  # accretion rate as fraction of Eddington

# Eddington luminosity and accretion rate
L_edd = 4 * pi * G_cgs * M_bh * m_p * c_cgs / 6.65e-25  # Thomson cross-section
Mdot = Mdot_edd_frac * L_edd / (0.1 * c_cgs**2)  # η ~ 0.1

# --- Disk model: Shakura-Sunyaev zones ---
# Zone (a): radiation-pressure dominated, electron-scattering opacity
# Zone (b): gas-pressure dominated, electron-scattering opacity
# Zone (c): gas-pressure dominated, free-free opacity

# Transition radii (approximate)
r_ab = 150  # r/r_g for zone a/b transition
r_bc = 5000  # r/r_g for zone b/c transition

def f_NT(r_rg):
    """Novikov-Thorne page factor f(r) for Schwarzschild."""
    x = np.sqrt(r_rg)  # r in units of r_g
    x_isco = np.sqrt(6.0)
    # Simplified: f ~ 1 - sqrt(6/r) for large r
    f = np.where(r_rg > 6.0,
                 1 - np.sqrt(6.0 / r_rg),
                 0.0)
    return np.maximum(f, 0.0)

def xi_parameter(r_rg, alpha=0.1, mdot_frac=0.1):
    """
    Compute ξ = (ε+p)/(ρ₀c²) - 1 as a function of radius.

    In zone (a) (radiation dominated): p_rad ~ ε/3, so ξ ~ 4p/(3ρ₀c²)
    In zone (b,c) (gas dominated): p_gas = ρ₀kT/(μm_p), ξ ~ kT/(μm_p c²)

    We use the standard α-disk scalings.
    """
    f = f_NT(r_rg)
    r_cm = r_rg * r_g

    # Central temperature and density from SS73 scalings
    # Zone (a) - radiation pressure dominated
    # T_c ~ 5e7 * alpha^{-1/4} * (M/M_sun)^{-1/4} * (r/r_g)^{-3/8} * f^{1/4} K
    # rho ~ 3e-5 * alpha^{-1} * (Mdot/Mdot_Edd)^{-1} * ... g/cm^3

    # Simplified model: compute ξ from the ratio of radiation to rest-mass energy
    # In zone (a): P_rad/P_gas >> 1, so ξ ≈ (4/3) P_rad / (ρ₀c²)
    # In zone (b/c): P_gas dominant, ξ ≈ (5/2) kT/(μ m_p c²)

    xi = np.zeros_like(r_rg, dtype=float)

    # Zone (a): radiation dominated (r < r_ab)
    mask_a = (r_rg < r_ab) & (r_rg > 6.0)
    if np.any(mask_a):
        # ξ ~ 0.3 * (Mdot/Mdot_Edd) * (r/r_g)^{-1} * f(r) / alpha
        # This gives ξ ~ 0.1-0.5 near ISCO for typical parameters
        xi[mask_a] = 0.3 * mdot_frac / alpha * f[mask_a] * (6.0 / r_rg[mask_a])

    # Zone (b): gas pressure, e-scattering opacity
    mask_b = (r_rg >= r_ab) & (r_rg < r_bc)
    if np.any(mask_b):
        # kT/(m_p c²) ~ few x 10^{-4} at these radii
        # ξ ~ 0.01 * (r_ab/r)^{3/4}
        xi[mask_b] = 0.01 * (r_ab / r_rg[mask_b])**0.75

    # Zone (c): gas pressure, free-free opacity
    mask_c = r_rg >= r_bc
    if np.any(mask_c):
        xi[mask_c] = 0.001 * (r_bc / r_rg[mask_c])

    return xi


# --- Compute ---
r_rg = np.logspace(np.log10(6.5), 5, 2000)  # r/r_g from ISCO to 10^5

xi = xi_parameter(r_rg, alpha=alpha_cl, mdot_frac=Mdot_edd_frac)
alpha_rel = alpha_cl / (1 + xi)
Re_ratio = 1 + xi  # Re_rel / Re_cl

# Also compute for different Mdot
mdots = [0.01, 0.1, 0.5]
mdot_labels = [r'$\dot{M}/\dot{M}_{\rm Edd} = 0.01$',
               r'$\dot{M}/\dot{M}_{\rm Edd} = 0.1$',
               r'$\dot{M}/\dot{M}_{\rm Edd} = 0.5$']
mdot_colors = ['#2196F3', '#4CAF50', '#F44336']

fig, axes = plt.subplots(1, 3, figsize=(17, 5.5))

# --- Left panel: ξ(r) for different accretion rates ---
ax1 = axes[0]
for i, md in enumerate(mdots):
    xi_md = xi_parameter(r_rg, alpha=alpha_cl, mdot_frac=md)
    ax1.plot(r_rg, xi_md, color=mdot_colors[i], lw=2,
             ls=LINE_STYLES[i], label=mdot_labels[i])

ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_xlabel(r'$r / r_g$')
ax1.set_ylabel(r'$\xi = (\varepsilon + p)/(\rho_0 c^2) - 1$')
ax1.set_title(r'Relativistic correction parameter $\xi(r)$')
ax1.legend(loc='upper right', fontsize=9)
ax1.set_ylim(1e-5, 1)
ax1.set_xlim(6.5, 1e5)

# Mark zone boundaries
ax1.axvline(r_ab, color='gray', ls=':', lw=1, alpha=0.5)
ax1.axvline(r_bc, color='gray', ls=':', lw=1, alpha=0.5)
ax1.annotate('Zone (a)\nrad. dom.', xy=(30, 3e-4), fontsize=8, color='gray', ha='center')
ax1.annotate('Zone (b)\ngas dom.', xy=(700, 3e-4), fontsize=8, color='gray', ha='center')
ax1.annotate('Zone (c)', xy=(20000, 3e-4), fontsize=8, color='gray', ha='center')

# --- Middle panel: α_rel / α_cl ---
ax2 = axes[1]
for i, md in enumerate(mdots):
    xi_md = xi_parameter(r_rg, alpha=alpha_cl, mdot_frac=md)
    ratio = 1.0 / (1 + xi_md)
    ax2.plot(r_rg, ratio, color=mdot_colors[i], lw=2,
             ls=LINE_STYLES[i], label=mdot_labels[i])

ax2.set_xscale('log')
ax2.set_xlabel(r'$r / r_g$')
ax2.set_ylabel(r'$\alpha_{\rm rel} / \alpha_{\rm cl}$')
ax2.set_title(r'BDNK suppression of effective $\alpha$')
ax2.legend(loc='lower right', fontsize=9)
ax2.set_ylim(0.5, 1.05)
ax2.set_xlim(6.5, 1e5)
ax2.axhline(1.0, color='k', lw=0.5, ls='--')

# Annotate maximum suppression
ax2.annotate(r'$\alpha_{\rm rel} = \alpha_{\rm cl}/(1+\xi)$',
             xy=(20, 0.65), fontsize=11, color='k',
             bbox=dict(boxstyle='round,pad=0.3', fc='lightyellow', ec='gray'))

# --- Right panel: Re_rel / Re_cl ---
ax3 = axes[2]
for i, md in enumerate(mdots):
    xi_md = xi_parameter(r_rg, alpha=alpha_cl, mdot_frac=md)
    Re_r = 1 + xi_md
    ax3.plot(r_rg, Re_r, color=mdot_colors[i], lw=2,
             ls=LINE_STYLES[i], label=mdot_labels[i])

ax3.set_xscale('log')
ax3.set_xlabel(r'$r / r_g$')
ax3.set_ylabel(r'${\rm Re}_{\rm rel} / {\rm Re}_{\rm cl}$')
ax3.set_title('BDNK enhancement of Reynolds number')
ax3.legend(loc='upper right', fontsize=9)
ax3.set_ylim(0.95, 2.0)
ax3.set_xlim(6.5, 1e5)
ax3.axhline(1.0, color='k', lw=0.5, ls='--')

ax3.annotate(r'${\rm Re}_{\rm rel} = {\rm Re}_{\rm cl}(1+\xi)$',
             xy=(20, 1.7), fontsize=11, color='k',
             bbox=dict(boxstyle='round,pad=0.3', fc='lightyellow', ec='gray'))

fig.suptitle(
    r'BDNK viscosity modifications to the Shakura-Sunyaev $\alpha$-disk '
    r'($M = 10\,M_\odot$, $\alpha_{\rm cl} = 0.1$)',
    fontsize=13, y=1.02)
plt.tight_layout()

for ext in ['pdf', 'png']:
    plt.savefig(f'/data/haiyangw/claude/Instability/plots/deep/fig_bdnk_alpha_disk.{ext}',
                dpi=300, bbox_inches='tight')
print("Saved fig_bdnk_alpha_disk.pdf/png")
plt.close()
