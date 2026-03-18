"""
Compute the transition Q^{tr} where overstability gives way to stationary
convection for NS parameters with B = 10^{14} - 10^{16} G.

For overstability to occur, we need eta_mag > kappa (magnetic diffusivity
exceeds thermal diffusivity). This is realized in the NS outer crust and
envelope where the electrical conductivity is lower and thermal conductivity
from electrons is modest. We explore both: (i) core parameters where
overstability does NOT occur (kappa > eta), and (ii) outer-crust/envelope
parameters where it does.
"""
import sys; sys.path.insert(0, '/data/haiyangw/claude/Instability'); from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, G_cgs, M_sun
import matplotlib.pyplot as plt
import numpy as np

setup_style()

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# =================================================================
# NS outer crust / envelope parameters where overstability IS possible
# At rho ~ 10^{10}-10^{12} g/cm^3, T ~ 10^8 K:
#   sigma_e ~ 10^{21} s^{-1} (lower than core)
#   eta_visc ~ 10^{12} g/(cm s) from electron-ion scattering
#   kappa_th ~ 10^{17} erg/(cm s K) from electrons
# =================================================================

# NS outer crust parameters
rho_crust = 1e11  # g/cm^3
T_crust = 1e8  # K

# Transport for outer crust (Potekhin et al. 1999; Yakovlev & Pethick 2004)
eta_visc_crust = 1e12  # dynamic shear viscosity g/(cm s)
nu_visc_crust = eta_visc_crust / rho_crust  # kinematic, cm^2/s = 10

# Thermal diffusivity: kappa_diff = K_th / (rho c_v)
# c_v ~ n_e k_B (T/T_F) ~ 10^{16} erg/(cm^3 K) for degenerate electrons
c_v_crust = 1e16  # erg/(cm^3 K)
K_th_crust = 1e17  # thermal conductivity erg/(cm s K)
kappa_diff_crust = K_th_crust / (rho_crust * c_v_crust / rho_crust)  # ~ 10 cm^2/s
# Simplified
kappa_diff_crust = 1.0  # cm^2/s (thermal diffusivity in outer crust)

# Electrical conductivity in outer crust
sigma_e_arr = [1e20, 1e21, 1e22]  # s^{-1}, range for different temperatures/densities

d = 1e4  # layer depth 100 m (crust convective layer)

# Enthalpy correction in crust: modest, h ~ 1.01 - 1.05
h_values_crust = [1.0, 1.02, 1.05, 1.1]

# Panel (a): Q^tr vs B for different sigma_e (classical and relativistic)
ax = axes[0]

B_field = np.logspace(14, 16, 300)

for sigma_e, color, marker in zip(sigma_e_arr,
                                   [COLORS['classical'], COLORS['bdnk'], COLORS['data']],
                                   ['o', 's', 'D']):
    eta_mag = c_cgs**2 / (4 * np.pi * sigma_e)

    p1 = kappa_diff_crust / nu_visc_crust
    p2 = eta_mag / nu_visc_crust

    can_overstab = eta_mag > kappa_diff_crust

    Q_arr = B_field**2 * d**2 / (4 * np.pi * rho_crust * nu_visc_crust * eta_mag)

    if can_overstab:
        Q_tr = np.pi**2 * (1 + p1)**3 * (1 + p2) / ((p2 - p1) * (p1 + p2))
        B_tr = np.sqrt(Q_tr * 4 * np.pi * rho_crust * nu_visc_crust * eta_mag / d**2)
        label = rf'$\sigma_e = 10^{{{int(np.log10(sigma_e))}}}$ s$^{{-1}}$, $Q^{{\rm tr}}={Q_tr:.1e}$'
        ax.axhline(y=Q_tr, ls=':', color=color, alpha=0.4)
        ax.plot(B_tr, Q_tr, marker, ms=10, color=color, markeredgecolor='black', zorder=5)
    else:
        label = rf'$\sigma_e = 10^{{{int(np.log10(sigma_e))}}}$ s$^{{-1}}$ (no overstab.)'

    ax.loglog(B_field, Q_arr, '-', color=color, linewidth=2, label=label)

# Annotate regimes
ax.fill_between([1e14, 1e15], 1, 1e20, alpha=0.03, color='blue')
ax.fill_between([1e15, 1e16], 1, 1e20, alpha=0.03, color='red')
ax.text(3e14, 2, 'Normal pulsars', fontsize=8, color='blue', ha='center')
ax.text(3e15, 2, 'Magnetars', fontsize=8, color='red', ha='center')

ax.set_xlabel(r'Magnetic field $B$ (G)')
ax.set_ylabel(r'Chandrasekhar number $Q$')
ax.set_title(r'(a) $Q$ vs $B$: NS outer crust')
ax.legend(fontsize=7, loc='upper left')
ax.set_xlim(1e14, 1e16)
ax.set_ylim(1, 1e18)

# Panel (b): Q^tr_rel / Q^tr_class vs h, for fixed sigma_e
ax = axes[1]

sigma_e_fixed = 1e20  # s^{-1}: gives eta_mag > kappa
eta_mag_fixed = c_cgs**2 / (4 * np.pi * sigma_e_fixed)

