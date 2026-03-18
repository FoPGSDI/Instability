# Agent 1: BDNK Hydrodynamics Framework (IS -> BDNK conversion)

## Status: COMPLETE

## File modified
- `output/chapters/relativistic/rel_framework_hydro.tex`

## Changes made

### Removed (Israel-Stewart content)
- Section "Israel-Stewart extended irreversible thermodynamics" and its relaxation equations for tau_pi, tau_q, tau_Pi
- Telegraph equation (tau_q d^2T/dt^2 + dT/dt = kappa nabla^2 T)
- IS relaxation-time causality conditions (tau > 0)
- IS higher-order dispersion relation with O(tau omega^2 k^2) corrections
- All references to dissipative quantities as independent dynamical variables

### Added (BDNK content)
- Section "BDNK general hydrodynamic frame" explaining the general frame (neither Landau nor Eckart)
- BDNK first-order constitutive relations: Pi^{mu nu} = -2 eta sigma^{mu nu}, Q^mu with frame corrections, E = epsilon + epsilon_1
- Frame coefficients epsilon_1, beta_1, alpha_1 and their role
- Strong hyperbolicity conditions (coupled inequalities on transport + frame coefficients)
- Proof sketch: contrast between rigorous BDNK strong hyperbolicity vs approximate IS hyperbolicity
- BDNK heat conduction section: first-order-in-time equation that is causal due to frame terms (replaces telegraph equation)
- Simplified dispersion relation: quadratic in omega (no spurious relaxation modes)
- Shear mode dispersion relation

### Preserved (unchanged)
- Perfect fluid section (Sec 1): four-velocity, EMT, conservation laws, Euler equations
- Linearized perturbation theory: background state, perturbation ansatz, linearized equations, sound waves
- Non-relativistic limit: v/c expansion, recovery of Euler/Navier-Stokes, Chandrasekhar equations
- Relativistic Boussinesq approximation: all subsections unchanged
- Causality bound on sound speed

### References added
- Bemfica, Disconzi & Noronha (2018, 2019)
- Kovtun (2019)
- Hoult & Kovtun (2020)
- Bemfica, Disconzi, Noronha & Kovtun (2023)
