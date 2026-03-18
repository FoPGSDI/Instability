---
agent: 33
chapter: 7
sections: 72-73
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Relativistic generalization of Chapter VII §72-73 (exchange of stabilities and wide gap solutions for Couette flow).

### §72: Exchange of stabilities — relativistic proof
- Extended the classical energy argument to the Israel-Stewart causal dissipation framework
- Showed that the Israel-Stewart relaxation time tau_pi modifies the viscous operator from parabolic to hyperbolic
- Proved that Im(sigma)=0 (stationary marginal state) is preserved under relativistic corrections when T_rel > 0 and the system is near marginal stability
- Noted that for mu < 0 (counter-rotating cylinders) overstability cannot be excluded, same as classical case

### §73: Wide gap solutions — relativistic
- Derived relativistic Taylor number T_rel and stability parameter kappa_rel with explicit correction terms
- Showed the eigenvalue problem structure is identical to classical; only T and kappa are shifted
- Obtained the characteristic equation (secular determinant) with T -> T_rel replacement
- Provided numerical comparison table for eta = 1/2 at various kappa values
- Analyzed gap ratio dependence: narrow gap (eta->1), wide gap (eta->0), and intermediate cases
- Derived relativistic critical angular velocity and showed stability boundary shifts inward

### Key relativistic effects
- Enhanced effective inertia (enthalpy w > rho_0) lowers critical Taylor number
- Correction parameter delta_rel ~ p/(rho c^2) ~ 1% for hot astrophysical fluids
- Wave number at onset practically unchanged
- Causality trivially satisfied at stationary marginal state

## Files created
- `output/chapters/relativistic/rel_chapter_7_sec72-73.tex`
- `progress/relativistic/subagent_33_couette_6_widegap.md`

## Issues / Notes
- The numerical table values assume a fiducial p/(rho c^2) = 0.01; actual astrophysical values vary
- Counter-rotating case (mu = -1) merits dedicated numerical investigation for relativistic overstability

## Next
- Git commit and push
