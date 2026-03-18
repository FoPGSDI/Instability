"""
Capillary breakup timescale vs jet Lorentz factor for GRB jets.

Physics:
- GRB jet: Gamma ~ 100-1000, R_jet ~ 10^7 cm, t_eng ~ 10 s
- Cocoon-confined: effective surface tension T ~ p_cocoon * R_jet
- Rayleigh-Plateau most unstable mode at x ~ 0.697
- Comoving breakup time: tau_co ~ 1/sigma_max ~ sqrt(w*c^2*R^3 / T)
- Observer frame: tau_obs ~ tau_co / (2*Gamma^2) (relativistic beaming)
- Compare with observed GRB variability: 10 ms - 100 ms

From eq. (rel-111-astro-sigma):
  sigma_max ~ 0.34 * sqrt(T / (w*c^2*R^3))
  tau_co = 1/sigma_max

Enthalpy ratio w/rho: ranges from ~1 (cold) to ~10 (radiation-dominated fireball)
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, G_cgs, pi
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# --- GRB jet parameters ---
R_jet = 1e7  # cm (jet radius)
t_eng = 10.0  # s (engine activity time)

# Cocoon pressure ~ 10^{18} erg/cm^3 (typical for collapsar jet breakout)
p_cocoon = 1e18  # erg/cm^3

# Effective surface tension
T_surf = p_cocoon * R_jet  # erg/cm^2

# Rest-mass density (jet comoving frame)
rho_jet = 1e-10  # g/cm^3

# Lorentz factor array
Gamma_arr = np.logspace(1, 3, 200)  # Gamma = 10 to 1000

# Enthalpy ratios w/rho to explore
w_over_rho_vals = [1.0, 3.0, 10.0, 30.0]
labels_w = [r'$w/\rho c^2 = 1$ (cold)', r'$w/\rho c^2 = 3$',
            r'$w/\rho c^2 = 10$ (fiducial)', r'$w/\rho c^2 = 30$ (hot)']
colors_w = [COLORS['classical'], COLORS['bdnk'], COLORS['relativistic'], COLORS['jet']]

# --- Compute breakup timescales ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# Left panel: tau_obs vs Gamma for several w/rho
for i, w_rho in enumerate(w_over_rho_vals):
    # Enthalpy density: w = w_rho * rho * c^2
    w = w_rho * rho_jet  # g/cm^3 (enthalpy density = (eps+p)/c^2)

    # Comoving growth rate (most unstable mode, x~0.697)
    sigma_max = 0.34 * np.sqrt(T_surf / (w * c_cgs**2 * R_jet**3))

    # Comoving breakup time
    tau_co = 1.0 / sigma_max  # seconds

    # Observer-frame timescale: tau_obs ~ tau_co / (2*Gamma^2)
    # (time compression from relativistic motion toward observer)
    tau_obs = tau_co / (2 * Gamma_arr**2)

    ax1.loglog(Gamma_arr, tau_obs * 1e3, '-', lw=2.0, color=colors_w[i],
               label=labels_w[i])

# Observed GRB variability band: 10 ms to 100 ms
ax1.axhspan(10, 100, alpha=0.15, color='gray')
ax1.annotate('Observed GRB variability\n(10--100 ms)', xy=(15, 40),
             fontsize=10, color='gray', style='italic')

# Mark specific GRBs
grb_data = {
    'GRB 090510\n(short)': (900, 0.5),
    'GRB 130427A': (300, 30),
    'GRB 080916C': (500, 50),
    'GRB 990123': (200, 20),
}
for name, (gamma, dt_ms) in grb_data.items():
    ax1.plot(gamma, dt_ms, 'o', ms=8, color=COLORS['data'], zorder=5)
    ax1.annotate(name, xy=(gamma, dt_ms), xytext=(5, 5),
                 textcoords='offset points', fontsize=7, color=COLORS['data'])

ax1.set_xlabel(r'Bulk Lorentz factor $\Gamma_{\rm jet}$')
ax1.set_ylabel(r'Observer-frame breakup time $\tau_{\rm obs}$ [ms]')
ax1.set_title(r'Capillary breakup timescale: $R_{\rm jet}=10^7$ cm')
ax1.set_xlim(10, 1000)
ax1.set_ylim(0.01, 1000)
ax1.legend(loc='upper right', fontsize=9)

# Right panel: sigma_max / sigma_max^{Newt} vs w/rho (relativistic suppression)
w_rho_arr = np.linspace(1, 50, 200)

# Newtonian: sigma_N = 0.34 * sqrt(T / (rho * c^2 * R^3))
# Relativistic: sigma_rel = 0.34 * sqrt(T / (w * c^2 * R^3)) = sigma_N / sqrt(w/rho)
suppression = 1.0 / np.sqrt(w_rho_arr)

ax2.plot(w_rho_arr, suppression, '-', lw=2.5, color=COLORS['relativistic'],
         label=r'$\sigma_{\max}^{\rm rel} / \sigma_{\max}^{\rm N} = (w/\rho c^2)^{-1/2}$')

# Mark astrophysical regimes
regimes = {
    'Cold jet\n(baryon-dominated)': (1.5, 1 / np.sqrt(1.5)),
    'GRB fireball\n(radiation-dominated)': (10, 1 / np.sqrt(10)),
    'Poynting-flux\ndominated': (30, 1 / np.sqrt(30)),
}
for name, (wr, sup) in regimes.items():
    ax2.plot(wr, sup, 's', ms=10, color=COLORS['data'], zorder=5)
    ax2.annotate(name, xy=(wr, sup), xytext=(5, 8),
                 textcoords='offset points', fontsize=9, color=COLORS['data'])

# Enhancement of breakup timescale
ax2_twin = ax2.twinx()
ax2_twin.plot(w_rho_arr, np.sqrt(w_rho_arr), '--', lw=1.8, color=COLORS['bdnk'],
              label=r'$\tau_{\rm breakup}^{\rm rel} / \tau_{\rm breakup}^{\rm N}$')
ax2_twin.set_ylabel(r'Timescale ratio $\tau^{\rm rel}/\tau^{\rm N}$',
                     color=COLORS['bdnk'])

ax2.set_xlabel(r'Enthalpy ratio $w / \rho c^2 = (\varepsilon + p) / \rho c^2$')
ax2.set_ylabel(r'Growth rate ratio $\sigma^{\rm rel} / \sigma^{\rm N}$',
               color=COLORS['relativistic'])
ax2.set_title('Relativistic suppression of capillary instability')
ax2.set_xlim(1, 50)
ax2.set_ylim(0, 1.1)

lines1, labels1 = ax2.get_legend_handles_labels()
lines2, labels2 = ax2_twin.get_legend_handles_labels()
ax2.legend(lines1 + lines2, labels1 + labels2, loc='center right', fontsize=9)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_grb_variability.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_grb_variability.png')
print("Saved fig_grb_variability.pdf/png")
