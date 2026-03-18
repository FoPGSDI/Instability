# Agent 17: BDNK Conversion - Perturbation + Convection (Ch IV, sec 41-44)

## File: `output/chapters/relativistic/rel_chapter_4_sec41-44.tex`

## Changes Made
- File header updated to reference BDNK instead of IS
- IS heat-flux relaxation description replaced by BDNK first-order heat flux with frame terms
- IS heat equation (telegrapher type with tau_q) replaced by standard first-order heat equation; causality via BDNK frame coefficients
- Normal-mode thermal operator simplified: removed tau_q sigma^2 term
- Causality checks updated: thermal modes now reference BDNK strong hyperbolicity instead of IS telegraph speed
- Overstable mode causality: IS relaxation times replaced by BDNK coupled inequalities
- Summary updated throughout

## Non-dissipative physics: UNCHANGED
- MHD energy-momentum tensor, induction equation, boundary conditions, variational principle, stationary convection solutions all untouched

## Marginal state (sigma=0): Identical results
- IS terms were proportional to sigma and already vanished; BDNK has no such terms
