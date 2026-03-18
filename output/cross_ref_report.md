# Cross-Reference Verification Report

**Date:** 2026-03-17
**Scope:** `chapter_1.tex` through `chapter_14.tex`, `appendix_1.tex` through `appendix_5.tex`
**Excluded:** Backup files (`backup_before_merge/`), fragment files (`*_part1.tex`, `*_part2.tex`, `*_sec*.tex`)

---

## 1. Summary Statistics

| Metric | Count |
|---|---|
| Files analyzed | 19 |
| Total unique labels defined | 3,511 |
| Total unique references used | 2,817 |
| Total label instances | 3,511 |
| Total reference instances | 2,817 |
| **Undefined references (unique labels)** | **6** |
| **Undefined reference instances** | **10** |
| **Duplicate labels** | **0** |
| Unused labels (defined, never referenced) | 1,738 |

### Label Categories

| Category | Count |
|---|---|
| `eq:` (equations) | 3,258 |
| `sec:` (sections) | 178 |
| `tab:` (tables) | 57 |
| `ch:` (chapters) | 13 |
| `app:` (appendices) | 5 |

### Labels Per File

| File | Labels Defined | References Made |
|---|---|---|
| chapter_1.tex | 21 | 0 |
| chapter_2.tex | 356 | 220 |
| chapter_3.tex | 340 | 290 |
| chapter_4.tex | 283 | 245 |
| chapter_5.tex | 6 | 0 |
| chapter_6.tex | 289 | 203 |
| chapter_7.tex | 337 | 297 |
| chapter_8.tex | 232 | 167 |
| chapter_9.tex | 319 | 262 |
| chapter_10.tex | 322 | 310 |
| chapter_11.tex | 187 | 164 |
| chapter_12.tex | 388 | 344 |
| chapter_13.tex | 138 | 101 |
| chapter_14.tex | 61 | 60 |
| appendix_1.tex | 45 | 27 |
| appendix_2.tex | 33 | 31 |
| appendix_3.tex | 37 | 10 |
| appendix_4.tex | 55 | 56 |
| appendix_5.tex | 62 | 30 |

---

## 2. Undefined References (CRITICAL)

These are `\ref{}` / `\eqref{}` calls that point to labels that do not exist anywhere in the analyzed files. Each will produce a **"??"** in the compiled PDF.

### 2.1 `eq:10-243` -- Missing label in chapter_10.tex

- **Referenced at:** chapter_10.tex line 1601
- **Context:** `On the other hand, according to equation~\eqref{eq:10-243},`
- **Diagnosis:** Labels jump from `eq:10-242` (line 1524) directly to `eq:10-244` (line 1531). The label `eq:10-243` was never defined. This is a numbering gap -- an equation was likely omitted or misnumbered during transcription.

### 2.2 `eq:10-269` -- Missing label in chapter_10.tex

- **Referenced at:** chapter_10.tex lines 1727, 1896, 1918 (3 instances)
- **Context:** `Now eliminating Pi_0 between equations \eqref{eq:10-269} and \eqref{eq:10-278}`
- **Diagnosis:** Labels jump from `eq:10-268` (line 1674) directly to `eq:10-270` (line 1679). The label `eq:10-269` was never defined. An equation is missing between these two.

### 2.3 `eq:7-27a` -- Missing label in chapter_7.tex

- **Referenced at:** chapter_7.tex line 718
- **Context:** `(cf.\ equations~\eqref{eq:7-27a} and~\eqref{eq:7-28}).`
- **Diagnosis:** Label `eq:7-27` exists (line 256), but `eq:7-27a` does not. This appears to be a sub-equation label (like a part (a) of equation 27) that was either never created or was named differently.

### 2.4 `eq:9-188` -- Missing label in chapter_9.tex

- **Referenced at:** chapter_9.tex line 919
- **Context:** `whereas in the framework of the approximations underlying equation~\eqref{eq:9-188}`
- **Diagnosis:** Labels jump from `eq:9-187` (line 911) directly to `eq:9-189` (line 917). The label `eq:9-188` was never defined.

### 2.5 `eq:9-245` -- Missing label in chapter_9.tex

- **Referenced at:** chapter_9.tex lines 1240, 1258, 1335 (3 instances)
- **Context:** `the secular matrix can be brought to exactly the same form~\eqref{eq:9-245}`
- **Diagnosis:** Labels jump from `eq:9-241` / `eq:9-241a` (line 1205/1209) directly to `eq:9-249` (line 1214). Equations 242 through 248 are missing entirely. The label `eq:9-245` is referenced 3 times but never defined.

### 2.6 `eq:9-260` -- Missing label in chapter_9.tex

- **Referenced at:** chapter_9.tex line 1353
- **Context:** `must be evaluated in accordance with equations~\eqref{eq:9-250}, \eqref{eq:9-251}, and \eqref{eq:9-260}`
- **Diagnosis:** Labels jump from `eq:9-259` (line 1329) directly to `eq:9-262` (line 1337). Equations 260 and 261 are missing.

