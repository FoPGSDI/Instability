"""
Magnetar QPO spectrum: torsional oscillation modes with BDNK damping.

Computes the fundamental and overtone torsional mode frequencies for
a magnetar crust model, with BDNK viscous damping rates.
Compares computed frequencies with observed SGR 1806-20 QPOs.
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, G_cgs, M_sun, k_B, m_p, pi
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# ---- Magnetar parameters ----
M_ns = 1.4 * M_sun
R_ns = 12e5       # cm
B_dip = 1e15      # G (magnetar-strength field)
rho_crust = 1e14  # g/cm^3 (inner crust average)
Delta_R = 1e5     # cm (1 km crust thickness)

# Shear modulus of NS crust (Coulomb lattice)
# mu_s ~ 0.1 * n_i * (Ze)^2 / a  where a = (3/(4 pi n_i))^{1/3}
# Approximate: mu_s ~ 1e29 - 1e30 erg/cm^3
mu_s = 3e29  # erg/cm^3

# Shear wave speed in crust
v_s = np.sqrt(mu_s / rho_crust)  # ~ 1.7e7 cm/s

# Alfven speed in crust
v_A = B_dip / np.sqrt(4 * pi * rho_crust)  # ~ 5.6e8 cm/s

# ---- Torsional oscillation frequencies ----
# Fundamental: f_0 ~ v_s / (2 * Delta_R)  or coupled magneto-elastic
# Overtones: f_n ~ (n+1) * f_0 for pure crustal modes
# For magnetically coupled modes: additional continuum spectrum

# Pure crustal torsional modes (l=2)
f_0_crust = v_s / (2 * Delta_R)  # ~ 85 Hz

# Magneto-elastic frequencies (Hansen & Cioffi 1980, Samuelsson & Andersson 2007)
# f_{n,l} = f_0 * sqrt((n+1)^2 + (v_A/v_s)^2 * l*(l+1)/(4*pi))
# For l=2: correction factor
mag_factor = (v_A / v_s)**2 * 2 * 3 / (4 * pi)

# Compute mode spectrum
n_modes = 15
l_values = [2, 4, 7, 10, 13]

computed_freqs = {}
for l in l_values:
    mag_l = (v_A / v_s)**2 * l * (l + 1) / (4 * pi)
    freqs = []
    for n in range(n_modes):
        f = f_0_crust * np.sqrt((n + 1)**2 + mag_l)
        freqs.append(f)
    computed_freqs[l] = np.array(freqs)

# ---- BDNK damping rates ----
# Viscous damping of torsional modes:
# gamma_visc = eta_s * k^2 / (rho * w/c^2)  where w = epsilon + p
# In BDNK: gamma_BDNK = gamma_NS * (1 + correction from frame coefficients)
# For NS crust at T ~ 10^8 K:
T_crust = 1e8  # K
eta_s_crust = 2e18 * (rho_crust / 1e14)**(9.0/4.0) * (T_crust / 1e9)**(-2)

# Damping rate: gamma ~ (n+1)^2 * pi^2 * eta_s / (rho * Delta_R^2)
enthalpy_factor = 1.0 + 0.1  # w/(rho c^2) ~ 1.1 for NS crust

# BDNK damping (no relaxation artifacts)
def gamma_BDNK(f_mode, n):
    k_n = (n + 1) * pi / Delta_R
    return eta_s_crust * k_n**2 / (rho_crust * enthalpy_factor)

# IS damping (with relaxation oscillations)
tau_R_IS = 1e-4  # s (relaxation time in crust)
def gamma_IS(f_mode, n):
    omega = 2 * pi * f_mode
    k_n = (n + 1) * pi / Delta_R
    # IS modifies: effective viscosity reduced by factor 1/(1 + omega^2 tau_R^2)
    suppression = 1.0 / (1.0 + (omega * tau_R_IS)**2)
    return eta_s_crust * k_n**2 * suppression / (rho_crust * enthalpy_factor)

# Compute damping for l=2 modes
gamma_bdnk_arr = np.array([gamma_BDNK(f, n) for n, f in enumerate(computed_freqs[2])])
gamma_is_arr = np.array([gamma_IS(f, n) for n, f in enumerate(computed_freqs[2])])
Q_bdnk = pi * computed_freqs[2] / (gamma_bdnk_arr + 1e-30)  # quality factor
Q_is = pi * computed_freqs[2] / (gamma_is_arr + 1e-30)

# ---- Observed QPO frequencies from SGR 1806-20 ----
# Israel et al. 2005, Watts & Strohmayer 2006
observed_freqs = [18, 26, 30, 92, 150, 625, 1840]
observed_labels = ['18', '26', '30', '92', '150', '625', '1840']

# ---- Plotting ----
fig, axes = plt.subplots(1, 2, figsize=(14, 7))

# Left panel: computed vs observed frequencies
ax = axes[0]

# Plot computed mode frequencies as horizontal lines for each l
colors_l = [COLORS['bdnk'], COLORS['relativistic'], COLORS['is'],
            COLORS['classical'], COLORS['data']]
y_positions = np.arange(len(l_values))

for j, l in enumerate(l_values):
    freqs = computed_freqs[l]
    # Only plot modes below 2500 Hz
    mask = freqs < 2500
    ax.scatter(freqs[mask], [j] * np.sum(mask), marker='|', s=200,
               color=colors_l[j], lw=2, zorder=3)
    ax.text(-0.02, j, f'$\\ell = {l}$', transform=ax.get_yaxis_transform(),
            fontsize=11, ha='right', va='center', color=colors_l[j], fontweight='bold')

# Overlay observed QPOs as vertical bands
for f_obs in observed_freqs:
    ax.axvline(f_obs, ls='-', color='red', alpha=0.3, lw=8)
    ax.axvline(f_obs, ls='-', color='red', alpha=0.8, lw=1)

# Add frequency labels at top
for i, (f_obs, lbl) in enumerate(zip(observed_freqs, observed_labels)):
    ax.text(f_obs, len(l_values) - 0.3, lbl + ' Hz', fontsize=8,
            ha='center', va='bottom', color='red', rotation=45)

ax.set_xlabel('Frequency [Hz]')
ax.set_yticks(y_positions)
ax.set_yticklabels([f'$\\ell={l}$' for l in l_values])
ax.set_title('SGR 1806$-$20 QPOs vs magnetar torsional modes')
ax.set_xlim(0, 2200)
ax.set_ylim(-0.5, len(l_values) - 0.3)

# Legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color='red', lw=8, alpha=0.3, label='Observed QPOs'),
    Line2D([0], [0], marker='|', color=COLORS['bdnk'], ls='', markersize=15,
           lw=2, label='Computed modes'),
]
ax.legend(handles=legend_elements, fontsize=10, loc='upper right')

# Right panel: Q-factor (BDNK vs IS)
ax = axes[1]
n_arr = np.arange(len(computed_freqs[2]))
freqs_2 = computed_freqs[2]
mask = freqs_2 < 2500

ax.semilogy(freqs_2[mask], Q_bdnk[mask], 'o-', lw=2, markersize=6,
            color=COLORS['bdnk'], label='BDNK')
ax.semilogy(freqs_2[mask], Q_is[mask], 's--', lw=2, markersize=6,
            color=COLORS['is'], label='Israel--Stewart')

# Mark observed QPOs on Q-factor plot
for f_obs in observed_freqs:
    ax.axvline(f_obs, ls=':', color='red', alpha=0.3, lw=1)

# Highlight where IS and BDNK diverge
ax.annotate('IS underestimates\ndamping at high $f$',
            xy=(1500, Q_is[np.argmin(np.abs(freqs_2 - 1500))]),
            xytext=(1200, 5e5), fontsize=9,
            arrowprops=dict(arrowstyle='->', color=COLORS['is']),
            color=COLORS['is'])

ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel('Quality factor $Q = \\pi f / \\gamma$')
ax.set_title('Mode damping: BDNK vs IS ($\\ell = 2$)')
ax.set_xlim(0, 2200)
ax.legend(fontsize=10, loc='upper left')

ax.text(0.95, 0.05, f'$B = 10^{{15}}$ G\n$T_{{\\rm crust}} = 10^8$ K\n'
        f'$\\mu_s = 3 \\times 10^{{29}}$ erg/cm$^3$',
        transform=ax.transAxes, fontsize=10, ha='right',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_magnetar_qpo.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_magnetar_qpo.png')
print("Saved fig_magnetar_qpo.pdf/png")
print(f"  v_s (shear) = {v_s:.3e} cm/s")
print(f"  v_A (Alfven) = {v_A:.3e} cm/s")
print(f"  f_0 (fundamental) = {f_0_crust:.1f} Hz")
print(f"  Computed l=2 modes: {computed_freqs[2][:6].astype(int)} Hz")
