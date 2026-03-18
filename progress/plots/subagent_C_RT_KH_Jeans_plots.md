# Subagent C: RT, KH, Jeans Instability Plots (Phase 3)

**Agent:** Phase 3 Plotting Agent C
**Branch:** `relativistic-causal`
**Date:** 2026-03-18

## Scripts Created

| # | Script | Output | Description |
|---|--------|--------|-------------|
| 1 | `plots/plot_RT_growth_rate.py` | `fig_RT_growth.pdf` | Rayleigh-Taylor growth rate: classical vs relativistic Atwood number, BDNK viscous damping |
| 2 | `plots/plot_KH_critical_velocity.py` | `fig_KH_critical.pdf` | KH critical velocity vs density ratio for various surface tensions, Lorentz factor correction |
| 3 | `plots/plot_KH_relativistic_jet.py` | `fig_KH_jet.pdf` | KH growth rate vs wavenumber for Gamma = 1, 2, 5, 10, 100; sigma ~ Gamma^{-2} suppression |
| 4 | `plots/plot_jeans_mass.py` | `fig_jeans_mass.pdf` | Jeans mass GR correction M_J,rel/M_J vs p/epsilon; Chandrasekhar gamma_c = 4/3 + 38GM/(21Rc^2) |
| 5 | `plots/plot_causality_speeds.py` | `fig_causality_speeds.pdf` | All characteristic speeds (c_s, v_A, v_f, v_s) vs magnetisation, bounded by c |
| 6 | `plots/plot_bdnk_vs_is_dispersion.py` | `fig_bdnk_vs_is.pdf` | BDNK (3rd-order) vs IS (5th-order) dispersion: agree at low k, diverge at high k |

## Physics Content

### Rayleigh-Taylor (RT)
- Classical Atwood number A = (rho2 - rho1)/(rho2 + rho1)
- Relativistic Atwood number A_rel = (w2 - w1)/(w2 + w1) with enthalpy density w
- BDNK viscous damping: sigma^2 + nu k^2 sigma - gkA = 0

### Kelvin-Helmholtz (KH)
- Classical V_crit depends on density ratio and surface tension
- Relativistic: V_rel^2 = V_class^2/(1 + V_class^2) ensures V < c
- Jet KH: sigma_peak ~ Gamma^{-2} for ultrarelativistic jets

### Jeans Instability
- GR correction: M_J,rel/M_J ~ 1 - (3/2)(p/eps)(1 + c_s^2)
- Pressure contributes to gravitational source in GR (destabilising)
- Chandrasekhar threshold: gamma_c = 4/3 + (38/21) GM/(Rc^2)

### Causality Verification
- Relativistic Alfven speed: v_A^2 = sigma_B/(1 + sigma_B) < c^2
- Fast magnetosonic: v_f^2 = c_s^2 + v_A^2 - c_s^2 v_A^2 < c^2
- All characteristic speeds remain subluminal

### BDNK vs Israel-Stewart
- BDNK: 3rd-order polynomial (only physical modes)
- IS: 5th-order polynomial (extra non-hydrodynamic relaxation modes)
- Agreement at low k (long wavelength), divergence at high k (UV)

## Status

All 6 scripts execute successfully and produce publication-quality PDF and PNG output.
