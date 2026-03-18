---
agent: 42
chapter: 10
sections: 90-92
task: Relativistic RT perturbation equations (inviscid case)
status: completed
timestamp: 2026-03-18T12:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_10_sec90-92.tex` containing the
relativistic generalization of Chandrasekhar Chapter X, sections 90--92:

- **Section 90 (Introduction):** Motivates relativistic RT instability with
  astrophysical contexts (relativistic jets, supernovae, GRBs). States the
  three key relativistic modifications: enthalpy replacing density, causality
  constraints, and astrophysical relevance.

- **Section 91 (Perturbation equations):** Derives the relativistic hydrostatic
  equilibrium (TOV weak-field limit), linearises the energy-momentum tensor for
  Eulerian perturbations, and obtains the normal-mode eigenvalue equation
  (eq. rel-10-14). Shows that the classical eq. (10-42) is recovered with
  the substitution rho -> w = (epsilon+p)/c^2. Includes relativistic surface
  tension via Israel junction conditions.

- **Section 92 (Inviscid case):** Solves two canonical problems:
  (a) Two uniform fluids: dispersion relation sigma^2 = gk * A_rel with
  relativistic Atwood number A_rel = (w2-w1)/(w2+w1).
  (b) Exponentially varying enthalpy: identical eigenvalue structure to
  classical case with beta = D(ln w0).
  Includes causality analysis confirming the RT mode is well-posed.

## Key relativistic features

- Pressure contributes to inertia: w = (epsilon+p)/c^2 replaces rho everywhere.
- Two equal-rest-mass-density fluids with different temperatures can be RT-unstable
  (genuinely relativistic effect).
- Causality: RT modes have real sigma (no propagation), sound-speed bounded by c,
  Israel-Stewart for dissipative extensions.

## Conventions

Follows RELATIVISTIC_CONVENTIONS.md: metric (-,+,+,+), c explicit,
T^{mu nu} = w u^mu u^nu + p g^{mu nu}.

## Next

Sections 93+ (variational principle, viscous case) to be handled by subsequent agents.
