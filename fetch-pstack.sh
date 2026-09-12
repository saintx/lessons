#!/usr/bin/env bash
# Pin: cursor/plugins @ 889ec4b68fa5aab0e867dad71ec3fdf386ae48f3 (pstack 0.15.2).
# Sparse-checkouts pstack/ then copies it to corpus/pstack/ so posts address
# corpus/pstack/README.md, not corpus/pstack/pstack/README.md.
set -euo pipefail

PIN=889ec4b68fa5aab0e867dad71ec3fdf386ae48f3
REPO=https://github.com/cursor/plugins.git
ROOT="$(cd "$(dirname "$0")" && pwd)"
SRC="${ROOT}/corpus/.pstack-src"
DEST="${ROOT}/corpus/pstack"

mkdir -p "${ROOT}/corpus"

head=""
if [ -d "${SRC}/.git" ]; then
  head="$(git -C "${SRC}" rev-parse HEAD 2>/dev/null || true)"
fi

if [ "$head" = "$PIN" ] && [ -f "${DEST}/README.md" ]; then
  echo "pstack already at ${PIN} -> ${DEST}"
  exit 0
fi

if [ -d "${SRC}/.git" ]; then
  git -C "${SRC}" fetch --depth 1 origin "${PIN}"
else
  git clone --filter=blob:none --sparse --no-checkout "${REPO}" "${SRC}"
  git -C "${SRC}" sparse-checkout set pstack
  git -C "${SRC}" fetch --depth 1 origin "${PIN}"
fi

git -C "${SRC}" -c advice.detachedHead=false checkout --detach "${PIN}"

if [ ! -d "${SRC}/pstack" ]; then
  echo "error: pstack directory missing at pin ${PIN}" >&2
  exit 1
fi

rm -rf "${DEST}"
cp -R "${SRC}/pstack" "${DEST}"
echo "pstack at ${PIN} -> ${DEST}"
