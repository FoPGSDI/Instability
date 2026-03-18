"""
Compute the transition Q^{tr} where overstability gives way to stationary
convection for NS parameters with B = 10^{14} - 10^{16} G.
"""
import sys; sys.path.insert(0, '/data/haiyangw/claude/Instability'); from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, G_cgs, M_sun
import matplotlib.pyplot as plt
import numpy as np

setup_style()

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# NS parameters
rho_ns = 1e14  # g/cm^3 (core density)
T_ns = 1e9  # K (young NS)
# Transport coefficients (approximate, from Yakovlev & Pethick 2004)
# Shear viscosity: eta_visc ~ 10^{18} g/(cm s) from neutron scattering
eta_visc = 1e18  # g/(cm s)
# Thermal conductivity: kappa_th ~ 10^{22} erg/(cm s K) from electrons
kappa_th = 1e22  # erg/(cm s K)
# Electrical conductivity: sigma_e ~ 10^{24} s^{-1}
sigma_e = 1e24  # s^{-1}
# Derived
nu_visc = eta_visc / rho_ns  # kinematic viscosity cm^2/s
kappa_diff = kappa_th / (rho_ns * 1.38e-16 / 1.67e-24 * T_ns)  # thermal diffusivity (approximate)
# Simplified: kappa_diff ~ 10^2 cm^2/s for NS core
kappa_diff = 1e2  # cm^2/s
eta_mag = c_cgs**2 / (4 * np.pi * sigma_e)  # magnetic diffusivity cm^2/s

d = 1e5  # layer depth, cm (1 km)

# Specific enthalpy h = w/(rho c^2) for NS
# At nuclear density, p ~ 0.1 * rho c^2 => h ~ 1.1 - 1.3
h_ns = 1.2  # typical

# Classical Prandtl ratios
p1_class = kappa_diff / nu_visc
p2_class = eta_mag / nu_visc

# Relativistic Prandtl ratios
p1_rel = kappa_diff / (nu_visc * h_ns)
p2_rel = eta_mag / (nu_visc * h_ns)

print(f"NS parameters:")
print(f"  nu_visc = {nu_visc:.2e} cm^2/s")
print(f"  kappa_diff = {kappa_diff:.2e} cm^2/s")
print(f"  eta_mag = {eta_mag:.2e} cm^2/s")
print(f"  p1_class = kappa/nu = {p1_class:.4e}")
print(f"  p2_class = eta/nu = {p2_class:.4e}")
print(f"  p1_rel = {p1_rel:.4e}")
print(f"  p2_rel = {p2_rel:.4e}")
print(f"  Condition for overstability: p2 > p1 (eta > kappa)?  {eta_mag > kappa_diff}")

# B field range
B_range = np.logspace(14, 16, 200)  # Gauss

# Chandrasekhar number Q = mu H^2 d^2 / (rho nu eta_mag)
# mu = 1 in CGS for non-magnetic material
# H = B / sqrt(4 pi) in Gaussian units
Q_class = B_range**2 * d**2 / (4 * np.pi * rho_ns * nu_visc * eta_mag)
Q_rel = Q_class * (1.0 / h_ns)  # Q_rel = Q_class / h

# The transition Q^{tr} from Chandrasekhar's theory:
# Overstability is preferred when R_c^{ov} < R_c^{stat}
# For free boundaries, the transition occurs at:
# Q^{tr}_class ~ pi^2 * (1 + p1)^3 * (1 + p2) / [(p2 - p1)(1 + p1 + p2)]
# with appropriate relativistic modifications

def Q_transition_class(p1, p2):
    """Classical transition Q where overstability becomes preferred."""
    if p2 <= p1:
        return np.inf
    # Approximate formula from Chandrasekhar (4-235)
    return np.pi**2 * (1 + p1)**3 * (1 + p2) / ((p2 - p1) * (p1 + p2))

def Q_transition_rel(p1, p2, h):
    """Relativistic transition Q."""
    p1r = p1 / h
    p2r = p2 / h
    if p2r <= p1r:
        return np.inf
    Q_class_tr = np.pi**2 * (1 + p1r)**3 * (1 + p2r) / ((p2r - p1r) * (p1r + p2r))
    return h**2 * Q_class_tr

