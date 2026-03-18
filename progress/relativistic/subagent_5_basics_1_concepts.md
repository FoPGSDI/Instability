---
agent: 5
chapter: 1 (relativistic)
task: Relativistic basic concepts
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_1.tex`, a relativistic
generalization of Chapter I (Basic Concepts) from Chandrasekhar's
*Hydrodynamic and Hydromagnetic Stability*.

### Key content

1. **Relativistic fluid equations** (Section 2):
   - Perfect-fluid energy-momentum tensor and relativistic Euler equations
     derived from conservation of T^{μν} and baryon current.
   - Israel-Stewart causal dissipative theory replacing Navier-Stokes:
     relaxation equations for bulk viscous pressure Π, shear stress π^{μν},
     and heat flux q^μ, with positive relaxation times τ_Π, τ_π, τ_q
     guaranteeing causality.

2. **Normal-mode analysis** (Section 3):
   - Perturbations of (ε, u^μ, Π, π^{μν}, q^μ) around a stationary
     background, respecting the 4-velocity normalization constraint.
   - Mode decomposition in plane, cylindrical, and spherical geometries.
   - Eigenvalue problem p_k = p_k^(r) + i p_k^(i) with the same
     stability/marginal/overstability classification as the classical theory.
   - **Causality constraint**: phase and group velocities of all modes ≤ c,
     automatically enforced by Israel-Stewart when relaxation times are positive.

3. **Relativistic dimensionless numbers** (Section 4):
   - Re_rel, Pr_rel, Ra_rel, Ta_rel, Q_rel defined with relativistic
     corrections of order v²/c².
   - Characteristic speeds (sound, Alfvén, fast/slow magnetosonic) shown
     to be sub-luminal by algebraic identities.
   - Relativistic Mach number.

4. **Non-relativistic limit** (Section 5):
   - Explicit demonstration that every equation reduces to Chapter I
     when v/c → 0, ε → ρc², τ → 0.

5. **Bibliographical notes** referencing Israel, Stewart, Synge, Anile,
   Romatschke, Lichnerowicz, and Komissarov.

## Conventions

- Metric signature (−,+,+,+), c kept explicit, u^μ u_μ = −c².
- All notation follows RELATIVISTIC_CONVENTIONS.md.

## Issues / Notes

- None. The chapter is self-contained and references the classical Chapter I
  for comparison.
