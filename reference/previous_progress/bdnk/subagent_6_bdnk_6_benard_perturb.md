# Agent 6: BDNK Benard Perturbation Equations (Ch II Sections 5-9)

## Status: COMPLETE

## File Modified
- `output/chapters/relativistic/rel_chapter_2_sec5-9.tex`

## Changes Made

### Section 5 (Introduction)
- Replaced Israel-Stewart description with BDNK formalism overview
- Removed references to tau_q as a dimensionless parameter affecting onset
- Emphasized that BDNK achieves causality through frame choice, not relaxation times
- Simplified non-relativistic limit: c -> infinity only (no tau_q -> 0 needed)

### Section 6 (Nature of the physical problem)
- Replaced discussion of tau_q role with BDNK frame-coefficient mechanism
- Removed tau_q kappa_T/d^2 as an additional dimensionless parameter
- Noted perturbation equations are lower order than IS yet still hyperbolic

### Section 7 (Basic hydrodynamic equations)
- **Section 7a (T^{mu nu})**: Rewrote in BDNK general-frame decomposition with E, P, Q^mu, Pi^{mu nu}; added algebraic constitutive relations (eqs 7a-7d); added remark on Landau frame acausality
- **Section 7c (Momentum)**: Noted BDNK requires no separate evolution equations for dissipative fluxes
- **Section 7d (Energy)**: Noted Q^mu determined by constitutive relation, no separate evolution equation
- **Section 7e (Transport)**: Complete rewrite - replaced IS relaxation equations (telegraph eq for q^mu, relaxation eq for pi^{mu nu}, relaxation eq for Pi) with BDNK algebraic constitutive relations. No tau_q, tau_pi, tau_Pi. Added comparison paragraph.
- **Section 7f (Dissipation)**: Used Pi^{mu nu} = -2 eta sigma^{mu nu} to write explicit dissipation function

### Section 8 (Boussinesq approximation)
- Replaced "relaxation times tau_q, tau_pi" with "BDNK frame coefficients" in constant-transport-coefficients prescription
- Momentum equation now has eta nabla^2 u_i directly (algebraic substitution)
- Heat equation described as first-order-in-time (not telegraph)

### Section 9 (Perturbation equations)
- **Section 9a (Equilibrium)**: Updated notation Q^mu, Pi^{mu nu}, Pi_bulk
- **Section 9b (Perturbation of T^{mu nu})**: Perturbation variables are only (u^i, theta, delta p); Q^mu, Pi^{mu nu} determined algebraically from gradients
- **Section 9c (Linearized motion)**: Equation is directly first-order in time; added remark comparing with IS tau_pi relaxation
- **Section 9d (Linearized heat)**: MAJOR CHANGE - replaced telegraph equation (tau_q d^2 theta/dt^2 + d theta/dt = ...) with first-order BDNK heat equation (d theta/dt = beta w + kappa_T nabla^2 theta). Explicit comparison with IS telegraph equation included.
- **Section 9e (Solenoidal)**: Unchanged
- **Section 9f (Vorticity/vertical velocity)**: Removed "rapid-relaxation limit for shear stress" language; system is naturally first-order
- **Section 9g (Boundary conditions)**: Removed IS-specific boundary condition on q_z (eq 42); noted BDNK needs no extra BC since Q_z is algebraically determined
- **Section 9h (Causality)**: Complete rewrite - replaced IS causality check (tau_q >= kappa_T/c^2, tau_pi >= nu/c^2, symmetric hyperbolic in Geroch-Lindblom sense) with BDNK causality (positive dissipation conditions, coupled frame-coefficient inequalities, subluminal characteristic speeds, strong hyperbolicity in BDN sense). Added dispersion relation comparison. Referenced Bemfica et al. 2023.
- **Summary equations**: Heat equation (ii) is now first-order; removed tau_q, tau_pi from causality bounds; replaced with BDNK frame-coefficient conditions

## Key Physics Changes
1. System order reduced: heat equation first-order in time (was second-order telegraph)
2. No relaxation times (tau_q, tau_pi, tau_Pi) anywhere in the formalism
3. Causality from BDNK frame coefficients, not relaxation-time bounds
4. Fewer independent dynamical variables (Q^mu, Pi^{mu nu} are algebraic)
5. Fewer boundary conditions needed (no BC for q_z)
6. Dispersion relation is lower-degree polynomial (no spurious relaxation modes)
7. Strong hyperbolicity proven rigorously (not just linearized)
