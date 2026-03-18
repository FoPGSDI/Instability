# Subagent B: Flow Stability Plots (Ch VII--IX)

**Date:** 2026-03-18
**Branch:** relativistic-causal
**Agent:** Phase 3 Plotting Agent B

## Scripts created

| # | Script | Output | Description |
|---|--------|--------|-------------|
| 1 | `plots/plot_couette_Taylor_critical.py` | `fig_couette_Taylor.pdf` | Critical Taylor number vs gap ratio and relativistic parameter. Ta_rel = Ta_cl (1+xi)^2 for eta = 0.5, 0.8, 0.95. |
| 2 | `plots/plot_couette_Rayleigh_criterion.py` | `fig_rayleigh_criterion.pdf` | Rayleigh stability diagram: classical d(r^2 Omega)^2/dr > 0 vs relativistic d(gamma^2 r^2 Omega)^2/dr > 0. Stability boundary shift with Lorentz factor. |
| 3 | `plots/plot_mri_dispersion.py` | `fig_mri_dispersion.pdf` | MRI dispersion omega(k) for Couette + axial B. Classical vs relativistic (bounded Alfven speed). Growth rate vs k for v_A/c = 0.1, 0.3, 0.5, 1.0, 2.0. |
| 4 | `plots/plot_couette_marginal_curves.py` | `fig_couette_marginal.pdf` | Marginal stability curves Ta vs wavenumber a, narrow gap. Classical minimum at a_c = 3.14, Ta_c = 3430. Relativistic curves for xi = 0, 0.05, 0.10, 0.20, 0.35, 0.50. |

## Physics summary

- **Taylor number:** Relativistic effects stabilise the flow -- the critical Taylor number increases as (1+xi)^2.
- **Rayleigh criterion:** The Lorentz factor gamma in the angular momentum shifts the stability boundary upward in mu = Omega_2/Omega_1 space, requiring more co-rotation for stability.
- **MRI:** Bounding the Alfven speed at c suppresses the MRI at high v_A/c, reducing growth rates and narrowing the unstable wavenumber band.
- **Marginal curves:** The neutral curve lifts uniformly with xi; the critical wavenumber stays near a_c ~ pi but the critical Ta increases.

## Status

All four scripts produce publication-quality PDF figures via matplotlib (Agg backend, serif fonts, 300 dpi).
