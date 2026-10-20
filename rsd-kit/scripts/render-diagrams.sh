#!/usr/bin/env bash
# Render every Mermaid diagram <RSD dir>/diagrams/*.mmd to <RSD dir>/images/*.png
#   rsd-kit/scripts/render-diagrams.sh <RSD dir>
# First run installs mermaid-cli into ~/.cache/erp-ba-mermaid (no Chromium download; uses the installed Chrome/Edge).
set -euo pipefail
KIT="$(cd "$(dirname "$0")/.." && pwd)"
D="$(cd "${1:?missing RSD directory}" && pwd)"
CACHE="$HOME/.cache/erp-ba-mermaid"
if [ ! -x "$CACHE/node_modules/.bin/mmdc" ]; then
  mkdir -p "$CACHE" && (cd "$CACHE" && { [ -f package.json ] || npm init -y >/dev/null; } \
    && PUPPETEER_SKIP_DOWNLOAD=true npm install --no-fund --no-audit @mermaid-js/mermaid-cli >/dev/null)
fi
CHROME="${CHROME_PATH:-}"
for c in "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge" \
         /usr/bin/google-chrome /usr/bin/google-chrome-stable /usr/bin/chromium /usr/bin/chromium-browser; do
  [ -z "$CHROME" ] && [ -x "$c" ] && CHROME="$c"
done
[ -n "$CHROME" ] || { echo "Chrome/Edge not found — set CHROME_PATH"; exit 1; }
TMP="$(mktemp -d)"
printf '{"executablePath":"%s","args":["--no-sandbox"]}' "$CHROME" > "$TMP/puppeteer.json"
mkdir -p "$D/images"
n=0
for f in "$D"/diagrams/*.mmd; do
  "$CACHE/node_modules/.bin/mmdc" -i "$f" -o "$D/images/$(basename "${f%.mmd}").png" \
    -c "$KIT/templates/diagrams/config.json" -p "$TMP/puppeteer.json" -s 2 -b white -q
  n=$((n + 1))
done
echo "OK — rendered $n diagrams into $D/images/"
