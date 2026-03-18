# Phase 2A Proofreading Report: Frameworks + Chapters I-III (12 files)

## Files Processed
1. `rel_framework_hydro.tex`
2. `rel_framework_mhd.tex`
3. `rel_framework_thermo.tex`
4. `rel_preamble.tex`
5. `rel_chapter_1.tex`
6. `rel_chapter_2_sec5-9.tex`
7. `rel_chapter_2_sec10-12.tex`
8. `rel_chapter_2_sec13-14.tex`
9. `rel_chapter_2_sec15.tex`
10. `rel_chapter_2_sec16.tex`
11. `rel_chapter_2_sec17-18.tex`
12. `rel_chapter_3_sec19-23.tex`

## Fixes Applied

### LaTeX Syntax

1. **`rel_framework_thermo.tex`**: Replaced `\ding{51}` (requires `pifont` package) with `$\checkmark$` in 8 checklist items (lines 685-702). This avoids an undefined command error.

2. **`rel_framework_thermo.tex`**: Replaced all instances of `\dd` (undefined without `physics` package) with `\mathrm{d}` throughout -- first law, Gibbs-Duhem, Schwarzschild criterion, Ledoux criterion, Brunt-Vaisala frequency, and NR limit (approx. 20 occurrences).

3. **`rel_framework_mhd.tex`**: Replaced `\dd\Sigma^{\mu\nu}`, `\dd\Phi_{\mathcal{S}}`, `\dd\tau` with `\mathrm{d}` equivalents (3 locations).

4. **`rel_chapter_2_sec13-14.tex`**: Removed duplicate `\input{rel_preamble}` (line 14) -- this file is included by `rel_main.tex` which already inputs the preamble.

5. **`rel_chapter_3_sec19-23.tex`**: Fixed incomplete `\begin{cases}` equation (eq:rel-3-25, lines 467-479) -- the second case branch was empty and the `where` clause was dangling. Replaced with a prose description of the BDNK dispersion behavior.

### Duplicate Labels

6. **`rel_framework_mhd.tex`**: Renamed `eq:lin-momentum` to `eq:mhd-lin-momentum` and `eq:lin-energy` to `eq:mhd-lin-energy` (duplicated from `rel_framework_hydro.tex`). Updated the cross-reference on line 675.

7. **`rel_chapter_2_sec10-12.tex`**: Renamed `eq:rel-dispersion` to `eq:rel-dispersion-benard` (duplicated from `rel_framework_hydro.tex`).

8. **`rel_framework_thermo.tex`**: Renamed `eq:shear-tensor` to `eq:thermo-shear-tensor` (duplicated from `rel_framework_hydro.tex`).

9. **`rel_chapter_2_sec17-18.tex`**: Renamed `eq:rel-Ra-def` to `eq:rel-Ra-def-sec17` (duplicated from `rel_chapter_2_sec13-14.tex`).

### Compatibility Macros (rel_preamble.tex)

10. **`rel_preamble.tex`**: Added `\providecommand` definitions for:
    - `\dd` (upright differential)
    - `\vect` (3-vector bold notation, used in `rel_framework_mhd.tex`)
    - `\Ra` (classical Rayleigh number, used in `rel_chapter_2_sec13-14.tex` and `sec17-18`)
    - `\bulkP` (bulk viscous pressure alias)
    - `\taupi`, `\tauq`, `\tauPi` (IS relaxation times, used only in historical comparison paragraphs)

### BDNK Consistency (removing IS concepts from BDNK descriptions)

11. **`rel_chapter_2_sec16.tex`** (causalitycheck box): Removed incorrect reference to "BDNK causal modifications times $\tau_\pi$ and $\tau_q$" -- replaced with "BDNK causal frame coefficients". BDNK has no relaxation times.

12. **`rel_chapter_2_sec16.tex`** (nonlinear section): Changed "the BDNK causal modifications time $\tau_q$ introduces..." to "the BDNK frame coefficients introduce..." since BDNK does not use relaxation times.

13. **`rel_chapter_2_sec17-18.tex`** (NR limit): Changed "and $\tau_q \to 0$" to "and the BDNK frame corrections vanishing" since BDNK has no $\tau_q$.

