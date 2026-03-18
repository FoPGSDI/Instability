---
agent: 31
chapter: 7
sections: 69-70
task: Relativistic viscous Couette perturbations
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_7_sec69-70.tex` containing the
relativistic generalization of Chandrasekhar Chapter VII, sections 69--70.

### Section 69: Relativistic viscous Couette flow
- Full Israel-Stewart energy-momentum tensor with shear stress relaxation
- Derivation of the viscous signal speed bound (causality)
- Equilibrium Couette profile with Lorentz factor corrections
- Relativistic shear tensor in cylindrical coordinates
- Velocity profile V(r) = Ar + B/r + O(V^3/c^2) corrections

### Section 70: Relativistic perturbation equations
- Linearized momentum equations with gamma^2 factors and Israel-Stewart viscous terms
- Linearized Israel-Stewart relaxation equation for shear stress perturbations
- Effective frequency-dependent viscosity nu_eff = nu/(1 + tau_pi * p)
- Normal mode decomposition and eigenvalue problem
- Relativistic Taylor number T_rel with gamma^2 corrections
- Proof that mu > eta^2 remains sufficient for stability (energy integral method)
- Eigenvalue problem for critical T_rel at marginal stability (p=0)
- Discussion of oscillatory modes and Israel-Stewart damping modification
- Causality: finite viscous propagation speed guaranteed by tau_pi > 0

## Key results
- Rayleigh criterion mu > eta^2 is unchanged as sufficient stability condition
- Relativity stabilises: T_rel,cr > T_cl,cr by O(V^2/c^2)
- Israel-Stewart drops out at marginal stability (p=0) but modifies damping of stable modes
- All viscous signals bounded by v_visc = sqrt(eta_s / (w * tau_pi)) <= c

## Conventions
- Metric signature (-,+,+,+), c explicit, as per RELATIVISTIC_CONVENTIONS.md
- Labels: eq:rel-7-134 through eq:rel-7-171
- Section labels: sec:rel-7-69, sec:rel-7-70

## Next
- File is self-contained; ready for integration into rel_main.tex
