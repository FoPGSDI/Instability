# Critical Proofread Batch C: Chapters VIII--XI

**Agent:** Critical Proofreading Agent C
**Date:** 2026-03-18
**Branch:** rel-lg
**Files reviewed:** 18 files (rel_chapter_8_sec75-76.tex through rel_chapter_11_sec105-106.tex)

## 10-Point Checklist

### 1. Spelling and Typographical Errors
- **No misspellings found** in rendered text across all 18 files.

### 2. Grammar and Syntax
- **FIXED** `rel_chapter_8_sec77-78.tex` line 75: "The BDNK first-order viscous constitutive relation equation introduces a BDNK frame coefficients" -- redundant "equation" and garbled article. Fixed to: "The BDNK first-order viscous constitutive relation introduces frame coefficients".
- **FIXED** `rel_chapter_8_sec77-78.tex` lines 78-80: "replacement of the diffusion operator $(D^2 - a^2 - \sigma)$ by $(D^2 - a^2 - \sigma)$" -- tautological replacement (replacing operator by itself). Fixed to: "modification of the diffusion operator in the viscous terms."
- **FIXED** `rel_chapter_9_sec87-89.tex` line 285-286: "the relaxation operators the BDNK frame corrections vanish" -- garbled sentence fragment ("relaxation operators" is a dangling leftover). Fixed to: "the BDNK frame corrections vanish".
- **FIXED** `rel_chapter_9_sec90-91.tex` line 92-93: "propagate at a finite speed ensured by" -- redundant "ensured" after "ensures". Fixed to: "propagate at a finite speed bounded by $c$, as guaranteed by".
- **FIXED** `rel_chapter_8_sec77-78.tex` line 134: "The \emph{BDNK causality} modifies" -- noun phrase incomplete. Fixed to: "The \emph{BDNK causal framework} modifies".
- **FIXED** `rel_chapter_8_sec77-78.tex` line 414: "The BDNK causality ensures" -- same pattern. Fixed to: "The BDNK causal framework ensures".

### 3. Mathematical Notation Consistency
- **FIXED** `rel_chapter_10_sec95.tex` lines 573, 597: Used `\Gamma_{\Omega}` while the rest of the file uses `\Lf_{\Omega}` for the Lorentz factor macro. Fixed both occurrences to `\Lf_{\Omega}`.
- **FIXED** `rel_chapter_8_sec77-78.tex` line 54: Missing parentheses in expression `$\enthalpy_0/c^2 = \rdensity(1 + \Xi + \edensity_0/\rdensity c^2 - 1)$` -- the division `\edensity_0/\rdensity c^2` is ambiguous. Fixed to `\edensity_0/(\rdensity c^2)`.
- **FIXED** `rel_chapter_10_sec93.tex` lines 397-399: In the non-relativistic limit section, bare `w` was used inside integrals for the eigenfunction variable, conflicting with `w` = enthalpy density defined earlier. Fixed to `\hat{w}` for consistency with the rest of the section.

### 4. LaTeX Structural Issues
- **Noted (not changed):** `rel_chapter_9_sec87-89.tex` label `\label{sec:rel-87-IS}` references "IS" (Israel--Stewart) but the subsection is about BDNK dissipation. Not changed to avoid breaking cross-references.
- **Noted (not changed):** `rel_chapter_9_sec90-91.tex` equation labels `eq:rel-9-IS-shear` and `eq:rel-9-IS-bulk` reference "IS" but describe BDNK equations. Same rationale.

### 5. Cross-reference Integrity
- All `\label`/`\ref` pairs checked for uniqueness within files. No duplicate labels found across the batch.
- Section numbering consistent within each file.

### 6. Equation Formatting
- Delimiter matching verified (`\bigl`/`\bigr`, `\Bigl`/`\Bigr`, `\left`/`\right`).
- No orphaned delimiters found.
- `\boxed{}` equations properly closed throughout.

### 7. Figure/Table References
- All `\label`/`\ref` pairs for figures and tables are consistent within files.
- Table column counts match header specifications.

### 8. Citation Consistency
- Citations use `\cite{}`, `\citep{}`, `\citet{}`, `\citealt{}` consistently within each file.
- Author-year inline citations follow consistent formatting.

### 9. Physical Content / Causality Checks
- All files include causality verification sections.
- The BDNK framework is consistently described as first-order causal (not second-order Israel--Stewart) throughout.
- Non-relativistic limits verified in each section.
- The `\textsc{Relativistic Conventions}` reference appears in slightly different forms across files (cosmetic, not fixed).

### 10. Placeholder/Scaffold Issues
- `rel_chapter_9_sec90-91.tex` lines 88-91 and 96-99 contain trivial identity replacements: `$\sigma \to \hat{\sigma} = \sigma$` and `$\eta \to \hat{\eta} = \eta$`. These appear to be intentional placeholders indicating that the BDNK corrections to these operators are encoded in the frame coefficients rather than in explicit modifications. Left as-is since the surrounding text explains this.

## Summary of Fixes

| File | Line(s) | Issue | Fix |
|------|---------|-------|-----|
| rel_chapter_8_sec77-78.tex | 54 | Missing parens in math | Added `()` around denominator |
| rel_chapter_8_sec77-78.tex | 75 | Garbled grammar | Removed redundant words |
| rel_chapter_8_sec77-78.tex | 78-80 | Tautological replacement | Rewrote sentence |
| rel_chapter_8_sec77-78.tex | 134 | Incomplete noun phrase | "causality" -> "causal framework" |
| rel_chapter_8_sec77-78.tex | 414 | Incomplete noun phrase | "causality" -> "causal framework" |
| rel_chapter_9_sec87-89.tex | 285-286 | Sentence fragment | Removed dangling text |
| rel_chapter_9_sec90-91.tex | 92-93 | Redundant "ensured" | Rewrote clause |
| rel_chapter_10_sec93.tex | 397-399 | Notation conflict (`w` vs `\hat{w}`) | Changed to `\hat{w}` |
| rel_chapter_10_sec95.tex | 573 | Wrong Lorentz factor symbol | `\Gamma_{\Omega}` -> `\Lf_{\Omega}` |
| rel_chapter_10_sec95.tex | 597 | Wrong Lorentz factor symbol | `\Gamma_{\Omega}` -> `\Lf_{\Omega}` |

**Total fixes: 10**
**Files modified: 5 of 18**
**No issues found in remaining 13 files.**
