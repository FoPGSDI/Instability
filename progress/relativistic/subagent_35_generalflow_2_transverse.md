---
agent: 35
chapter: 8
section: 77-78
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created relativistic extension of Chapter VIII §§77-78: stability of viscous
flow between rotating cylinders with a transverse pressure gradient.

### Content produced

File: `output/chapters/relativistic/rel_chapter_8_sec77-78.tex`

**§77 — Transverse pressure gradient with rotation (relativistic):**
- Relativistic base flow formulation with enthalpy-density inertia
- Perturbation equations for narrow gap: Israel-Stewart causal viscous operator
  replaces classical diffusion operator; relativistic Taylor number
  Ta_rel = T/(1+Xi)^2
- Characteristic value problem at sigma=0: operator structure identical to
  classical case; critical wave number unchanged; T_c scales as (1+Xi)^2
- Physical interpretation: pressure contribution to inertia stabilizes against
  centrifugal instability; all three lambda-regimes preserved
- Comparison with experiments: corrections negligible for lab fluids (Xi ~ 10^-10);
  relevant for neutron stars (Xi ~ 0.1-0.3), QGP, accretion discs

**§78 — Inviscid flow with axial pressure gradient (relativistic):**
- Relativistic Rayleigh discriminant with (1+Xi)^-2 prefactor
- Howard-Gupta semi-circle theorem generalization

**Causality check:**
- Viscous signal speed bounded by c via Israel-Stewart tau_pi bound
- Marginal stability (sigma=0) is elliptic — no propagation issues
- All characteristic speeds (viscous, sound, rotation, transverse flow) < c
- Non-relativistic limit recovers classical equations exactly

## Issues / Notes

- The exchange-of-stabilities principle is not established for this problem,
  even classically. The sigma=0 assumption is based on experimental evidence.
- At marginal stability, the Israel-Stewart correction vanishes identically,
  so the only relativistic effect is the (1+Xi)^2 rescaling of T_c.

## Next

No further sub-tasks required for this section.
