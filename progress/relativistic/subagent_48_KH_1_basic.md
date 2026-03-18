---
agent: 48
chapter: 11
sections: 100-101
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created relativistic generalization of Chapter XI sections 100-101
(Kelvin-Helmholtz perturbation equations and two uniform fluids).

File: `output/chapters/relativistic/rel_chapter_11_sec100-101.tex`

### Section 100 (Relativistic perturbation equations)
- Lorentz boost kinematics between two-fluid frames
- Relativistic velocity addition for shear flow (V_rel formula)
- Equilibrium energy-momentum tensor with enthalpy density w = epsilon + p
- Key substitution: rho -> rho_hat = (epsilon + p)/c^2
- Linearized perturbation equations with gamma^2 factors for longitudinal inertia
- Reduction to single ODE and interface jump condition

### Section 101 (Two uniform fluids — relativistic)
- Relativistic dispersion relation (eq. rel-11-18)
- Without surface tension: critical velocity with Lorentz-factor weighting
- Classical limit recovered: V_crit^2 ~ g(rho_1^2 - rho_2^2)/(rho_1 rho_2 k)
- With surface tension: stabilization criterion (eq. rel-11-29)
- Relativistic Doppler and aberration effects on growth rates
- Causality checks: streaming velocities, relative velocity, phase/group velocities all < c
- Non-relativistic limit verified: all equations reduce to Chandrasekhar originals

## Conventions
- Metric signature (-,+,+,+), c kept explicit
- Followed RELATIVISTIC_CONVENTIONS.md throughout
- Used macros from rel_preamble.tex (enthalpy, edensity, etc.)

## Issues / Notes
- The incompressibility assumption is retained from the classical treatment; a fully
  compressible relativistic analysis would require coupling to the equation of state
  and would yield additional modes (sound waves).
- Surface tension in the relativistic context is treated as a purely surface quantity;
  a covariant treatment via the Israel junction conditions would be more rigorous.
