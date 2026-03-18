---
agent: 14
chapter: 3
sections: 29-31
task: Relativistic overstability with rotation
status: completed
timestamp: 2026-03-18T12:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_3_sec29-31.tex` containing
the relativistic (Israel-Stewart) extension of Ch III sections 29-31 on
overstability in a rotating fluid layer.

### Section-by-section content

- **Section 29 (relativistic):** Derived the Israel-Stewart dispersion relation
  for overstability.  The classical cubic characteristic equation becomes a
  quintic due to two additional relaxation modes (heat flux and shear stress).
  Oscillatory solutions sigma = i*omega identified; conditions for overstability
  derived with relativistic corrections at O(p0/(rho*c^2)).  Critical Prandtl
  number p* = 0.67659 receives a small relativistic shift.

- **Section 30 (relativistic):** Extended the variational principle for
  discriminating stationary vs oscillatory onset.  The variational functional
  retains its extremal (but not minimal) character.  Boundary conditions are
  unchanged since they are local.  The algorithm (compare Ra_c vs Ra_o) remains
  valid; the two relaxation-mode roots stay in the left half-plane for all Ra.

- **Section 31 (relativistic):** Numerical results for all three boundary
  condition sets (free-free, rigid-rigid, rigid-free).  Asymptotic scaling laws
  T^{2/3} for R_c and T^{1/2} for |sigma| are preserved; only prefactors
  receive O(p0/(rho*c^2)) corrections.  Summary table provided.

- **Causality verification:** Demonstrated that Israel-Stewart thermal
  characteristic speed v_th = sqrt(kappa/(tau_q * c_v * rho)) <= c.  All five
  modes of the quintic have causal phase velocities.  The classical infinite
  propagation speed pathology is resolved.

## Conventions

- Followed RELATIVISTIC_CONVENTIONS.md and rel_preamble.tex macros throughout.
- Used \relcorr, \causalitycheck, \relcorrection environments from rel_preamble.
- Kept c explicit (not set to 1) per convention.
- All results reduce to Chandrasekhar's classical results in c -> infinity limit.

## Files created

1. `output/chapters/relativistic/rel_chapter_3_sec29-31.tex`
2. `progress/relativistic/subagent_14_rotation_3_overstab.md` (this file)
