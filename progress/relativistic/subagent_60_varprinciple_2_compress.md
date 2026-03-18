---
agent: 60
chapter: 14
section: 123
task: Relativistic compressibility extension of variational principle
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_14_sec123.tex` containing the
relativistic generalization of Chapter XIV §123 (extension of the variational
principle to allow for compressibility).

## Content

### §123: Compressibility extension — relativistic
- **Compressible perturbations**: Eulerian perturbations δε, δp linked through
  the relativistic equation of state via the adiabatic sound speed
  c_s² = (∂p/∂ε)_s, replacing the classical γp/ρ relation.
- **Modified energy functional**: The compressibility terms I and II are
  generalized to use the relativistic enthalpy density w = (ε+p)/c² in place
  of ρ, covariant derivatives in place of partial derivatives, and the magnetic
  four-vector b^μ in place of H_i.
- **Sound speed bound**: The causality constraint c_s ≤ c enters explicitly
  in the compressibility contribution δW_comp, bounding the adiabatic restoring
  force and ensuring causal propagation of compressional disturbances.
- **Fast magnetosonic speed**: Verified that v_f < c automatically when c_s < c,
  confirming causal character of the full MHD variational principle.
- **Connection to relativistic MHD stability**: Applications to interchange
  modes, Parker instability, MRI, and neutron-star oscillations discussed.

### Bibliographical notes
- Bernstein et al. (1958): foundational energy principle for compressible MHD
- Frieman & Rotenberg (1960): extension to stationary equilibria with flow
- Schutz (1970): variational formulation of relativistic perfect fluids
- Friedman & Schutz (1978): Lagrangian perturbation theory for relativistic
  self-gravitating fluids; self-adjointness and variational principle
- Friedman & Schutz (1978b): CFS instability mechanism
- Kokkotas & Schutz (1986): quasi-normal modes and energy principle
- Lichnerowicz (1967): relativistic MHD characteristic speeds
- Komissarov (1999): numerical relativistic MHD with causal bounds
- Bedaque & Steiner (2015): sound velocity bound in neutron stars

### CAUSALITY verification
Compressibility introduces the sound speed c_s into the variational principle.
The causality constraint c_s < c must be verified for all equilibrium
configurations before applying the stability analysis. The document includes
explicit bounds showing that the compressibility term is bounded by the total
enthalpy-plus-magnetic energy, and that v_f < c follows from c_s < c.

## Conventions
- Metric signature (-,+,+,+), c kept explicit
- 4-velocity normalization u^μ u_μ = -c²
- Relativistic enthalpy density w = (ε+p)/c²
- All notation consistent with RELATIVISTIC_CONVENTIONS.md

## Issues / Notes
None. The section is self-contained and follows the structure of existing
relativistic chapter files.

## Next
Git commit and push.
