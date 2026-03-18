# Subagent 7: BDNK Normal Modes (Ch II, Sections 10-12)

## Status: COMPLETE

## Changes Made

### `output/chapters/relativistic/rel_chapter_2_sec10-12.tex`

#### Section 10 (Normal modes)
- Replaced IS framework description with BDNK first-order causal viscous hydrodynamics
- Removed "Additional modes" item from the introductory enumeration (BDNK has no extra relaxation DOFs)
- Removed IS relaxation-time correction terms from momentum eq (eq:rel-2-92), energy eq (eq:rel-2-93), and vorticity eq (eq:rel-2-94)
- Changed dispersion relation from 5th-order (IS) to 3rd-order (BDNK): 3 physical modes only
- Removed entire discussion of "transient relaxation modes" (Section rel-11c deleted)
- Replaced `relcorrection` block: explains BDNK vs IS mode structure difference clearly
- Updated causality check: BDNK strong hyperbolicity replaces IS relaxation-time bounds

#### Section 11 (Exchange of stabilities)
- Removed IS remainder term R_IS from the proof: BDNK has no such term
- The proof now yields Im(sigma) = 0 EXACTLY (not O(v^2/c^2) as in IS)
- Updated `relcorrection` block to state exact exchange of stabilities in BDNK
- Added key insight: at marginal state (sigma=0), IS and BDNK give identical results

#### Section 12 (Marginal state eigenvalue problem)
- "IS correction terms vanish at sigma=0" replaced with "BDNK dissipative terms vanish at sigma=0"
- Added explicit statement: IS and BDNK yield identical eigenvalue problems at marginal state
- New subsection (rel-12c) comparing BDNK and IS at/near marginal state
- Updated causality check: no transient-mode check needed in BDNK
- Simplified non-relativistic limit (no five-to-three mode collapse needed)

## Key Physical Insight
At marginal stability (sigma=0), IS and BDNK give IDENTICAL results because:
- IS relaxation terms are proportional to sigma and vanish at sigma=0
- BDNK dissipative terms are proportional to sigma and vanish at sigma=0
Differences only appear in transient dynamics and mode structure away from marginal state.

## Conventions Followed
- All changes follow `BDNK_CONVENTIONS.md`
- Removed references to tau_pi, tau_q relaxation times in the equations
- Kept Rarel (relativistic Rayleigh number) with O(v^2/c^2) corrections
- Used BDNK terminology: "frame coefficients," "strong hyperbolicity," "first-order constitutive relations"
