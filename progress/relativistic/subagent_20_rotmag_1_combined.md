---
agent: 20
chapter: 5
sections: 49-50
task: Relativistic rotation + magnetic field combined effects
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_5_sec49-50.tex` containing
the relativistic extension of Chapter V, Sections 49--50.

### Section 49: Like and contrary effects — relativistic analysis
- Explained how the enthalpy density w = epsilon + p replaces rho as the
  inertial mass, weakening both rotational and magnetic stabilisation in
  hot fluids.
- Derived relativistic Taylor number Ta_rel and Chandrasekhar number Q_rel.
- Showed that the ratio Q/Ta is corrected only at O(v^4/c^4), so the
  qualitative competition is robust against leading relativistic corrections.
- Discussed how p/c^2 terms interact with Omega and B.

### Section 50: Hydromagnetic waves — relativistic dispersion
- Derived linearised relativistic MHD + Coriolis equations in co-rotating frame.
- Obtained incompressible relativistic dispersion relation (eq. rel50-dispersion),
  formally identical to classical eq. (16) with v_A replaced by relativistic value.
- Derived full compressible dispersion relation (cubic in omega^2) combining
  Alfven, inertial, and acoustic modes: omega(k, theta, phi, Omega, v_A, c_s, c).
- Identified all limiting cases:
  (a) Omega=0: standard relativistic MHD fast/slow/Alfven modes
  (b) v_A=0: inertial-acoustic mode
  (c) c_s -> c: incompressible (causal) limit
  (d) c -> infinity: classical Chandrasekhar result
  (e) B || Omega: aligned magneto-inertial modes
- CAUSALITY VERIFIED: group velocity <= c for all branches via
  v_f^2 = c_s^2 + v_A^2 - c_s^2 v_A^2/c^2 < c^2, proved algebraically.

## Conventions
- Metric signature (-,+,+,+), c explicit, u^mu u_mu = -c^2
- Uses macros from rel_preamble.tex
- All non-relativistic limits verified by c -> infinity

## Files
- `output/chapters/relativistic/rel_chapter_5_sec49-50.tex` (new)
- `progress/relativistic/subagent_20_rotmag_1_combined.md` (this file)
