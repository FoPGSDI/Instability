"""
Rayleigh criterion near the ISCO for Kerr black holes.

Plot the specific angular momentum ℓ(r) and epicyclic frequency κ²(r)
for Schwarzschild and Kerr spacetimes with a/M = 0, 0.5, 0.9, 0.998.
Identifies where dℓ/dr = 0 (the ISCO) for each spin value.

Reference: Bardeen, Press & Teukolsky (1972), ApJ 178, 347.
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, LINE_STYLES
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# --- Kerr geodesic quantities ---
# Use Boyer-Lindquist coordinates, units G = M = c = 1
# Prograde orbits only.

def isco_radius(a):
    """ISCO radius for Kerr BH with spin parameter a (prograde).
    Bardeen, Press & Teukolsky (1972), Eq. (2.21)."""
    z1 = 1 + (1 - a**2)**(1/3) * ((1 + a)**(1/3) + (1 - a)**(1/3))
    z2 = np.sqrt(3 * a**2 + z1**2)
    return 3 + z2 - np.sqrt((3 - z1) * (3 + z1 + 2 * z2))

def omega_kerr(r, a):
    """Orbital angular velocity for circular geodesic in Kerr."""
    return 1.0 / (r**1.5 + a)

def specific_angular_momentum(r, a):
    """Specific angular momentum ℓ = u_φ for circular geodesic in Kerr.
    ℓ = (r² - 2a√r + a²) / (r^{3/4} √(r^{3/2} - 3r^{1/2} + 2a))
    More precisely, from Bardeen+1972:
    ℓ = √M (r² - 2a√(Mr) + a²) / (r^{3/4} (r^{3/2} - 3M r^{1/2} + 2a√M)^{1/2})
    In units M=1:
    """
    sqr = np.sqrt(r)
    num = r**2 - 2 * a * sqr + a**2
    denom_sq = r**1.5 - 3 * sqr + 2 * a  # = r^{3/2} - 3r^{1/2} + 2a (M=1)
    # Only valid for r > r_ph (photon orbit)
    mask = denom_sq > 0
    result = np.full_like(r, np.nan)
    result[mask] = num[mask] / (r[mask]**0.75 * np.sqrt(denom_sq[mask]))
    return result

def kappa_r_squared(r, a):
    """Radial epicyclic frequency squared κ_r² for Kerr, in units of M.
    κ_r² = Ω_K² (1 - 6/r + 8a/r^{3/2} - 3a²/r²)
    """
    Om2 = omega_kerr(r, a)**2
    return Om2 * (1 - 6.0/r + 8*a/r**1.5 - 3*a**2/r**2)

def kappa_theta_squared(r, a):
    """Vertical epicyclic frequency squared κ_θ² for Kerr.
    κ_θ² = Ω_K² (1 - 4a/r^{3/2} + 3a²/r²)
    """
    Om2 = omega_kerr(r, a)**2
    return Om2 * (1 - 4*a/r**1.5 + 3*a**2/r**2)


# --- Spin values ---
spins = [0.0, 0.5, 0.9, 0.998]
colors = ['#2196F3', '#4CAF50', '#FF9800', '#F44336']
labels = [r'$a/M = 0$ (Schwarzschild)', r'$a/M = 0.5$',
          r'$a/M = 0.9$', r'$a/M = 0.998$']

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# --- Left panel: specific angular momentum ℓ(r) ---
ax1 = axes[0]
for i, a in enumerate(spins):
    r_is = isco_radius(a)
    # Radial range: from just outside photon orbit to 30M
    r_ph = 2 * (1 + np.cos(2/3 * np.arccos(-a)))  # prograde photon orbit
    r_min = max(r_is * 0.85, r_ph + 0.05)
    r = np.linspace(r_min, 30, 1000)
    ell = specific_angular_momentum(r, a)

    ax1.plot(r, ell, color=colors[i], ls=LINE_STYLES[i % len(LINE_STYLES)],
             label=labels[i], lw=2)
    # Mark ISCO
    ell_isco = specific_angular_momentum(np.array([r_is]), a)[0]
    ax1.plot(r_is, ell_isco, 'o', color=colors[i], ms=8, zorder=5,
             markeredgecolor='k', markeredgewidth=0.8)

ax1.set_xlabel(r'$r / M$')
ax1.set_ylabel(r'$\ell(r)$ [specific angular momentum, units $M$]')
ax1.set_title(r'Specific angular momentum $\ell(r)$')
ax1.set_xlim(0.5, 30)
ax1.set_ylim(1.5, 6)
ax1.legend(loc='upper right', fontsize=10)
ax1.axhline(0, color='k', lw=0.5)

# --- Right panel: κ²(r) radial epicyclic frequency ---
ax2 = axes[1]
for i, a in enumerate(spins):
    r_is = isco_radius(a)
    r_ph = 2 * (1 + np.cos(2/3 * np.arccos(-a)))
    r_min = max(r_is * 0.7, r_ph + 0.05)
    r = np.linspace(r_min, 30, 1000)
    kr2 = kappa_r_squared(r, a)

    ax2.plot(r, kr2, color=colors[i], ls=LINE_STYLES[i % len(LINE_STYLES)],
             label=labels[i], lw=2)
    # Mark ISCO where κ² = 0
    ax2.plot(r_is, 0.0, 'o', color=colors[i], ms=8, zorder=5,
             markeredgecolor='k', markeredgewidth=0.8)

ax2.set_xlabel(r'$r / M$')
ax2.set_ylabel(r'$\kappa_r^2(r)$ [$M^{-2}$]')
ax2.set_title(r'Radial epicyclic frequency $\kappa_r^2(r)$')
ax2.set_xlim(0.5, 30)
ax2.axhline(0, color='k', lw=0.5, ls='--')
ax2.legend(loc='upper right', fontsize=10)

# Shade unstable region
ax2.fill_between([0.5, 30], [-0.01, -0.01], [0, 0],
                 alpha=0.08, color='red', zorder=0)
ax2.annotate('Rayleigh unstable\n' + r'$(\kappa_r^2 < 0)$',
             xy=(15, -0.003), fontsize=10, color='red', ha='center')

fig.suptitle(
    'Rayleigh criterion near the ISCO: Schwarzschild and Kerr spacetimes',
    fontsize=14, y=1.02)
plt.tight_layout()

for ext in ['pdf', 'png']:
    plt.savefig(f'/data/haiyangw/claude/Instability/plots/deep/fig_isco_rayleigh_kerr.{ext}',
                dpi=300, bbox_inches='tight')
print("Saved fig_isco_rayleigh_kerr.pdf/png")
plt.close()
