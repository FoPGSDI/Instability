"""
Observed vs predicted knot spacing for 5 AGN jets.

Physics:
- Knot spacing set by gravitational/capillary fragmentation scale
- From rel_chapter_12_sec110.tex eq. (rel-12-110-17):
  lambda_min = 2*pi*R / x_a, where x_a depends on H/H_0,rel
- Magnetic stabilization criterion:
  H_0,rel = 4*pi*R*c * sqrt(G * rho_G^2 / w_tot)
- For ultra-relativistic EOS (p=eps/3): rho_G = 2*eps/c^2, w_tot = 4*eps/(3*c^2)

Observed data (approximate, from literature):
- M87: R_jet ~ 100 pc, knot spacing ~ 0.5-2 kpc, B ~ 10 muG
- 3C 273: R_jet ~ 500 pc, knot spacing ~ 5-20 kpc, B ~ 5 muG
- Cygnus A: R_jet ~ 1 kpc, hotspot-dominated (smooth), B ~ 50 muG
- Centaurus A: R_jet ~ 50 pc, knot spacing ~ 0.5-1 kpc, B ~ 20 muG
- 3C 31: R_jet ~ 200 pc, knot spacing ~ 2-5 kpc, B ~ 3 muG

Plot:
  Left: Observed vs predicted knot spacing (scatter + 1:1 line)
  Right: Knot spacing / R_jet vs H/H_0 with data overlaid
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, G_cgs, pi
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import i0 as I0, i1 as I1, k0 as K0, k1 as K1

setup_style()

# --- Modified Bessel function helpers ---
def dispersion_grav_mag(x, H_ratio):
    """
    Dimensionless dispersion relation from eq. (rel-12-110-17):
    sigma^2 / (4*pi*G*rho_G) = (x*I1(x)/I0(x)) * [K0(x)*I0(x) - 1/2 - H_ratio^2 * x^2*K0(x)/(I0(x)*K1(x))]
    """
    I0x, I1x, K0x, K1x = I0(x), I1(x), K0(x), K1(x)
    grav_term = K0x * I0x - 0.5
    mag_term = H_ratio**2 * x**2 * K0x / (I0x * K1x)
    return (x * I1x / I0x) * (grav_term - mag_term)

def find_critical_x(H_ratio, x_max=1.0668):
    """Find x_a where sigma^2 = 0 (critical wavenumber)."""
    x_arr = np.linspace(0.001, x_max, 10000)
    sigma2 = np.array([dispersion_grav_mag(x, H_ratio) for x in x_arr])
    # Find where sigma2 crosses zero
    crossings = np.where(np.diff(np.sign(sigma2)))[0]
    if len(crossings) > 0:
        return x_arr[crossings[-1]]
    elif sigma2[-1] > 0:
        return x_max  # all unstable up to x_a
    else:
        return 0.01  # strong field: only very long wavelengths unstable

def find_max_instability_x(H_ratio, x_max=1.0668):
    """Find x_max where sigma^2 is maximum."""
    x_arr = np.linspace(0.01, x_max, 5000)
    sigma2 = np.array([dispersion_grav_mag(x, H_ratio) for x in x_arr])
    if np.max(sigma2) > 0:
        idx = np.argmax(sigma2)
        return x_arr[idx]
    return 0.01

# --- AGN jet data ---
# Name: (R_jet [pc], B_field [muG], eps_cgs [erg/cm^3], knot_spacing_obs [kpc], knot_err [kpc])
# eps estimated from synchrotron minimum energy arguments
pc_to_cm = 3.086e18
kpc_to_cm = 3.086e21
muG_to_G = 1e-6

jets = {
    'M87': {
        'R_jet_pc': 100, 'B_muG': 10, 'eps_cgs': 1e-9,
        'knot_kpc': 1.0, 'knot_err': 0.5, 'Gamma': 6,
        'marker': 'o', 'color': COLORS['classical']
    },
    '3C 273': {
        'R_jet_pc': 500, 'B_muG': 5, 'eps_cgs': 5e-10,
        'knot_kpc': 10.0, 'knot_err': 5.0, 'Gamma': 15,
        'marker': 's', 'color': COLORS['relativistic']
    },
    'Cygnus A': {
        'R_jet_pc': 1000, 'B_muG': 50, 'eps_cgs': 2e-9,
        'knot_kpc': 50.0, 'knot_err': 20.0, 'Gamma': 3,
        'marker': 'D', 'color': COLORS['bdnk']
    },
    'Centaurus A': {
        'R_jet_pc': 50, 'B_muG': 20, 'eps_cgs': 5e-9,
        'knot_kpc': 0.5, 'knot_err': 0.2, 'Gamma': 3,
        'marker': '^', 'color': COLORS['is']
    },
    '3C 31': {
        'R_jet_pc': 200, 'B_muG': 3, 'eps_cgs': 3e-10,
        'knot_kpc': 3.0, 'knot_err': 1.5, 'Gamma': 2,
        'marker': 'v', 'color': COLORS['data']
    },
}

# --- Compute predicted knot spacings ---
predicted_kpc = {}
H_over_H0_vals = {}

for name, d in jets.items():
    R_jet = d['R_jet_pc'] * pc_to_cm
    B = d['B_muG'] * muG_to_G
    H = B  # Gaussian units: H = B for vacuum permeability mu=1
    eps = d['eps_cgs']

    # Ultra-relativistic EOS: p = eps/3
    p = eps / 3.0
    rho_G = (eps + 3 * p) / c_cgs**2  # = 2*eps/c^2
    w_tot = (eps + p + H**2 / (4 * pi)) / c_cgs**2  # ~ 4*eps/(3*c^2)

    # Critical field H_0,rel
    H0_rel = 4 * pi * R_jet * c_cgs * np.sqrt(G_cgs * rho_G**2 / w_tot)

    H_ratio = H / H0_rel
    H_over_H0_vals[name] = H_ratio

    # Find most unstable wavenumber
    x_m = find_max_instability_x(H_ratio)

    # Predicted knot spacing (fragmentation wavelength)
    lambda_pred = 2 * pi * R_jet / x_m
    predicted_kpc[name] = lambda_pred / kpc_to_cm

# --- Plotting ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# Left panel: Observed vs predicted knot spacing
obs_vals = []
pred_vals = []
err_vals = []

for name, d in jets.items():
    obs = d['knot_kpc']
    pred = predicted_kpc[name]
    err = d['knot_err']

    ax1.errorbar(pred, obs, yerr=err, fmt=d['marker'], ms=12,
                 color=d['color'], markeredgecolor='black', markeredgewidth=0.8,
                 capsize=4, elinewidth=1.5, zorder=5,
                 label=f"{name} ($\\Gamma={d['Gamma']}$)")
    obs_vals.append(obs)
    pred_vals.append(pred)
    err_vals.append(err)

# 1:1 line
lims = [0.05, 200]
ax1.plot(lims, lims, 'k--', lw=1.5, alpha=0.5, label='1:1 correspondence')
ax1.fill_between(lims, [l * 0.3 for l in lims], [l * 3 for l in lims],
                  alpha=0.08, color='gray')
ax1.annotate('Factor of 3', xy=(1, 0.4), fontsize=9, color='gray', style='italic')

ax1.set_xlabel('Predicted knot spacing [kpc]')
ax1.set_ylabel('Observed knot spacing [kpc]')
ax1.set_title('Magnetic stabilization: observed vs. predicted knot spacing')
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_xlim(0.05, 200)
ax1.set_ylim(0.05, 200)
ax1.set_aspect('equal')
ax1.legend(loc='upper left', fontsize=9)

# Right panel: lambda_knot / R_jet vs H/H_0
H_ratio_arr = np.linspace(0.01, 5.0, 200)
lambda_over_R = np.zeros_like(H_ratio_arr)

for i, hr in enumerate(H_ratio_arr):
    x_m = find_max_instability_x(hr)
    lambda_over_R[i] = 2 * pi / x_m

ax2.semilogy(H_ratio_arr, lambda_over_R, '-', lw=2.5, color=COLORS['relativistic'],
             label=r'$\lambda_{\rm knot}/R_{\rm jet}$ (theory)')

# Overlay data points
for name, d in jets.items():
    hr = H_over_H0_vals[name]
    obs_ratio = d['knot_kpc'] * kpc_to_cm / (d['R_jet_pc'] * pc_to_cm)
    err_ratio = d['knot_err'] * kpc_to_cm / (d['R_jet_pc'] * pc_to_cm)

    ax2.errorbar(hr, obs_ratio, yerr=err_ratio, fmt=d['marker'], ms=12,
                 color=d['color'], markeredgecolor='black', markeredgewidth=0.8,
                 capsize=4, elinewidth=1.5, zorder=5, label=name)

# Reference: Newtonian (H=0) value
ax2.axhline(2 * pi / 0.580, ls=':', color='gray', alpha=0.5, lw=1.0)
ax2.annotate(r'Newtonian ($H=0$): $\lambda/R = 2\pi/x_{\max}^{\rm N} \approx 10.8$',
             xy=(0.1, 2 * pi / 0.580 * 1.1), fontsize=9, color='gray')

# Label regimes
ax2.annotate('Weak field\n(knotty jets)', xy=(0.3, 15), fontsize=10,
             color=COLORS['classical'])
ax2.annotate('Strong field\n(smooth jets)', xy=(3, 500), fontsize=10,
             color=COLORS['relativistic'])

ax2.set_xlabel(r'Field strength ratio $H / H_{0,\rm rel}$')
ax2.set_ylabel(r'$\lambda_{\rm knot} / R_{\rm jet}$')
ax2.set_title('Knot spacing vs. magnetic field strength')
ax2.set_xlim(0, 5)
ax2.set_ylim(5, 5000)
ax2.legend(loc='upper left', fontsize=9, ncol=2)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_knot_spacing_data.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_knot_spacing_data.png')
print("Saved fig_knot_spacing_data.pdf/png")
