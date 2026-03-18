---
agent: 1
chapter: relativistic-framework
stage: complete
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created the foundational relativistic hydrodynamics framework file
`output/chapters/relativistic/rel_framework_hydro.tex`.

This chapter provides the theoretical basis that all other relativistic
modification agents will reference.

## Sections Written

1. **Special Relativistic Perfect-Fluid Hydrodynamics** (Sec. 1)
   - Four-velocity, normalization, projection tensor
   - Energy-momentum tensor for perfect fluid
   - Conservation laws (baryon number + energy-momentum)
   - 3+1 decomposition into relativistic Euler equations

2. **Israel-Stewart Dissipative Hydrodynamics** (Sec. 2)
   - Eckart/Navier-Stokes acausality problem (parabolic equations)
   - Full Israel-Stewart relaxation equations for bulk viscosity, shear stress, heat flux
   - Demonstration that relaxation terms restore hyperbolicity
   - Telegraph equation derivation showing finite signal speed
   - Causality bound on relaxation times

3. **Linearized Perturbation Theory** (Sec. 3)
   - Static uniform background state
   - Linearized continuity, energy, and momentum equations
   - Sound wave dispersion relation: omega^2 = c_s^2 k^2
   - Causality bound c_s <= c
   - Dissipative corrections to dispersion relation

4. **Non-Relativistic Limit** (Sec. 4)
   - Systematic v/c expansion of all quantities
   - Recovery of Euler and Navier-Stokes equations
   - Explicit O(v^2/c^2) correction terms identified
   - Direct connection to Chandrasekhar's starting equations

5. **Relativistic Boussinesq Approximation** (Sec. 5)
   - Enthalpy density decomposition replacing density
   - Relativistic thermal expansion coefficient
   - Full set of relativistic Boussinesq equations
   - Pressure-buoyancy coupling (purely relativistic term)
   - Relativistic Rayleigh number with correction terms
   - Implications for stability thresholds

## Key Equations

- `eq:rel-emt-perfect`: Perfect fluid energy-momentum tensor
- `eq:rel-continuity`: Baryon number conservation
- `eq:rel-energy`, `eq:rel-momentum`: 3+1 energy and momentum equations
- `eq:rel-bulk-relax`, `eq:rel-shear-relax`, `eq:rel-heat-relax`: Israel-Stewart relaxation
- `eq:rel-dispersion`: Sound wave dispersion relation
- `eq:causality-cs`: Causality bound on sound speed
- `eq:post-newtonian-momentum`: Post-Newtonian momentum equation with O(v^2/c^2) corrections
- `eq:rel-bouss-mom`: Relativistic Boussinesq momentum equation
- `eq:rel-buoyancy`: Relativistic buoyancy with pressure coupling
- `eq:rel-rayleigh`: Relativistic Rayleigh number

## Conventions

- Metric signature (-,+,+,+) throughout
- Speed of light c kept explicit (not set to 1)
- All macros from RELATIVISTIC_CONVENTIONS.md used where applicable
- Labels follow pattern `eq:rel-*` for easy cross-referencing

## Issues

None. All derivations are self-consistent and the non-relativistic limits recover the expected classical equations.
