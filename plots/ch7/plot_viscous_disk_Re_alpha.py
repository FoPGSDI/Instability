"""
Plot: Viscous accretion disk parameters: effective Reynolds number and
Shakura-Sunyaev alpha parameter, with BDNK relativistic corrections.
Agent 27, sec69-70.
"""
import sys; sys.path.insert(0, '../..'); from SHARED_PLOT_STYLE import setup_style, COLORS, LINE_STYLES
setup_style()

import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# Left panel: Effective Reynolds number Re_rel / Re_classical vs enthalpy ratio
xi = np.linspace(0, 1.5, 200)  # xi = (eps+p)/(rho c^2) - 1
# Re_rel = V d / nu_rel = V d (eps+p) / (eta_s c^2)
# Re_class = V d rho / eta_s
# Re_rel / Re_class = (eps+p)/(rho c^2) = 1 + xi
Re_ratio = 1 + xi

ax1.plot(xi, Re_ratio, color=COLORS['relativistic'], linewidth=2.5)
ax1.fill_between(xi, 1, Re_ratio, alpha=0.15, color=COLORS['relativistic'])

# Mark astrophysical regimes
regimes = [
    (1e-2, 'NS outer core', COLORS['neutron_star']),
    (0.1, 'NS inner core', COLORS['neutron_star']),
    (0.33, r'QGP ($p \sim \varepsilon/3$)', COLORS['qgp']),
    (1.0, r'Ultra-rel ($p \sim \varepsilon$)', COLORS['jet']),
]
for xi_val, label, col in regimes:
    re_val = 1 + xi_val
    ax1.plot(xi_val, re_val, 'o', color=col, markersize=9, zorder=5,
             markeredgecolor='black', markeredgewidth=0.8)
    ax1.annotate(label, xy=(xi_val, re_val), xytext=(xi_val+0.08, re_val+0.08),
                 fontsize=9, color=col)

ax1.set_xlabel(r'$\xi = (\varepsilon + p)/(\rho_0 c^2) - 1$', fontsize=13)
ax1.set_ylabel(r'$\mathrm{Re}_{\mathrm{rel}} / \mathrm{Re}_{\mathrm{class}}$', fontsize=13)
ax1.set_title(r'Relativistic Reynolds number enhancement', fontsize=12)
ax1.set_xlim(0, 1.5)
ax1.set_ylim(0.9, 2.6)

# Right panel: Critical Taylor number ratio vs xi for different alpha-disk models
# T_rel / T_cl = (1+xi)^2
xi2 = np.linspace(0, 1.0, 200)
T_ratio = (1 + xi2)**2

ax2.plot(xi2, T_ratio, color=COLORS['classical'], linewidth=2.5, label=r'$T_{c}^{\rm rel}/T_{c}^{\rm cl} = (1+\xi)^2$')

# Alpha-disk: alpha = nu/(c_s H), BDNK correction: nu_rel = eta_s c^2/(eps+p)
# vs classical nu = eta_s/rho.  So alpha_rel = alpha_cl * rho c^2 / (eps+p) = alpha_cl/(1+xi)
alpha_class = np.array([0.01, 0.03, 0.1, 0.3])
for alpha_val in alpha_class:
    alpha_rel = alpha_val / (1 + xi2)
    ax2.plot(xi2, alpha_rel / alpha_val, color=COLORS['accretion'], linewidth=1.5,
             linestyle='--', alpha=0.5)

# Add a cleaner line for the ratio
ax2.plot(xi2, 1.0/(1+xi2), color=COLORS['accretion'], linewidth=2.5, linestyle='--',
         label=r'$\alpha_{\rm rel}/\alpha_{\rm cl} = (1+\xi)^{-1}$')

ax2.axhline(1, color='gray', linewidth=0.8, linestyle=':')
ax2.set_xlabel(r'$\xi = (\varepsilon + p)/(\rho_0 c^2) - 1$', fontsize=13)
ax2.set_ylabel('Ratio to classical value', fontsize=13)
ax2.set_title(r'Relativistic corrections to $T_c$ and $\alpha$-viscosity', fontsize=12)
ax2.legend(fontsize=11, loc='center right')
ax2.set_xlim(0, 1.0)
ax2.set_ylim(0, 4.5)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/ch7/fig_viscous_disk_Re_alpha.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/ch7/fig_viscous_disk_Re_alpha.png')
plt.close()
print("Saved fig_viscous_disk_Re_alpha.pdf/png")
