# Agent 9: BDNK Conversion - rel_chapter_2_sec15.tex (Exact Solutions)

## Status: COMPLETE

## Changes Applied
- Replaced IS causal heat transport with BDNK first-order heat transport
- Removed Upsilon = tau_q*kappa_T/d^2 parameter (no relaxation time in BDNK)
- Simplified R_rel = R/(1+Xi) instead of R/[(1+Xi)(1+Upsilon)]
- Updated all critical R_c formulas: removed (1+Upsilon) factor
- Updated table to show only (1+Xi) correction
- Replaced IS causality check with BDNK frame-coefficient argument
- Stated explicitly: at sigma=0, BDNK and IS yield IDENTICAL results

## Key Physics Preserved
- All critical Rayleigh numbers numerically unchanged (657.511, 1707.762, 1100.65)
- All critical wavenumbers unchanged
- Eigenfunctions identical
- Xi = p_0/(epsilon_0 c^2) parameter retained (non-dissipative physics)
