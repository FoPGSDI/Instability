#!/usr/bin/env python3
"""
Magnetically stabilized RT: B-field threshold for jet stability.

In relativistic astrophysical jets (AGN, GRBs, microquasars), the
jet-cocoon interface is subject to RT instability when the jet
decelerates. A toroidal or poloidal magnetic field can stabilize the
interface. The critical field strength depends on the relativistic
Alfven speed and the enthalpy-based Atwood number.

Reference: Chandrasekhar Ch X §§96-97 (relativistic extension).
"""
import sys; sys.path.insert(0, '/data/haiyangw/claude/Instability'); from SHARED_PLOT_STYLE import setup_style, COLORS
import numpy as np
import matplotlib.pyplot as plt

setup_style()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Left panel: Critical B-field vs enthalpy ratio ---
# From the horizontal field dispersion (§97):
# n^2 = gk [ A_rel - 2 b^2 k_x^2 / ((w1+w2) k (1 - vA^2/c^2)) ]
# Stability when n^2 <= 0, i.e., B >= B_crit
# B_crit^2 ~ A_rel * g * (w1 + w2) * (1 - vA^2/c^2) / (2 k cos^2 theta)

# Enthalpy ratio w2/w1
w_ratio = np.linspace(1.01, 10.0, 500)
A_rel = (w_ratio - 1.0) / (w_ratio + 1.0)

# For different vA/c values
vA_over_c = [0.0, 0.3, 0.5, 0.7, 0.9]
colors_vA = ['#2196F3', '#4CAF50', '#FF9800', '#F44336', '#9C27B0']

for i, vc in enumerate(vA_over_c):
    # Critical condition: the magnetic stabilization must overcome RT
    # B_crit ~ sqrt(A_rel * g * (w1+w2) / (2k)) * (1 - vA^2/c^2)^{1/2}
    # Normalized: B_crit / B_0 where B_0 = sqrt(g * w_total / (2k))
    # = sqrt(A_rel) * (1 - vA^2/c^2)^{1/2}
    factor = np.sqrt(A_rel) * np.sqrt(1.0 - vc**2) if vc > 0 else np.sqrt(A_rel)
    label = 'Classical' if vc == 0 else rf'$v_A/c = {vc}$'
    ls = '-' if vc > 0 else '--'
    ax1.plot(w_ratio, factor, ls, color=colors_vA[i], linewidth=2.0, label=label)

ax1.set_xlabel(r'Enthalpy ratio $w_2/w_1$', fontsize=14)
ax1.set_ylabel(r'$B_\mathrm{crit} / B_0$', fontsize=14)
ax1.set_title('Critical B-field for RT stabilization', fontsize=14)
ax1.legend(loc='lower right', fontsize=10, frameon=True, edgecolor='0.7')
ax1.set_xlim(1, 10)
ax1.grid(True, linestyle=':', alpha=0.4)
ax1.text(0.05, 0.95, r'Horizontal field, $\cos\theta = 1$',
         transform=ax1.transAxes, fontsize=10, va='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# --- Right panel: Growth rate vs k for vertical field (§96) ---
# From eq rel96-dispersion (cubic in n_hat):
# Asymptotic: n -> g/vA * (sqrt(alpha2) - sqrt(alpha1)) * sqrt(1-vA^2/c^2) as k->inf
# n^2 -> gk (alpha2 - alpha1) as k -> 0

k = np.linspace(0.01, 10.0, 500)
alpha2_values = [0.6, 0.7, 0.8, 0.9]
alpha1_from_a2 = [1.0 - a for a in alpha2_values]

vA_c = 0.5  # moderate Alfven speed
g_norm = 1.0

for j, a2 in enumerate(alpha2_values):
    a1 = 1.0 - a2

    # Asymptotic limits for the growth rate
    # k -> 0: n^2 ~ g*k*(a2-a1)
    # k -> inf: n -> (g/vA) * (sqrt(a2) - sqrt(a1)) * sqrt(1 - vA^2/c^2)
    n_k0 = np.sqrt(g_norm * k * (a2 - a1))
    n_kinf = (g_norm / vA_c) * (np.sqrt(a2) - np.sqrt(a1)) * np.sqrt(1 - vA_c**2)

    # Simple interpolation that matches both limits
    # n = n_kinf * (1 - exp(-k * n_k0^2 / n_kinf^2))^{1/2} ... approximate
    n_approx = np.zeros_like(k)
    for ik, kk in enumerate(k):
        n_low = np.sqrt(g_norm * kk * (a2 - a1))
        n_high = n_kinf
        # Smooth interpolation
        n_approx[ik] = n_low * n_high / np.sqrt(n_low**2 + n_high**2)

    color = ['#2196F3', '#4CAF50', '#FF9800', '#F44336'][j]
    ax2.plot(k, n_approx, '-', color=color, linewidth=2.0,
             label=rf'$\alpha_2 = {a2}$')

    # Show the saturation level
    ax2.axhline(y=n_kinf, color=color, linestyle=':', alpha=0.3)

# Classical comparison (no magnetic field)
for j, a2 in enumerate(alpha2_values):
    a1 = 1.0 - a2
    n_class = np.sqrt(g_norm * k * (a2 - a1))
    color = ['#2196F3', '#4CAF50', '#FF9800', '#F44336'][j]
    ax2.plot(k, n_class, '--', color=color, linewidth=1.0, alpha=0.4)

ax2.plot([], [], '--', color='gray', alpha=0.5, label='No B-field')
ax2.plot([], [], '-', color='gray', label=rf'$v_A/c = {vA_c}$')

ax2.set_xlabel(r'Wavenumber $k$', fontsize=14)
ax2.set_ylabel(r'Growth rate $n$', fontsize=14)
ax2.set_title(r'RT with vertical B-field: growth rate saturation', fontsize=14)
ax2.legend(loc='upper left', fontsize=9, frameon=True, edgecolor='0.7')
ax2.set_xlim(0, 10)
ax2.grid(True, linestyle=':', alpha=0.4)
ax2.text(0.95, 0.05, 'Dotted: saturation levels',
         transform=ax2.transAxes, fontsize=9, ha='right',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

fig.tight_layout()
fig.savefig('/data/haiyangw/claude/Instability/plots/ch10/fig_magnetic_RT_jet.pdf')
fig.savefig('/data/haiyangw/claude/Instability/plots/ch10/fig_magnetic_RT_jet.png')
print("Saved fig_magnetic_RT_jet.pdf and fig_magnetic_RT_jet.png")
plt.close(fig)
