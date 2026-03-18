# Agent 22: BDNK Conversion - Overstability + Experiments (Ch V, sec 53-54)

## File: `output/chapters/relativistic/rel_chapter_5_sec53-54.tex`

## Changes Made
- IS relaxation equations (tau_q, tau_pi, tau_Pi) completely removed and replaced by BDNK algebraic constitutive relations
- Frequency-dependent effective transport coefficients (kappa_eff(omega), eta_eff(omega), zeta_eff(omega)) replaced by frequency-independent BDNK values
- IS frequency shift formula removed; BDNK frequency shift is O(v^2/c^2) only
- Effective Prandtl ratios: IS frequency-dependent -> BDNK constant (p_1/h, p_2/h)
- Mercury tau_q estimate removed; replaced by BDNK frame correction estimate
- IS correction formula simplified (removed omega^2 tau_q^2 term)
- Astrophysical applications: IS relaxation references -> BDNK frame corrections
- Bibliographical notes completely rewritten: IS references replaced by BDNK (Bemfica et al. 2018, Kovtun 2019, BDN 2019, Hoult & Kovtun 2020, BDNK 2023)

## Non-dissipative physics: UNCHANGED
- Background energy-momentum tensor, magnetar/accretion disk/neutron star applications structure preserved

## Marginal state (sigma=0): Identical results
