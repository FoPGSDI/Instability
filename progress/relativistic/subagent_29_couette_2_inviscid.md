---
agent: 29
chapter: 7
section: 67
task: Relativistic inviscid Couette flow stability analysis
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_7_sec67.tex` containing
the relativistic generalization of Chandrasekhar Chapter VII §67 (Analytical
discussion of the stability of inviscid Couette flow).

### Content produced

1. **§67(a) — Lagrangian displacement formulation in SR**
   - Relativistic background flow with Lorentz factor gamma
   - Relativistic pressure perturbation variable
   - Normal-mode decomposition and Lagrangian displacement definition
   - Derivation of relativistic Rayleigh discriminant Phi_rel(r)
   - Self-adjoint system for variational formulation

2. **§67(b) — Case m=0 (axisymmetric): relativistic Rayleigh criterion**
   - Sturm-Liouville equation with Phi_rel
   - Variational expression for p^2/k^2
   - Necessary and sufficient condition: d/dr(gamma^2 r^2 Omega) >= 0
   - Physical interpretation of relativistic angular momentum

3. **§67(c) — Case m!=0 (non-axisymmetric): relativistic Howard semicircle theorem**
   - Hermitian system for real p, real k^2 eigenvalues
   - Generalized variational expression
   - Howard semicircle bound with proof sketch
   - Growth-rate bound identical to classical

4. **§67(d) — Energy principle for relativistic rotating flow**
   - Quadratic energy functional delta^2 W
   - Stability iff delta^2 W > 0
   - Sufficient condition for non-axisymmetric stability

5. **§67(e) — Causality constraint on perturbation modes**
   - Subluminal phase velocity requirement
   - Minimum wavenumber bound |k| >= |m| Omega_max / c
   - Group velocity bounded by hyperbolic structure
   - Modes violating causality excluded from physical spectrum

### Conventions

- Metric signature (-,+,+,+), c explicit throughout
- Lorentz factor gamma = (1-V^2/c^2)^{-1/2}
- Enthalpy density w = (epsilon+p)/c^2
- All macros from rel_preamble.tex used where applicable
- Non-relativistic limits verified for every key equation

## Issues / Notes

- The relativistic Rayleigh discriminant involves gamma^4 factors from both
  the inertia enhancement and angular-momentum transport modification.
- The Howard semicircle theorem's algebraic structure is unchanged by
  relativity; only the discriminant Phi_rel is modified.
- The causality section is entirely new (no classical counterpart).

## Next

This section is complete. Integration into rel_main.tex can proceed when
all Chapter VII relativistic sections are available.
