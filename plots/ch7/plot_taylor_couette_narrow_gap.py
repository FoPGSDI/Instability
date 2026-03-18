"""
Plot: Critical Taylor number for narrow-gap relativistic Taylor-Couette flow
as a function of mu, showing the relativistic enhancement factor.
Agent 28, sec71.
"""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')); from SHARED_PLOT_STYLE import setup_style, COLORS, LINE_STYLES
setup_style()

import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# Left panel: T_c^rel vs mu for different xi values
mu = np.linspace(-1.0, 0.95, 300)

def Tc_classical(mu_arr):
    """Classical narrow-gap critical Taylor number (approximate formula)."""
    return 3430.0 / (1.0 + mu_arr)

xi_values = [0, 0.01, 0.1, 0.33, 1.0]
labels = [
    r'$\xi=0$ (classical)',
    r'$\xi=0.01$ (NS crust)',
    r'$\xi=0.1$ (NS core)',
    r'$\xi=1/3$ (QGP)',
    r'$\xi=1$ (ultra-rel)',
]
colors_list = [COLORS['classical'], COLORS['neutron_star'], COLORS['data'],
               COLORS['qgp'], COLORS['relativistic']]
linestyles = ['-', '--', '-.', ':', (0, (3, 1, 1, 1))]

for xi_val, label, col, ls in zip(xi_values, labels, colors_list, linestyles):
    Tc_rel = Tc_classical(mu) * (1 + xi_val)**2
    valid = Tc_rel > 0
    ax1.semilogy(mu[valid], Tc_rel[valid], color=col, linewidth=2, linestyle=ls, label=label)

ax1.set_xlabel(r'$\mu = \Omega_2/\Omega_1$', fontsize=13)
ax1.set_ylabel(r'$T_c^{\rm rel}$', fontsize=13)
ax1.set_title('Critical Taylor number: narrow-gap limit', fontsize=12)
ax1.legend(fontsize=9, loc='upper left')
ax1.set_xlim(-1, 1)
ax1.set_ylim(1e3, 1e6)
ax1.axvline(0, color='gray', linewidth=0.5, linestyle=':')

# Right panel: T_c^rel / T_c^cl as a function of xi for fixed mu
xi_plot = np.linspace(0, 2, 200)
ratio = (1 + xi_plot)**2

ax2.plot(xi_plot, ratio, color=COLORS['relativistic'], linewidth=2.5)
ax2.fill_between(xi_plot, 1, ratio, alpha=0.1, color=COLORS['relativistic'])

# Mark specific regimes
regime_points = [
    (0.01, 'NS crust', COLORS['neutron_star']),
    (0.1, 'NS core', COLORS['data']),
    (1/3, 'QGP', COLORS['qgp']),
    (1.0, 'Ultra-rel', COLORS['jet']),
]
for xi_val, label, col in regime_points:
    r_val = (1 + xi_val)**2
    ax2.plot(xi_val, r_val, 'o', color=col, markersize=10, zorder=5,
             markeredgecolor='black', markeredgewidth=0.8)
    ax2.annotate(f'{label}\n' + r'$T_c^{\rm rel}/T_c^{\rm cl}$' + f' = {r_val:.2f}',
                 xy=(xi_val, r_val),
                 xytext=(xi_val + 0.15, r_val + 0.3),
                 fontsize=9, color=col,
                 arrowprops=dict(arrowstyle='->', color=col, alpha=0.6))

ax2.set_xlabel(r'$\xi = (\varepsilon + p)/(\rho_0 c^2) - 1$', fontsize=13)
ax2.set_ylabel(r'$T_c^{\rm rel} / T_c^{\rm cl}$', fontsize=13)
ax2.set_title(r'Relativistic enhancement: $T_c^{\rm rel}/T_c^{\rm cl} = (1+\xi)^2$', fontsize=12)
ax2.set_xlim(0, 2)
ax2.set_ylim(0.8, 10)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/ch7/fig_taylor_couette_narrow_gap.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/ch7/fig_taylor_couette_narrow_gap.png')
plt.close()
print("Saved fig_taylor_couette_narrow_gap.pdf/png")
