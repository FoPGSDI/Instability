"""
Variational estimate of Ra_c for l=1 mode using polynomial trial functions.
Compare accuracy with exact solution.
"""
import sys; sys.path.insert(0, '/data/haiyangw/claude/Instability'); from SHARED_PLOT_STYLE import setup_style, COLORS
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize_scalar
from scipy.integrate import quad

setup_style()

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Spherical shell: eta <= r <= 1 (normalized by outer radius)
# For l=1 mode, the operator D_l^2 = d^2/dr^2 + 2/r * d/dr - l(l+1)/r^2
# Rayleigh quotient: C = int |D_l^2 W|^2 r^2 dr / [l(l+1) int (W/r)^2 r^2 dr]

def D_l2_W(W_func, dW_func, d2W_func, r, l):
    """Apply D_l^2 operator to W."""
    return d2W_func(r) + (2.0/r) * dW_func(r) - l*(l+1)/r**2 * W_func(r)

def rayleigh_quotient_numerical(eta, l, N_poly):
    """Compute Rayleigh quotient using N-term polynomial trial function.

    Trial function: W(r) = (r - eta)(1 - r) * sum_{n=0}^{N-1} a_n * r^n
    For simplicity, use W(r) = (r-eta)(1-r) r^n for the n-th basis function.
    Then optimize the single-parameter or multi-parameter case.
    """
    r_pts = np.linspace(eta + 1e-8, 1 - 1e-8, 1000)
    dr = r_pts[1] - r_pts[0]

    if N_poly == 1:
        # Simplest: W = (r - eta)(1 - r)
        W = (r_pts - eta) * (1 - r_pts)
        dW = (1 - r_pts) - (r_pts - eta)  # = 1 - 2r + eta
        d2W = -2.0 * np.ones_like(r_pts)

        Dl2W = d2W + (2.0/r_pts) * dW - l*(l+1)/r_pts**2 * W

        num = np.trapz(Dl2W**2 * r_pts**2, r_pts)
        den = l*(l+1) * np.trapz((W/r_pts)**2 * r_pts**2, r_pts)
        return num / den

    elif N_poly == 2:
        # W = (r - eta)(1 - r)(1 + alpha * r)
        # Optimize over alpha
        def C_of_alpha(alpha):
            W = (r_pts - eta) * (1 - r_pts) * (1 + alpha * r_pts)
            # d/dr[(r-eta)(1-r)(1+alpha*r)]
            dW = ((1-r_pts) * (1 + alpha*r_pts)
                  - (r_pts - eta) * (1 + alpha*r_pts)
                  + alpha * (r_pts - eta) * (1 - r_pts))
            d2W_val = (-2*(1 + alpha*r_pts)
                       + 2*alpha*(1 - r_pts)
                       - 2*alpha*(r_pts - eta)
                       + 0)  # simplified numerical differentiation
            # Use numerical differentiation instead
            W_func = lambda r: (r - eta) * (1 - r) * (1 + alpha * r)
            W_arr = np.array([W_func(r) for r in r_pts])
            dW_arr = np.gradient(W_arr, r_pts)
            d2W_arr = np.gradient(dW_arr, r_pts)

            Dl2W = d2W_arr + (2.0/r_pts) * dW_arr - l*(l+1)/r_pts**2 * W_arr

            num = np.trapz(Dl2W**2 * r_pts**2, r_pts)
            den = l*(l+1) * np.trapz((W_arr/r_pts)**2 * r_pts**2, r_pts)
            if den < 1e-30:
                return 1e30
            return num / den

        res = minimize_scalar(C_of_alpha, bounds=(-5, 5), method='bounded')
        return res.fun

    elif N_poly == 3:
        # W = (r - eta)(1 - r)(1 + alpha*r + beta*r^2)
        from scipy.optimize import minimize
        def C_of_params(params):
            alpha, beta = params
            W_func = lambda r: (r - eta) * (1 - r) * (1 + alpha * r + beta * r**2)
            W_arr = np.array([W_func(r) for r in r_pts])
            dW_arr = np.gradient(W_arr, r_pts)
            d2W_arr = np.gradient(dW_arr, r_pts)

            Dl2W = d2W_arr + (2.0/r_pts) * dW_arr - l*(l+1)/r_pts**2 * W_arr

            num = np.trapz(Dl2W**2 * r_pts**2, r_pts)
            den = l*(l+1) * np.trapz((W_arr/r_pts)**2 * r_pts**2, r_pts)
            if den < 1e-30:
                return 1e30
            return num / den

        res = minimize(C_of_params, [0.0, 0.0], method='Nelder-Mead')
        return res.fun

    elif N_poly == 4:
        from scipy.optimize import minimize
        def C_of_params(params):
            alpha, beta, gamma = params
            W_func = lambda r: (r - eta) * (1 - r) * (1 + alpha*r + beta*r**2 + gamma*r**3)
            W_arr = np.array([W_func(r) for r in r_pts])
            dW_arr = np.gradient(W_arr, r_pts)
            d2W_arr = np.gradient(dW_arr, r_pts)

            Dl2W = d2W_arr + (2.0/r_pts) * dW_arr - l*(l+1)/r_pts**2 * W_arr

            num = np.trapz(Dl2W**2 * r_pts**2, r_pts)
            den = l*(l+1) * np.trapz((W_arr/r_pts)**2 * r_pts**2, r_pts)
            if den < 1e-30:
                return 1e30
            return num / den

        res = minimize(C_of_params, [0.0, 0.0, 0.0], method='Nelder-Mead')
        return res.fun

