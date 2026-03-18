# Agents 28-33: BDNK Conversion -- Chapter VII (Couette Flow)

## Status: COMPLETE

## Files Modified
1. `output/chapters/relativistic/rel_chapter_7_sec64-66.tex` (Agent 28)
   - Replaced IS relaxation times tau_pi, tau_q in causality subsection with BDNK frame-coefficient constraints
   - Cited Bemfica2018, Kovtun2019

2. `output/chapters/relativistic/rel_chapter_7_sec67.tex` (Agent 29)
   - No changes needed: purely inviscid analysis, no IS references

3. `output/chapters/relativistic/rel_chapter_7_sec68.tex` (Agent 30)
   - Updated file header comment from IS to BDNK
   - Replaced IS causality check (taupi>0, tauq>0) with BDNK framework description
   - Cited Bemfica2018, Kovtun2019

4. `output/chapters/relativistic/rel_chapter_7_sec69-70.tex` (Agent 31) -- MAJOR CHANGES
   - Replaced IS energy-momentum tensor section with BDNK general-frame formulation
   - Replaced IS relaxation equation with BDNK first-order constitutive relation Pi^{mu nu} = -2 eta sigma^{mu nu}
   - Removed IS viscous signal speed; replaced with BDNK characteristic speed bound
   - Removed IS perturbation of shear stress section; replaced with BDNK constitutive perturbation
   - Removed frequency-dependent effective viscosity nu/(1+tau_pi p); BDNK uses plain nu
   - Simplified coupled perturbation equations (removed 1/(1+tau_pi p) factors)
   - Replaced IS oscillatory mode section with BDNK causality bounds
   - Updated summary section
   - At marginal state sigma=0: both IS and BDNK give identical eigenvalue problem (noted explicitly)

5. `output/chapters/relativistic/rel_chapter_7_sec71.tex` (Agent 32)
   - Updated file header comment
   - Replaced IS paragraph with BDNK framework paragraph
   - Noted sigma=0 equivalence of IS and BDNK
   - Cited Bemfica2018, Kovtun2019

6. `output/chapters/relativistic/rel_chapter_7_sec72-73.tex` (Agent 33)
   - Replaced IS framework description with BDNK
   - Simplified viscous operator: D^2-a^2-sigma (no taupi modification)
   - Simplified energy integrals (removed taupi factors)
   - Simplified exchange-of-stabilities proof (cleaner without taupi conditions)
   - Updated causality checks throughout
   - Updated mu<0 discussion
   - Noted IS/BDNK equivalence at sigma=0

## Key Conversion Principles Applied
- IS "frequency-dependent effective viscosity nu/(1+tau_pi sigma)" -> BDNK "nu with frame-dependent causality bounds"
- At marginal state sigma=0: both formulations identical (critical Taylor numbers unchanged)
- IS relaxation times (tau_pi, tau_q, tau_Pi) removed entirely; replaced by BDNK frame coefficients
- IS relaxation equations removed; replaced by first-order constitutive relations
- Dispersion relations simplified (no extra IS relaxation modes)
- Citations: Bemfica2018, Kovtun2019, Bemfica2019, HoultKovtun2020, BemficaDN2023
