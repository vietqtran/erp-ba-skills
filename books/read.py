"""Read the ERP books in tiers, to keep context small.

    python3 books/read.py index                     # tier 1: chapter index (one line per chapter) of all four books
    python3 books/read.py W ch09                    # tier 3: core idea, key takeaways, BA application of one chapter
    python3 books/read.py W ch09 --add "Khái niệm chính,Bảng tham chiếu"   # plus extra sections when a rule needs them
    python3 books/read.py W ch09 --full             # whole chapter (only when really needed)

Books: P Parthasarathy · W Wallace & Kremzar · O O'Leary · E Elbardan & Kholeif. Tier 2 (choosing chapters) uses books/TOPICS.md.
Chapter files are Vietnamese summaries with the same sections; section names below are the Vietnamese headings.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
BOOKS = {'P': 'parthasarathy-erp-fundamentals', 'W': 'wallace-erp-implementation',
         'O': 'oleary-erp-systems-lifecycle', 'E': 'elbardan-erp-governance-audit'}
DEFAULT = ['Ý tưởng cốt lõi', 'Điểm cần nhớ', 'Ứng dụng cho BA ERP']


def index():
    for code, folder in BOOKS.items():
        readme = open(os.path.join(ROOT, folder, 'README.md'), encoding='utf-8').read()
        title = re.search(r'^# (.+)$', readme, re.M).group(1)
        print(f'## {code} — {title}')
        table = readme.split('## Chapter Index', 1)[1].split('\n## ', 1)[0]
        for row in re.findall(r'^\|.*\|$', table, re.M):
            cells = [c.strip() for c in row.strip('|').split('|')]
            if cells[0] in ('#', '') or set(cells[0]) <= set('-: '):
                continue
            num = re.sub(r'\[(ch\d+)\]\([^)]*\)', r'\1', cells[0])
            print(f'{num} | ' + ' | '.join(cells[1:]))
        print()


def chapter(code, ch, add=(), full=False):
    files = glob.glob(os.path.join(ROOT, BOOKS[code.upper()], 'chapters', f'{ch}-*.md'))
    if not files:
        sys.exit(f'No chapter {ch} in {BOOKS[code.upper()]}')
    text = open(files[0], encoding='utf-8').read()
    print(f'[{os.path.relpath(files[0], os.path.dirname(ROOT))}]')
    if full:
        print(text)
        return
    print(text.split('\n', 1)[0])
    want = DEFAULT + [a.strip() for a in add if a.strip()]
    for part in re.split(r'\n(?=## )', text)[1:]:
        name = re.sub(r'\s*\(.*', '', part.split('\n', 1)[0][3:]).strip()
        if name in want:
            print('\n' + part.strip())


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] == 'index':
        index()
    else:
        extra = a[a.index('--add') + 1].split(',') if '--add' in a else ()
        chapter(a[0], a[1], extra, '--full' in a)
