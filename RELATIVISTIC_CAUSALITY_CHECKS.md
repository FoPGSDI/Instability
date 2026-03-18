# Causality Verification Log

Each agent MUST verify and log causality bounds for every modified dispersion relation.

## Format
| Agent | Chapter | Mode | Phase velocity | Group velocity | Causal? | Notes |
|-------|---------|------|---------------|----------------|---------|-------|
| (to be filled by agents) | | | | | | |

## Required Checks per Agent
1. Identify all wave/perturbation modes in the relativistic calculation
2. Compute phase velocity v_ph = ω/k for each mode
3. Compute group velocity v_g = ∂ω/∂k for each mode
4. Verify v_g ≤ c (this is the physical causality bound)
5. If v_ph > c, note this is acceptable as long as v_g ≤ c and no information travels superluminally
6. For dissipative modes: verify the Israel-Stewart relaxation times τ > 0
7. For growing modes (instabilities): verify the growth rate σ is real and the spatial structure is causal

## Common Pitfalls
- Navier-Stokes → leads to infinite signal speed (parabolic); MUST use Israel-Stewart (hyperbolic)
- Fourier heat conduction → acausal; MUST use Cattaneo/Israel-Stewart relaxation
- Newtonian gravity → instantaneous; use retarded potentials or GR for consistency
- Alfvén speed can approach c for strong fields; always use relativistic formula
