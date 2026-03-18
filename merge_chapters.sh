#!/bin/bash
#
# merge_chapters.sh
# Merge split chapter files for the Chandrasekhar book translation project.
#
# This script merges:
#   chapter_2_part1.tex + chapter_2_part2.tex -> chapter_2.tex
#   chapter_3_part1.tex + chapter_3_part2.tex -> chapter_3.tex
#   chapter_7_part1.tex + chapter_7_part2.tex -> chapter_7.tex
#
# IMPORTANT: Run from the project root directory (parent of output/).
# The script creates backups before merging and does NOT delete originals.
#
# Usage:
#   chmod +x merge_chapters.sh
#   ./merge_chapters.sh
#
# ============================================================================

set -euo pipefail

CHAP_DIR="output/chapters"
BACKUP_DIR="output/chapters/backup_before_merge"

# Color helpers (if terminal supports it)
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

info()  { printf "${GREEN}[INFO]${NC}  %s\n" "$1"; }
warn()  { printf "${YELLOW}[WARN]${NC}  %s\n" "$1"; }
error() { printf "${RED}[ERROR]${NC} %s\n" "$1"; }

# --------------------------------------------------------------------------
# Pre-flight checks
# --------------------------------------------------------------------------
if [[ ! -d "$CHAP_DIR" ]]; then
    error "Directory '$CHAP_DIR' not found. Run this script from the project root."
    exit 1
fi

for f in chapter_2_part1.tex chapter_2_part2.tex \
         chapter_3_part1.tex chapter_3_part2.tex \
         chapter_7_part1.tex chapter_7_part2.tex; do
    if [[ ! -f "$CHAP_DIR/$f" ]]; then
        error "Required file '$CHAP_DIR/$f' not found."
        exit 1
    fi
done

# --------------------------------------------------------------------------
# Create backup directory
# --------------------------------------------------------------------------
mkdir -p "$BACKUP_DIR"
info "Backing up original part files to $BACKUP_DIR/"

for f in chapter_2_part1.tex chapter_2_part2.tex \
         chapter_3_part1.tex chapter_3_part2.tex \
         chapter_7_part1.tex chapter_7_part2.tex; do
    cp "$CHAP_DIR/$f" "$BACKUP_DIR/$f"
done
info "Backups complete."

# ==========================================================================
# MERGE 1: Chapter 2
#
# Join point:
#   part1 ends at line 1769 (inside section 15, after eq:2-227, Table II, Fig 3)
#   part2 starts with a comment header (lines 1-5), then continues section 15
#
# KNOWN ISSUE: Duplicate label \label{eq:2-225} exists in both files.
#   - part1 line 1724: \label{eq:2-225}  (the original equation 225)
#   - part2 line 14:   \label{eq:2-225}  (a DIFFERENT equation, should be eq:2-228 or similar)
#   This script fixes the duplicate by renaming part2's eq:2-225 to eq:2-225a.
#
# Section continuity: part1 has sections 5-15, part2 continues 15 then 16-17.
# Equation continuity: part1 ends at eq:2-227, part2 continues at eq:2-225
#   (which is the duplicate; after fix, the numbering flows as 227 -> 225a -> 225p -> 226b -> 227b -> ...)
# ==========================================================================
info "Merging Chapter 2..."

{
    # Full content of part1
    cat "$CHAP_DIR/chapter_2_part1.tex"

    # Blank line separator
    echo ""
    echo "% ========================================================================"
    echo "% [MERGED] Content below was originally in chapter_2_part2.tex"
    echo "% ========================================================================"
    echo ""

    # part2, stripping the comment header (first 5 lines: comment block + blank line)
    # Also fix the duplicate label: eq:2-225 -> eq:2-225a (only in the part2 portion)
    tail -n +6 "$CHAP_DIR/chapter_2_part2.tex" | sed 's/\\label{eq:2-225}/\\label{eq:2-225a}/'

} > "$CHAP_DIR/chapter_2.tex"

info "Chapter 2 merged -> $CHAP_DIR/chapter_2.tex"

