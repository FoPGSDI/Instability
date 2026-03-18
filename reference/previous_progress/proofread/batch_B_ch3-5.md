# Phase 2B Proofread Report: Chapters III-V (10 files)

**Agent:** Proofreading Agent B
**Branch:** relativistic-causal
**Date:** 2026-03-18
**Files:** 10 tex files in `output/chapters/relativistic/`

## Summary of Changes

### 1. `rel_chapter_3_sec24-28.tex`
- **IS->BDNK consistency:** Fixed header comment from "Israel-Stewart dissipation" to "BDNK first-order causal dissipation"
- **Redundant phrasing:** Simplified "a BDNK causal first-order heat equation rather than the parabolic Fourier law" to "the BDNK causal heat equation rather than the parabolic Fourier law"
- **IS leftover in causalitycheck:** Replaced IS-style description (tau_q, relaxation equation for shear stress) with proper BDNK language (frame coefficients, algebraic constitutive relations) in the causality verification box
- **Grammar:** Fixed "BDNK causal modifications times" (x3) to proper BDNK terminology ("frame coefficients", "coupled inequalities")

### 2. `rel_chapter_3_sec29-31.tex`
- **Critical math error:** Text claimed BDNK produces a "quintic" dispersion relation (line 70), directly contradicting the later statement that it's degree 3 (cubic). Fixed to state it remains cubic in BDNK (quintic only in Israel-Stewart)
- **Broken cross-references:** All 4 occurrences of `\eqref{eq:rel-3-quintic}` replaced with `\eqref{eq:rel-3-cubic}` (the quintic label was never defined)
- **Structural contradiction:** "quintic has five roots" with "two relaxation modes" rewritten to describe the cubic's three hydrodynamic roots, with a note that IS (not BDNK) would produce the quintic
- **IS leftover naming:** `\xi_{\mathrm{IS}}` renamed to `\xi_{\mathrm{rel}}`; `\xi_\tau` renamed to `\xi_{\mathrm{fr}}`
- **IS-specific formula:** Critical Prandtl number correction had `\tauq/\taupi` ratio (IS concept); replaced with generic BDNK frame coefficient `c_{\mathrm{fr}}`
- **Section framing:** Renamed subsection to clarify that IS relaxation equations are presented for comparison, not as the BDNK result
- **Table fix:** Replaced `\tauq\nu/d^2` correction term with `p_0/\rho_0 c^2` in the summary table for consistency
- **Redundant relaxation-mode text:** Removed IS-specific "two additional relaxation-mode roots" passage; replaced with BDNK statement

### 3. `rel_chapter_3_sec32-35.tex`
- **IS leftover naming:** `\dot{s}_{\mathrm{IS}}` renamed to `\dot{s}_{\mathrm{BDNK}}` (2 occurrences)
- **Awkward phrasing:** "BDNK causal modifications contributions" -> "BDNK causal transport contributions" (2 occurrences)
- **IS terminology:** "BDNK causal modifications time \tauq" -> "BDNK frame coefficients" (2 occurrences)

### 4. `rel_chapter_4_sec36-40.tex`
- No substantive changes needed. File is clean and internally consistent.

### 5. `rel_chapter_4_sec41-44.tex`
- No substantive changes needed. Israel-Stewart references are comparative (appropriate context).

### 6. `rel_chapter_4_sec45-46.tex`
- **Notation inconsistency:** `p_1^{(0)}` and `p_2^{(0)}` replaced with `p_1^{(\mathrm{rel})}` and `p_2^{(\mathrm{rel})}` throughout (13 occurrences total) to match the defined notation in eq:rel-p1p2
- **Math error:** `\mu^2 H^2` in eq:rel-beta-c-inviscid corrected to `\mu H^2/(4\pi)` (permeability appears linearly, not squared, and the 4pi factor was missing)

### 7. `rel_chapter_4_sec47-48.tex`
- **Dimensional error:** eq:rel-rhoeff had `\bsq/1` (dimensionally inconsistent); fixed to `\bsq/c^2`
- **Consequent fix:** eq:rel-vA-def denominator corrected from `\enthalpy + \bsq c^2` to `\enthalpy + \bsq` for dimensional consistency
- **Undefined macro:** `\Ra` (classical Rayleigh number) replaced with `R` since `\Ra` is not defined in the preamble
- **Unit inconsistency:** `\mu_0` (SI notation) replaced with Gaussian-consistent notation (2 occurrences)
- **Typo:** "tailof" -> "tail of" in bibliographical note (Watts & Strohmayer reference)

### 8. `rel_chapter_5_sec49-50.tex`
- No substantive changes needed. File is clean and internally consistent.

### 9. `rel_chapter_5_sec51-52.tex`
- No substantive changes needed. Israel-Stewart references are comparative (appropriate context).

### 10. `rel_chapter_5_sec53-54.tex`
- **Math error in T^{mu nu}:** eq:rel53-T0 had wrong magnetic pressure term: inner factor `1/2` on `g^{\mu\nu}` gave `b^2/4` instead of correct `b^2/2`; fixed
- **Notation inconsistency:** `p_1^{(\mathrm{eff})}`, `p_2^{(\mathrm{eff})}` replaced with `p_1^{(\mathrm{rel})}`, `p_2^{(\mathrm{rel})}` to match definitions in eq:rel53-prel (6 occurrences)
- **Unnecessary superscript:** `\sigma^{(\mathrm{eff})}` simplified to `\sigma` (2 occurrences) since no "effective sigma" is defined
- **Definition error:** `\enthalpy = (\varepsilon+p)/c^2` corrected to `\enthalpy = \varepsilon+p` (matching preamble convention)
- **Typo:** "tailof" -> "tail of" in Watts & Strohmayer bibliographical reference

### Preamble fix (`rel_preamble.tex`)
- Added missing macro definitions: `\Pran`, `\tauq`, `\taupi`, `\bulkP` (used in chapter files but previously undefined, would cause compilation errors)

## Checks Performed
1. **LaTeX syntax:** Cross-references, brace matching, macro definitions
2. **Math consistency:** Signs, c^2 factors, 4pi factors, dimensional analysis
3. **BDNK consistency:** Removed/fixed IS leftovers (naming, equations, relaxation times)
4. **Notation uniformity:** Prandtl ratio notation, field conventions, macro usage
5. **Cross-references:** Fixed 4 broken `\eqref` references
6. **Grammar:** Fixed ungrammatical phrases, typos
7. **Bibliography:** Verified citation style consistency
8. **Dimensional analysis:** Fixed 3 dimensional errors
9. **Non-relativistic limits:** Verified stated limits are correct

## Known Minor Issues (Not Fixed)
- Electrical conductivity notation varies: `\sigma_{\mathrm{e}}` (sec45-46) vs `\sigma_{\text{cond}}` (sec41-44). Both are defined in context; a project-wide convention should be chosen.
- Some files use $b^\mu$ absorbing $\sqrt{4\pi}$ (sec47-48, sec49-50, sec53-54) while sec36-40 keeps explicit $4\pi$ factors. Both conventions are internally consistent within each file.
- The sec29-31 file presents IS relaxation equations with `\tauq`, `\taupi` for comparison purposes; these are correctly framed as IS (not BDNK) after the fixes.
