---
agent: 40
chapter: 9
sections: 87-89
status: completed
timestamp: 2026-03-18T12:00:00Z
task: Relativistic dissipative Couette MHD
---

## Summary

Created `output/chapters/relativistic/rel_chapter_9_sec87-89.tex` containing the
relativistic extension of Chandrasekhar's Ch IX sections 85--89 on dissipative
Couette flow in hydromagnetics.

## Content produced

### Section rel-87: Perturbation equations (relativistic Israel-Stewart + resistive MHD)
- Covariant equilibrium setup with 4-velocity and magnetic 4-vector
- Israel-Stewart relaxation equations for shear stress and heat flux
- Causal resistive Ohm's law with relaxation time tau_eta
- Full linearised perturbation equations with IS operators
- Viscous and resistive signal speed bounds (eqs rel-9-vvisc, rel-9-vres)
- Normal mode decomposition yielding relativistic eigenvalue system
- Boundary conditions: conducting and non-conducting walls (unchanged in form)
- Marginal state equations with Q_rel replacing Q
- Narrow-gap reduction yielding relativistic Taylor number Ta_rel

### Section rel-88: Solutions for mu > 0
- Variational principle (relativistic): positive-definite functional identical
  in structure to classical, with Q -> Q_rel
- Secular determinant via Harris-Reid function expansion
- Non-conducting walls: integration constants
- Conducting walls: integration constants
- Numerical results: critical Ta(Q) with relativistic corrections tabulated
- Fractional shift formula for weakly relativistic regime
- Asymptotic Q -> infinity behaviour: same proportionality constants (107.2, 451.2)
  but expressed in terms of Q_rel

### Section rel-89: General case (mu arbitrary)
- Mixed C/S Harris-Reid expansion for broken parity symmetry
- Case mu = -1 (counter-rotating): secular equations
- Asymptotic behaviours for counter-rotation (726Q, 6203Q)

### Causality analysis
- Viscous sector: tau_pi >= eta_s / (w c^2)
- Resistive sector: tau_eta >= eta / c^2
- Relativistic Alfven speed automatically subluminal
- Mode counting: order 8 -> 12 dispersion relation with 4 transient IS modes
- Stationary onset formally identical to classical; new physics in oscillatory modes

## Key design decisions

1. At marginal stability (p=0), IS operators reduce to identity, so classical
   eigenvalue problem structure is preserved with parametric reinterpretation.
2. Relativistic corrections enter through: (a) enthalpy w replacing density rho,
   (b) Alfven inertia factor A = 1 + b^2/(4pi w c^2), (c) relativistic Taylor number.
3. All classical tables/numerical results apply with Q -> Q_rel, T -> Ta_rel.
4. Causality is ensured by finite relaxation times in both viscous and resistive sectors.

## Files created
- `output/chapters/relativistic/rel_chapter_9_sec87-89.tex`
- `progress/relativistic/subagent_40_couettemhd_3_dissipative.md` (this file)
