# Subagent 2: BDNK MHD Framework Conversion

## Status: COMPLETE

## File Modified
- `output/chapters/relativistic/rel_framework_mhd.tex`

## Changes Made

### 1. Header updated
- Added BDNK formulation note and reference to BDNK_CONVENTIONS.md.

### 2. Resistive RMHD section (Section 4) rewritten for BDNK
- Replaced IS resistive MHD dissipation with BDNK first-order resistive terms.
- Ohm's law presented as an algebraic (non-dynamical) constitutive relation.
- Added explicit comparison box: BDNK vs IS for the resistive current (no relaxation time tau_r).
- Resistive induction equation now derived directly from first-order Ohm's law.
- Added "No telegraph-type equation" remark: BDNK does not need the telegraph modification; causality comes from frame coefficients in the energy-momentum sector.
- Magnetic diffusivity and Reynolds number sections retained (identical in both frameworks).
- Joule dissipation retained (identical in both frameworks).

### 3. Characteristic speed analysis updated
- Added new subsection "Characteristic speeds in resistive BDNK MHD" (sec:char-speeds-resistive).
- BDNK: same-degree characteristic polynomial, no spurious relaxation modes.
- IS (for comparison): extra relaxation modes with speeds ~ sqrt(eta_m / tau_r).
- Causality guaranteed by construction in BDNK, not by parameter tuning.

### 4. Linearised perturbation section extended
- Added subsection "Resistive dispersion relation in the BDNK framework" (sec:resistive-dispersion-bdnk).
- Alfven mode: quadratic in omega (BDNK) vs cubic (IS). Explicit roots given.
- Magnetosonic modes: quartic (BDNK) vs sextic (IS).
- Lower-order polynomials simplify both analytic and numerical treatment.

### 5. Summary section updated
- Point 3: notes that no relaxation times for resistive current are needed.
- Point 4: references lower-order BDNK dispersion relations.
- Added "BDNK vs IS for MHD" paragraph: ideal sector identical, only dissipative terms differ; BDNK has fewer PDEs, lower-order dispersion, rigorous nonlinear causality proof.

### 6. Content preserved unchanged
- All ideal MHD content (covariant Maxwell, Alfven waves, flux freezing, energy-momentum tensor, ideal characteristic speeds, non-relativistic limits).
