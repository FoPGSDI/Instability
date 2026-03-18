"""
Plot: Wide-gap accretion disk critical conditions for thick disks.
Shows T_c^rel vs kappa for eta=0.5 (wide gap), and the relativistic correction
delta_rel as a function of gap ratio eta.
Agent 29, sec72-73.
"""
import sys; sys.path.insert(0, '../..'); from SHARED_PLOT_STYLE import setup_style, COLORS, LINE_STYLES
setup_style()

import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# Left panel: T_c vs kappa for eta=0.5, classical vs relativistic
# Using data from Table XXXIV (Chandrasekhar) and relativistic correction
kappa_vals = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.333, 1.4, 1.6, 1.8])
# Classical T_c values for eta=0.5 (approximate interpolation from text)
Tc_class = np.array([15340, 15400, 15590, 15640, 14700, 13110, 12500, 13050, 12000, 9883, 30860])

# Smooth interpolation for plotting
from scipy.interpolate import interp1d
kappa_fine = np.linspace(0, 1.8, 200)
# Use the data points we have
kappa_data = np.array([0, 0.4, 0.6, 1.0, 1.333, 1.6, 1.8])
Tc_data = np.array([15340, 15590, 15640, 13110, 13050, 9883, 30860])

try:
    f_interp = interp1d(kappa_data, Tc_data, kind='cubic', fill_value='extrapolate')
    Tc_smooth = f_interp(kappa_fine)
except:
    Tc_smooth = np.interp(kappa_fine, kappa_data, Tc_data)

# Plot for different p/(rho c^2) values
p_rho_vals = [0, 0.01, 0.05, 0.1]
labels_p = [
    r'Classical ($p/\rho c^2 = 0$)',
    r'$p/\rho c^2 = 0.01$',
    r'$p/\rho c^2 = 0.05$',
    r'$p/\rho c^2 = 0.10$',
]
colors_p = [COLORS['classical'], COLORS['accretion'], COLORS['data'], COLORS['relativistic']]
ls_p = ['-', '--', '-.', ':']

for p_val, label, col, ls in zip(p_rho_vals, labels_p, colors_p, ls_p):
    # T_c^rel = T_c^cl * (1 - delta_rel) where delta_rel ~ p/(rho c^2)
    Tc_rel = Tc_smooth * (1 - p_val)
    ax1.plot(kappa_fine, Tc_rel / 1e3, color=col, linewidth=2, linestyle=ls, label=label)

# Mark special kappa values
ax1.axvline(0.25, color='gray', linewidth=0.5, linestyle=':', alpha=0.5)
ax1.text(0.25, 32, r'$\mu=\eta^2$', fontsize=9, color='gray', ha='center')

ax1.set_xlabel(r'$\kappa = -A R_2^4 / B$', fontsize=13)
ax1.set_ylabel(r'$T_c \times 10^{-3}$', fontsize=13)
ax1.set_title(r'Critical Taylor number for $\eta = 0.5$ (wide gap)', fontsize=12)
ax1.legend(fontsize=9, loc='upper left')
ax1.set_xlim(0, 1.8)
ax1.set_ylim(5, 35)

# Right panel: delta_rel vs eta for different p/(rho c^2)
eta_vals = np.linspace(0.1, 0.99, 200)

for p_val, label, col, ls in zip([0.01, 0.05, 0.1], labels_p[1:], colors_p[1:], ls_p[1:]):
    # delta_rel = p/(rho c^2) + viscous correction that grows as eta -> 0
    # From eq (rel-7-305): for eta->0, delta ~ p/(rho c^2) + 4 eta_s^2/(rho^2 c^2 R1^2)
    # Simplified model: delta_rel = p_val * (1 + 0.05 * (1-eta_vals)/eta_vals)
    delta_rel = p_val * (1 + 0.12 * (1 - eta_vals**2) / (1 + eta_vals)**2)
    ax2.plot(eta_vals, delta_rel * 100, color=col, linewidth=2, linestyle=ls, label=label)

ax2.set_xlabel(r'$\eta = R_1/R_2$', fontsize=13)
ax2.set_ylabel(r'$\delta_{\rm rel}$ (\%)', fontsize=13)
ax2.set_title(r'Relativistic correction $\delta_{\rm rel}$ vs gap ratio', fontsize=12)
ax2.legend(fontsize=10, loc='upper right')
ax2.set_xlim(0.1, 1.0)

# Mark thick disk and thin disk regimes
ax2.axvspan(0.1, 0.5, alpha=0.05, color='blue')
ax2.axvspan(0.5, 1.0, alpha=0.05, color='green')
ax2.text(0.3, ax2.get_ylim()[1]*0.9, 'Thick disk\n(wide gap)', fontsize=10,
         ha='center', color='blue', alpha=0.7)
ax2.text(0.75, ax2.get_ylim()[1]*0.9, 'Thin disk\n(narrow gap)', fontsize=10,
         ha='center', color='green', alpha=0.7)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/ch7/fig_wide_gap_critical_conditions.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/ch7/fig_wide_gap_critical_conditions.png')
plt.close()
print("Saved fig_wide_gap_critical_conditions.pdf/png")
