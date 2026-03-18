---
agent: 52
chapter: 12
sections: 107-109
task: Relativistic gravitational cylinder instability
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_12_sec107-109.tex` containing the
relativistic generalization of Chapter XII, sections 107--109 (gravitational instability
of an infinite cylinder).

### Section 107: Introduction — Relativistic jets and cylinders
- Motivation from AGN jets (bulk Lorentz factors 10--50), cosmic strings (deficit-angle
  gravity), and GRB jets
- Key physical differences from Newtonian theory: finite gravitational signal speed,
  inertia of energy and pressure, causal dissipation (Israel--Stewart)
- Introduced compactness parameter C = pi G rho_0 R^2 / c^2

### Section 108: Gravitational instability of relativistic infinite cylinder
- **Equilibrium**: 1PN equilibrium pressure with energy/pressure corrections
- **Self-gravity**: Poisson equation replaced by linearized Einstein equation with wave
  operator term (sigma^2/c^2) giving Helmholtz equation; modified wavenumber
  k_tilde^2 = k^2 + sigma^2/c^2
- **Dispersion relation**: Implicit equation with modified Bessel functions of argument
  k_tilde R; effective gravitating density rho_0* includes (eps + 3p)/(2 rho_0 c^2)
- **Characteristic frequencies**: 1PN corrections factored into enhanced gravitating mass
  (destabilizing) and retardation from finite signal speed (stabilizing)
- **Critical wavenumber**: x_a = 1.0668 unchanged (marginal modes are static)
- **Mode of maximum instability**: shifted to longer wavelengths by retardation
- **Energy principle in GR**: Friedman--Schutz canonical energy functional; relativistic
  Lagrangian with enthalpy w replacing rho_0 reproduces dispersion relation
- **Non-axisymmetric modes**: stable (sigma_m^2 < 0 for m != 0), unchanged from Newtonian

### Section 109: Viscosity effects — Israel--Stewart on cylindrical instability
- **Causal viscosity**: Israel--Stewart relaxation equation for shear stress with
  relaxation time tau_pi > 0; effective viscosity nu_eff = nu/(1 + tau_pi sigma)
- **Dominant viscosity case**: quadratic equation for sigma; Newtonian limit recovered as
  tau_pi -> 0; large tau_pi gives intermediate scaling sigma ~ 1/sqrt(nu tau_pi)
- **General case**: full characteristic equation with rho_0 -> rho_0*, nu -> nu_eff;
  relativistic viscous parameter J* = J(rho_0*/rho_0); Israel--Stewart parameter
  T = tau_pi nu / R^2
- **Causality**: growth rate bounded by c/R in all regimes; viscous signal speed < c

### CAUSALITY treatment
- Gravitational signal speed = c throughout (wave equation replaces Poisson equation)
- Viscous signal speed = sqrt(eta_s / (w tau_pi)) < c (Israel--Stewart)
- Growth rate bounded: sigma < c/R (post-Newtonian regime); sigma saturates for
  ultracompact cylinders

## Conventions
- Metric signature (-,+,+,+), c and G explicit
- All notation per RELATIVISTIC_CONVENTIONS.md
- LaTeX macros: \Lf, \enthalpy, \taupi, \shearvisc, \covd, \emt, etc.

## Issues / Notes
- The 1PN expansion coefficients alpha, beta in eqs (17)--(18) are left as positive
  constants; their numerical evaluation requires solving the implicit dispersion relation
  numerically.
- For ultracompact cylinders (C ~ 1), the post-Newtonian framework breaks down and
  full numerical relativity is needed.
- The incompressibility assumption is maintained for direct comparison with the original
  Chandrasekhar treatment; a compressible relativistic treatment would additionally
  involve the sound speed c_s.

## Next
- Sections 110--112 (magnetic field effects, capillary instability) can be relativistically
  generalized following the same post-Newtonian + Israel--Stewart framework.
