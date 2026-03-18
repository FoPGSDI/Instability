---
agent: 50
chapter: 11
section: 104
task: Relativistic shear layer instability (Kelvin-Helmholtz, part 3)
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_11_sec104.tex` containing
the relativistic generalisation of Chandrasekhar Ch XI section 104 (shear layer
instability in an unbounded heterogeneous inviscid fluid, Drazin's
hyperbolic-tangent profile).

## Content

The new section covers:

1. **Relativistic equilibrium shear layer** -- Drazin's profile
   V = V_0 tanh(z/d) with the associated Lorentz factor gamma(z) and
   enthalpy-based equilibrium condition.

2. **Linearised perturbation equations** -- Derivation of the relativistic
   Rayleigh equation with enthalpy inertia w*gamma^2, compressibility
   factor, and relativistic Doppler shift.  Definition of the relativistic
   Richardson number J_rel.

3. **Relativistic Drazin solution (incompressible)** -- Perturbative
   extension of Drazin's closed-form trick.  Marginal curve
   J_rel = k^2(1-k^2)[1 + O(V_0^2/c^2)] with explicit leading correction.
   Maximum J_max^rel = 1/4(1 + V_0^2/3c^2 + ...).

4. **Compressible relativistic shear layer** -- Vortex-sheet dispersion
   relation, growth rate sigma = k V_0 gamma_0 in incompressible limit,
   compressible stabilisation threshold V_0 > c_s/sqrt(1+c_s^2/c^2).

5. **Astrophysical application: relativistic jets (Gamma >> 1)** --
   Lab-frame growth rate scaling as Gamma_j^{-2}, explaining jet
   collimation over Mpc scales.  Role of equation of state (c_s = c/sqrt(3)
   for ultra-relativistic gas).

6. **Comparison table** -- Classical vs relativistic results for all key
   quantities.

7. **Non-relativistic limit** -- Explicit verification that all results
   reduce to Chandrasekhar's equations (11-95) through (11-135).

## Conventions

All conventions follow RELATIVISTIC_CONVENTIONS.md:
- Signature (-,+,+,+)
- c kept explicit
- Four-velocity normalised u^mu u_mu = -c^2
- Enthalpy density w = (epsilon+p)/c^2
- LaTeX macros: \Lf, \cs, \enthalpy, etc.

## Issues / Notes

- The full Drazin closed-form solution does not carry over exactly to the
  relativistic case because the effective velocity profile hat{U}(z) is no
  longer exactly tanh.  The perturbative expansion to O(V_0^2/c^2) is used
  instead, which is exact in the NR limit.
- For Gamma >> 1 jets, the vortex-sheet approximation is more appropriate
  than the smooth-profile analysis.

## Next

No further work needed for this sub-task.
