## Agent 10: Ch III, Sections 29-31 — Completed

### Application added
- **Topic**: Overstability in NS core — BDNK cubic vs classical growth rates
- **Quantitative calculations**:
  - Thermal relaxation: tau_q ~ 3e-13 s (electron mfp / c)
  - Viscous relaxation: tau_pi ~ 1e-12 s (neutron Fermi velocity)
  - Overstable frequency for 500 Hz pulsar: f_osc ~ 4490 Hz (12% below classical)
  - tau_q * omega ~ 1e-8 (BDNK corrections perturbatively small)
  - Growth rate reduced by 23% due to enthalpy factor for w/(rho c^2) = 1.3
  - Growth timescale: t_grow ~ 12 days for Ra/Ra_c = 2

### Figure
- Script: `plots/ch3/plot_ns_overstability_growth.py`
- Output: `plots/ch3/fig_ns_overstability_growth.pdf`
- Two panels: (a) growth rates near onset (Classical/BDNK/IS), (b) oscillation frequency vs Ta_rel

### References
- Complete references section with 9 entries (Bemfica et al., Chandrasekhar, Flowers & Itoh, Israel, Israel & Stewart, Kovtun, Radice et al., Romatschke, Shternin & Yakovlev)

### Files modified
- `output/chapters/relativistic/rel_chapter_3_sec29-31.tex`
