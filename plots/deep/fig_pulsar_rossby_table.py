"""
Relativistic Rossby number for known pulsars.
Computes Ro_rel = U / (2 * Omega_eff * L) with relativistic corrections.
Produces table and bar chart for ~5 pulsars.
"""
import sys; sys.path.insert(0, '../../..'); from SHARED_PLOT_STYLE import setup_style, COLORS, G_cgs, c_cgs, M_sun
import matplotlib.pyplot as plt
import numpy as np

setup_style()

# Pulsar data: name, period (ms), mass (M_sun), radius (km), estimated convective velocity (cm/s)
# Convective velocity estimated from mixing-length theory: U ~ (L * g * alpha * Delta_T)^{1/3}
pulsars = [
    {'name': 'PSR J1748-2446ad', 'P_ms': 1.40, 'M': 1.4, 'R_km': 12.0,
     'U_conv': 1e6, 'L_conv_km': 1.0, 'note': 'Fastest known'},
    {'name': 'PSR B1937+21', 'P_ms': 1.56, 'M': 1.4, 'R_km': 11.5,
     'U_conv': 8e5, 'L_conv_km': 1.0, 'note': 'First MSP'},
    {'name': 'PSR J0537-6910', 'P_ms': 16.1, 'M': 1.4, 'R_km': 12.0,
     'U_conv': 5e5, 'L_conv_km': 2.0, 'note': 'Young, frequent glitches'},
    {'name': 'Crab pulsar', 'P_ms': 33.5, 'M': 1.4, 'R_km': 12.0,
     'U_conv': 3e5, 'L_conv_km': 3.0, 'note': 'Young pulsar'},
    {'name': 'Vela pulsar', 'P_ms': 89.3, 'M': 1.4, 'R_km': 12.0,
     'U_conv': 2e5, 'L_conv_km': 3.0, 'note': 'Glitching pulsar'},
]

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

names = []
Ro_class_list = []
Ro_rel_list = []
regime_list = []

print("=" * 90)
print(f"{'Pulsar':<25} {'P (ms)':>8} {'Omega':>10} {'Omega_LT':>10} {'Ro_class':>10} {'Ro_rel':>10} {'Regime'}")
print("=" * 90)

for p in pulsars:
    P = p['P_ms'] * 1e-3  # seconds
    Omega = 2 * np.pi / P  # rad/s
    M = p['M'] * M_sun  # grams
    R = p['R_km'] * 1e5  # cm
    U = p['U_conv']  # cm/s
    L = p['L_conv_km'] * 1e5  # cm

    # Moment of inertia (approximate)
    I = 0.35 * M * R**2

    # Lense-Thirring precession rate
    Omega_LT = 2 * G_cgs * I * Omega / (c_cgs**2 * R**3)

    # Effective rotation rate
    Omega_eff = Omega - Omega_LT

    # Compactness
    C_compact = G_cgs * M / (R * c_cgs**2)

    # Enthalpy correction (NS core: h ~ 1 + xi, xi ~ 0.1-0.2)
    xi = 2 * C_compact  # approximate from TOV
    h = 1 + xi

    # Classical Rossby number
    Ro_class = U / (2 * Omega * L)

    # Relativistic Rossby number: accounts for frame dragging and enthalpy
    # Ro_rel = U / (2 * Omega_eff * L * h)
    # The factor h enters because the effective inertia is w/c^2 not rho
    Ro_rel = U / (2 * Omega_eff * L * h)

    # Regime determination
    if Ro_rel < 0.1:
        regime = 'Rotation-dominated'
    elif Ro_rel < 1.0:
        regime = 'Intermediate'
    else:
        regime = 'Convection-dominated'

    names.append(p['name'].replace('PSR ', ''))
    Ro_class_list.append(Ro_class)
    Ro_rel_list.append(Ro_rel)
    regime_list.append(regime)

    print(f"{p['name']:<25} {p['P_ms']:>8.2f} {Omega:>10.1f} {Omega_LT:>10.1f} "
          f"{Ro_class:>10.4f} {Ro_rel:>10.4f} {regime}")

