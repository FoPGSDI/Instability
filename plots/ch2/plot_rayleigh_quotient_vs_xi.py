"""
Plot: Relativistic Rayleigh quotient as a function of xi.
Shows how the enthalpy weight modifies the variational principle.
"""
import sys; sys.path.insert(0, '../..'); from SHARED_PLOT_STYLE import setup_style, COLORS
setup_style()

import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# --- Panel (a): Rayleigh quotient ratio vs xi ---
xi = np.linspace(0, 0.5, 500)

# For both-free BCs: Ra_rel = Ra_class * (w/rho c^2) = Ra_class * (1 + xi)/(1)
# The Rayleigh quotient: Ra_rel = I1_rel / I2_rel
# where I2_rel has weight (epsilon+p)/c^2 = rho(1+xi)
# So Ra_rel/Ra_class = 1/(1+xi) for the quotient itself (at same eigenfunction)
# But the actual critical Ra in classical terms is Ra_c_class * (1+xi)

ratio_quotient = 1.0 / (1.0 + xi)  # Quotient decreases with xi
ratio_critical = 1.0 + xi  # Critical Ra (classical measure) increases

ax1.plot(xi, ratio_quotient, '-', color=COLORS['bdnk'], linewidth=2.5,
         label=r'$\mathscr{R}_{\mathrm{rel}}/\mathscr{R}_{\mathrm{class}}$ (Rayleigh quotient)')
ax1.plot(xi, ratio_critical, '-', color=COLORS['relativistic'], linewidth=2.5,
         label=r'$R_c^{\mathrm{rel}}/R_c^{\mathrm{class}}$ (critical Ra)')
ax1.plot(xi, np.ones_like(xi), ':', color='gray', linewidth=1)

# Annotate specific values
for xi_val, name in [(0.015, 'NS crust'), (0.15, 'NS core'), (1./3, 'QGP')]:
    ax1.plot(xi_val, 1 + xi_val, 'o', color=COLORS['relativistic'], markersize=7)
    ax1.plot(xi_val, 1./(1+xi_val), 's', color=COLORS['bdnk'], markersize=7)
    ax1.annotate(name, (xi_val, 1 + xi_val), textcoords="offset points",
                 xytext=(8, 5), fontsize=9, color=COLORS['relativistic'])

ax1.set_xlabel(r'$\xi = p_0/(\varepsilon_0 c^2)$', fontsize=14)
ax1.set_ylabel('Ratio to classical value', fontsize=14)
ax1.set_title(r'(a) Relativistic modification of Rayleigh quotient', fontsize=12)
ax1.legend(fontsize=10, loc='center left')

# --- Panel (b): Viscous dissipation vs buoyancy release ---
# Show the energy balance epsilon_v = epsilon_g as a function of xi
# epsilon_v^rel / epsilon_v^class = (1 + xi) (enthalpy weight in viscous dissipation)
# epsilon_g^rel / epsilon_g^class = (1 + xi) (enthalpy weight in buoyancy)

xi_range = np.linspace(0, 0.5, 100)

# At the critical state, the balance gives Ra
# Viscous dissipation rate (normalized)
eps_v = 1 + xi_range  # increases with xi due to enthalpy inertia
eps_g = 1 + xi_range  # buoyancy also increases

# For sub-critical Ra (say Ra = 0.8 * Ra_c_rel)
eps_v_sub = 0.8 * (1 + xi_range)
eps_g_sub = 1 + xi_range  # buoyancy release exceeds dissipation? No - subcritical means no convection

ax2.fill_between(xi_range, 1, 1 + xi_range, alpha=0.15, color=COLORS['relativistic'],
                  label='Relativistic enhancement')
ax2.plot(xi_range, eps_v, '-', color=COLORS['relativistic'], linewidth=2.5,
         label=r'$\epsilon_v^{\mathrm{rel}} / \epsilon_v^{\mathrm{class}}$')
ax2.plot(xi_range, eps_g, '--', color=COLORS['bdnk'], linewidth=2.5,
         label=r'$\epsilon_g^{\mathrm{rel}} / \epsilon_g^{\mathrm{class}}$')

# Show the entropy production contribution
entropy_rate = (1 + xi_range) * (1 + 0.5 * xi_range)  # schematic
ax2.plot(xi_range, entropy_rate, '-.', color=COLORS['data'], linewidth=2,
         label=r'$\dot{S}_{\mathrm{prod}}^{\mathrm{rel}}/\dot{S}_{\mathrm{prod}}^{\mathrm{class}}$')

ax2.set_xlabel(r'$\xi = p_0/(\varepsilon_0 c^2)$', fontsize=14)
ax2.set_ylabel('Ratio to classical value', fontsize=14)
ax2.set_title('(b) Energy balance at marginal stability', fontsize=12)
ax2.legend(fontsize=10)
ax2.set_ylim(0.9, 2.0)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/ch2/fig_rayleigh_quotient_vs_xi.pdf')
plt.close()
print("Saved fig_rayleigh_quotient_vs_xi.pdf")
