# Relativistic Instabilities — Figure-Integrated Book with Complete References

## Overview
Transform the BDNK relativistic Chandrasekhar book into a modern publishable work with:
1. **Serious astrophysical applications** with quantitative figures embedded in each chapter
2. **Complete reference lists** per chapter (classical + relativistic + BDNK)
3. **Publication-quality Python-generated figures** integrated into the LaTeX text
4. **Proofread, recalculated, syntax-correct** final product

## Branch: `relativistic-figs-ref`

## Methodology (from Claude-for-Research framework)
- Markers: [HYPOTHESIS], [VALIDATED], [BLOCKING], [FUTURE], [SPECULATION]
- Session protocol: evaluate → plan → execute → reflect
- Agents: tactical execution; humans: strategic direction

## Phase 1: Applications + Figures + References (60 agents)
Each agent:
1. Reads its chapter section tex file
2. **Adds serious astrophysical applications** with quantitative calculations:
   - Neutron stars, accretion disks, relativistic jets, QGP, early universe, GW sources
   - Numerical estimates with physical parameters
3. **Writes a Python plotting script** that generates publication-quality figures
4. **Integrates figures into the LaTeX** using \includegraphics
5. **Compiles a complete reference list** for the chapter section (BibTeX entries)
6. Documents progress in `progress/phase1/subagent_{N}_{task}_{tasknumber}_{desc}.md`
7. Commits and pushes

## Phase 2: Proofread + Recalculate (batch agents)
## Phase 3: Final PDF Compilation

## Shared Files
- `MASTER_PLAN.md` — this file
- `SHARED_REFERENCES.bib` — master bibliography
- `SHARED_PLOT_STYLE.py` — common matplotlib style
- `progress/phase1/` — agent documentation
