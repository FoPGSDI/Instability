---
agent: 12
chapter: 3 (sections 19--23)
task: Relativistic rotating frame equations
status: completed
timestamp: 2026-03-18T00:00:00Z
branch: relativistic
---

## Summary

Created `output/chapters/relativistic/rel_chapter_3_sec19-23.tex` containing the
relativistic generalization of Chandrasekhar Chapter III, Sections 19--23 (rotating
frames, vorticity theorems, wave propagation).

### Sections produced

| Section | Title | Key content |
|---------|-------|-------------|
| 19 (rel) | Introduction: relativistic rotating fluids | Motivation: neutron stars, accretion disks, QGP |
| 20 (rel) | Helmholtz--Kelvin theorems | Relativistic vorticity 2-form, Kelvin circulation theorem in SR/GR |
| 21 (rel) | Equations in rotating frame | Born coordinates, relativistic Coriolis/centrifugal, Lense-Thirring analogy |
| 22 (rel) | Taylor--Proudman theorem | Relativistic version with enthalpy corrections |
| 23 (rel) | Wave propagation | Relativistic inertial waves, Israel-Stewart dispersion relation, causality checks |

### Key relativistic features introduced

1. **Relativistic vorticity**: omega_{mu nu} = nabla_mu(h u_nu) - nabla_nu(h u_mu), with specific enthalpy h = (epsilon+p)/(rho_0 c^2).
2. **Kelvin's theorem**: dGamma/dtau = 0 for barotropic perfect fluid, with circulation defined using h u_mu.
3. **Inertial mass density**: (epsilon+p)/c^2 replaces rho in all force-balance equations.
4. **Light-cylinder constraint**: r < c/Omega limits rigid rotation; centrifugal potential becomes logarithmic.
5. **Israel-Stewart viscosity**: Converts parabolic diffusion to hyperbolic, ensuring causal wave propagation.
6. **Causality verification**: All wave modes have phase and group velocities bounded by c.
7. **Non-relativistic limits**: Every result reduces exactly to the corresponding Chandrasekhar equation.

### Conventions followed

- Metric signature (-,+,+,+), c kept explicit
- Macros from rel_preamble.tex used throughout
- causalitycheck and relcorrection environments used for highlighting

## Issues / Notes

- The inviscid inertial-wave frequency is identical to the classical result (independent of c), since the Coriolis restoring force does not involve c.
- Frame-dragging (Lense-Thirring) is discussed qualitatively for GR context but full GR rotating-frame equations are deferred to a dedicated GR chapter.
- The Israel-Stewart crossover wavenumber k_IS provides a natural UV cutoff for the viscous mode.

## Next

- Integration with other relativistic chapter files (rel_chapter_3 assembly)
- Sections 24--36 (thermal instability with rotation) to be handled by subsequent agents
