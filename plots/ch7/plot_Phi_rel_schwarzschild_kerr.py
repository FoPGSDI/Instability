"""
Plot: Relativistic Rayleigh discriminant Phi_rel(r) for Schwarzschild and Kerr
black holes, demonstrating stability of inviscid disk flow.
Agent 25, sec67.
"""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')); from SHARED_PLOT_STYLE import setup_style, COLORS, LINE_STYLES
setup_style()

import numpy as np
import matplotlib.pyplot as plt

def Omega_K_schw(r):
    """Keplerian angular velocity in Schwarzschild, r in units of M (= r_g)."""
    return 1.0 / (r**1.5 + 0.0)  # Omega_K = sqrt(M/r^3) * 1/(1-3M/r)^{1/2} but simplified: Omega = 1/r^{3/2} in geom units

def Omega_K_kerr(r, a):
    """Keplerian angular velocity in Kerr (prograde), r in units of M."""
    return 1.0 / (r**1.5 + a)

def Phi_rel_geodesic(r, a=0):
    """Relativistic Rayleigh discriminant for Keplerian geodesic flow.
    Phi_rel = (2 Omega / r) * d(gamma^2 r^2 Omega)/dr
    For geodesic motion in Schwarzschild:
    kappa_r^2 = Omega_K^2 (1 - 6/r) and Phi_rel ~ kappa_r^2
    More precisely Phi_rel = kappa_r^2 for the Schwarzschild case.
    For Kerr: kappa_r^2 = Omega_K^2 (1 - 6/r + 8a/(r^{3/2}) - 3a^2/r^2)
    """
    if a == 0:
        Omega = 1.0 / r**1.5
        kappa_r2 = Omega**2 * (1 - 6.0/r)
    else:
        Omega = 1.0 / (r**1.5 + a)
        kappa_r2 = Omega**2 * (1 - 6.0/r + 8.0*a/r**1.5 - 3.0*a**2/r**2)
    return kappa_r2

def isco_kerr(a_star):
    Z1 = 1 + (1 - a_star**2)**(1/3) * ((1 + a_star)**(1/3) + (1 - a_star)**(1/3))
    Z2 = np.sqrt(3 * a_star**2 + Z1**2)
    return 3 + Z2 - np.sqrt((3 - Z1) * (3 + Z1 + 2*Z2))

fig, ax = plt.subplots(figsize=(9, 6))

spins = [
    (0.0, 'Schwarzschild ($a/M=0$)', COLORS['classical'], '-'),
    (0.5, 'Kerr ($a/M=0.5$)', COLORS['accretion'], '--'),
    (0.9, 'Kerr ($a/M=0.9$)', COLORS['data'], '-.'),
    (0.998, 'Kerr ($a/M=0.998$)', COLORS['relativistic'], ':'),
]

for a_star, label, color, ls in spins:
    r_isco = 6.0 if a_star == 0 else isco_kerr(a_star)
    r = np.linspace(r_isco * 0.85, 25, 500)
    Phi = Phi_rel_geodesic(r, a_star)
    # Normalise by Omega_K^2 at r=10 for comparison
    Omega_10 = 1.0 / (10**1.5 + a_star)
    ax.plot(r, Phi / Omega_10**2, color=color, linewidth=2.2, linestyle=ls, label=label)
    # Mark ISCO
    ax.plot(r_isco, 0, 'o', color=color, markersize=8, markeredgecolor='black',
            markeredgewidth=0.8, zorder=5)

ax.axhline(0, color='black', linewidth=0.8)
ax.fill_between([1, 25], [-0.5, -0.5], [0, 0], alpha=0.08, color='red')
ax.text(2.5, -0.15, 'Unstable\n' + r'($\Phi_{\mathrm{rel}} < 0$)', fontsize=11,
        color='red', ha='center', style='italic')
ax.text(15, 0.3, 'Stable\n' + r'($\Phi_{\mathrm{rel}} > 0$)', fontsize=11,
        color='green', ha='center', style='italic')

ax.set_xlabel(r'$r / r_g$', fontsize=14)
ax.set_ylabel(r'$\Phi_{\mathrm{rel}}(r) / \Omega_K^2(10\,r_g)$', fontsize=14)
ax.set_title(r'Relativistic Rayleigh discriminant $\Phi_{\mathrm{rel}}(r)$ for Keplerian flow', fontsize=13)
ax.legend(fontsize=11, loc='upper right')
ax.set_xlim(1, 25)
ax.set_ylim(-0.4, 1.2)

# Annotate ISCOs
ax.annotate(r'ISCO ($6\,r_g$)', xy=(6.0, 0), xytext=(8, -0.25),
            arrowprops=dict(arrowstyle='->', color=COLORS['classical']),
            fontsize=10, color=COLORS['classical'])
r_isco_998 = isco_kerr(0.998)
ax.annotate(f'ISCO ({r_isco_998:.2f}' + r'$\,r_g$)', xy=(r_isco_998, 0), xytext=(3.5, -0.32),
            arrowprops=dict(arrowstyle='->', color=COLORS['relativistic']),
            fontsize=10, color=COLORS['relativistic'])

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/ch7/fig_Phi_rel_schwarzschild_kerr.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/ch7/fig_Phi_rel_schwarzschild_kerr.png')
plt.close()
print("Saved fig_Phi_rel_schwarzschild_kerr.pdf/png")