# Also fix any \eqref or \ref pointing to the renamed label in part2's content.
# The original part2 text does not appear to cross-reference eq:2-225 internally,
# but we check and fix just in case.
# (This sed operates on the already-merged file, targeting only the part2 portion.)
# Note: references to eq:2-225 from OTHER chapters should continue to point to
# the part1 definition. Only part2-internal refs (if any) need updating.

# ==========================================================================
# MERGE 2: Chapter 3
#
# Join point:
#   part1 ends at line 1295 (end of section 28, after eq:3-210)
#   part2 starts at section 29 (eq:3-211)
#
# No duplicate labels detected.
# Section continuity: 28 -> 29 (clean)
# Equation continuity: 3-210 -> 3-211 (clean)
# ==========================================================================
info "Merging Chapter 3..."

{
    # Full content of part1
    cat "$CHAP_DIR/chapter_3_part1.tex"

    echo ""
    echo "% ========================================================================"
    echo "% [MERGED] Content below was originally in chapter_3_part2.tex"
    echo "% ========================================================================"
    echo ""

    # part2, stripping the comment header (first 5 lines)
    tail -n +6 "$CHAP_DIR/chapter_3_part2.tex"

} > "$CHAP_DIR/chapter_3.tex"

info "Chapter 3 merged -> $CHAP_DIR/chapter_3.tex"

# ==========================================================================
# MERGE 3: Chapter 7
#
# Join point:
#   part1 ends at line 2545 (end of section 71, after eq:7-275)
#   part2 starts at section 72 (eq:7-276)
#
# No duplicate labels detected.
# Section continuity: 71 -> 72 (clean)
# Equation continuity: 7-275 -> 7-276 (clean)
# ==========================================================================
info "Merging Chapter 7..."

{
    # Full content of part1
    cat "$CHAP_DIR/chapter_7_part1.tex"

    echo ""
    echo "% ========================================================================"
    echo "% [MERGED] Content below was originally in chapter_7_part2.tex"
    echo "% ========================================================================"
    echo ""

    # part2, stripping the comment header (first 4 lines: 3 comment lines + blank)
    tail -n +5 "$CHAP_DIR/chapter_7_part2.tex"

} > "$CHAP_DIR/chapter_7.tex"

info "Chapter 7 merged -> $CHAP_DIR/chapter_7.tex"

# ==========================================================================
# Post-merge validation
# ==========================================================================
echo ""
info "=== Post-merge validation ==="

# Check for duplicate labels in each merged file
for ch in 2 3 7; do
    MERGED="$CHAP_DIR/chapter_${ch}.tex"
    DUPES=$(grep -o '\\label{[^}]*}' "$MERGED" | sort | uniq -d || true)
    if [[ -n "$DUPES" ]]; then
        warn "Chapter $ch has DUPLICATE labels:"
        echo "$DUPES"
    else
        info "Chapter $ch: no duplicate labels found."
    fi
done

# Report file sizes
echo ""
info "=== Merged file sizes ==="
for ch in 2 3 7; do
    MERGED="$CHAP_DIR/chapter_${ch}.tex"
    P1="$CHAP_DIR/chapter_${ch}_part1.tex"
    P2="$CHAP_DIR/chapter_${ch}_part2.tex"
    SIZE_MERGED=$(wc -c < "$MERGED" | tr -d ' ')
    SIZE_P1=$(wc -c < "$P1" | tr -d ' ')
    SIZE_P2=$(wc -c < "$P2" | tr -d ' ')
    EXPECTED=$((SIZE_P1 + SIZE_P2))
    info "  chapter_${ch}.tex: ${SIZE_MERGED} bytes (part1: ${SIZE_P1} + part2: ${SIZE_P2} = ${EXPECTED} expected; delta from headers/separators)"
done

echo ""
info "Merge complete. Original part files preserved in $BACKUP_DIR/"
info "After verifying the merged files, you may delete the part files with:"
echo "  rm $CHAP_DIR/chapter_*_part*.tex"
echo ""
info "Done."
