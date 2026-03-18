---
agent: 1
chapter: 0
stage: 3
status: completed
timestamp: 2026-03-17
---
## Summary
Reviewed and refined math typesetting in the front matter:
- Very little inline math in the Preface and Acknowledgements (none, actually).
- The TOC comments contain numerous math expressions in section titles, all properly typeset:
  - Greek letters: $\Omega$, $\Pi$, $\epsilon$, $\eta$, $\mu$, $\nu$, $\sigma$, $\rho$, $\alpha$, $\beta$, $\gamma$
  - Script letters: $\mathscr{T}$, $\mathscr{L}$, $\mathscr{S}$
  - Subscripts/superscripts: $\rho_1$, $\rho_2$, $\Omega_1/\Omega_2$, $r^2$, $N^2$, etc.
  - Operators: $\to$, $\neq$, $>$, $<$
  - Text within math: $\text{constant}$
  - Fractions: $\frac{1}{2}$
- Applied accent corrections: B\'enard, Alfv\'en
- Standardized en-dashes for compound names: Taylor--Proudman, Schmidt--Milverton, Rayleigh--Taylor, Kelvin--Helmholtz
- Corrected section 37 -> 39 for "The Alfv\'en waves" based on re-reading the PDF

## Issues / Notes
- Section numbering in Ch. IV appears to skip from 36 to 39 (sections 37-38 absent from the TOC). This may be a feature of the original book's numbering.
- All math in the TOC is in comments only (for reference); LaTeX will auto-generate the actual TOC.

## Next
Stage 4: Bibliography and cross-references handling.
