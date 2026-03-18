"""
Full 7-wave characteristic structure of relativistic MHD:
  2 Alfven + 2 slow magnetosonic + 2 fast magnetosonic + 1 entropy
plotted as functions of the angle theta_Bk between the wavevector
and the background magnetic field, for neutron star magnetar parameters.

Physics:
- In relativistic MHD, the 7 characteristic speeds are the roots of
  the characteristic polynomial of the ideal MHD system.
- All speeds are bounded by c (causality), unlike the classical case
  where v_A can exceed c for strong fields.
- For magnetar parameters (B ~ 10^15-10^16 G), the Alfven speed
  approaches a significant fraction of c.

References:
  Anile, "Relativistic Fluids and Magneto-Fluids" (1989)
  Rezzolla & Zanotti, "Relativistic Hydrodynamics" (2013)
  Komissarov, MNRAS 303 (1999) 343
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# ============================================================
# Relativistic MHD characteristic speeds
# ============================================================
# The 7 characteristic speeds for propagation at angle theta to B:
#   +/- v_f (fast magnetosonic)
#   +/- v_A cos(theta) (Alfven)
#   +/- v_s (slow magnetosonic)
#   0 (entropy/contact)
#
# Fast and slow speeds from:
#   v^4 - v^2*(cs^2 + vA^2 - cs^2*vA^2/c^2) + cs^2*vA^2*cos^2(theta) = 0
#
# where cs = adiabatic sound speed, vA = relativistic Alfven speed

def rel_alfven_speed(B, eps, p):
    """Relativistic Alfven speed: vA^2 = b^2*c^2 / (4*pi*(eps+p) + b^2)
    where b^2 = B^2 (in Gaussian units, rest frame).
    """
    c2 = 1.0  # c=1 units
    b2 = B**2 / (4.0 * np.pi)
    w = eps + p
    return np.sqrt(b2 * c2 / (w + b2))

def magnetosonic_speeds(cs2, vA2, theta, c2=1.0):
    """Compute fast and slow magnetosonic speeds.

    v^4 - v^2*(cs^2 + vA^2 - cs^2*vA^2/c^2) + cs^2*vA^2*cos^2(theta) = 0
    """
    cos2 = np.cos(theta)**2

    # Coefficients of quadratic in v^2
    b_coeff = cs2 + vA2 - cs2 * vA2 / c2
    c_coeff = cs2 * vA2 * cos2

    discriminant = b_coeff**2 - 4.0 * c_coeff
    discriminant = np.maximum(discriminant, 0.0)  # numerical safety

    vf2 = 0.5 * (b_coeff + np.sqrt(discriminant))
    vs2 = 0.5 * (b_coeff - np.sqrt(discriminant))
    vs2 = np.maximum(vs2, 0.0)

    return np.sqrt(vf2), np.sqrt(vs2)


# ============================================================
# Magnetar parameters
# ============================================================
# Three cases: weak field, moderate magnetar, strong magnetar

# Neutron star matter: nuclear saturation density
# eps ~ 4 * 10^14 g/cm^3 * c^2, p ~ 0.1 * eps
# In natural units (c=1, 4*pi*G=1 not needed since we use ratios)

# We work in dimensionless units where c = 1

theta = np.linspace(0, np.pi/2, 500)

fig, axes = plt.subplots(1, 3, figsize=(16, 5.5), sharey=True)

# Parameters for three regimes
cases = [
    {
        'title': r'(a) Pulsar: $B = 10^{12}$ G',
        'cs2': 0.15,   # cs^2/c^2 for nuclear matter ~ nsat
        'vA_over_c': 0.005,  # vA/c ~ 0.005 for B=10^12 G
        'color_fast': '#1565C0',
        'color_alfven': '#2E7D32',
        'color_slow': '#E65100',
    },
    {
        'title': r'(b) Magnetar surface: $B = 10^{15}$ G',
        'cs2': 0.15,
        'vA_over_c': 0.45,  # vA/c for B~10^15 in outer crust
        'color_fast': '#1565C0',
        'color_alfven': '#2E7D32',
        'color_slow': '#E65100',
    },
    {
        'title': r'(c) Magnetar interior: $B = 10^{16}$ G',
        'cs2': 0.33,   # stiffer at higher density
        'vA_over_c': 0.8,  # magnetically dominated
        'color_fast': '#1565C0',
        'color_alfven': '#2E7D32',
        'color_slow': '#E65100',
    },
]

for ax, case in zip(axes, cases):
    cs2 = case['cs2']
    vA = case['vA_over_c']
    vA2 = vA**2

    # Compute 7 wave speeds
    vf, vs = magnetosonic_speeds(cs2, vA2, theta)
    va_proj = vA * np.abs(np.cos(theta))

    # Classical (non-relativistic) Alfven and fast speeds for comparison
    cs_class = np.sqrt(cs2)
    vA_class = vA / np.sqrt(1.0 - vA2) if vA < 0.99 else 10.0  # unbounded classically
    vf_class2 = cs2 + vA_class**2

    # Plot positive speeds (forward propagating)
    ax.plot(np.degrees(theta), vf, '-', lw=2.5, color=case['color_fast'],
            label=r'$v_{\rm f}$ (fast)')
    ax.plot(np.degrees(theta), va_proj, '-', lw=2.5, color=case['color_alfven'],
            label=r'$v_{\rm A}\cos\theta$ (Alfv\'en)')
    ax.plot(np.degrees(theta), vs, '-', lw=2.5, color=case['color_slow'],
            label=r'$v_{\rm s}$ (slow)')

    # Negative speeds (backward propagating) - mirror
    ax.plot(np.degrees(theta), -vf, '-', lw=1.5, color=case['color_fast'], alpha=0.4)
    ax.plot(np.degrees(theta), -va_proj, '-', lw=1.5, color=case['color_alfven'], alpha=0.4)
    ax.plot(np.degrees(theta), -vs, '-', lw=1.5, color=case['color_slow'], alpha=0.4)

    # Entropy wave (zero speed in fluid frame)
    ax.axhline(y=0, ls='-', lw=1.5, color='gray', alpha=0.5, label='Entropy')

    # Light speed bound
    ax.axhline(y=1.0, ls='--', lw=1.5, color='black', alpha=0.6)
    ax.axhline(y=-1.0, ls='--', lw=1.5, color='black', alpha=0.6)
    ax.fill_between(np.degrees(theta), 1.0, 1.15, alpha=0.1, color='red')
    ax.fill_between(np.degrees(theta), -1.0, -1.15, alpha=0.1, color='red')

    # Sound speed reference
    ax.axhline(y=np.sqrt(cs2), ls=':', lw=1.0, color='gray', alpha=0.4)

    # Classical fast speed (can be superluminal)
    if vA_class < 3.0:
        vf_class = np.sqrt(cs2 + vA_class**2 - cs2 * vA_class**2)
        # This is the NR formula: vf_NR = sqrt(cs^2 + vA_NR^2)
        vf_NR = np.sqrt(cs2 + vA_class**2) * np.ones_like(theta)
        if np.max(vf_NR) > 1.01:
            ax.plot(np.degrees(theta), np.minimum(vf_NR, 1.14),
                    ':', lw=1.8, color=case['color_fast'], alpha=0.5,
                    label=r'$v_{\rm f}^{\rm NR}$ (classical)')

    ax.set_xlabel(r'$\theta_{Bk}$ [degrees]', fontsize=12)
    ax.set_title(case['title'], fontsize=12)
    ax.set_xlim(0, 90)

    if ax == axes[0]:
        ax.set_ylabel(r'Characteristic speed $v/c$', fontsize=12)
        ax.legend(loc='lower left', fontsize=8.5, ncol=1, framealpha=0.9)

axes[0].set_ylim(-1.15, 1.15)

# Annotate light speed
axes[2].text(45, 1.06, r'$c$ (causal limit)', fontsize=9, ha='center',
             color='red', style='italic')
axes[2].text(45, -1.06, r'$-c$', fontsize=9, ha='center',
             color='red', style='italic')

# Add labels for the 7 waves on the rightmost panel
ax3 = axes[2]
ax3.annotate('7 waves total:\n2 fast + 2 Alfv. + 2 slow + 1 entropy',
             xy=(65, 0.5), fontsize=8.5, ha='center',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow',
                       edgecolor='gray', alpha=0.9))

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_mhd_7wave_structure.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_mhd_7wave_structure.png')
print("Saved fig_mhd_7wave_structure.pdf/png")
