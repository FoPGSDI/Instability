---
agent: 41
chapter: 9
sections: 90-91
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Created relativistic extension of Ch IX §88-89 (curved channel MHD stability
and experiments) as new §90-91 in
`output/chapters/relativistic/rel_chapter_9_sec90-91.tex`.

### Section 90: Relativistic curved channel MHD stability
- Formulated the curved-channel Poiseuille flow with axial B in covariant
  MHD using the energy-momentum tensor with Israel-Stewart causal dissipation.
- Derived relativistic versions of the marginal stability equations (9-306)
  and (9-307) with:
  - Israel-Stewart relaxation replacement sigma -> sigma/(1 + tau_pi sigma)
  - Relativistic Chandrasekhar number Q_rel = Q / (1 + v_A^2/c^2)
  - Relativistic Dean number Lambda_rel = Lambda * gamma^2
- Showed asymptotic behaviour for large Q_rel reproduces classical result.
- Demonstrated non-hydrodynamic (Israel-Stewart) modes are always damped,
  so critical Lambda_rel agrees with classical up to O(v_A^2/c^2).
- Verified non-relativistic limit c -> infty recovers equations (9-306)-(9-307).

### Section 91: Experiments — classical and astrophysical
- Summarised Donnelly-Ozima laboratory experiments (classical regime).
- Connected the Velikhov-Chandrasekhar instability to the magnetorotational
  instability (MRI) in relativistic accretion discs.
- Presented the relativistic MRI dispersion relation with:
  - Bounded Alfven speed v_A < c
  - Israel-Stewart corrections to growth rate
  - Frame-dragging effects on epicyclic frequency
  - Light cylinder constraint
- Discussed GRMHD simulation results confirming relativistic MRI.
- Bibliographical notes with 16 references covering covariant MHD,
  Israel-Stewart theory, MRI discovery, relativistic MRI analysis,
  GRMHD simulations, and laboratory MRI experiments.

## Issues / Notes
- Classical §88-89 end at §89; new relativistic sections numbered §90-91.
- The MRI dispersion relation (eq:rel-9-MRI-disp) is given in local WKB form
  appropriate for thin-disc geometry.
- Laboratory experiments remain entirely non-relativistic; the relativistic
  regime is accessed only through astrophysical accretion discs and numerical
  simulations.

## Next
- Integration with rel_main.tex when all Chapter IX relativistic sections
  are complete.
