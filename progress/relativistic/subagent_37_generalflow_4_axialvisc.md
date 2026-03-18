---
agent: 37
chapter: 8
section: 80 (relativistic §79)
status: completed
timestamp: 2026-03-18T12:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_8_sec80.tex`, the relativistic
extension of Chapter VIII §79 (viscous stability of combined rotational + axial
flow between coaxial cylinders).

## Content produced

1. **Relativistic background state** (§rel-80-bg): 4-velocity with both rotational
   and axial components, Israel-Stewart energy-momentum tensor, relativistic
   Poiseuille profile with O(V²/c²) corrections.

2. **Perturbation equations** (§rel-80-pert): Linearised conservation law
   ∇_μ T^{μν}=0 coupled with Israel-Stewart shear relaxation.  Three coupled
   equations for (u,v,w) with causal viscous operator replacing Newtonian
   diffusion.  Elimination to two coupled equations for u and v.

3. **Narrow-gap reduction** (§rel-80-narrow): Dimensionless formulation with
   Israel-Stewart relaxation number T = τ_π ν/d².  Equations (217)-(218) reduce
   to classical (178)-(179) when T→0 and c→∞.

4. **Approximate solution for μ > 0** (§rel-80-approx): Gap-averaged causal
   operator, cosine-series expansion, relativistic eigenvalues γ^(rel) and
   characteristic roots q^(rel).  First-approximation formula for Ta_rel (eq 230).
   Table of critical Taylor numbers for R = 0, 10, 40, 100 and T = 0, 10⁻⁴,
   10⁻², 10⁻¹.

5. **Comparison with experiments** (§rel-80-comparison): Laboratory regime
   (Donnelly-Fultz): T ~ 10⁻¹⁵, corrections negligible.  Astrophysical regimes:
   accretion columns, quark-gluon plasma, relativistic jets.

6. **Bibliographical notes**: Israel & Stewart (1976, 1979); Hiscock & Lindblom
   (1983, 1985); Romatschke (2010); Denicol, Koide & Rischke (2010); Takamoto &
   Inutsuka (2013); Chandrasekhar (1960); Donnelly & Fultz (1960); Rezzolla &
   Zanotti (2013); Romatschke & Romatschke (2019).

## Key design decisions

- Used dimensionless Israel-Stewart number T = τ_π ν/d² as the single
  relativistic parameter, so classical limit is simply T→0.
- Causal viscous operator (D²-a²)/[1+iT(σ+Ra)] replaces Newtonian (D²-a²).
- Characteristic equation becomes quartic (not quadratic) in q² due to relaxation.
- Causality checks verify v_shear ≤ c throughout.

## Issues / Notes

- Table values for T > 0 are analytically estimated from first-order expansion
  of eq (230); full numerical evaluation would require a separate computation.
- The O(c⁻²) corrections to the Taylor number from relativistic inertia are
  kept as formal correction factors [1 + O(V²/c²)] rather than explicit
  post-Newtonian coefficients.

## Next

No further action required. File is self-contained and ready for integration
into rel_main.tex.
