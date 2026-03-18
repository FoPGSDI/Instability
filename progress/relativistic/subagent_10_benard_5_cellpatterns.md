---
agent: 10
chapter: 2
section: 16
task: Relativistic cell patterns
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_2_sec16.tex` containing the
relativistic extension of Ch II Section 16 (Cell patterns).

### Content produced

1. **Relativistic horizontal eigenvalue problem** -- Derived the correction to
   `a^2 = k_x^2 + k_y^2` from the conformal rescaling of horizontal lengths
   in a static gravitational background. The correction is isotropic and of
   order `gd/c^2`.

2. **Degeneracy of planforms at marginal stability** -- Proved that the infinite
   planform degeneracy persists relativistically: the Israel-Stewart perturbation
   equations depend only on `a_rel^2`, not on the direction of the horizontal
   wave vector. Includes a causality verification box.

3. **Rolls, rectangles, hexagons, triangles** -- Showed all classical solutions
   carry over with `a -> a_rel`. Wrote explicit relativistic forms for each
   pattern type including the general Bisshopp solution.

4. **Non-linear amplitude equations** -- Wrote the Landau-type amplitude
   equations with relativistic corrections to self-interaction, cross-coupling,
   and resonant triad coefficients. Identified three sources of correction:
   relativistic inertia (enthalpy replacing density), causal heat transport
   (Israel-Stewart dispersive correction), and compressibility coupling.

5. **Physical discussion** -- Quantitative estimates for four regimes:
   - Laboratory fluids: corrections ~ 10^{-18}, completely negligible
   - Neutron-star oceans: corrections ~ 10^{-2}, potentially observable
   - Quark-gluon plasma: corrections O(1), Newtonian limit inapplicable
   - Early-universe plasma: corrections O(1), full relativistic treatment needed

### Conventions

- Uses macros from `rel_preamble.tex` (enthalpy, edensity, Rarel, tauq, etc.)
- Uses `relcorrection` and `causalitycheck` tcolorbox environments
- Metric signature (-,+,+,+), c kept explicit throughout
- Israel-Stewart causal dissipation framework

## Issues / Notes

- No figures created; the classical figure placeholders are referenced where
  appropriate.
- The amplitude equations are written schematically; a full derivation from
  the Israel-Stewart equations would require a dedicated calculation.

## Next

Ready for integration into `rel_main.tex` when all Chapter 2 relativistic
sections are assembled.