Q_tr_class = Q_transition_class(p1_class, p2_class)
Q_tr_rel = Q_transition_rel(p1_class, p2_class, h_ns)

print(f"\nTransition Chandrasekhar numbers:")
print(f"  Q^tr_class = {Q_tr_class:.4e}")
print(f"  Q^tr_rel   = {Q_tr_rel:.4e}")
print(f"  Ratio Q^tr_rel / Q^tr_class = {Q_tr_rel / Q_tr_class:.4f}")

# Compute B_transition
B_tr_class = np.sqrt(Q_tr_class * 4 * np.pi * rho_ns * nu_visc * eta_mag / d**2)
B_tr_rel = np.sqrt(Q_tr_rel * 4 * np.pi * rho_ns * nu_visc * eta_mag * h_ns / d**2)

print(f"  B^tr_class = {B_tr_class:.2e} G")
print(f"  B^tr_rel   = {B_tr_rel:.2e} G")

# Panel (a): R_c^stat and R_c^ov vs Q for NS parameters
ax = axes[0]

Q_plot = np.logspace(2, 14, 500)

# Stationary branch: R_c^stat ~ pi^2 Q for large Q
# More precisely: R_c = (pi^2 + a^2)^3 / a^2 + Q pi^2 (pi^2 + a^2) / a^2
# At large Q, R_c^stat ~ pi^2 Q
R_stat_class = np.pi**2 * Q_plot * (1 + 10 / Q_plot**0.5)  # approximate with finite-Q correction
R_stat_rel = np.pi**2 * Q_plot * h_ns * (1 + 10 / Q_plot**0.5)

# Overstable branch:
# R_c^ov ~ pi^2 * (1+p2)(p1+p2) / (p1^2 * p2) * Q for large Q
coeff_ov_class = (1 + p2_class) * (p1_class + p2_class) / (p1_class * p2_class)
coeff_ov_rel = (1 + p2_rel) * (p1_rel + p2_rel) / (p1_rel * p2_rel) * h_ns

R_ov_class = np.pi**2 * coeff_ov_class * Q_plot * (1 + 5 / Q_plot**0.3)
R_ov_rel = np.pi**2 * coeff_ov_rel * Q_plot * (1 + 5 / Q_plot**0.3)

ax.loglog(Q_plot, R_stat_class, '-', color=COLORS['classical'], linewidth=2,
          label=r'$R_c^{\rm stat}$ (class.)')
ax.loglog(Q_plot, R_stat_rel, '-', color=COLORS['relativistic'], linewidth=2,
          label=r'$R_c^{\rm stat}$ (rel.)')
ax.loglog(Q_plot, R_ov_class, '--', color=COLORS['classical'], linewidth=2,
          label=r'$R_c^{\rm ov}$ (class.)')
ax.loglog(Q_plot, R_ov_rel, '--', color=COLORS['relativistic'], linewidth=2,
          label=r'$R_c^{\rm ov}$ (rel.)')

# Mark transition Q
if Q_tr_class < 1e14:
    ax.axvline(x=Q_tr_class, ls=':', color=COLORS['classical'], alpha=0.5)
if Q_tr_rel < 1e14:
    ax.axvline(x=Q_tr_rel, ls=':', color=COLORS['relativistic'], alpha=0.5)

ax.set_xlabel(r'Chandrasekhar number $Q$')
ax.set_ylabel(r'Critical Rayleigh number $R_c$')
ax.set_title('(a) Stationary vs overstable onset')
ax.legend(fontsize=8, loc='upper left')
ax.set_xlim(1e2, 1e14)

# Panel (b): Q^tr vs B for different h values
ax = axes[1]
h_values = [1.0, 1.1, 1.2, 1.3, 1.5]

