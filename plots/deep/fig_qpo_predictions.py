"""
QPO frequency predictions for GRS 1915+105 and GRO J1655-40.

Plot radial (f_r) and vertical (f_θ) epicyclic frequencies versus r
for two well-studied X-ray binaries. Observed twin-peak QPO frequencies
are marked with horizontal bands.

Sources:
  GRS 1915+105: M ≈ 14 M☉, a/M ≈ 0.98 (McClintock et al. 2006)
    Observed QPOs: ~67 Hz and ~113 Hz (twin peaks, 3:2 ratio)
  GRO J1655-40: M ≈ 6.3 M☉, a/M ≈ 0.70 (Beer & Podsiadlowski 2002)
    Observed QPOs: ~300 Hz and ~450 Hz (twin peaks, 3:2 ratio)

References:
  - Abramowicz & Kluzniak (2001), A&A 374, L19
  - Kato & Fukue (1980), PASJ 32, 377
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, LINE_STYLES, c_cgs, G_cgs, M_sun
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# --- Physical parameters ---
sources = {
    'GRS 1915+105': {
        'M': 14.0 * M_sun,  # grams
        'a_star': 0.98,
        'qpo_lower': 67.0,   # Hz
        'qpo_upper': 113.0,  # Hz
        'qpo_err': 5.0,      # Hz uncertainty
        'color': '#F44336',
    },
    'GRO J1655-40': {
        'M': 6.3 * M_sun,
        'a_star': 0.70,
        'qpo_lower': 300.0,
        'qpo_upper': 450.0,
        'qpo_err': 10.0,
        'color': '#2196F3',
    },
}


def isco_radius(a):
    """ISCO radius for Kerr (prograde), units G=M=c=1."""
    z1 = 1 + (1 - a**2)**(1/3) * ((1 + a)**(1/3) + (1 - a)**(1/3))
    z2 = np.sqrt(3 * a**2 + z1**2)
    return 3 + z2 - np.sqrt((3 - z1) * (3 + z1 + 2 * z2))


def epicyclic_freqs_hz(r_over_M, a_star, M_grams):
    """Compute f_r, f_θ, f_φ in Hz for Kerr geodesics.
    r_over_M: radius in units of GM/c²
    Returns (f_r, f_theta, f_phi) in Hz.
    """
    r = r_over_M
    a = a_star
    # Orbital frequency (geometrized units, M=1)
    Omega = 1.0 / (r**1.5 + a)
    # Convert to Hz: Omega_phys = Omega * c³/(GM)
    freq_scale = c_cgs**3 / (G_cgs * M_grams) / (2 * np.pi)
    f_phi = Omega * freq_scale

    # Radial epicyclic
    kr2_over_Om2 = 1 - 6.0/r + 8*a/r**1.5 - 3*a**2/r**2
    kr2 = kr2_over_Om2 * Omega**2
    f_r = np.where(kr2 > 0, np.sqrt(kr2) * freq_scale, np.nan)

    # Vertical epicyclic
    kz2_over_Om2 = 1 - 4*a/r**1.5 + 3*a**2/r**2
    kz2 = kz2_over_Om2 * Omega**2
    f_theta = np.where(kz2 > 0, np.sqrt(kz2) * freq_scale, np.nan)

    return f_r, f_theta, f_phi


fig, axes = plt.subplots(1, 2, figsize=(14, 6))

for idx, (name, params) in enumerate(sources.items()):
    ax = axes[idx]
    a = params['a_star']
    M = params['M']
    r_is = isco_radius(a)

    r = np.linspace(r_is * 1.001, 50, 2000)
    f_r, f_theta, f_phi = epicyclic_freqs_hz(r, a, M)

    # Plot frequencies
    ax.plot(r, f_r, color='#F44336', lw=2.2, label=r'$f_r$ (radial)')
    ax.plot(r, f_theta, color='#2196F3', lw=2.2, ls='--',
            label=r'$f_\theta$ (vertical)')
    ax.plot(r, f_phi, color='#4CAF50', lw=1.5, ls='-.',
            label=r'$f_\phi$ (orbital)')

    # Mark ISCO
    ax.axvline(r_is, color='gray', lw=1.2, ls=':', alpha=0.7)
    ax.annotate('ISCO', xy=(r_is, ax.get_ylim()[0]),
                xytext=(r_is + 0.5, 0.85 * max(np.nanmax(f_phi[:100]), 500)),
                fontsize=10, color='gray')

    # Mark observed QPO frequencies as horizontal bands
    qpo_lo = params['qpo_lower']
    qpo_hi = params['qpo_upper']
    qpo_err = params['qpo_err']

    ax.axhspan(qpo_lo - qpo_err, qpo_lo + qpo_err,
               alpha=0.2, color='#FF9800', zorder=0)
    ax.axhspan(qpo_hi - qpo_err, qpo_hi + qpo_err,
               alpha=0.2, color='#9C27B0', zorder=0)

    ax.annotate(f'Observed lower QPO\n({qpo_lo} Hz)',
                xy=(35, qpo_lo), fontsize=9, color='#FF9800',
                ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#FF9800', alpha=0.8))
    ax.annotate(f'Observed upper QPO\n({qpo_hi} Hz)',
                xy=(35, qpo_hi), fontsize=9, color='#9C27B0',
                ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#9C27B0', alpha=0.8))

    ax.set_xlabel(r'$r\;[GM/c^2]$')
    ax.set_ylabel('Frequency [Hz]')
    ax.set_title(f'{name}\n' + r'$M = {:.1f}\,M_\odot$, $a/M = {:.2f}$'.format(
        params['M'] / M_sun, a))
    ax.set_xlim(r_is * 0.95, 50)
    y_max = max(np.nanmax(f_phi[:200]), qpo_hi * 2)
    ax.set_ylim(0, min(y_max, 2000))
    ax.legend(loc='upper right', fontsize=10)

fig.suptitle(
    'Epicyclic frequency predictions vs observed twin-peak QPOs',
    fontsize=14, y=1.02)
plt.tight_layout()

for ext in ['pdf', 'png']:
    plt.savefig(f'/data/haiyangw/claude/Instability/plots/deep/fig_qpo_predictions.{ext}',
                dpi=300, bbox_inches='tight')
print("Saved fig_qpo_predictions.pdf/png")
plt.close()
