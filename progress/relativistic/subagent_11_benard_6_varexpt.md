---
agent: 11
chapter: 2
sections: 17-18
task: Relativistic variational solution and experiments
status: completed
timestamp: 2026-03-18T12:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_2_sec17-18.tex` containing
the relativistic extension of Chapter II, sections 17 and 18.

### Section 17 — Relativistic variational solution
- Extended the classical perturbation equations (277)–(278) with relativistic
  inertial corrections of order w/(rho_0 c^2) and Israel–Stewart causal
  heat-flux relaxation time tau_q.
- Trial functions and variational functional carry over from the classical
  analysis; the secular determinant has identical structure with Ra replaced
  by Ra_rel.
- Derived the relativistic correction factor Ra_rel/Ra = 1 + w/(rho_0 c^2)
  + c_s^2/c^2 + O(v^4/c^4).
- Provided numerical table comparing Ra_classical and Ra_rel across regimes
  from laboratory water (correction ~ 10^{-20}) to ultra-relativistic gas
  (correction factor 5/3).
- Verified causality: heat perturbations propagate at finite speed
  v_heat = sqrt(kappa_T / tau_q) <= c.

### Section 18 — Experimental considerations
- Laboratory experiments: relativistic corrections unmeasurably small
  (v/c ~ 10^{-10} at best for liquid metals).
- Astrophysical relevance:
  * Neutron star interiors: w/(rho_0 c^2) ~ 0.01–0.1, corrections 2–20%.
  * Accretion disks: radiation-dominated, c_s^2 = c^2/3, corrections O(1).
  * Early universe: ultra-relativistic EOS p = epsilon/3, Ra_rel/Ra = 5/3.
- Quark–gluon plasma: c_s^2 = c^2/3, shear viscosity near KSS bound,
  Israel–Stewart dynamics mandatory; correction factor ~ 5/3.
- Numerical simulations: validation of linear threshold, necessity of causal
  heat transport, pattern formation, shock formation in strongly nonlinear regime.
- Bibliographical notes: 13 references including Weinberg (1971), Israel &
  Stewart (1979), Rezzolla & Zanotti (2013), Romatschke & Romatschke (2019),
  Kovtun–Son–Starinets (2005), Eckart (1940), and others.

## Conventions
- Metric signature (−,+,+,+), c kept explicit
- All macros from rel_preamble.tex used consistently
- Causality verification boxes (causalitycheck environment) included
- Relativistic correction boxes (relcorrection environment) included
- Non-relativistic limit verified at each stage

## Next
File ready for integration into rel_main.tex via \input{rel_chapter_2_sec17-18}.
