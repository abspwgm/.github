#!/usr/bin/env bash
# Vendor the organization-facing brand assets out of absolute-power-brand.
#
# absolute-power-brand is the source of truth and is private; this repository is
# public because GitHub requires it to be for default community health files and
# the profile page to work. So the org-facing assets are vendored here rather
# than referenced, exactly as absolute-power-tcg vendors the generated Flutter
# tokens. Never edit brand/ by hand — change the source and re-run this.
#
# Usage:  bash scripts/sync-brand-assets.sh
#         BRAND_REPO=/path/to/absolute-power-brand bash scripts/sync-brand-assets.sh
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BRAND_REPO="${BRAND_REPO:-$(cd "$ROOT/../absolute-power-brand" 2>/dev/null && pwd || true)}"

if [ -z "${BRAND_REPO:-}" ] || [ ! -d "$BRAND_REPO" ]; then
  echo "error: absolute-power-brand not found. Set BRAND_REPO=/path/to/absolute-power-brand" >&2
  exit 1
fi

mkdir -p "$ROOT/brand"
for asset in ap-org-avatar.svg ap-social-preview.svg ap-gameservers-lockup.svg ap-tcgaming-lockup.svg; do
  src="$BRAND_REPO/logos/$asset"
  [ -f "$src" ] || { echo "error: missing $src" >&2; exit 1; }
  {
    echo "<!-- VENDORED — do not edit by hand."
    echo "     Source of truth: absolute-power-brand/logos/$asset"
    echo "     Resync: bash scripts/sync-brand-assets.sh -->"
    cat "$src"
  } > "$ROOT/brand/$asset"
  echo "  brand/$asset"
done
echo "done."
