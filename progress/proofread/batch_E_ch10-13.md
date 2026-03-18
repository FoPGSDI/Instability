# Phase 2E Proofreading Report: Chapters X--XIII (13 files)

**Agent:** E
**Date:** 2026-03-18
**Branch:** relativistic-causal
**Files:** `output/chapters/relativistic/rel_chapter_10_sec96-97.tex` through `rel_chapter_13_sec120.tex`

## Summary of Changes

### rel_chapter_10_sec96-97.tex
- **No changes needed.** LaTeX syntax clean; math consistent; cross-refs valid; BDNK not applicable (ideal MHD); Alfven speed causality bound verified ($v_A < c$); classical limits recovered correctly; dimensional analysis verified.

### rel_chapter_10_sec98-99.tex
- **Line 310:** Removed duplicate `where` (two consecutive "where" on adjacent lines before eq. `eq:rel-10-z`).

### rel_chapter_11_sec100-101.tex
- **No changes needed.** Clean LaTeX; Lorentz-factor weighting of KH density fractions correct; dispersion relation dimensionally consistent; NR limits verified.

### rel_chapter_11_sec102-103.tex
- **Labels eq:rel-11-1, eq:rel-11-2, eq:rel-11-3:** Renamed to `eq:rel-11-102-1`, `eq:rel-11-102-2`, `eq:rel-11-102-3` to avoid collision with identically-named labels in `rel_chapter_11_sec100-101.tex`.
- **Line 477:** Fixed misleading Taylor expansion: `$\Lf^{4}\approx 1+4U^{2}/(2c^{2})$` corrected to `$\Lf^{4}\approx 1+2U^{2}/c^{2}$`. The expansion of $(1-U^2/c^2)^{-2}$ to leading order gives $1+2U^2/c^2$; the intermediate `4/2` was an unnecessary and confusing factorisation.

### rel_chapter_11_sec104.tex
- **No changes needed.** Drazin profile analysis clean; marginal-curve relativistic correction $J_{\max}^{\rm rel} = \frac{1}{4}(1+V_0^2/3c^2+\cdots)$ verified dimensionally; table formatting correct.

### rel_chapter_11_sec105-106.tex
- **Line 98 (eq:rel-11-R7):** Fixed typo `k_{1}` to `k_{x}` in the Coriolis-modified characteristic equation. The subscript `1` is a fluid-region index, not a wavevector component; the correct quantity is $k_x$.
- **Line 366 (eq:rel-11-R22):** Removed spurious `\frac{...}{1}` (division by 1) in the phase-speed bound expression.
- **Bibliographical Notes (lines 403--468):** Fixed five instances of `\medskip\noindent` appearing inside `enumerate` environments, which is invalid LaTeX. Each such break now properly closes and re-opens the enumerate with the correct counter.

### rel_chapter_12_sec107-109.tex
- **No changes needed.** Post-Newtonian gravitational cylinder analysis correct; modified Bessel function arguments use $\tilde{k}^2 = k^2 + \sigma^2/c^2$ consistently; BDNK viscous treatment properly replaces $\rho_0 \to \rho_0^*$ without frequency-dependent corrections; causality bounds verified.

### rel_chapter_12_sec110.tex
- **Line 102 (eq:rel-12-110-4):** Removed meaningless `\cdot \frac{1}{1}` (multiply by 1) in the boxed definition of $v_A^2$.

### rel_chapter_12_sec111-112.tex
- **No changes needed.** Capillary instability dispersion relations dimensionally correct; Israel junction conditions properly applied; BDNK viscous capillary number $J_{\rm rel}$ defined consistently; ideal MHD and resistive limits verified.

### rel_chapter_12_sec113-115.tex
- **No changes needed.** Equipartition stability theorem proof clean; Elsasser variables correctly defined; pinch dispersion relation structurally matches classical with proper relativistic substitutions; Kruskal--Shafranov criterion includes $\Gamma^2$ correction; all MHD mode speeds verified subluminal.

### rel_chapter_13_sec116-118.tex
- **No changes needed.** Virial theorem tensor formulation correct; post-Newtonian scalar virial identity consistent; critical adiabatic index $\gamma_c = 4/3 + \kappa GM/(Rc^2)$ with $\kappa = 38/21$ verified; comparison table well-formatted.

### rel_chapter_13_sec119.tex
- **No changes needed.** Relativistic Jeans dispersion relation dimensionally consistent; pressure-destabilisation mechanism correctly explained; three limiting cases (NR, radiation, maximally stiff) verified; note: $c_s^2$ convention in this file includes explicit $c^2$ factor ($c_s^2 = (\partial p/\partial\varepsilon)_s c^2$), which differs from some other files but is internally consistent.

### rel_chapter_13_sec120.tex
- **No changes needed.** Combined rotation + magnetic field dispersion relation (sextic) correct; Jeans criterion unaffected by rotation and B-field as in classical case; relativistic Toomre parameter defined; fast magnetosonic speed formula $v_f^2 = c_s^2 + v_A^2 - c_s^2 v_A^2/c^2 < c^2$ verified.

## Checks Performed

| Check | Status |
|-------|--------|
| LaTeX syntax (unmatched braces, environments) | PASS (5 fixes applied) |
| Math consistency (equation structure, factors) | PASS (2 fixes: Taylor expansion, spurious /1) |
| BDNK consistency (first-order, no relaxation time) | PASS |
| Notation ($\enthalpy$, $\Lf$, $\vA$, etc.) | PASS |
| Cross-references (label collisions) | PASS (3 labels renamed) |
| Grammar and spelling | PASS (1 duplicate word removed) |
| Bibliography formatting | PASS (5 enumerate breaks fixed) |
| Dimensional analysis | PASS |
| Classical limits ($c \to \infty$) | PASS |
| Causality bounds ($v_A < c$, $c_s \le c$, $v_f < c$) | PASS |

## Total Fixes: 12
- 1 duplicate word removed
- 3 label collisions resolved
- 1 Taylor expansion corrected
- 2 spurious factors removed (division by 1, multiply by 1)
- 1 wavevector subscript typo fixed ($k_1 \to k_x$)
- 5 bibliography enumerate environment breaks fixed (invalid LaTeX)
