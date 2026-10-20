#!/usr/bin/env python3
"""Sinh BPMN 2.0 (kèm toạ độ DI) và tài liệu markdown từ định nghĩa quy trình.

Dùng chung cho mọi dự án. Một dự án là một thư mục có defs/:
    defs/_common.py   gọi register(roles=..., pools=..., processes=...) — danh mục dùng chung của dự án
    defs/bpNN_*.py    mỗi file một quy trình, khai báo biến PROCESS (dict)
Sơ đồ và bảng bước trong tài liệu sinh từ CÙNG một định nghĩa nên không lệch nhau.

    python3 bpmn_gen.py <thư-mục-dự-án>            # sinh bpmn/, docs/, viewer.html, CAU-HOI-KHAO-SAT.md
    python3 bpmn_gen.py <thư-mục-dự-án> BP-05      # chỉ sinh một quy trình
Thường gọi qua scripts/build.sh (sinh → render → bpmnlint).

Bố cục theo lưới: mỗi phần tử nằm ở (làn, cột, hàng trong làn). Đường nối được
định tuyến vuông góc; công cụ kiểm tra va chạm sẽ cảnh báo khi một đường đi
xuyên qua phần tử khác để sửa lại vị trí trong định nghĩa.
"""
import glob
import importlib.util
import math
import os
import sys
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.dirname(HERE)
BOOKS_DIR = os.path.join(os.path.dirname(KIT), 'books')
ROOT = None  # thư mục dự án, đặt trong main()

# ---------------------------------------------------------------- kích thước
POOL_X = 100
POOL_LABEL = 30
LANE_LABEL = 30
PAD_X = 20
COLW = 175
ROWH = 140
EXT_H = 60
EXT_GAP = 64
TOP_MARGIN = 40
LOOP_OFF = 20

SIZES = {
    'task': (136, 88), 'event': (36, 36), 'gateway': (50, 50),
    'store': (50, 50), 'obj': (36, 50),
}

TASK_TYPES = {
    'task': 'task', 'user': 'userTask', 'service': 'serviceTask', 'send': 'sendTask',
    'receive': 'receiveTask', 'manual': 'manualTask', 'rule': 'businessRuleTask',
    'script': 'scriptTask', 'call': 'callActivity', 'sub': 'subProcess',
}
GW_TYPES = {'xor': 'exclusiveGateway', 'and': 'parallelGateway', 'evt': 'eventBasedGateway'}
EV_TYPES = {
    'start': 'startEvent', 'end': 'endEvent', 'catch': 'intermediateCatchEvent',
    'throw': 'intermediateThrowEvent', 'boundary': 'boundaryEvent',
}
EV_DEFS = {
    'message': 'messageEventDefinition', 'timer': 'timerEventDefinition',
    'signal': 'signalEventDefinition', 'conditional': 'conditionalEventDefinition',
    'terminate': 'terminateEventDefinition', 'error': 'errorEventDefinition',
    'escalation': 'escalationEventDefinition',
}
KIND_LABEL = {
    'start': 'Sự kiện bắt đầu', 'end': 'Sự kiện kết thúc', 'catch': 'Sự kiện chờ',
    'throw': 'Sự kiện phát', 'boundary': 'Sự kiện biên',
    'task': 'Công việc', 'user': 'Người dùng thao tác', 'service': 'Hệ thống tự động',
    'send': 'Gửi thông điệp', 'receive': 'Nhận thông điệp', 'manual': 'Thủ công ngoài hệ thống',
    'rule': 'Quy tắc nghiệp vụ', 'script': 'Hệ thống tự động', 'call': 'Gọi quy trình khác',
    'sub': 'Quy trình con', 'xor': 'Rẽ nhánh (XOR)', 'and': 'Song song (AND)',
    'evt': 'Rẽ nhánh theo sự kiện',
}
EV_LABEL = {
    'message': 'thông điệp', 'timer': 'hẹn giờ', 'signal': 'tín hiệu',
    'conditional': 'điều kiện', 'terminate': 'kết thúc toàn bộ', 'error': 'lỗi',
    'escalation': 'leo thang',
}


# ---------------------------------------------------------------- DSL
# ---------------------------------------------------------------- danh mục dự án
REG = dict(roles={}, pools={}, processes={})


def register(roles, pools, processes):
    """Gọi một lần trong defs/_common.py. processes: {mã: (slug, tiêu đề ngắn)}."""
    REG['roles'].update(roles)
    REG['pools'].update(pools)
    REG['processes'].update(processes)


def lane(key, desc):
    return (key, REG['roles'][key], desc)


def pool(key, side, band=0, cols=None, name=None):
    d = dict(key=key, name=name or REG['pools'][key], side=side, band=band)
    if cols:
        d['cols'] = cols
    return d


def slug(code):
    return REG['processes'][code][0]


def title(code):
    return REG['processes'][code][1]


def call_name(code):
    """Tên chuẩn cho call activity gọi sang quy trình khác."""
    return '%s %s' % (code, title(code))


def bp(code, text=''):
    """Liên kết tới tài liệu của quy trình khác."""
    return '[%s](%s.md)%s' % (code, slug(code), (' ' + text) if text else '')


_BOOKS = {
    'P': ('parthasarathy-erp-fundamentals', 'Parthasarathy'),
    'W': ('wallace-erp-implementation', 'Wallace & Kremzar'),
    'O': ('oleary-erp-systems-lifecycle', "O'Leary"),
    'E': ('elbardan-erp-governance-audit', 'Elbardan & Kholeif'),
}


def _link(path):
    return os.path.relpath(path, os.path.join(ROOT, 'docs')) if os.path.exists(path) else None


def book(code, chapter_file, text):
    """Trích sách trong erp-ba-skills/books. code: P, W, O, E; chapter_file: 'ch08-....md' hoặc 'cheatsheet.md'."""
    folder, author = _BOOKS[code]
    sub = 'chapters/' + chapter_file if chapter_file.startswith('ch') else chapter_file
    chap = chapter_file.split('-')[0] if chapter_file.startswith('ch') else chapter_file.replace('.md', '')
    link = _link(os.path.join(BOOKS_DIR, folder, sub))
    src = ' ([nguồn](%s))' % link if link else ''
    return '**%s, %s**%s — %s' % (author, chap, src, text)


def ref(label, path, text):
    """Trích một tài liệu bất kỳ (tuyệt đối hoặc tương đối thư mục dự án); có liên kết nếu file tồn tại."""
    full = path if os.path.isabs(path) else os.path.join(ROOT, path)
    link = _link(full)
    return '**%s**%s — %s' % (label, ' ([nguồn](%s))' % link if link else '', text)


def core(rel, section, text):
    """Trích thư viện quy trình erp-ba-core (nếu còn trên đĩa thì có liên kết)."""
    return ref('erp-ba-core `%s` %s' % (rel.split('/')[-1], section),
               os.path.join(os.path.dirname(KIT), 'erp-ba-core', 'references', rel), text)


def N(id, kind, lane, col, name, row=0, **kw):
    """Phần tử luồng: sự kiện, công việc, cổng."""
    d = dict(id=id, kind=kind, lane=lane, col=col, row=row, name=name)
    d.update(kw)
    return d


def F(src, tgt, name=None, **kw):
    """Luồng tuần tự. kw: default, via=[(col, lane, row)], loop='top'|'bottom', route='vh'|'hv'."""
    d = dict(src=src, tgt=tgt, name=name)
    d.update(kw)
    return d


