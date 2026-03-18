# Critical Proofread Batch B: Chapters IV--VII

## Files reviewed

### Chapter IV (Relativistic Hydromagnetic Stability)
- `rel_chapter_4_sec36-40.tex` -- Covariant MHD, Alfven waves, causality
- `rel_chapter_4_sec41-44.tex` -- Thermal instability with magnetic field
- `rel_chapter_4_sec45-46.tex` -- pi^2 Q law and overstability
- `rel_chapter_4_sec47-48.tex` -- H-g directions and experiments

### Chapter V (Combined Rotation and Magnetic Field)
- `rel_chapter_5_sec49-50.tex` -- Like/contrary effects, wave propagation
- `rel_chapter_5_sec51-52.tex` -- Perturbation equations, stationary convection
- `rel_chapter_5_sec53-54.tex` -- Overstability, experiments/astrophysical apps

### Chapter VI (Spherical Geometry)
- `rel_chapter_6_sec55-56.tex` -- Spherical perturbation equations
- `rel_chapter_6_sec57-58.tex` -- Exchange of stabilities, variational principle
- `rel_chapter_6_sec59.tex` -- Onset in self-gravitating sphere
- `rel_chapter_6_sec60.tex` -- Spherical shells
- `rel_chapter_6_sec61-63.tex` -- Rotation in spheres

### Chapter VII (Couette Flow)
- `rel_chapter_7_sec64-66.tex` -- Rayleigh criterion, relativistic version
- `rel_chapter_7_sec67.tex` -- Inviscid stability, Howard semicircle
- `rel_chapter_7_sec68.tex` -- Oscillation periods of rotating column
- `rel_chapter_7_sec69-70.tex` -- Viscous Couette flow, perturbation equations
- `rel_chapter_7_sec71.tex` -- Narrow gap solutions
- `rel_chapter_7_sec72-73.tex` -- Exchange of stabilities, wide gap

## Issues found and fixed

### 1. Duplicate bibitem key (rel_chapter_6_sec59.tex)
- **Issue:** Two `\bibitem{Radice2018}` entries at lines 627 and 633 referenced different papers (Radice et al. 2016 and Radice et al. 2018).
- **Fix:** Renamed the first entry to `\bibitem{Radice2016}` and updated the corresponding `\cite{Radice2016}` at line 575.

### 2. Undefined cross-reference (rel_chapter_6_sec60.tex)
- **Issue:** `\ref{sec:rel-60-Ra}` referenced at lines 825 and 836 but no corresponding `\label{sec:rel-60-Ra}` exists in the file.
- **Fix:** Changed both references to `\ref{sec:rel-60-thick}`, which is the closest appropriate section covering critical Rayleigh numbers for shells.

## Checklist verification (all 18 files)

### 1. LaTeX syntax
- No unmatched braces, environments, or missing `\end{}` commands found.
- All `\begin{equation}` / `\end{equation}`, `\begin{align}` / `\end{align}`, `\begin{figure}` / `\end{figure}`, and `\begin{table}` / `\end{table}` pairs are balanced.
- `\boxed{}` environments properly closed throughout.

### 2. Math correctness
- Relativistic Alfven speed formula `v_A^2 = b^2 c^2 / (w + b^2)` consistent across files.
- Fast magnetosonic speed `v_f^2 = c_s^2 + v_A^2 - c_s^2 v_A^2 / c^2 < c^2` correctly stated.
- Enthalpy density definition `w = (epsilon + p)/c^2` consistent.
- TOV equation correctly written with all three correction factors.
- Epicyclic frequency `kappa_r^2 = Omega_K^2 (1 - 6 r_g/r)` correctly stated for Schwarzschild.

### 3. Gavassino citations
- All Gavassino citations use proper keys: `GavassinoCarter2022`, `GavassinoCausality2021`, `GavassinoBulkViscosity2020`, `GavassinoCouette2025`, `GavassinoRadDispersion2025`, `GavassinoAntonelliHaskellSuperfluid2021`, `GavassinoAntonelliPizzocheroHaskell2020`.
- The Gavassino theorem on Carter multifluid stability (sec60) is correctly stated with entrainment matrix positivity condition.
- Gavassino--Niekamp--Schlichting--Denicol exact Couette solution (sec64-66) correctly presented.

