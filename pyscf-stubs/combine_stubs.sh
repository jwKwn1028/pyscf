#!/usr/bin/env bash
#
# combine_stubs.sh - drop per-subpackage stub folders from Colab runs into this repo.
#
# A Colab run of `gen_pyscf_stubs.py --only <sp...>` produces a zip in which only
# the *selected* subpackage folders (`pyscf-stubs/pyscf/<sp>/`) carry real merged
# types; every other module is an untouched all-`Incomplete` stubgen skeleton. So
# combining runs is just: for each typed folder in a zip, replace this repo's
# `pyscf/<sp>/` with it.
#
# Which folders are "typed" is auto-detected: a merged folder has function
# signatures with return annotations (`def ... -> ...`), whereas a pure stubgen
# skeleton has none. This handles both single- and multi-subpackage bundles, so
# the zip's filename doesn't matter. Use -s to state the list explicitly instead.
#
# Usage:
#   ./combine_stubs.sh bundle.zip                 # auto-detect every typed folder
#   ./combine_stubs.sh gto.zip scf.zip cc.zip     # many zips, each auto-detected
#   ./combine_stubs.sh /path/to/zips/*.zip        # glob
#   ./combine_stubs.sh -n *.zip                   # dry run (show, change nothing)
#   ./combine_stubs.sh -s "gto scf ao2mo" b.zip   # explicit list, skip detection
#   ./combine_stubs.sh -t /other/repo *.zip       # target a different repo root
#
# Options:
#   -n          dry run: report what would change, write nothing
#   -s "LIST"   space-separated subpackages to copy from each zip (overrides
#               auto-detection; errors if a named folder is missing from a zip)
#   -t DIR      target repo root (must contain pyscf/); default: this script's dir
#   -h          show this help
#
set -euo pipefail

SELF_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_ROOT="$SELF_DIR"
DRY_RUN=0
EXPLICIT=""

usage() { sed -n '2,/^set -euo/p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//; /^set -euo/d'; }

while getopts ":ns:t:h" opt; do
  case "$opt" in
    n) DRY_RUN=1 ;;
    s) EXPLICIT="$OPTARG" ;;
    t) TARGET_ROOT="$(cd "$OPTARG" && pwd)" ;;
    h) usage; exit 0 ;;
    \?) echo "unknown option -$OPTARG" >&2; exit 2 ;;
    :)  echo "option -$OPTARG needs an argument" >&2; exit 2 ;;
  esac
done
shift $((OPTIND - 1))

[[ $# -eq 0 ]] && { usage; exit 2; }

TARGET_PKG="$TARGET_ROOT/pyscf"
if [[ ! -d "$TARGET_PKG" ]]; then
  echo "error: no pyscf/ under target root: $TARGET_ROOT" >&2
  echo "       pass -t <repo-root> pointing at the stub repo." >&2
  exit 1
fi
command -v unzip >/dev/null || { echo "error: unzip not found on PATH" >&2; exit 1; }

# Shallowest directory named `pyscf` in an extracted zip = the package root.
# One awk pass (no sort|head) so nothing SIGPIPEs under `set -o pipefail`.
locate_pkg_dir() {
  find "$1" -type d -name pyscf 2>/dev/null | awk '
    { d = gsub(/\//, "/"); if (best == "" || d < bestd) { bestd = d; best = $0 } }
    END { if (best != "") print best }'
}

# Count `def ... -> ...` signatures under a folder (0 => pure skeleton). grep
# exits non-zero on zero matches, so guard it or `set -e`+pipefail would abort.
arrow_count() {
  local n
  n=$( { grep -rhE 'def .*->' "$1" --include='*.pyi' 2>/dev/null || true; } | wc -l )
  echo "${n//[[:space:]]/}"
}

overlay() {  # <src-folder> <sp> <arrows>
  local src="$1" sp="$2" arrows="$3" dst="$TARGET_PKG/$2"
  local n_pyi; n_pyi="$(find "$src" -name '*.pyi' | wc -l | tr -d ' ')"
  if [[ $DRY_RUN -eq 1 ]]; then
    echo "    would replace pyscf/$sp/  ($n_pyi .pyi, $arrows typed sigs)"
  else
    rm -rf "$dst"; cp -r "$src" "$dst"
    echo "    updated  pyscf/$sp/  ($n_pyi .pyi, $arrows typed sigs)"
  fi
}

TMP_ROOT="$(mktemp -d)"; trap 'rm -rf "$TMP_ROOT"' EXIT

ok=0; skip=0
for zip in "$@"; do
  echo "== $zip =="
  if [[ ! -f "$zip" ]]; then echo "  SKIP: not a file"; skip=$((skip+1)); continue; fi

  tmp="$TMP_ROOT/$(basename "$zip").d"; mkdir -p "$tmp"
  unzip -q -o "$zip" -d "$tmp"
  pkg="$(locate_pkg_dir "$tmp")"
  if [[ -z "$pkg" ]]; then echo "  SKIP: no pyscf/ package dir inside"; skip=$((skip+1)); continue; fi

  copied_any=0
  if [[ -n "$EXPLICIT" ]]; then
    # Explicit list: copy exactly what was named (validate each exists & is typed).
    for sp in $EXPLICIT; do
      src="$pkg/$sp"
      if [[ ! -d "$src" ]]; then echo "  MISS pyscf/$sp/ not in zip"; skip=$((skip+1)); continue; fi
      a="$(arrow_count "$src")"
      [[ "$a" -eq 0 ]] && echo "  warn pyscf/$sp/ looks like a skeleton (0 typed sigs) - copying anyway"
      overlay "$src" "$sp" "$a"; ok=$((ok+1)); copied_any=1
    done
  else
    # Auto-detect: every immediate subpackage folder that carries merged types.
    for src in "$pkg"/*/; do
      [[ -d "$src" ]] || continue
      sp="$(basename "$src")"
      a="$(arrow_count "$src")"
      [[ "$a" -eq 0 ]] && continue          # pure skeleton -> not selected in this run
      overlay "$src" "$sp" "$a"; ok=$((ok+1)); copied_any=1
    done
  fi

  if [[ $copied_any -eq 0 ]]; then
    echo "  SKIP: no typed folders detected (use -s \"<sp...>\" to force)"
    skip=$((skip+1))
  fi
done

echo
if [[ $DRY_RUN -eq 1 ]]; then
  echo "dry run: $ok folder(s) would change, $skip zip(s)/folder(s) skipped (nothing written)"
else
  echo "done: $ok folder(s) updated, $skip skipped"
  echo "review with: git -C \"$TARGET_ROOT\" status && git -C \"$TARGET_ROOT\" diff --stat"
fi
