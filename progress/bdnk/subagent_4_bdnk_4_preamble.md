# Subagent 4: BDNK Preamble and Macros

## Status: COMPLETE

## Changes Made

### `output/chapters/relativistic/rel_preamble.tex`
- Removed IS-specific relaxation time macros: `\taupi`, `\tauq`, `\tauPi`
- Renamed `\bulkP` to `\Pibulk` for BDNK bulk viscous pressure
- Added BDNK frame coefficient macros:
  - `\epsone` (varepsilon_1 frame energy correction)
  - `\betaone` (beta_1 temperature gradient coefficient)
  - `\alphaone` (alpha_1 chemical potential coefficient)
  - `\Efr` (frame energy density E)
  - `\Pfr` (frame pressure P)
  - `\sheartensor` (shear tensor sigma^{mu nu})
  - `\expansion` (expansion scalar theta)
- Updated dissipation section header and comments from IS to BDNK
- Updated `causalitycheck` environment title and description to reference BDNK conditions
- Added `bdnkframe` environment (green tcolorbox) for BDNK frame specification

### `output/chapters/relativistic/rel_main.tex`
- Updated title to reference BDNK formalism
- Added subtitle: "Using BDNK first-order causal viscous hydrodynamics"
- Updated author line to indicate BDNK Formalism

## Conventions Followed
- All macros follow `BDNK_CONVENTIONS.md`
- Non-dissipative macros (4-vectors, tensors, physical quantities, dimensionless numbers, operators) left unchanged
- Heat flux macro updated to use Q^mu (BDNK convention) instead of q^mu (IS convention)
