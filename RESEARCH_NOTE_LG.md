# Research Notes — Gavassino Integration

## Central Goal
Integrate the theoretical framework and results of Lorenzo Gavassino's ~48 papers into our relativistic instability book, focusing on:

1. **Stability-causality connection**: Gavassino proved that thermodynamic stability implies causality. This is the foundational theorem our book should build on.
2. **Universality of hydro formulations**: BDNK and IS give identical physics in the linear regime (universality classes). Our book should present this equivalence.
3. **Acausality-driven instabilities**: IS formalism can produce nonlinear instabilities from acausality — this validates our choice of BDNK.
4. **Specific astrophysical calculations**: Couette flows, bulk viscosity in NS, superfluid dynamics.

## Paper-to-Chapter Mapping

### Framework chapters
- [VALIDATED] 2105.14621 "Stability implies causality" → rel_framework_hydro, rel_framework_thermo
- [VALIDATED] 2302.03478 "Universality classes: foundations" → rel_framework_hydro
- [VALIDATED] 2302.05332 "Universality classes: applications" → all chapters
- [HYPOTHESIS] 2109.06389 "Gauge theory of hydro" → rel_chapter_1
- [HYPOTHESIS] 2401.13852 "Information current" → rel_framework_hydro, rel_framework_thermo
- [HYPOTHESIS] 2210.05067 "Symmetric-hyperbolic" → rel_framework_hydro

### Thermal instability (Ch II-VI)
- [HYPOTHESIS] 2006.09843 "Entropy has no maximum" → rel_chapter_2 (exchange of stabilities)
- [HYPOTHESIS] 2104.09142 "Gibbs stability criterion" → rel_chapter_2 (variational)
- [HYPOTHESIS] 2312.13553 "Heat conduction large-flux" → rel_chapter_2 (Benard)
- [HYPOTHESIS] 2509.00198 "Heat in rotating bodies" → rel_chapter_3 (rotation)
- [HYPOTHESIS] 2412.00275 "Radiation hydro dispersion" → rel_chapter_6 (spheres)

### Flow stability (Ch VII-IX)
- [VALIDATED] 2512.10420 "Stationary Couette flows" → rel_chapter_7 (DIRECTLY relevant!)
- [VALIDATED] 2003.04609 "Bulk viscosity" → rel_chapter_7 §72-73, rel_chapter_9 §87-89
- [VALIDATED] 2501.12543 "Extending IS: causal bulk viscosity" → rel_chapter_8 §80, rel_chapter_9 §87-89

### Superposed fluids (Ch X-XI)
- [HYPOTHESIS] 2508.04918 "Acausality instabilities" → rel_chapter_10, rel_chapter_11

### Jets and gravitational (Ch XII-XIV)
- [HYPOTHESIS] 2507.19985 "Superflows in GR" → rel_chapter_12
- [VALIDATED] 2305.04119 "Bulk rheology: NS mergers to cosmology" → rel_chapter_13 §119
- [VALIDATED] 2304.05455 "Burgers-type bulk viscosity in NS" → rel_chapter_12 §110, rel_chapter_13 §119

### Neutron star specific
- [VALIDATED] 2012.10288 "Superfluid dynamics in NS crusts" → rel_chapter_6 §60 (crust convection)
- [VALIDATED] 2204.11809/10 "Simulating bulk viscosity in NS" → rel_chapter_7 §72-73, rel_chapter_12 §110
- [VALIDATED] 2001.08951 "Mutual friction coupling" → rel_chapter_3 §19-23

## Batch 3 Status: COMPLETE — 8 papers integrated (2003.04609, 2304.05455, 2305.04119, 2501.12543, 2204.11809, 2204.11810, 2012.10288, 2001.08951)
