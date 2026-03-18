"""
Plot: QPO-relevant epicyclic oscillation frequencies vs r/r_g for
Kerr black holes with a/M = 0, 0.5, 0.998.
Shows radial (kappa_r), vertical (kappa_z), and orbital (Omega_K) frequencies.
Agent 26, sec68.
"""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')); from SHARED_PLOT_STYLE import setup_style, COLORS, LINE_STYLES
setup_style()

import numpy as np
import matplotlib.pyplot as plt

def isco_kerr(a_star):
    Z1 = 1 + (1 - a_star**2)**(1/3) * ((1 + a_star)**(1/3) + (1 - a_star)**(1/3))
    Z2 = np.sqrt(3 * a_star**2 + Z1**2)
    return 3 + Z2 - np.sqrt((3 - Z1) * (3 + Z1 + 2*Z2))

def frequencies_kerr(r, a):
    """Epicyclic frequencies for prograde Kerr orbits, in units of c^3/(GM).
    Omega_K = 1/(r^{3/2} + a)
    kappa_r^2 = Omega_K^2 (1 - 6/r + 8a/r^{3/2} - 3a^2/r^2)
    kappa_z^2 = Omega_K^2 (1 - 4a/r^{3/2} + 3a^2/r^2)
    """
    Omega = 1.0 / (r**1.5 + a)
    kr2 = Omega**2 * (1 - 6.0/r + 8.0*a/r**1.5 - 3.0*a**2/r**2)
    kz2 = Omega**2 * (1 - 4.0*a/r**1.5 + 3.0*a**2/r**2)
    return Omega, np.sqrt(np.maximum(kr2, 0)), np.sqrt(np.maximum(kz2, 0)), kr2

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

spin_params = [
    (0.0, r'$a/M = 0$ (Schwarzschild)'),
    (0.5, r'$a/M = 0.5$'),
    (0.998, r'$a/M = 0.998$'),
]

for idx, (a_star, title) in enumerate(spin_params):
    ax = axes[idx]
    r_isco = 6.0 if a_star == 0 else isco_kerr(a_star)
    r = np.linspace(r_isco, 30, 500)

    Omega, kr, kz, kr2 = frequencies_kerr(r, a_star)

    # Convert to Hz for a 10 M_sun black hole: f = (c^3/(2*pi*G*M)) * omega_dimless
    # c^3/(G * 10 M_sun) = 2.03e4 Hz
    scale = 2.03e4 / (2 * np.pi)  # to Hz for 10 M_sun
    # Actually let's keep dimensionless: plot nu = omega/(2pi) * (GM/c^3)^{-1} but in kHz for 10Msun
    f_scale = 1.0 / (2*np.pi) * 3.23e4  # c^3/(2 pi G M) for M=10 Msun in Hz -> 3231 Hz ... let me compute properly
    # c^3/(GM) = 2.03e5 / (M/Msun) rad/s. For 10 Msun: 2.03e4 rad/s
    # nu = Omega * c^3/(2 pi GM) Hz. For M=10Msun: nu = Omega * 2.03e4/(2pi) = Omega * 3231 Hz
    f_Hz = 3231.0  # Hz per unit of c^3/(GM) / (2pi) for 10 M_sun

    ax.plot(r, Omega * f_Hz, color=COLORS['classical'], linewidth=2, label=r'$\Omega_K$')
    ax.plot(r, kr * f_Hz, color=COLORS['relativistic'], linewidth=2, linestyle='--', label=r'$\kappa_r$')
    ax.plot(r, kz * f_Hz, color=COLORS['accretion'], linewidth=2, linestyle='-.', label=r'$\kappa_z$')

    # Mark ISCO
    ax.axvline(r_isco, color='gray', linestyle=':', alpha=0.6)
    ax.text(r_isco + 0.3, ax.get_ylim()[1] if idx > 0 else 700, 'ISCO',
            fontsize=9, color='gray', rotation=90, va='top')

    # Mark max of kappa_r
    if len(kr) > 0:
        idx_max = np.argmax(kr)
        r_max = r[idx_max]
        kr_max = kr[idx_max] * f_Hz
        ax.plot(r_max, kr_max, 'v', color=COLORS['relativistic'], markersize=8)
        ax.annotate(f'{kr_max:.0f} Hz', xy=(r_max, kr_max),
                    xytext=(r_max+2, kr_max+50), fontsize=9,
                    arrowprops=dict(arrowstyle='->', color=COLORS['relativistic']))

    ax.set_xlabel(r'$r / r_g$', fontsize=13)
    if idx == 0:
        ax.set_ylabel(r'Frequency (Hz) for $M = 10\,M_\odot$', fontsize=13)
    ax.set_title(title, fontsize=12)
    ax.legend(fontsize=10, loc='upper right')
    ax.set_xlim(max(1, r_isco - 1), 25)
    ax.set_ylim(0, 1200 if a_star < 0.9 else 3000)

plt.suptitle('Epicyclic frequencies and QPO predictions in Kerr spacetime', fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/ch7/fig_epicyclic_frequencies_qpo.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/ch7/fig_epicyclic_frequencies_qpo.png')
plt.close()
print("Saved fig_epicyclic_frequencies_qpo.pdf/png")