def M(src, tgt, name, dx=0, side=None):
    """Luồng thông điệp giữa phần tử và pool ngoài (khoá pool). side: nhãn nằm 'left' hay 'right' đường."""
    return dict(src=src, tgt=tgt, name=name, dx=dx, side=side or ('right' if dx >= 0 else 'left'))


def A(id, target, text, lane, col, row=0, w=None, h=58, dx=0, dy=0):
    """Chú thích (thường dùng để ghi điểm kiểm soát) đặt ở một ô lưới trống."""
    return dict(id=id, target=target, text=text, lane=lane, col=col, row=row, w=w, h=h, dx=dx, dy=dy)


def D(id, kind, name, lane, col, row=0, links=(), dx=0, dy=0):
    """Kho dữ liệu ('store') hoặc chứng từ ('obj'); links=[(node_id, 'out'|'in')]."""
    return dict(id=id, kind=kind, name=name, lane=lane, col=col, row=row, links=list(links), dx=dx, dy=dy)


# ---------------------------------------------------------------- tiện ích
def x_esc(s):
    return escape(s or '', {'"': '&quot;'})


def size_of(n):
    k = n['kind']
    if k in TASK_TYPES:
        return n.get('w', SIZES['task'][0]), n.get('h', SIZES['task'][1])
    if k in GW_TYPES:
        return SIZES['gateway']
    if k in EV_TYPES:
        return SIZES['event']
    return SIZES[k]


def cat(n):
    k = n['kind']
    if k in TASK_TYPES:
        return 'task'
    if k in GW_TYPES:
        return 'gateway'
    if k in EV_TYPES:
        return 'event'
    return k


class Box(object):
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = float(x), float(y), float(w), float(h)

    @property
    def cx(self):
        return self.x + self.w / 2

    @property
    def cy(self):
        return self.y + self.h / 2

    @property
    def r(self):
        return self.x + self.w

    @property
    def b(self):
        return self.y + self.h


def r2(v):
    return int(round(v))


