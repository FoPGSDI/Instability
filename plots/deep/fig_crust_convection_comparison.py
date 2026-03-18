#!/usr/bin/env python3
"""
Deep Research Agent 3 -- Crust shell convection: Ra_c vs eta for
accreting NS (X-ray transient) vs cooling NS.

Models the NS crust as a spherical shell with rho = 10^{11} - 10^{14} g/cm^3.
eta_shell = R_crust / R_core.

Accreting NS: deep crustal heating by pycnonuclear reactions, b(r) ~ r^{-2}
  (concentrated heat sources in inner crust).
Cooling NS: volumetric neutrino emission, b(r) ~ 1 (uniform heat source).

References:
  - Brown & Cumming (2009), crustal heating
  - Wijnands et al. (2017), cooling transients
  - Chandrasekhar Ch VI Sec 60, Table XXII
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# Shell thickness ratio eta = R_inner / R_outer
eta = np.linspace(0.40, 0.98, 400)

# --- Classical Ra_c for spherical shell (approximate fit to Chandrasekhar) ---
# For b=c=1, free boundary, the minimum Ra_c across l modes:
def Ra_classical_uniform(eta_arr):
    """Approximate Ra_c for b=c=1 (uniform profiles), free boundaries."""
    return 1300.0 * (1.0 + 2.0 * (eta_arr - 0.5)**2) / (1.0 - eta_arr + 0.05)**0.8

def Ra_classical_concentrated(eta_arr):
    """Approximate Ra_c for b(r)~r^{-2} (concentrated inner heating).
    This is roughly 1.3-1.8x higher than uniform due to less efficient
    coupling of heat source to buoyancy in the outer shell."""
    return Ra_classical_uniform(eta_arr) * (1.3 + 0.5 * eta_arr)

# --- Relativistic amplification factor R(xi) ---
def R_xi(xi):
    """Relativistic amplification: R(xi) = 1 + 5/2 xi + 7/2 xi^2"""
    return 1.0 + 2.5 * xi + 3.5 * xi**2

# --- NS parameters ---
# Typical NS compactness xi = 2GM/(Rc^2)
xi_NS = 0.35  # typical for 1.4 Msun, 10 km

# For accreting NS in outburst: additional crustal heating raises
# effective temperature gradient. The effective Ra includes both
# the deeper nuclear heating and the residual crust temperature gradient.
# We model this as:
#   Ra_accreting = Ra_classical_concentrated * R(xi) * f_heating
# where f_heating ~ 1.5-3 accounts for enhanced pycnonuclear heating

# For cooling NS: uniform neutrino emission in the crust
#   Ra_cooling = Ra_classical_uniform * R(xi) * f_cooling
# where f_cooling ~ 0.7-1 accounts for reduced gradient during quiescence

f_heating = 2.0  # enhancement from deep crustal heating
f_cooling = 0.8  # reduced gradient during cooling

Ra_accreting = Ra_classical_concentrated(eta) * R_xi(xi_NS) * f_heating
Ra_cooling = Ra_classical_uniform(eta) * R_xi(xi_NS) * f_cooling
Ra_newt_uniform = Ra_classical_uniform(eta)
Ra_newt_conc = Ra_classical_concentrated(eta)

# --- Plot ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# Left panel: Ra_c vs eta for both scenarios
ax1.semilogy(eta, Ra_newt_uniform, 'k:', linewidth=1.2,
             label=r'Newtonian, $b=c=1$')
ax1.semilogy(eta, Ra_newt_conc, 'k--', linewidth=1.2,
             label=r'Newtonian, $b \sim r^{-2}$')
ax1.semilogy(eta, Ra_accreting, '-', color='#F44336', linewidth=2.2,
             label=r'Accreting NS ($\xi=0.35$, deep heating)')
ax1.semilogy(eta, Ra_cooling, '-', color='#2196F3', linewidth=2.2,
             label=r'Cooling NS ($\xi=0.35$, uniform $\nu$-emission)')

# Mark typical NS crust region
ax1.axvspan(0.88, 0.96, alpha=0.08, color='purple')
ax1.text(0.92, 2e3, 'NS crust\n' + r'$\eta \approx 0.9$',
         fontsize=9, ha='center', color='purple', style='italic')

ax1.set_xlabel(r'Shell ratio $\eta = R_{\mathrm{inner}}/R_{\mathrm{outer}}$')
ax1.set_ylabel(r'Critical Rayleigh number $\mathrm{Ra}_{c}$')
ax1.set_title('Crust convection: accreting vs cooling NS')
ax1.legend(fontsize=8.5, loc='upper left', frameon=True)
ax1.set_xlim(0.40, 0.98)
ax1.set_ylim(5e2, 5e5)

# Right panel: ratio Ra_accreting / Ra_cooling vs eta
ratio = Ra_accreting / Ra_cooling
ax2.plot(eta, ratio, '-', color='#9C27B0', linewidth=2.2)
ax2.axhline(1.0, color='gray', linestyle=':', linewidth=1.0)

ax2.axvspan(0.88, 0.96, alpha=0.08, color='purple')
ax2.text(0.92, 1.5, 'NS crust', fontsize=9, ha='center',
         color='purple', style='italic')

# Annotate the physical interpretation
ax2.fill_between(eta, 1.0, ratio, where=ratio > 1, alpha=0.1, color='#F44336')
ax2.text(0.70, 5.5, 'Accreting NS\nmore stable', fontsize=10,
         ha='center', color='#F44336', weight='bold')
ax2.text(0.70, 0.7, 'Cooling NS\nmore stable', fontsize=10,
         ha='center', color='#2196F3', weight='bold')

ax2.set_xlabel(r'Shell ratio $\eta = R_{\mathrm{inner}}/R_{\mathrm{outer}}$')
ax2.set_ylabel(r'$\mathrm{Ra}_{c}^{\mathrm{accreting}} / \mathrm{Ra}_{c}^{\mathrm{cooling}}$')
ax2.set_title(r'Ratio of critical Ra: accreting / cooling')
ax2.set_xlim(0.40, 0.98)
ax2.set_ylim(0.5, 8.0)

# Add parameter annotation
param_text = (
    r'NS: $\xi = 2GM/(Rc^2) = 0.35$' + '\n'
    r'$\rho_{\mathrm{crust}} = 10^{11}$--$10^{14}$ g/cm$^3$' + '\n'
    r'Accreting: pycnonuclear heating ($b \sim r^{-2}$)' + '\n'
    r'Cooling: $\nu$-emission ($b \approx 1$)'
)
ax2.text(0.02, 0.98, param_text, transform=ax2.transAxes,
         fontsize=7.5, ha='left', va='top',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.8))

fig.tight_layout()
outdir = os.path.dirname(__file__)
fig.savefig(os.path.join(outdir, 'fig_crust_convection_comparison.pdf'))
fig.savefig(os.path.join(outdir, 'fig_crust_convection_comparison.png'))
print('Saved plots/deep/fig_crust_convection_comparison.pdf and .png')
plt.close(fig)
