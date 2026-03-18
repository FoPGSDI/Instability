# Deep Research Agent 1, Sub-task 2
## rel_chapter_2_sec5-9.tex: BDNK/IS thermal relaxation scales

### Status: COMPLETE

### Changes made:
- Added new Section "BDNK and Israel-Stewart thermal relaxation scales" before References
- Derived l_BDNK = kappa/(c^2 rho c_p) and l_IS = sqrt(kappa tau_q / (rho c_p))
- Showed leading-order agreement and O(l/lambda)^2 differences in dispersion
- Numerical evaluation for NS ocean: l_BDNK ~ 10^{-18} cm

### New plot:
- `plots/deep/fig_relaxation_scales.py` -> `fig_relaxation_scales.pdf`
  - Left: l_BDNK and l_IS vs T for NS ocean
  - Right: ratio and higher-order correction
