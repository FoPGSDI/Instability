---
agent: 39
chapter: 9 (relativistic, §84-86)
task: Relativistic Couette flow with axial current and combined fields
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_9_sec84-86.tex`, the
relativistic generalisation of Chapter IX §84-86 from Chandrasekhar's
*Hydrodynamic and Hydromagnetic Stability*.

### Content produced

1. **§84 — Axial current (toroidal B-field), relativistic stability:**
   - Relativistic equilibrium with effective inertia
     rho_eff = gamma^2 w/c^2 + b^2/(4pi c^2).
   - m=0 case: Relativistic Michael discriminant Psi_rel replacing
     Psi, with Lorentz-factor corrections to the centrifugal term
     and enthalpy+magnetic-energy corrections to the inertia.
     Necessary and sufficient stability criterion preserved in form.
   - m!=0 case: Variational integral relation generalised with
     relativistic Alfven frequencies and effective rotation.

2. **§85 — Combined axial + toroidal B, relativistic:**
   - Master equation (9-142) generalised to relativistic regime.
   - Case Omega=0 (pure magnetic stability): Relativistic kink/sausage
     criterion derived; stabilising effect of axial field weakened
     because Omega_{A,rel} < Omega_A.  Sufficient condition
     (H_theta decays faster than 1/r) unchanged.

3. **§86 — General non-dissipative case:**
   - Full eigenvalue problem stated with all three relativistic
     replacements (inertia, rotation, Alfven frequencies).
   - Summary of physical consequences: reduced magnetic stabilisation,
     enhanced centrifugal destabilisation, overall reduced stability.

4. **Causality verification:**
   - All mode phase speeds bounded by relativistic fast magnetosonic
     speed v_f < c (verified in dedicated causalitycheck boxes).
   - Characteristic speed hierarchy v_s < v_A < v_f < c confirmed.

### Non-relativistic limit

Every equation reduces to the classical Chandrasekhar form when
V/c -> 0, v_A/c -> 0, confirming consistency.

## Files

- `output/chapters/relativistic/rel_chapter_9_sec84-86.tex`
- `progress/relativistic/subagent_39_couettemhd_2_current.md`
