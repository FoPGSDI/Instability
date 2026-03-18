# Relativistic Conventions and Notation

## Metric Signature
(-,+,+,+) — the "mostly plus" convention (particle physics standard)

## Fundamental Constants
- c: speed of light (kept explicit, NOT set to 1, so non-relativistic limits are transparent)
- G: gravitational constant
- k_B: Boltzmann constant

## 4-Vectors and Tensors
- Greek indices μ,ν,α,β = 0,1,2,3 (spacetime)
- Latin indices i,j,k = 1,2,3 (spatial)
- Einstein summation convention throughout
- g^{μν}: metric tensor (Minkowski η^{μν} for SR, general for GR sections)
- u^μ: 4-velocity, normalized u^μ u_μ = -c²
- Δ^{μν} = g^{μν} + u^μ u^ν / c²: projection tensor onto local rest frame

## Energy-Momentum Tensor
### Perfect fluid:
T^{μν} = (ε + p) u^μ u^ν / c² + p g^{μν}

where ε = energy density (including rest mass), p = pressure

### Dissipative fluid (Israel-Stewart):
T^{μν} = ε u^μ u^ν / c² + (p + Π) Δ^{μν} + π^{μν} + (q^μ u^ν + q^ν u^μ)/c²

where:
- Π: bulk viscous pressure
- π^{μν}: shear stress tensor (traceless, orthogonal to u^μ)
- q^μ: heat flux 4-vector (orthogonal to u^μ)

## Israel-Stewart Relaxation Equations (causal dissipation)
τ_Π u^α ∇_α Π + Π = -ζ ∇_μ u^μ
τ_π u^α ∇_α π^{⟨μν⟩} + π^{μν} = 2η σ^{μν}
τ_q u^α ∇_α q^{⟨μ⟩} + q^μ = -κ (Δ^{μν} ∇_ν T + T u^μ u^α ∇_α T / c²)

where τ_Π, τ_π, τ_q are relaxation times (MUST be > 0 for causality)

## Relativistic MHD
- F^{μν}: Faraday tensor
- b^μ: magnetic field 4-vector in fluid frame: b^μ = (1/2) ε^{μναβ} u_ν F_{αβ} / c
- b² = b^μ b_μ: magnetic pressure parameter
- Ideal MHD condition: F^{μν} u_ν = 0 (E = 0 in fluid frame)
- MHD energy-momentum: T^{μν}_{MHD} = T^{μν}_{fluid} + (b²/2)(u^μ u^ν/c² + g^{μν}/2) - b^μ b^ν

## Characteristic Speeds (Causality Bounds)
All must satisfy v ≤ c:
- Sound speed: c_s² = (∂p/∂ε)_s ≤ c²
- Alfvén speed: v_A² = b²/(4πw + b²) c² where w = (ε+p)/c²
- Fast magnetosonic: v_f² = (c_s² + v_A² - c_s² v_A²/c²) (automatically < c²)
- Slow magnetosonic: v_s² = c_s² v_A² / v_f²
- Israel-Stewart relaxation: ensures finite propagation speed for heat/viscosity

## Dimensionless Numbers (Relativistic)
- Relativistic Rayleigh number: Ra_rel = (αg d³ ΔT / νκ_T) × [1 + corrections O(v²/c²)]
- Relativistic Taylor number: Ta_rel = (4Ω² d⁴ / ν²) × [1 + frame-dragging corrections]
- Relativistic Chandrasekhar number: Q_rel = (μ H² d² / ρ₀ν η) × [1 + v_A²/c² corrections]
- Mach number: M = v/c_s (relevant for compressibility)
- Lorentz factor: γ = (1 - v²/c²)^{-1/2}

## LaTeX Macros (defined in rel_preamble.tex)
\newcommand{\four}[1]{#1^{\mu}}           % 4-vector
\newcommand{\fvel}{u^{\mu}}               % 4-velocity
\newcommand{\proj}{\Delta^{\mu\nu}}       % projection tensor
\newcommand{\emt}{T^{\mu\nu}}             % energy-momentum tensor
\newcommand{\farad}{F^{\mu\nu}}           % Faraday tensor
\newcommand{\covd}{\nabla_{\mu}}          % covariant derivative
\newcommand{\Lf}{\gamma}                  % Lorentz factor
\newcommand{\cs}{c_{\mathrm{s}}}          % sound speed
\newcommand{\vA}{v_{\mathrm{A}}}          % Alfven speed
\newcommand{\enthalpy}{w}                 % relativistic enthalpy density
\newcommand{\taupi}{\tau_{\pi}}           % shear relaxation time
\newcommand{\tauq}{\tau_{q}}             % heat relaxation time
\newcommand{\bulkvisc}{\zeta}             % bulk viscosity
\newcommand{\shearvisc}{\eta_{\mathrm{s}}}% shear viscosity
