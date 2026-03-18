# Book Translation: PDF to LaTeX+BibTeX

## Project: Chandrasekhar — "Hydrodynamic and Hydromagnetic Stability" (1961)

**Source:** `18ChandrasekharBook copy.pdf` (685 PDF pages, scanned/image-based)
**Target:** LaTeX source files + BibTeX bibliography, organized by chapter.

---

## Essentials

**Your role:** You are one of 20 parallel translation agents. Each agent owns a specific chapter/section assignment. You must OCR the scanned PDF pages, transcribe text faithfully, and convert it to publication-quality LaTeX with proper mathematical typesetting.

**Primary output:** LaTeX `.tex` files in `output/chapters/` and BibTeX entries in `output/bibtex/`.

**Progress tracking:** Each agent records stage-wise progress in `progress/agent_{N}_chapter_{C}_stage_{S}.md` files.

---

## PDF Page ↔ Book Page Mapping

Book page 1 (Chapter I start) = PDF page 17. **Offset = 16.**
- `PDF_page = book_page + 16` (for numbered pages)
- Front matter (roman numerals) = PDF pages 1–16

---

## Agent Assignments

### Wave 1 (Agents 1–20): Initial parallel translation — COMPLETED
All 20 original agents have finished. Chapters 2, 3, 7 were split across two agents and merged.

### Wave 2 (Agents 21–30): Gap-filling for content-filter failures — COMPLETED
10 targeted agents filled gaps in Ch V (§51-52, §53-54+bib), Ch III (§35+bib), Ch VII (§74+bib), merged references.bib, and created merge_chapters.sh.

### Wave 3 (Agents 31–50): Final gap closure — ACTIVE
20 agents targeting the 5 remaining TODO stubs, each failed task split into 3 sub-agents.

**Remaining TODO stubs (as of Wave 3 launch):**

| # | File | Stub | Content | Pages |
|---|------|------|---------|-------|
| A | chapter_5.tex | §49-50 | Descriptive text on rotation+field effects | ~2pp |
| B | chapter_2.tex | §18 + bib notes | Experiments on thermal instability | ~15pp |
| C | chapter_11.tex | §106 | Effect of horizontal magnetic field | ~5pp |
| D | chapter_11.tex | bib notes | Bibliographical reference list | ~3pp |
| E | chapter_3.tex/chapter_7.tex | fragment assembly | Append fragment files to merged chapters | — |

**Failure-splitting rule:** When a task fails (content filter / timeout), split into 3 smaller sub-agents. Assembly of fragments happens ONLY after ALL sub-tasks complete.

### Wave 4 (Final): Assembly + Compilation — COMPLETED
3 agents: (1) assembled Ch II §18+bib into chapter_2.tex, (2) verified Ch V + Ch XI, (3) compiled PDF.

**Result: main.pdf — 639 pages, 0 errors, compiled successfully.**

---

## Known Issues (for future work)

1. **Content filter gaps**: Ch II §18(c)-(d) (Silveston/optical experiments) and Ch XI §106(a) (streaming-direction field) could not be transcribed due to persistent content filtering. The surrounding content IS present.
2. **12 undefined equation refs**: eq:10-116, eq:10-243, eq:10-269, eq:7-27a, eq:9-188, eq:9-245, eq:9-260 — labels never defined.
3. **1 missing bib entry**: `Hain1957` cited but not in references.bib.
4. **Ch V §52 truncation**: sec51_52 fragment ends mid-sentence around line 895.
5. **Equation numbering gaps**: Ch 6 (4), Ch 9 (10), Ch 10 (2) — some equations not transcribed from scanned pages.
6. **438 overfull hboxes**: Cosmetic layout warnings from long equations.

### PDF Page Offset Note
The offset varies due to inserted half-tone plates:
- Ch I–III: offset ≈ 16 (PDF page = book page + 16)
- Ch IV–V: offset ≈ 22–24 (plates inserted)
- Ch VI+: offset ≈ 24–32 (more plates)
- Always verify by checking page headers in the PDF

---

## Translation Stages (per agent)

Each agent proceeds through 5 stages, recording progress after each:

### Stage 1: OCR & Raw Transcription
- Read assigned PDF pages (max 20 pages per Read call — batch accordingly)
- Transcribe all text faithfully, preserving paragraph structure
- Note all equation numbers, section numbers, figure/table references
- **Figures: SKIP content, insert placeholder** `\figurePlaceholder{fig_number}{caption_text}`
- Record: `progress/agent_{N}_chapter_{C}_stage_1.md`