# ---------------------------------------------------------------- bố cục
class Layout(object):
    def __init__(self, P):
        self.P = P
        self.nodes = {n['id']: n for n in P['nodes']}
        self.lane_keys = [l[0] for l in P['lanes']]
        self.warnings = []
        self._compute()

    def col_left(self, c):
        return POOL_X + POOL_LABEL + LANE_LABEL + PAD_X + c * COLW

    def col_cx(self, c):
        return self.col_left(c) + COLW / 2.0

    def row_cy(self, lane, row):
        return self.lane_y[lane] + row * ROWH + ROWH / 2.0

    def row_edge(self, n, side):
        """Mép trên (side=-1) hoặc mép dưới (side=1) của hàng chứa phần tử n."""
        return self.row_cy(n['lane'], n['row']) + side * ROWH / 2.0

    def _compute(self):
        P = self.P
        rows = dict((k, 1) for k in self.lane_keys)
        maxcol = 0
        items = list(P['nodes']) + list(P.get('annotations', [])) + list(P.get('data', []))
        for it in items:
            if it.get('kind') == 'boundary':
                continue
            if it['lane'] not in rows:
                raise ValueError('%s: làn %s không tồn tại' % (it['id'], it['lane']))
            span = 1
            if 'target' in it and it.get('h', 58) > ROWH - 10:
                span = int(math.ceil(it['h'] / float(ROWH)))
            rows[it['lane']] = max(rows[it['lane']], int(math.floor(it['row'])) + span)
            wc = 1
            if 'target' in it and it.get('w'):
                wc = int(math.ceil(it['w'] / float(COLW)))
            maxcol = max(maxcol, int(math.ceil(it['col'])) + wc - 1)
        for k, v in P.get('lane_rows', {}).items():
            rows[k] = max(rows[k], v)
        self.ncols = maxcol + 1
        self.main_w = POOL_LABEL + LANE_LABEL + PAD_X * 2 + self.ncols * COLW

        ext = P.get('pools', [])
        self.ext = {}
        top_bands = max([e.get('band', 0) + 1 for e in ext if e['side'] == 'top'] or [0])
        self.main_y = TOP_MARGIN + top_bands * (EXT_H + EXT_GAP)
        y = self.main_y
        self.lane_y, self.lane_h = {}, {}
        for k in self.lane_keys:
            self.lane_y[k] = y
            self.lane_h[k] = rows[k] * ROWH
            y += self.lane_h[k]
        self.main_h = y - self.main_y
        for e in ext:
            band = e.get('band', 0)
            if 'cols' in e:
                c0, c1 = e['cols']
                x0 = self.col_left(c0) + 6
                x1 = self.col_left(c1 + 1) - 6
            else:
                x0, x1 = POOL_X, POOL_X + self.main_w
            if e['side'] == 'top':
                yy = self.main_y - EXT_GAP - EXT_H - band * (EXT_H + EXT_GAP)
            else:
                yy = self.main_y + self.main_h + EXT_GAP + band * (EXT_H + EXT_GAP)
            self.ext[e['key']] = dict(e, box=Box(x0, yy, x1 - x0, EXT_H))

        # phần tử luồng
        self.box = {}
        for n in P['nodes']:
            if n['kind'] == 'boundary':
                continue
            w, h = size_of(n)
            cx = self.col_cx(n['col']) + n.get('dx', 0)
            cy = self.row_cy(n['lane'], n['row']) + n.get('dy', 0)
            self.box[n['id']] = Box(cx - w / 2.0, cy - h / 2.0, w, h)
        for n in P['nodes']:
            if n['kind'] != 'boundary':
                continue
            host = self.box[n['attach']]
            n['lane'] = self.nodes[n['attach']]['lane']
            n['col'] = self.nodes[n['attach']]['col']
            n['row'] = self.nodes[n['attach']]['row']
            pos = n.get('pos', 0.75)
            cx = host.x + host.w * pos
            edge_y = host.y if n.get('edge') == 'top' else host.b
            self.box[n['id']] = Box(cx - 18, edge_y - 18, 36, 36)
        for a in P.get('annotations', []):
            w = a['w'] or COLW - 14
            x = self.col_left(a['col']) + 7 + a['dx']
            cy = self.row_cy(a['lane'], a['row']) + a['dy']
            self.box[a['id']] = Box(x, cy - a['h'] / 2.0, w, a['h'])
        for d in P.get('data', []):
            w, h = SIZES[d['kind']]
            cx = self.col_cx(d['col']) + d['dx']
            cy = self.row_cy(d['lane'], d['row']) + d['dy']
            self.box[d['id']] = Box(cx - w / 2.0, cy - h / 2.0, w, h)

        self.total_w = POOL_X + self.main_w + 60
        bottoms = [self.main_y + self.main_h] + [e['box'].b for e in self.ext.values()]
        self.total_h = max(bottoms) + 40

    # ------------------------------------------------------------ định tuyến
    def anchor_toward(self, nid, pt):
        b = self.box[nid]
        dx, dy = pt[0] - b.cx, pt[1] - b.cy
        if abs(dx) >= abs(dy):
            return (b.r, b.cy) if dx > 0 else (b.x, b.cy)
        return (b.cx, b.b) if dy > 0 else (b.cx, b.y)

    def route(self, f):
        s, t = self.box[f['src']], self.box[f['tgt']]
        sn, tn = self.nodes[f['src']], self.nodes[f['tgt']]
        if f.get('via'):
            via = [(self.col_cx(c), self.row_cy(lane, row)) for c, lane, row in f['via']]
            first, last = via[0], via[-1]
            a = self.anchor_toward(f['src'], first)
            z = self.anchor_toward(f['tgt'], last)
            pts = [a]
            # bảo đảm đoạn đầu/cuối vuông góc
            if a[0] != first[0] and a[1] != first[1]:
                horizontal_exit = a[1] == s.cy and a[0] in (s.x, s.r)
                pts.append((first[0], a[1]) if horizontal_exit else (a[0], first[1]))
            pts += via
            if z[0] != last[0] and z[1] != last[1]:
                horizontal_entry = z[1] == t.cy and z[0] in (t.x, t.r)
                pts.append((last[0], z[1]) if horizontal_entry else (z[0], last[1]))
            pts.append(z)
            return pts
        if sn['kind'] == 'boundary' and sn.get('edge') == 'top':
            if t.b < s.y:
                if t.x <= s.cx <= t.r:
                    return [(s.cx, s.y), (s.cx, t.b)]
                if t.cx > s.cx:
                    return [(s.cx, s.y), (s.cx, t.cy), (t.x, t.cy)]
                return [(s.cx, s.y), (s.cx, t.cy), (t.r, t.cy)]
            yt = s.y - LOOP_OFF
            return [(s.cx, s.y), (s.cx, yt), (t.cx, yt), (t.cx, t.y)]
        if sn['kind'] == 'boundary':
            if t.y > s.b:
                if t.x <= s.cx <= t.r:
                    return [(s.cx, s.b), (s.cx, t.y)]
                if t.cx > s.cx:
                    return [(s.cx, s.b), (s.cx, t.cy), (t.x, t.cy)]
                return [(s.cx, s.b), (s.cx, t.cy), (t.r, t.cy)]
            yb = s.b + LOOP_OFF
            return [(s.cx, s.b), (s.cx, yb), (t.cx, yb), (t.cx, t.b)]
        backward = t.cx < s.cx - 1 or f.get('loop')
        if backward:
            # vòng lặp chạy sát mép hàng để không sượt qua các ô cao hơn nằm giữa đường
            if f.get('loop', 'bottom') == 'top':
                yt = min(self.row_edge(sn, -1), self.row_edge(tn, -1)) + 10
                return [(s.cx, s.y), (s.cx, yt), (t.cx, yt), (t.cx, t.y)]
            yb = max(self.row_edge(sn, 1), self.row_edge(tn, 1)) - 10
            return [(s.cx, s.b), (s.cx, yb), (t.cx, yb), (t.cx, t.b)]
        if abs(s.cy - t.cy) < 1:
            return [(s.r, s.cy), (t.x, t.cy)]
        route = f.get('route')
        if abs(t.cx - s.cx) < 1:  # cùng cột: nối thẳng đứng
            return [(s.cx, s.b), (t.cx, t.y)] if t.cy > s.cy else [(s.cx, s.y), (t.cx, t.b)]
        if route is None and cat(sn) == 'gateway' and \
                self._side_used_by_incoming(sn['id'], 'b' if t.cy > s.cy else 't'):
            # cạnh trên/dưới của cổng đã có luồng đi vào: luồng ra rẽ ngang trước để không chồng lên
            route = 'hv_in' if cat(tn) == 'gateway' else 'hv'
        if route == 'vh' or (route is None and cat(sn) == 'gateway'):
            sy = s.b if t.cy > s.cy else s.y
            return [(s.cx, sy), (s.cx, t.cy), (t.x, t.cy)]
        if route == 'hv_in' or (route is None and cat(tn) == 'gateway'):
            ty = t.y if s.cy < t.cy else t.b
            return [(s.r, s.cy), (t.cx, s.cy), (t.cx, ty)]
        xm = self.col_left(tn['col']) + 12 if 'xm' not in f else self.col_left(f['xm']) + 12
        return [(s.r, s.cy), (xm, s.cy), (xm, t.cy), (t.x, t.cy)]

    def _side_used_by_incoming(self, nid, side):
        b = self.box[nid]
        for f in self.P['flows']:
            if f['tgt'] == nid and side_of(b, self.route(f)[-1]) == side:
                return True
        return False

    def msg_route(self, m):
        if m['src'] in self.ext:
            pool, nid, out = self.ext[m['src']], m['tgt'], False
        else:
            pool, nid, out = self.ext[m['tgt']], m['src'], True
        b = self.box[nid]
        x = b.cx + m.get('dx', 0)
        if pool['side'] == 'top':
            npt, ppt = (x, b.y), (x, pool['box'].b)
        else:
            npt, ppt = (x, b.b), (x, pool['box'].y)
        pts = [npt, ppt] if out else [ppt, npt]
        return pts, pool

    # ------------------------------------------------------------ kiểm tra
    def check(self):
        P = self.P
        ids = [n['id'] for n in P['nodes']]
        if len(ids) != len(set(ids)):
            self.warnings.append('ID phần tử trùng lặp')
        cells = {}
        for n in P['nodes']:
            if n['kind'] in ('service', 'script') and n['lane'] != 'SYS':
                self.warnings.append('%s là bước tự động nhưng không nằm ở làn SYS' % n['id'])
            if n['kind'] in ('user', 'manual') and n['lane'] == 'SYS':
                self.warnings.append('%s là bước người làm nhưng nằm ở làn SYS' % n['id'])
            if n['kind'] == 'boundary':
                continue
            key = (n['lane'], n['col'], n['row'])
            if key in cells:
                self.warnings.append('Trùng ô lưới: %s và %s' % (cells[key], n['id']))
            cells[key] = n['id']
        boxes = list(self.box.items())
        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                a, b = boxes[i][1], boxes[j][1]
                ia, ib = boxes[i][0], boxes[j][0]
                na, nb = self.nodes.get(ia, {}), self.nodes.get(ib, {})
                if na.get('attach') == ib or nb.get('attach') == ia:
                    continue
                if a.x < b.r and b.x < a.r and a.y < b.b and b.y < a.b:
                    self.warnings.append('Chồng lấn: %s và %s' % (ia, ib))
        routed = []
        for f in P['flows']:
            pts = self.route(f)
            routed.append((f, pts))
            self._seg_check('Luồng %s→%s' % (f['src'], f['tgt']), pts, (f['src'], f['tgt']))
        # hai luồng đi chồng lên cùng một đoạn thẳng thì không đọc được hướng (trừ khi cùng đổ vào một đích)
        for i in range(len(routed)):
            for j in range(i + 1, len(routed)):
                (fa, pa), (fb, pb) = routed[i], routed[j]
                if fa['tgt'] == fb['tgt']:
                    continue
                if _overlap(pa, pb):
                    self.warnings.append('Luồng %s→%s chồng lên luồng %s→%s'
                                         % (fa['src'], fa['tgt'], fb['src'], fb['tgt']))
        for m in P.get('messages', []):
            pts, _ = self.msg_route(m)
            self._seg_check('Thông điệp %s→%s' % (m['src'], m['tgt']), pts, (m['src'], m['tgt']))

    def _seg_check(self, label, pts, ends):
        skip = set(ends)
        for e in ends:
            n = self.nodes.get(e)
            if n and n.get('attach'):
                skip.add(n['attach'])
            for o in self.P['nodes']:
                if o.get('attach') == e:
                    skip.add(o['id'])
        for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
            lo_x, hi_x = min(x1, x2), max(x1, x2)
            lo_y, hi_y = min(y1, y2), max(y1, y2)
            for nid, b in self.box.items():
                if nid in skip:
                    continue
                if lo_x < b.r - 2 and hi_x > b.x + 2 and lo_y < b.b - 2 and hi_y > b.y + 2:
                    self.warnings.append('%s cắt qua %s' % (label, nid))


