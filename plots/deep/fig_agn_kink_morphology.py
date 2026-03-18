"""
Kink growth length vs B_toroidal/B_axial for AGN jets: FR I vs FR II.

Physics (Lyubarsky 2009, Bromberg & Tchekhovskoy 2016):
- Current-driven kink instability (m=-1 mode) in force-free jets
- Growth length L_kink ~ (B_z/B_phi) * R_jet * Gamma (for relativistic jets)
- In force-free limit: L_kink ~ R_jet * (B_z/B_phi)^2 * (1 + Gamma^2*V^2/(2c^2))
- FR I jets: Gamma ~ 2-5, disrupted at L ~ few kpc
- FR II jets: Gamma ~ 10-50, coherent to L ~ 100 kpc - 1 Mpc
- Blandford, Meier, Readhead (2019): comprehensive review of AGN jet physics

Plot:
  Left: L_kink / R_jet vs B_phi/B_z for several Gamma values
  Right: Jet morphology diagram in (B_phi/B_z, Gamma) plane with FR I/II regions
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, pi
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# --- Kink instability growth length ---
# From Lyubarsky (2009) and Bromberg & Tchekhovskoy (2016):
# The kink instability of a force-free jet with pitch profile
# B_phi/B_z = (r/R_jet) * (B_phi0/B_z0) has growth rate
#   gamma_kink ~ v_A / (R_jet * B_z/B_phi)
# where v_A is the Alfven speed.
# For a relativistic jet with bulk Gamma:
#   The growth length (distance along jet for e-folding) is:
#   L_kink ~ Gamma * v_jet / gamma_kink ~ Gamma * R_jet * (B_z/B_phi)
#
# More precisely (Bromberg & Tchekhovskoy 2016, eq. 15):
#   L_kink / R_jet ~ (B_z/B_phi) * sqrt(1 + (B_z/B_phi)^2) * Gamma

# B_phi/B_z ratio array
Bphi_over_Bz = np.logspace(-1, 1.5, 300)  # 0.1 to ~30
Bz_over_Bphi = 1.0 / Bphi_over_Bz

# Lorentz factor values
Gamma_vals = [2, 5, 10, 20, 50]
colors_G = [COLORS['classical'], COLORS['bdnk'], COLORS['is'],
            COLORS['relativistic'], COLORS['jet']]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# Left panel: L_kink / R_jet vs B_phi/B_z
for i, Gamma in enumerate(Gamma_vals):
    # L_kink / R_jet = Gamma * (B_z/B_phi) * sqrt(1 + (B_z/B_phi)^2)
    L_kink_over_R = Gamma * Bz_over_Bphi * np.sqrt(1 + Bz_over_Bphi**2)

    ax1.loglog(Bphi_over_Bz, L_kink_over_R, '-', lw=2.0, color=colors_G[i],
               label=rf'$\Gamma = {Gamma}$')

# Reference lines for jet scales
# R_jet ~ 100 pc for kpc-scale jets
# FR I disruption: L ~ 1-10 kpc => L/R ~ 10-100
# FR II jets: L ~ 100 kpc => L/R ~ 1000
ax1.axhspan(10, 100, alpha=0.10, color='blue')
ax1.annotate('FR I disruption\n($L \\sim 1$--$10$ kpc)', xy=(8, 30),
             fontsize=9, color='blue', style='italic')

ax1.axhspan(500, 5000, alpha=0.08, color='red')
ax1.annotate('FR II coherent\n($L \\sim 100$ kpc--Mpc)', xy=(8, 1500),
             fontsize=9, color='red', style='italic')

# Lyubarsky (2009) critical B_phi/B_z ~ 1 for onset
ax1.axvline(1.0, ls=':', color='gray', alpha=0.5, lw=1.0)
ax1.annotate('$B_\\phi = B_z$', xy=(1.1, 2), fontsize=9, color='gray')

ax1.set_xlabel(r'$B_\phi / B_z$ (toroidal-to-axial field ratio)')
ax1.set_ylabel(r'Kink growth length $L_{\rm kink} / R_{\rm jet}$')
ax1.set_title('Current-driven kink instability growth length')
ax1.set_xlim(0.1, 30)
ax1.set_ylim(1, 1e5)
ax1.legend(loc='upper right', fontsize=10)

# Right panel: Morphology diagram in (B_phi/B_z, Gamma) plane
Gamma_grid = np.logspace(np.log10(1.5), np.log10(100), 200)
Bphi_Bz_grid = np.logspace(-0.5, 1.2, 200)
GG, BB = np.meshgrid(Gamma_grid, Bphi_Bz_grid)

# L_kink / R_jet
L_over_R = GG * (1.0 / BB) * np.sqrt(1 + 1.0 / BB**2)

# Contour levels: L/R = 10, 50, 100, 500, 1000
levels = [10, 50, 100, 500, 1000]

cf = ax2.contourf(GG, BB, np.log10(L_over_R), levels=np.linspace(0.5, 4.5, 20),
                   cmap='RdYlBu_r', alpha=0.7)
cs = ax2.contour(GG, BB, L_over_R, levels=levels,
                  colors='black', linewidths=1.0, linestyles='--')
ax2.clabel(cs, inline=True, fontsize=8, fmt=r'$L/R=%g$')

cbar = plt.colorbar(cf, ax=ax2)
cbar.set_label(r'$\log_{10}(L_{\rm kink}/R_{\rm jet})$')

# Mark observed AGN jets
agn_jets = {
    'M87': (6, 2.0),        # Gamma~6, moderate B_phi/B_z
    '3C 273': (15, 3.0),     # Gamma~15, higher B_phi/B_z
    'Cygnus A': (3, 0.5),    # Gamma~3, low B_phi/B_z => FR II
    'Centaurus A': (3, 3.0), # FR I
    '3C 31 (FR I)': (2, 5.0),  # typical FR I
}
for name, (gam, brat) in agn_jets.items():
    ax2.plot(gam, brat, 'o', ms=9, color='white', markeredgecolor='black',
             markeredgewidth=1.5, zorder=5)
    ax2.annotate(name, xy=(gam, brat), xytext=(5, 5),
                 textcoords='offset points', fontsize=8, color='black',
                 fontweight='bold')

# Shade FR I and FR II approximate regions
ax2.annotate('FR I\n(disrupted)', xy=(2.5, 8), fontsize=11, color='white',
             fontweight='bold', ha='center')
ax2.annotate('FR II\n(coherent)', xy=(30, 0.5), fontsize=11, color='navy',
             fontweight='bold', ha='center')

ax2.set_xlabel(r'Bulk Lorentz factor $\Gamma$')
ax2.set_ylabel(r'$B_\phi / B_z$')
ax2.set_title('AGN jet morphology: kink stability diagram')
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.set_xlim(1.5, 100)
ax2.set_ylim(0.3, 15)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_agn_kink_morphology.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_agn_kink_morphology.png')
print("Saved fig_agn_kink_morphology.pdf/png")
