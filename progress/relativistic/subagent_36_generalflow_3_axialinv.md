---
agent: 36
chapter: 8
section: 79 (relativistic inviscid axial flow stability)
status: completed
timestamp: 2026-03-18T12:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_8_sec79.tex` containing the
relativistic generalisation of Chapter VIII, sections 78--78(b) (inviscid
stability of flow between coaxial cylinders with an axial pressure gradient).

### Content produced

1. **Relativistic stationary solution** (§rel-8-79a): combined rotation + axial
   flow base state with full Lorentz factor; relativistic pressure balance
   equation; causality bound V^2 + W^2 < c^2.

2. **Relativistic Poiseuille/Hagen flow analog** (§rel-8-79b): pure axial flow
   case; relativistic master equation with Lorentz-weighted curvature function
   Psi_rel; inflexion-point theorem (necessary condition for instability);
   subluminal bounds on phase speed; sufficient condition for instability via
   Sturm-Liouville theory.

3. **General case: rotation + axial flow** (§rel-8-79c): relativistic Rayleigh
   discriminant Phi_rel incorporating both rotation and axial-flow coupling;
   variational principle for c; stability criterion proving that Rayleigh's
   criterion remains the governing one even with arbitrary axial flow.

4. **Sufficient conditions for stability** (§rel-8-79d): collected summary for
   pure axial, rotation+axial, and causality constraints.

5. **Causality checks**: explicit verification that all base-flow speeds and
   perturbation phase speeds remain subluminal; causalitycheck boxes included.

6. **Non-relativistic limits**: all results reduce to the classical
   Chandrasekhar results when gamma -> 1.

## Key relativistic modifications

- Classical Psi(r) replaced by Psi_rel involving d(gamma^2 W)/dr
- Classical Phi(r) replaced by Phi_rel with gamma^2-weighted angular momentum
- Rayleigh criterion: d(r^2 Omega)/dr > 0 becomes d(r^2 gamma^2 Omega)/dr > 0
- Critical layer shifts by O(W^2/c^2) correction
- All flow speeds explicitly bounded by c

## Issues / Notes

- The analysis is for incompressible inviscid flow; compressible relativistic
  extensions would require the full relativistic Euler equations with equation
  of state.
- Israel-Stewart dissipative corrections are not included (inviscid limit).

## Next

No further work needed for this sub-task. The file is ready for integration
into the relativistic main document.
