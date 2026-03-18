# Relativistic Modification Master Plan

## Central Task
Make ALL calculations in Chandrasekhar's "Hydrodynamic and Hydromagnetic Stability" relativistic.

## Causality Enforcement
Every modification MUST ensure:
1. All signal speeds ≤ c (speed of light)
2. Use Israel-Stewart formalism for dissipative processes (NOT Eckart/Fourier which are acausal)
3. Relativistic dispersion relations must have subluminal group velocities
4. Energy conditions (weak, strong, dominant) must be satisfied
5. Covariant formulation using 4-vectors and tensors throughout

## Framework
- **Hydrodynamics**: Replace Navier-Stokes with relativistic Euler + Israel-Stewart dissipation
- **MHD**: Covariant GRMHD (ideal + resistive)
- **Thermodynamics**: Relativistic enthalpy w = ε + p, with ε = rest-mass energy + internal energy
- **Gravity**: Newtonian → post-Newtonian or GR (Tolman-Oppenheimer-Volkoff for equilibrium)

## Key Replacements
| Classical | Relativistic |
|-----------|-------------|
| ρ (mass density) | ρ₀ = rest-mass density, w = (ε+p)/c² (inertial mass density) |
| p (pressure) | p appears in inertia: (ε+p)/c² replaces ρ in momentum eq |
| ∂/∂t + v·∇ | uᵘ∇ᵤ (covariant convective derivative along 4-velocity) |
| Navier-Stokes | ∇ᵤTᵘᵛ = 0 with Tᵘᵛ = (ε+p)uᵘuᵛ + pgᵘᵛ + πᵘᵛ |
| Fourier heat law q = -κ∇T | Israel-Stewart: τ_q u^α ∇_α q^μ + q^μ = -κ(∇^μ T - T u^μ u^α ∇_α T/c²) |
| Ohm's law | Relativistic Ohm's law: jᵘ = σ Fᵘᵛ uᵥ |
| Maxwell eqs | ∇ᵤFᵘᵛ = jᵛ/c, ∇_{[α}F_{βγ]} = 0 |
| ∇²φ = 4πGρ | Gᵘᵛ = 8πG/c⁴ Tᵘᵛ (or post-Newtonian for weak gravity) |
| Alfvén speed v_A = B/√(4πρ) | v_A = B/√(4π(ε+p)/c² + B²/c²), capped at c |
| Sound speed c_s² = dp/dρ | c_s² = (∂p/∂ε)_s, must satisfy c_s ≤ c/√3 (for ideal gas) |
| Rayleigh number Ra | Relativistic Ra with w replacing ρ, relativistic heat flux |
| Taylor number Ta | Relativistic Ta with frame-dragging corrections |
| Jeans length λ_J | Relativistic Jeans: λ_J,rel includes pressure contribution to gravity |

## Causality Bounds (Critical)
- Sound speed: c_s² = ∂p/∂ε|_s ≤ c² (stability of EOS)
- Alfvén speed: v_A² = B²/(4πw + B²/c²) < c² (automatically satisfied)
- Phase velocities of perturbation modes: must check for each instability
- Israel-Stewart relaxation times: τ_π, τ_q > 0 (ensures hyperbolicity)
- Group velocity of all wave modes ≤ c

## Agent Decomposition (60 agents)

### Phase 0 — Prerequisites (Agents 1–4, MUST complete before Phase 1)
| Agent | Task | Output File |
|-------|------|-------------|
| 1 | Relativistic hydrodynamics framework | rel_framework_hydro.tex |
| 2 | Relativistic MHD framework | rel_framework_mhd.tex |
| 3 | Relativistic thermodynamics + causality | rel_framework_thermo.tex |
| 4 | Shared LaTeX macros + preamble update | rel_preamble.tex |

### Phase 1 — Independent Chapter Modifications (Agents 5–56, parallel)

#### Ch I: Basic Concepts
| 5 | Relativistic basic concepts, normal modes in SR | rel_chapter_1.tex |

#### Ch II: Bénard / Thermal Instability
| 6 | Perturbation equations (relativistic) §5-9 | rel_chapter_2_sec5-9.tex |
| 7 | Normal mode analysis + exchange of stabilities §10-12 | rel_chapter_2_sec10-12.tex |
| 8 | Variational principles (relativistic) §13-14 | rel_chapter_2_sec13-14.tex |
| 9 | Exact solutions §15 | rel_chapter_2_sec15.tex |
| 10 | Cell patterns §16 | rel_chapter_2_sec16.tex |
| 11 | Variational solution + experiments §17-18 | rel_chapter_2_sec17-18.tex |

#### Ch III: Thermal + Rotation
| 12 | Rotating frame equations §19-23 | rel_chapter_3_sec19-23.tex |
| 13 | Perturbation eqs + stationary convection §24-28 | rel_chapter_3_sec24-28.tex |
| 14 | Overstability + discrimination §29-31 | rel_chapter_3_sec29-31.tex |
| 15 | Special cases + thermodynamics §32-35 | rel_chapter_3_sec32-35.tex |