def _overlap(pa, pb, min_len=6):
    """Có cặp đoạn thẳng cùng phương, cùng đường, trùng nhau dài hơn min_len không."""
    for (a1, a2) in zip(pa, pa[1:]):
        for (b1, b2) in zip(pb, pb[1:]):
            if abs(a1[0] - a2[0]) < 1 and abs(b1[0] - b2[0]) < 1 and abs(a1[0] - b1[0]) < 1:
                lo = max(min(a1[1], a2[1]), min(b1[1], b2[1]))
                hi = min(max(a1[1], a2[1]), max(b1[1], b2[1]))
                if hi - lo > min_len:
                    return True
            if abs(a1[1] - a2[1]) < 1 and abs(b1[1] - b2[1]) < 1 and abs(a1[1] - b1[1]) < 1:
                lo = max(min(a1[0], a2[0]), min(b1[0], b2[0]))
                hi = min(max(a1[0], a2[0]), max(b1[0], b2[0]))
                if hi - lo > min_len:
                    return True
    return False


# ---------------------------------------------------------------- vị trí nhãn
def label_box_for_node(L, n, used_sides):
    b = L.box[n['id']]
    name = n.get('name') or ''
    lines = max(1, int(math.ceil(len(name) / 16.0)))
    h = 14 * min(lines, 4)
    w = 100
    lane_top = L.lane_y[n['lane']]
    lane_bot = lane_top + L.lane_h[n['lane']]
    if n['kind'] == 'boundary':
        if n.get('edge') == 'top':
            return Box(b.r + 2, b.y - h + 2, 90, h)
        return Box(b.r + 2, b.b - 2, 90, h)
    top = Box(b.cx - w / 2.0, b.y - h - 6, w, h)
    bottom = Box(b.cx - w / 2.0, b.b + 6, w, h)
    if cat(n) == 'gateway':
        cands = [(top, 't'), (bottom, 'b')]
        fallback = Box(b.x - w - 4, b.y - h + 8, w, h)  # phía trên bên trái
    else:
        cands = [(bottom, 'b'), (top, 't')]
        fallback = Box(b.r + 4, b.b - 4, w, h)
    for box, side in cands:
        if side not in used_sides and box.y >= lane_top + 2 and box.b <= lane_bot - 2:
            return box
    return fallback


def side_of(b, pt):
    x, y = pt
    if abs(y - b.y) < 0.6:
        return 't'
    if abs(y - b.b) < 0.6:
        return 'b'
    if abs(x - b.x) < 0.6:
        return 'l'
    return 'r'


def flow_label_box(pts, name):
    (x1, y1), (x2, y2) = pts[0], pts[1]
    w = max(36, min(130, 7 * len(name)))
    lines = int(math.ceil(7 * len(name) / 130.0))
    h = 14 * max(1, lines)
    if abs(y1 - y2) < 0.6:  # rời theo phương ngang
        if x2 >= x1:
            return Box(x1 + 6, y1 - h - 3, w, h)
        return Box(x1 - w - 6, y1 - h - 3, w, h)
    if y2 > y1:
        return Box(x1 + 5, y1 + 4, w, h)
    return Box(x1 + 5, y1 - h - 4, w, h)