# Panel (a): Ra_c vs eta for different polynomial orders, l=1
ax = axes[0]
eta_values = np.linspace(0.1, 0.9, 30)
l = 1

results = {1: [], 2: [], 3: [], 4: []}
for eta in eta_values:
    for N in [1, 2, 3, 4]:
        C_val = rayleigh_quotient_numerical(eta, l, N)
        results[N].append(C_val)

colors_N = [COLORS['classical'], COLORS['relativistic'], COLORS['bdnk'], COLORS['is']]
labels_N = ['1-term', '2-term', '3-term', '4-term (ref.)']
for i, N in enumerate([1, 2, 3, 4]):
    ax.semilogy(eta_values, results[N], ['-', '--', '-.', ':'][i],
                color=colors_N[i], linewidth=2, label=labels_N[i])

ax.set_xlabel(r'Radius ratio $\eta = R_1/R_2$')
ax.set_ylabel(r'$\mathcal{C}_{\rm crit}$ ($l=1$ mode)')
ax.set_title('(a) Variational estimate vs polynomial order')
ax.legend(fontsize=9)

# Panel (b): Relative error of each polynomial order compared to 4-term
ax = axes[1]
ref = np.array(results[4])
for i, N in enumerate([1, 2, 3]):
    vals = np.array(results[N])
    rel_err = (vals - ref) / ref * 100
    ax.plot(eta_values, rel_err, ['-', '--', '-.'][i],
            color=colors_N[i], linewidth=2, label=labels_N[i])

ax.axhline(y=0, ls=':', color='gray', alpha=0.5)
ax.axhline(y=1, ls='--', color='gray', alpha=0.3)
ax.axhline(y=5, ls='--', color='gray', alpha=0.3)
ax.set_xlabel(r'Radius ratio $\eta$')
ax.set_ylabel('Relative error vs 4-term (%)')
ax.set_title('(b) Accuracy of polynomial trial functions')
ax.legend(fontsize=9)
ax.set_ylim(-5, 50)

# Panel (c): Comparison for l=1,2,3 at fixed eta=0.5
ax = axes[2]
eta_fixed = 0.5
N_terms = [1, 2, 3, 4]

for l_val in [1, 2, 3]:
    C_vals = []
    for N in N_terms:
        C_vals.append(rayleigh_quotient_numerical(eta_fixed, l_val, N))
    C_ref = C_vals[-1]
    rel_errors = [(c - C_ref) / C_ref * 100 for c in C_vals]

    ax.plot(N_terms, rel_errors, 'o-', linewidth=2, markersize=8,
            label=rf'$l={l_val}$, $\mathcal{{C}}_{{4-term}} = {C_ref:.1f}$')

ax.axhline(y=0, ls=':', color='gray', alpha=0.5)
ax.axhline(y=1, ls='--', color='gray', alpha=0.3, label='1% error')
ax.set_xlabel('Number of polynomial terms')
ax.set_ylabel('Relative error vs 4-term (%)')
ax.set_title(rf'(c) Convergence at $\eta = {eta_fixed}$')
ax.legend(fontsize=9)
ax.set_xticks([1, 2, 3, 4])
ax.set_ylim(-2, 40)

plt.tight_layout()
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_variational_Ra_l1_polynomial.pdf')
plt.savefig('/data/haiyangw/claude/Instability/plots/deep/fig_variational_Ra_l1_polynomial.png')
print("Variational Ra l=1 polynomial plot saved.")