#### Ch IV: Thermal + Magnetic Field
| 16 | Hydromagnetic equations §36-40 | rel_chapter_4_sec36-40.tex |
| 17 | Perturbation eqs + stationary convection §41-44 | rel_chapter_4_sec41-44.tex |
| 18 | Q-law + overstability §45-46 | rel_chapter_4_sec45-46.tex |
| 19 | Different H-g directions + experiments §47-48 | rel_chapter_4_sec47-48.tex |

#### Ch V: Thermal + Rotation + B-field
| 20 | Combined effects + wave propagation §49-50 | rel_chapter_5_sec49-50.tex |
| 21 | Perturbation eqs + stationary convection §51-52 | rel_chapter_5_sec51-52.tex |
| 22 | Overstability + experiments §53-54 | rel_chapter_5_sec53-54.tex |

#### Ch VI: Thermal in Spheres
| 23 | Perturbation equations spherical §55-56 | rel_chapter_6_sec55-56.tex |
| 24 | Exchange of stabilities + variational §57-58 | rel_chapter_6_sec57-58.tex |
| 25 | Fluid sphere onset §59 | rel_chapter_6_sec59.tex |
| 26 | Spherical shells §60 | rel_chapter_6_sec60.tex |
| 27 | Rotation in sphere §61-63 | rel_chapter_6_sec61-63.tex |

#### Ch VII: Couette Flow
| 28 | Rayleigh criterion (relativistic) §64-66 | rel_chapter_7_sec64-66.tex |
| 29 | Inviscid analysis §67 | rel_chapter_7_sec67.tex |
| 30 | Periods of oscillation §68 | rel_chapter_7_sec68.tex |
| 31 | Viscous perturbation equations §69-70 | rel_chapter_7_sec69-70.tex |
| 32 | Narrow gap solutions §71 | rel_chapter_7_sec71.tex |
| 33 | Exchange of stabilities + wide gap §72-73 | rel_chapter_7_sec72-73.tex |

#### Ch VIII: General Flows
| 34 | Curved channel §75-76 | rel_chapter_8_sec75-76.tex |
| 35 | Transverse pressure gradient §77-78 | rel_chapter_8_sec77-78.tex |
| 36 | Axial pressure gradient (inviscid) §79 | rel_chapter_8_sec79.tex |
| 37 | Axial pressure gradient (viscous) §80 | rel_chapter_8_sec80.tex |

#### Ch IX: Couette in Hydromagnetics
| 38 | Non-dissipative + axial B §81-83 | rel_chapter_9_sec81-83.tex |
| 39 | Non-dissipative + axial current + combined §84-86 | rel_chapter_9_sec84-86.tex |
| 40 | Dissipative + solutions §87-89 | rel_chapter_9_sec87-89.tex |
| 41 | General case + curved channel §90-91 | rel_chapter_9_sec90-91.tex |

#### Ch X: Rayleigh-Taylor Instability
| 42 | Perturbation eqs + inviscid §90-92 | rel_chapter_10_sec90-92.tex |
| 43 | Variational principle §93 | rel_chapter_10_sec93.tex |
| 44 | Viscous two-fluid §94 | rel_chapter_10_sec94.tex |
| 45 | Rotation effect §95 | rel_chapter_10_sec95.tex |
| 46 | Magnetic field effects §96-97 | rel_chapter_10_sec96-97.tex |
| 47 | Viscous globe + drop oscillations §98-99 | rel_chapter_10_sec98-99.tex |

#### Ch XI: Kelvin-Helmholtz Instability
| 48 | Perturbation eqs + two uniform fluids §100-101 | rel_chapter_11_sec100-101.tex |
| 49 | Continuous variation §102-103 | rel_chapter_11_sec102-103.tex |
| 50 | Shear layer §104 | rel_chapter_11_sec104.tex |
| 51 | Rotation + magnetic field effects §105-106 | rel_chapter_11_sec105-106.tex |

#### Ch XII: Jets and Cylinders
| 52 | Gravitational instability of cylinder §107-109 | rel_chapter_12_sec107-109.tex |
| 53 | Axial B-field on cylinder §110 | rel_chapter_12_sec110.tex |
| 54 | Capillary instability §111-112 | rel_chapter_12_sec111-112.tex |
| 55 | Pinch stability §113-115 | rel_chapter_12_sec113-115.tex |

#### Ch XIII: Gravitational/Jeans
| 56 | Virial theorem (relativistic) §116-118 | rel_chapter_13_sec116-118.tex |
| 57 | Jeans criterion (relativistic) §119 | rel_chapter_13_sec119.tex |
| 58 | Rotation + B on Jeans §120 | rel_chapter_13_sec120.tex |

#### Ch XIV: General Variational
| 59 | Variational principle (relativistic) §121-122 | rel_chapter_14_sec121-122.tex |
| 60 | Compressibility extension §123 | rel_chapter_14_sec123.tex |

## Documentation Convention
Each agent creates:
- `progress/relativistic/subagent_{N}_{task}_{tasknumber}_{description}.md` — per-stage progress
- Updates shared files as needed

## Shared Files
- `RELATIVISTIC_MASTER_PLAN.md` — this file (read-only for agents)
- `RELATIVISTIC_STATUS.md` — overall completion tracking
- `RELATIVISTIC_CONVENTIONS.md` — notation and convention decisions
- `RELATIVISTIC_CAUSALITY_CHECKS.md` — causality verification log
