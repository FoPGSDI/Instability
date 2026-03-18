---
agent: 59
chapter: 14
sections: 121-122
stage: completed
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Relativistic extension of Ch XIV sections 121-122 (General Variational Principle for Hydromagnetic Stability).

### What was done

1. **Section 121 (Introduction):** Motivated the relativistic energy principle, introduced the decomposition of the second-variation energy functional into kinetic, magnetic, gravitational, and pressure terms, each with relativistic modifications.

2. **Section 122 (Variational Principle):** Full development including:
   - Relativistic equilibrium state with covariant energy-momentum tensor
   - Lagrangian displacement 4-vector and perturbation equations
   - Explicit forms of all four energy functional contributions:
     * Kinetic: w = (epsilon+p)/c^2 replacing rho
     * Magnetic: b^mu b^nu replacing H_i H_j
     * Gravitational: G_{mu nu} / lapse+extrinsic curvature terms
     * Pressure/surface: covariant jump conditions
   - Self-adjointness proof and stability criterion (delta^2 W > 0)
   - Israel-Stewart causal dissipation in the variational framework
   - Dispersion relation with finite relaxation times
   - Proof that stability boundary is unaffected by dissipation
   - Connection to Bernstein-Frieman-Kruskal-Kulsrud energy principle
   - Explicit non-relativistic limits recovering all classical equations

### Key relativistic features
- Enthalpy density w = (epsilon+p)/c^2 as inertial mass density
- Magnetic 4-vector b^mu with b^mu u_mu = 0 constraint
- Causality bounds on all characteristic speeds
- Israel-Stewart relaxation times ensuring causal dissipation
- Gravitational contributions via lapse function and extrinsic curvature

## Output file
- `output/chapters/relativistic/rel_chapter_14_sec121-122.tex`
