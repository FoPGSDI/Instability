---
agent: 22
chapter: 5
sections: 53-54
task: Relativistic overstability with rotation+B
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_5_sec53-54.tex` containing the
relativistic extension of Ch V sections 53-54 (overstability and experiments with
rotation + magnetic field).

### Section 53 — Relativistic overstability

- Linearised Israel-Stewart perturbation equations for heat flux, shear stress,
  and bulk viscosity in a rotating, magnetised layer.
- Frequency-dependent effective transport coefficients from IS relaxation,
  showing how causality is restored via finite propagation speeds.
- Full relativistic characteristic equation (analogue of Chandrasekhar's eq. 62),
  with relaxation-corrected Prandtl numbers p1_eff, p2_eff.
- Approximate solution for liquid metals: relativistic analogue of eqs. (70)-(71)
  with proper non-relativistic limit recovery.
- Mercury results: quantitative estimates showing all relativistic corrections
  are O(10^{-17}) or smaller under lab conditions, confirming classical results.
- Identification of regimes where corrections matter: hot dense plasmas,
  magnetar interiors, millisecond pulsars.

### Section 54 — Astrophysical applications

- Magnetar crusts: v_A/c ~ 0.1-0.3, significant Q_rel corrections, link to QPOs.
- Magnetised accretion disks: enthalpy coupling, causal heat transport,
  frame-dragging near Kerr black holes.
- Neutron-star oceans: gravitational redshift as the leading relativistic correction
  (~30% increase in effective Rayleigh number).

### Bibliographical notes

15 references spanning Israel-Stewart theory, relativistic MHD, magnetar QPOs,
accretion disk simulations, and neutron-star ocean convection.

## Issues / Notes

- No laboratory experiments exist that probe the relativistic regime of combined
  rotation+B convective instability; all applications are astrophysical.
- The Israel-Stewart relaxation corrections to overstability frequencies are
  formally derived but negligible for mercury; they become important only for
  relativistic plasma conditions.

## Next

File is self-contained and ready for inclusion in rel_main.tex.
