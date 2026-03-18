---
agent: 34
chapter: 8
sections: 75--76
task: Relativistic curved channel stability (Dean problem)
status: completed
timestamp: 2026-03-18T12:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_8_sec75-76.tex` containing
the relativistic extension of Chandrasekhar Ch. VIII, Sections 75--76
(stability of viscous flow in a curved channel).

### Content produced

1. **Introduction (Sec. rel-75):** Motivation for relativistic treatment of
   curved channel flow; connection to accretion tori and relativistic plasma
   ducts.

2. **Perturbation equations with Israel-Stewart viscosity (Sec. rel-76):**
   - Equilibrium state with enthalpy density replacing rest-mass density.
   - Linearised radial and azimuthal momentum equations incorporating the
     Israel-Stewart relaxation factor $(1 + \tau_\pi^* \sigma_*)$.
   - Relativistic Dean parameter $\Lambda_{\mathrm{rel}}$ with explicit
     $O(V_m^2/c^2)$ corrections from enthalpy and pressure inertia.
   - Boundary conditions including Israel-Stewart stress conditions at walls.

3. **Characteristic value problem for sigma=0 (Sec. rel-76b):**
   - Marginal-state equations with relativistic enthalpy corrections.
   - Galerkin expansion following Dean/Reid method.
   - Secular determinant with classical + relativistic matrix elements.
   - Perturbative solution: $\Lambda_{\mathrm{rel},c} = 92,975[1 + 3.8 V_m^2/c^2 + ...]$.
   - Relativistic critical Reynolds number: lower than classical (enhanced
     inertia destabilises).

4. **Numerical results table (Sec. rel-76c):**
   - Classical vs relativistic critical Dean parameter for $V_m/c = 0$,
     $10^{-2}$, $10^{-1}$, $0.3$, $0.5$.
   - Fractional shifts ranging from $3.8 \times 10^{-4}$ to $0.25$.

5. **Causality: finite viscous signal propagation (Sec. rel-76-causality):**
   - Viscous signal speed $c_{\mathrm{visc}} = \sqrt{\eta_s/(\enthalpy_0 \tau_\pi)}$.
   - Causality bound $\tau_\pi \geq \eta_s/(\enthalpy_0 c^2)$.
   - Non-hydrodynamic relaxation mode $\sigma_* = -1/\tau_\pi^*$.
   - Resolution of the plane-parallel limit difficulty: overstable modes
     propagate at finite speed bounded by $c$.
   - Summary of three governing dimensionless groups.

### Conventions

- Metric signature $(-,+,+,+)$, $c$ kept explicit throughout.
- Israel-Stewart causal dissipation with relaxation time $\tau_\pi$.
- All macros from `rel_preamble.tex` used consistently.
- Classical limit $c \to \infty$, $\tau_\pi \to 0$ recoverable at every stage.

## Issues / Notes

- The numerical coefficient $\mathcal{A} \approx 3.8$ in the critical Dean
  parameter correction is estimated from the 4th-order Galerkin truncation;
  higher-order computation would refine this.
- The overstable branch analysis (connecting Dean to Tollmien-Schlichting)
  is discussed qualitatively; a full numerical treatment of the complex
  eigenvalue problem with Israel-Stewart relaxation is deferred.

## Next

- Integration into `rel_main.tex` table of contents.
- Possible extension to Sections 77--78 (transverse pressure gradient +
  axial flow with relativistic corrections).
