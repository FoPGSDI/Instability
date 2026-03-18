#!/usr/bin/env python3
"""
Agent 11: Proto-neutron star neutrino convection - double-diffusive parameter space.

Plots the double-diffusive stability diagram for proto-NS convection:
  - Lepton fraction gradient (stabilising, fast neutrino diffusion)
  - Entropy gradient (destabilising, convection-driving)
  - Rotation (Taylor number)

Physical setup:
  - Proto-NS age ~ 0.1-10 s after core bounce
  - T ~ 10-50 MeV, rho ~ 10^{14} g/cm^3
  - Neutrino diffusion coefficient D_nu ~ 10^4-10^6 cm^2/s
  - Thermal diffusivity kappa ~ 10^2-10^4 cm^2/s
  - Kinematic viscosity nu ~ 1-10 cm^2/s
  => "Inverse" Pr_nu = D_nu/kappa >> 1 (neutrinos diffuse faster than heat)
  => Double-diffusive regime with Lewis number Le = D_nu/kappa ~ 10-100
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS
setup_style()

import numpy as np
import matplotlib.pyplot as plt

# === Panel (a): Double-diffusive parameter space ===
# Axes: R_rho = alpha*dT/dz / (beta*dY_L/dz) vs Le = D_nu/kappa
# Regimes: stable, lepto-convection, semi-convection, full convection

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- (a) Stability regions in (Le, R_rho) plane ---
Le = np.linspace(1, 200, 500)

# Ledoux stable: R_rho > 1 (composition gradient dominates)
# Schwarzschild unstable: R_rho < Le/(Le+1) approximately
# Semi-convective: Le/(Le+1) < R_rho < 1
# Overstable: depends on Pr

# Boundary 1: Full convection (Schwarzschild) R_rho < R_crit_1
R_crit_1 = np.ones_like(Le) * 0.0  # R_rho = 0 line

# Boundary 2: Semi-convection boundary
# R_rho = Pr / (Pr + 1) * (Le + 1) / Le approximately
Pr_nu = 0.01  # nu/kappa for nuclear matter
R_semi = (Pr_nu + 1) / (Pr_nu + Le)

# Boundary 3: Oscillatory double-diffusive (overstability)
# R_rho = (Le + Pr) / (1 + Pr) for overstable onset
R_overstab = (Le + Pr_nu) / (1.0 + Pr_nu)

# Boundary 4: Ledoux stability (R_rho > 1)
R_ledoux = np.ones_like(Le)

# Fill regions
ax1.fill_between(Le, 0, R_semi, alpha=0.2, color=COLORS['relativistic'],
                  label='Direct convection')
ax1.fill_between(Le, R_semi, R_overstab, alpha=0.15, color=COLORS['is'],
                  label='Oscillatory double-diffusive')
ax1.fill_between(Le, R_overstab, R_ledoux, alpha=0.1, color=COLORS['bdnk'],
                  label='Semi-convective')
ax1.fill_between(Le, R_ledoux, R_ledoux * 2, alpha=0.08, color=COLORS['classical'],
                  label='Ledoux stable')

ax1.plot(Le, R_semi, color=COLORS['relativistic'], linewidth=1.5, ls='--')
ax1.plot(Le, R_overstab, color=COLORS['is'], linewidth=1.5, ls='-.')
ax1.plot(Le, R_ledoux, color='gray', linewidth=1.5, ls='-')

# Mark proto-NS regime: Le ~ 10-100
ax1.axvspan(10, 100, alpha=0.05, color=COLORS['neutron_star'])
ax1.annotate('Proto-NS\nneutrino\nregime', xy=(35, 0.3), fontsize=10,
             color=COLORS['neutron_star'], ha='center', style='italic')

# Relativistic correction arrows
# At Le = 50, BDNK shifts the overstable boundary upward
Le_mark = 50
R_ov_cl = (Le_mark + Pr_nu) / (1.0 + Pr_nu)
R_ov_rel = R_ov_cl * 1.15  # 15% shift for w/(rho c^2) = 1.3
ax1.annotate('', xy=(Le_mark, R_ov_rel), xytext=(Le_mark, R_ov_cl),
             arrowprops=dict(arrowstyle='->', color=COLORS['relativistic'],
                             lw=2))
ax1.annotate(r'Rel. shift', xy=(Le_mark + 5, 0.5 * (R_ov_cl + R_ov_rel)),
             fontsize=9, color=COLORS['relativistic'])

ax1.set_xlabel(r'Lewis number $\mathrm{Le} = D_\nu / \kappa$')
ax1.set_ylabel(r'Density ratio $R_\rho = \alpha \Delta T / \beta \Delta Y_L$')
ax1.set_title('(a) Double-diffusive parameter space')
ax1.legend(fontsize=9, loc='upper left')
ax1.set_xlim(1, 200)
ax1.set_ylim(0, 1.5)

# === Panel (b): Critical Ra vs Ta for proto-NS with double diffusion ===
Ta = np.logspace(0, 16, 500)

# Single-component (no composition): Ra_c grows with Ta
Ra_stat = 657.5 + 8.696 * Ta**(2.0/3.0)

# Double-diffusive: composition stabilises, need higher Ra
# Ra_DD = Ra_stat + R_rho * Le * Ra_composition_threshold
R_rho_vals = [0.0, 0.3, 0.6, 0.9]
Le_val = 50  # typical for proto-NS

dd_colors = [COLORS['classical'], COLORS['bdnk'],
             COLORS['is'], COLORS['relativistic']]
dd_ls = ['-', '--', '-.', ':']
dd_labels = [r'$R_\rho=0$ (no $Y_L$ gradient)',
             r'$R_\rho=0.3$', r'$R_\rho=0.6$',
             r'$R_\rho=0.9$ (strong $Y_L$ stabilisation)']

for i, (Rrho, lab) in enumerate(zip(R_rho_vals, dd_labels)):
    # Double-diffusive enhancement to critical Ra
    # Ra_DD ~ Ra_stat * (1 + R_rho * Le / (Le - 1))
    enhancement = 1.0 + Rrho * Le_val / (Le_val - 1.0)
    Ra_dd = Ra_stat * enhancement

    ax2.loglog(Ta, Ra_dd, dd_ls[i], color=dd_colors[i],
               linewidth=2.0, label=lab)

# Mark proto-NS regime
# Omega ~ 100-1000 rad/s for newborn NS, d ~ 10^5 cm, nu ~ 1 cm^2/s
# Ta ~ 4*Omega^2*d^4/nu^2 ~ 4e20 to 4e22
ax2.axvspan(1e8, 1e14, alpha=0.08, color=COLORS['neutron_star'])
ax2.annotate('Proto-NS\nregime', xy=(3e10, 3e4), fontsize=10,
             color=COLORS['neutron_star'], ha='center', style='italic')

ax2.set_xlabel(r'Taylor number $\mathrm{Ta}$')
ax2.set_ylabel(r'Critical Rayleigh number $\mathrm{Ra}_c$')
ax2.set_title(r'(b) Double-diffusive onset with rotation ($\mathrm{Le}=50$)')
ax2.legend(fontsize=9, loc='upper left')
ax2.set_xlim(1, 1e16)
ax2.set_ylim(1e2, 1e13)

fig.tight_layout()
outdir = os.path.dirname(__file__)
fig.savefig(os.path.join(outdir, 'fig_proto_ns_double_diffusive.pdf'))
fig.savefig(os.path.join(outdir, 'fig_proto_ns_double_diffusive.png'))
print("Saved plots/ch3/fig_proto_ns_double_diffusive.pdf and .png")
plt.close(fig)
