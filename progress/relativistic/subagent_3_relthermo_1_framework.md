---
agent: 3
task: relativistic_thermodynamics_causality_framework
stage: 1
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_framework_thermo.tex` containing the
complete relativistic thermodynamics and causality framework. The file covers:

1. **Relativistic thermodynamics** — first law (per unit volume), enthalpy
   density w = eps + p, specific enthalpy h, Gibbs-Duhem relation, EOS choices.
2. **Causality constraints on EOS** — sound speed bound 0 <= c_s^2 <= c^2,
   Le Chatelier stability, ideal gas expression, ultrarelativistic (c^2/3) and
   non-relativistic limits.
3. **Thermal conduction** — Fourier (acausal) -> Cattaneo (telegraph eqn) ->
   Israel-Stewart (fully covariant with Tolman-Ehrenfest term); thermal wave
   speed and entropy production.
4. **Viscosity** — Bulk (relaxation eqn, signal speed, entropy production) and
   shear (relaxation eqn, shear tensor, signal speed, entropy production);
   all tau > 0 required.
5. **Relativistic buoyancy** — Schwarzschild criterion with w replacing rho,
   Ledoux criterion with composition, Brunt-Vaisala frequency, connection to
   Chandrasekhar's thermal instability.
6. **Causality summary** — Table of all signal speeds and bounds, modification
   summary, verification checklist for downstream agents.

## Conventions

- Metric signature (-,+,+,+), c kept explicit throughout.
- Notation follows RELATIVISTIC_CONVENTIONS.md exactly.
- Uses macros \cs, \vA, etc. from rel_preamble.tex.
- Uses \ding{51} for checklist items (requires pifont package).

## Issues / Notes

- The file uses `\ding{51}` (checkmark) from the `pifont` package; the main
  preamble should include `\usepackage{pifont}`.
- Equation labels use prefix `eq:rel-` or `eq:` for cross-referencing by
  other agents.
- The Brunt-Vaisala frequency (eq:rel-BV) is given in a simplified radial
  form appropriate for spherically symmetric backgrounds; a fully covariant
  version would require specifying the foliation.

## Next

This framework is referenced by subsequent relativistic sections on Benard
convection, Taylor-Couette flow, and MHD instabilities. Downstream agents
should use the equation labels and causality checklist defined here.
