---
agent: 18
chapter: 4
sections: 45-46
task: Relativistic Q-law and overstability
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_4_sec45-46.tex` containing
the relativistic generalisation of Chapter IV, sections 45 and 46.

### Section 45: The pi^2 Q-law and invariant — relativistic derivation

- Derived the pi^2 Q law in the relativistic framework where the enthalpy
  density w = epsilon + p replaces rho_0 as the effective inertia.
- Showed the inviscid perturbation equation has identical operator structure
  to the classical case, with Q_rel replacing Q.
- Physical origin: magnetic tension vs relativistic inertia (w_0/c^2).
- Critical temperature gradient modified by factor 1/h where h = w_0/(rho_0 c^2).
- Effective magnetic viscosity reduced by 1/h in relativistic regime.
- Relativistic invariant Psi = (1/2)(w_0/c^2) nu W_0^2, reducing to
  classical (1/2) rho_0 nu W_0^2 when h -> 1.

### Section 46: Overstability with magnetic field — relativistic treatment

- Derived the full relativistic characteristic equation including
  Israel-Stewart relaxation terms (tau_q, tau_pi, tau_Pi).
- Characteristic equation is 7th order in sigma_1 (vs 4th classically)
  due to three relaxation channels.
- Condition for overstability remains kappa < eta (unchanged by relativity).
- Transition Q^(tr) shifted to h^2 times classical value.
- Relativistic Prandtl and magnetic Prandtl numbers defined with factor h.
- Oscillation frequency governed by relativistic Alfven speed v_A < c.
- Comparison of classical vs relativistic critical curves provided.
- Israel-Stewart effects: frequency-dependent effective Prandtl numbers,
  possible suppression or promotion of overstability depending on tau_q/tau_pi.

### Causality

- Phase velocity of overstable modes shown to be subluminal:
  v_ph -> 0 as Q -> infinity (asymptotically safe).
- Explicit causality bound derived for finite Q.
- Israel-Stewart group velocity bounds verified.

### Non-relativistic limit

- All results reduce to classical equations (4-193)-(4-243) when c -> infinity.

## Files

- `output/chapters/relativistic/rel_chapter_4_sec45-46.tex` (new)
- `progress/relativistic/subagent_18_magfield_3_qlaw.md` (this file)

## Issues / Notes

- The seventh-order characteristic equation is written in implicit form
  via the IS correction factors T_q, T_pi, T_Pi. An explicit polynomial
  expansion is straightforward but lengthy.
- Under terrestrial conditions the causality bounds are never restrictive;
  they become relevant for neutron star envelopes and accretion discs.
