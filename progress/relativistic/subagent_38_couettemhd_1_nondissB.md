---
agent: 38
chapter: 9
sections: 81-83
task: Relativistic non-dissipative Couette flow with magnetic field
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_9_sec81-83.tex` containing
the relativistic generalisation of Chandrasekhar Ch. IX, sections 81--83
(non-dissipative Couette flow in hydromagnetics).

## Content

1. **Section rel-80: Relativistic MHD in cylindrical coordinates**
   - Covariant energy-momentum conservation for magnetised perfect fluid
   - Cylindrical coordinate form of relativistic momentum and induction equations
   - Key replacement: rho -> w = (epsilon+p)/c^2 (enthalpy density)
   - Stationary Couette base flow with axial B-field

2. **Section rel-81: Stability of non-dissipative Couette flow with axial B**
   - Relativistic Alfven frequency Omega_{A,rel}^2 = B_0^2 k^2 c^2 / [4pi(epsilon+p)]
   - Case m=0: eigenvalue problem with real eigenvalues (proof carries over)
   - Variational principle for lambda^2 (Sturmian structure preserved)
   - Relativistic stability criterion: d/dr[(epsilon+p)/c^2 * r^2 Omega]^2 > 0
   - Angular momentum weighted by enthalpy rather than rest-mass density

3. **Section rel-82: Oscillation periods with axial B-field**
   - Omega = const: relativistic magneto-inertial oscillations
   - Dispersion relation sigma^2 - sigma_0 sigma - Omega_{A,rel}^2 = 0
   - Oscillation periods and strong-field Alfven limit
   - Narrow-gap stabilisation: stronger B needed due to enhanced inertia

4. **Section rel-83: Transverse (azimuthal) B-field**
   - Michael's criterion generalised: enthalpy-weighted angular momentum gradient
     must dominate azimuthal field gradient
   - Non-axisymmetric modes: variational formulation extends with Omega_H -> Omega_{H,rel}

5. **Causality section**
   - v_A < c proven: enthalpy in denominator self-regulates
   - Fast/slow magnetosonic speeds subluminal
   - Phase and group velocities of magneto-inertial modes bounded by c
   - Self-regulation mechanism: (epsilon+p) grows with B^2

## Key Relativistic Modifications

- rho -> w = (epsilon+p)/c^2 everywhere as inertial mass
- Omega_A^2 = mu H^2 k^2/(4pi rho) -> B_0^2 k^2 c^2/[4pi(epsilon+p)]
- Rayleigh criterion uses enthalpy-weighted angular momentum
- Stronger B fields needed for stabilisation in relativistic regime
- All mode speeds automatically subluminal

## Issues / Notes

- The functional structure of eigenvalue problems is identical to classical;
  only the definition of Alfven frequency and inertial density changes.
- Notation follows RELATIVISTIC_CONVENTIONS.md: (-,+,+,+) signature,
  c kept explicit, w = (epsilon+p)/c^2.

## Next

No further work needed for this sub-task. Ready for assembly into rel_main.tex.