# ---------------------------------------------------------------- XML
def build_xml(P, L):
    code = P['id'].replace('-', '')
    proc_id = 'Process_' + code
    out = []
    w = out.append
    w('<?xml version="1.0" encoding="UTF-8"?>')
    w('<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" '
      'xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" '
      'xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" '
      'xmlns:di="http://www.omg.org/spec/DD/20100524/DI" '
      'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
      'id="Definitions_%s" targetNamespace="http://tour-erp.local/bpmn" '
      'exporter="tour-erp-bpmn (bpmn_gen.py)" exporterVersion="1.0">' % code)
    # collaboration
    w('  <bpmn:collaboration id="Collab_%s">' % code)
    w('    <bpmn:participant id="P_MAIN" name="%s" processRef="%s" />'
      % (x_esc(P.get('pool_name', 'Công ty lữ hành')), proc_id))
    for e in P.get('pools', []):
        w('    <bpmn:participant id="P_%s" name="%s" />' % (e['key'], x_esc(e['name'])))
    for i, m in enumerate(P.get('messages', []), 1):
        s = 'P_' + m['src'] if m['src'] in L.ext else m['src']
        t = 'P_' + m['tgt'] if m['tgt'] in L.ext else m['tgt']
        w('    <bpmn:messageFlow id="MF_%d" name="%s" sourceRef="%s" targetRef="%s" />'
          % (i, x_esc(m['name']), s, t))
    w('  </bpmn:collaboration>')

    # process
    w('  <bpmn:process id="%s" name="%s" isExecutable="false">' % (proc_id, x_esc(P['id'] + ' ' + P['name'])))
    if P.get('objective'):
        w('    <bpmn:documentation>%s</bpmn:documentation>' % x_esc(P['objective']))
    w('    <bpmn:laneSet id="LaneSet_%s">' % code)
    for k, name, _desc in P['lanes']:
        w('      <bpmn:lane id="Lane_%s" name="%s">' % (k, x_esc(name)))
        for n in P['nodes']:
            if n['lane'] == k:
                w('        <bpmn:flowNodeRef>%s</bpmn:flowNodeRef>' % n['id'])
        w('      </bpmn:lane>')
    w('    </bpmn:laneSet>')

    flows = P['flows']
    for i, f in enumerate(flows, 1):
        f['_id'] = 'Flow_%d' % i
    inc = dict((n['id'], []) for n in P['nodes'])
    outg = dict((n['id'], []) for n in P['nodes'])
    for f in flows:
        outg[f['src']].append(f)
        inc[f['tgt']].append(f)
    data_links = {}
    for d in P.get('data', []):
        for nid, direction in d['links']:
            data_links.setdefault(nid, []).append((d, direction))

    for n in P['nodes']:
        k = n['kind']
        attrs = 'id="%s" name="%s"' % (n['id'], x_esc(n.get('name')))
        if k in TASK_TYPES:
            tag = TASK_TYPES[k]
            if k == 'call' and n.get('called'):
                attrs += ' calledElement="%s"' % ('Process_' + n['called'].replace('-', ''))
        elif k in GW_TYPES:
            tag = GW_TYPES[k]
            dflt = [f for f in outg[n['id']] if f.get('default')]
            if dflt:
                attrs += ' default="%s"' % dflt[0]['_id']
        else:
            tag = EV_TYPES[k]
            if k == 'boundary':
                attrs += ' attachedToRef="%s"' % n['attach']
                if n.get('interrupting') is False:
                    attrs += ' cancelActivity="false"'
        w('    <bpmn:%s %s>' % (tag, attrs))
        if n.get('doc'):
            w('      <bpmn:documentation>%s</bpmn:documentation>' % x_esc(n['doc']))
        for f in inc[n['id']]:
            w('      <bpmn:incoming>%s</bpmn:incoming>' % f['_id'])
        for f in outg[n['id']]:
            w('      <bpmn:outgoing>%s</bpmn:outgoing>' % f['_id'])
        if k in TASK_TYPES:
            ins = [d for d, dr in data_links.get(n['id'], []) if dr == 'in']
            outs = [d for d, dr in data_links.get(n['id'], []) if dr == 'out']
            if ins:
                w('      <bpmn:property id="Prop_%s" name="__targetRef_placeholder" />' % n['id'])
            for d in ins:
                w('      <bpmn:dataInputAssociation id="DIA_%s_%s"><bpmn:sourceRef>%s</bpmn:sourceRef>'
                  '<bpmn:targetRef>Prop_%s</bpmn:targetRef></bpmn:dataInputAssociation>'
                  % (n['id'], d['id'], d['id'], n['id']))
            for d in outs:
                w('      <bpmn:dataOutputAssociation id="DOA_%s_%s"><bpmn:targetRef>%s</bpmn:targetRef>'
                  '</bpmn:dataOutputAssociation>' % (n['id'], d['id'], d['id']))
            if n.get('loop'):
                w('      <bpmn:standardLoopCharacteristics id="Loop_%s" />' % n['id'])
            for line in inner_xml(n):
                w('      ' + line)
        if k in EV_TYPES and n.get('ev'):
            ed = EV_DEFS[n['ev']]
            if n['ev'] == 'timer':
                w('      <bpmn:%s id="Def_%s" />' % (ed, n['id']))
            elif n['ev'] == 'conditional':
                w('      <bpmn:%s id="Def_%s"><bpmn:condition xsi:type="bpmn:tFormalExpression">%s'
                  '</bpmn:condition></bpmn:%s>' % (ed, n['id'], x_esc(n.get('name')), ed))
            else:
                w('      <bpmn:%s id="Def_%s" />' % (ed, n['id']))
        w('    </bpmn:%s>' % tag)

    for f in flows:
        sn = L.nodes[f['src']]
        attrs = 'id="%s" sourceRef="%s" targetRef="%s"' % (f['_id'], f['src'], f['tgt'])
        if f.get('name'):
            attrs += ' name="%s"' % x_esc(f['name'])
        cond = sn['kind'] == 'xor' and len(outg[sn['id']]) > 1 and not f.get('default')
        if cond:
            w('    <bpmn:sequenceFlow %s>' % attrs)
            w('      <bpmn:conditionExpression xsi:type="bpmn:tFormalExpression">%s</bpmn:conditionExpression>'
              % x_esc(f.get('cond') or f.get('name') or ''))
            w('    </bpmn:sequenceFlow>')
        else:
            w('    <bpmn:sequenceFlow %s />' % attrs)

    for d in P.get('data', []):
        if d['kind'] == 'store':
            w('    <bpmn:dataStoreReference id="%s" name="%s" />' % (d['id'], x_esc(d['name'])))
        else:
            w('    <bpmn:dataObjectReference id="%s" name="%s" dataObjectRef="DO_%s" />'
              % (d['id'], x_esc(d['name']), d['id']))
            w('    <bpmn:dataObject id="DO_%s" />' % d['id'])
    for a in P.get('annotations', []):
        w('    <bpmn:textAnnotation id="%s"><bpmn:text>%s</bpmn:text></bpmn:textAnnotation>'
          % (a['id'], x_esc(a['text'])))
        w('    <bpmn:association id="Assoc_%s" associationDirection="None" sourceRef="%s" targetRef="%s" />'
          % (a['id'], a['target'], a['id']))
    w('  </bpmn:process>')

    # ---------------------------------------------------------- DI
    def bounds(b):
        return '<dc:Bounds x="%d" y="%d" width="%d" height="%d" />' % (r2(b.x), r2(b.y), r2(b.w), r2(b.h))

    def wps(pts):
        return ''.join('<di:waypoint x="%d" y="%d" />' % (r2(x), r2(y)) for x, y in pts)

    w('  <bpmndi:BPMNDiagram id="Diagram_%s" name="%s">' % (code, x_esc(P['id'] + ' ' + P['name'])))
    w('    <bpmndi:BPMNPlane id="Plane_%s" bpmnElement="Collab_%s">' % (code, code))
    w('      <bpmndi:BPMNShape id="P_MAIN_di" bpmnElement="P_MAIN" isHorizontal="true">%s</bpmndi:BPMNShape>'
      % bounds(Box(POOL_X, L.main_y, L.main_w, L.main_h)))
    for k, _n, _d in P['lanes']:
        w('      <bpmndi:BPMNShape id="Lane_%s_di" bpmnElement="Lane_%s" isHorizontal="true">%s</bpmndi:BPMNShape>'
          % (k, k, bounds(Box(POOL_X + POOL_LABEL, L.lane_y[k], L.main_w - POOL_LABEL, L.lane_h[k]))))
    for key, e in L.ext.items():
        w('      <bpmndi:BPMNShape id="P_%s_di" bpmnElement="P_%s" isHorizontal="true">%s</bpmndi:BPMNShape>'
          % (key, key, bounds(e['box'])))

    routes = dict((f['_id'], L.route(f)) for f in flows)
    used = dict((n['id'], set()) for n in P['nodes'])
    for f in flows:
        pts = routes[f['_id']]
        used[f['src']].add(side_of(L.box[f['src']], pts[0]))
        used[f['tgt']].add(side_of(L.box[f['tgt']], pts[-1]))
    msg_routes = []
    for m in P.get('messages', []):
        pts, pool = L.msg_route(m)
        msg_routes.append((m, pts, pool))
        nid = m['tgt'] if m['src'] in L.ext else m['src']
        used[nid].add('t' if pool['side'] == 'top' else 'b')
    for n in P['nodes']:
        if n.get('attach'):
            used[n['attach']].add('b')

    for n in P['nodes']:
        b = L.box[n['id']]
        extra = ''
        if n['kind'] == 'sub':
            extra = ' isExpanded="false"'
        if n['kind'] == 'xor':
            extra = ' isMarkerVisible="true"'
        lbl = ''
        if cat(n) in ('event', 'gateway') and n.get('name'):
            lbl = '<bpmndi:BPMNLabel>%s</bpmndi:BPMNLabel>' % bounds(label_box_for_node(L, n, used[n['id']]))
        w('      <bpmndi:BPMNShape id="%s_di" bpmnElement="%s"%s>%s%s</bpmndi:BPMNShape>'
          % (n['id'], n['id'], extra, bounds(b), lbl))
    for d in P.get('data', []):
        b = L.box[d['id']]
        lb = Box(b.cx - 50, b.b + 4, 100, 28)
        w('      <bpmndi:BPMNShape id="%s_di" bpmnElement="%s">%s<bpmndi:BPMNLabel>%s</bpmndi:BPMNLabel></bpmndi:BPMNShape>'
          % (d['id'], d['id'], bounds(b), bounds(lb)))
    for a in P.get('annotations', []):
        w('      <bpmndi:BPMNShape id="%s_di" bpmnElement="%s">%s</bpmndi:BPMNShape>'
          % (a['id'], a['id'], bounds(L.box[a['id']])))

    for f in flows:
        pts = routes[f['_id']]
        lbl = ''
        if f.get('name'):
            lbl = '<bpmndi:BPMNLabel>%s</bpmndi:BPMNLabel>' % bounds(flow_label_box(pts, f['name']))
        w('      <bpmndi:BPMNEdge id="%s_di" bpmnElement="%s">%s%s</bpmndi:BPMNEdge>'
          % (f['_id'], f['_id'], wps(pts), lbl))
    for i, (m, pts, pool) in enumerate(msg_routes, 1):
        x = pts[0][0]
        if pool['side'] == 'top':
            gy = (pool['box'].b + L.main_y) / 2.0
        else:
            gy = (L.main_y + L.main_h + pool['box'].y) / 2.0
        lines = int(math.ceil(len(m['name']) / 18.0))
        h = 14 * max(1, lines)
        lb = Box(x + 4, gy - h / 2.0, 118, h) if m['side'] == 'right' else Box(x - 122, gy - h / 2.0, 118, h)
        w('      <bpmndi:BPMNEdge id="MF_%d_di" bpmnElement="MF_%d">%s<bpmndi:BPMNLabel>%s</bpmndi:BPMNLabel></bpmndi:BPMNEdge>'
          % (i, i, wps(pts), bounds(lb)))
    for d in P.get('data', []):
        for nid, direction in d['links']:
            nb, db = L.box[nid], L.box[d['id']]
            p_task = nearest_on_box(nb, (db.cx, db.cy))
            p_data = nearest_on_box(db, (nb.cx, nb.cy))
            if direction == 'out':
                eid, pts = 'DOA_%s_%s' % (nid, d['id']), [p_task, p_data]
            else:
                eid, pts = 'DIA_%s_%s' % (nid, d['id']), [p_data, p_task]
            w('      <bpmndi:BPMNEdge id="%s_di" bpmnElement="%s">%s</bpmndi:BPMNEdge>' % (eid, eid, wps(pts)))
    for a in P.get('annotations', []):
        ab, tb = L.box[a['id']], L.box[a['target']]
        p1 = nearest_on_box(tb, (ab.cx, ab.cy))
        p2 = nearest_on_box(ab, (tb.cx, tb.cy))
        w('      <bpmndi:BPMNEdge id="Assoc_%s_di" bpmnElement="Assoc_%s">%s</bpmndi:BPMNEdge>'
          % (a['id'], a['id'], wps([p1, p2])))
    w('    </bpmndi:BPMNPlane>')
    w('  </bpmndi:BPMNDiagram>')
    for n in P['nodes']:
        for line in inner_di(n):
            w(line)
    w('</bpmn:definitions>')
    return '\n'.join(out) + '\n'


