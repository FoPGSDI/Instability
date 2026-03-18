"""
Relativistic Dean number vs mass transfer rate for accretion streams
in X-ray binaries.

Models the accretion stream from the L1 point in a close binary system,
computing the relativistic Dean number De_rel for realistic stream
parameters as a function of mass transfer rate.

References:
  - Frank, King & Raine (2002), Accretion Power in Astrophysics
  - Lubow (1989), ApJ 340, 1064
  - Balbus (2003), ARAA 41, 555
"""
import sys
sys.path.insert(0, '/data/haiyangw/claude/Instability')
from SHARED_PLOT_STYLE import setup_style, COLORS, c_cgs, G_cgs, M_sun, R_sun, pi, k_B, m_p
import numpy as np
import matplotlib.pyplot as plt

setup_style()

# === Binary system parameters ===
# X-ray binary: compact object + donor star
# Compact object masses
M_ns = 1.4 * M_sun   # neutron star
M_bh = 10.0 * M_sun  # stellar-mass black hole

# Donor star mass (typical low-mass X-ray binary)
M_donor = 0.5 * M_sun

# Binary separation (from Kepler's law for P_orb)
# For typical LMXB with P_orb ~ 5 hours
P_orb = 5.0 * 3600  # s

def binary_separation(M1, M2, P):
    """Binary separation from Kepler's third law."""
    return (G_cgs * (M1 + M2) * P**2 / (4.0 * pi**2))**(1.0/3.0)

def roche_lobe_radius(q):
    """Eggleton's formula for Roche lobe radius (donor) / separation.
    q = M_donor / M_accretor."""
    return 0.49 * q**(2.0/3.0) / (0.6 * q**(2.0/3.0) + np.log(1 + q**(1.0/3.0)))

def stream_properties(Mdot, M_acc, M_don, P_orb_val):
    """
    Compute accretion stream properties at the point of maximum curvature
    (roughly where stream impacts the accretion disk).

    Returns: V_stream, R_curv, rho_stream, H_stream, T_stream
    """
    a_bin = binary_separation(M_acc, M_don, P_orb_val)
    q = M_don / M_acc
    R_L1 = roche_lobe_radius(q) * a_bin

    # Stream velocity at L1: roughly the sound speed of the donor photosphere
    # T_photosphere ~ 4000-6000 K for low-mass donors
    T_phot = 5000.0  # K
    c_s_L1 = np.sqrt(k_B * T_phot / m_p)

    # Stream accelerates due to gravity of the accretor
    # At the circularization radius r_circ ~ 0.1 * a_bin:
    r_circ = 0.1 * a_bin
    V_stream = np.sqrt(2.0 * G_cgs * M_acc / r_circ)
    V_stream = np.minimum(V_stream, 0.5 * c_cgs)  # cap at 0.5c

    # Stream cross-section at circularization
    # Width ~ H ~ (Mdot / (rho * V_stream))^{1/2}
    # Temperature in stream: shock-heated to ~ virial
    T_stream = G_cgs * M_acc * m_p / (k_B * r_circ)
    T_stream = np.minimum(T_stream, 1e11)  # cap

    c_s_stream = np.sqrt(k_B * T_stream / m_p)

    # Stream density
    H_stream = c_s_stream / np.sqrt(G_cgs * M_acc / r_circ**3)
    rho_stream = Mdot / (pi * H_stream**2 * V_stream)

    # Radius of curvature of the stream trajectory
    # Approximately the circularization radius
    R_curv = r_circ

    return V_stream, R_curv, rho_stream, H_stream, T_stream


def dean_number_rel(V, R_curv, H, rho, T, nu_val=None):
    """
    Compute the relativistic Dean number:
      De_rel = Re^2 * (H / R_curv) * [1 + 5/2 * V^2/c^2]

    where Re = V * H / nu is the Reynolds number.
    """
    # Kinematic viscosity estimate
    # For ionized plasma: nu ~ (k_B*T)^{5/2} / (rho * e^4 * ln_Lambda * m_e^{1/2})
    # Use Spitzer formula approximately:
    if nu_val is None:
        ln_Lambda = 20.0
        # Simplified: nu ~ 10^{-2} * T^{5/2} / (rho * ln_Lambda) for hydrogen plasma
        # More precisely: nu_Spitzer ~ 2.2e5 * T^{5/2} / (rho * ln_Lambda) cm^2/s
        nu_val = 2.2e5 * T**2.5 / (np.maximum(rho, 1e-30) * ln_Lambda)
        nu_val = np.maximum(nu_val, 1.0)  # floor

    Re = V * H / nu_val

    # Classical Dean number
    De_classical = Re**2 * (H / R_curv)

    # Relativistic correction
    gamma_factor = 1.0 + 2.5 * (V / c_cgs)**2

    De_rel = De_classical * gamma_factor

    return De_classical, De_rel, Re