### 4. BDNK terminology
- Consistently written as "BDNK (Bemfica--Disconzi--Noronha--Kovtun)" throughout.
- First-order constitutive relations correctly stated: `Pi^{mu nu} = -2 eta sigma^{mu nu}`.
- Frame coefficients correctly described as ensuring strong hyperbolicity.
- No Israel--Stewart relaxation times incorrectly attributed to BDNK.
- Citations: `BemficaDN2018`, `Kovtun2019`, `BemficaDN2019`, `HoultKovtun2020`, `BemficaDNK2023` consistently used.

### 5. Notation consistency
- Metric signature `(-,+,+,+)` stated consistently.
- Four-velocity normalization `u^mu u_mu = -c^2` consistent.
- Projection tensor `Delta^{mu nu} = g^{mu nu} + u^mu u^nu / c^2` consistent.
- Custom macros (`\enthalpy`, `\edensity`, `\rdensity`, `\shearvisc`, `\bulkvisc`, `\thermcond`, `\vA`, `\cs`, `\Lf`, `\Qrel`, `\Rarel`, `\Tarel`, `\bsq`, `\relcorr`, `\NRlimit`) used consistently.

### 6. Cross-references
- All `\eqref` and `\ref` commands use proper label syntax.
- References to classical chapter equations (`eq:4-xxx`, `eq:6-xxx`, `eq:7-xxx`) are consistent cross-chapter references to the non-relativistic text.
- Internal relativistic labels (`eq:rel-...`, `sec:rel-...`) properly defined and used.
- Fixed two undefined `\ref{sec:rel-60-Ra}` references.

### 7. Grammar and style
- Prose is clear and professional throughout.
- Consistent use of British/American conventions within each file.
- Proper use of `\emph{}` for emphasis, `\textbf{}` for key results.
- Bibliographic notes sections follow Chandrasekhar's style.

### 8. Physics correctness
- Relativistic inertia replacement `rho -> (epsilon + p)/c^2` correctly applied throughout.
- Causality checks (`v_A < c`, `v_f < c`, `v_s < c`) correctly proven.
- Non-relativistic limits explicitly verified in every section.
- Exchange of stabilities proofs correctly adapted with enthalpy-inertia factor.
- Rayleigh criterion correctly generalized with Lorentz factor: `d(Gamma^2 r^2 Omega)/dr >= 0`.
- Taylor number relativistic enhancement `T_rel = T_cl * [(epsilon+p)/(rho c^2)]^2` correct.

### 9. Gavassino theorem coverage
- Carter multifluid stability theorem (sec60): correctly stated with entrainment matrix positivity.
- Bulk viscosity formalism (sec72-73): Gavassino--Antonelli--Haskell mapping to effective chemical reactions.
- Exact Couette solution (sec64-66): Gavassino--Niekamp--Schlichting--Denicol inertia-of-heat effect.
- Wagner--Gavassino regime of applicability (sec64-66): IS truncation ranking correctly referenced.

### 10. Universality
- The pi^2 Q law correctly shown to persist relativistically (sec41-44, sec45-46).
- Exchange of stabilities proven for relativistic spherical shells (sec57-58) and Couette flow (sec72-73).
- Variational principles carry over with enthalpy-inertia factor cancellation.
- Asymptotic scalings (T_c ~ tau (1-mu)^4, Ra ~ Ta^{2/3}) preserved with multiplicative relativistic factors.

## Notes

- Convention file naming inconsistency: Ch IV-V and Ch VII files reference `RELATIVISTIC_CONVENTIONS.md`; Ch VI files reference `BDNK_CONVENTIONS.md`. Both are in comments only and do not affect compilation.
- The `\textsc{}` usage for author names in bibliographic notes (sec47-48) is a stylistic choice consistent within that file.
- Multiple files contain `\thebibliography` environments (sec55-56, sec57-58, sec59, sec60) which is valid for standalone compilation but may need consolidation for the final book build.
