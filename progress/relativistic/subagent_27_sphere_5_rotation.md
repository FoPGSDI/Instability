---
agent: 27
chapter: 6 (§§61-63)
task: Relativistic rotating sphere — thermal instability with rotation
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_6_sec61-63.tex` containing the
relativistic generalization of Chapter VI §§61-63 (rotation in spheres,
geophysical applications).

### §61 — Rotation effect on thermal instability in sphere (relativistic)
- Axisymmetric solenoidal field representation using 3+1 decomposition with
  conformal spatial metric; modified phi-Laplacian operator with gravitational
  redshift corrections
- Perturbation equations with relativistic Coriolis term: inertial density
  replaced by enthalpy w = (eps+p)/c^2, effective rotation Omega_eff including
  Lense-Thirring frame dragging
- Israel-Stewart causal heat equation (tau_q relaxation time)
- Boundary conditions for rigid crust and free surface; additional IS boundary
  condition on heat flux
- Variational principle with conformal volume element e^{3Phi/c^2}

### §62 — Stationary convection onset (relativistic)
- Marginal stability equations (sigma=0) with relativistic operators
- Critical Ra_rel(Ta_rel) with post-Newtonian corrections: modified effective
  gravity, frame-dragging reduction, redshift weighting of volume element
- Asymptotic scaling Ra ~ Ta^{2/3} preserved with relativistic prefactor

### §63 — Astrophysical applications (replacing geophysical)
- Neutron star core convection: parameter table comparing Earth's core vs
  neutron star core; compactness 0.1-0.3 gives 10-30% corrections
- Millisecond pulsars: Ta_rel ~ 10^{20}-10^{24}, Lense-Thirring reduces
  effective rotation by ~20-30%, net effect lowers critical Ra
- Proto-neutron star cooling: neutrino-driven convection, double-diffusive
  generalization (entropy + lepton fraction), time-dependent background,
  mildly relativistic regime (~10-15% corrections)

## Conventions followed
- Metric signature (-,+,+,+), c kept explicit
- Israel-Stewart causal dissipation
- Relativistic enthalpy density w = (eps+p)/c^2
- All dimensionless numbers per RELATIVISTIC_CONVENTIONS.md

## Next
- Git commit and push
