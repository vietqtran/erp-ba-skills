"""Turn an RSD Markdown file (following templates/rsd-template.md) into a Confluence page in the BA team's RSD frame.

Two output dialects:
- "adf"     : HTML accepted by the Atlassian Rovo MCP (data-type=..., images referenced by media id).
- "storage" : Confluence storage format for the REST API (ac: macros, images referenced by attachment file name).

Frame (references/confluence-format.md): version table + document info + auto table of contents; use-case table with a grey
label column; coloured status lozenges; expand blocks for step details / rule groups / error table / examples; colour-coded
permission matrix; status column for open questions; portrait figures paired in two columns.
Strings inserted into the page ("Mục lục", "ĐANG MỞ", ...) are Vietnamese on purpose: they are part of the document.

    python3 confluence_page.py <RSD.md> [--dialect adf|storage] [--files files.json --page-id ID] > page.html
files.json (adf only): {"h01-....png": "<fileId>"}. Storage needs nothing (images point to the attachment file name).
"""
import argparse
import html as H
import json
import os
import re
import struct
import subprocess
import sys

GRAY, GREEN, BLUE, YELLOW = '#F4F5F7', '#E3FCEF', '#DEEBFF', '#FFFAE6'
MARKED = """
const { createRequire } = require('module');
const r = createRequire(process.env.HOME + '/.cache/erp-ba-mermaid/node_modules/noop.js');
const { marked } = r('marked');
process.stdout.write(marked.parse(require('fs').readFileSync(process.argv[1], 'utf8')));
"""


class ADF:
    name = 'adf'

    def __init__(self, files=None, page_id=''):
        self.files, self.page_id = files or {}, page_id

    def lozenge(self, label, color):
        return f'<span data-type="status" data-color="{color}">{label}</span>'

    def panel(self, kind, inner):
        return f'<div data-type="panel-{kind}">{inner}</div>'

    def expand(self, title, inner):
        return f'<details><summary>{H.escape(title, quote=False)}</summary>{inner}</details>'

    def toc(self):
        return ('<div data-type="extension" data-extension-key="toc" data-extension-type="com.atlassian.confluence.macro.core" '
                'data-layout="default" data-parameters=\'{"macroParams":{"maxLevel":{"value":"2"},"style":{"value":"none"}},'
                '"macroMetadata":{"schemaVersion":{"value":"1"},"title":"Table of Contents"}}\'>Table of Contents</div>')

    def two_columns(self, a, b):
        return f'<section data-type="layout-two-equal"><div data-type="column">{a}</div><div data-type="column">{b}</div></section>'

    def image(self, filename, alt, pct):
        fid = self.files.get(filename)
        if not fid:
            return '<p>Hình đang được tải lên.</p>'
        return (f'<figure data-type="media-single" data-layout="center" data-width="{pct}" data-width-type="percentage">'
                f'<div data-type="media" data-media-type="file" data-id="{fid}" data-collection="contentId-{self.page_id}" '
                f'data-alt="{H.escape(alt)}"></div></figure>')

    def bg(self, tag, color):
        return f'<{tag} data-background="{color}">'


class Storage(ADF):
    name = 'storage'
    COLOUR = {'neutral': 'Grey', 'red': 'Red', 'yellow': 'Yellow', 'green': 'Green', 'blue': 'Blue', 'purple': 'Purple'}
    PANEL = {'info': 'info', 'warning': 'note', 'note': 'info'}

    @staticmethod
    def _macro(name, params, body=None):
        p = ''.join(f'<ac:parameter ac:name="{k}">{v}</ac:parameter>' for k, v in params.items())
        b = f'<ac:rich-text-body>{body}</ac:rich-text-body>' if body is not None else ''
        return f'<ac:structured-macro ac:name="{name}">{p}{b}</ac:structured-macro>'

    def lozenge(self, label, color):
        return self._macro('status', {'colour': self.COLOUR[color], 'title': label})

    def panel(self, kind, inner):
        return self._macro(self.PANEL[kind], {}, inner)

    def expand(self, title, inner):
        return self._macro('expand', {'title': H.escape(title, quote=False)}, inner)

    def toc(self):
        return self._macro('toc', {'maxLevel': '2'})

    def two_columns(self, a, b):           # 2-cell table: works in both the legacy and the new editor
        return f'<table data-layout="wide"><tbody><tr><td>{a}</td><td>{b}</td></tr></tbody></table>'

    def image(self, filename, alt, pct):
        return (f'<p><ac:image ac:align="center" ac:width="{int(760 * pct / 100)}" ac:alt="{H.escape(alt)}">'
                f'<ri:attachment ri:filename="{H.escape(filename)}"/></ac:image></p>')

    def bg(self, tag, color):
        return f'<{tag} data-highlight-colour="{color.lower()}">'


