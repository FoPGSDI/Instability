---
agent: 25
chapter: 6
section: 59
task: Relativistic fluid sphere onset
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_6_sec59.tex`, a relativistic
generalisation of Chandrasekhar Ch VI §59 (onset of thermal instability in a
self-gravitating fluid sphere).

### Content produced

1. **TOV equilibrium background** (§rel-59-TOV): Schwarzschild interior metric,
   TOV equation, compactness parameter, Schwarzschild interior pressure profile.

2. **Relativistic perturbation equations** (§rel-59-pert): Coupled eigenvalue
   equations for W and F with metric factor e^{-Lambda} and pressure-to-energy
   ratio Xi(r), plus Israel-Stewart parameter Upsilon.

3. **Eigenvalue problem** (§rel-59-eigen): Fourier-Bessel expansion, relativistic
   matrix elements Q_jk^{rel}, secular determinant, first approximation formula.

4. **Cell patterns** (§rel-59-cells): Streamline equation with W^{rel}, l=1
   remains easiest mode.

5. **Newtonian vs relativistic comparison** (§rel-59-comparison): Compact formula
   C_rel = C / [(1+Xi_bar)(1+Upsilon) G(C)], table of C_rel/C ratios for
   compactness 0 to 0.4, table of mode-by-mode comparison at C=0.10.

### Key physics

- Relativistic fluid sphere is *more* unstable (lower critical Rayleigh number)
  due to pressure contribution to inertia, metric curvature, and causal heat
  transport effects.
- For neutron-star compactness (C ~ 0.2), critical parameter reduced by ~50%.
- l=1 remains most unstable mode across all compactness values.
- All results reduce to Newtonian §59 in the limit C -> 0, Upsilon -> 0.

### Conventions

- Follows RELATIVISTIC_CONVENTIONS.md (metric signature, c explicit, macros).
- Uses rel_preamble.tex macros (Rarel, edensity, tauq, etc.).
- relcorrection and causalitycheck environments used for highlighting.

## Issues / Notes

- Numerical values in comparison tables are illustrative (based on perturbative
  expansion in compactness); full numerical solution of the relativistic
  eigenvalue problem would require a numerical ODE solver.

## Next

Ready for git commit and push.
