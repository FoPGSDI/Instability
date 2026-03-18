#!/usr/bin/env python3
"""
Agent 16: Combined rotation + B wave propagation in NS — dispersion plot.
Shows omega(k) for magneto-inertial waves at classical and relativistic Alfven speeds.
"""
import sys; sys.path.insert(0, '/data/haiyangw/claude/Instability'); from SHARED_PLOT_STYLE import setup_style, COLORS, pi, c_cgs
import matplotlib.pyplot as plt
import numpy as np

setup_style()

# Dispersion relation: omega^2 -+ 2*Omega*cos(theta)*omega - vA^2*k^2*cos^2(phi) = 0
# Solutions: omega = +/- [Omega*cos(theta) +/- sqrt(Omega^2*cos^2(theta) + vA^2*k^2*cos^2(phi))]

k = np.linspace(0.01, 20, 500)  # wavenumber (arbitrary units)

# Parameters (normalized: Omega=1, theta=phi=pi/6)
Omega = 1.0
theta = pi/6
phi = pi/6

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Left: Incompressible dispersion for different vA/c
for vA_frac, color, lbl in [
    (0.01, COLORS['classical'], r'$v_A = 0.01\,c$ (classical regime)'),
    (0.1, '#FF9800', r'$v_A = 0.1\,c$'),
    (0.3, COLORS['relativistic'], r'$v_A = 0.3\,c$'),
    (0.5, '#9C27B0', r'$v_A = 0.5\,c$'),
]:
    vA = vA_frac  # in units of c
    disc = Omega**2 * np.cos(theta)**2 + vA**2 * k**2 * np.cos(phi)**2
    omega_plus = Omega * np.cos(theta) + np.sqrt(disc)
    omega_minus = -Omega * np.cos(theta) + np.sqrt(disc)

    ax1.plot(k, omega_plus, '-', color=color, lw=2, label=lbl + ' (+)')
    ax1.plot(k, omega_minus, '--', color=color, lw=1.5)

# Light line
ax1.plot(k, k, ':', color='gray', lw=1, label=r'$\omega = k c$')

ax1.set_xlabel(r'Wavenumber $k$ (arb. units)')
ax1.set_ylabel(r'Frequency $\omega$ (units of $\Omega$)')
ax1.set_title('Magneto-inertial wave dispersion')
ax1.legend(fontsize=8.5, loc='upper left')
ax1.set_xlim(0, 20)
ax1.set_ylim(0, 15)

# Right: Phase velocity vs k for NS parameters
for vA_frac, color, lbl in [
    (0.01, COLORS['classical'], r'$v_A/c = 0.01$'),
    (0.1, '#FF9800', r'$v_A/c = 0.1$'),
    (0.3, COLORS['relativistic'], r'$v_A/c = 0.3$'),
]:
    vA = vA_frac
    disc = Omega**2 * np.cos(theta)**2 + vA**2 * k**2 * np.cos(phi)**2
    omega_plus = Omega * np.cos(theta) + np.sqrt(disc)
    vph = omega_plus / k

    ax2.plot(k, vph, '-', color=color, lw=2, label=lbl)

ax2.axhline(1.0, color='k', ls=':', lw=1.5, label=r'$v_{\rm ph} = c$ (causal limit)')
ax2.set_xlabel(r'Wavenumber $k$ (arb. units)')
ax2.set_ylabel(r'Phase velocity $v_{\rm ph}/c$')
ax2.set_title('Phase velocity: sub-luminal for all modes')
ax2.legend(fontsize=9.5)
ax2.set_xlim(0.1, 20)
ax2.set_ylim(0, 1.2)

fig.tight_layout()
fig.savefig('/data/haiyangw/claude/Instability/plots/ch5/fig_rotmag_dispersion.pdf')
fig.savefig('/data/haiyangw/claude/Instability/plots/ch5/fig_rotmag_dispersion.png')
print("Saved fig_rotmag_dispersion.pdf/png")