# === Compute Dean number vs mass transfer rate ===
Mdot_range = np.logspace(-12, -6, 200) * M_sun / (365.25 * 86400)  # g/s
Mdot_Msun_yr = Mdot_range / (M_sun / (365.25 * 86400))

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# === Left panel: De_rel vs Mdot for NS and BH accretors ===
ax1 = axes[0]

systems = [
    (M_ns, M_donor, 'NS binary', COLORS['neutron_star'], '-'),
    (M_bh, M_donor, 'BH binary (10 M$_\\odot$)', COLORS['accretion'], '--'),
]

for M_acc, M_don, label, color, ls in systems:
    De_cl_arr = np.zeros_like(Mdot_range)
    De_rel_arr = np.zeros_like(Mdot_range)
    Re_arr = np.zeros_like(Mdot_range)

    for idx, Mdot in enumerate(Mdot_range):
        V, R_c, rho, H, T = stream_properties(Mdot, M_acc, M_don, P_orb)
        De_cl, De_rel, Re = dean_number_rel(V, R_c, H, rho, T)
        De_cl_arr[idx] = De_cl
        De_rel_arr[idx] = De_rel
        Re_arr[idx] = Re

    ax1.loglog(Mdot_Msun_yr, De_rel_arr, color=color, lw=2, ls=ls,
               label=label + ' (rel.)')
    ax1.loglog(Mdot_Msun_yr, De_cl_arr, color=color, lw=1.5, ls=':',
               alpha=0.6, label=label + ' (class.)')

# Mark critical Dean number (De_crit ~ 92975)
De_crit = 92975
ax1.axhline(y=De_crit, color='gray', ls='--', lw=1.2, alpha=0.7)
ax1.text(3e-11, De_crit * 1.5, r'$De_{c} = 92{,}975$', fontsize=9, color='gray')

# Typical mass transfer rates
ax1.axvspan(1e-10, 1e-8, alpha=0.06, color='blue', label='Typical LMXB range')

ax1.set_xlabel(r'$\dot{M}$ [M$_\odot$ yr$^{-1}$]')
ax1.set_ylabel(r'Dean number $De$')
ax1.set_title('Dean instability in binary accretion streams')
ax1.legend(loc='upper left', fontsize=8.5)
ax1.set_xlim(1e-12, 1e-6)
ax1.set_ylim(1e0, 1e15)

# === Right panel: V/c and relativistic correction vs Mdot ===
ax2 = axes[1]

for M_acc, M_don, label, color, ls in systems:
    V_arr = np.zeros_like(Mdot_range)
    corr_arr = np.zeros_like(Mdot_range)

    for idx, Mdot in enumerate(Mdot_range):
        V, R_c, rho, H, T = stream_properties(Mdot, M_acc, M_don, P_orb)
        V_arr[idx] = V / c_cgs
        corr_arr[idx] = 2.5 * (V / c_cgs)**2

    ax2.semilogx(Mdot_Msun_yr, V_arr, color=color, lw=2, ls=ls,
                 label=label + r', $V/c$')

ax2_twin = ax2.twinx()
for M_acc, M_don, label, color, ls in systems:
    V_arr = np.zeros_like(Mdot_range)
    corr_arr = np.zeros_like(Mdot_range)

    for idx, Mdot in enumerate(Mdot_range):
        V, R_c, rho, H, T = stream_properties(Mdot, M_acc, M_don, P_orb)
        corr_arr[idx] = 2.5 * (V / c_cgs)**2 * 100  # percent

    ax2_twin.semilogx(Mdot_Msun_yr, corr_arr, color=color, lw=1.5,
                      ls='-.', alpha=0.6)

ax2.set_xlabel(r'$\dot{M}$ [M$_\odot$ yr$^{-1}$]')
ax2.set_ylabel(r'$V_{\rm stream}\,/\,c$')
ax2_twin.set_ylabel(r'Relativistic correction (\%)')
ax2.set_title('Stream velocity and relativistic correction')
ax2.legend(loc='upper left', fontsize=10)
ax2.set_xlim(1e-12, 1e-6)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_dean_binary_stream.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_dean_binary_stream.png')
print("Saved fig_dean_binary_stream.pdf and .png")
