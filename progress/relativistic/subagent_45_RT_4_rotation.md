---
agent: 45
chapter: 10
section: 95
task: Relativistic RT with rotation
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_10_sec95.tex` containing the
relativistic extension of Chapter X, Section 95 (Effect of rotation on the
Rayleigh--Taylor instability).

## Content

The file covers the following topics:

1. **Relativistic perturbation equations with rotation** -- Linearised momentum,
   continuity, and divergence-free equations in the co-rotating frame with
   enthalpy-based inertia (w/c^2 replacing rho) and covariant Coriolis force
   carrying Lorentz factor gamma_Omega^2.

2. **Two uniform fluids with rotation** -- Relativistic dispersion relation
   (eq. rel95-disp-two) generalising Chandrasekhar eq. (10-159)/(10-160).
   Solutions for stable/unstable branches. Enthalpy-based Atwood number.
   Minimum oscillation frequency bound 2*Omega_rel.

3. **Exponentially varying density with rotation** -- Relativistic counterpart
   of eqs. (10-165)--(10-170). Critical wavenumber k_d,rel for rotational
   stabilisation. Correction ratio k_d,rel/k_d quantified.

4. **Relativistic effective gravity** -- Centrifugal term with Lorentz
   enhancement, gravitational acceleration, and frame-dragging (Lense-Thirring)
   contribution from Kerr spacetime.

5. **Modified growth rates** -- Explicit formula with limits for no-rotation,
   strong-rotation, and Newtonian regimes.

6. **Causality check** -- Five-point verification: phase velocity bound, group
   velocity bound, co-rotation speed < c, effective wavenumber positivity, and
   no superluminal signals.

## Conventions

- Metric signature (-,+,+,+), c kept explicit
- Uses rel_preamble.tex macros (enthalpy, edensity, Lf, cs, etc.)
- causalitycheck and relcorrection tcolorbox environments used
- All results reduce to Newtonian S95 in c -> infinity limit

## Issues / Notes

- The incompressibility assumption is noted as an idealisation valid when
  perturbation velocities are much less than the sound speed.
- Frame-dragging contribution is presented at the order-of-magnitude level
  (Lense-Thirring scaling) since a full Kerr treatment would require
  specifying the complete background metric.

## Next

No further stages required. File is complete and ready for integration into
rel_main.tex.