print("=" * 90)

# Panel (a): Bar chart comparing Ro_class and Ro_rel
ax = axes[0]
x = np.arange(len(names))
width = 0.35

bars1 = ax.bar(x - width/2, Ro_class_list, width, color=COLORS['classical'],
               label=r'${\rm Ro}_{\rm class}$', alpha=0.8, edgecolor='black', linewidth=0.5)
bars2 = ax.bar(x + width/2, Ro_rel_list, width, color=COLORS['relativistic'],
               label=r'${\rm Ro}_{\rm rel}$', alpha=0.8, edgecolor='black', linewidth=0.5)

ax.axhline(y=0.1, ls='--', color='gray', alpha=0.5)
ax.axhline(y=1.0, ls='--', color='gray', alpha=0.5)
ax.text(4.6, 0.12, 'Rotation-dominated', fontsize=8, color='gray', va='bottom')
ax.text(4.6, 1.05, 'Convection-dominated', fontsize=8, color='gray', va='bottom')

ax.set_yscale('log')
ax.set_ylabel(r'Rossby number Ro')
ax.set_title('(a) Relativistic Rossby number for known pulsars')
ax.set_xticks(x)
ax.set_xticklabels(names, rotation=30, ha='right', fontsize=9)
ax.legend(fontsize=10)
ax.set_ylim(1e-4, 10)

# Panel (b): Ro_rel vs spin period, with regime bands
ax = axes[1]
P_range = np.logspace(-0.5, 3, 500)  # ms
Omega_range = 2 * np.pi / (P_range * 1e-3)

# Typical NS parameters
M_typ = 1.4 * M_sun
R_typ = 12e5  # cm
I_typ = 0.35 * M_typ * R_typ**2
U_typ = 5e5  # cm/s
L_typ = 2e5  # cm
C_typ = G_cgs * M_typ / (R_typ * c_cgs**2)
xi_typ = 2 * C_typ
h_typ = 1 + xi_typ

Omega_LT_range = 2 * G_cgs * I_typ * Omega_range / (c_cgs**2 * R_typ**3)
Omega_eff_range = Omega_range - Omega_LT_range

Ro_class_curve = U_typ / (2 * Omega_range * L_typ)
Ro_rel_curve = U_typ / (2 * Omega_eff_range * L_typ * h_typ)

ax.loglog(P_range, Ro_class_curve, '-', color=COLORS['classical'],
          linewidth=2, label=r'${\rm Ro}_{\rm class}$')
ax.loglog(P_range, Ro_rel_curve, '-', color=COLORS['relativistic'],
          linewidth=2, label=r'${\rm Ro}_{\rm rel}$')

# Plot individual pulsars
for i, p in enumerate(pulsars):
    ax.plot(p['P_ms'], Ro_rel_list[i], 'o', ms=8, color=COLORS['data'],
            zorder=5, markeredgecolor='black', markeredgewidth=0.5)
    ax.annotate(names[i], (p['P_ms'], Ro_rel_list[i]),
                textcoords="offset points", xytext=(5, 5), fontsize=7)

# Regime shading
ax.axhspan(0, 0.1, alpha=0.08, color='blue')
ax.axhspan(0.1, 1.0, alpha=0.05, color='yellow')
ax.axhspan(1.0, 100, alpha=0.08, color='red')
ax.text(0.5, 0.02, 'Rotation-dominated', fontsize=9, color='blue')
ax.text(5, 0.3, 'Intermediate', fontsize=9, color='orange')
ax.text(200, 3, 'Convection-\ndominated', fontsize=9, color='red')

ax.set_xlabel('Spin period (ms)')
ax.set_ylabel(r'Rossby number Ro')
ax.set_title(r'(b) ${\rm Ro}_{\rm rel}$ vs spin period')
ax.legend(fontsize=10, loc='lower right')
ax.set_xlim(0.5, 1000)
ax.set_ylim(1e-4, 100)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_pulsar_rossby_table.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_pulsar_rossby_table.png')
print("Pulsar Rossby number plot saved.")
