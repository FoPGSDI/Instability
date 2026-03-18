---
agent: 23
chapter: 6
sections: 55-56
task: Relativistic spherical perturbation equations
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_6_sec55-56.tex` containing the
relativistic generalization of Chapter VI sections 55-56 (thermal instability in
spheres, perturbation equations).

### Content produced

- **Section 55 (Introduction):** Motivation for spherical geometry in the
  relativistic context — neutron stars, proto-neutron stars, compact stellar
  interiors. Identified five key differences from the classical treatment
  (strong gravity, TOV equilibrium, causality bounds, Israel-Stewart transport,
  Tolman redshift corrections to buoyancy).

- **Section 56 (Perturbation equations):** Full relativistic treatment including:
  - TOV background equilibrium (eqs. rel6-mass through rel6-Phi) replacing
    Newtonian hydrostatic balance
  - Relativistic thermal background with Tolman-redshifted temperature and
    Israel-Stewart steady-state heat equation
  - Angular momentum operator L^2 shown to be identical in curved spacetime
    (angular sector is the round two-sphere)
  - Relativistic radial operator D_{l,rel}^2 incorporating metric functions
    Phi and Lambda
  - Normal mode analysis: Eulerian perturbations decomposed in spherical
    harmonics Y_l^m, yielding coupled radial ODE system
  - Israel-Stewart thermal perturbation equation (hyperbolic, causal)
  - Combined sixth-order equation (relativistic analogue of eq. 6-23)
  - Boundary conditions: regularity at centre, junction conditions at stellar
    surface (Lagrangian pressure, metric continuity, heat flux continuity)
  - Toroidal/poloidal decomposition in curved spacetime
  - Summary of all relativistic corrections with explicit non-relativistic limits

### Conventions

All notation follows RELATIVISTIC_CONVENTIONS.md: signature (-,+,+,+), c kept
explicit, Greek indices for spacetime, Israel-Stewart causal dissipation.

## Issues / Notes

- The curvature-coupling terms R_W and R_Theta in the perturbation equations are
  indicated schematically; their full expansion depends on the specific gauge
  choice (Regge-Wheeler vs. others) and is deferred to later sections.
- The Israel-Stewart relaxation time tau_q is treated as a given parameter;
  its microscopic derivation from kinetic theory is beyond the scope of this
  chapter.

## Next

Subsequent agents should address:
- Sections 57-59: Principle of exchange of stabilities in the relativistic case,
  variational methods, and numerical solutions for specific stellar models
- The explicit form of the curvature-coupling terms in a chosen gauge
