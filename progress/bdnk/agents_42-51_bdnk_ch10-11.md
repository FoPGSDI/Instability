# BDNK Conversion: Agents 42-51 (Chapters X-XI)

## Files Modified

### Chapter X: Rayleigh-Taylor Instability
1. `rel_chapter_10_sec90-92.tex` (Agent 42) - Inviscid RT perturbations
   - Replaced IS formalism references with BDNK in causality discussion
   - Added BDNK citations (Bemfica2018, Kovtun2019)
   - Updated summary item on causal dissipation

2. `rel_chapter_10_sec93.tex` (Agent 43) - Variational principle
   - Replaced IS effective viscosity mu/(1+tau_pi*n) with BDNK eta
   - Updated viscous dissipation functional description
   - Removed tau_pi dependence from eigenvalue problem
   - Updated overstability argument to use BDNK eta > 0
   - Updated NR limit section (removed tau_pi -> 0)
   - Updated summary items on causal dissipation

3. `rel_chapter_10_sec94.tex` (Agent 44) - Viscous RT (MAJOR REWRITE)
   - Replaced IS relaxation equations with BDNK first-order constitutive relations
   - Removed effective viscosity eta/(1+tau_pi*n) throughout
   - Simplified dispersion: q^2 = k^2 + n/nu (no tau_pi*n^2/nu term)
   - Simplified n-from-y relation: n = k^2*nu*(y^2-1) (no quadratic in n)
   - Rewrote causality section: BDNK frame-coefficient bounds replace IS tau_pi bounds
   - Updated asymptotic limits (no IS damping at short wavelengths)
   - Added comparison paragraphs noting IS/BDNK equivalence at marginal state

4. `rel_chapter_10_sec95.tex` (Agent 45) - Rotation effects
   - No IS content present; file already compatible with BDNK

5. `rel_chapter_10_sec96-97.tex` (Agent 46) - Magnetic field effects
   - No IS content present; file already compatible with BDNK

6. `rel_chapter_10_sec98-99.tex` (Agent 47) - Globe/drop oscillations (MAJOR REWRITE)
   - Replaced IS relaxation equation with BDNK first-order constitutive relation
   - Removed effective viscosity nu_eff = nu/(1-tau_pi*sigma)
   - Simplified q = sqrt(sigma/nu) (no IS factor)
   - Simplified characteristic equation argument z = R*sqrt(sigma/nu)
   - Updated decay rates: removed tau_pi corrections
   - Updated aperiodic modes: BDNK causality via hyperbolicity, not IS saturation
   - Updated bibliographical notes to cite BDNK

### Chapter XI: Kelvin-Helmholtz Instability
7. `rel_chapter_11_sec100-101.tex` (Agent 48) - KH basic
   - No IS content; file already compatible with BDNK

8. `rel_chapter_11_sec102-103.tex` (Agent 49) - Continuous variation
   - Single IS reference replaced with BDNK citation

9. `rel_chapter_11_sec104.tex` (Agent 50) - Shear layer
   - No IS content; file already compatible with BDNK

10. `rel_chapter_11_sec105-106.tex` (Agent 51) - Rotation+B on KH
    - No IS content; file already compatible with BDNK

## Key Conversion Rules Applied
- tau_pi, tau_q, tau_Pi relaxation times removed
- IS effective viscosity eta/(1+tau_pi*n) -> BDNK eta (first-order)
- Dispersion relations simplified (no extra IS relaxation modes)
- Marginal state (n=0) results identical between IS and BDNK
- Causality: IS tau_pi bounds -> BDNK frame-coefficient bounds
- Citations added: Bemfica et al. 2018, Kovtun 2019
