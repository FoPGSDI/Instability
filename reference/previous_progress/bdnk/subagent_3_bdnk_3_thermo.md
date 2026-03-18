# Agent 3: BDNK Thermodynamics and Causality

## File modified
- `output/chapters/relativistic/rel_framework_thermo.tex`

## Changes made

### Heat conduction section (Fourier -> BDNK)
- Replaced Fourier -> Cattaneo -> Israel-Stewart progression with Fourier -> BDNK
- Removed telegraph equation (tau d²T/dt² + dT/dt = chi nabla²T) as the causality mechanism
- Explained BDNK resolution: causality through frame choice, not relaxation terms
- Added BDNK heat flux equation Q^mu with frame correction terms F^mu
- Described how the full coupled first-order system is strongly hyperbolic
- Explained that characteristic speeds come from the characteristic polynomial, not from v_T = sqrt(chi/tau_q)

### Viscosity section (IS relaxation -> BDNK first-order)
- Replaced IS shear equation (tau_pi u^alpha nabla_alpha pi + pi = 2 eta sigma) with BDNK: Pi^{mu nu} = -2 eta sigma^{mu nu}
- Replaced IS bulk equation with BDNK: Pi_bulk = -zeta nabla_mu u^mu
- Removed all relaxation times (tau_pi, tau_Pi, tau_q)
- Added full BDNK energy-momentum tensor decomposition with frame coefficients
- Emphasized that u^mu is in general frame (neither Landau nor Eckart)

### Causality bounds (tau > 0 -> BDNK coupled inequalities)
- Replaced IS causality conditions (tau_q > 0, tau_Pi > 0, tau_pi > 0) with BDNK strong hyperbolicity conditions
- Added three BDNK conditions: eta > 0, zeta + (2/3)eta > 0, coupled frame coefficient inequalities
- Noted that BDNK causality proof is nonlinear (not just linearized)
- Added conformal fluid simplified case

### Signal speed table
- Replaced IS signal speed formulas (v_T = sqrt(kappa/(tau_q c_v)), etc.) with BDNK characteristic polynomial description
- Thermal, bulk, and shear speeds now described as emerging from coupled characteristic polynomial
- Removed explicit relaxation-time-dependent speed formulas
- Kept sound, Alfven, and fast magnetosonic speeds unchanged

### Causality checklist
- Updated from IS checks (relaxation times positive, individual signal speeds) to BDNK checks (frame coefficients, strong hyperbolicity, coupled inequalities)

### Unchanged sections
- Relativistic thermodynamics (first law, enthalpy, Gibbs-Duhem, EOS)
- EOS causality constraints (sound speed bound, Le Chatelier)
- Ideal relativistic gas
- Schwarzschild and Ledoux criteria
- Brunt-Vaisala frequency

## Status: COMPLETE