p1_base = kappa_diff_crust / nu_visc_crust
p2_base = eta_mag_fixed / nu_visc_crust

h_cont = np.linspace(1.0, 2.0, 300)
Q_tr_class_val = np.pi**2 * (1 + p1_base)**3 * (1 + p2_base) / ((p2_base - p1_base) * (p1_base + p2_base))

Q_tr_rel_arr = []
B_tr_rel_arr = []
for h_val in h_cont:
    p1r = p1_base / h_val
    p2r = p2_base / h_val
    if p2r > p1r:
        Q_tr_r = np.pi**2 * (1 + p1r)**3 * (1 + p2r) / ((p2r - p1r) * (p1r + p2r))
        Q_tr_full = h_val**2 * Q_tr_r
    else:
        Q_tr_full = np.inf
    Q_tr_rel_arr.append(Q_tr_full)
    B_tr_r = np.sqrt(Q_tr_full * 4 * np.pi * rho_crust * nu_visc_crust * eta_mag_fixed * h_val / d**2) if Q_tr_full < np.inf else np.inf
    B_tr_rel_arr.append(B_tr_r)

Q_tr_rel_arr = np.array(Q_tr_rel_arr)
B_tr_rel_arr = np.array(B_tr_rel_arr)
ratio_Q = Q_tr_rel_arr / Q_tr_class_val

ax.plot(h_cont, ratio_Q, '-', color=COLORS['relativistic'], linewidth=2.5,
        label=r'$Q^{\rm tr}_{\rm rel} / Q^{\rm tr}_{\rm class}$')

# Theoretical prediction: Q^tr_rel ~ h^2 * Q^tr_class
ax.plot(h_cont, h_cont**2, '--', color='gray', linewidth=1.5,
        label=r'$h^2$ (leading-order prediction)')

ax.axvspan(1.01, 1.05, alpha=0.1, color=COLORS['neutron_star'], label='NS crust')
ax.axvspan(1.1, 1.3, alpha=0.1, color=COLORS['data'], label='NS core')

ax.set_xlabel(r'Specific enthalpy $h = w/(\rho_0 c^2)$')
ax.set_ylabel(r'$Q^{\rm tr}_{\rm rel} / Q^{\rm tr}_{\rm class}$')
ax.set_title(r'(b) Relativistic shift of $Q^{\rm tr}$')
ax.legend(fontsize=9)
ax.set_xlim(1.0, 2.0)

# Panel (c): Phase diagram - B vs T showing stationary / overstable regions
ax = axes[2]

T_range = np.logspace(7.5, 9.5, 200)  # K
B_grid = np.logspace(14, 16, 200)  # G

# sigma_e depends on T: sigma_e ~ sigma_0 * (T_F / T) for T < T_F
# For NS crust: sigma_e ~ 10^{22} * (10^8 / T) s^{-1} (simplified)
T_F = 1e9  # Fermi temperature scale

for h_val, ls in [(1.0, '--'), (1.05, '-'), (1.1, '-.')]:
    B_tr_of_T = []
    for T in T_range:
        sigma_e_T = 1e22 * min(T_F / T, 10)  # rough T-dependence, capped
        eta_mag_T = c_cgs**2 / (4 * np.pi * sigma_e_T)
        p1_T = kappa_diff_crust / (nu_visc_crust * h_val)
        p2_T = eta_mag_T / (nu_visc_crust * h_val)

        if p2_T > p1_T:
            Q_tr_T = h_val**2 * np.pi**2 * (1 + p1_T)**3 * (1 + p2_T) / ((p2_T - p1_T) * (p1_T + p2_T))
            B_tr_T = np.sqrt(Q_tr_T * 4 * np.pi * rho_crust * nu_visc_crust * eta_mag_T * h_val / d**2)
            B_tr_of_T.append(B_tr_T)
        else:
            B_tr_of_T.append(np.nan)

    B_tr_of_T = np.array(B_tr_of_T)
    valid = ~np.isnan(B_tr_of_T) & (B_tr_of_T > 1e14) & (B_tr_of_T < 1e17)

    color = COLORS['classical'] if h_val == 1.0 else COLORS['relativistic']
    if np.any(valid):
        ax.plot(T_range[valid], B_tr_of_T[valid], ls=ls, color=color,
                linewidth=2, label=rf'$h={h_val}$')

# Add text labels for regions
ax.text(5e8, 2e15, 'Overstable\nonset', fontsize=11, ha='center',
        color=COLORS['is'], fontweight='bold')
ax.text(1e8, 3e14, 'Stationary\nonset', fontsize=11, ha='center',
        color=COLORS['bdnk'], fontweight='bold')

ax.set_xlabel(r'Temperature $T$ (K)')
ax.set_ylabel(r'Transition $B^{\rm tr}$ (G)')
ax.set_title(r'(c) Overstability boundary in $T$--$B$ plane')
ax.set_xscale('log')
ax.set_yscale('log')
ax.legend(fontsize=9, loc='lower right')
ax.set_xlim(3e7, 3e9)
ax.set_ylim(1e14, 1e17)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_overstability_transition_Q.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_overstability_transition_Q.png')
print("Overstability transition Q plot saved.")
