---
agent: 8
chapter: 2
sections: 13-14
task: Relativistic variational principles and thermodynamic significance
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_2_sec13-14.tex` containing
the relativistic extension of Chapter II, Sections 13--14.

### Section 13: Relativistic variational principles

- Derived the relativistic characteristic value problem with enthalpy-weighted
  inertia: $(D^2-a^2)F_{\mathrm{rel}} = -\mathrm{Ra_{rel}}\,a^2\,(w/c^2)\,W$
- First variational principle: relativistic Rayleigh quotient with weight
  $w/c^2 = (\varepsilon+p)/c^2$ replacing $\rho$ in the denominator integral
- Proved stationary property and minimum property of the lowest $\mathrm{Ra_{rel}}$
- Orthogonality of eigenfunctions with respect to the enthalpy-weighted
  inner product
- Second variational principle in terms of temperature perturbation $\Theta$

### Section 14: Thermodynamic significance

- Relativistic viscous dissipation rate with enthalpy-inertia factor
- Relativistic buoyancy energy release rate
- Energy balance yields the same Rayleigh quotient, confirming physical
  interpretation: instability at minimum temperature gradient balancing
  viscous dissipation against buoyancy release
- Connection to Israel-Stewart entropy current and the covariant second law
  $\nabla_\mu s^\mu \geq 0$
- Maximum entropy production principle promoted to covariant form

### Non-relativistic recovery

- All seven key results verified to reduce to their classical counterparts
  when $w \to \rho_0 c^2$
- Corrections are O(p/rho_0 c^2)

### Causality verification

- Israel-Stewart relaxation times do not appear at marginal stability
  ($\sigma=0$) but bound signal speeds for growing perturbations
- Standard causality bounds on $\tau_\pi$ ensure $v_{\mathrm{signal}} \leq c$

## Files created

- `output/chapters/relativistic/rel_chapter_2_sec13-14.tex`
- `progress/relativistic/subagent_8_benard_3_variational.md` (this file)
