"""
Plot: BDNK vs classical dispersion relation for thermal modes in the Benard problem.
Shows how BDNK modifies the dispersion at high wavenumber while preserving hydrodynamic modes.
"""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')); from SHARED_PLOT_STYLE import setup_style, COLORS
setup_style()

import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# --- Panel (a): Growth rate sigma vs wavenumber a ---
# Classical dispersion: sigma is real at marginal state
# For the Benard problem with both-free BCs at Ra near Ra_c:
# sigma_* solves: (pi^2 + a^2 - sigma)(pi^2 + a^2 - Pr*sigma)(pi^2 + a^2) = Ra * a^2
# At marginal state sigma=0: (pi^2+a^2)^3 = Ra*a^2

a = np.linspace(0.5, 8, 500)
Ra_c = 657.511  # both free
Pr = 1.0  # Prandtl number

# For supercritical Ra (Ra/Ra_c = 1.5), find growth rate
# Approximate: sigma ~ (Ra - Ra_c(a)) * a^2 / [(pi^2+a^2)^2 * (1 + Pr)]
Ra_over_Rac = np.array([1.0, 1.1, 1.5, 2.0])

for i, ratio in enumerate(Ra_over_Rac):
    Ra = Ra_c * ratio
    Ra_a = (np.pi**2 + a**2)**3 / a**2  # Ra_c(a) function
    # Growth rate approximation (valid near marginal)
    sigma_approx = (Ra - Ra_a) * a**2 / ((np.pi**2 + a**2)**2 * (1 + Pr))

    color = COLORS['classical'] if ratio == 1.0 else plt.cm.Reds(0.3 + 0.5 * (ratio - 1))
    ls = '--' if ratio == 1.0 else '-'
    label = f'Ra/Ra$_c$ = {ratio:.1f}'
    ax1.plot(a, sigma_approx, ls, color=color, linewidth=1.8, label=label)

ax1.axhline(0, color='black', linewidth=0.5)
ax1.set_xlabel(r'Horizontal wavenumber $a = kd$', fontsize=14)
ax1.set_ylabel(r'Growth rate $\sigma_*$', fontsize=14)
ax1.set_title('(a) Classical growth rate (both free)', fontsize=12)
ax1.set_ylim(-50, 30)
ax1.set_xlim(0.5, 8)
ax1.legend(fontsize=10)

# --- Panel (b): BDNK vs Israel-Stewart mode structure ---
# Schematic: BDNK has 3 modes, IS has 5
k = np.linspace(0.01, 5, 500)

# Hydrodynamic modes (same in both BDNK and IS)
# Heat mode: omega = -i * kappa_T * k^2
kappa_T_eff = 0.5
omega_heat = -kappa_T_eff * k**2

# Sound modes: omega = +/- c_s k - i * Gamma_s k^2
c_s = 0.3  # in units of c
Gamma_s = 0.1
omega_sound_re = c_s * k
omega_sound_im = -Gamma_s * k**2

# Shear mode: omega = -i * nu * k^2
nu_eff = 0.3
omega_shear = -nu_eff * k**2

# IS transient modes (not present in BDNK)
tau_q = 0.1  # relaxation time
tau_pi = 0.08
omega_IS_heat = -1.0 / tau_q * np.ones_like(k) - 0.5 * kappa_T_eff * k**2
omega_IS_shear = -1.0 / tau_pi * np.ones_like(k) - 0.3 * nu_eff * k**2

# Plot imaginary parts (damping rates)
ax2.plot(k, omega_heat, '-', color=COLORS['bdnk'], linewidth=2.5, label='BDNK: heat mode')
ax2.plot(k, omega_sound_im, '-', color=COLORS['relativistic'], linewidth=2.5, label='BDNK: sound modes')
ax2.plot(k, omega_shear, '-', color=COLORS['is'], linewidth=2.5, label='BDNK: shear mode')

# IS transient modes
ax2.plot(k, omega_IS_heat, '--', color=COLORS['bdnk'], linewidth=1.5, alpha=0.5,
         label=r'IS: heat relaxation ($\tau_q^{-1}$)')
ax2.plot(k, omega_IS_shear, '--', color=COLORS['is'], linewidth=1.5, alpha=0.5,
         label=r'IS: shear relaxation ($\tau_\pi^{-1}$)')

# Mark the relaxation gap
ax2.axhline(-1.0/tau_q, color='gray', linestyle=':', alpha=0.3)
ax2.text(0.2, -1.0/tau_q + 0.3, r'$-1/\tau_q$', color='gray', fontsize=9)
ax2.axhline(-1.0/tau_pi, color='gray', linestyle=':', alpha=0.3)
ax2.text(0.2, -1.0/tau_pi + 0.3, r'$-1/\tau_\pi$', color='gray', fontsize=9)

ax2.set_xlabel(r'Wavenumber $k d$', fontsize=14)
ax2.set_ylabel(r'$\mathrm{Im}(\omega)\, d^2/\nu$  (damping rate)', fontsize=14)
ax2.set_title('(b) BDNK (3 modes) vs IS (5 modes)', fontsize=12)
ax2.set_ylim(-15, 1)
ax2.legend(fontsize=8.5, loc='lower left')

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/ch2/fig_bdnk_vs_classical_dispersion.pdf')
plt.close()
print("Saved fig_bdnk_vs_classical_dispersion.pdf")
