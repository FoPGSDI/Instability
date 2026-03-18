---
agent: 51
chapter: 11 (relativistic, §105-106)
task: Relativistic KH with rotation and magnetic field effects
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_11_sec105-106.tex`, a
relativistic generalization of Chapter XI §105-106 from Chandrasekhar's
*Hydrodynamic and Hydromagnetic Stability*.

### Key content

1. **Section 105: Rotation effect on relativistic KH** (§rel-11-105)
   - Relativistic Coriolis coupling: effective inertia gamma^2 w replaces rho,
     yielding an enhanced rotation parameter 4 gamma^4 Omega^2 in place of
     the classical 4 Omega^2.
   - Two uniform fluids with rotation: characteristic equation (R7) with
     fluid-dependent relativistic density fractions alpha_j^rel.
   - Graphical analysis: P-, S1-, S2-, C-branches carry over with
     fluid-dependent omega_j parameters.
   - Stability criterion (R11): relativistic generalization of eq. (179).
   - Causality constraint (R12): phase speed bounded by c.

2. **Section 106: Horizontal B-field effect on relativistic KH** (§rel-11-106)
   - Relativistic Alfven speed v_A,rel = b^2/(4pi w + b^2) c^2 < c^2,
     ensuring automatic causality.
   - Two uniform magnetised fluids (parallel field): characteristic equation
     (R16)-(R17) and stability criterion (R18) — relative velocity bounded
     by rms relativistic Alfven speed.
   - Effective surface tension (R20): magnetic field equivalent.
   - Transverse B-field: anisotropic stabilisation; streaming-direction
     instability unaffected (as in classical case).
   - Causality section: combined Alfven + KH mode speeds bounded via fast
     magnetosonic speed v_f^2 = c_s^2 + v_A^2 - c_s^2 v_A^2/c^2 < c^2.

3. **Bibliographical notes**: Classical references (Chandrasekhar, Solberg,
   Michael, Northrop) plus relativistic jet stability literature (Ferrari
   et al., Hardee, Perucho et al., Mizuno et al.) and relativistic MHD
   foundations (Lichnerowicz, Rezzolla & Zanotti, Komissarov).

### Non-relativistic limits

All equations reduce to their classical counterparts when gamma -> 1 and
w -> rho (i.e., c -> infinity).

## Issues / Notes

- The classical §106(a) content was not available (content filter gap), so
  the relativistic version derives the parallel-field case directly from
  relativistic MHD principles rather than following the classical derivation
  step-by-step.
- Causality constraints are boxed throughout for emphasis.

## Next

No further action required for this sub-task.
