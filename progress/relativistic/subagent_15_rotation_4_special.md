---
agent: 15
chapter: 3
sections: 32-35
task: Relativistic special cases (Pr=0, thermodynamics, Omega-g misalignment, experiments)
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_3_sec32-35.tex` containing
relativistic modifications to Chapter III, Sections 32--35.

### Section 32: The case Pr = 0 (relativistic)
- Extended to nuclear matter in neutron star interiors (Pr ~ 10^{-5}--10^{-3})
- Critical Rayleigh number acquires factor w/(rho_0 c^2) from relativistic enthalpy
- Oscillation frequency reduced by (rho_0 c^2 / w)^{1/2} (8--30% for neutron stars)
- Israel-Stewart causality constraint provides lower bound on heat relaxation time tau_q
- Causality check: Navier-Stokes Pr=0 limit violates causality; IS formalism resolves this

### Section 33: Thermodynamic significance (relativistic entropy production)
- Reformulated in terms of entropy current s^mu and Israel-Stewart dissipation
- Stationary case: minimum entropy production principle with enthalpy correction
- Oscillatory case: entropy balance with IS relaxation modifying effective thermal diffusivity
- New coupling between oscillation frequency sigma and relaxation time tau_q
- General thermodynamic principle restated in relativistic form

### Section 34: Omega and g in different directions (frame dragging)
- Lense-Thirring precession reduces effective rotation rate
- Taylor number correction: Omega -> Omega - omega_LT
- New gravitomagnetic tilt coupling: sin(theta) terms from frame dragging enter vorticity equation
- Quantified for millisecond pulsars: omega_LT/Omega ~ 0.01--0.1

### Section 35: Experiments -> Astrophysical observations
- Neutron star convection: QPOs, pulsar glitches, gravitational wave emission
- Accretion disk convection: CDAFs, GRMHD simulations, EHT observations
- Parameter tables for neutron star conditions

### Bibliographical notes
- 16 relativistic references (R1--R16) covering Israel-Stewart theory, nuclear transport,
  neutron star convection, frame dragging, accretion physics, QPOs, gravitational waves, EHT

## Conventions followed
- Metric signature (-,+,+,+), c kept explicit
- Macros from rel_preamble.tex used throughout (\Rarel, \Tarel, \enthalpy, \rdensity, etc.)
- relcorrection and causalitycheck tcolorbox environments used
- Non-relativistic limits verified for all key equations

## Issues / Notes
- All cross-references to original chapter_3.tex sections use \ref{sec:3-XX} labels
- Frame-dragging analysis uses Hartle slow-rotation approximation (valid for most pulsars)
- CDAF comparison with GRMHD simulations is qualitative; detailed numerical comparison awaits future work
