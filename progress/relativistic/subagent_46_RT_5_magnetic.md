---
agent: 46
chapter: 10
sections: 96-97
task: Relativistic RT instability with magnetic field effects
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_10_sec96-97.tex` extending
Chandrasekhar's Chapter X, sections 96-97 (magnetic field effects on
Rayleigh-Taylor instability) to the relativistic regime.

### Section 96: Vertical magnetic field (relativistic)
- Linearised relativistic perturbation equations with enthalpy replacing density
- Integral relation proving n^2 real (using causality v_A < c)
- Unstable case: cubic dispersion relation with (1 - v_A^2/c^2)^{1/2} corrections
- Asymptotic limits: long-wave unaffected, short-wave growth rate suppressed
- Stable case: oscillatory Alfven waves with relativistic wavenumber m_{j,rel}
- No dispersion relation in stable case (same qualitative structure as classical)

### Section 97: Horizontal magnetic field (relativistic)
- Anisotropic stabilisation with cos^2(theta) factor preserved
- Relativistic dispersion relation with enhanced equivalent surface tension
- Interchange instability: k_x = 0 modes unaffected by field (only enthalpy Atwood number)
- Critical wavenumber for stability modified by (1 - v_A^2/c^2) factor

### Causality
- v_A^2 = b^2 c^2 / (w + b^2) < c^2 automatically for positive enthalpy
- All spatial exponents, wave speeds, and surface tensions finite and well-defined
- Ultra-relativistic limit: growth rates suppressed, not enhanced

## Conventions
- Metric: (-,+,+,+), c explicit, u^mu u_mu = -c^2
- Enthalpy w = epsilon + p replaces rho throughout
- Relativistic Alfven speed from RELATIVISTIC_CONVENTIONS.md
- Classical limits recovered transparently by c -> infinity

## Files created
- `output/chapters/relativistic/rel_chapter_10_sec96-97.tex`
- `progress/relativistic/subagent_46_RT_5_magnetic.md`
