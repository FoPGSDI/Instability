# Critical Proofread Batch A: Framework + Chapters I--III

**Agent:** Critical Proofreading Agent A
**Branch:** rel-lg
**Date:** 2026-03-18
**Files reviewed:** 15 files in `output/chapters/relativistic/`

---

## Fixes Applied

### 1. Notation: w = (epsilon+p)/c^2 EVERYWHERE (Critical)

The canonical definition used throughout the book is `w = (epsilon+p)/c^2`.
Multiple files had the incorrect notation `w = epsilon + p` (missing the `/c^2`).

| File | Line(s) | Issue | Fix |
|------|---------|-------|-----|
| `rel_preamble.tex` | 76, 79 | Comment said `w = epsilon + p` | Changed to `w = (epsilon + p)/c^2` |
| `rel_framework_thermo.tex` | 637 | `$w = \varepsilon + p$` | Changed to `$w = (\varepsilon + p)/c^{2}$` |
| `rel_chapter_2_sec13-14.tex` | 27 | `$\enthalpy = \edensity + p$` | Changed to `$\enthalpy = (\edensity + p)/c^{2}$` |
| `rel_chapter_2_sec13-14.tex` | 447 | `$\enthalpy = \edensity + p \to \rdensity c^2$` | Changed to `$\enthalpy = (\edensity + p)/c^{2} \to \rdensity$` |
| `rel_chapter_2_sec17-18.tex` | 31 | `$\enthalpy = \edensity + p$` | Changed to `$\enthalpy = (\edensity + p)/c^{2}$` |
| `rel_chapter_3_sec19-23.tex` | 327 | `$\enthalpy = \edensity + p = \text{const}$` | Changed to `$\enthalpy = (\edensity + p)/c^{2} = \text{const}$` |
| `rel_chapter_3_sec24-28.tex` | 34 | `$\enthalpy = \edensity + p$` | Changed to `$\enthalpy = (\edensity + p)/c^{2}$` |
| `rel_chapter_3_sec32-35.tex` | 26 | `$\enthalpy = \edensity + p$` | Changed to `$\enthalpy = (\edensity + p)/c^{2}$` |

### 2. BDNK Consistency: Removed IS Relaxation Times from BDNK Equations (Critical)

**File:** `rel_chapter_3_sec24-28.tex`, lines 81--102

The perturbation equations in Sec. 25 (rotating convection) were labeled as BDNK
but contained Israel--Stewart equations:
- The momentum equation (eq. rel-3-78) had a spurious IS heat-flux term
  `$+ (1/\tauq)\,\partial_i q_{\mathrm{IS}}$`
- The heat equation (eq. rel-3-79) was the IS telegraph equation
  `$\tauq \partial^2 \Theta/\partial t^2 + ...$` instead of the BDNK
  first-order form

**Fix:** Removed the IS heat-flux term from the momentum equation. Replaced the
IS telegraph equation with the standard diffusion equation (the BDNK form, where
causality comes from frame coefficients, not from a second time derivative).
Updated the causality check box (lines 523--524) to remove the IS thermal speed
formula `$v_{\mathrm{heat}} = \sqrt{\kappa/\tauq}$`.

### 3. Math Verification: Alfven Speed Dimensional Error (Critical)

**File:** `rel_chapter_1.tex`, line 440 (eq. rel-1-24)

The Alfven speed formula had an erroneous factor of c^2:
```
v_A^2 = b^2 / (4*pi*w + b^2/c^2) * c^2   [WRONG: gives v_A^2 ~ c^4]
```
should be:
```
v_A^2 = b^2 / (4*pi*w + b^2/c^2)          [CORRECT: velocity squared]
```

With w = (epsilon+p)/c^2, the denominator = (4*pi*(epsilon+p) + b^2)/c^2, so
v_A^2 = b^2 c^2 / (4*pi*(epsilon+p) + b^2), which matches the correct formula
in eq. rel-1-26 and the MHD framework.

### 4. MHD Framework: Effective Enthalpy Definition (Minor)

**File:** `rel_framework_mhd.tex`, line 567

The linearised MHD effective enthalpy was written as
`$w^*_0 = (\varepsilon_0 + p_0 + b^2_{(0)})/(4\pi c^2)$`
which places the `4\pi` dividing the entire expression. The correct Gaussian-unit
form is `$w^*_0 = (\varepsilon_0 + p_0 + b^2_{(0)}/(4\pi))/c^2$`.

### 5. LaTeX Compilation: Duplicate Macro Definitions

**File:** `rel_preamble.tex`, lines 134--160

`\bulkP` was defined twice with different values:
- Line 136: `\newcommand{\bulkP}{\Pi}`
- Line 157: `\providecommand{\bulkP}{\Pi_{\mathrm{bulk}}}`

The `\providecommand` is silently ignored (since `\bulkP` already exists), but
the intent was inconsistent. Also `\taupi` and `\tauq` had redundant
`\providecommand` duplicates.

**Fix:** Removed the duplicate `\providecommand` definitions for `\bulkP`,
`\taupi`, and `\tauq`. Added only `\tauPi` which was genuinely new.

---

## Checks Completed (No Issues Found)

### Gavassino Citations
All `\cite{GavassinoXXX}` keys verified against `SHARED_REFERENCES.bib`:
- `GavassinoCausality2021`, `GavassinoGibbs2021`, `GavassinoLyapunov2020`,
  `GavassinoGapless2024`, `GavassinoUniversality1`, `GavassinoUniversality2`,
  `GavassinoAntonelliPizzocheroHaskell2020`, `GavassinoRotatingHeat2025`,
  `Gavassino2024`, `GavassinoCausalityHIC2025`, `GavassinoAcausalityIS2025`,
  and all others -- all present.

### Gavassino Theorem Statement
"Stability implies causality" correctly stated as "thermodynamic stability
(Gibbs stability) implies causality" in:
- `rel_framework_hydro.tex` (theorem box, Sec. gavassino-stability-causality)
- `rel_chapter_1.tex` (Sec. rel-1-6, item 4)

### Universality Remark
The formalism-independence corollary correctly applied in:
- `rel_framework_hydro.tex` (Sec. gavassino-universality, blue box)
- `rel_chapter_2_sec10-12.tex` (Sec. rel-12c, relcorrection box)
- `rel_chapter_1.tex` (Sec. rel-1-6, gauge structure discussion)

### Cross-References
All `\label`/`\ref`/`\eqref` pairs are internally consistent within each file.
Cross-file references (e.g., `\eqref{eq:3-79}`) refer to the classical chapters.

### IS Relaxation Times in Comparison Context
The following files use `\taupi`, `\tauq` only in explicit IS-vs-BDNK comparison
passages (acceptable per convention 4):
- `rel_chapter_1.tex`: Table comparing IS and BDNK DOFs
- `rel_chapter_2_sec10-12.tex`: IS vs BDNK mode structure comparison
- `rel_chapter_2_sec15.tex`: Note that IS parameter does not appear in BDNK
- `rel_chapter_3_sec29-31.tex`: Full IS-vs-BDNK overstability comparison

### Physical Correctness
- Sound speed bound $c_s^2 \leq c^2$ correctly stated everywhere
- Fast magnetosonic speed bound proof correct in MHD framework
- Relativistic Rayleigh number corrections consistent across Ch II files
- Taylor number enhancement by enthalpy factor consistent across Ch III files
- Non-relativistic limits correctly recover classical results in all files

### Grammar
Professional academic English throughout. No significant grammar issues found.
