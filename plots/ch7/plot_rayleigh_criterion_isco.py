"""
Plot: Relativistic Rayleigh criterion near ISCO for Keplerian accretion disks.
Shows the relativistic specific angular momentum tilde{ell}^2 vs r/r_g for
Schwarzschild and Kerr black holes, highlighting the ISCO where d(tilde{ell}^2)/dr=0.
Agent 24, sec64-66.
"""
import sys; sys.path.insert(0, '../..'); from SHARED_PLOT_STYLE import setup_style, COLORS, LINE_STYLES
setup_style()

import numpy as np
import matplotlib.pyplot as plt

# Gravitational radius
# We work in units of r_g = GM/c^2, so r_g = 1

def ell_squared_schwarzschild(r):
    """Relativistic specific angular momentum squared for Schwarzschild Keplerian orbit.
    tilde{ell}^2 = gamma^4 r^4 Omega^2, for Keplerian geodesic in Schwarzschild.
    For test particle: ell^2 = r^2 M / (r - 2M) in geometric units (G=c=1, M=1).
    Here r in units of r_g = GM/c^2, so r_Schw = r * r_g.
    ell^2 = r * r_g / (1 - 3 r_g/r) ... using Schwarzschild circular orbit.
    Actually ell = L/E = r^2 Omega_K / (1 - 2M/r) etc.
    Specific angular momentum: l^2 = M r^2 / (r - 3M) for Schwarzschild, r in units of M.
    """
    # r in units of r_g = GM/c^2. Schwarzschild metric: r_s = 2 r_g.
    # Circular geodesic: l^2 = M r^2 / (r - 3M) with r in Schwarzschild coords, M = r_g (geom units c=G=1)
    # Using r in units of r_g: l^2 = r_g * (r * r_g)^2 / (r * r_g - 3 * r_g) = r_g^3 * r^2/(r-3)
    # We normalise by r_g^3 so: l^2 / r_g^3 = r^2 / (r - 3)
    mask = r > 3.0
    result = np.full_like(r, np.nan)
    result[mask] = r[mask]**2 / (r[mask] - 3.0)
    return result

def ell_squared_kerr(r, a_star):
    """Specific angular momentum squared for prograde Kerr circular geodesic.
    l = (r^2 - 2a sqrt(r) + a^2) / (sqrt(r) * (r - 3 + 2a/sqrt(r))^{1/2} * sqrt(r))
    Using Boyer-Lindquist coords, r in units of M (= r_g in geom units).
    l = (r^2 - 2*a*sqrt(r) + a^2) / (sqrt(r) * Delta_r^{1/2})
    where Delta_r = r^{3/2} - 3*r^{1/2} + 2*a
    Simpler: l(r, a) for prograde Kerr:
    l = sqrt(M) * (r^2 - 2a*sqrt(M*r) + a^2) / (r^{3/4} * sqrt(r^{3/2} - 3M*r^{1/2} + 2*a*sqrt(M)))
    In units M=1: l = (r^2 - 2*a*sqrt(r) + a^2) / (r^{3/4} * sqrt(r^{3/2} - 3*sqrt(r) + 2*a))
    """
    sr = np.sqrt(r)
    denom_inner = r**1.5 - 3.0 * sr + 2.0 * a_star
    mask = denom_inner > 0
    result = np.full_like(r, np.nan)
    numer = r**2 - 2.0 * a_star * sr[mask] + a_star**2
    denom = sr[mask] * np.sqrt(r[mask]) * np.sqrt(denom_inner[mask])
    # Actually the standard expression: l = (r^2 - 2a sqrt(r) + a^2) / (r^{3/4} sqrt(r^{3/2} - 3r^{1/2} + 2a))
    l_val = (r[mask]**2 - 2*a_star*np.sqrt(r[mask]) + a_star**2) / (r[mask]**0.75 * np.sqrt(denom_inner[mask]))
    result[mask] = l_val**2
    return result

def isco_schwarzschild():
    return 6.0

def isco_kerr(a_star):
    """ISCO radius for prograde orbits in Kerr, r in units of M."""
    Z1 = 1 + (1 - a_star**2)**(1/3) * ((1 + a_star)**(1/3) + (1 - a_star)**(1/3))
    Z2 = np.sqrt(3 * a_star**2 + Z1**2)
    return 3 + Z2 - np.sqrt((3 - Z1) * (3 + Z1 + 2*Z2))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# Left panel: tilde{ell}^2 vs r/r_g
