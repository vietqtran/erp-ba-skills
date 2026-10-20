"""Self-check an RSD (business version) before export/publish. Prints errors (E) and warnings (W); exit code 1 if any error.

    python3 rsd-kit/scripts/check.py <RSD dir>

The RSD itself is written in Vietnamese, so the required headings and column names below are Vietnamese
(they must match templates/rsd-template.md exactly; confluence_page.py relies on them).
"""
import glob
import os
import re
import sys

D = sys.argv[1]
MD = glob.glob(os.path.join(D, 'RSD-*.md'))
if len(MD) != 1:
    sys.exit(f'E: expected exactly one RSD-*.md in {D}')
s = open(MD[0], encoding='utf-8').read()
L = s.split('\n')
errs, warns = [], []

# 1. Required frame
for h in ['## 1. Mô tả chung', '## 2. Mô tả các bước thực hiện', '## 3. Input / Output', '## 4. Phân quyền thực hiện',
          '## 5. Tham số hệ thống', '## 6. Flow Diagrams', '## 7. Kiểm soát nội bộ', '## 8. Yêu cầu phi chức năng',
          '## 9. Tiêu chí nghiệm thu', '## 10. Câu hỏi cần doanh nghiệp xác nhận', '## 11. Tài liệu tham khảo',
          '### 2.3 Mô tả chi tiết từng bước', '## Cách đọc tài liệu']:
    if not any(l.startswith(h) for l in L):
        errs.append(f'missing heading "{h}" (exact text as in the template)')
if not re.search(r'^\| Version \| Lý do \| Date \| Người sửa \| Mô tả \|', s, re.M):
    errs.append('missing version table "| Version | Lý do | Date | Người sửa | Mô tả |"')
sec1 = s.split('## 1. Mô tả chung', 1)[-1].split('### 1.1', 1)[0]
for row in ['Tên', 'Mã', 'Mô tả', 'Tác nhân', 'Mức độ ưu tiên', 'Điều kiện kích hoạt']:
    if not re.search(rf'^\| {row} \|', sec1, re.M):
        errs.append(f'use-case table (top of section 1) is missing row "{row}"')

# 2. Reference codes: every code used must be defined (first cell of a table row)
CODE = r'(?:QT|TS|KS|TN|BC|NT|CH)-\d+'
defs = set(re.findall(rf'^\|\s*({CODE})\s*\|', s, re.M))
for c in sorted(set(re.findall(rf'\b({CODE})\b', s)) - defs):
    errs.append(f'code {c} is referenced but never defined')
for d in sorted(x for x in defs if x.startswith('CH') and len(re.findall(rf'\b{x}\b', s)) < 2):
    warns.append(f'question {d} is not referenced anywhere in the document')

# 3. Images
imgs = re.findall(r'!\[[^\]]*\]\((images/[^)]+)\)', s)
for p in imgs:
    if not os.path.exists(os.path.join(D, p)):
        errs.append(f'missing image {p} (run render-diagrams.sh)')
for f in glob.glob(os.path.join(D, 'diagrams', '*.mmd')):
    if 'images/' + os.path.basename(f)[:-4] + '.png' not in imgs:
        warns.append(f'diagram {os.path.basename(f)} is not used in the document')
if len(imgs) < 6:
    warns.append(f'section 6 has only {len(imgs)} figures (the sample has 11)')

# 4. No technical leftovers (readers are business users)
TECH = [(r'`[^`]+`', 'code in backticks'), (r'(?<![\w/])\.\./|/Users/|\.md\b|\.py\b', 'file path / file name'),
        (r'\b[a-z]+_[a-z_]+\b', 'technical field name (snake_case)'),
        (r'\b(DRAFT|PENDING|APPROVED|POSTED|REJECTED|CANCELLED|IN_PROGRESS|REVERSED|RETURNED)\b', 'English status code'),
        (r'\b(BR|PRM|MSG|ROLE|SOD|FR|NFR|FN|DOC|NTF|INT)-[A-Z0-9]', 'technical ID scheme'),
        (r'\b(TODO|TBD)\b|\?\?\?|\{\{', 'unfinished text / template placeholder')]
for i, l in enumerate(L, 1):
    if l.startswith('!['):
        continue
    for pat, why in TECH:
        m = re.search(pat, l)
        if m:
            errs.append(f'line {i}: {why}: "{m.group(0)}"')

# 5. Tables have a consistent column count; lists need a blank line before them (pandoc)
hdr = None
for i, l in enumerate(L, 1):
    if l.startswith('|'):
        n = len(l.strip().strip('|').split('|'))
        if hdr is None:
            hdr = n
        elif n != hdr:
            errs.append(f'line {i}: table row has {n} columns, header has {hdr}')
    else:
        hdr = None
    if re.match(r'^(- |\d+\. )', l) and i > 1 and L[i - 2].strip() and not re.match(r'^\s*(- |\d+\. )', L[i - 2]):
        errs.append(f'line {i}: a list needs a blank line before it')

