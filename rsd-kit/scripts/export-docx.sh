#!/usr/bin/env bash
# Export the RSD Markdown to Word (.docx) with embedded images — for Google Docs / Confluence upload or sending to the customer.
#   rsd-kit/scripts/export-docx.sh <RSD dir>      (directory with exactly one RSD-*.md and images/)
# Requires pandoc (macOS: brew install pandoc).
set -euo pipefail
KIT="$(cd "$(dirname "$0")/.." && pwd)"
D="$(cd "${1:?missing RSD directory}" && pwd)"
command -v pandoc >/dev/null || { echo "pandoc is missing — install: brew install pandoc"; exit 1; }
MD="$(ls "$D"/RSD-*.md | head -1)"
TMP="$(mktemp -d)"
python3 - "$MD" "$TMP/in.md" "$D" <<'PY'
import os, re, struct, sys
src, out, d = sys.argv[1:4]
s = open(src, encoding='utf-8').read()
def att(m):
    p = os.path.join(d, m.group(2))
    with open(p, 'rb') as f:
        w, h = struct.unpack('>II', f.read(24)[16:24])
    return f'![{m.group(1)}]({p})' + ('{height=21cm}' if h / w > 1.25 else '{width=16cm}')
s = re.sub(r'!\[([^\]]*)\]\((images/[^)]+)\)', att, s)
s = re.sub(r'^---\s*$', '', s, flags=re.M)          # drop horizontal rules
open(out, 'w', encoding='utf-8').write(s)
PY
pandoc "$TMP/in.md" -f markdown-implicit_figures --columns=10000 --reference-doc="$KIT/templates/word-reference.docx" -o "$TMP/raw.docx"
python3 "$KIT/scripts/docx_style.py" "$TMP/raw.docx" "${MD%.md}.docx"
echo "OK — ${MD%.md}.docx"
