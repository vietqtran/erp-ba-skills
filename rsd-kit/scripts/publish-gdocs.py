"""Publish the RSD Word file to Google Docs and share it by link. Connection is picked by connect.py: API (OAuth) -> MCP -> manual.

    python3 rsd-kit/scripts/publish-gdocs.py <RSD dir> [--title "..."] [--share reader|commenter|writer|off]
                                             [--folder-id <id>] [--via auto|api|mcp|manual] [--new]

If already published (.gdocs.json exists) it only prints the existing link; add --new to create another copy.
Verification uses the HTML export of the public link (no Google Docs API needed).
"""
import argparse
import glob
import html
import json
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import connect  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument('dir')
ap.add_argument('--title')
ap.add_argument('--share', default='reader', choices=['reader', 'commenter', 'writer', 'off'])
ap.add_argument('--folder-id', default='root')
ap.add_argument('--via')
ap.add_argument('--new', action='store_true')
a = ap.parse_args()

D = os.path.abspath(a.dir)
DOCX = glob.glob(os.path.join(D, 'RSD-*.docx'))
if not DOCX:
    sys.exit('No .docx yet — run rsd-kit/scripts/export-docx.sh first')
DOCX = DOCX[0]
md = open(DOCX[:-5] + '.md', encoding='utf-8').read()
if not a.title:                                   # title from the document heading "## Quy trình BP-xx: <name>"
    m = re.search(r'^## Quy trình (BP-\d+): (.+)$', md, re.M)
    a.title = f'RSD {m.group(1)} - {m.group(2).strip()}' if m else os.path.basename(DOCX)[:-5]
STATE = os.path.join(D, '.gdocs.json')
if os.path.exists(STATE) and not a.new:
    sys.exit('Already published: ' + json.load(open(STATE))['url'] + '  (add --new to create another copy)')

cfg = connect.config()
if a.via:
    cfg['google']['via'] = a.via
g, how = connect.google(cfg)
print('Google connection:', how)
if not g:
    print(f'''
MANUAL UPLOAD (no Google OAuth or MCP on this machine — setup: rsd-kit/README.md, section "Connections"):
  1. Open https://drive.google.com -> New -> File upload -> choose {DOCX}
  2. Right-click the file -> Open with -> Google Docs (Drive creates a Google Docs copy, keeping images and tables).
  3. Rename it to "{a.title}"; Share -> General access -> "Anyone with the link" -> Viewer.''')
    sys.exit(0)

doc_id = g.import_docx(DOCX, a.title, a.folder_id)
url = f'https://docs.google.com/document/d/{doc_id}/edit?usp=drivesdk'
print('Created Google Doc:', url)
if a.share != 'off':
    g.share(doc_id, a.share)
    print('Shared: anyone with the link can', {'reader': 'view', 'commenter': 'comment', 'writer': 'edit'}[a.share])

result = {'docId': doc_id, 'url': url, 'share': a.share, 'via': g.via}
if a.share != 'off':
    try:
        page = urllib.request.urlopen(f'https://docs.google.com/document/d/{doc_id}/export?format=html', timeout=120).read().decode('utf-8', 'ignore')
        plain = html.unescape(re.sub(r'<[^>]+>', ' ', page))
        want = len(re.findall(r'!\[[^\]]*\]\(images/', md))
        last = re.findall(r'^## (.+)$', md, re.M)[-1]
        result['check'] = {'images': page.count('<img'), 'tables': page.count('<table'), 'last_section': last in plain}
        ok = result['check']['images'] >= want and result['check']['last_section']
        print(('OK' if ok else 'WARNING') + f" — images {result['check']['images']}/{want}, tables {result['check']['tables']}, "
              f"last section present: {result['check']['last_section']}")
    except Exception as e:
        print('Could not download the export to verify:', e)
json.dump(result, open(STATE, 'w'), ensure_ascii=False, indent=1)
print(url)
