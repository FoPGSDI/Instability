---
agent: 32
chapter: 7
section: 71
task: Relativistic narrow gap Couette solutions
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_7_sec71.tex` containing the
relativistic extension of Ch VII §71 (narrow gap Couette flow, marginal
stationary state).

### Content produced

1. **Relativistic perturbation equations** (§rel-71-equations): Derived the
   narrow-gap equations with ρ → (ε+p)/c² inertia replacement. Defined
   Ta_rel = 4AΩ₁d⁴(ε+p)²/(η_s²c⁴) and showed
   Ta_rel/Ta_cl = [(ε+p)/(ρ₀c²)]².

2. **Characteristic value problem** (§rel-71-eigenvalue): Demonstrated that the
   secular determinant is structurally identical to the classical one, yielding
   T_c^rel = 3430(ε+p)²/[ρ₀²c⁴(1+μ)] with a_min = 3.12 unchanged.

3. **Numerical results** (§rel-71-numerical): Table of relativistic correction
   factors (1+ξ)² for representative astrophysical regimes, from terrestrial
   (negligible) to ultra-relativistic (factor of 4).

4. **Alternative method** (§rel-71-alternative): Confirmed that the 6th-order
   formulation gives the same numerical results as the 4th-order method, as in
   the classical case.

5. **Approximate solution for μ→1** (§rel-71-approx): Extended the perturbation
   expansion to show T_c^rel = 3416(ε+p)²/[ρ₀²c⁴(1+μ)] ×
   {1 - 7.61×10⁻²[(1-μ)/(1+μ)]²}, with λ⁽¹⁾=0 preserved by parity.

6. **Asymptotic behaviour for (1-μ)→∞** (§rel-71-asymptotic): Showed that
   T_c ~ τ(1-μ)⁴(1+ξ)² with τ≈1182 and a(T_c) ~ q(1-μ) with q≈2.035,
   identical universal constants as classical theory.

### Key physical result

The relativistic modification is a uniform multiplicative factor
[(ε+p)/(ρ₀c²)]² on all critical Taylor numbers. The eigenvalue problem is
isospectral to the classical one because the enthalpy-inertia factor is
spatially uniform in the narrow-gap limit. Israel-Stewart causal corrections
do not affect the stationary marginal state.

## Conventions

- Followed RELATIVISTIC_CONVENTIONS.md (metric signature, c explicit, macros)
- Used `\relcorrection` environment for highlighted relativistic modifications
- Cross-referenced classical equations via \eqref
- Consistent with existing relativistic files in style and notation

## Files

- `output/chapters/relativistic/rel_chapter_7_sec71.tex` — main output
- `progress/relativistic/subagent_32_couette_5_narrowgap.md` — this file
