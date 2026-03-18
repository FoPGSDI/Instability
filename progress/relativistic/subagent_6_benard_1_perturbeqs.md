---
agent: 6
chapter: 2 (relativistic)
sections: 5--9
status: completed
timestamp: 2026-03-18T12:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_2_sec5-9.tex` containing the
relativistic generalization of Chandrasekhar Ch II sections 5--9 (Benard problem
perturbation equations).

### Sections produced

- **§5 (Introduction):** Motivation for relativistic treatment — acausal heat
  propagation in Fourier's law, enthalpy density providing inertia, astrophysical
  applications (neutron-star oceans, accretion discs, quark-gluon plasma).

- **§6 (Physical problem):** Heated layer with relativistic fluid; enthalpy density
  w = (ε+p)/c² as inertial mass; enthalpy expansion coefficient α_w ≠ α;
  relativistic Rayleigh number definition.

- **§7 (Basic hydrodynamic equations):** Full relativistic equations:
  - Continuity: ∇_μ(ρ₀ u^μ) = 0
  - Momentum: w u^ν ∇_ν u^μ = -Δ^{μν}∇_ν p + dissipative terms
  - Energy: u^μ ∇_μ ε + (ε+p)∇_μ u^μ = dissipation
  - Israel-Stewart transport: relaxation equations for q^μ, π^{μν}, Π
  - Dissipation function Φ_rel = π^{μν} σ_{μν} + Π ∇_μ u^μ

- **§8 (Boussinesq approximation):** Relativistic version where:
  - Inertial mass density is w₀ = (ε₀+p₀)/c², not ρ₀
  - Pressure contributes to buoyancy via α_w = α + (∂p/∂T)_ρ/(w₀c²)
  - Kinematic viscosity: ν_rel = η_s/w₀
  - Thermal diffusivity: κ_T = κ_IS/(w₀ c_p)

- **§9 (Perturbation equations):** Linearized about static heated-from-below
  equilibrium:
  - δT^{μν} perturbation analysis (momentum density includes q^i/c term)
  - Vertical velocity equation with g α_w replacing g α
  - Telegraph heat equation (Cattaneo-Vernotte) with τ_q relaxation
  - Vorticity equation with ν_rel
  - Boundary conditions (rigid + free, with IS heat-flux condition)
  - **Causality check:** Perturbation system is symmetric hyperbolic when
    τ_q ≥ κ_T/c² and τ_π ≥ ν_rel/c²; thermal signal speed v_heat = √(κ_T/τ_q) ≤ c

### Non-relativistic limit recovery

All equations verified to reduce to Chandrasekhar's classical equations (2), (18),
(39), (41), (43), (55)-(57), (73), (74), (76) when c → ∞, τ_q → 0, w₀ → ρ₀.

### Conventions

Follows RELATIVISTIC_CONVENTIONS.md: metric (-,+,+,+), c explicit, Israel-Stewart
dissipation, u^μ u_μ = -c².

## Issues / Notes

- Shear relaxation time τ_π kept general but rapid-relaxation limit (τ_π → 0)
  used for the final vorticity/velocity equations to maintain closest parallel
  with Chandrasekhar's presentation.
- Full τ_π dynamics available via eqs (rel2-31) + (rel2-32) when needed.
- The enthalpy expansion coefficient α_w is a genuinely new relativistic quantity
  with no classical analogue.

## Next

Sections 10--15 (normal-mode analysis, critical Rayleigh number determination)
should be generalized to the relativistic setting, using the perturbation equations
derived here as the starting point.