---

## 3. Duplicate Labels

**No duplicate labels were found** across the main chapter and appendix files. (Note: duplicate labels *do* exist in the fragment/part files like `chapter_2_part1.tex`, but these were excluded from analysis per instructions.)

---

## 4. Equation Numbering Continuity

This section documents gaps and sub-equation duplicates in the `eq:X-Y` numbering scheme within each chapter.

### 4.1 chapter_2.tex (Prefix `2`)
- **Total equations:** 328 labels for range 1..322
- **Sub-equation labels (causing numeric "duplicates"):**
  - `eq:2-225a` (line 1783) -- sub-part of eq 225
  - `eq:2-225p` (line 1790) -- sub-part of eq 225
  - `eq:2-226b` (line 1809) -- sub-part of eq 226
  - `eq:2-227b` (line 1870) -- sub-part of eq 227
  - `eq:2-242b` (line 1979) -- sub-part of eq 242
  - `eq:2-264b` (line 2127) -- sub-part of eq 264
- **Verdict:** No true gaps. The extra labels are sub-equations (a, b, p suffixes). Numbering is contiguous.

### 4.2 chapter_3.tex (Prefix `3`)
- **Total equations:** 311 labels for range 1..307
- **Sub-equation labels:**
  - `eq:3-168b` (line 979)
  - `eq:3-176b` (line 1031)
  - `eq:3-234` (line 1492) -- duplicate number
  - `eq:3-248` (line 1587) -- duplicate number
- **Verdict:** Two genuine duplicate equation numbers (`eq:3-234` appears twice, `eq:3-248` appears twice). These need investigation.

### 4.3 chapter_6.tex (Prefix `6`)
- **Total equations:** 256 labels for range 1..260
- **Gaps (4 missing numbers):**
  - **eq:6-24** is missing (jumps from eq:6-23 to eq:6-25)
  - **eq:6-82** is missing (jumps from eq:6-81 to eq:6-83)
  - **eq:6-110** is missing (jumps from eq:6-109 to eq:6-111)
  - **eq:6-116** is missing (jumps from eq:6-115 to eq:6-117)
- **Verdict:** 4 equations missing from the sequence. If these are intentional (e.g., equations displayed inline without labels), they may be acceptable. Otherwise, content is missing.

### 4.4 chapter_7.tex (Prefix `7`)
- **Total equations:** 320 labels for range 1..320
- **Sub-equation labels:**
  - `eq:7-207a` (line 2061) -- sub-part of eq 207
- **Gaps:**
  - **eq:7-208** is missing (jumps from eq:7-207 to eq:7-209 at line 1780)
- **Verdict:** One missing equation (eq:7-208). The sub-equation label `eq:7-207a` accounts for one extra.

### 4.5 chapter_8.tex (Prefix `8`)
- **Total equations:** 206 labels for range 1..197
- **Sub-equation labels (9 extras):**
  - `eq:8-6b` (line 44)
  - `eq:8-23b` (line 162)
  - `eq:8-23c` (line 166)
  - `eq:8-23d` (line 170)
  - `eq:8-25b` (line 188)
  - `eq:8-25c` (line 194)
  - `eq:8-34b` (line 285)
  - `eq:8-106b` (line 791)
  - `eq:8-132b` (line 952)
- **Verdict:** No gaps. The extra 9 labels are sub-equations with letter suffixes. Numbering is contiguous through 197.

### 4.6 chapter_9.tex (Prefix `9`)
- **Total equations:** 308 labels for range 1..312
- **Sub-equation labels:**
  - `eq:9-74a` (line 361)
  - `eq:9-92a` (line 443)
  - `eq:9-241a` (line 1209)
  - `eq:9-253a` (line 1238)
  - `eq:9-265a` (line 1363)
  - `eq:9-266b` (line 1375)
- **Gaps:**
  - **eq:9-188** is missing (jumps from eq:9-187 to eq:9-189) -- **also an undefined reference** (see Section 2.4)
  - **eq:9-242 through eq:9-248** are missing (jumps from eq:9-241 to eq:9-249) -- **eq:9-245 is also an undefined reference** (see Section 2.5)
  - **eq:9-260, eq:9-261** are missing (jumps from eq:9-259 to eq:9-262) -- **eq:9-260 is also an undefined reference** (see Section 2.6)
- **Verdict:** 10 equations missing from the sequence. Three of these are actively referenced, causing undefined reference errors.

### 4.7 chapter_10.tex (Prefix `10`)
- **Total equations:** 305 labels for range 1..306
- **Sub-equation labels:**
  - `eq:10-70a` (line 418)
- **Gaps:**
  - **eq:10-243** is missing (jumps from eq:10-242 to eq:10-244) -- **also an undefined reference** (see Section 2.1)
  - **eq:10-269** is missing (jumps from eq:10-268 to eq:10-270) -- **also an undefined reference** (see Section 2.2)