INNER_X, INNER_Y, INNER_GAP = 100, 100, 60


def _inner(n):
    """Các bước tuần tự bên trong quy trình con: [(id, kind, name, doc)], id đã gắn tiền tố."""
    out = []
    for item in n.get('inner', []):
        iid, kind, name = item[:3]
        doc = item[3] if len(item) > 3 else ''
        out.append(('%s_%s' % (n['id'], iid), kind, name, doc))
    return out


def inner_xml(n):
    steps = _inner(n)
    if not steps:
        return []
    lines = []
    for i, (iid, kind, name, doc) in enumerate(steps):
        tag = TASK_TYPES.get(kind) or EV_TYPES[kind]
        lines.append('<bpmn:%s id="%s" name="%s">' % (tag, iid, x_esc(name)))
        if doc:
            lines.append('  <bpmn:documentation>%s</bpmn:documentation>' % x_esc(doc))
        if i > 0:
            lines.append('  <bpmn:incoming>%s_F%d</bpmn:incoming>' % (n['id'], i))
        if i < len(steps) - 1:
            lines.append('  <bpmn:outgoing>%s_F%d</bpmn:outgoing>' % (n['id'], i + 1))
        lines.append('</bpmn:%s>' % tag)
    for i in range(1, len(steps)):
        lines.append('<bpmn:sequenceFlow id="%s_F%d" sourceRef="%s" targetRef="%s" />'
                     % (n['id'], i, steps[i - 1][0], steps[i][0]))
    return lines


def inner_di(n):
    """Mặt phẳng riêng cho quy trình con thu gọn (mở bằng cách bấm vào ô trong công cụ BPMN)."""
    steps = _inner(n)
    if not steps:
        return []
    lines = ['  <bpmndi:BPMNDiagram id="Diagram_%s">' % n['id'],
             '    <bpmndi:BPMNPlane id="Plane_%s" bpmnElement="%s">' % (n['id'], n['id'])]
    x, cy, boxes = INNER_X, INNER_Y + SIZES['task'][1] / 2.0, []
    for iid, kind, name, _doc in steps:
        w, h = SIZES['task'] if kind in TASK_TYPES else SIZES['event']
        b = Box(x, cy - h / 2.0, w, h)
        boxes.append(b)
        label = ''
        if kind in EV_TYPES:
            label = '<bpmndi:BPMNLabel><dc:Bounds x="%d" y="%d" width="100" height="28" /></bpmndi:BPMNLabel>' % (
                r2(b.cx - 50), r2(b.b + 6))
        lines.append('      <bpmndi:BPMNShape id="%s_di" bpmnElement="%s"><dc:Bounds x="%d" y="%d" width="%d" height="%d" />%s'
                     '</bpmndi:BPMNShape>' % (iid, iid, r2(b.x), r2(b.y), r2(b.w), r2(b.h), label))
        x += w + INNER_GAP
    for i in range(1, len(steps)):
        a, b = boxes[i - 1], boxes[i]
        lines.append('      <bpmndi:BPMNEdge id="%s_F%d_di" bpmnElement="%s_F%d"><di:waypoint x="%d" y="%d" />'
                     '<di:waypoint x="%d" y="%d" /></bpmndi:BPMNEdge>'
                     % (n['id'], i, n['id'], i, r2(a.r), r2(a.cy), r2(b.x), r2(b.cy)))
    lines += ['    </bpmndi:BPMNPlane>', '  </bpmndi:BPMNDiagram>']
    return lines


def nearest_on_box(b, pt):
    """Điểm trên cạnh hộp b gần nhất theo hướng tới pt (cắt tia từ tâm)."""
    dx, dy = pt[0] - b.cx, pt[1] - b.cy
    if dx == 0 and dy == 0:
        return (b.cx, b.y)
    sx = (b.w / 2.0) / abs(dx) if dx else float('inf')
    sy = (b.h / 2.0) / abs(dy) if dy else float('inf')
    s = min(sx, sy)
    return (b.cx + dx * s, b.cy + dy * s)


# ---------------------------------------------------------------- tài liệu
def md_cell(s):
    return (s or '').replace('|', '\\|').replace('\n', '<br>')