### Stage 2: LaTeX Structure
- Create proper LaTeX document structure: `\chapter`, `\section`, `\subsection`
- Set up equation environments: `equation`, `align`, `gather` as appropriate
- Handle numbered equations with `\label{eq:chN-NUM}` and `\eqref` cross-refs
- Create table environments for any data tables
- Record: `progress/agent_{N}_chapter_{C}_stage_2.md`

### Stage 3: Mathematical Typesetting
- Convert ALL mathematical expressions to proper LaTeX
- Inline math: `$...$`; display math: `\begin{equation}...\end{equation}`
- Vectors bold: `\boldsymbol{}` or `\mathbf{}`; operators: `\nabla`, `\partial`, etc.
- Matrices, determinants, integrals, summations — all proper LaTeX
- Verify equation numbering matches original
- Record: `progress/agent_{N}_chapter_{C}_stage_3.md`

### Stage 4: Bibliography & Cross-References
- Extract all citations from "Bibliographical Notes" sections
- Create BibTeX entries in `output/bibtex/chapter_{C}.bib`
- Use `\cite{}` commands with keys like `chandrasekhar1961`, `rayleigh1880`, etc.
- Handle internal cross-references: `\ref`, `\eqref`, `\pageref`
- Record: `progress/agent_{N}_chapter_{C}_stage_4.md`

### Stage 5: Review & Output
- Proofread LaTeX for typographical errors
- Verify structural completeness against PDF
- Write final `.tex` file to `output/chapters/chapter_{C}.tex`
- Write final `.bib` file to `output/bibtex/chapter_{C}.bib`
- Record: `progress/agent_{N}_chapter_{C}_stage_5.md`

---

## LaTeX Conventions

```latex
\documentclass[12pt]{book}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{bm}           % bold math
\usepackage{mathrsfs}     % script letters
\usepackage{graphicx}     % figure placeholders
\usepackage{natbib}       % bibliography
\usepackage{hyperref}     % cross-references

% Custom commands for this book
\newcommand{\vect}[1]{\boldsymbol{#1}}
\newcommand{\mat}[1]{\mathbf{#1}}
\newcommand{\dd}{\mathrm{d}}            % differential d
\newcommand{\pp}{\partial}              % partial
\newcommand{\Ra}{\mathrm{Ra}}           % Rayleigh number
\newcommand{\Ta}{\mathrm{Ta}}           % Taylor number
\newcommand{\Rey}{\mathrm{Re}}          % Reynolds number
\newcommand{\Pran}{\mathrm{Pr}}         % Prandtl number
\newcommand{\figurePlaceholder}[2]{%
  \begin{figure}[htbp]
    \centering
    \fbox{\parbox{0.8\textwidth}{\centering\vspace{2cm}[Figure #1: #2]\vspace{2cm}}}
    \caption{#2}
    \label{fig:#1}
  \end{figure}
}
```

---

## Progress File Format

Each `progress/agent_{N}_chapter_{C}_stage_{S}.md` must contain:

```markdown
---
agent: {N}
chapter: {C}
stage: {S}
status: {in_progress | completed | blocked}
timestamp: {ISO 8601}
---

## Summary
[What was accomplished in this stage]

## Issues / Notes
[Any problems encountered, ambiguous text, unclear equations]

## Next
[What the next stage will address]
```

---

## Markers (from research framework)

- `[UNCLEAR: ...]` — OCR text that is ambiguous or illegible
- `[EQUATION_CHECK: ...]` — equation that needs verification
- `[CROSS_REF: ...]` — cross-reference that needs resolution
- `[FIGURE: fig_N]` — figure placeholder location
- `[TABLE: table_N]` — table requiring manual data entry verification

---

## When to Flag for Human Review

- Illegible text in the scanned PDF
- Equations where symbols are ambiguous (e.g., similar-looking Greek letters)
- Tables with complex numerical data requiring verification
- Cross-references to sections handled by other agents

---

## Anti-patterns

- Do NOT guess at illegible text — mark it `[UNCLEAR]`
- Do NOT attempt to recreate figures — use placeholders only
- Do NOT rewrite or modernize the author's prose — transcribe faithfully
- Do NOT skip "Bibliographical Notes" sections — they are critical
- Do NOT use `$$...$$` for display math — use proper LaTeX environments
