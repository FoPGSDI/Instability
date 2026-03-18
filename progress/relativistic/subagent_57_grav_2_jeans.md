---
agent: 57
chapter: 13 (relativistic)
task: Relativistic Jeans gravitational instability criterion (§119)
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_13_sec119.tex`, a relativistic
generalization of Chapter XIII §119 (Jeans gravitational instability criterion)
from Chandrasekhar's *Hydrodynamic and Hydromagnetic Stability*.

### Key content

1. **Classical Jeans recapitulation** (§119a):
   - Standard dispersion relation ω² = c_s² k² − 4πGρ
   - Jeans wavenumber k_J² = 4πGρ/c_s², Jeans length λ_J = c_s √(π/(Gρ))

2. **Relativistic perturbation equations** (§119c):
   - Relativistic Poisson equation with source (ε + 3p)/(2c²)
   - Relativistic Euler equation with enthalpy density w = (ε+p)/c² as inertia
   - Energy conservation with (ε+p) replacing ρ

3. **Relativistic dispersion relation** (§119d):
   - ω² = c_s² k² − 4πG(ε+p)/c² × (1 + 3c_s²/c²)/2
   - Correct Newtonian limit recovered for p ≪ ε, c_s ≪ c

4. **Relativistic Jeans wavenumber, length, and mass** (§119e):
   - k_{J,rel}² > k_{J,classical}²: instability at shorter wavelengths
   - M_{J,rel} < M_{J,classical}: pressure DESTABILISES in GR
   - The Chandrasekhar insight: pressure aids collapse

5. **Pressure-destabilisation mechanism** (§119f):
   - Energy argument: pressure appears in both inertial and gravitational source terms
   - Connection to Chandrasekhar mass limit and TOV limit

6. **Causality constraints** (§119g):
   - c_s ≤ c (causality bound on sound speed)
   - Gravitational response propagates at c, not instantaneously
   - Maximum Jeans wavenumber at c_s = c sets minimum stable mass

7. **Limiting cases** (§119h):
   - Non-relativistic limit recovers classical Jeans
   - Radiation-dominated fluid (p = ε/3)
   - Maximally stiff causal equation of state (c_s = c)

### Conventions
- Metric signature (−,+,+,+), c kept explicit
- w = (ε+p)/c² for enthalpy density
- c_s² = (∂p/∂ε)_s as relativistic sound speed
- All notation consistent with RELATIVISTIC_CONVENTIONS.md
