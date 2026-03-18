---
agent: 9
chapter: 2
section: 15
task: Relativistic exact solutions of the characteristic value problem
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_2_sec15.tex` containing the
relativistic modification of Chapter II, Section 15 (Exact solutions of the
characteristic value problem for thermal instability).

### Content produced

1. **Relativistic eigenvalue equation**: Demonstrated that the sixth-order
   operator structure is unchanged; all relativistic physics enters through the
   definition of the relativistic Rayleigh number Ra_rel = R / [(1+Xi)(1+Upsilon)],
   where Xi = p_0/(epsilon_0 c^2) (pressure-to-inertia ratio) and
   Upsilon = tau_q kappa_T / d^2 (Israel-Stewart relaxation parameter).

2. **Two free boundaries**: Ra_rel^(c) = 27 pi^4 / 4 = 657.511 (unchanged);
   classical R_c^(rel) = 657.511 (1+Xi)(1+Upsilon).

3. **Two rigid boundaries**: Ra_rel^(c) = 1707.762 at a_c = 3.117 (unchanged);
   classical R_c^(rel) = 1707.762 (1+Xi)(1+Upsilon). Worked example: for
   quark-gluon plasma with p ~ epsilon/3, the correction is ~25%.

4. **One rigid, one free boundary**: Ra_rel^(c) = 1100.65 at a_c = 2.682
   (unchanged); classical R_c^(rel) = 1100.65 (1+Xi)(1+Upsilon).

5. **Summary table**: Classical vs relativistic critical values for all three
   boundary types.

6. **Key physical insight**: Pressure contribution to inertia LOWERS the
   effective Rayleigh number, making the system MORE unstable at a given
   temperature gradient. Highlighted in a `relcorrection` environment.

7. **Causality verification**: Verified that critical modes (stationary at onset)
   and near-critical modes propagate causally. Israel-Stewart relaxation ensures
   thermal signal speed v_th = sqrt(kappa_T / tau_q) <= c.

### Design decisions

- The operator structure of the eigenvalue problem is identical to the classical
  case, so the eigenfunctions and critical wavenumbers are unchanged. This is a
  clean result: all relativistic corrections factor out into the definition of
  Ra_rel.
- Used the `relcorrection` and `causalitycheck` environments from rel_preamble.tex.
- Cross-references to classical equations (eq:2-187 through eq:2-227) are preserved.

## Issues / Notes

- The relativistic corrections are multiplicative, not additive to the operator.
  This is specific to the Boussinesq approximation; compressible relativistic
  convection would have a more complex eigenvalue structure.
- For neutron-star ocean conditions, Xi can be O(0.1-1), making the corrections
  astrophysically significant.

## Next

This section can be integrated into a full relativistic Chapter II by including
it via `\input{rel_chapter_2_sec15}` in the appropriate location.
