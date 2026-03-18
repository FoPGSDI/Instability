# Gavassino Integration Batch 4: Heat, Radiation, Thermodynamics

## Papers Integrated (8 total)

| # | arXiv ID | Title | Target | Status |
|---|----------|-------|--------|--------|
| 25 | 2312.13553 | Large-flux heat conduction | Ch II sec5-9 | VALIDATED |
| 26 | 2509.00198 | Heat in rotating bodies | Ch III sec19-23 | VALIDATED |
| 27 | 2412.00275 | Radiation hydro dispersion | Ch VI sec55-56 | VALIDATED |
| 28 | 2502.08740 | Causality in radiative transfer | Framework thermo | VALIDATED |
| 29 | 2005.06396 | Zeroth law in SR | Framework thermo | VALIDATED |
| 30 | 2105.15184 | Unified EIT and stability | Framework hydro | VALIDATED |
| 31 | 2111.05254 | Dissipation without causality | Framework hydro | VALIDATED |
| 32 | 2209.12865 | GENERIC or EIT | Framework hydro | VALIDATED |

## Key Integration Details

### Paper 25 (2312.13553) → Ch II §5-9
- Added new section "Nonlinear Heat Conduction in the Large-Flux Regime"
- Key physics: GENERIC-Multifluid theory for non-perturbative heat flux
- Equations: Non-equilibrium free energy, anisotropic stress-energy tensor, nonlinear heat equation
- Minerbo and Levermore flux-limited diffusion closures
- Applications to NS surfaces, proto-NS cooling, QGP

### Paper 26 (2509.00198) → Ch III §19-23
- Added new section "Heat Propagation in Rotating Relativistic Bodies"
- KEY RESULT: Unique causal heat equation for Born-rigid rotation: u^mu nabla_mu(KT) = (1/nc_v) nabla_mu[kappa nabla^mu(KT)]
- Tolman-Ehrenfest condition KT = const derived from rigidity + energy conservation
- Hyperbolicity proven (principal part is wave operator)
- Applications to NS cooling with rotation corrections

### Paper 27 (2412.00275) → Ch VI §55-56
- Added section on radiation hydro dispersion relations
- Exact dispersion relations for shear, heat, and sound waves in matter+radiation fluids
- Key formulas: omega(k) involving arctan(k*tau) interpolating diffusive/free-streaming
- Implications for convective spectrum truncation at high spherical harmonics

### Paper 28 (2502.08740) → Framework thermo
- Added subsection "Causality Constraints on Radiative Transfer"
- Shows Spiegel's classic formula for radiative smoothing is UNSTABLE under Lorentz boosts
- Exact solution falls inside the "hydrohedron" of Heller et al.
- Direct relevance to thermal conductivity in Rayleigh number calculations

### Paper 29 (2005.06396) → Framework thermo
- Added subsection "The Zeroth Law and Tolman-Ehrenfest Equilibrium"
- Resolves Planck-Ott controversy: thermal equilibrium requires co-moving + same T
- Covariant equation of state S = S(M, Q_A, W^2)
- Temperature is a Lorentz scalar defined in rest frame
- Tolman-Ehrenfest law T*sqrt(-xi_mu*xi^mu) = const

### Paper 30 (2105.15184) → Framework hydro
- Added section "Unified Extended Irreversible Thermodynamics and Stability"
- UEIT encompasses IS, Carter, BDNK, radiation hydro
- Lyapunov stability follows from second law of thermodynamics
- Explains why Eckart/Landau are unstable (slow limit breaks hyperbolicity)

### Paper 31 (2111.05254) → Framework hydro
- Integrated into UEIT section as subsection on frame-dependent stability
- Two theorems: (1) causal+stable in one frame => stable in all; (2) acausal+dissipative => unstable in some frame
- 14 applications to physical problems
- Validates BDNK as automatically stable in all frames

### Paper 32 (2209.12865) → Framework hydro
- Integrated as subsection "GENERIC Theory and Israel-Stewart: The Equivalence"
- GENERIC linearized = constrained IS theory
- Describes viscoelastic liquid behavior (Maxwell model)
- Physical predictions identical in linear regime

## Files Modified
- output/chapters/relativistic/rel_chapter_2_sec5-9.tex
- output/chapters/relativistic/rel_chapter_3_sec19-23.tex
- output/chapters/relativistic/rel_chapter_6_sec55-56.tex
- output/chapters/relativistic/rel_framework_thermo.tex
- output/chapters/relativistic/rel_framework_hydro.tex
- SHARED_REFERENCES.bib (8 new entries)
- RESEARCH_NOTE_LG.md (updated status)

## BibTeX Keys Added
- GavassinoLargeFlux2024
- GavassinoRotatingHeat2025
- GavassinoRadDispersion2025
- GavassinoCausalRadTransfer2025
- GavassinoZerothLaw2020
- GavassinoUEIT2021
- GavassinoDissipationCausality2021
- GavassinoGENERIC2023
