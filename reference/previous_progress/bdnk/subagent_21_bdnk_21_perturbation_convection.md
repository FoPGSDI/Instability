# Agent 21: BDNK Conversion - Perturbation + Convection (Ch V, sec 51-52)

## File: `output/chapters/relativistic/rel_chapter_5_sec51-52.tex`

## Changes Made
- IS causal dissipation framework replaced by BDNK first-order framework throughout
- IS heat equation (telegrapher with tau_q) replaced by standard first-order heat equation
- Normal-mode thermal operator simplified: tau_q sigma^2/d^2 term removed from eq (35)
- Master equation simplified: IS term removed from thermal operator
- Causality checks updated: IS telegraph speed -> BDNK strong hyperbolicity; IS shear relaxation -> BDNK frame coefficient bounds
- Stationary convection: IS relaxation drop-out note replaced by formalism-independent statement
- NR limit: tau_q -> 0 removed (not needed in BDNK)
- "Israel--Stewart shear viscosity" -> "BDNK shear viscosity"

## Non-dissipative physics: UNCHANGED
- Background state, rotating frame, induction equation, divergence-free conditions, vorticity equations, dimensionless parameters, two-free-boundary solution, competition/cooperation analysis, two-minimum phenomenon all untouched

## Marginal state (sigma=0): Identical results
- Dissipative terms vanish at sigma=0 regardless of formalism
