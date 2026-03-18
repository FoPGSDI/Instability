#!/usr/bin/env python3
"""
Agent 13: Magneto-convection in NS — Ra_rel(Q_rel) stability diagram.
Plots critical Rayleigh number vs Chandrasekhar number for
classical and relativistic cases with NS parameters.
"""
import sys; sys.path.insert(0, '/data/haiyangw/claude/Instability'); from SHARED_PLOT_STYLE import setup_style, COLORS, pi
import matplotlib.pyplot as plt
import numpy as np

setup_style()

Q = np.logspace(0, 8, 500)

def Ra_c_free(Q_val):
    """Critical Ra for two free boundaries: solve cubic 2x^3+3x^2 = 1+Q/pi^2,
    then Ra = pi^4 * (1+x)/x * [(1+x)^2 + Q/pi^2]."""
    Q1 = Q_val / pi**2
    # Newton's method for 2x^3 + 3x^2 - 1 - Q1 = 0
    x = max((Q1/2)**(1./3), 0.5)
    for _ in range(50):
        f = 2*x**3 + 3*x**2 - 1 - Q1
        fp = 6*x**2 + 6*x
        if abs(fp) < 1e-30:
            break
        x = x - f/fp
        x = max(x, 0.01)
    Ra = pi**4 * (1+x)/x * ((1+x)**2 + Q1)
    return Ra

Ra_classical = np.array([Ra_c_free(q) for q in Q])

fig, ax = plt.subplots(figsize=(8, 5.5))

# Classical
ax.loglog(Q, Ra_classical, '-', color=COLORS['classical'], lw=2.5, label='Classical')

# Relativistic corrections for various v_A^2/c^2
for vA2_c2, ls, clr, lbl in [
    (0.01, '--', '#4CAF50', r'$v_A^2/c^2 = 0.01$ (outer core)'),
    (0.05, '-.', '#FF9800', r'$v_A^2/c^2 = 0.05$'),
    (0.1, ':', '#F44336', r'$v_A^2/c^2 = 0.1$ (inner core)'),
]:
    # Q_rel = Q * rho*c^2 / w = Q * (1 - vA^2/c^2) approximately
    Q_rel = Q * (1 - vA2_c2)
    Ra_rel = np.array([Ra_c_free(q) for q in Q_rel])
    ax.loglog(Q, Ra_rel, ls, color=clr, lw=2, label=lbl)

# Asymptotic pi^2 Q law
ax.loglog(Q, pi**2 * Q, ':', color='gray', lw=1, alpha=0.7, label=r'$\pi^2 Q$ asymptote')

ax.set_xlabel(r'Chandrasekhar number $Q$')
ax.set_ylabel(r'Critical Rayleigh number $\mathrm{Ra}_c$')
ax.set_title('Magneto-convection stability: classical vs relativistic (NS parameters)')
ax.set_xlim(1, 1e8)
ax.set_ylim(500, 1e10)
ax.legend(loc='upper left', fontsize=9.5)

# Shade magnetar regime
ax.axvspan(1e5, 1e8, alpha=0.05, color='red', label=None)
ax.text(3e6, 800, 'Magnetar\nregime', fontsize=9, color='red', ha='center', style='italic')

fig.tight_layout()
fig.savefig('/data/haiyangw/claude/Instability/plots/ch4/fig_magneto_convection_stability.pdf')
fig.savefig('/data/haiyangw/claude/Instability/plots/ch4/fig_magneto_convection_stability.png')
print("Saved fig_magneto_convection_stability.pdf/png")
