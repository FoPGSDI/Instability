---
agent: 43
chapter: 10
section: 93
task: Relativistic variational principle for Rayleigh-Taylor instability
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Extended Chandrasekhar's general variational principle for Rayleigh-Taylor
instability (§93, Ch X) to the relativistic regime.

### What was done

1. **Read** classical §93 (chapter_10.tex, lines 412-577) and RELATIVISTIC_CONVENTIONS.md.

2. **Created** `output/chapters/relativistic/rel_chapter_10_sec93.tex` containing:
   - Relativistic preliminaries: energy-momentum tensor, enthalpy density w = (epsilon+p)/c^2, TOV equilibrium.
   - Linearised perturbation equations with rho -> w replacement and Israel-Stewart viscosity.
   - Orthogonality relations (relativistic analogue of eq 10-83).
   - Reality conditions for characteristic values.
   - **Variational principle**: energy functional with relativistic kinetic energy T = (1/2)w|v|^2 instead of (1/2)rho|v|^2, potential energy from Dw stratification, extremal condition -> eigenvalue problem.
   - **Eigenvalue problem** for growth rate n (quadratic in n for Navier-Stokes limit).
   - **Bounds on growth rate**: upper bound from inviscid Rayleigh quotient with w in denominator; lower bound from viscous damping; Israel-Stewart reduction of effective viscosity at high n.
   - **Non-relativistic limit**: explicit verification that c -> infinity recovers all classical equations (10-88 through 10-94).

### Key physical results

- The replacement rho -> w = (epsilon+p)/c^2 increases inertia, reducing RT growth rates.
- The Atwood number is modified to use enthalpy-density contrast rather than mass-density contrast.
- Israel-Stewart causal dissipation weakens viscous stabilisation for rapidly growing modes (tau_pi * n >> 1).
- All results reduce exactly to Chandrasekhar's §93 in the non-relativistic limit.

## Issues / Notes

- The Israel-Stewart effective viscosity mu_hat = mu/(1 + tau_pi * n) introduces an implicit nonlinearity in the eigenvalue equation (n appears in both the eigenvalue and the viscosity). This is a known feature of causal dissipation theories.
- No content-filter issues encountered.

## Next

This section is complete. Ready for integration into rel_main.tex if needed.
