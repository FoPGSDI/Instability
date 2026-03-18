---
agent: 47
chapter: 10
sections: 98-99
task: Relativistic globe+drop oscillations
status: completed
timestamp: 2026-03-18T12:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_10_sec98-99.tex` extending
Chandrasekhar's analysis of viscous liquid globe oscillations (§98) and
viscous liquid drop oscillations (§99) to the relativistic regime.

### Key modifications from classical to relativistic:

1. **Equilibrium structure**: Newtonian hydrostatic balance replaced by the
   Tolman-Oppenheimer-Volkoff (TOV) equation; interior Schwarzschild solution
   used for the unperturbed uniform-density sphere. Compactness parameter
   C = GM/(Rc^2) controls relativistic corrections.

2. **Inertial density**: Rest-mass density rho replaced by relativistic
   enthalpy density w/c^2 = (epsilon + p)/c^2 in all dynamical equations.

3. **Israel-Stewart causal viscosity**: Navier-Stokes instantaneous viscous
   stress replaced by Israel-Stewart relaxation equation with shear relaxation
   time tau_pi > 0. Effective viscosity nu_eff = nu/(1 - tau_pi sigma).

4. **Kelvin frequencies**: Relativistic correction beta_l * C derived for the
   inviscid eigenfrequencies of the globe (eq rel-10-258R).

5. **Characteristic equation**: Same functional form as classical (eq 280 of §98)
   but with z_rel = R sqrt(sigma(1 - tau_pi sigma)/nu) replacing z, and
   sigma_{Kl,rel} replacing sigma_{Kl}.

6. **Damping rates**: Leading-order Israel-Stewart correction to Kelvin mode
   decay time derived (eq rel-10-291R). Higher-order modes saturate at
   sigma_max = 1/tau_pi, ensuring causality.

7. **Drop oscillations (§99)**: Surface tension promoted to relativistic
   surface energy via Israel junction conditions. Chandrasekhar-Reid identity
   (globe and drop share same characteristic equation) shown to persist in
   the relativistic theory.

8. **Causality verification**: Two causalitycheck boxes verify that shear
   propagation speed <= c and that higher-order damping rates are bounded.

9. **Non-relativistic limit**: All results reduce to Chandrasekhar's classical
   expressions when C -> 0 and tau_pi -> 0.

## Files created

- `output/chapters/relativistic/rel_chapter_10_sec98-99.tex`
- `progress/relativistic/subagent_47_RT_6_globe.md` (this file)

## Issues / Notes

- The relativistic correction coefficient beta_l (eq rel-10-beta) combines
  three separate physical effects (TOV pressure, metric matching, enthalpy
  inertia). The individual contributions could be disentangled but are
  presented as a single coefficient for compactness.
- Bulk viscosity (zeta) is not included; for incompressible perturbations
  div u = 0, bulk viscosity does not contribute.
- The surface energy density epsilon_S in the drop problem is a free parameter;
  for quark-gluon plasma applications epsilon_S ~ T is typical.
