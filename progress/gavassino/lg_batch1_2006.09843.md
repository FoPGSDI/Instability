# LG Batch 1: Paper 7 -- Gavassino, Antonelli & Haskell 2006.09843
## "When the entropy has no maximum" (PRD 102, 043018, 2020)

### Status: INTEGRATED

### Key Result
The instability of Eckart and Landau-Lifshitz first-order theories has a transparent thermodynamic origin: the total entropy S, restricted to dynamically accessible states, **has no upper bound**. The first-order truncation of the entropy current converts the entropy maximum into a saddle point. The runaway modes found by Hiscock & Lindblom are the directions in state space along which entropy grows without bound.

For Israel-Stewart: stability conditions are exactly the requirements for S to have an absolute maximum.

For BDNK: stability is achieved by allowing small transient violations of nabla_mu s^mu >= 0, while maintaining a bounded Lyapunov functional.

### Integration Points
- **rel_chapter_2_sec13-14.tex**: relcorrection box "Why Eckart/Landau-Lifshitz theories are unstable" explaining saddle-point mechanism
- **rel_framework_hydro.tex**: Listed in "Complementary results" of Gavassino theorem section
- **SHARED_REFERENCES.bib**: Entry `GavassinoLyapunov2020`

### Physical Insight
The Hiscock-Lindblom instability is not a mathematical pathology but a thermodynamic one: the entropy functional is unbounded above, so the second law drives the system away from "equilibrium" (which is actually a saddle point).
