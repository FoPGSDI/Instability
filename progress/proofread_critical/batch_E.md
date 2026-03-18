# Critical Proofreading Batch E: BibTeX Cleanup + Final Compile

**Agent:** Critical Proofreading Agent E
**Date:** 2026-03-18
**Branch:** rel-lg

## Part 1: SHARED_REFERENCES.bib Cleanup

### Duplicates Removed
- **AbramowiczFragile2013**: Exact duplicate entry removed (same paper appeared twice)
- **Gourgouliatos2018**: Two DIFFERENT papers with same key
  - Kept: Gourgouliatos & Hollerbach (2018) magnetar crust simulations (ApJ 852, 21)
  - Renamed: Gourgouliatos & Komissarov (2018) jet reconfinement (Nat. Astron. 2, 167) -> `GourgouliatosKomissarov2018`
  - Updated citations in `rel_chapter_10_sec96-97.tex` and `rel_chapter_11_sec105-106.tex`
- **Radice2018**: Two DIFFERENT papers with same key
  - Kept: Radice et al. (2018) long-lived remnants (MNRAS 481, 3670)
  - Renamed: Radice & Bernuzzi (2018) neutrino-radiation hydro (ApJ 869, 130) -> `RadiceBernuzzi2018`
- **LattimerPrakash2001 / Lattimer2001**: Same paper, different keys. Removed unused `LattimerPrakash2001`

### Unused Entries Removed (12 total)
AloyRezzolla2006, Busse1978, DenicolNiemi2012, DR11_BDNKNSevolution2025,
FontLRR2008, HiscockLindblom1983, LattimerPrakash2001, LattimerPrakash2007,
Rayleigh1880, RomatschkeRomatschke2019, Stergioulas2003, WeinbergGC1972

### Final Bib Stats
- **234 unique entries** (down from 247 raw entries)
- Sorted alphabetically by first author last name, then year
- All 228 `\cite` keys in tex files verified to have matching bib entries
- 16 BibTeX warnings (all "empty journal" for arXiv-only preprints, expected)

## Part 2: Plot Scripts

### Deep plots (52 scripts)
All 52 `plots/deep/fig_*.py` scripts ran successfully. Minor runtime warnings:
- `fig_jet_rt_magnetic.py`: sqrt of negative values (clamped to 0, expected)
- `fig_ns_merger_mixing.py`: divide by zero (at k=0, expected)
- `fig_nuclear_transport.py`: tight_layout warning (cosmetic)

### Chapter plots (57 scripts across ch1-ch14)
All 57 chapter plot scripts ran successfully. Minor warnings:
- `ch2/plot_benard_Ra_rel_contours.py`: no contour levels in one subplot
- `ch7/plot_taylor_couette_narrow_gap.py`: divide by zero at mu=−1 (expected)
- `ch11/plot_grb_jet_growth_rate.py`: deprecated pcolormesh grid auto-removal

**Total: 109/109 plot scripts successful.**

## Part 3: Final Compilation

### Fixes Applied
1. Added `{../../../plots/framework/relativistic/}` to `\graphicspath` -- resolved missing figures:
   - `fig_bdnk_char_speeds.pdf`
   - `fig_alfven_magnetosonic_speeds.pdf`
   - `fig_eos_comparison.pdf`
2. Fixed `fig_gw_convection.pdf` path (was `plots/deep/fig_gw_convection.pdf`, changed to `fig_gw_convection.pdf`)
3. Added `\usepackage{amsthm}` and `\newtheorem{theorem}{Theorem}[chapter]` to resolve undefined `theorem` environment

### Compilation Results
- **Final page count: 745 pages**
- **PDF size: 9.68 MB**
- **BibTeX warnings: 16** (empty journal fields for arXiv preprints)
- **LaTeX warnings: ~1173** (mostly overfull hboxes, some undefined table refs)
- **Remaining errors: 118** (pre-existing math-mode issues in chapter tex files)
  - 46 double subscripts
  - 26 missing $ signs
  - 10 display math endings
  - Other misc math formatting
- **Undefined references:**
  - `eq:14-30` (4 occurrences, page 662)
  - Various `tab:XX*` table references (~20 occurrences across chapters)

### Compilation Command
```bash
pdflatex -> bibtex -> pdflatex -> pdflatex
```
All 4 passes completed without fatal errors; PDF generated successfully.
