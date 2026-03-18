---
agent: 55
chapter: 12
sections: 113-115
task: Relativistic pinch stability (Ch XII §113-115)
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created `output/chapters/relativistic/rel_chapter_12_sec113-115.tex`
containing the relativistic extension of Chandrasekhar's Ch XII
§§113--115 (hydromagnetic stability of cylindrical systems, helical
fields, and the pinch).

### §113 — Stability of the simplest MHD solution (relativistic)
- Covariant ideal MHD formulation with energy-momentum tensor
- Relativistic equipartition condition: classical Alfven relation
  generalised with enthalpy w = (epsilon+p)/c^2
- Stability theorem proved via energy integral with positive-definite
  norm (w c^2 + b^2)
- Detailed example: kink/sausage modes in cylindrical column with
  Lorentz-factor corrections to Alfven frequency

### §114 — Fluid motions on helical B-field stability (relativistic)
- General dispersion relation with relativistic corrections:
  x_{m,j}^2 -> x_{m,j}^2/(1 - V^2/c^2)
- Case f=0 (pure velocity field): neutrally stable, shifted frequencies
- Case f=1 (pure magnetic field): instability criteria unchanged
- General case: enhanced stability threshold f_crit > 1/2 due to
  relativistic inertia; reduced growth rates for unstable modes

### §115 — Stability of the pinch (relativistic)
- Relativistic pressure balance including ram pressure for streaming plasma
- Relativistic dispersion relation with modified Alfven frequencies
- Kruskal-Shafranov criterion in relativistic regime: weaker internal
  field needed for stabilisation when Lorentz factor is large
- Application to astrophysical jets: bulk Lorentz factor provides
  inherent stabilisation against kink instability
- Numerical table of critical beta_1 values for Gamma=2

### Causality verification
- All Alfven, fast/slow magnetosonic speeds bounded by c
- Phase and group velocities of all pinch modes subluminal
- Composition law v_f^2 = c_s^2 + v_A^2 - c_s^2 v_A^2/c^2 < c^2

### Bibliographical notes
- Classical references (Chandrasekhar, Trehan, Kruskal, Shafranov, Tayler)
- Relativistic MHD references (Lichnerowicz, Anton et al.)
- Jet stability references (Istomin & Pariev, Begelman, Bromberg &
  Tchekhovskoy)
- Causality references (Komissarov, Bodo et al.)

## Issues / Notes
- The relativistic corrections to the dispersion relations maintain
  the same Bessel-function structure as the classical equations; only
  the Alfven frequencies and inertial terms are modified.
- For the pure magnetic field case (f=1, §114), relativistic
  corrections cancel since there is no kinetic energy, and the
  classical instability criteria apply verbatim.

## Next
No further action required. File ready for integration into the
relativistic edition.
