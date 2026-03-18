# Phase 3A: Thermal Instability Verification Plots

**Agent:** Plotting Subagent A
**Date:** 2026-03-18
**Branch:** `relativistic-causal`

## Overview

Five self-contained Python scripts were created in `plots/` to generate
publication-quality figures verifying the thermal instability results of
Chapters I--VI.  Each script uses matplotlib + numpy, outputs both PDF and
PNG, and requires no external data files.

## Scripts

| # | Script | Output | Description |
|---|--------|--------|-------------|
| 1 | `plot_benard_Ra_critical.py` | `fig_benard_Ra.{pdf,png}` | Critical Rayleigh number Ra_c vs relativistic parameter xi for three boundary types (free-free, rigid-rigid, rigid-free). Shows the 1/(1+xi) suppression. |
| 2 | `plot_rotation_Ra_Ta.py` | `fig_rotation_Ra_Ta.{pdf,png}` | Critical Ra vs Taylor number Ta for rotating convection. Stationary and overstable branches with Ta^{2/3} and Ta^{1/3} asymptotic laws. Classical vs relativistic (xi = 0, 0.1, 0.33). |
| 3 | `plot_magnetic_Ra_Q.py` | `fig_magnetic_Ra_Q.{pdf,png}` | Critical Ra vs Chandrasekhar number Q for magneto-convection. Verifies the pi^2 Q asymptote and shows relativistic Q_rel = Q/(1 + v_A^2/c^2) correction. |
| 4 | `plot_dispersion_thermal.py` | `fig_dispersion_thermal.{pdf,png}` | Four-panel dispersion relation comparison: classical Navier-Stokes vs BDNK relativistic. Sound modes, thermal diffusion mode, attenuation, and group velocity causality check (v_g < c). |
| 5 | `plot_sphere_Ra_compactness.py` | `fig_sphere_Ra.{pdf,png}` | Critical Ra vs stellar compactness GM/(Rc^2) for spherical convection. Shows metric and enthalpy corrections for stiff, moderate, and soft EOS. Marks the Buchdahl limit and neutron-star compactness band. |

## Key physics verified

- **Benard problem:** Relativistic enthalpy 1/(1+xi) universally lowers the
  convective threshold, independent of boundary conditions.
- **Rotation:** Both stationary and overstable branches shift downward; the
  effective Taylor number Ta_rel = Ta/(1+xi)^2 encapsulates the correction.
- **Magnetic field:** The Alfven-speed correction Q_rel = Q/(1+v_A^2/c^2)
  reduces magnetic stabilisation; pi^2 Q law preserved.
- **Dispersion:** BDNK thermal mode saturates at Im(omega) = -1/tau_q
  (causal), unlike the classical parabolic Im(omega) = -kappa k^2 (acausal).
  All group velocities remain subluminal.
- **Spherical geometry:** Competition between metric enhancement and enthalpy
  softening; Ra_c(C) is non-monotonic for soft equations of state.

## How to run

```bash
cd /data/haiyangw/claude/Instability
python plots/plot_benard_Ra_critical.py
python plots/plot_rotation_Ra_Ta.py
python plots/plot_magnetic_Ra_Q.py
python plots/plot_dispersion_thermal.py
python plots/plot_sphere_Ra_compactness.py
```
