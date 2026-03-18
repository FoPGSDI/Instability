---
agent: 16
chapter: 4
sections: 36-40
task: Relativistic hydromagnetic equations
status: completed
timestamp: 2026-03-18T12:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_4_sec36-40.tex` containing the
relativistic generalisation of Chapter IV, sections 36--40 (hydromagnetic equations,
Alfven waves, and special solutions).

### Content produced

- **Section 36 (rel):** Motivation for relativistic MHD; key qualitative changes
  (enthalpy-based inertia, automatic sub-luminality).
- **Section 37 (rel):** Full covariant Maxwell equations (eqs rel4-1, rel4-2);
  electromagnetic decomposition into fluid-frame e^mu, b^mu; ideal MHD condition
  F^{mu nu} u_nu = 0; total energy-momentum tensor T^{mu nu} = T_fluid + T_EM
  (eq rel4-11, boxed); relativistic Euler equation (eq rel4-16) with explicit
  non-relativistic limit verification.
- **Section 38 (rel):** Relativistic induction equation (eq rel4-17, boxed);
  relativistic Ohm's law with finite conductivity and Joule dissipation rate
  (eqs rel4-18, rel4-19); relativistic Alfven theorem -- flux freezing
  d Phi/d tau = 0 (eq rel4-21, boxed); transport equation for b^mu / rho_0.
- **Section 39 (rel):** Alfven wave dispersion omega^2 = v_A^2 k^2 cos^2 theta
  (eq rel4-23); relativistic Alfven speed v_A (eq rel4-24) with explicit proof
  that v_A < c always (eq rel4-26); fast/slow magnetosonic speeds (eq rel4-27)
  with proof v_f < c (eq rel4-28); damped waves with finite viscosity/resistivity
  (eq rel4-29, rel4-30); Israel-Stewart causal dissipation note.
- **Section 40 (rel):** Relativistic equipartition solution; force-free fields
  with covariant Beltrami condition; Taylor-Proudman analogue (eq rel4-37).

### Causality verification

All three MHD characteristic speeds verified sub-luminal:
- Alfven: v_A^2 = (b^2/4pi)/(eps+p+b^2/4pi) < c^2 (dominant energy condition)
- Fast magnetosonic: v_f^2 = c_s^2 + v_A^2(1 - c_s^2/c^2) < c^2
- Slow magnetosonic: v_s^2 = c_s^2 v_A^2 cos^2 theta / v_f^2 < v_f^2 < c^2

### Non-relativistic limits

Each major equation includes a `relcorrection` box showing recovery of the
corresponding Chandrasekhar equation in the limit eps -> rho c^2, p << rho c^2,
b^2 << rho c^2.

## Issues / Notes

- Uses macros from `rel_preamble.tex` (verified present in relativistic/ directory).
- Requires `tcolorbox` package for `causalitycheck` and `relcorrection` environments.
- The Israel-Stewart treatment of resistive MHD is noted but not developed in full
  detail; a complete treatment would require specifying the resistive relaxation
  time tau_eta.

## Next

File is ready for integration into `rel_main.tex` via `\input{rel_chapter_4_sec36-40}`.
