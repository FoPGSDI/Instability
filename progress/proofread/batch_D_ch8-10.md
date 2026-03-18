# Batch D Proofreading Report: Chapters VIII--X (12 files)

## Files Processed

1. `rel_chapter_8_sec75-76.tex`
2. `rel_chapter_8_sec77-78.tex`
3. `rel_chapter_8_sec79.tex`
4. `rel_chapter_8_sec80.tex`
5. `rel_chapter_9_sec81-83.tex`
6. `rel_chapter_9_sec84-86.tex`
7. `rel_chapter_9_sec87-89.tex`
8. `rel_chapter_9_sec90-91.tex`
9. `rel_chapter_10_sec90-92.tex`
10. `rel_chapter_10_sec93.tex`
11. `rel_chapter_10_sec94.tex`
12. `rel_chapter_10_sec95.tex`

## Issues Found and Fixed

### LaTeX Syntax Errors

| File | Line(s) | Issue | Fix |
|------|---------|-------|-----|
| sec77-78 | 84--90 | Duplicated `\begin{equation}`, `\label{eq:rel-8-Psi}`, and definition block | Removed duplicate block; kept single equation |
| sec77-78 | 89 | `\Psi ;\equiv;` (missing backslashes on `\;`) | Changed to `\Psi \;\equiv\;` |
| sec77-78 | 347--348 | Duplicated sentence "automatically satisfied in the BDNK framework." | Removed duplicate |
| sec77-78 | 340--342 | Malformed equation: displayed `= \frac{d}{\sqrt{\Psi}}...` as part of inequality | Simplified to clean `v_{\mathrm{char}} \leqslant c` bound |
| sec80 | 66 | Missing `\pi^{\mu\nu}` term in energy-momentum tensor | Added `+ \pi^{\mu\nu}` line |
| sec80 | 80--82 | Blank line inside equation (between `\pi^{\mu\nu}` and `= -2\shearvisc`) | Removed blank line |
| sec80 | 194--195 | Broken fraction `\frac{...}{1,}` (denominator was literal `1`) | Replaced with relativistic correction `+ \order{v^2/c^2}` |
| sec80 | 207,216 | `$( D^{2}-k^{2})$` nested dollar signs inside display math | Removed spurious `$` delimiters |
| sec84-86 | 14 | `\input{rel_preamble}` included directly (loaded by rel_main.tex) | Removed the `\input` line |
| sec87-89 | 672 | Invalid label `\label{eq:rel-causality-\text{BDNK frame condition}}` | Changed to `\label{eq:rel-causality-BDNK-frame}` |
| sec87-89 | 156 | Redundant `\leqslant c \le c` | Fixed to `\leqslant c` |
| sec87-89 | 179 | Redundant `\leqslant c \le c` | Fixed to `\leqslant c` |
| sec75-76 | 338 | Undefined `\figurePlaceholder` macro | Replaced with commented-out figure placeholder |

### Duplicate Labels (Cross-File)

| Files | Labels | Fix |
|-------|--------|-----|
| sec79 vs sec80 | `eq:rel-8-200` through `eq:rel-8-232` (30+ duplicates) | Renamed all sec80 labels to `eq:rel-80-2xx` prefix |
| sec81-83 vs sec80 | `\label{sec:rel-80}` | Renamed ch9 instance to `sec:rel-9-80` |
| sec87-89 vs sec90-91 | `eq:rel-9-Qrel` | Renamed sec90-91 instance to `eq:rel-9-90-Qrel` |

### Grammar and Broken Text

| File | Line(s) | Issue | Fix |
|------|---------|-------|-----|
| sec80 | 470--474 | Garbled sentence with duplicate fragments ("...are negligible, giving entirely negligible relativistic corrections are thus entirely negligible...") | Rewrote to single clean sentence |
| sec80 | 91--93 | Referenced "angular brackets" in equation with no angular brackets | Changed to describe "shear tensor" correctly |
| sec87-89 | 25--26 | Incomplete/broken sentence ("In the BDNK formulation, the electric current.") | Removed orphaned fragment |
| sec87-89 | 149--150 | Duplicate sentence start ("The BDNK operator / The BDNK constitutive relations") | Removed orphaned fragment |
| sec87-89 | 712--716 | Garbled sentence about mode counting and BDNK | Rewrote for clarity |
| sec90-91 | 192--193 | Tautological "recovering the BDNK frame corrections" | Fixed to "recovering the classical Navier--Stokes viscous diffusion" |
| sec90-91 | 301--302 | Broken sentence "which damps modes with the BDNK characteristic scale is exceeded" | Fixed grammar |
| sec90-91 | 172--184 | Incorrectly attributed "non-hydrodynamic modes" to BDNK (this is an IS feature) | Corrected BDNK description: no extra modes |

### Bibliography Issues

| File | Issue | Fix |
|------|-------|-----|
| sec80 | Israel--Stewart entry (item 2) empty; Bemfica/Kovtun/Hoult entries triplicated | Deduplicated to single set of 5 entries; completed IS reference |
| sec80 | `\setcounter{enumi}` values wrong after dedup | Corrected numbering: 5, 7, 9, 11 |
| sec80 | "Dave Fultz" in bibliography | Changed to "D. Fultz" |
| sec90-91 | IS entry (item 3) empty; Bemfica/Kovtun triplicated with interleaved fragments | Deduplicated to 3 clean entries; completed IS reference |

### BDNK Consistency

- Verified all 12 files use BDNK first-order causal framework consistently
- Verified no Israel--Stewart relaxation times appear in main derivations (only in comparison paragraphs)
- Verified `\shearvisc` (eta_s), `\bulkvisc` (zeta), `\enthalpy` (w) macros used consistently
- Corrected sec90-91 paragraph that incorrectly attributed non-hydrodynamic modes to BDNK

### Notation Consistency

- `\rho \to w = (\varepsilon + p)/c^2` replacement verified across all Ch VIII--X files
- Relativistic Taylor number `\Tarel`, Chandrasekhar number `\Qrel` used consistently
- Lorentz factor `\Lf = \gamma` used consistently
- Alfven speed `\vA` bounded by c verified in all MHD sections

### Files Requiring No Changes

- `rel_chapter_8_sec75-76.tex` (minor: figurePlaceholder fix only)
- `rel_chapter_8_sec79.tex` (no issues found)
- `rel_chapter_9_sec81-83.tex` (label fix only)
- `rel_chapter_10_sec90-92.tex` (clean)
- `rel_chapter_10_sec93.tex` (clean)
- `rel_chapter_10_sec94.tex` (clean)
- `rel_chapter_10_sec95.tex` (clean)

## Summary

- **Total issues found and fixed**: 28
- **LaTeX syntax errors**: 13
- **Duplicate labels**: 3 cross-file conflicts (30+ individual labels renamed)
- **Grammar/broken text**: 8
- **Bibliography**: 4 (deduplication, completion, formatting)
- **BDNK consistency**: 1 conceptual correction
