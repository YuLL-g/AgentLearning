#!/bin/sh
set -eu

MYLS_BIN=$1
export MYLS_BIN

if [ ! -x "$MYLS_BIN" ]; then
    printf 'missing executable: %s\n' "$MYLS_BIN" >&2
    exit 1
fi

found=0
for case_file in "$(dirname "$0")"/cases/*.sh; do
    [ -f "$case_file" ] || continue
    found=1
    printf 'RUN %s\n' "${case_file##*/}"
    sh "$case_file"
done

if [ "$found" -eq 0 ]; then
    printf 'No behavioral tests yet; build smoke check passed.\n'
fi
