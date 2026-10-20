"""Publish the RSD to Confluence in the BA team's RSD frame. Connection is picked by connect.py: API token -> MCP -> manual.

    python3 rsd-kit/scripts/publish-confluence.py <RSD dir> [--space <key|id>] [--parent <page id>] [--title "..."]
                                                  [--page-id <id>] [--via auto|api|mcp|manual] [--dry-run]

If the space already has a page with the same title, that page is updated; otherwise a new page is created
(under the space homepage or --parent). Uploads images/*.png as attachments, builds the page, updates it, then reads it back
to verify. Result saved to <RSD dir>/.confluence.json. --space defaults to confluence.space in ~/.config/rsd-kit/config.json.
"""
import argparse
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import connect                                             # noqa: E402
from confluence_page import ADF, Storage, build, stats     # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument('dir')
ap.add_argument('--space')
ap.add_argument('--parent')
ap.add_argument('--title')
ap.add_argument('--page-id')
ap.add_argument('--via')
ap.add_argument('--dry-run', action='store_true')
a = ap.parse_args()

D = os.path.abspath(a.dir)
MD = glob.glob(os.path.join(D, 'RSD-*.md'))[0]
md = open(MD, encoding='utf-8').read()
if not a.title:                                   # title from the document heading "## Quy trình BP-xx: <name>"
    m = re.search(r'^## Quy trình (BP-\d+): (.+)$', md, re.M)
    a.title = f'RSD {m.group(1)} – {m.group(2).strip()}' if m else os.path.basename(MD)[:-3]
images = sorted(set(re.findall(r'\]\(images/([^)]+\.png)\)', md)))

cfg = connect.config()
if a.via:
    cfg['confluence']['via'] = a.via
a.space = a.space or cfg['confluence'].get('space')
c, how = connect.confluence(cfg)
print('Confluence connection:', how)
docx = MD[:-3] + '.docx'
if not c:
    print(f'''
MANUAL UPLOAD (no Atlassian API token or MCP on this machine — setup: rsd-kit/README.md, section "Connections"):
  1. Open the space in Confluence -> "+" -> Import -> Word document (or on a new page: ••• -> Import -> Word).
  2. Choose: {docx if os.path.exists(docx) else docx + "  (run rsd-kit/scripts/export-docx.sh first)"}
  3. Title: {a.title}
  Note: a Word import keeps text, tables and images, but not the lozenges, expand blocks and table of contents of the team frame.''')
    sys.exit(0)
if not a.space:
    sys.exit('Missing --space (or confluence.space in the config)')

space = c.space(a.space)
if not space:
    sys.exit(f'Space "{a.space}" not found (check the key and your account permissions)')
if space['instructions']:
    print('NOTE — this space has authoring instructions; review them before publishing:\n', space['instructions'])
print(f"Space {space['key']} ({space['name']}) · title: {a.title} · {len(images)} images")
dialect = Storage() if c.dialect == 'storage' else ADF()

if a.dry_run:
    out = os.path.join(D, '.confluence-preview.html')
    open(out, 'w', encoding='utf-8').write(build(MD, dialect))
    print(f'DRY RUN — nothing written to Confluence. Preview: {out}')
    sys.exit(0)

pid = a.page_id or c.find_page(space, a.title)
if pid:
    print(f'Page with the same title exists ({pid}) — updating it')
else:
    pid = c.create_page(space, a.parent, a.title, build(MD, dialect))
    print(f'Created page {pid}')

refs = {name: c.upload(pid, os.path.join(D, 'images', name)) for name in images}
print(f'Uploaded {len(refs)} images')
if c.dialect == 'adf':
    dialect = ADF(refs, pid)
body = build(MD, dialect)
c.update_page(pid, body, 'Updated by rsd-kit')

want, got = stats(body, c.dialect), stats(c.read_body(pid), c.dialect)
bad = {k: (got[k], want[k]) for k in want if got[k] < want[k]}
url = c.url(pid)
json.dump({'pageId': pid, 'url': url, 'space': space['key'], 'via': c.via}, open(os.path.join(D, '.confluence.json'), 'w'), ensure_ascii=False, indent=1)
print(('OK' if not bad else f'WARNING missing after save: {bad}') + ' — ' + ', '.join(f'{k} {got[k]}/{want[k]}' for k in want))
print(url)
