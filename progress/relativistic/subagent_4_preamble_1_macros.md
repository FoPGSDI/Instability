# Agent 4: Relativistic LaTeX Preamble and Master Document

## Status: COMPLETE

## Files produced
- `output/chapters/relativistic/rel_preamble.tex` -- shared macro definitions
- `output/chapters/relativistic/rel_main.tex` -- master document

## Macro groups defined in rel_preamble.tex
1. **4-Vector notation** -- `\fourv`, `\fvel`, `\fveldown`, `\proj`, `\projdown`
2. **Tensors** -- `\emt`, `\farad`, `\dualF`, `\metric`, `\mink`, etc.
3. **Covariant derivatives** -- `\covd`, `\covdu`, `\covda`, `\Lie`
4. **Physical quantities** -- `\enthalpy`, `\edensity`, `\rdensity`, `\Lf`, `\cs`, `\vA`, `\vf`, `\vs`, `\bfour`, `\bsq`
5. **Israel-Stewart dissipation** -- `\bulkP`, `\shearten`, `\heatflux`, `\taupi`, `\tauq`, `\tauPi`, `\bulkvisc`, `\shearvisc`, `\thermcond`
6. **Relativistic dimensionless numbers** -- `\Rarel`, `\Tarel`, `\Qrel`, `\Mach`
7. **Operators** -- `\dAlembert`, `\Dalembertian`, `\order`
8. **Correction helpers** -- `\relcorr`, `\NRlimit`
9. **Environments** -- `causalitycheck`, `relcorrection` (require tcolorbox)

## Dependencies
- Requires `\usepackage{tcolorbox}` in `../../preamble.tex`

## Notes
- All macros are documented with inline comments
- Master document includes framework chapters and has placeholders for all modified chapters