- **Verdict:** 2 equations missing, both actively referenced.

### 4.8 chapter_11.tex (Prefix `11`)
- **Total equations:** 178 labels for range 1..179
- **Gaps:**
  - **eq:11-67** is missing (jumps from eq:11-66 to eq:11-68)
- **Verdict:** 1 equation missing. Not referenced, so no undefined-reference error, but the gap may indicate missing content.

### 4.9 appendix_5.tex (Prefix `A5`)
- **Total equations:** 55 labels for range 1..53
- **Sub-equation labels:**
  - `eq:A5-36a` (line 305)
  - `eq:A5-36b` (line 310)
- **Verdict:** No gaps. The 2 extra labels are sub-equations. Numbering is contiguous through 53.

### 4.10 Files with No Issues
The following files have fully contiguous equation numbering with no gaps or anomalies:
- chapter_1.tex (eq:1-1 through eq:1-15)
- chapter_4.tex (eq:4-1 through eq:4-267)
- chapter_12.tex (eq:12-1 through eq:12-367)
- chapter_13.tex (eq:13-1 through eq:13-126)
- chapter_14.tex (eq:14-1 through eq:14-48)
- appendix_1.tex (eq:A1-1 through eq:A1-36)
- appendix_2.tex (eq:A2-1 through eq:A2-24)
- appendix_3.tex (eq:A3-1 through eq:A3-28)
- appendix_4.tex (eq:A4-1 through eq:A4-42)

---

## 5. Missing Chapter Labels

The following chapters lack a `\label{ch:X}` definition:
- **chapter_5.tex** -- no `\label{ch:5}` defined

Note: `chapter_5.tex` is a stub file (33 lines) with section headers but `% TODO` placeholders for content. It defines only 6 section labels and zero equations.

---

## 6. Unused Labels Summary

Labels that are defined but never referenced elsewhere. A high unused count is normal for section and chapter labels (which serve as navigation anchors) and for equations in introductory chapters.

| File | Unused / Total | % Unused |
|---|---|---|
| chapter_1.tex | 21 / 21 | 100% |
| chapter_2.tex | 221 / 356 | 62% |
| chapter_3.tex | 189 / 340 | 56% |
| chapter_4.tex | 136 / 283 | 48% |
| chapter_5.tex | 6 / 6 | 100% |
| chapter_6.tex | 178 / 289 | 62% |
| chapter_7.tex | 0 / 337 | 0% |
| chapter_8.tex | 131 / 232 | 56% |
| chapter_9.tex | 175 / 319 | 55% |
| chapter_10.tex | 145 / 322 | 45% |
| chapter_11.tex | 94 / 187 | 50% |
| chapter_12.tex | 195 / 388 | 50% |
| chapter_13.tex | 78 / 138 | 57% |
| chapter_14.tex | 33 / 61 | 54% |
| appendix_1.tex | 28 / 45 | 62% |
| appendix_2.tex | 16 / 33 | 48% |
| appendix_3.tex | 27 / 37 | 73% |
| appendix_4.tex | 27 / 55 | 49% |
| appendix_5.tex | 38 / 62 | 61% |

**Note:** chapter_1.tex (100% unused) and chapter_5.tex (100% unused) stand out. Chapter 1 has full content but no other chapter references its equations. Chapter 5 is a stub with no content.

---

## 7. Action Items (Priority Order)

### HIGH -- Undefined References (will show "??" in PDF)

1. **chapter_10.tex:** Add missing `\label{eq:10-243}` (or fix the reference at line 1601)
2. **chapter_10.tex:** Add missing `\label{eq:10-269}` (or fix references at lines 1727, 1896, 1918)
3. **chapter_9.tex:** Add missing `\label{eq:9-245}` and surrounding equations 242-248 (referenced at lines 1240, 1258, 1335)
4. **chapter_9.tex:** Add missing `\label{eq:9-188}` (referenced at line 919)
5. **chapter_9.tex:** Add missing `\label{eq:9-260}` (referenced at line 1353)
6. **chapter_7.tex:** Add missing `\label{eq:7-27a}` or change reference to `eq:7-27` (line 718)

### MEDIUM -- Equation Numbering Gaps (may indicate missing content)

7. **chapter_6.tex:** 4 gaps in equation numbering (eq:6-24, eq:6-82, eq:6-110, eq:6-116)
8. **chapter_7.tex:** 1 gap (eq:7-208)
9. **chapter_9.tex:** 10 total missing equations in numbering sequence
10. **chapter_11.tex:** 1 gap (eq:11-67)

### LOW -- Structural Issues

11. **chapter_5.tex:** Stub file with no content -- needs full transcription
12. **chapter_5.tex:** Missing `\label{ch:5}` chapter label
13. **chapter_3.tex:** Duplicate equation numbers for eq:3-234 and eq:3-248 (two definitions each with same numeric label)

---

*Report generated by automated cross-reference analysis of 19 .tex files containing 3,511 labels and 2,817 references.*