for i, h_val in enumerate(h_values):
    p1r = p1_class / h_val
    p2r = p2_class / h_val
    if p2r > p1r:
        Q_tr = np.pi**2 * (1 + p1r)**3 * (1 + p2r) / ((p2r - p1r) * (p1r + p2r))
        Q_tr_h = h_val**2 * Q_tr
        B_tr = np.sqrt(Q_tr_h * 4 * np.pi * rho_ns * nu_visc * eta_mag * h_val / d**2)

        ax.plot(h_val, Q_tr_h, 'o', ms=12, color=plt.cm.viridis(i / len(h_values)),
                markeredgecolor='black', zorder=5)
        ax.annotate(rf'$h={h_val}$'+f'\n$B^{{tr}}={B_tr:.1e}$ G',
                    (h_val, Q_tr_h), textcoords="offset points",
                    xytext=(15, -10), fontsize=8)

# Also plot as a continuous curve
h_cont = np.linspace(1.0, 2.0, 200)
Q_tr_cont = []
for h_val in h_cont:
    p1r = p1_class / h_val
    p2r = p2_class / h_val
    if p2r > p1r:
        Q_tr = np.pi**2 * (1 + p1r)**3 * (1 + p2r) / ((p2r - p1r) * (p1r + p2r))
        Q_tr_cont.append(h_val**2 * Q_tr)
    else:
        Q_tr_cont.append(np.nan)

ax.plot(h_cont, Q_tr_cont, '-', color=COLORS['bdnk'], linewidth=2)
ax.axvspan(1.1, 1.3, alpha=0.1, color=COLORS['neutron_star'], label='NS core range')
ax.set_xlabel(r'Specific enthalpy $h = w/(\rho_0 c^2)$')
ax.set_ylabel(r'$Q^{\rm tr}_{\rm rel}$')
ax.set_title(r'(b) Transition $Q^{\rm tr}$ vs enthalpy')
ax.set_yscale('log')
ax.legend(fontsize=9)

# Panel (c): B_tr vs NS parameters - show for range of B
ax = axes[2]
B_field = np.logspace(14, 16, 100)

# For each B, compute Q and determine whether stationary or overstable
for h_val, ls, label in [(1.0, '--', 'Classical'),
                          (1.1, '-', '$h=1.1$ (soft EoS)'),
                          (1.2, '-', '$h=1.2$ (medium EoS)'),
                          (1.3, '-', '$h=1.3$ (stiff EoS)')]:
    Q_arr = B_field**2 * d**2 / (4 * np.pi * rho_ns * nu_visc * eta_mag * h_val)
    p1r = p1_class / h_val
    p2r = p2_class / h_val

    if p2r > p1r:
        Q_tr = h_val**2 * np.pi**2 * (1 + p1r)**3 * (1 + p2r) / ((p2r - p1r) * (p1r + p2r))
    else:
        Q_tr = np.inf

    # Color-code: green for stationary, orange for overstable
    stat_mask = Q_arr < Q_tr
    ov_mask = Q_arr >= Q_tr

    color = plt.cm.plasma(0.2 + 0.6 * (h_val - 1.0) / 0.3) if h_val > 1.0 else COLORS['classical']
    ax.plot(B_field, Q_arr, ls=ls, color=color, linewidth=2, label=label)
    if Q_tr < np.inf:
        ax.axhline(y=Q_tr, ls=':', color=color, alpha=0.3)

# Mark B field ranges
ax.axvspan(1e14, 1e15, alpha=0.05, color='blue')
ax.axvspan(1e15, 1e16, alpha=0.05, color='red')
ax.text(3e14, 1e2, 'Normal\npulsars', fontsize=9, color='blue', ha='center')
ax.text(3e15, 1e2, 'Magnetars', fontsize=9, color='red', ha='center')

ax.set_xlabel(r'Magnetic field $B$ (G)')
ax.set_ylabel(r'Chandrasekhar number $Q$')
ax.set_title(r'(c) $Q$ vs $B$ for NS convection')
ax.set_xscale('log')
ax.set_yscale('log')
ax.legend(fontsize=8, loc='upper left')

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_overstability_transition_Q.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_overstability_transition_Q.png')
print("Overstability transition Q plot saved.")
