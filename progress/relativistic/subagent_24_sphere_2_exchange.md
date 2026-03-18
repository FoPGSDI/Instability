---
agent: 24
task: relativistic_exchange_stabilities_spheres_ch6_sec57-58
stage: completed
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_6_sec57-58.tex` containing the
relativistic extension of Chandrasekhar's Chapter VI, sections 57 and 58.

### Section 57: Exchange of stabilities in relativistic spherical geometry

- Introduced the enthalpy-inertia parameter I = 1 + p/epsilon, which replaces
  rho with w = (epsilon + p)/c^2 as the inertial density.
- Posed and answered the question: does the exchange of stabilities survive when
  pressure contributes to inertia? Answer: YES.
- Modified proof tracks the factor I through the integral identity. Since I > 0
  always, positive-definiteness of the coefficient of sigma_i is preserved.
- Israel-Stewart relaxation time tau_q makes the effective Prandtl number
  frequency-dependent, but enters only through a positive factor D_{tau_q}^{-1},
  so the proof remains valid.

### Section 58: Variational principle -- relativistic

- Derived the relativistic Rayleigh quotient (eq. rel-83), which has the SAME
  functional form as the classical one (eq. 6-83).
- All relativistic physics is absorbed into C_rel = I * C, so the critical
  parameter is larger: C_rel^(crit) > C^(crit). Relativistic pressure-inertia
  coupling stabilizes the shell.
- Thermodynamic significance: viscous dissipation and buoyancy work both acquire
  the factor I, which cancels in their ratio, recovering the Rayleigh quotient.
- Entropy production in Israel-Stewart theory is non-negative; at marginal state,
  net production by the convective mode is zero to leading order.

### Causality

- Thermal signal speed v_th = sqrt(kappa / tau_q w c^2) must satisfy v_th <= c.
- Viscous signal speed similarly bounded.
- No l-dependent causality violation: spherical harmonic decomposition preserves
  the plane-wave causality bounds.
- At marginal state (sigma = 0), kappa_IS reduces to kappa, so the critical
  Rayleigh quotient is independent of tau_q.

### Summary table

Provided a comparison table (classical vs relativistic) covering inertial
density, control parameter, exchange of stabilities, Rayleigh quotient,
thermodynamic content, heat transport, causality, and stabilizing effect.

## Conventions

- Metric signature (-,+,+,+), c kept explicit throughout.
- Notation follows RELATIVISTIC_CONVENTIONS.md.
- Uses macros from rel_preamble.tex (\enthalpy, \tauq, \taupi, \shearvisc, etc.).
- Equation labels use prefix `eq:rel-` for new equations, `eq:6-` for references
  to the original chapter_6.tex.

## Issues / Notes

- The enthalpy-inertia parameter I is defined for a single-component fluid.
  Multi-component fluids (e.g., neutron star matter with muons) would require
  a composition-dependent generalization.
- The proof assumes the background state is static and spherically symmetric;
  rotation and magnetic fields are not included here.
- General relativistic corrections (spacetime curvature, gravitational redshift)
  are not treated; this is a special-relativistic extension.

## Next

This section is referenced by any downstream work on relativistic convection
in spherical shells, including GR extensions and magnetized configurations.
