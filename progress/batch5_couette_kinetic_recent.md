# Batch 5: Couette Flows, Kinetic Theory, and Recent Papers

## Agent: Claude Opus 4.6 (1M context)
## Date: 2026-03-18
## Branch: rel-lg

## Papers Integrated

### Paper 33: 2512.10420 — Stationary Couette-type flows (Gavassino, Niekamp, Schlichting, Denicol)
- **Target**: Ch VII sec64-66 (new section at end)
- **Key results**: Exact velocity profile u(x) = tan[2x/L arctan(v/sqrt(1-v^2))]; inertia of heat modifies profile; IS relaxation vanishes for stationary planar flows; Landau frame deflection ~ Kn
- **Integration**: New section "Exact stationary Couette-type solutions" with subsections on setup, exact velocity, temperature profiles, implications for perturbation analysis

### Paper 34: 2309.14828 — Regime of applicability of IS (Wagner & Gavassino)
- **Target**: Framework hydro (new section)
- **Key results**: IReD > DNMR > 2nd-order > 14-moment in accuracy; IS is falsifiable; tau_Pi = sum(zeta_n tau_n)/sum(zeta_m) is optimal
- **Integration**: New section "Regime of Applicability of Israel-Stewart Theory" with ranking and criterion for book chapters

### Paper 35: 2402.19343 — Infinite order hydrodynamics (Gavassino)
- **Target**: Framework hydro (new section)
- **Key results**: Gradient series factorially divergent with (n+3)! growth; UV cutoff regularizes; breakdown at Kn~0.1 same as Navier-Stokes; odd-order truncations elliptic
- **Integration**: New section "Convergence and Divergence of the Hydrodynamic Gradient Expansion"

### Paper 36: 2408.14316 — Convergence of hydro gradient expansion (Gavassino)
- **Target**: Framework hydro (same section as paper 35)
- **Key results**: Finite gap implies convergent gradient expansion; R_shear >= 1/(2 tau_g); gap exists when total cross-section bounded below
- **Integration**: Subsection within gradient expansion section; formal theorem statement

### Paper 37: 2404.12327 — Gapless non-hydrodynamic modes (Gavassino)
- **Target**: Ch II sec10-12
- **Key results**: Four equivalent gaplessness criteria; QFT cross-sections vanishing at high E → gapless; 1/t power law decay of non-hydro perturbations
- **Integration**: New section "Gapless non-hydrodynamic modes and validity of normal-mode analysis"

### Paper 38: 2405.10878 — Stochastic fluctuations in kinetic theory (Rocha, Gavassino, Mullins)
- **Target**: Framework hydro
- **Key results**: Covariant fluctuating kinetic theory; molecular chaos breaks at N^{-1/2}; IS captures 80% of stress-energy fluctuations; dehydrodynamization at high energy
- **Integration**: Subsection in gradient expansion section

### Paper 39: 2307.11615 — Multicomponent IS-Maxwell stability (Gavassino & Shokri)
- **Target**: Ch IX sec81-83
- **Key results**: Information current for multicomponent IS; EM stability automatic for non-polarizable media; maps to Carter's multifluid
- **Integration**: New section "Stability of multicomponent Israel-Stewart-Maxwell theory"

### Paper 40: 2202.06760 — Stability of Carter's multifluid (Gavassino)
- **Target**: Ch VI sec60
- **Key results**: Entrainment matrix must be positive definite; stability implies causality; Lyapunov functional from Gibbs criterion
- **Integration**: New subsection "Stability of Carter's multifluid: the Gavassino theorem"

## Files Modified
- output/chapters/relativistic/rel_chapter_7_sec64-66.tex (major: ~120 lines added)
- output/chapters/relativistic/rel_framework_hydro.tex (major: ~130 lines added)
- output/chapters/relativistic/rel_chapter_2_sec10-12.tex (major: ~70 lines added)
- output/chapters/relativistic/rel_chapter_9_sec81-83.tex (major: ~70 lines added)
- output/chapters/relativistic/rel_chapter_6_sec60.tex (moderate: ~50 lines added)
- SHARED_REFERENCES.bib (8 new entries)
- RESEARCH_NOTE_LG.md (batch 5 status)

## Reflection
1. Paper 33 (Couette) was the crown jewel — direct relevance to Ch VII base state
2. The IS regime paper (34) provides the meta-criterion for the entire book
3. Papers 35-37 form a coherent trilogy on gradient expansion convergence/divergence
4. The multifluid papers (39-40) close the loop between IS and Carter formalisms