def text(s):
    return re.sub(r'\s+', ' ', H.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()


def status_color(t):
    """Lozenge colour for a (Vietnamese) document status name; None if the text is not a status."""
    if len(t.split()) > 5:
        return None
    for pat, color in [(r'^(Nháp|Giữ chỗ)', 'neutral'), (r'^Chờ', 'yellow'), (r'^Trả lại', 'purple'),
                       (r'^(Từ chối|Đã hủy|Đã bị|Đã đảo|Hủy)', 'red'), (r'^(Hoàn thành|Đã chi|Đã có mã|Đã ghi sổ|Đã đóng)', 'green'),
                       (r'^(Đã duyệt|Đã ký|Đã gửi|Đã xác nhận|Đang)', 'blue')]:
        if re.match(pat, t):
            return color
    return None


def edit_section(html, start_pat, fn, end_pat=r'<h2>'):
    m = re.search(start_pat, html)
    if not m:
        return html
    e = re.compile(end_pat).search(html, m.end())
    end = e.start() if e else len(html)
    return html[:m.start()] + fn(html[m.start():end]) + html[end:]


def build(md_path, d):
    images = os.path.join(os.path.dirname(os.path.abspath(md_path)), 'images')
    html = subprocess.run(['node', '-e', MARKED, md_path], capture_output=True, text=True, check=True).stdout
    html = re.sub(r'<(h[1-6]) id="[^"]*">', r'<\1>', html)      # Confluence rejects id on headings
    html = re.sub(r'<(t[hd]) align="[^"]*">', r'<\1>', html)
    html = re.sub(r'<hr>\s*', '', html)
    html = re.sub(r'<br>', '<br/>', html)
    html = re.sub(r'>\s*\n\s*<', '><', html)

    # ---- page header: version table + info table + table of contents + collapsed "how to read"
    head_end = html.index('<h2>1. ')
    head, html = html[:head_end], html[head_end:]
    cach_doc = ''
    m = re.search(r'<h2>Cách đọc tài liệu</h2>(.*)$', head, re.S)
    if m:
        cach_doc, head = m.group(1), head[:m.start()]
    tables = re.findall(r'<table>.*?</table>', head, re.S)
    version = next((t for t in tables if '<th>Version</th>' in t), '')
    version = re.sub(r'<td>(\d{2})/(\d{2})/(\d{4})</td>', r'<td><time datetime="\3-\2-\1"/></td>', version)
    info = next((t for t in tables if t is not version), '')
    info = re.sub(r'<thead>.*?</thead>', '', info, flags=re.S)
    info = re.sub(r'(<td>(?:Trạng thái|Phiên bản)</td><td>)[^<]*[Nn]háp[^<]*(</td>)', lambda x: x.group(1) + d.lozenge('BẢN NHÁP', 'yellow') + x.group(2), info)
    html = (version + info + '<p><strong>Mục lục</strong></p>' + d.toc() +
            (d.expand('Cách đọc tài liệu: mã tham chiếu, nhãn, ký hiệu', cach_doc) if cach_doc else '') + html)

    # ---- lozenges
    html = re.sub(r'(?:<strong>)?\[?(Cần xác nhận|Đề xuất): (CH-(?:\d+|xx)(?:, CH-\d+)*)\]?(?:</strong>)?',
                  lambda x: d.lozenge(f'{x.group(1).upper()} {x.group(2).upper()}', 'yellow' if x.group(1) == 'Cần xác nhận' else 'purple'), html)
    html = re.sub(r'<em>([^<]+)</em>', lambda x: d.lozenge(x.group(1).upper(), status_color(x.group(1))) if status_color(x.group(1)) else x.group(0), html)
    PRIO = {'High': 'red', 'Cao': 'red', 'Medium': 'yellow', 'Trung bình': 'yellow', 'Low': 'green', 'Thấp': 'green'}
    html = re.sub(r'(<td>Mức độ ưu tiên</td><td>)(High|Medium|Low|Cao|Trung bình|Thấp)(</td>)',
                  lambda x: x.group(1) + d.lozenge(x.group(2).upper(), PRIO[x.group(2)]) + x.group(3), html)

    def status_column(t):          # table with a "Trạng thái … sau …" column: last cell becomes lozenges
        if not re.search(r'<th>Trạng thái[^<]*sau[^<]*</th>', t):
            return t
        def cell(x):
            parts = [p.strip() for p in x.group(1).split(' / ')]
            return '<td>' + ' '.join(d.lozenge(p.upper(), status_color(p)) for p in parts) + '</td>' if all(map(status_color, parts)) else x.group(0)
        return re.sub(r'<td>([^<]+)</td>(?=</tr>)', cell, t)
    html = re.sub(r'<table>.*?</table>', lambda x: status_column(x.group(0)), html, flags=re.S)

    # ---- panels
    html = re.sub(r'<blockquote>(.*?)</blockquote>', lambda x: d.panel('info', x.group(1)), html, flags=re.S)
    html = re.sub(r'(<h2>5\. [^<]*</h2>)((?:<p>.*?</p>)+)', lambda x: x.group(1) + d.panel('warning', x.group(2)), html, count=1, flags=re.S)
    html = re.sub(r'(<h2>8\. [^<]*</h2>)(<p>.*?</p>)', lambda x: x.group(1) + d.panel('note', x.group(2)), html, count=1, flags=re.S)
    html = re.sub(r'(<h2>10\. [^<]*</h2>)', lambda x: x.group(1) + d.panel('warning', '<p>Các câu hỏi dưới đây cần được trả lời trước '
                  'khi cấu hình hệ thống, nhóm theo người cần trả lời.</p>'), html, count=1)

    # ---- expand blocks
    html = edit_section(html, r'<h3>2\.3 ', lambda p: re.sub(
        r'<h4>(.*?)</h4>(.*?)(?=<h4>|$)', lambda x: d.expand(text(x.group(1)), x.group(2)), p, flags=re.S)
        .replace('</h3>', '</h3><p>Bấm vào từng bước để xem chi tiết.</p>', 1), r'<h[23]>(?!2\.3)')
    html = re.sub(r'(<h3>2\.6 [^<]*</h3>(?:<p>.*?</p>)*)(<table>.*?</table>)',
                  lambda x: x.group(1) + d.expand(f'Xem {x.group(2).count("<tr>") - 1} tình huống và thông báo hiển thị', x.group(2)),
                  html, count=1, flags=re.S)

    def group(x):
        ids = re.findall(r'<td>((?:QT|TS)-\d+)</td>', x.group(2))
        return d.expand(text(x.group(1)) + (f' ({ids[0]} – {ids[-1]})' if len(ids) > 1 else ''), x.group(2))
    html = re.sub(r'<p><strong>([a-z]\) [^<]+)</strong></p>(<table>.*?</table>)', group, html, flags=re.S)
    html = re.sub(r'<p><strong>(Ví dụ \d[^<]*)</strong></p>(<table>.*?</table>)', lambda x: d.expand(text(x.group(1)), x.group(2)), html, flags=re.S)

    # ---- tables: 2-column -> grey label column; section 4 colour-codes permissions; section 10 gets a status column
    def two_col(t):
        first = re.search(r'<tr>.*?</tr>', t, re.S)
        if first and len(re.findall(r'<t[hd]>', first.group(0))) == 2:
            t = re.sub(r'<tr><td>(.*?)</td>', lambda c: '<tr>' + d.bg('td', GRAY) + f'<strong>{c.group(1)}</strong></td>', t, flags=re.S)
        return t
    html = re.sub(r'<table>.*?</table>', lambda x: two_col(x.group(0)), html, flags=re.S)

    LEVEL = {'Thực hiện': GREEN, 'Duyệt': BLUE, 'Duyệt, Một phần': BLUE, 'Một phần': YELLOW, '—': GRAY, 'Ẩn': GRAY, 'Che': YELLOW}

    def color_cells(t):
        def row(m):
            out = m.group(0)
            for i, c in enumerate(re.findall(r'<td>.*?</td>', out, re.S)):
                v = text(c)
                color = (GREEN if v.startswith(('✔', 'Sửa')) else LEVEL.get(v)) if i else None
                if color:
                    out = out.replace(c, d.bg('td', color) + c[4:], 1)
            return out
        return re.sub(r'<tr>.*?</tr>', row, t, flags=re.S) if re.search(r'✔|>Thực hiện<|>Ẩn<', t) else t
    html = edit_section(html, r'<h2>4\. ', lambda p: re.sub(r'<table>.*?</table>', lambda x: color_cells(x.group(0)), p, flags=re.S))

    def questions(t):
        if not re.search(r'<thead><tr><th>Mã</th><th>Câu hỏi</th>', t):
            return t
        t = re.sub(r'(<thead><tr>.*?)(</tr></thead>)', r'\1<th>Trạng thái</th>\2', t, count=1, flags=re.S)
        head, body = t.split('<tbody>', 1)
        return head + '<tbody>' + body.replace('</tr>', '<td>' + d.lozenge('ĐANG MỞ', 'yellow') + '</td></tr>')
    html = edit_section(html, r'<h2>10\. ', lambda p: re.sub(r'<table>.*?</table>', lambda x: questions(x.group(0)), p, flags=re.S))
    html = html.replace('<table>', '<table data-layout="wide">').replace('<th>', d.bg('th', GRAY))

    # ---- section 6: landscape images full width, consecutive portrait images side by side
    pat = re.compile(r'<h3>(Hình \d+[^<]*)</h3>((?:<p>(?!<img)[^<]*</p>)?)<p><img src="images/([^"]+\.png)" alt="[^"]*"></p>')
    items = list(pat.finditer(html))
    if items:
        def ratio(f):
            with open(os.path.join(images, f), 'rb') as fh:
                w, h = struct.unpack('>II', fh.read(24)[16:24])
            return w / h

        def one(it, pct):
            t, note, f = it.groups()
            return f'<h3>{t}</h3>{note}' + d.image(f, t, pct)
        blocks, i = [], 0
        while i < len(items):
            f = items[i].group(3)
            if ratio(f) < 1 and i + 1 < len(items) and ratio(items[i + 1].group(3)) < 1:
                blocks.append(d.two_columns(one(items[i], 100), one(items[i + 1], 100)))
                i += 2
            else:
                blocks.append(one(items[i], 100 if ratio(f) > 1.6 else 80))
                i += 1
        html = html[:items[0].start()] + ''.join(blocks) + html[items[-1].end():]
    return html


def stats(body, dialect):
    """Count page elements to compare before/after saving."""
    if dialect == 'storage':
        return {'images': body.count('<ac:image'), 'tables': body.count('<table'), 'expands': body.count('ac:name="expand"'),
                'toc': body.count('ac:name="toc"')}
    return {'images': body.count('data-type="media"'), 'tables': body.count('<table'), 'expands': body.count('<details'),
            'toc': body.count('extension-key="toc"')}


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('md')
    ap.add_argument('--dialect', default='adf', choices=['adf', 'storage'])
    ap.add_argument('--files')
    ap.add_argument('--page-id', default='')
    a = ap.parse_args()
    files = json.load(open(a.files)) if a.files else {}
    sys.stdout.write(build(a.md, Storage() if a.dialect == 'storage' else ADF(files, a.page_id)))
