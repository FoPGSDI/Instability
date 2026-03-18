# LG Batch 1: Paper 8 -- Gavassino 2105.09294
## "Proving the Lorentz invariance of the entropy and the covariance of thermodynamics" (Found. Phys. 52, 11, 2022)

### Status: INTEGRATED

### Key Result
Rigorous proof that the thermodynamic entropy S is a Lorentz scalar, from two assumptions only:
1. There exists one inertial frame where the second law holds (dot{S} >= 0)
2. Microscopic dynamics is governed by a Lorentz-invariant field-theory Lagrangian

The proof shows adiabatic accelerations preserve rest mass to leading order (delta p^nu ~ epsilon, but delta S ~ epsilon^2 >= 0 for both signs of epsilon, forcing delta S = 0). By van Kampen's argument, S = S(M) depends only on the Lorentz-invariant rest mass.

Key insight: Thermodynamics need not be postulated to be Lorentz covariant -- covariance follows from the scalar nature of S.

### Integration Points
- **rel_framework_thermo.tex**: New subsection "Lorentz Invariance of Thermodynamic Entropy" before causality constraints
- **rel_framework_hydro.tex**: Listed in "Complementary results" of Gavassino theorem section
- **SHARED_REFERENCES.bib**: Entries `GavassinoLorentz2021` and `vanKampen1968`

### Physical Insight
The covariant entropy current s^mu = s n u^mu + ... used throughout the book transforms correctly under Lorentz boosts, and nabla_mu s^mu >= 0 is frame-independent. This is proven, not assumed.
