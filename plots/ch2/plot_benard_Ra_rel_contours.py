"""
Plot: Relativistic Benard problem - Ra_rel contours for neutron star ocean.
Shows how the critical Rayleigh number varies with xi and boundary type.
"""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')); from SHARED_PLOT_STYLE import setup_style, COLORS
setup_style()

import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# --- Panel (a): Critical Ra vs xi for different boundary conditions ---
xi = np.linspace(0, 0.5, 200)

# Classical critical values
Ra_c_free = 657.511
Ra_c_rigid = 1707.762
Ra_c_mixed = 1100.65

# Relativistic: R_c^rel = R_c^class * (1 + xi)
Ra_rel_free = Ra_c_free * (1 + xi)
Ra_rel_rigid = Ra_c_rigid * (1 + xi)
Ra_rel_mixed = Ra_c_mixed * (1 + xi)

ax1.plot(xi, Ra_rel_rigid, '-', color=COLORS['relativistic'], linewidth=2.5, label='Both rigid')
ax1.plot(xi, Ra_rel_mixed, '--', color=COLORS['bdnk'], linewidth=2.5, label='One rigid, one free')
ax1.plot(xi, Ra_rel_free, '-.', color=COLORS['classical'], linewidth=2.5, label='Both free')

# Mark specific astrophysical regimes
astro_points = {
    'NS crust\n($\\xi=0.015$)': (0.015, Ra_c_rigid * 1.015),
    'NS core\n($\\xi=0.15$)': (0.15, Ra_c_rigid * 1.15),
    'QGP\n($\\xi=1/3$)': (1./3, Ra_c_rigid * (1 + 1./3)),
}

for label, (x, y) in astro_points.items():
    ax1.plot(x, y, 'o', markersize=8, color=COLORS['data'], zorder=5)
    offset = (10, 15) if 'crust' in label else (10, -20) if 'core' in label else (10, 10)
    ax1.annotate(label, (x, y), textcoords="offset points", xytext=offset, fontsize=9,
                 arrowprops=dict(arrowstyle='->', color='gray'))

ax1.axhline(Ra_c_rigid, color='gray', linestyle=':', alpha=0.5)
ax1.text(0.4, Ra_c_rigid - 30, f'Classical: {Ra_c_rigid:.1f}', color='gray', fontsize=9)

ax1.set_xlabel(r'$\xi = p_0/(\varepsilon_0 c^2)$', fontsize=14)
ax1.set_ylabel(r'$R_c^{\mathrm{rel}} = R_c^{\mathrm{class}} (1 + \xi)$', fontsize=14)
ax1.set_title('(a) Critical Rayleigh number vs. compactness', fontsize=12)
ax1.legend(fontsize=10, loc='upper left')
ax1.set_xlim(0, 0.5)

# --- Panel (b): Neutron star ocean parameter space ---
# For a NS ocean: g ~ 10^14 cm/s^2, d ~ 1-100 m, rho ~ 10^8-10^10 g/cm^3
# Thermal diffusivity kappa_T ~ 10^3-10^5 cm^2/s, nu ~ 1-10 cm^2/s
# beta = DeltaT/d, alpha ~ 10^-5 /K

# Compute Ra for different layer depths and temperature gradients
d_cm = np.logspace(2, 4, 100)  # 1 m to 100 m in cm
beta = np.logspace(3, 7, 100)  # K/cm temperature gradient

D, B = np.meshgrid(d_cm, beta)

# NS parameters
g_ns = 2e14  # cm/s^2
alpha_th = 1e-5  # 1/K
kappa_T = 1e4  # cm^2/s
nu = 5.0  # cm^2/s
xi_ns = 0.015  # NS crust

Ra_grid = g_ns * alpha_th * B * D**4 / (kappa_T * nu)
Ra_rel_grid = Ra_grid / (1 + xi_ns)  # Effective relativistic Ra

# Critical Ra for rigid boundaries
levels = [Ra_c_rigid, Ra_c_rigid * 10, Ra_c_rigid * 100, Ra_c_rigid * 1000]

cs = ax2.contourf(np.log10(D), np.log10(B), np.log10(Ra_rel_grid),
                   levels=np.linspace(0, 12, 25), cmap='RdYlBu_r')
plt.colorbar(cs, ax=ax2, label=r'$\log_{10}\,\mathrm{Ra}_{\mathrm{rel}}$')

# Mark critical contour
ax2.contour(np.log10(D), np.log10(B), np.log10(Ra_rel_grid),
            levels=[np.log10(Ra_c_rigid)], colors='white', linewidths=2.5)
ax2.text(2.6, 5.5, r'$\mathrm{Ra}_{\mathrm{rel}} = 1708$' + '\n(onset)', color='white',
         fontsize=10, fontweight='bold')

ax2.set_xlabel(r'$\log_{10}(d\,/\,\mathrm{cm})$', fontsize=14)
ax2.set_ylabel(r'$\log_{10}(\beta\,/\,\mathrm{K\,cm^{-1}})$', fontsize=14)
ax2.set_title(r'(b) NS ocean: $\mathrm{Ra}_{\mathrm{rel}}$ contours ($\xi=0.015$)', fontsize=12)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/ch2/fig_benard_Ra_rel_contours.pdf')
plt.close()
print("Saved fig_benard_Ra_rel_contours.pdf")
