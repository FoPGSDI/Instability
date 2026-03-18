# BDNK (Bemfica-Disconzi-Noronha-Kovtun) Formalism Conventions

## What is BDNK?

BDNK is a **first-order** causal viscous relativistic hydrodynamics formalism.
Unlike Israel-Stewart (IS) which introduces relaxation equations (second-order theory),
BDNK achieves causality through careful choice of hydrodynamic frame and
first-order constitutive relations with constrained transport coefficients.

**Key references:**
- Bemfica, Disconzi & Noronha, Phys. Rev. D 98 (2018) 104064
- Kovtun, JHEP 10 (2019) 034
- Bemfica, Disconzi & Noronha, Phys. Rev. Lett. 122 (2019) 221602
- Hoult & Kovtun, JHEP 06 (2020) 067
- Bemfica, Disconzi, Noronha & Kovtun, Phys. Rev. D 107 (2023) 076012

## Core Differences from Israel-Stewart

| Feature | Israel-Stewart | BDNK |
|---------|---------------|------|
| Order | Second-order (relaxation eqs) | First-order (gradient expansion) |
| Extra DOFs | π^{μν}, q^μ, Π evolve dynamically | None — only (ε, n, u^μ) |
| PDE structure | Conservation + relaxation eqs | Conservation laws ONLY |
| Causality proof | Approximate (linearized) | Rigorous (full nonlinear) |
| Frame choice | Typically Landau or Eckart | General frame (neither Landau nor Eckart) |
| Relaxation times | τ_π, τ_q, τ_Π > 0 required | Not needed — replaced by frame coefficients |
| Dispersion relation | Higher-order polynomial (extra modes) | Standard polynomial (no spurious modes) |
| Strong hyperbolicity | Not proven in general | Proven rigorously |

## BDNK Energy-Momentum Tensor

### General frame decomposition
T^{μν} = E u^μ u^ν / c² + P Δ^{μν} + 2 Q^{(μ} u^{ν)} / c + Π^{μν}

where:
- E = energy density in the general frame (NOT equilibrium ε)
- P = isotropic pressure in the general frame (NOT equilibrium p)
- Q^μ = heat flux (Q^μ u_μ = 0)
- Π^{μν} = traceless anisotropic stress (Π^{μν} u_ν = 0, Π^μ_μ = 0)
- Δ^{μν} = g^{μν} + u^μ u^ν / c²

### BDNK constitutive relations (first-order)
E = ε + ε_1    where ε_1 = -ζ_1 ∇_μ u^μ - β_1 u^μ ∂_μ T / T - α_1 u^μ ∂_μ (μ/T)
P = p + Π_bulk  where Π_bulk = -ζ ∇_μ u^μ + ...
Q^μ = -κ T Δ^{μα} (∂_α (μ/T) + ...) + frame terms
Π^{μν} = -2η σ^{μν}

Key: The frame coefficients (ε_1, additional terms in Q^μ, P) are what make the theory causal.
In Landau frame: Q^μ = 0, ε_1 = 0 → ACAUSAL (Eckart's problem)
In BDNK general frame: frame coefficients chosen to ensure hyperbolicity.

## BDNK Causality Conditions

The transport coefficients must satisfy coupled nonlinear inequalities:

### For a conformal fluid (simplest case):
η > 0   (shear viscosity positive)
The characteristic speeds are bounded by:
v_char² ≤ c² provided the BDNK coefficients satisfy specific bounds

### General case:
The system is strongly hyperbolic (hence causal) if and only if:
1. η > 0 (positive shear viscosity)
2. ζ + (2/3)η > 0 (positive bulk+shear combination)
3. The frame coefficients satisfy a set of coupled inequalities
   (these replace the IS requirement τ > 0)

### Characteristic speeds in BDNK:
Unlike IS which has extra "relaxation modes" at speed ~ √(η/(τ_π ρ)),
BDNK has ONLY the physical hydrodynamic modes:
- Sound modes: modified by viscosity, speed ≤ c
- Shear modes: ω = -i η k² / (w/c²) + O(k³) [diffusive at low k, causal at high k]
- Heat mode (if present): similarly bounded

## LaTeX Macros for BDNK

\newcommand{\Efr}{E}                    % frame energy density
\newcommand{\Pfr}{P}                    % frame pressure
\newcommand{\Qheat}{Q^{\mu}}           % heat flux 4-vector
\newcommand{\Pistress}{\Pi^{\mu\nu}}   % anisotropic stress
\newcommand{\shearvisc}{\eta}           % shear viscosity
\newcommand{\bulkvisc}{\zeta}           % bulk viscosity
\newcommand{\thermcond}{\kappa}         % thermal conductivity
\newcommand{\sheartensor}{\sigma^{\mu\nu}} % shear tensor
\newcommand{\expansion}{\theta}         % expansion scalar ∇_μ u^μ

% BDNK frame coefficients
\newcommand{\epsone}{\varepsilon_1}    % energy correction
\newcommand{\betaone}{\beta_1}         % temperature gradient coefficient
\newcommand{\alphaone}{\alpha_1}       % chemical potential coefficient

## Key Replacement Rules: IS → BDNK

When converting Israel-Stewart equations to BDNK:

1. **Remove all relaxation equations**: Delete τ_π, τ_q, τ_Π and their evolution equations
2. **Replace IS constitutive relations** with BDNK first-order:
   - IS: τ_π u^α ∇_α π^{⟨μν⟩} + π^{μν} = 2η σ^{μν}
   - BDNK: Π^{μν} = -2η σ^{μν} (first-order, no relaxation)
3. **Replace IS heat flux** with BDNK:
   - IS: τ_q u^α ∇_α q^{⟨μ⟩} + q^μ = -κ(...)
   - BDNK: Q^μ = -κ T Δ^{μα} ∂_α(μ/T) + frame correction terms
4. **Replace causality conditions**:
   - IS: τ_π > 0, τ_q > 0, τ_Π > 0
   - BDNK: coupled inequalities on (η, ζ, κ, frame coefficients)
5. **Simplify dispersion relations**: Remove extra IS relaxation modes
   - IS gives higher-order polynomial (e.g., quintic for thermal)
   - BDNK gives standard polynomial (cubic for thermal) — SAME physical modes
6. **Replace "telegraph equation"** with standard dissipative wave equation
   - IS: τ ∂²T/∂t² + ∂T/∂t = κ ∇²T (telegraph)
   - BDNK: ∂T/∂t = κ_eff ∇²T but with modified dispersion ensuring causality
7. **Frame specification**: State explicitly that BDNK uses a general frame
   where the fluid 4-velocity u^μ is NOT the Landau frame velocity

## Non-relativistic Limit
In the limit v/c → 0:
- BDNK reduces to standard Navier-Stokes (same as IS)
- Frame corrections vanish at O(v²/c²)
- All Chandrasekhar results recovered identically

## Metric and Notation (unchanged from relativistic branch)
- Signature: (-,+,+,+)
- c: kept explicit
- u^μ u_μ = -c²
- w = ε + p (enthalpy density)
- Δ^{μν} = g^{μν} + u^μ u^ν / c²
