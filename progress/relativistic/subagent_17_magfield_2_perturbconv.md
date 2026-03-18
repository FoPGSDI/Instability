---
agent: 17
chapter: 4
sections: 41-44
task: Relativistic thermal+magnetic perturbations and stationary convection
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_4_sec41-44.tex` containing
the relativistic generalization of Chapter IV, §41--44 (perturbation equations
for thermal instability with a vertical magnetic field, and stationary
convection solutions).

### §41 (General considerations)
- Alfven speed bound v_A < c from relativistic MHD
- Causal heat transport via Israel-Stewart with finite thermal signal speed

### §42 (Perturbation equations)
- Linearized relativistic MHD equations with ρ₀ → w₀/c² (enthalpy inertia)
- Israel-Stewart heat equation (telegrapher form) replacing parabolic Fourier law
- Normal mode analysis with relativistic Chandrasekhar number Q_rel
- Boundary conditions (Cases A and B) from covariant junction conditions on F^{μν}

### §43 (Stationary convection — variational principle)
- Marginal-state equations formally identical to classical with (R,Q)→(Ra_rel,Q_rel)
- Israel-Stewart terms vanish at σ=0
- Variational principle for Ra_rel as Rayleigh quotient
- Thermodynamic significance: minimum entropy production via covariant ∇_μ s^μ ≥ 0

### §44 (Solutions)
- Two free boundaries: W = A sin πz, characteristic equation with Q_rel
- π²Q law persists: Ra_rel^(c) → π² Q_rel for Q_rel → ∞
- Two rigid boundaries: variational/secular determinant with Q→Q_rel
- One rigid + one free: geometric reduction from rigid-rigid, unchanged relativistically
- Cell patterns: narrowing with Q_rel, but slightly wider than classical (increased inertia)
- Critical gradient reduced by factor ρ₀c²/w₀ relative to classical

### Causality verification
- Stationary modes: v_phase = 0 ✓
- Alfven modes: v_A < c ✓
- Thermal modes: v_q = √(κ_T/τ_q) ≤ c ✓
- Fast magnetosonic: v_f² = c_s² + v_A² - c_s²v_A²/c² < c² ✓
- Overstable modes: bounded by max(v_A, v_f, v_q) < c ✓

## Key relativistic corrections
- Q_rel = Q · ρ₀c²/(ε₀+p₀), reducing Q by O(v_A²/c²)
- Critical β_c reduced by same factor (field more effective due to increased inertia)
- π²Q universality law unchanged

## Issues / Notes
- None. The formal structure at σ=0 is identical to the classical problem.

## Next
- §45-46 (strong-field limit, overstability with magnetic field) to be handled by other agents.