14. **`rel_chapter_2_sec17-18.tex`** (causalitycheck box): Completely rewrote the causality verification box. The original incorrectly described BDNK using a relaxation-time formula $v_{\mathrm{heat}} = \sqrt{\kappa_T/\tau_q} \le c$; replaced with correct BDNK description (frame coefficients ensure bounded characteristic speeds).

15. **`rel_chapter_2_sec17-18.tex`** (QGP section): Replaced "The causal relaxation times $\tau_q$ and $\tau_\pi$ are of order..." with "The microscopic time-scales governing transport are of order..." to avoid attributing IS relaxation times to BDNK.

16. **`rel_chapter_2_sec17-18.tex`** (numerical simulations): Removed "($\tau_q = 0$)" from the description of replacing BDNK with Fourier law.

17. **`rel_chapter_2_sec17-18.tex`** (bibliographical notes, item 2): Fixed critical error where IS theory was described as "BDNK theory". Corrected to properly distinguish IS (relaxation equations) from BDNK (first-order constitutive relations in general frame).

18. **`rel_chapter_3_sec19-23.tex`** (linearized equations): Removed "(relaxation time $\tau_\pi$)" from the BDNK shear viscosity description. BDNK has no relaxation times.

19. **`rel_chapter_3_sec19-23.tex`** (after eq:rel-3-21): Completely rewrote the paragraph that incorrectly described "The BDNK causal term $\tau_\pi \partial^2 \delta v_i / \partial t^2$". Replaced with correct description: BDNK uses algebraic constitutive relations with no relaxation equation.

20. **`rel_chapter_3_sec19-23.tex`** (NR limit): Changed "and $\tau_\pi \to 0$" to "(in which limit the BDNK frame corrections also vanish)".

### Notation Consistency

21. **`rel_chapter_2_sec5-9.tex`**: Fixed `$\mu\nabla^2 u_i$` to `$\eta\nabla^2 u_i$` (line 277) -- the file uses $\eta$ for shear viscosity throughout, not $\mu$.

22. **`rel_chapter_2_sec17-18.tex`**: Changed "Boussinesq--Eckart limit" to "Boussinesq limit" since the Eckart frame is acausal and not used in BDNK.

## Items Verified (No Changes Needed)

### Mathematical Consistency
- All equation derivations checked: signs, factors of $c^2$, factors of $4\pi$ are correct
- Relativistic Alfven speed formula $v_A^2 = b^2 c^2 / (4\pi(\varepsilon + p) + b^2)$ correctly bounded by $c^2$
- Fast magnetosonic causality proof (eq:vf-causal-proof) is algebraically correct
- Sound speed bound $c_s^2 \le c^2$ consistently applied
- All $v/c \to 0$ limits verified to recover correct Newtonian forms
- Critical Rayleigh numbers: 657.511 (free-free), 1707.762 (rigid-rigid), 1100.65 (mixed) -- all correct

### BDNK Citations
- Bemfica, Disconzi & Noronha (2018) and Kovtun (2019) cited in all framework chapters
- Full bibliography in `rel_chapter_1.tex` and `rel_chapter_2_sec17-18.tex`
- Israel-Stewart references properly confined to historical comparison sections

### Cross-References
- All `\label`/`\ref` pairs checked for consistency within each file
- Cross-file references (e.g., to classical Chapter II equations) use consistent numbering

### Physical Correctness
- Enthalpy density $w = (\varepsilon + p)/c^2$ consistently replaces $\rho$ in all inertial terms
- Projection tensor $\Delta^{\mu\nu} = g^{\mu\nu} + u^\mu u^\nu / c^2$ used consistently
- BDNK constitutive relations are algebraic (first-order gradients) with no relaxation equations
- All environment balances verified: equation, align, enumerate, itemize, table, tcolorbox

### Notation
- $w$ for enthalpy density (with $w_0$ for background value)
- $\Delta^{\mu\nu}$ for projector
- $\eta$ (or `\shearvisc` = $\eta_{\mathrm{s}}$) for shear viscosity
- $\zeta$ (or `\bulkvisc`) for bulk viscosity
- $\kappa$ (or `\thermcond`) for thermal conductivity
- Note: $w$ is also used for vertical velocity component (Chandrasekhar convention), distinguished by context