r = np.linspace(3.01, 30, 500)

# Schwarzschild
l2_schw = ell_squared_schwarzschild(r)
ax1.plot(r, l2_schw, color=COLORS['classical'], linewidth=2, label=r'Schwarzschild ($a/M=0$)')

# Kerr a=0.5
a05 = 0.5
r_kerr05 = np.linspace(isco_kerr(a05)*0.98, 30, 500)
l2_k05 = ell_squared_kerr(r_kerr05, a05)
ax1.plot(r_kerr05, l2_k05, color=COLORS['accretion'], linewidth=2, linestyle='--',
         label=r'Kerr ($a/M=0.5$)')

# Kerr a=0.998
a998 = 0.998
r_kerr998 = np.linspace(isco_kerr(a998)*0.98, 30, 500)
l2_k998 = ell_squared_kerr(r_kerr998, a998)
ax1.plot(r_kerr998, l2_k998, color=COLORS['relativistic'], linewidth=2, linestyle='-.',
         label=r'Kerr ($a/M=0.998$)')

# Mark ISCOs
for a_star, col, marker in [(0, COLORS['classical'], 'o'),
                             (0.5, COLORS['accretion'], 's'),
                             (0.998, COLORS['relativistic'], 'D')]:
    r_isco = isco_schwarzschild() if a_star == 0 else isco_kerr(a_star)
    l2_isco = ell_squared_schwarzschild(np.array([r_isco]))[0] if a_star == 0 else ell_squared_kerr(np.array([r_isco]), a_star)[0]
    if not np.isnan(l2_isco):
        ax1.plot(r_isco, l2_isco, marker=marker, color=col, markersize=10, zorder=5,
                 markeredgecolor='black', markeredgewidth=1)
    ax1.axvline(r_isco, color=col, alpha=0.3, linestyle=':')

ax1.set_xlabel(r'$r / r_g$', fontsize=14)
ax1.set_ylabel(r'$\tilde{\ell}^2 / r_g^3$', fontsize=14)
ax1.set_title(r'Relativistic specific angular momentum $\tilde{\ell}^2(r)$', fontsize=13)
ax1.legend(fontsize=10, loc='upper left')
ax1.set_xlim(1, 30)
ax1.set_ylim(0, 50)
ax1.annotate('ISCO', xy=(6.0, 12), fontsize=10, color=COLORS['classical'],
             ha='center')

# Right panel: d(tilde{ell}^2)/dr — Rayleigh stability indicator
r_fine = np.linspace(3.5, 25, 1000)
dl2_schw = np.gradient(ell_squared_schwarzschild(r_fine), r_fine)
ax2.plot(r_fine, dl2_schw, color=COLORS['classical'], linewidth=2,
         label=r'Schwarzschild ($a/M=0$)')

for a_star, col, ls in [(0.5, COLORS['accretion'], '--'), (0.998, COLORS['relativistic'], '-.')]:
    r_k = np.linspace(isco_kerr(a_star)+0.01, 25, 1000)
    l2_k = ell_squared_kerr(r_k, a_star)
    dl2_k = np.gradient(l2_k, r_k)
    ax2.plot(r_k, dl2_k, color=col, linewidth=2, linestyle=ls,
             label=f'Kerr ($a/M={a_star}$)')

ax2.axhline(0, color='black', linewidth=0.8, linestyle='-')
ax2.fill_between([1, 25], [-5, -5], [0, 0], alpha=0.08, color='red', label='Rayleigh unstable')
ax2.set_xlabel(r'$r / r_g$', fontsize=14)
ax2.set_ylabel(r'$\mathrm{d}(\tilde{\ell}^2)/\mathrm{d}r$', fontsize=14)
ax2.set_title('Relativistic Rayleigh criterion', fontsize=13)
ax2.legend(fontsize=10, loc='upper right')
ax2.set_xlim(1, 25)
ax2.set_ylim(-2, 8)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/ch7/fig_rayleigh_criterion_isco.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/ch7/fig_rayleigh_criterion_isco.png')
plt.close()
print("Saved fig_rayleigh_criterion_isco.pdf/png")
