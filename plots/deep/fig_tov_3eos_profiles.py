#!/usr/bin/env python3
"""
Deep Research Agent 3 -- TOV profile comparison for 3 realistic NS EOSs.

Solves the TOV equations numerically using polytropic approximations to
3 nuclear EOSs (APR, SLy, BSk21) and plots:
  - epsilon(r) / epsilon_c  (energy density profile)
  - p(r) / p_c  (pressure profile)
  - xi(r) = p(r) / (epsilon(r) c^2)  (pressure-to-energy ratio)

Uses a simple polytropic EOS: p = K * rho^Gamma, with
  epsilon = rho * c^2 + p / (Gamma - 1)  (including internal energy).

References:
  - Akmal, Pandharipande, Ravenhall (1998), APR EOS
  - Douchin & Haensel (2001), SLy EOS
  - Potekhin et al. (2013), BSk21 EOS
  - Oppenheimer & Volkoff (1939), Tolman (1939)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SHARED_PLOT_STYLE import setup_style, COLORS, G_cgs, c_cgs, M_sun
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

setup_style()

G = G_cgs
c = c_cgs
km = 1e5  # cm

# --- Polytropic EOS: p = K rho^Gamma ---
# epsilon = rho c^2 + p/(Gamma-1) = rho c^2 (1 + K rho^{Gamma-1} / ((Gamma-1) c^2))
# We calibrate K so that at nuclear saturation density rho_0 = 2.8e14 g/cm^3
# the pressure matches the EOS.

# Calibrated polytropic parameters (Read et al. 2009 style)
# These produce realistic NS models:
eos_models = {
    'APR': {
        'Gamma': 2.58,
        'rho_c': 1.5e15,   # central rest-mass density for ~1.4 Msun
        'K_factor': 1.0,
        'p_nuc': 3.5e33,    # pressure at rho_0 in dyne/cm^2
        'color': '#F44336', 'ls': '-',
        'label': r'APR ($1.4\,M_\odot$)',
    },
    'SLy': {
        'Gamma': 2.35,
        'rho_c': 3.0e15,
        'K_factor': 1.0,
        'p_nuc': 2.5e33,
        'color': '#2196F3', 'ls': '--',
        'label': r'SLy ($1.4\,M_\odot$)',
    },
    'BSk21': {
        'Gamma': 2.60,
        'rho_c': 2.5e15,   # for ~2.0 Msun
        'K_factor': 1.0,
        'p_nuc': 3.0e33,
        'color': '#4CAF50', 'ls': '-.',
        'label': r'BSk21 ($2.0\,M_\odot$)',
    },
}

rho_0 = 2.8e14  # nuclear saturation density g/cm^3

# Calibrate K for each EOS
for name, params in eos_models.items():
    # p = K rho^Gamma => K = p_nuc / rho_0^Gamma
    params['K'] = params['p_nuc'] / rho_0**params['Gamma']


def solve_tov(rho_c, K, Gamma, r_max=20.0 * km, N=10000):
    """Solve TOV equations for a polytropic EOS p = K rho^Gamma.

    All quantities in CGS.
    Returns r, epsilon, p, m arrays (CGS).
    """
    def pressure(rho):
        return K * rho**Gamma

    def energy_density(rho):
        """epsilon = rho c^2 + p/(Gamma-1) for polytrope with internal energy."""
        p = pressure(rho)
        return rho * c**2 + p / (Gamma - 1.0)

    def rho_from_p(p_val):
        if p_val <= 0:
            return 0.0
        return (p_val / K)**(1.0 / Gamma)

    p_c = pressure(rho_c)
    eps_c = energy_density(rho_c)

    def tov_rhs(r, y):
        m_enc, p_val = y
        if p_val <= 1e10 or r <= 0:  # pressure floor
            return [0.0, 0.0]
        rho = rho_from_p(p_val)
        if rho <= 0:
            return [0.0, 0.0]
        eps = energy_density(rho)

        # dm/dr = 4 pi r^2 epsilon / c^2
        dmdr = 4.0 * np.pi * r**2 * eps / c**2

        # TOV: dp/dr = -G(eps/c^2 + p/c^4)(m + 4pi r^3 p/c^2) / (r(r - 2Gm/c^2))
        factor1 = eps / c**2 + p_val / c**4
        factor2 = m_enc + 4.0 * np.pi * r**3 * p_val / c**2
        factor3 = r * (r - 2.0 * G * m_enc / c**2)
        if factor3 <= 0:
            return [0.0, 0.0]
        dpdr = -G * factor1 * factor2 / factor3

        return [dmdr, dpdr]

    def surface_event(r, y):
        return y[1] - 1e10  # stop when p drops to floor

    surface_event.terminal = True
    surface_event.direction = -1

    r_start = 100.0  # 1 m
    m_start = 4.0 / 3.0 * np.pi * r_start**3 * eps_c / c**2
    p_start = p_c

    sol = solve_ivp(tov_rhs, (r_start, r_max), [m_start, p_start],
                    method='RK45', events=surface_event,
                    max_step=r_max / N, rtol=1e-10, atol=1e-15)

    r_arr = sol.t
    m_arr = sol.y[0]
    p_arr = sol.y[1]

    # Compute derived quantities
    rho_arr = np.array([rho_from_p(p) for p in p_arr])
    eps_arr = np.array([energy_density(rho) for rho in rho_arr])
    xi_arr = np.where(eps_arr > 0, p_arr / eps_arr, 0.0)

    return r_arr, eps_arr, p_arr, m_arr, xi_arr


# --- Solve for each EOS ---
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

results = {}
for name, params in eos_models.items():
    r, eps, p, m, xi = solve_tov(params['rho_c'], params['K'], params['Gamma'])
    R_star = r[-1]
    M_star = m[-1]
    C_star = G * M_star / (R_star * c**2)

    results[name] = {
        'r_norm': r / R_star,
        'eps_norm': eps / eps[0],
        'p_norm': p / p[0],
        'xi': xi,
        'R_km': R_star / km,
        'M_Msun': M_star / M_sun,
        'C': C_star,
    }

    print(f'{name}: R = {R_star/km:.2f} km, M = {M_star/M_sun:.3f} Msun, '
          f'C = {C_star:.4f}, xi_c = {xi[0]:.4f}')

    full_label = (f'{name} '
                  rf'($R={R_star/km:.1f}$ km, $\mathcal{{C}}={C_star:.3f}$)')

    # Panel 1: epsilon(r)/epsilon_c
    axes[0].plot(results[name]['r_norm'], results[name]['eps_norm'],
                 params['ls'], color=params['color'], linewidth=2.0,
                 label=name)

    # Panel 2: p(r)/p_c
    axes[1].plot(results[name]['r_norm'], results[name]['p_norm'],
                 params['ls'], color=params['color'], linewidth=2.0,
                 label=name)

    # Panel 3: xi(r) = p/(eps c^2) -- note xi already = p/eps which is p/(rho c^2 + ...)
    axes[2].plot(results[name]['r_norm'], results[name]['xi'],
                 params['ls'], color=params['color'], linewidth=2.0,
                 label=full_label)

# --- Schwarzschild interior comparison (uniform density) ---
r_frac = np.linspace(0.01, 1.0, 300)
for C_ref, clr, lbl in [(0.18, '#999999', r'Uniform, $\mathcal{C}=0.18$'),
                          (0.27, '#666666', r'Uniform, $\mathcal{C}=0.27$')]:
    sq_r = np.sqrt(1.0 - 2.0 * C_ref * r_frac**2)
    sq_R = np.sqrt(1.0 - 2.0 * C_ref)
    p_over_eps = (sq_r - sq_R) / (3.0 * sq_R - sq_r)
    # For uniform density: eps = const => eps_norm = 1
    # p_norm = p(r)/p(0) = p_over_eps(r) / p_over_eps(0)
    p_over_eps_0 = (1.0 - sq_R) / (3.0 * sq_R - 1.0)
    p_norm_schwarz = p_over_eps / p_over_eps_0

    axes[1].plot(r_frac, p_norm_schwarz, ':', color=clr, linewidth=1.0,
                 label=lbl)
    # xi for Schwarzschild interior
    xi_schwarz = p_over_eps / (1.0 + p_over_eps)
    axes[2].plot(r_frac, xi_schwarz, ':', color=clr, linewidth=1.0,
                 label=lbl)

# --- Panel formatting ---
axes[0].set_xlabel(r'$r/R$')
axes[0].set_ylabel(r'$\varepsilon(r) / \varepsilon_c$')
axes[0].set_title(r'Energy density profile')
axes[0].legend(fontsize=9)
axes[0].set_xlim(0, 1.05)
axes[0].set_ylim(0, 1.05)

axes[1].set_xlabel(r'$r/R$')
axes[1].set_ylabel(r'$p(r) / p_c$')
axes[1].set_title(r'Pressure profile')
axes[1].legend(fontsize=8)
axes[1].set_xlim(0, 1.05)
axes[1].set_ylim(0, 1.05)

axes[2].set_xlabel(r'$r/R$')
axes[2].set_ylabel(r'$\xi(r) = p(r) / \varepsilon(r)$')
axes[2].set_title(r'Pressure-to-energy ratio $\xi(r)$')
axes[2].legend(fontsize=6.5, loc='upper right')
axes[2].set_xlim(0, 1.05)

fig.suptitle('TOV profiles for 3 nuclear EOSs', fontsize=14, y=1.02)
fig.tight_layout()
outdir = os.path.dirname(__file__)
fig.savefig(os.path.join(outdir, 'fig_tov_3eos_profiles.pdf'))
fig.savefig(os.path.join(outdir, 'fig_tov_3eos_profiles.png'))
print('\nSaved plots/deep/fig_tov_3eos_profiles.pdf and .png')
plt.close(fig)
