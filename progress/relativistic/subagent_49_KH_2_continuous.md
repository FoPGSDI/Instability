---
agent: 49
chapter: 11
sections: 102-103
task: Relativistic KH continuous variation
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_11_sec102-103.tex` containing
the relativistic generalization of Chandrasekhar Ch XI §102-103 (Kelvin-Helmholtz
instability with continuous velocity and density profiles).

### Section 102: Continuous variation of U (relativistic)

- Three-layer profile with enthalpy density w (not rest-mass density rho) as the
  stratification variable, following RELATIVISTIC_CONVENTIONS.md.
- Perturbation equation derived with the crucial Gamma^4 factor from relativistic
  inertia (Lorentz boost of the material acceleration).
- Relativistic Richardson number: J_rel = J_class / Gamma_0^4, reflecting the
  enhanced effective inertia of relativistic shear flow.
- Characteristic equation (eq rel-11-12) reduces to the classical eq 11-58 as
  U_0/c -> 0.
- Instability band narrower than classical by factor Gamma_0^{-4}.
- Causality: phase speeds bounded by relativistic velocity addition; group speeds
  sub-luminal via Howard semicircle theorem.

### Section 103: Both w and U continuously variable (relativistic)

- Relativistic energy argument: interchange work uses enthalpy density; available
  kinetic energy carries Gamma^4 factor.
- General relativistic Richardson number: J_rel = -(g/w)(dw/dz) / [Gamma^4 (dU/dz)^2].
- Relativistic Brunt-Vaisala frequency N_rel^2 includes compressibility correction
  involving c_s and c.
- Miles-Howard theorem: J_rel >= 1/4 is sufficient for stability. Critical value
  remains 1/4 because Gamma^4 cancels in numerator and denominator.
- Howard semicircle theorem: complex phase speed bounded by U_max < c.
- Analytical results for exponential-density + linear-velocity profiles:
  * Whittaker function solutions carry over with J -> J_rel.
  * Perturbative Gamma^4 correction to eigenvalues (eq rel-11-35).
  * Algebraic decay exponent modified: t^{-3/2+sqrt(1/4-J_rel)}, slower decay
    than classical due to reduced effective J.
  * Flow stable for all positive J_rel, same as classical.
- Causality: phase speeds, group speeds, and signal speeds all < c, verified via
  velocity-addition formula and semicircle bounds.

## Conventions

- Metric (-,+,+,+), c explicit, following RELATIVISTIC_CONVENTIONS.md.
- Enthalpy density w = (epsilon + p)/c^2 used throughout.
- Lorentz factor Gamma = (1 - U^2/c^2)^{-1/2}.
- LaTeX macros: \Lf, \enthalpy, \cs from rel_preamble.tex.

## Files

- Output: `output/chapters/relativistic/rel_chapter_11_sec102-103.tex`
- Progress: `progress/relativistic/subagent_49_KH_2_continuous.md`
