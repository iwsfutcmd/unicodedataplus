#!/bin/bash
# Script to generate unicodedata.c.h using CPython's Argument Clinic.
# Generates both unicodedata.3.12.c.h (from commit 41e844a) and unicodedata.c.h (from main).

CPYTHON_DIR="$1"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
UNICODEDATA_C="${SCRIPT_DIR}/unicodedataplus/unicodedata.c"
UNICODEDATA_312_C="${SCRIPT_DIR}/unicodedataplus/unicodedata.3.12.c"
CLINIC_PY="${CPYTHON_DIR}/Tools/clinic/clinic.py"

sed '/@permit_long_summary/d' "$UNICODEDATA_C" > "$UNICODEDATA_312_C" 

cd "$CPYTHON_DIR"
git checkout 41e844a

python3 "$CLINIC_PY" "$UNICODEDATA_312_C"

rm "$UNICODEDATA_312_C"

git checkout main

python3 "$CLINIC_PY" "$UNICODEDATA_C"
