# LG Batch 1: Paper 6 -- Gavassino 2104.09142
## "Applying the Gibbs stability criterion to relativistic hydrodynamics" (CQG 38, 21LT02, 2021)

### Status: INTEGRATED

### Key Result
Systematic method to construct a Lyapunov functional E = -delta S for any relativistic fluid theory:
1. Given equilibrium state phi_i and perturbation delta phi_i, impose delta U = delta N = 0
2. First-order variation delta S = 0 defines equilibrium (recovers covariant Gibbs relation)
3. Second-order variation gives Lyapunov functional E = -delta^(2)S >= 0
4. Positive definiteness of E implies Lyapunov stability

The method requires only: (a) symmetric T^ab with nabla_a T^ab = 0, (b) entropy current s^a with nabla_a s^a >= 0.

### Integration Points
- **rel_chapter_2_sec13-14.tex**: New subsection "Gavassino's Gibbs stability criterion and the Lyapunov functional" connecting to the variational principle
- **rel_framework_hydro.tex**: Listed in "Complementary results" of Gavassino theorem section
- **SHARED_REFERENCES.bib**: Entry `GavassinoGibbs2021`

### Physical Insight
The Rayleigh quotient from the variational principle is controlled by the Gibbs stability criterion. Positive definiteness of E is the relativistic generalization of Chandrasekhar's energy balance.
