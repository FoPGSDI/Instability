# LG Batch 1: Paper 1 -- Gavassino 2105.14621
## "Can We Make Sense of Dissipation without Causality?" (Phys. Rev. X 12, 041001, 2022)

### Status: INTEGRATED

### Key Result
**Theorem:** If a relativistic hydrodynamic theory has:
1. An entropy current s^mu with nabla_mu s^mu >= 0
2. Entropy maximized at equilibrium (Gibbs stability: information current E^mu future-directed timelike)

Then the linearised theory is **symmetric-hyperbolic and causal**.

The proof constructs explicit solutions showing M^j_AB = E^j_AB and Xi_(AB) = sigma_AB, converting the evolution equations into symmetric-hyperbolic form E^mu_AB d_mu phi^B = -sigma_AB phi^B - Xi_[AB] phi^B.

### Integration Points
- **rel_framework_hydro.tex**: Added as highlighted theorem box (Section "The Gavassino Theorem: Thermodynamic Stability Implies Causality") with full statement, proof sketch, and three consequences for the book
- **rel_chapter_1.tex**: Added to formalism comparison section as item 4
- **SHARED_REFERENCES.bib**: Entry `GavassinoCausality2021`

### Physical Insight
Thermodynamic stability is not just a desirable property -- it is THE mechanism that guarantees causality. This unifies the causality proofs for BDNK and IS under a single principle.
