# Agent 18: BDNK Conversion - Q-law + Overstability (Ch IV, sec 45-46)

## File: `output/chapters/relativistic/rel_chapter_4_sec45-46.tex`

## Changes Made
- IS relaxation equations (tau_q, tau_pi, tau_Pi) completely removed
- BDNK first-order constitutive relations substituted: Pi^{mu nu} = -2 eta sigma^{mu nu}, Q^mu algebraic
- Characteristic equation simplified: IS 7th-order -> BDNK 4th-order (same as classical)
- IS correction factors T_q, T_pi, T_Pi removed entirely
- Frequency-dependent effective Prandtl ratios p_1^IS(sigma), p_2^IS(sigma) replaced by constant BDNK Prandtl ratios p_1/h, p_2/h
- IS "Eckart limit" subsection replaced by "Relation to classical characteristic equation" (no limit needed in BDNK)
- IS relaxation effect subsection replaced by BDNK causality constraints subsection
- IS group velocity bounds replaced by BDNK strong hyperbolicity guarantee
- Non-relativistic limit: simplified (no tau -> 0 limits needed)
- Citations: Bemfica et al. 2018, Kovtun 2019, Hoult & Kovtun 2020, BDNK 2023

## Marginal state (sigma=0): Identical results
- pi^2 Q law preserved identically
