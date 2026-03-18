# Agent 14: BDNK Conversion - rel_chapter_3_sec29-31.tex (Overstability)

## Status: COMPLETE

## Key Change: IS quintic -> BDNK cubic dispersion relation
- IS theory: 5th-order polynomial (3 physical + 2 spurious relaxation modes)
- BDNK theory: 3rd-order polynomial (3 physical modes only, no spurious modes)
- This is the most significant simplification in the BDNK conversion

## Changes Applied
- Replaced IS relaxation equations (tau_q, tau_pi) with BDNK first-order constitutive relations
- Replaced sigma -> sigma/(1+tau_q*sigma) substitution with identity (no frequency-dependent replacement)
- Changed quintic P_5(sigma) to cubic P_3(sigma) throughout
- Updated classical limit discussion (no factorization of spurious modes needed)
- Updated summary table: dispersion degree 3 (not 5), 0 relaxation modes (not 2)
- Replaced IS causality check (v_th = sqrt(kappa/(tau_q*c_v*rho))) with BDNK frame inequalities
- Updated variational principle: IS -> BDNK modifications

## Key Physics Preserved
- 3 physical hydrodynamic modes unchanged
- Overstability conditions qualitatively unchanged
- Critical Prandtl number p* at leading order unchanged (0.67659)
- T^{2/3} and T^{1/2} scaling laws preserved
- Boundary conditions unchanged
