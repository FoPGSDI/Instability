---
agent: 7
chapter: 2 (sections 10-12)
task: Relativistic normal modes and exchange of stabilities
status: completed
timestamp: 2026-03-18T00:00:00Z
branch: relativistic
---

## Summary

Created `output/chapters/relativistic/rel_chapter_2_sec10-12.tex` containing the
relativistic modification of Chapter II, sections 10--12 of Chandrasekhar's
*Hydrodynamic and Hydromagnetic Stability*.

### Section 10: Normal mode analysis (relativistic)
- Perturbation ansatz exp[i(k_x x + k_y y) + sigma t] retained, but the
  linearised equations now include Israel-Stewart relaxation terms for both
  shear stress (tau_pi) and heat flux (tau_q).
- The dispersion relation becomes a **fifth-order** polynomial in sigma
  (vs. cubic classically), producing 3 physical modes + 2 transient
  relaxation modes.
- Transient modes decay on the microscopic relaxation time-scale and do not
  participate in convective instability.
- Causality constraint: group velocities bounded by sqrt(nu/tau_pi) and
  sqrt(kappa/tau_q), both <= c by Israel-Stewart bounds.

### Section 11: Exchange of stabilities (relativistic)
- Chandrasekhar's integration-by-parts proof is extended.  The Israel-Stewart
  remainder term R_IS contributes Im(sigma) = O(tau_pi, tau_q), which is
  O(v^2/c^2) — vanishing in the non-relativistic limit.
- The principle of exchange of stabilities is therefore valid to extraordinary
  accuracy for any macroscopic fluid.

### Section 12: Marginal state and characteristic value problem
- At sigma = 0, all Israel-Stewart correction terms vanish (they are
  proportional to sigma).  The marginal-state equations are structurally
  identical to the classical ones, with R replaced by Ra_rel.
- The critical Rayleigh number receives only O(v^2/c^2) corrections:
  Ra_rel^(crit) = R_c^(class) [1 + O(v^2/c^2)].
- Causality verification box confirms all modes are subluminal.

## Conventions
- Metric signature (-,+,+,+), c kept explicit throughout.
- Uses macros from rel_preamble.tex (taupi, tauq, Rarel, etc.).
- Environments: `causalitycheck` (yellow box) and `relcorrection` (blue box).

## Files produced
- `output/chapters/relativistic/rel_chapter_2_sec10-12.tex`
- `progress/relativistic/subagent_7_benard_2_normalmodes.md` (this file)

## Non-relativistic limit
Every equation reduces to the corresponding Chandrasekhar equation when
c -> infinity (tau_pi, tau_q -> 0, Ra_rel -> R).

## Next
This file is ready to be included in rel_main.tex via
`\input{rel_chapter_2_sec10-12}`.
