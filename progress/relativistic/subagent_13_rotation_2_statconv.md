---
agent: 13
chapter: 3 (relativistic)
sections: 24-28
task: Relativistic stationary convection with rotation
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_3_sec24-28.tex` containing
the relativistic extension of Chandrasekhar's Chapter III, §§24–28 (stationary
convection with rotation).

### Sections produced

- **§24 (rel)** General considerations: relativistic Taylor–Proudman theorem
  with inertial mass density w/c² replacing ρ₀.

- **§25 (rel)** Perturbation equations: Coriolis coupling with relativistic
  inertia; Israel–Stewart causal heat equation (telegraph-type); normal-mode
  analysis yielding three coupled ODEs with effective kinematic viscosity
  ν_eff = η_s c²/w.

- **§26 (rel)** Variational principle: self-adjoint structure preserved;
  Rayleigh number expressed as ratio of positive-definite integrals, exactly
  as in the classical case but with ν → ν_eff.

- **§27 (rel)** Solutions for three boundary conditions:
  - Two free: characteristic equation identical in form, with T → Ta_rel ≥ T.
  - Two rigid: variational/determinantal method, same secular equation at
    shifted Taylor number.
  - One rigid + one free: odd-mode reduction still valid.
  - T^{1/3} and T^{2/3} laws: persist with identical exponents; prefactors
    modified by (w/ρ₀c²)^{4/3}.

- **§28 (rel)** Cell patterns: rolls, squares, hexagons — qualitatively
  unchanged; spirals wound more tightly by √(Ta_rel/T); Veronis's invariance
  of streamline wavelength in the roll plane extends to the relativistic case.

- **Causality verification**: All modes (heat, shear, inertial, combined)
  shown to be causal with Israel–Stewart relaxation times.

## Key relativistic modifications

1. ν → ν_eff = η_s c²/(ε+p) — relativistic kinematic viscosity
2. Ta_rel = 4Ω²d⁴ w²/(η_s² c⁴) ≥ T (classical) — enhanced Taylor number
3. Israel–Stewart heat equation ensures finite thermal signal speed
4. Power-law scaling exponents (1/3, 2/3) are universal; prefactors change
5. Non-relativistic limit (w → ρ₀c², τ_q → 0) recovers original §§24–28

## Issues / Notes

- The detailed numerical tables (VII–IX) are not recomputed; they can be
  reused at the shifted Ta_rel values.
- The analysis is restricted to Ω ∥ g (as in the original); the oblique
  case (§34) would require separate treatment.
- Radiation-dominated EOS gives the largest corrections; for ordinary matter
  the corrections are O(p/ε) ≪ 1.

## Next

- Companion sections on oscillatory convection with rotation (§§29–33)
  would complete the relativistic treatment of Chapter III rotation effects.
