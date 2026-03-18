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
- [VALIDATED] 2508.04918 "Acausality instabilities" → rel_chapter_10, rel_chapter_11
- [VALIDATED] 2508.08936 "Charge separation in accelerating plasmas" → rel_chapter_10 §98-99, rel_chapter_11 §105-106, rel_framework_thermo

### Jets and gravitational (Ch XII-XIV)
- [VALIDATED] 2507.19985 "Superflows in GR" → rel_chapter_12 §113-115
- [VALIDATED] 2305.04119 "Bulk rheology: NS mergers to cosmology" → rel_chapter_13 §119
- [VALIDATED] 2304.05455 "Burgers-type bulk viscosity in NS" → rel_chapter_12 §110, rel_chapter_13 §119
- [VALIDATED] 2504.20332 "Solitons in ultrastiff fluids" → rel_chapter_14 §123

### Neutron star specific
- [VALIDATED] 2012.10288 "Superfluid dynamics in NS crusts" → rel_chapter_6 §60 (crust convection)
- [VALIDATED] 2204.11809/10 "Simulating bulk viscosity in NS" → rel_chapter_7 §72-73, rel_chapter_12 §110
- [VALIDATED] 2001.08951 "Mutual friction coupling" → rel_chapter_3 §19-23

## Batch 3 Status: COMPLETE — 8 papers integrated (2003.04609, 2304.05455, 2305.04119, 2501.12543, 2204.11809, 2204.11810, 2012.10288, 2001.08951)

## Batch 4 Integration Status (Heat, Radiation, Thermodynamics)

### Completed Integrations
- [VALIDATED] 2312.13553 "Large-flux heat" → rel_chapter_2_sec5-9: new §"Nonlinear Heat Conduction in the Large-Flux Regime"
- [VALIDATED] 2509.00198 "Rotating heat" → rel_chapter_3_sec19-23: new §"Heat Propagation in Rotating Relativistic Bodies"
- [VALIDATED] 2412.00275 "Radiation hydro dispersion" → rel_chapter_6_sec55-56: new §"Radiation Hydrodynamic Dispersion Relations"
- [VALIDATED] 2502.08740 "Causality in radiative transfer" → rel_framework_thermo: new §"Causality Constraints on Radiative Transfer"
- [VALIDATED] 2005.06396 "Zeroth law" → rel_framework_thermo: new §"The Zeroth Law and Tolman-Ehrenfest Equilibrium"
- [VALIDATED] 2105.15184 "Unified EIT" → rel_framework_hydro: new §"Unified Extended Irreversible Thermodynamics and Stability"
- [VALIDATED] 2111.05254 "Dissipation without causality" → rel_framework_hydro: subsection on frame-dependent stability
- [VALIDATED] 2209.12865 "GENERIC or EIT" → rel_framework_hydro: subsection on GENERIC-IS equivalence

## Batch 4 Status: COMPLETE — 8 papers integrated (2312.13553, 2509.00198, 2412.00275, 2502.08740, 2005.06396, 2105.15184, 2111.05254, 2209.12865)

## Batch 5 Integration (Couette Flows, Kinetic Theory, Recent Papers)

- [VALIDATED] 2512.10420 "Stationary Couette flows" → rel_chapter_7_sec64-66: new section with exact velocity profile, temperature, Landau frame, implications for perturbation analysis
- [VALIDATED] 2309.14828 "Regime of applicability of IS" → rel_framework_hydro: new section ranking IS truncations (IReD > DNMR > 2ndOH > 14-moment)
- [VALIDATED] 2402.19343 "Infinite order hydrodynamics" → rel_framework_hydro: gradient expansion divergence, UV cutoff regularization, Kn~0.1 breakdown
- [VALIDATED] 2408.14316 "Convergence of hydro gradient expansion" → rel_framework_hydro: convergence theorem with gap, R_shear >= 1/(2 tau_g)
- [VALIDATED] 2404.12327 "Gapless non-hydro modes" → rel_chapter_2_sec10-12: gapless criteria, implications for normal-mode analysis and exchange of stabilities
- [VALIDATED] 2405.10878 "Stochastic fluctuations in kinetic theory" → rel_framework_hydro: covariant fluctuating kinetic theory, IS captures 80% of fluctuations
- [VALIDATED] 2307.11615 "Multicomponent IS-Maxwell stability" → rel_chapter_9_sec81-83: multicomponent stability conditions, EM sector automatic, Carter connection
- [VALIDATED] 2202.06760 "Stability of Carter's multifluid" → rel_chapter_6_sec60: entrainment matrix positivity, stability implies causality

## Batch 5 Status: COMPLETE — 8 papers integrated (2512.10420, 2309.14828, 2402.19343, 2408.14316, 2404.12327, 2405.10878, 2307.11615, 2202.06760)

## Batch 6 Integration (Remaining Gavassino Papers)

- [VALIDATED] 2507.19985 "Superflows in GR" → rel_chapter_12_sec113-115: new §"Jet stability viewed as a superflow problem"
- [VALIDATED] 2506.19786 "Perfect spinfluid" → rel_framework_hydro: new §"Spin Hydrodynamics: The Perfect Spinfluid"
- [VALIDATED] 2504.20332 "Solitons in ultrastiff fluids" → rel_chapter_14_sec123: new §"Solitonic waves and singularity formation"
- [VALIDATED] 2508.08936 "Charge separation" → rel_chapter_10_sec98-99, rel_chapter_11_sec105-106, rel_framework_thermo
- [VALIDATED] 2509.23845 "Thermoelectric conduction" → rel_framework_thermo: new §"Relativistic Thermoelectricity"
- [VALIDATED] 2511.14344 "Plasma oscillations within IS" → rel_chapter_9_sec87-89: new §"Plasma oscillations and non-hydro modes"
- [VALIDATED] 2311.10897 "GENERIC to Carter" → rel_framework_hydro: new §"GENERIC-Carter Correspondence"
- [VALIDATED] 1906.03140 "Multifluid thermo" → rel_framework_thermo: multifluid thermo underpinning

## Batch 6 Status: COMPLETE — 8 papers integrated (2507.19985, 2506.19786, 2504.20332, 2508.08936, 2509.23845, 2511.14344, 2311.10897, 1906.03140)
