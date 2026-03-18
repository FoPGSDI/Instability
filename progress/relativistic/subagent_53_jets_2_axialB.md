---
agent: 53
chapter: 12
section: 110
status: completed
timestamp: 2026-03-18T00:00:00Z
task: Relativistic generalization of Ch XII §110 (axial B-field on gravitational cylinder instability)
---

## Summary

Created `output/chapters/relativistic/rel_chapter_12_sec110.tex` containing the
relativistic generalization of Chandrasekhar's §110: the effect of a uniform axial
magnetic field on the gravitational instability of an infinite cylinder.

## Key content

1. **Relativistic MHD framework**: Energy-momentum tensor for magnetized perfect fluid;
   relativistic enthalpy density w_tot = (ε + p + H²/4π)/c²; effective gravitational
   mass density ρ_G = (ε + 3p + H²/8π)/c².

2. **Relativistic Alfvén speed**: v_A² = H²c²/[4π(ε+p) + H²], automatically < c²
   (causality satisfied).

3. **Dispersion relation**: Generalization of Chandrasekhar eq. (126)/(128) with
   ρ → ρ_G (gravitational source) and ρ → w_tot (inertia). Same Bessel-function
   structure as non-relativistic case.

4. **Critical field strength**: H₀,rel defined so that H²/(8π) competes with
   (ε+p) × gravitational energy. Relativistic pressure enhances gravitational drive
   (ρ_G > ρ₀) while enhanced inertia slows growth.

5. **Qualitative persistence**: No magnetic field can fully stabilize the cylinder
   (logarithmic divergence at long wavelengths unchanged by relativity).

6. **Strong-field asymptotics**: x_a, x_m, σ_max all exponentially suppressed
   with (H/H₀,rel)², same form as classical result but with relativistic scales.

7. **Causality**: v_A < c always; fast magnetosonic speed v_f < c for causal EOS.

8. **Astrophysical application**: Magnetized relativistic jet fragmentation —
   knotty vs smooth vs disrupted jet morphology explained by H/H₀,rel.

## Non-relativistic limit

All equations reduce exactly to Chandrasekhar's §110 results when p → 0,
ε → ρ₀c², H²/(8π) ≪ ρ₀c².

## Files produced

- `output/chapters/relativistic/rel_chapter_12_sec110.tex`
- `progress/relativistic/subagent_53_jets_2_axialB.md` (this file)