# 6. ERP standard grounded in the books (books/TOPICS.md): notes file, section 7 sources, section 11 citations
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
BOOKS = {'Wallace': 'wallace-erp-implementation', 'Elbardan': 'elbardan-erp-governance-audit',
         'Parthasarathy': 'parthasarathy-erp-fundamentals', "O'Leary": 'oleary-erp-systems-lifecycle'}
BOOK_RE = "|".join(re.escape(b) for b in BOOKS)


def chapter(book, n):
    return glob.glob(os.path.join(REPO, 'books', BOOKS[book], 'chapters', f'ch{int(n):02d}-*.md'))


for b, n in set(re.findall(rf"({BOOK_RE})[^|\n]{{0,30}}?\bch(\d+)", s)):
    if not chapter(b, n):
        errs.append(f'cites {b} ch{n}, but that chapter does not exist in books/')
sec7 = s.split('## 7. ', 1)[-1].split('## 8. ', 1)[0]
head7 = next((l for l in sec7.split('\n') if l.startswith('| Mã |')), '')
if 'Căn cứ' not in head7:
    errs.append('section 7 table needs a "Căn cứ" column (book chapter behind each control)')
else:
    col = [c.strip() for c in head7.strip('|').split('|')].index('Căn cứ')
    rows7 = [[c.strip() for c in l.strip().strip('|').split('|')] for l in sec7.split('\n') if re.match(r'^\| KS-\d+ \|', l)]
    for r in rows7:
        if len(r) <= col or not r[col]:
            errs.append(f'{r[0]}: empty "Căn cứ"')
    with_book = [r for r in rows7 if len(r) > col and re.search(BOOK_RE, r[col])]
    if rows7 and len(with_book) * 2 < len(rows7):
        errs.append(f'only {len(with_book)}/{len(rows7)} controls in section 7 cite a book chapter (need at least half)')
sec11 = s.split('## 11. ', 1)[-1]
cited = set()
for l in sec11.split('\n'):
    m = re.match(rf'^\| ({BOOK_RE})', l)
    if m:
        cited.add(m.group(1))
        for grp in re.findall(r'Ch\. (\d+(?:, \d+)*)', l):
            for n in grp.split(', '):
                if not chapter(m.group(1), n):
                    errs.append(f'section 11 cites {m.group(1)} Ch. {n}, which does not exist in books/')
if len(cited) < 3:
    errs.append(f'section 11 cites {len(cited)} of the 4 books (need at least 3)')
notes = os.path.join(D, 'book-notes.md')
if not os.path.exists(notes):
    errs.append('missing book-notes.md (templates/book-notes.md): the ERP standard taken from the books')
else:
    nrows = [l for l in open(notes, encoding='utf-8').read().split('\n') if re.match(r'^\| \d+ \|', l)]
    paths = [re.search(r'books/[\w-]+/chapters/ch\d+-[\w-]+\.md', l) for l in nrows]
    for l, p in zip(nrows, paths):
        if not p or not os.path.exists(os.path.join(REPO, p.group(0))):
            errs.append(f'book-notes.md row {l.split("|")[1].strip()}: source must be an existing books/<book>/chapters/chNN-*.md file')
    nbooks = {p.group(0).split('/')[1] for p in paths if p}
    if len(nrows) < 8 or len(nbooks) < 3:
        errs.append(f'book-notes.md has {len(nrows)} rows from {len(nbooks)} books (need ≥ 8 rows from ≥ 3 books)')
    ntext = open(notes, encoding='utf-8').read()
    short_sec = ntext.split('## Shortlist', 1)[1].split('\n## ', 1)[0] if '## Shortlist' in ntext else ''
    short = set(re.findall(rf'^\| ({BOOK_RE}) (ch\d+) \|', short_sec, re.M))
    used = set(re.findall(rf'\| ({BOOK_RE}) (ch\d+) — books/', ntext))
    if not short:
        errs.append('book-notes.md needs a "## Shortlist" table of chosen chapters (tiered reading: index → shortlist → chapters)')
    elif len(short) > 15:
        errs.append(f'book-notes.md shortlist has {len(short)} chapters (at most 15; read less, choose better from the index)')
    for b, n in sorted(used - short) if short else []:
        errs.append(f'book-notes.md cites {b} {n}, which is not in the shortlist')

for e in errs:
    print('E', e)
for w in warns:
    print('W', w)
print(('OK' if not errs else f'{len(errs)} errors') + f' — {os.path.basename(MD[0])}: {len(defs)} codes, {len(imgs)} figures, '
      f'{len(cited)} books cited')
sys.exit(1 if errs else 0)
