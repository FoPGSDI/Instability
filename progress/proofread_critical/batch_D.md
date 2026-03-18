# Critical Proofreading Batch D: Chapters XII--XIV, Epilogue, book_main.tex

**Agent:** Critical Proofreading Agent D
**Date:** 2026-03-18
**Branch:** rel-lg

## Files Reviewed

1. `rel_chapter_12_sec107-109.tex`
2. `rel_chapter_12_sec110.tex`
3. `rel_chapter_12_sec111-112.tex`
4. `rel_chapter_12_sec113-115.tex`
5. `rel_chapter_13_sec116-118.tex`
6. `rel_chapter_13_sec119.tex`
7. `rel_chapter_13_sec120.tex`
8. `rel_chapter_14_sec121-122.tex`
9. `rel_chapter_14_sec123.tex`
10. `rel_epilogue.tex`
11. `book_main.tex`

## 10-Point Checklist Results

### 1. Spelling and Typos
- No misspellings found (checked common error patterns).

### 2. LaTeX Syntax and Compilation
- **FIXED** (`rel_chapter_14_sec123.tex`): Spurious `\frac{3.42}{\phantom{0}}` -- a fraction with an invisible denominator. Changed to plain coefficient `3.42\,\mathscr{C}^{2}`.

### 3. Structural / Sectioning Issues
- **FIXED** (`rel_chapter_12_sec110.tex`): Used `\chapter*{...}` with `\addcontentsline`, creating a spurious unnumbered chapter inside Chapter XII. Changed to `\section{...}` to maintain proper hierarchy.
- **FIXED** (`rel_chapter_14_sec123.tex`): Used `\chapter*{...}` with `\addcontentsline`, creating a spurious unnumbered chapter inside Chapter XIV. Changed to `\section{...}` and removed duplicate section heading that resulted.

### 4. Cross-Reference and Label Consistency
- **FIXED** (`rel_chapter_14_sec121-122.tex`): Used `\ref*{ch:rel-mhd-framework}` (non-standard) with verbose prose reference "Chapter on Relativistic MHD Framework". Simplified to `Chapter~\ref{ch:rel-mhd-framework}`.
- Noted: Equation label `eq:rel-12-33` is skipped (goes from 32 to 34 in sec107-109). No functional impact since labels are referenced by name, not number.

### 5. Bibliography Numbering
- **FIXED** (`rel_chapter_12_sec111-112.tex`): BDNK bibliography section started at `\setcounter{enumi}{7}` but the preceding GRB section already used items up to 9 (Gottlieb et al. 2024), causing duplicate numbering. Changed to `\setcounter{enumi}{9}`.

### 6. Formatting of File References
- **FIXED** (`rel_chapter_12_sec110.tex`): Two instances of bare `RELATIVISTIC\_CONVENTIONS.md` wrapped in `\texttt{}`.
- **FIXED** (`rel_chapter_12_sec113-115.tex`): One instance of bare `RELATIVISTIC\_CONVENTIONS.md` wrapped in `\texttt{}`.
- **FIXED** (`rel_chapter_13_sec119.tex`): One instance of bare `RELATIVISTIC\_CONVENTIONS.md` wrapped in `\texttt{}`.

### 7. Sound-Speed Convention Consistency
- **FIXED** (`rel_chapter_13_sec119.tex`): Defined $c_s^2 = (\partial p/\partial\varepsilon)_s \cdot c^2$, inconsistent with the convention used everywhere else in the book ($c_s^2 = (\partial p/\partial\varepsilon)_s \leq c^2$). Also fixed the adiabatic perturbation expression to be consistent.
- **FIXED** (`rel_chapter_12_sec113-115.tex`): Same spurious $c^2$ factor in sound-speed definition at line 987. Removed.

### 8. book_main.tex Verification
- All `\input` lines present and correctly ordered for Chapters XII--XIV and epilogue.
- `\graphicspath` includes all 14 chapter directories plus `plots/` and `plots/deep/`.
- Bibliography setup correct: `\bibliographystyle{unsrt}` with `\bibliography{../../../SHARED_REFERENCES}`. The `.bib` file exists at the expected path.
- All framework files (`rel_framework_hydro`, `rel_framework_mhd`, `rel_framework_thermo`) and chapter section files exist on disk.
- Front matter (preface, acknowledgments, notation) and back matter (list of figures, bibliography) properly structured.

### 9. Causality and Physics Consistency
- All files systematically verify causality bounds ($c_s \leq c$, $v_A < c$, $v_f < c$).
- BDNK first-order framework consistently used (no Israel-Stewart relaxation equations for viscous transport).
- Newtonian limits explicitly verified in all dispersion relations.

### 10. Notation and Macro Usage
- `\enthalpy`, `\edensity`, `\rdensity`, `\Lf`, `\cs`, `\vA` used consistently.
- Gaussian units for electromagnetic quantities consistently declared.
- `\Gamma` (capital) correctly reserved for GRB bulk Lorentz factor in sec113-115, distinct from `\Lf` = `\gamma` (local Lorentz factor).

## Summary of Changes

| File | Issue | Fix |
|------|-------|-----|
| `rel_chapter_12_sec110.tex` | `\chapter*` inside Ch XII | Changed to `\section` |
| `rel_chapter_12_sec110.tex` | Bare file references | Wrapped in `\texttt{}` |
| `rel_chapter_12_sec111-112.tex` | Bibliography enumi overlap | `\setcounter{enumi}{9}` |
| `rel_chapter_12_sec113-115.tex` | Bare file reference | Wrapped in `\texttt{}` |
| `rel_chapter_12_sec113-115.tex` | Wrong $c_s^2$ convention | Removed spurious $c^2$ |
| `rel_chapter_13_sec119.tex` | Bare file reference | Wrapped in `\texttt{}` |
| `rel_chapter_13_sec119.tex` | Wrong $c_s^2$ convention | Fixed to match book convention |
| `rel_chapter_14_sec121-122.tex` | `\ref*` non-standard | Simplified cross-reference |
| `rel_chapter_14_sec123.tex` | `\chapter*` inside Ch XIV | Changed to `\section` |
| `rel_chapter_14_sec123.tex` | Duplicate section heading | Removed |
| `rel_chapter_14_sec123.tex` | `\frac{3.42}{\phantom{0}}` | Fixed to plain `3.42` |

## Files with No Changes Needed

- `rel_chapter_12_sec107-109.tex` -- clean
- `rel_chapter_13_sec116-118.tex` -- clean
- `rel_chapter_13_sec120.tex` -- clean
- `rel_epilogue.tex` -- clean
- `book_main.tex` -- verified correct, no changes needed
