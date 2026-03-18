# Plot Generation Report

**Date:** 2026-03-18
**Branch:** relativistic-figs-ref
**Agent:** Wave 2 Plot Polishing Agent B

## Summary

- **Total scripts:** 117
- **Successfully generated:** 117
- **Failed:** 0

## Initial Failures (13 scripts, all fixed)

All 13 failures were caused by the same issue: `SHARED_PLOT_STYLE` module import
using a relative path (`sys.path.insert(0, '../..')`) that resolves incorrectly
when scripts are executed from the repository root rather than from the script's
own directory.

**Fix applied:** Replaced relative path with `__file__`-based absolute path
resolution:
```python
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
```

### Affected scripts

| # | Script | Chapter |
|---|--------|---------|
| 1 | `plots/ch1/plot_xi_astrophysical_regimes.py` | Ch 1 |
| 2 | `plots/ch2/plot_bdnk_vs_classical_dispersion.py` | Ch 2 |
| 3 | `plots/ch2/plot_benard_Ra_rel_contours.py` | Ch 2 |
| 4 | `plots/ch2/plot_cell_pattern_selection.py` | Ch 2 |
| 5 | `plots/ch2/plot_critical_Ra_table.py` | Ch 2 |
| 6 | `plots/ch2/plot_observational_parameter_space.py` | Ch 2 |
| 7 | `plots/ch2/plot_rayleigh_quotient_vs_xi.py` | Ch 2 |
| 8 | `plots/ch7/plot_epicyclic_frequencies.py` | Ch 7 |
| 9 | `plots/ch7/plot_Phi_rel_schwarzschild_kerr.py` | Ch 7 |
| 10 | `plots/ch7/plot_rayleigh_criterion_isco.py` | Ch 7 |
| 11 | `plots/ch7/plot_taylor_couette_narrow_gap.py` | Ch 7 |
| 12 | `plots/ch7/plot_viscous_disk_Re_alpha.py` | Ch 7 |
| 13 | `plots/ch7/plot_wide_gap_critical_conditions.py` | Ch 7 |

## Warnings (non-fatal)

- `plots/ch2/plot_benard_Ra_rel_contours.py`: "No contour levels were found within the data range" (cosmetic; plot still saved)
- `plots/ch7/plot_taylor_couette_narrow_gap.py`: "divide by zero encountered in divide" (handled by numpy; plot still correct)

## PDF Output Counts by Directory

| Directory | PDF count |
|-----------|-----------|
| `plots/` (root) | 15 |
| `plots/ch1/` | 1 |
| `plots/ch2/` | 6 |
| `plots/ch3/` | 4 |
| `plots/ch4/` | 4 |
| `plots/ch5/` | 3 |
| `plots/ch6/` | 5 |
| `plots/ch7/` | 6 |
| `plots/ch8/` | 4 |
| `plots/ch9/` | 4 |
| `plots/ch10/` | 6 |
| `plots/ch11/` | 4 |
| `plots/ch12/` | 4 |
| `plots/ch13/` | 3 |
| `plots/ch14/` | 2 |
| `plots/deep/` | 43 |
| `plots/framework/relativistic/` | 3 |
| **Total** | **117** |
