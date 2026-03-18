---
agent: 2
task: relativistic MHD framework
stage: completed
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_framework_mhd.tex` containing the complete
relativistic MHD framework chapter with six main sections:

1. **Covariant Electrodynamics** — Faraday tensor, dual tensor, Maxwell equations in covariant form, electric/magnetic field decomposition in fluid frame.

2. **Ideal Relativistic MHD** — Ideal MHD condition (E^μ = 0 in fluid frame), total energy-momentum tensor T^{μν} = T^{μν}_fluid + T^{μν}_EM with explicit b² terms, covariant induction equation, relativistic Alfvén flux-freezing theorem.

3. **Characteristic Speeds** — Relativistic Alfvén speed v_A² = b²c²/[4π(ε+p)+b²], fast/slow magnetosonic speeds from quartic dispersion, explicit causality proof (all speeds < c).

4. **Resistive Relativistic MHD** — Relativistic Ohm's law with projected current, magnetic diffusivity η_m = c²/(4πσ), relativistic magnetic Reynolds number, Joule dissipation rate, Ohmic decay timescale.

5. **Linearised Perturbations** — Static background with uniform B₀, plane-wave perturbation ansatz, linearised momentum/energy/induction equations, full dispersion relation factoring into Alfvén + magnetosonic branches, explicit recovery of Chandrasekhar Ch IV equations in v/c → 0 limit.

6. **Relativistic Alfvén Waves** — Alfvén dispersion ω² = k²v_A²cos²θ, comparison with Chandrasekhar §39, non-relativistic limit v_A → B/√(4πρ), ultra-relativistic saturation v_A → c, polarisation eigenmodes.

## Conventions

- Metric signature (−,+,+,+), c kept explicit throughout
- All macros from RELATIVISTIC_CONVENTIONS.md used (\vA, \cs, \farad, \fvel, \proj, \enthalpy, etc.)
- Gaussian units with 4π factors
- u^μ u_μ = −c²

## Issues / Notes

- None. All sections complete with cross-references and equation labels.
