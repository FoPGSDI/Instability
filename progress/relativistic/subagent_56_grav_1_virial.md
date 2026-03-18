---
agent: 56
chapter: 13 (relativistic, §116-118)
task: Relativistic virial theorem
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_13_sec116-118.tex`, a
relativistic generalization of Chapter XIII §116-118 (virial theorem) from
Chandrasekhar's *Hydrodynamic and Hydromagnetic Stability*.

### Key content

1. **§116 — Introduction** (Section rel-116):
   - Three key GR effects: pressure as gravity source, gravitational redshift,
     non-linearity of Einstein equations.
   - Overview of the destabilising nature of GR for self-gravitating systems.

2. **§117 — Relativistic virial theorem** (Section rel-117):
   - Definitions: relativistic moment of inertia I^(rel)_ik using
     (epsilon+p)/c^2 weighting, relativistic kinetic-energy tensor, and
     gravitational potential energy (ADM binding energy and post-Newtonian
     tensor W^(PN)_ik).
   - Tensor virial theorem via integral of T^{0i} x^j d^3x, with time
     derivative yielding the second time derivative of I^(rel)_ij.
   - Special-relativistic exact form and post-Newtonian scalar virial
     identity with 1/c^2 correction terms.
   - Equilibrium configurations: virial equilibrium includes pressure
     contribution to gravitational mass through (epsilon+p)/c^2.

3. **§118 — Virial theorem for small oscillations** (Section rel-118):
   - Chandrasekhar (1964) radial pulsation equation with metric functions.
   - Relativistic virial estimate for omega^2 with homologous trial function.
   - Connection to Chandrasekhar mass limit: M_Ch ~ 1.44 M_sun.
   - Critical adiabatic index: gamma_c = 4/3 + kappa GM/(Rc^2), with
     kappa = 38/21 for uniform-density sphere.
   - GR correction makes stars MORE unstable: positive feedback loop where
     pressure gravitates.
   - Astrophysical consequences: white dwarfs, neutron star maximum mass,
     supermassive star collapse.
   - Comparison table of Newtonian vs GR stability criteria.

## Conventions

- Metric signature (-,+,+,+), c kept explicit throughout.
- Uses `\edensity` for energy density, `\rdensity` for rest-mass density,
  `\Lf` for Lorentz factor, per RELATIVISTIC_CONVENTIONS.md.
- Labels: `sec:rel-116`, `sec:rel-117`, `sec:rel-118`, `eq:rel-13-*`.
- Cross-references to classical §116-118 via `\ref{sec:116}` etc.
- `\begin{relcorrection}` environments for GR vs Newtonian comparisons.

## Issues / Notes

- The exact numerical coefficient kappa depends on the density profile;
  38/21 is for the uniform-density (Schwarzschild interior) case.
- Non-radial stability and CFS instability noted as future work.

## Next

This section provides the foundation for relativistic gravitational
instability analysis in subsequent sections (Jeans instability in GR,
rotating relativistic stars, etc.).
