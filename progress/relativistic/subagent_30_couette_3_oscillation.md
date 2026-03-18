---
agent: 30
chapter: 7
section: 68
task: Relativistic oscillation periods of rotating fluid column
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_7_sec68.tex` containing the
relativistic modification of Chapter VII, Section 68 (The periods of oscillation
of a rotating column of liquid).

### Content produced

1. **Relativistic perturbation equations**: Derived the relativistic analogues of
   the classical equations (7-83)--(7-84) with Lorentz-factor corrections to
   the Doppler-shifted frequency and Rayleigh discriminant. The enthalpy density
   w = epsilon + p replaces the rest-mass density as the effective inertia.

2. **Case Omega = constant (relativistic inertial oscillations)**:
   - Relativistic discriminant: Phi_rel = 4 Omega^2 gamma^4 (1 + r^2 Omega^2/c^2)
   - Dispersion relation for eta=0: p/Omega = +/- 2/sqrt(1 + alpha^2/a^2) *
     1/(1 + 2 r_bar^2 Omega^2/c^2) - m
   - For m=0: p = +/- 2Omega/sqrt(1+alpha_{0,j}^2/a^2) / (1+2r_bar^2 Omega^2/c^2)
   - Bessel-function eigenmode structure preserved; eigenvalues unchanged
   - Net effect: frequency REDUCTION due to enhanced relativistic inertia

3. **Case Omega = A + B/r^4, m=0 (relativistic modification)**:
   - Narrow gap: lambda -> lambda_rel = lambda * gamma_0^4 [1 + O(r_bar^2 Omega_1^2/c^2)]
   - Airy-function structure and (x2,x1)-relation preserved with lambda_rel
   - For mu=1: explicit boxed formula for relativistic frequency
   - Wide gap: perturbative correction to cylinder-function solutions

4. **Relativistic epicyclic oscillations and QPOs**:
   - Connected column oscillation modes to epicyclic frequencies in GR
   - Schwarzschild radial epicyclic: kappa_r^2 = Omega_K^2 (1 - 6r_g/r)
   - Vanishing of kappa_r at ISCO (r = 6r_g): no classical analogue
   - Maximum QPO frequency: ~2198 Hz / (M/M_sun)
   - Link between Couette deviations and trapped disk oscillation modes

5. **Causality verification**:
   - Phase speed bound v_ph = |p|/k <= c verified for constant Omega
   - Group velocity v_g < c follows from dispersion relation
   - Israel-Stewart framework guarantees hyperbolicity for general profiles
   - Constraint reduces to v_rot < c for inviscid, adiabatic perturbations

### Design decisions

- Used leading-order v^2/c^2 expansion throughout, consistent with other
  relativistic sections in the project
- Kept Bessel-function eigenvalue structure from classical theory unchanged at
  leading order; relativistic corrections enter multiplicatively
- Connected the column modes to astrophysical epicyclic oscillations (QPOs) as
  the natural physical application of the relativistic extension
- Used relcorrection and causalitycheck environments from rel_preamble.tex

## Issues / Notes

- The wide-gap solution requires numerical treatment for exact relativistic
  corrections due to the r-dependent Lorentz factor
- For Kerr spacetimes (spinning black holes), the epicyclic frequencies have
  additional frame-dragging corrections not treated here
- The connection to QPOs is at the level of individual particle orbits;
  collective fluid modes in relativistic disks require full GR MHD treatment

## Next

This section can be integrated into a full relativistic Chapter VII by including
it via `\input{rel_chapter_7_sec68}` in the appropriate location.