def build_md(P, L):
    lanes = dict((k, (name, desc)) for k, name, desc in P['lanes'])
    lane_order = dict((k, i) for i, k in enumerate(L.lane_keys))
    out = []
    w = out.append
    w('# %s — %s' % (P['id'], P['name']))
    w('')
    w('> Sinh tự động từ `defs/%s` bằng bpmn-kit — sửa định nghĩa rồi chạy lại, '
      'không sửa tay file này.' % P['_file'])
    w('')
    w('![%s](../svg/%s.svg)' % (P['id'], P['_slug']))
    w('')
    w('File BPMN 2.0: [`bpmn/%s.bpmn`](../bpmn/%s.bpmn) · Ảnh: [`png/%s.png`](../png/%s.png)'
      % (P['_slug'], P['_slug'], P['_slug'], P['_slug']))
    w('')
    w('## 1. Thông tin chung')
    w('')
    w('| Mục | Nội dung |')
    w('|---|---|')
    for label, key in [('Mục tiêu', 'objective'), ('Sự kiện kích hoạt', 'trigger'),
                       ('Kết quả đầu ra', 'outcome'), ('Phạm vi', 'scope'),
                       ('Ngoài phạm vi', 'out_of_scope'), ('Module ERP', 'modules'),
                       ('Quy trình chuẩn ERP tương ứng', 'erp_standard'),
                       ('Quy trình đầu vào', 'upstream'), ('Quy trình tiếp theo', 'downstream')]:
        v = P.get(key)
        if not v:
            continue
        if isinstance(v, (list, tuple)):
            v = '; '.join(v)
        w('| %s | %s |' % (label, md_cell(v)))
    w('')
    w('## 2. Vai trò (làn)')
    w('')
    w('| Làn | Vai trò | Trách nhiệm trong quy trình |')
    w('|---|---|---|')
    for k, name, desc in P['lanes']:
        w('| `%s` | %s | %s |' % (k, md_cell(name), md_cell(desc)))
    if P.get('pools'):
        w('')
        w('Bên ngoài (pool hộp đen, trao đổi bằng luồng thông điệp): ' +
          '; '.join('**%s**' % e['name'] for e in P['pools']) + '.')
    w('')
    w('## 3. Các bước')
    w('')
    w('| # | ID | Bước | Làn | Loại | Mô tả | Chứng từ / trạng thái | Kiểm soát |')
    w('|---|---|---|---|---|---|---|---|')
    # cổng gộp nhánh không tên chỉ là cú pháp BPMN, không phải một bước nghiệp vụ
    steps = [n for n in P['nodes'] if not (cat(n) == 'gateway' and not n.get('name'))]
    order = sorted(steps, key=lambda n: (n['col'], lane_order[n['lane']], n['row'],
                                         1 if n['kind'] == 'boundary' else 0))
    for i, n in enumerate(order, 1):
        kind = KIND_LABEL[n['kind']]
        if n.get('ev'):
            kind += ' (%s)' % EV_LABEL[n['ev']]
        if n['kind'] == 'boundary':
            kind += ' trên %s%s' % (n['attach'], ', không ngắt' if n.get('interrupting') is False else '')
        if n['kind'] == 'call' and n.get('called'):
            kind += ' → %s' % n['called']
        if n.get('loop'):
            kind += ' (lặp)'
        ctrl = ', '.join(n.get('ctrl', []))
        w('| %d | `%s` | %s | %s | %s | %s | %s | %s |' % (
            i, n['id'], md_cell(n.get('name')), md_cell(lanes[n['lane']][0]), kind,
            md_cell(n.get('doc', '')), md_cell(n.get('docs', '')), ctrl))
    for n in P['nodes']:
        steps = _inner(n)
        if not steps:
            continue
        w('')
        w('Bên trong quy trình con `%s` %s (mở bằng cách bấm vào ô trong công cụ BPMN):' % (n['id'], n.get('name')))
        w('')
        w('| ID | Bước | Loại | Mô tả |')
        w('|---|---|---|---|')
        for iid, kind, name, doc in steps:
            w('| `%s` | %s | %s | %s |' % (iid, md_cell(name), KIND_LABEL[kind], md_cell(doc)))
    gws = [n for n in P['nodes'] if n['kind'] in ('xor', 'evt') and
           len([f for f in P['flows'] if f['src'] == n['id']]) > 1]
    if gws:
        w('')
        w('## 4. Điểm quyết định')
        w('')
        w('| Cổng | Câu hỏi / điều kiện | Nhánh → bước tiếp theo |')
        w('|---|---|---|')
        for g in gws:
            br = []
            for f in P['flows']:
                if f['src'] != g['id']:
                    continue
                t = L.nodes[f['tgt']]
                # đi qua các cổng gộp không tên tới bước nghiệp vụ đầu tiên
                seen = set()
                while cat(t) == 'gateway' and not t.get('name') and t['id'] not in seen:
                    seen.add(t['id'])
                    nxt = [x for x in P['flows'] if x['src'] == t['id']]
                    if len(nxt) != 1:
                        break
                    t = L.nodes[nxt[0]['tgt']]
                br.append('%s%s → `%s` %s' % (f.get('name') or '(sự kiện)', ' (mặc định)' if f.get('default') else '',
                                              t['id'], t.get('name') or ''))
            w('| `%s` | %s | %s |' % (g['id'], md_cell(g.get('name')), md_cell('\n'.join(br))))
    if P.get('messages'):
        w('')
        w('## 5. Trao đổi với bên ngoài')
        w('')
        w('| Từ | Đến | Thông điệp |')
        w('|---|---|---|')
        names = dict((e['key'], e['name']) for e in P.get('pools', []))
        for m in P['messages']:
            s = names.get(m['src']) or '`%s` %s' % (m['src'], L.nodes[m['src']].get('name'))
            t = names.get(m['tgt']) or '`%s` %s' % (m['tgt'], L.nodes[m['tgt']].get('name'))
            w('| %s | %s | %s |' % (md_cell(s), md_cell(t), md_cell(m['name'])))
    sec = 6
    for title, key, header in [
        ('Kiểm soát nội bộ', 'controls', ('Mã', 'Kiểm soát', 'Loại', 'Nguồn')),
        ('Chứng từ & trạng thái', 'documents', ('Chứng từ', 'Trạng thái chuẩn', 'Ghi chú')),
        ('Bút toán phát sinh', 'postings', ('Nghiệp vụ', 'Nợ', 'Có', 'Ghi chú')),
        ('Tham số hệ thống gợi ý', 'parameters', ('Tham số', 'Ý nghĩa', 'Mặc định gợi ý')),
        ('Chỉ số đo (KPI)', 'kpis', ('Chỉ số', 'Cách tính', 'Mục tiêu gợi ý')),
    ]:
        rows = P.get(key)
        if not rows:
            continue
        w('')
        w('## %d. %s' % (sec, title))
        sec += 1
        w('')
        w('| ' + ' | '.join(header) + ' |')
        w('|' + '---|' * len(header))
        for r in rows:
            w('| ' + ' | '.join(md_cell(c) for c in r) + ' |')
    if P.get('extra_md'):
        w('')
        w(P['extra_md'].replace('{sec}', str(sec)))
        sec += 1
    for title, key in [('Căn cứ từ sách', 'references'), ('Điểm cần xác nhận với doanh nghiệp', 'questions')]:
        items = P.get(key)
        if not items:
            continue
        w('')
        w('## %d. %s' % (sec, title))
        sec += 1
        w('')
        for it in items:
            w('- ' + it)
    return '\n'.join(out) + '\n'


# ---------------------------------------------------------------- main
def load_defs(only=None):
    # defs import "bpmn_gen": trỏ về chính module đang chạy để dùng chung REG và ROOT
    sys.modules.setdefault('bpmn_gen', sys.modules[__name__])
    defs = os.path.join(ROOT, 'defs')
    if defs not in sys.path:
        sys.path.insert(0, defs)
    procs = []
    for path in sorted(glob.glob(os.path.join(defs, 'bp*.py'))):
        spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        P = mod.PROCESS
        P['_file'] = os.path.basename(path)
        P['_slug'] = P.get('slug') or (slug(P['id']) if P['id'] in REG['processes'] else P['id'])
        if only and P['id'] not in only:
            continue
        procs.append(P)
    return procs


