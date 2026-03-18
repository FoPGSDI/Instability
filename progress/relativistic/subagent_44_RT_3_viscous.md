---
agent: 44
chapter: 10
section: 94
task: Relativistic viscous Rayleigh--Taylor instability
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_10_sec94.tex`, which
extends Chandrasekhar's §94 (two uniform viscous fluids separated by a
horizontal boundary, Rayleigh--Taylor problem) to the special-relativistic
regime using Israel--Stewart causal dissipation.

## Content

1. **Israel--Stewart viscous perturbation equations**: frequency-dependent
   effective viscosity eta_eff = eta/(1 + tau_pi n) replaces constant eta.

2. **Relativistic dispersion in each uniform region**: q_rel^2 = k^2 +
   n(1 + tau_pi n)/nu generalises q^2 = k^2 + n/nu.

3. **nu_1 = nu_2 case**: The quartic characteristic equation (10-121) is
   structurally preserved, but alpha_i become enthalpy fractions
   w_i/(w_1+w_2) and the growth rate n is obtained from a quadratic
   involving tau_pi.

4. **Maximum instability modes**: k_max shifts to smaller k, n_max is
   reduced by O(tau_pi (g^2/nu)^{1/3}) corrections.

5. **Surface tension**: Relativistic surface energy density T_rel =
   T(1 + T/(2 Sigma c^2)) lowers the critical wavenumber k_c slightly.

6. **Gravity waves**: omega^2 = gk (rho/w) with w = (epsilon+p)/c^2;
   ultra-relativistic limit gives omega^2 = (3/4)gk.

7. **Causality**: Israel--Stewart viscous signal speed v_visc =
   sqrt(nu/tau_pi) is finite and bounded by c when tau_pi >= nu/c^2.
   The Navier--Stokes acausality is fully cured.

8. **Non-relativistic limit**: All results reduce to Chandrasekhar's
   classical §94 as c -> infinity, tau_pi -> 0.

## Conventions

- Metric: (-,+,+,+), c explicit
- Enthalpy density: w = (epsilon+p)/c^2 replaces rho
- Israel--Stewart relaxation: tau_pi > 0 for causality
- All macros from rel_preamble.tex used consistently

## Files

- `output/chapters/relativistic/rel_chapter_10_sec94.tex`
- `progress/relativistic/subagent_44_RT_3_viscous.md` (this file)
