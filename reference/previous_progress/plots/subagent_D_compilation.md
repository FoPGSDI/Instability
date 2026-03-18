# Phase 3D: Compilation Report

## Summary

Created a self-contained `book_main.tex` that compiles successfully to a 480-page PDF.

## Files Created

- `output/chapters/relativistic/book_main.tex` -- Complete, self-contained LaTeX document
- `output/chapters/relativistic/Makefile` -- Build automation (two-pass pdflatex)
- `output/chapters/relativistic/book_main.pdf` -- Generated PDF (480 pages, ~2.1 MB)

## Compilation Details

- **Compiler**: pdfTeX 3.141592653-2.6-1.40.25 (TeX Live 2023)
- **Document class**: `book`, 12pt
- **Total pages**: 480 (including title page and table of contents)
- **Chapters included**: 3 framework chapters + 14 stability chapters (55 input files total)

## Issues Fixed

1. **Illegal parameter number in hyperref bookmark** (fatal): `\boldsymbol{\Omega}` in a
   `\section` title in `rel_chapter_3_sec32-35.tex` caused hyperref to crash when generating
   PDF bookmarks. Fixed by wrapping in `\texorpdfstring`. Also added global
   `\pdfstringdefDisableCommands` to the preamble for robustness.

2. **headheight warning**: Added `headheight=15pt` to geometry options to suppress
   fancyhdr warning.

3. **Undefined cross-references**: Some `\ref` targets (e.g., `eq:3-293`, `sec:3-33`)
   point to labels in the original Chandrasekhar text that are not defined in the
   relativistic chapters. These produce LaTeX warnings but do not prevent compilation.
   They appear as "??" in the output and can be resolved in a future editing pass.

## Compilation Attempts

| Attempt | Result | Notes |
|---------|--------|-------|
| 1 | Fatal error | `\boldsymbol` in section title crashed hyperref |
| 2 | Success (464 pp) | First pass, TOC placeholder |
| 3 | Success (480 pp) | Second pass, cross-refs and TOC resolved |

## Build Instructions

```bash
cd output/chapters/relativistic
make          # builds book_main.pdf (two pdflatex passes)
make clean    # removes auxiliary files
```