def validate_refs(P):
    errs = []
    ids = set(n['id'] for n in P['nodes'])
    pools = set(e['key'] for e in P.get('pools', []))
    for f in P['flows']:
        for e in (f['src'], f['tgt']):
            if e not in ids:
                errs.append('Luồng tham chiếu phần tử không tồn tại: %s' % e)
    for m in P.get('messages', []):
        for e in (m['src'], m['tgt']):
            if e not in ids and e not in pools:
                errs.append('Thông điệp tham chiếu không tồn tại: %s' % e)
        if (m['src'] in pools) == (m['tgt'] in pools):
            errs.append('Thông điệp phải nối một phần tử với một pool ngoài: %s→%s' % (m['src'], m['tgt']))
    for a in P.get('annotations', []):
        if a['target'] not in ids:
            errs.append('Chú thích %s trỏ tới phần tử không tồn tại %s' % (a['id'], a['target']))
    for d in P.get('data', []):
        for nid, _ in d['links']:
            if nid not in ids:
                errs.append('Dữ liệu %s nối tới phần tử không tồn tại %s' % (d['id'], nid))
    for n in P['nodes']:
        if n['kind'] == 'boundary' and n.get('attach') not in ids:
            errs.append('Sự kiện biên %s không gắn vào phần tử hợp lệ' % n['id'])
        for c in n.get('ctrl', []):
            if c not in [r[0] for r in P.get('controls', [])]:
                errs.append('%s tham chiếu kiểm soát chưa khai báo: %s' % (n['id'], c))
    return errs


VIEWER = '''<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Bộ quy trình BPMN — ERP điều hành tour</title>
<!-- Sinh tự động bởi bpmn-kit. Cần chạy qua HTTP: python3 -m http.server 8000 rồi mở http://localhost:8000/viewer.html -->
<link rel="stylesheet" href="{{NM}}/bpmn-js/dist/assets/diagram-js.css">
<link rel="stylesheet" href="{{NM}}/bpmn-js/dist/assets/bpmn-js.css">
<link rel="stylesheet" href="{{NM}}/bpmn-js/dist/assets/bpmn-font/css/bpmn.css">
<style>
  html, body { margin: 0; height: 100%%; font-family: system-ui, sans-serif; }
  header { display: flex; gap: 12px; align-items: center; padding: 8px 12px; border-bottom: 1px solid #ddd; font-size: 14px; }
  header select { font-size: 14px; padding: 4px; }
  header .hint { color: #666; margin-left: auto; }
  #canvas { position: absolute; top: 46px; bottom: 0; left: 0; right: 0; }
  #err { color: #b00; }
</style>
</head>
<body>
<header>
  <select id="pick"></select>
  <a id="doc" href="#">Tài liệu</a>
  <a id="dl" href="#" download>Tải .bpmn</a>
  <span id="err"></span>
  <span class="hint">Cuộn chuột để phóng to, kéo để di chuyển, bấm biểu tượng ở góc ô quy trình con để mở bên trong</span>
</header>
<div id="canvas"></div>
<script src="{{NM}}/bpmn-js/dist/bpmn-navigated-viewer.production.min.js"></script>
<script>
  const FILES = %s;
  const pick = document.getElementById('pick');
  FILES.forEach(([slug, title]) => pick.add(new Option(title, slug)));
  const viewer = new BpmnJS({ container: '#canvas' });
  async function show(slug) {
    document.getElementById('doc').href = 'docs/' + slug + '.md';
    document.getElementById('dl').href = 'bpmn/' + slug + '.bpmn';
    try {
      const xml = await (await fetch('bpmn/' + slug + '.bpmn')).text();
      await viewer.importXML(xml);
      viewer.get('canvas').zoom('fit-viewport');
      document.getElementById('err').textContent = '';
      location.hash = slug;
    } catch (e) {
      document.getElementById('err').textContent = 'Không mở được: ' + e.message;
    }
  }
  pick.onchange = () => show(pick.value);
  const start = location.hash.slice(1) || FILES[0][0];
  pick.value = start;
  show(start);
</script>
</body>
</html>
'''


def write_questions(procs):
    """Gom mục "Điểm cần xác nhận" của mọi quy trình thành một bộ câu hỏi khảo sát mang đi gặp khách hàng."""
    out = ['# Bộ câu hỏi khảo sát khách hàng', '',
           '> Sinh tự động từ mục "Điểm cần xác nhận" của từng quy trình (bpmn-kit). Mọi nội dung trong bộ sơ đồ là '
           '**đề xuất theo chuẩn ERP**, chưa được khách hàng xác nhận. Dùng danh sách này cho buổi khảo sát; câu trả lời '
           'nào khác đề xuất thì sửa định nghĩa quy trình rồi sinh lại.', '']
    n = 0
    for P in procs:
        qs = P.get('questions') or []
        params = P.get('parameters') or []
        if not qs and not params:
            continue
        out.append('## %s — %s' % (P['id'], P['name']))
        out.append('')
        out.append('Sơ đồ: [%s](docs/%s.md)' % (P['id'], P['_slug']))
        out.append('')
        for q in qs:
            n += 1
            out.append('%d. %s' % (n, q))
        if params:
            out.append('')
            out.append('Tham số đang dùng giá trị đề xuất — xác nhận con số của doanh nghiệp:')
            out.append('')
            out.append('| Tham số | Ý nghĩa | Đề xuất | Doanh nghiệp xác nhận |')
            out.append('|---|---|---|---|')
            for name, meaning, default in params:
                out.append('| %s | %s | %s | |' % (md_cell(name), md_cell(meaning), md_cell(default)))
        out.append('')
    with open(os.path.join(ROOT, 'CAU-HOI-KHAO-SAT.md'), 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(out) + '\n')


def write_viewer(procs):
    import json
    files = [[P['_slug'], '%s — %s' % (P['id'], P['name'])] for P in procs]
    with open(os.path.join(ROOT, 'viewer.html'), 'w', encoding='utf-8') as fh:
        nm = os.path.relpath(os.path.join(KIT, 'node_modules'), ROOT)
        fh.write((VIEWER % json.dumps(files, ensure_ascii=False)).replace('{{NM}}', nm))


def main(argv):
    global ROOT
    if len(argv) < 2 or not os.path.isdir(os.path.join(argv[1], 'defs')):
        print('Dùng: python3 bpmn_gen.py <thư-mục-dự-án có defs/> [BP-xx ...]')
        return 2
    ROOT = os.path.abspath(argv[1])
    for sub in ('bpmn', 'docs', 'svg', 'png'):
        os.makedirs(os.path.join(ROOT, sub), exist_ok=True)
    only = set(argv[2:]) or None
    procs = load_defs(only)
    if not only:
        write_viewer(procs)
        write_questions(procs)
    total_warn = 0
    for P in procs:
        errs = validate_refs(P)
        if errs:
            print('[%s] LỖI:\n  - %s' % (P['id'], '\n  - '.join(errs)))
            sys.exit(1)
        L = Layout(P)
        L.check()
        xml = build_xml(P, L)
        md = build_md(P, L)
        with open(os.path.join(ROOT, 'bpmn', P['_slug'] + '.bpmn'), 'w', encoding='utf-8') as fh:
            fh.write(xml)
        with open(os.path.join(ROOT, 'docs', P['_slug'] + '.md'), 'w', encoding='utf-8') as fh:
            fh.write(md)
        status = 'OK' if not L.warnings else '%d cảnh báo' % len(L.warnings)
        print('[%s] %s — %d phần tử, %d luồng — %s' % (P['id'], P['_slug'], len(P['nodes']), len(P['flows']), status))
        for wmsg in L.warnings:
            print('    ! ' + wmsg)
        total_warn += len(L.warnings)
    return 1 if total_warn else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
