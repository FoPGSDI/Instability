---
agent: 21
chapter: 5
sections: 51-52
task: Relativistic rotation+B perturbations and stationary convection
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_5_sec51-52.tex`, the
relativistic generalization of Chandrasekhar Chapter V, sections 51--52
(perturbation equations with rotation + magnetic field, and stationary
convection).

## Content produced

### Section 51 — Relativistic perturbation equations
- Background state with covariant rotating frame and magnetic 4-vector
- Full linearized relativistic MHD momentum equation in rotating frame,
  with enthalpy density w* replacing rho as inertial mass
- Relativistic induction equation with O(v_A^2/c^2) corrections
- Israel-Stewart causal energy equation (telegraph equation for heat)
- Vorticity and double-curl equations (z-components)
- Normal mode decomposition: 5-equation system (eqs rel51-35 to rel51-39)
- Relativistic dimensionless parameters: Ra_rel, Ta_rel, Q_rel
- Master equation (rel51-master) — same form as Chandrasekhar (43) with
  relativistic parameters and Israel-Stewart thermal term
- Causality check on all mode families

### Section 52 — Stationary convection (sigma = 0)
- Marginal equations at sigma = 0 (Israel-Stewart term drops out)
- Two free boundaries: sinusoidal solutions yield characteristic equation
  (rel52-57) — identical functional form to Chandrasekhar (57) with
  relativistic parameters
- Explicit relation R_{c,rel} to R_{c,classical} via w*/rho_0 factor
- Competition/cooperation of rotation and magnetic field in relativistic
  regime: field relieves rotational inhibition, but both effects are
  reduced by enhanced inertia
- Two-minimum phenomenon persists; transition Q shifted by rho_0/w*
- Modified stability boundaries summarized
- Non-relativistic limit verified: all equations reduce to Chandrasekhar

## Conventions followed
- Metric (-,+,+,+), c explicit, u^mu u_mu = -c^2
- All macros from rel_preamble.tex used consistently
- causalitycheck and relcorrection tcolorbox environments used
- Six mode families checked for causality: thermal, Alfven, fast/slow
  magnetosonic, inertial, viscous

## Issues / Notes
- The Israel-Stewart relaxation term has no effect on stationary
  convection (sigma=0), only on overstability (to be treated in §53)
- The functional form of R_c(T,Q) is preserved; only the definitions
  of the dimensionless parameters change
- The two-minimum phenomenon (discontinuous jump in cell size) persists
  with shifted transition point
