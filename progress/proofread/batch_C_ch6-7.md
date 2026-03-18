# Batch C Proofreading: Chapters VI--VII (11 files)

**Agent:** Phase 2 Proofreading Agent C
**Branch:** relativistic-causal
**Date:** 2026-03-18
**Files proofread:** 11

## Files

1. `rel_chapter_6_sec55-56.tex`
2. `rel_chapter_6_sec57-58.tex`
3. `rel_chapter_6_sec59.tex`
4. `rel_chapter_6_sec60.tex`
5. `rel_chapter_6_sec61-63.tex`
6. `rel_chapter_7_sec64-66.tex`
7. `rel_chapter_7_sec67.tex`
8. `rel_chapter_7_sec68.tex`
9. `rel_chapter_7_sec69-70.tex`
10. `rel_chapter_7_sec71.tex`
11. `rel_chapter_7_sec72-73.tex`

## Issues Found and Fixed

### LaTeX Syntax / Compilation Errors

| File | Issue | Fix |
|------|-------|-----|
| sec55-56 | `\pp` undefined (partial derivative) | Replaced all `\pp` with `\partial` |
| sec57-58 | `\vect{u}` undefined macro | Replaced with `\boldsymbol{u}` (preamble has `\providecommand` but `\boldsymbol` is more portable) |
| sec68 | Stray `\input{rel_preamble}` in section file | Removed (should be in main file only) |
| sec64-66 | `\ref{eq:7-18}` and `\ref{eq:7-1}` used instead of `\eqref` | Changed to `\eqref{eq:7-18}` and `\eqref{eq:7-1}` for consistency |

### Dimensional / Physics Errors

| File | Issue | Fix |
|------|-------|-----|
| sec55-56 | Kinematic viscosity written as `\shearvisc/[(\varepsilon+p)/c^2]` (unclear bracket nesting) | Rewrote as `\shearvisc c^2/(\varepsilon+p)` |
| sec59 | Dimensionless ratio `\Xi(r)` defined as `p/(\varepsilon c^2)` -- has units of `1/c^2`, not dimensionless | Fixed to `p/\varepsilon` (pressure-to-energy-density ratio) |
| sec59 | Central value `\Xi_c = p_c/(\varepsilon c^2)` -- same dimensional error | Fixed to `p_c/\varepsilon` |
| sec60 | Effective gravity `g_eff` formula had `e^{-\Lambda}/(\varepsilon+p) dp/dr` -- wrong dimensions (1/length not acceleration) | Fixed to `-c^2/(\varepsilon+p) e^{-\Lambda} dp/dr` matching TOV relation |
| sec60 | Tolman thermal gradient had wrong sign on second term: `-T e^{-\Lambda} d\Phi/dr` | Fixed to `+(T/c^2) e^{-\Lambda} d\Phi/dr` matching sec55-56 eq. (rel6-beta) |
| sec60 | Relativistic radial operator `\mathscr{D}_{l,rel}^2` missing `(1/c^2) d\Phi/dr` term | Added missing term to match sec55-56 eq. (rel6-Dlrel) |
| sec57-58 | Buoyancy work formula `\alpha \enthalpy c^2 \beta\gamma` dimensionally wrong | Fixed to `\alpha \enthalpy \beta\gamma` (with `\enthalpy = (epsilon+p)/c^2`) |

### Notation / Convention Consistency

| File | Issue | Fix |
|------|-------|-----|
| sec68 | Enthalpy defined as `w = epsilon + p` contradicting project convention `w = (epsilon+p)/c^2` | Fixed both definitions to match project convention |
| sec67 | Solenoidal condition written with `\enthalpy` instead of `\enthalpy/c^2` for mass conservation | Fixed to `(\enthalpy/c^2) \delta u^\mu` |
| sec69-70 | Mixed `\pi^{\mu\nu}` (lowercase) and `\Pi^{\mu\nu}` (uppercase) for anisotropic stress | Standardised to `\Pi^{\mu\nu}` throughout |
| sec69-70, sec72-73 | Citation key `BemficaDN2023` inconsistent with `BemficaEtAl2023` used elsewhere | Standardised to `BemficaEtAl2023` |

### Math / Formula Errors

| File | Issue | Fix |
|------|-------|-----|
| sec68 | Couette profile written as `\Omega = A + B/r^4` everywhere -- should be `A + B/r^2` | Fixed all occurrences (section title, inline text, equations) |
| sec68 | Rayleigh discriminant formula had `\Lf^4/r^3` prefactor -- gives extra `\Lf^2` vs sec67 definition | Fixed to `\Lf^2/r^3` for consistency with sec67 eq. (rel-7-53) |

## Items Verified Correct (No Change Needed)

- TOV equation in sec60 (eq. rel-60-2): dimensional analysis confirms correct form
- Metric convention `(-,+,+,+)` consistent across all files
- Speed of light `c` kept explicit throughout, as per BDNK_CONVENTIONS
- BDNK framework described consistently: first-order constitutive relations, no relaxation equations, causality via frame coefficients
- Spherical harmonic decomposition operator `\mathscr{L}^2` unchanged from classical (correct: angular sector is standard round sphere)
- Exchange-of-stabilities proofs structurally sound in both sec57-58 and sec72-73
- Boundary conditions properly stated at stellar surface and shell boundaries
- Non-relativistic limits correctly identified in all sections
- `\citep` (Ch7) vs `\cite` (Ch6) difference: both valid with natbib package, left as is

## Known Issues Outside Scope

- Citation keys `Bemfica2018`, `Kovtun2019`, `Bemfica2019`, `HoultKovtun2020`, `BemficaEtAl2023` not found in any `.bib` file -- bibliography entries need to be created (project-wide issue)
- Preamble `rel_preamble.tex` has duplicate `\newcommand{\relcorr}` and `\newcommand{\NRlimit}` definitions (lines 132-133 and 153-154) which will cause compilation error
- Preamble comment says `w = epsilon + p` but framework convention (and most files) use `w = (epsilon+p)/c^2`
