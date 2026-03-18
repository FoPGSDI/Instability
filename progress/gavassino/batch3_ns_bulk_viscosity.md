# Gavassino Integration Batch 3: NS Bulk Viscosity and Superfluid Papers

## Papers Integrated

| # | arXiv ID | Title | Chapters Modified |
|---|----------|-------|-------------------|
| 17 | 2003.04609 | Bulk viscosity: thermodynamics to hydro | Ch VII (sec72-73), Ch VIII (sec80), Ch IX (sec87-89) |
| 18 | 2304.05455 | Burgers-type bulk viscosity in NS | Ch XII (sec110), Ch XIII (sec119) |
| 19 | 2305.04119 | Bulk rheology: NS mergers to cosmology | Ch IX (sec87-89), Ch XIII (sec119) |
| 20 | 2501.12543 | Extending IS: causal bulk viscosity | Ch VIII (sec80), Ch IX (sec87-89) |
| 21 | 2204.11809 | Simulating bulk viscosity in NS I | Ch VII (sec72-73), Ch XII (sec110) |
| 22 | 2204.11810 | Simulating bulk viscosity in NS II | Ch VII (sec72-73), Ch XII (sec110) |
| 23 | 2012.10288 | Superfluid dynamics in NS crusts | Ch VI (sec60) |
| 24 | 2001.08951 | Mutual friction coupling in NS | Ch III (sec19-23) |

## Key Physics Integrated

### Bulk Viscosity Framework (Paper 17: 2003.04609)
- Any bulk viscosity source maps to effective chemical reactions
- Telegraph-type relaxation: tau_M * A_dot + A = k * div(u)
- Frequency-dependent zeta_eff = zeta/(1 + omega^2 * tau_M^2)
- Israel-Stewart is the 2nd-order expansion of a more general non-perturbative theory
- Bridge formula: tau_M = chi * zeta connects IS to microphysics

### Burgers Model (Paper 18: 2304.05455)
- Three-component mixture (n, p, e, mu) with two reactions => Burgers rheology
- Bulk stress obeys 2nd-order ODE, not Maxwell-Cattaneo relaxation
- Viscous stress can overshoot Navier-Stokes value
- NS matter with muons is genuinely Burgers-type

### Pseudoplastic Rheology (Paper 19: 2305.04119)
- First causal/stable theory of relativistic pseudoplastic fluid
- NS mergers behave as pseudoplastic material (zeta_eff decreases with expansion rate)
- Applicable from NS mergers to viscous cosmology

### Extended IS Theory (Paper 20: 2501.12543)
- Standard IS becomes acausal when Pi ~ -P
- New class: symmetric-hyperbolic, causal for ALL flows
- Total pressure P+Pi stays in (0, epsilon) automatically
- Second law exact, not just perturbative

### NS Simulation Papers (Papers 21-22: 2204.11809/10)
- Multi-component fluid vs Hiscock-Lindblom vs Maxwell-Cattaneo
- Good agreement for small perturbations, single particle fraction
- Neutrino energy loss > bulk stress effect on dynamics
- Multiple particle fractions require beyond-IS models

### Superfluid Crust Dynamics (Paper 23: 2012.10288)
- Relativistic HVBK hydrodynamics for NS inner crust
- Chemical gauge covariance requires Iordanskii force
- Entrainment parameter |epsilon_n| ~ 10 in inner crust
- Resolves Sonin-Stone vs Thouless-Wexler controversy (different regimes)

### Mutual Friction Coupling (Paper 24: 2001.08951)
- Universal formula: tau_rise^GR/tau_rise^Newton = f(compactness only)
- ~25% correction for canonical NS, ~40% for compact stars
- Universal because reservoir in thin shell near surface
- Directly impacts convective onset conditions in rotating NS

## Files Modified
- SHARED_REFERENCES.bib: 8 new BibTeX entries added
- RESEARCH_NOTE_LG.md: Status updated from HYPOTHESIS to VALIDATED
- rel_chapter_3_sec19-23.tex: New section on superfluid coupling and convective onset
- rel_chapter_6_sec60.tex: New subsection on superfluid dynamics and entrainment
- rel_chapter_7_sec72-73.tex: New section on bulk viscosity in NS Couette flow
- rel_chapter_8_sec80.tex: New section on extended IS theory at large gradients
- rel_chapter_9_sec87-89.tex: New section on bulk viscosity in magnetised NS matter
- rel_chapter_12_sec110.tex: New subsection on Burgers-type viscosity in jets
- rel_chapter_13_sec119.tex: New subsection on bulk rheology and Burgers model
- progress/gavassino/batch3_ns_bulk_viscosity.md: This file

## Status: COMPLETE
