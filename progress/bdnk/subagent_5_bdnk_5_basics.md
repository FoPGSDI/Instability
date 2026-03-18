# Agent 5: BDNK Basic Concepts (Ch I)

## File modified
- `output/chapters/relativistic/rel_chapter_1.tex`

## Changes made (IS -> BDNK conversion)

1. **Introduction**: Replaced Israel-Stewart reference with BDNK description; cited Bemfica, Disconzi & Noronha (2018) and Kovtun (2019).

2. **Dissipative sector** (Sec 1.2b): Completely rewritten.
   - Renamed from "Israel-Stewart dissipative sector" to "BDNK dissipative sector".
   - Replaced IS relaxation equations (tau_pi, tau_q, tau_Pi) with BDNK algebraic constitutive relations.
   - General-frame decomposition: E, P, Q^mu, Pi^{mu nu} given algebraically, not via relaxation.
   - Explicit statement: "BDNK achieves causality with a simpler PDE structure than IS."
   - Causality enforcement: replaced "tau > 0 ensures hyperbolicity" with "BDNK frame coefficients ensure strong hyperbolicity."
   - Non-relativistic limit: BDNK -> Navier-Stokes (frame corrections vanish at O(v^2/c^2)).

3. **Normal-mode analysis** (Sec 1.3):
   - Background state: dissipative quantities determined algebraically, not independent DOFs.
   - Perturbations: only (delta epsilon, delta u^mu) are independent; dissipative perturbations follow from constitutive relations.
   - Linearised equations: closed system from conservation laws + BDNK constitutive relations alone.
   - Dispersion relations: standard-order polynomials (no extra relaxation modes from IS).

4. **Causality constraint on modes** (Sec 1.3d):
   - Replaced IS causality proof (positive relaxation times) with BDNK strong hyperbolicity (frame coefficient inequalities).
   - Noted BDNK proof is rigorous at full nonlinear level (stronger than IS linearised proof).

5. **Summary** (Sec 1.5):
   - Replaced "tau -> 0 (instantaneous relaxation)" with "BDNK frame corrections -> 0 at O(v^2/c^2)."
   - Updated constitutive relation references from IS to BDNK.

6. **Bibliographical notes**:
   - Added Bemfica, Disconzi & Noronha (2018), Kovtun (2019), BDN (2019 PRL), Hoult & Kovtun (2020).
   - Retained IS references (Israel 1976, Israel & Stewart 1979) in separate block for historical context.

7. **Dimensionless numbers** (Sec 1.4): Unchanged (Ra, Ta, Re, Pr corrections are the same since they appear at marginal state where dissipative terms vanish).

## Status: COMPLETE
