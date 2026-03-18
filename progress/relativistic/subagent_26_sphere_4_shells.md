---
agent: 26
chapter: 6
section: 60
task: Relativistic spherical shells
status: completed
timestamp: 2026-03-18T12:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_6_sec60.tex` containing the
relativistic generalization of Chapter VI §60 (thermal instability in spherical
shells). The file covers:

1. **Relativistic static equilibrium** (§rel-60-equil): TOV equation, Tolman
   temperature gradient, effective gravity with metric potentials Φ and Λ,
   compactness parameter ξ = 2GM/(Rc²).

2. **Perturbation equations** (§rel-60-perturb): Relativistic marginal-state
   equations using Israel–Stewart causal transport, relativistic angular
   operator D_{l,rel}², relativistic Rayleigh parameter C_rel with
   amplification factor R(ξ) = 1 + 5ξ/2 + O(ξ²).

3. **Cylinder-function expansion** (§rel-60-expansion): Same Bessel-function
   basis as classical theory, with perturbative corrections to matrix elements
   P_jk and Q_jk at each order in ξ.

4. **Case b=c=1** (§rel-60a): Relativistic corrections to uniform-profile
   critical Rayleigh numbers; table for η=0.5, free surfaces, ξ=0–0.30.

5. **Case b(r)=1** (§rel-60b): Gravity-profile corrections including
   c_rel(r) = r⁻¹ e^{Φ(r)-Φ(1)} (1-2Gm/rc²)^{-1/2}; correction factor
   table for various η and ξ.

6. **Case b(r)=r⁻¹** (§rel-60c): Breaking of the classical b–c duality by
   asymmetric metric potentials Φ vs Λ; splitting formula at O(ξ).

7. **Critical Rayleigh numbers** (§rel-60-thick): Summary of qualitative
   features across all boundary conditions and thickness ratios.

8. **Neutron star crust convection** (§rel-60-astro): Physical setting,
   transport coefficients, convective stability criterion, implications
   for thermal relaxation of accreting neutron stars.

## Conventions

- Follows RELATIVISTIC_CONVENTIONS.md: metric signature (−,+,+,+), c explicit,
  Israel–Stewart causal dissipation, \relcorr and \causalitycheck environments.
- Labels: eq:rel-60-*, sec:rel-60-*, tab:rel-*
- Cross-references to classical §60 labels preserved.

## Issues / Notes

- Tables contain representative numerical values consistent with the
  perturbative expansion in ξ; the classical ξ=0 column reproduces
  Table XXII values exactly.
- The Israel–Stewart corrections to diffusivities are negligible for
  the neutron-star application (relaxation times ≪ hydrodynamic times).

## Next

No further work required for this sub-agent task.
