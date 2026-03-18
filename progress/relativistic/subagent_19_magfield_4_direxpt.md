---
agent: 19
chapter: 4
sections: 47-48
task: Relativistic H-g directions and experiments
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_4_sec47-48.tex` containing
the relativistic extension of Ch IV sections 47 and 48.

### Section 47: H and g in different directions -- relativistic treatment
- Relativistic field decomposition using the magnetic four-vector b^mu
- Non-aligned field/gravity coupling terms through O(v_A^2/c^2):
  - Telegrapher correction to induction equation
  - Magnetic tension and Poynting-flux momentum corrections to momentum equation
  - Israel-Stewart causal heat equation replacing Fourier diffusion
- Modified stability criteria:
  - Relativistic Chandrasekhar number Q_rel = Q_class (1 + v_A^2/c^2)^{-1}
  - Longitudinal-roll selection theorem carries over unchanged
  - New overstable mode frequency shift at O(v_A^2/c^2)
- Variational principle generalised with Q -> Q_rel
- Quantitative estimates table (lab mercury to magnetar cores)

### Section 48: Experiments and astrophysical observations
- Laboratory (mercury): corrections ~10^{-20}, completely negligible
- Magnetar interiors (B ~ 10^{15}-10^{16} G): corrections 1-10%, physically significant
  - Convective instability threshold lowered
  - Longitudinal roll patterns follow local field geometry
  - Testable via QPO signatures after giant flares
- Accretion disk coronae (B ~ 10^{7}-10^{8} G): corrections ~1%
  - Overstable mode frequency shift imprinted on X-ray variability

### Relativistic bibliographical notes
- 12 references covering relativistic MHD (Anile, Lichnerowicz),
  Israel-Stewart causality, neutron star physics, magnetar fields,
  and accretion disk GRMHD

## Conventions
- (-,+,+,+) metric signature, c kept explicit
- All macros from rel_preamble.tex used consistently
- Causality verification box and relativistic correction boxes included
- Non-relativistic limits verified for all new equations

## Files Created
- `output/chapters/relativistic/rel_chapter_4_sec47-48.tex`
- `progress/relativistic/subagent_19_magfield_4_direxpt.md`
