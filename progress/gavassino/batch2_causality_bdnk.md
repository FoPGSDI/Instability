# Gavassino Integration Batch 2: Causality and BDNK Papers

## Status: COMPLETE

## Papers Processed

### Paper 9: 2401.13852 — Information current in first-order hydro
- **Authors:** Gavassino, Abboud, Speranza, Noronha
- **Key result:** First construction of a timelike future-directed information current E^mu within BDNK first-order hydrodynamics. UV-regularization of the truncated entropy current makes E^mu timelike at all gradients. Equal-time correlators computed; frame-independence of physical correlators demonstrated.
- **Target:** Framework hydro (rel_framework_hydro.tex)
- **Integration:** New section "Information Current and Fluctuating BDNK Hydrodynamics" added with definition of E^mu, stability conditions, and connection to fluctuations.
- **BibTeX key:** GavassinoInfoCurrentBDNK2024

### Paper 10: 2402.06776 — Fluctuations in BDNK
- **Authors:** Gavassino, Hippert, Mullins, Noronha
- **Key result:** First mathematically consistent BDNK theory for linear stochastic fluctuations. MSR action is bilocal, noise is not white, but conserved-density correlators are localized and match IS. Non-local mapping between IS and BDNK actions constructed.
- **Target:** Framework hydro (rel_framework_hydro.tex)
- **Integration:** Subsection on fluctuating BDNK theory with noise correlator formula and MSR effective action.
- **BibTeX key:** GavassinoBDNKFluctuations2024

### Paper 11: 2309.00512 — Hydro fluctuations from effective action
- **Authors:** Mullins, Hippert, Gavassino, Noronha
- **Key result:** Schwinger-Keldysh approach to first-order BDNK shows causality-stability tradeoff for fluctuations; MSR approach using information current resolves this for IS-type theories. Z_2 symmetry (modified KMS) identified that implements detailed balance covariantly.
- **Target:** Framework hydro (rel_framework_hydro.tex)
- **Integration:** Added discussion of Z_2/KMS symmetry in the fluctuations section; cited in reference list.
- **BibTeX key:** MullinsHippertGavassinoNoronha2024

### Paper 12: 2508.04918 — Acausality-driven instabilities in IS [KEY PAPER]
- **Authors:** Gavassino, Hirvonen, Paquet, Singh, Soares Rocha
- **Key result:** IS acausality causes NONLINEAR instabilities (blowup). Classification of fluid cells into "good" (causal), "bad" (acausal but stable), "ugly" (acausal and unstable). Condition v^2 w^2 >= 1 for instability onset. New analytical benchmark solution demonstrating bifurcation. Numerical confirmation with MUSIC solver.
- **Target:** Ch X (RT) and Ch XI (KH)
- **Integration:**
  - New subsection in rel_chapter_10_sec98-99.tex: "Israel-Stewart acausality and nonlinear Rayleigh-Taylor instabilities"
  - New subsection in rel_chapter_11_sec105-106.tex: "Acausality-driven instabilities in Israel-Stewart and validation of BDNK"
  - Both sections explain good/bad/ugly classification, reversed dissipation mechanism, and why BDNK avoids the pathology
- **BibTeX key:** GavassinoAcausalityIS2025

### Paper 13: 2511.07946 — Causality violation in heavy-ion sims
- **Authors:** Gavassino, Hirvonen, Paquet, Singh, Soares Rocha
- **Key result:** Conference proceedings summarizing Paper 12 results with additional context from IP-Glasma initial conditions showing significant fractions of computational domain entering "bad"/"ugly" regimes. MUSIC solver comparison with analytical benchmark.
- **Target:** Ch II sec17-18
- **Integration:** New subsection in rel_chapter_2_sec17-18.tex: "Acausality-driven instabilities in practical simulations" discussing IP-Glasma results and analytical benchmark bifurcation.
- **BibTeX key:** GavassinoCausalityHIC2025

### Paper 14: 2307.05987 — Dispersion relations alone can't guarantee causality
- **Authors:** Gavassino, Disconzi, Noronha
- **Key result:** Proves that individual dispersion relations omega(k) are ALWAYS superluminal unless omega = a + bk. Causality emerges from cancellation of all excitation branches. Analogy: non-hydrodynamic modes are to hydrodynamics as antiparticles are to relativistic QM.
- **Target:** Framework thermo (rel_framework_thermo.tex)
- **Integration:** New subsection "Dispersion Relations and Causality" explaining why single-branch arguments for causality fail, and the essential role of non-hydrodynamic modes.
- **BibTeX key:** GavassinoDispersions2024

### Paper 15: 2301.06651 — Bounds on transport from stability
- **Authors:** Gavassino
- **Key result:** Im(omega) <= |Im(k)| is a NECESSARY condition for covariant stability. Identical to the bound derived by HSSW from microcausality. Implies: c_s <= c, D >= 0 with upper bound, and fluids with c_s = c have vanishing viscosities.
- **Target:** Framework thermo (rel_framework_thermo.tex)
- **Integration:** New subsection "Transport Bounds from Stability and Causality" with the fundamental inequality and its physical consequences.
- **BibTeX key:** GavassinoBounds2023

### Paper 16: 2312.07442 — Stochastic hydro from information flow
- **Authors:** Mullins, Hippert, Gavassino, Noronha
- **Key result:** Conference proceedings presenting the information current approach to stochastic fluctuations. Noise correlators determined by entropy production: <xi_A xi_B> = 2 sigma_AB delta^4(x-x'). Effective action derived via MSR path integral with detailed-balance symmetry.
- **Target:** Framework hydro (rel_framework_hydro.tex)
- **Integration:** Cited alongside Papers 10-11 in the fluctuations section.
- **BibTeX key:** MullinsGavassinoStochastic2024

## Files Modified
- `/data/haiyangw/claude/Instability/SHARED_REFERENCES.bib` — 8 new BibTeX entries
- `/data/haiyangw/claude/Instability/output/chapters/relativistic/rel_framework_hydro.tex` — New section on information current and fluctuating BDNK
- `/data/haiyangw/claude/Instability/output/chapters/relativistic/rel_framework_thermo.tex` — New subsections on transport bounds and dispersion relations
- `/data/haiyangw/claude/Instability/output/chapters/relativistic/rel_chapter_10_sec98-99.tex` — IS acausality discussion for RT
- `/data/haiyangw/claude/Instability/output/chapters/relativistic/rel_chapter_11_sec105-106.tex` — IS acausality discussion for KH
- `/data/haiyangw/claude/Instability/output/chapters/relativistic/rel_chapter_2_sec17-18.tex` — Practical acausality discussion

## Papers Downloaded
All 8 papers downloaded to `/data/haiyangw/claude/Instability/gavassino_papers/`:
- 2401.13852/, 2402.06776/, 2309.00512/, 2508.04918/
- 2511.07946/, 2307.05987/, 2301.06651/, 2312.07442/
