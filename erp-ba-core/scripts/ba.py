#!/usr/bin/env python3
"""ba.py — công cụ kiểm soát chất lượng cho skill erp-ba-core (chỉ dùng thư viện chuẩn Python 3.8+).

Lệnh:
  init <root> --project TÊN            Tạo workspace tài liệu từ template
  new-meeting <root> [--date YYYY-MM-DD]
                                        Tạo file biên bản họp MTG kế tiếp
  new-function <root> --id FN-PUR-03 --name "Tên" [--type "Chứng từ"]
                                        Tạo file đặc tả chức năng (type "Báo cáo" dùng template báo cáo)
  lint <root> [--json] [--no-write]     Kiểm tra placeholder, marker, ID trùng/thiếu, cấu trúc, sơ đồ Mermaid,
                                        từ mơ hồ, nguồn, nhất quán catalog. Ghi <root>/lint-report.md
  trace <root> [--json] [--no-write]    Ma trận truy vết REQ → FN → FR/US/AC; phát hiện thiếu/thừa.
                                        Ghi <root>/traceability.md
  checklist <root> --step {1,2,3,3F,3R,4,5,all} --round N [--fn FN-...] [--out FILE]
                                        Sinh bảng checklist Yes/No để điền (vào báo cáo tự kiểm/review)
  status <report.md>                    Đếm Yes/No/N/A, phát hiện còn mở → PASS/FAIL

Mã thoát: 0 = đạt, 1 = còn lỗi (Error) / FAIL, 2 = dùng sai lệnh.
"""
import argparse
import datetime as _dt
import json
import os
import re
import shutil
import sys
import unicodedata
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent          # erp-ba-core
# Bộ skill: erp-ba-core + erp-ba-step1..5 nằm cùng một thư mục cha (có thể đặt lại bằng biến ERP_BA_SUITE_ROOT).
SUITE_ROOT = Path(os.environ.get("ERP_BA_SUITE_ROOT", str(SKILL_DIR.parent)))


def _step_skills():
    return sorted(p for p in SUITE_ROOT.glob("erp-ba-step*") if p.is_dir())


def template_roots():
    roots = [d / "assets" / "templates" for d in _step_skills()] + [SKILL_DIR / "assets" / "templates"]
    return [r for r in roots if r.exists()]


def all_templates():
    """(root, path) của mọi template; cùng đường dẫn tương đối thì root đứng trước được dùng."""
    seen = set()
    for r in template_roots():
        for t in sorted(r.rglob("*.md")):
            k = str(t.relative_to(r))
            if k not in seen:
                seen.add(k)
                yield r, t


def find_template(relpath):
    for r in template_roots():
        if (r / relpath).exists():
            return r / relpath
    raise SystemExit(f"Không tìm thấy template '{relpath}'. Cần cài đủ bộ skill erp-ba-step1…5 cạnh erp-ba-core "
                     f"(thư mục cha hiện tại: {SUITE_ROOT}; có thể đặt biến ERP_BA_SUITE_ROOT).")


def checklist_dirs():
    dirs = [d / "references" / "checklists" for d in _step_skills()] + [SKILL_DIR / "references" / "checklists"]
    return [d for d in dirs if d.exists()]


def find_checklist(name):
    for d in checklist_dirs():
        if (d / name).exists():
            return d / name
    raise SystemExit(f"Không tìm thấy checklist '{name}' trong các skill bước (thư mục cha: {SUITE_ROOT}).")


GENERATED = {"traceability.md", "lint-report.md"}
# Template không copy khi init (dùng cho lệnh tạo mới)
NON_INIT_TEMPLATES = {
    "00-inputs/meeting-notes.md",
    "03-specification/function-spec.md",
    "03-specification/report-spec.md",
    "04-verification/verify-report.md",
    "05-review/review-report.md",
}

# ---------------------------------------------------------------- ID ----------
ID_PATTERNS = {
    "SRC": r"SRC-\d{3,}",
    "MTG": r"MTG-\d{3,}",
    "FEAT": r"FEAT-[A-Z]{2,5}-\d{2,}",
    "REQ": r"REQ-\d{3,}",
    "BO": r"BO-\d{2,}",
    "BP": r"BP-\d{2,}",
    "MOD": r"MOD-[A-Z]{2,5}",
    "FN": r"FN-[A-Z]{2,5}-\d{2,}",
    "FR": r"FR-[A-Z]{2,5}-\d{2,}-\d{2,}",
    "BR": r"BR-(?:GEN-\d{2,}|[A-Z]{2,5}-\d{2,}-\d{2,})",
    "US": r"US-[A-Z]{2,5}-\d{2,}-\d{2,}",
    "AC": r"AC-[A-Z]{2,5}-\d{2,}-\d{2,}",
    "MSG": r"MSG-[A-Z]{2,5}-\d{2,}-\d{2,}",
    "NFR": r"NFR-[A-Z]{2,5}-\d{2,}(?:-\d{2,})?",
    "ROLE": r"ROLE-[A-Z0-9]+(?:-[A-Z0-9]+)*",
    "PRM": r"PRM-[A-Z]{2,5}-\d{3,}",
    "MD": r"MD-[A-Z0-9]+(?:-[A-Z0-9]+)*",
    "DOC": r"DOC-[A-Z0-9]+(?:-[A-Z0-9]+)*",
    "RPT": r"RPT-[A-Z]{2,5}-\d{2,}",
    "INT": r"INT-\d{2,}",
    "NTF": r"NTF-[A-Z]{2,5}-\d{2,}",
    "SOD": r"SOD-\d{2,}",
    "Q": r"Q-\d{3,}",
    "ASM": r"ASM-\d{3,}",
    "DEC": r"DEC-\d{3,}",
    "CFL": r"CFL-\d{3,}",
    "CHG": r"CHG-\d{3,}",
    "VF": r"VF-R\d+-\d{2,}",
    "RV": r"RV-R\d+-\d{2,}",
}
ID_RE = re.compile(
    r"(?<![A-Za-z0-9_\-])(" + "|".join(ID_PATTERNS.values()) + r")(?![A-Za-z0-9_])"
)


def id_kind(i):
    """Loại ID dùng để tra nơi định nghĩa (phân biệt BR-GEN và NFR chung)."""
    p = i.split("-")[0]
    if p == "BR":
        return "BR-GEN" if i.startswith("BR-GEN-") else "BR-FN"
    if p == "NFR":
        return "NFR-FN" if len(i.split("-")) == 4 else "NFR-GEN"
    return p


SPEC = "03-specification"
DEF_LOC = {
    "SRC": ["00-inputs/source-register.md"],
    "MTG": ["00-inputs/source-register.md"],
    "FEAT": ["01-research/feature-catalog.md"],
    "REQ": ["02-requirements/requirement-register.md"],
    "BO": ["02-requirements/requirements-overview.md"],
    "BP": ["02-requirements/requirements-overview.md"],
    "Q": ["02-requirements/issue-log.md"],
    "ASM": ["02-requirements/issue-log.md"],
    "DEC": ["02-requirements/issue-log.md"],
    "CFL": ["02-requirements/issue-log.md"],
    "CHG": ["02-requirements/issue-log.md"],
    "MOD": [SPEC + "/srs-overview.md"],
    "BR-GEN": [SPEC + "/srs-overview.md"],
    "NFR-GEN": [SPEC + "/srs-overview.md"],
    "ROLE": [SPEC + "/catalogs/roles-permissions.md"],
    "SOD": [SPEC + "/catalogs/roles-permissions.md"],
    "MD": [SPEC + "/catalogs/master-data.md"],
    "DOC": [SPEC + "/catalogs/document-types.md"],
    "PRM": [SPEC + "/catalogs/system-parameters.md"],
    "RPT": [SPEC + "/catalogs/reports.md"],
    "INT": [SPEC + "/catalogs/integrations-notifications.md"],
    "NTF": [SPEC + "/catalogs/integrations-notifications.md"],
    "FN": [SPEC + "/functions/"],
    "FR": [SPEC + "/functions/"],
    "BR-FN": [SPEC + "/functions/"],
    "US": [SPEC + "/functions/"],
    "AC": [SPEC + "/functions/"],
    "MSG": [SPEC + "/functions/"],
    "NFR-FN": [SPEC + "/functions/"],
    "VF": ["04-verification/"],
    "RV": ["05-review/"],
}

CANONICAL_STATUSES = [
    "DRAFT", "PENDING", "RETURNED", "REJECTED", "APPROVED", "IN_PROGRESS",
    "PARTIAL", "COMPLETED", "POSTED", "CLOSED", "CANCELLED", "REVERSED",
    "ACTIVE", "INACTIVE", "LOCKED",
]

VAGUE_RE = re.compile(
    r"(?<!\w)(nhanh chóng|nhanh|chậm|dễ dùng|dễ sử dụng|thân thiện|linh hoạt|tối ưu|hợp lý|phù hợp|"
    r"v\.v\.?|vv\.|tương tự|một số|thường xuyên|khi cần|nếu có thể|kịp thời|real-?time|hiệu quả|"
    r"trực quan|đơn giản|có thể|nhiều(?! nhất)|ít(?! nhất))(?!\w)",
    re.IGNORECASE,
)
PLACEHOLDER_RE = re.compile(r"\{\{.*?\}\}")
FORBIDDEN_RE = re.compile(r"(?<!\w)(TODO|TBD|FIXME)(?!\w)|\?\?\?|(?<!\w)xxx(?!\w)", re.IGNORECASE)
MARK_CONFIRM_RE = re.compile(r"\[CẦN XÁC NHẬN(?::\s*(Q-\d{3,}))?\s*\]")
MARK_PROPOSE_RE = re.compile(r"\[ĐỀ XUẤT(?:\s*(?:→|->)\s*((?:Q|DEC)-\d{3,}))?\s*\]")
MARK_ASSUME_RE = re.compile(r"\[GIẢ ĐỊNH(?::\s*(ASM-\d{3,}))?\s*\]")
NA_RE = re.compile(r"(?<!\w)(N/A|Không áp dụng)(?!\w)")
NA_OK_RE = re.compile(r"(?<!\w)(N/A|Không áp dụng)\s*[–—\-:]\s*\S")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
FENCE_RE = re.compile(r"^\s*```")


# ------------------------------------------------------------ helpers -------
def nfc(s):
    return unicodedata.normalize("NFC", s)


def today():
    return _dt.date.today().isoformat()


def read(p):
    return nfc(Path(p).read_text(encoding="utf-8"))


def strip_comments(text):
    """Xóa HTML comment nhưng giữ nguyên số dòng."""
    def repl(m):
        return "\n" * m.group(0).count("\n")
    return re.sub(r"<!--.*?-->", repl, text, flags=re.S)


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
    return fm


def split_row(line):
    s = line.strip()
    if not s.startswith("|"):
        return None
    s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    cells, cur, esc = [], "", False
    for ch in s:
        if ch == "\\" and not esc:
            esc = True
            cur += ch
            continue
        if ch == "|" and not esc:
            cells.append(cur.strip())
            cur = ""
        else:
            cur += ch
        esc = False
    cells.append(cur.strip())
    return cells


def is_sep_row(cells):
    return cells is not None and all(re.fullmatch(r":?-{2,}:?", c or "") for c in cells if c != "") and any(cells)


def iter_tables(lines):
    """Trả về list bảng: {'start': idx, 'header': [...], 'rows': [(lineno, cells)]}."""
    tables, i, n = [], 0, len(lines)
    in_fence = False
    while i < n:
        if FENCE_RE.match(lines[i]):
            in_fence = not in_fence
            i += 1
            continue
        if in_fence:
            i += 1
            continue
        hdr = split_row(lines[i])
        if hdr is not None and i + 1 < n and is_sep_row(split_row(lines[i + 1])):
            t = {"start": i + 1, "header": hdr, "rows": []}
            j = i + 2
            while j < n:
                r = split_row(lines[j])
                if r is None:
                    break
                t["rows"].append((j + 1, r))
                j += 1
            tables.append(t)
            i = j
            continue
        i += 1
    return tables


def col_index(header, *keywords):
    """Tìm cột theo từ khóa; từ khóa bắt đầu bằng 're:' là biểu thức chính quy."""
    for k in keywords:
        for idx, h in enumerate(header):
            if k.startswith("re:"):
                if re.search(k[3:], h):
                    return idx
            elif k.lower() in h.lower():
                return idx
    return None


def headings(lines):
    out, in_fence = [], False
    for idx, line in enumerate(lines):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING_RE.match(line)
        if m:
            out.append((idx, len(m.group(1)), m.group(2).strip()))
    return out


def sections_by_number(lines, level=2):
    """{'4': (start_idx, end_idx)} cho các tiêu đề dạng '## 4. ...'."""
    hs = headings(lines)
    res = {}
    for k, (idx, lvl, title) in enumerate(hs):
        if lvl != level:
            continue
        m = re.match(r"(\d+)\.", title)
        if not m:
            continue
        end = len(lines)
        for idx2, lvl2, _ in hs[k + 1:]:
            if lvl2 <= level:
                end = idx2
                break
        res[m.group(1)] = (idx, end)
    return res


def mermaid_blocks(lines):
    """[(start_line_idx, end_line_idx, [lines])] cho các khối ```mermaid."""
    out, i, n = [], 0, len(lines)
    while i < n:
        if re.match(r"^\s*```\s*mermaid\s*$", lines[i]):
            j = i + 1
            while j < n and not FENCE_RE.match(lines[j]):
                j += 1
            out.append((i, j, lines[i + 1:j]))
            i = j + 1
            continue
        i += 1
    return out


def md_files(root):
    for p in sorted(Path(root).rglob("*.md")):
        if p.name in GENERATED and p.parent == Path(root):
            continue
        if "files" in p.relative_to(root).parts[:2] and p.relative_to(root).parts[0] == "00-inputs":
            continue
        yield p


def rel(root, p):
    return str(Path(p).relative_to(root)).replace("\\", "/")


def in_def_loc(relpath, kind):
    for loc in DEF_LOC.get(kind, []):
        if loc.endswith("/"):
            if relpath.startswith(loc):
                return True
        elif relpath == loc:
            return True
    return False


def ids_in(text):
    text = PLACEHOLDER_RE.sub(" ", text)
    return [m.group(1) for m in ID_RE.finditer(text)]


# ------------------------------------------------------------ mermaid -------
DIAGRAM_TYPES = (
    "flowchart", "graph", "sequenceDiagram", "stateDiagram-v2", "stateDiagram", "erDiagram",
    "classDiagram", "gantt", "journey", "pie", "mindmap", "timeline", "gitGraph", "quadrantChart",
    "requirementDiagram", "C4Context", "sankey-beta", "xychart-beta", "block-beta",
)
SHAPES = [("(((", ")))"), ("([", "])"), ("[[", "]]"), ("[(", ")]"), ("((", "))"), ("{{", "}}"),
          ("[/", "/]"), ("[\\", "\\]"), ("[", "]"), ("(", ")"), ("{", "}")]
NODE_START_RE = re.compile(r"(?<![A-Za-z0-9_\-\.>|\"])([A-Za-z_][A-Za-z0-9_]*)\s*(?=[\[\(\{])")
SPECIAL = set('()[]{}|<>;#&"')


def _label_issues(content, where):
    issues = []
    c = content.strip()
    if len(c) >= 2 and c[0] == '"' and c[-1] == '"':
        if '"' in c[1:-1]:
            issues.append(("E", "MERMAID", where + ": nhãn chứa dấu ngoặc kép bên trong"))
    else:
        if any(ch in SPECIAL for ch in c):
            issues.append(("E", "MERMAID", where + f": nhãn có ký tự đặc biệt phải đặt trong ngoặc kép: {c[:60]}"))
        elif any(ord(ch) > 127 for ch in c):
            issues.append(("W", "MERMAID", where + f": nên đặt nhãn tiếng Việt trong ngoặc kép: {c[:60]}"))
    return issues


def check_flowchart(body, base):
    issues = []
    opens = sum(1 for _, l in body if re.match(r"^\s*subgraph\b", l))
    ends = sum(1 for _, l in body if re.match(r"^\s*end\s*;?\s*$", l))
    if opens != ends:
        issues.append(("E", "MERMAID", f"dòng {base}: số 'subgraph' ({opens}) khác số 'end' ({ends})"))
    for ln, line in body:
        s = line.strip()
        if not s or s.startswith("%%") or re.match(r"^(classDef|class|style|linkStyle|click|direction)\b", s):
            continue
        if re.match(r"^end\s*;?$", s):
            continue
        if re.search(r"(?<![A-Za-z0-9_])end\s*[\[\(\{]", s):
            issues.append(("E", "MERMAID", f"dòng {ln}: không dùng 'end' làm id nút"))
        # nhãn cạnh |...|
        for m in re.finditer(r"\|([^|]*)\|", s):
            lab = m.group(1)
            issues += [(lv, c, msg) for lv, c, msg in _label_issues(lab, f"dòng {ln} (nhãn cạnh)") if lv == "E"]
        # nhãn nút
        pos = 0
        while True:
            m = NODE_START_RE.search(s, pos)
            if not m:
                break
            k = m.end()
            opener = closer = None
            for o, c in SHAPES:
                if s.startswith(o, k):
                    opener, closer = o, c
                    break
            if not opener:
                pos = k
                continue
            start = k + len(opener)
            if s[start:start + 1] == '"':
                q = s.find('"', start + 1)
                if q == -1:
                    issues.append(("E", "MERMAID", f"dòng {ln}: thiếu dấu ngoặc kép đóng"))
                    break
                end = s.find(closer, q + 1)
            else:
                end = s.find(closer, start)
            if end == -1:
                issues.append(("E", "MERMAID", f"dòng {ln}: thiếu ký tự đóng '{closer}' cho nút {m.group(1)}"))
                break
            issues += _label_issues(s[start:end], f"dòng {ln}")
            pos = end + len(closer)
    return issues


def check_sequence(body, base):
    issues, depth = [], 0
    for ln, line in body:
        s = line.strip()
        if re.match(r"^(alt|opt|loop|par|critical|break|rect|box)\b", s):
            depth += 1
        elif re.match(r"^end\s*$", s):
            depth -= 1
            if depth < 0:
                issues.append(("E", "MERMAID", f"dòng {ln}: 'end' thừa"))
                depth = 0
        if re.search(r"(->>|-->>|->|-->|-x|--x|-\)|--\))", s) and ":" in s:
            msg = s.split(":", 1)[1]
            if ";" in msg:
                issues.append(("E", "MERMAID", f"dòng {ln}: dấu ';' trong thông điệp sequence bị hiểu là xuống dòng"))
            if "#" in msg:
                issues.append(("W", "MERMAID", f"dòng {ln}: ký tự '#' trong thông điệp có thể lỗi hiển thị"))
    if depth != 0:
        issues.append(("E", "MERMAID", f"dòng {base}: khối alt/opt/loop/par chưa đóng đủ 'end'"))
    return issues


def _brace_delta(s):
    if re.search(r"\{\s*$", s):
        return 1
    if re.fullmatch(r"\}\s*", s):
        return -1
    return 0


def check_state(body, base):
    issues, depth = [], 0
    for ln, line in body:
        s = line.strip()
        if not s or s.startswith("%%"):
            continue
        depth += _brace_delta(s)
        m = re.match(r"^(\S+)\s*-->\s*(\S+?)(\s*:.*)?$", s)
        if m:
            for sid in (m.group(1), m.group(2)):
                if sid != "[*]" and not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", sid):
                    issues.append(("E", "MERMAID", f"dòng {ln}: id trạng thái '{sid}' phải là chữ ASCII không dấu (dùng state \"Nhãn\" as ID)"))
            if m.group(3) and ";" in m.group(3):
                issues.append(("E", "MERMAID", f"dòng {ln}: không dùng ';' trong nhãn chuyển trạng thái"))
    if depth != 0:
        issues.append(("E", "MERMAID", f"dòng {base}: ngoặc nhọn {{ }} không cân"))
    return issues


def check_er(body, base):
    issues, depth = [], 0
    for ln, line in body:
        s = line.strip()
        if not s or s.startswith("%%"):
            continue
        depth += _brace_delta(s)
        m = re.match(r"^([A-Za-z0-9_\-]+)\s+[|}o][|o]?(--|\.\.)[|o{][|{]?\s+([A-Za-z0-9_\-]+)\s*:\s*(.+)$", s)
        if m:
            lab = m.group(4).strip()
            if " " in lab and not (lab.startswith('"') and lab.endswith('"')):
                issues.append(("E", "MERMAID", f"dòng {ln}: nhãn quan hệ có khoảng trắng phải đặt trong ngoặc kép"))
        m2 = re.match(r"^(\S+)\s*\{$", s)
        if m2 and not re.fullmatch(r"[A-Za-z0-9_\-]+", m2.group(1)):
            issues.append(("E", "MERMAID", f"dòng {ln}: tên thực thể '{m2.group(1)}' phải là chữ ASCII không dấu"))
    if depth != 0:
        issues.append(("E", "MERMAID", f"dòng {base}: ngoặc nhọn {{ }} không cân"))
    return issues


def check_mermaid_block(start_idx, block):
    body = [(start_idx + 2 + k, l) for k, l in enumerate(block)]
    content = [(ln, l) for ln, l in body if l.strip() and not l.strip().startswith("%%")]
    if not content:
        return [("E", "MERMAID", f"dòng {start_idx + 1}: khối mermaid rỗng")], None
    first = content[0][1].strip()
    dtype = first.split()[0]
    if dtype not in DIAGRAM_TYPES:
        return [("E", "MERMAID", f"dòng {content[0][0]}: loại sơ đồ không hợp lệ '{dtype}'")], None
    if PLACEHOLDER_RE.search("\n".join(block)):
        return [], dtype  # placeholder đã báo ở kiểm tra khác
    rest = content[1:]
    if dtype in ("flowchart", "graph"):
        return check_flowchart(rest, start_idx + 1), dtype
    if dtype == "sequenceDiagram":
        return check_sequence(rest, start_idx + 1), dtype
    if dtype.startswith("stateDiagram"):
        return check_state(rest, start_idx + 1), dtype
    if dtype == "erDiagram":
        return check_er(rest, start_idx + 1), dtype
    return [], dtype


# ----------------------------------------------------------------- load -----
class Doc:
    def __init__(self, root, path):
        self.path = Path(path)
        self.rel = rel(root, path)
        self.raw = read(path)
        self.text = strip_comments(self.raw)
        self.lines = self.text.split("\n")
        self.fm = frontmatter(self.raw)
        self.tables = iter_tables(self.lines)
        self.kind = self.fm.get("doc", "")


def load_docs(root):
    return [Doc(root, p) for p in md_files(root)]


def collect_ids(docs):
    """definitions: id -> [(doc, line)], references: id -> [(doc, line)]."""
    defs, refs = {}, {}
    for d in docs:
        in_fence = False
        for idx, line in enumerate(d.lines):
            if FENCE_RE.match(line):
                in_fence = not in_fence
            found = ids_in(line)
            if not found:
                continue
            first_def = None
            if not in_fence:
                cells = split_row(line)
                if cells:
                    m = ID_RE.fullmatch(PLACEHOLDER_RE.sub("", cells[0]).strip().strip("*`"))
                    if m:
                        first_def = m.group(1)
                hm = HEADING_RE.match(line)
                if hm:
                    m = ID_RE.match(hm.group(2).strip().strip("*`"))
                    if m:
                        first_def = m.group(1)
            for k, i in enumerate(found):
                if first_def == i and k == 0 and in_def_loc(d.rel, id_kind(i)):
                    defs.setdefault(i, []).append((d, idx + 1))
                else:
                    refs.setdefault(i, []).append((d, idx + 1))
    return defs, refs


def fn_docs(docs):
    return [d for d in docs if d.rel.startswith(SPEC + "/functions/") and d.kind in ("function-spec", "report-spec")]


def fn_id_of(d):
    for _, lvl, title in headings(d.lines):
        if lvl == 1:
            m = ID_RE.match(title)
            if m and m.group(1).startswith("FN-"):
                return m.group(1)
    return d.fm.get("id", "")


# ----------------------------------------------------------------- lint -----
def required_sections(template_name):
    p = find_template("03-specification/" + template_name)
    lines = strip_comments(read(p)).split("\n")
    return [m for m in sections_by_number(lines).keys()]


def lint(root):
    root = Path(root)
    docs = load_docs(root)
    issues = []

    def add(level, code, doc, line, msg):
        issues.append({"level": level, "code": code, "file": doc.rel if doc else "", "line": line, "msg": msg})

    defs, refs = collect_ids(docs)
    open_markers = []

    for d in docs:
        status = d.fm.get("status", "")
        final = status in ("Ready", "Approved")
        is_report = d.kind in ("verify-report", "review-report")
        fm_end = 0
        if d.lines and d.lines[0].strip() == "---":
            for k in range(1, len(d.lines)):
                if d.lines[k].strip() == "---":
                    fm_end = k + 1
                    break
        in_fence = False
        for idx, line in enumerate(d.lines):
            ln = idx + 1
            if FENCE_RE.match(line):
                in_fence = not in_fence
            for m in PLACEHOLDER_RE.finditer(line):
                add("E", "PLACEHOLDER", d, ln, f"còn placeholder {m.group(0)[:50]}")
            if idx < fm_end or is_report:
                continue
            if FORBIDDEN_RE.search(line):
                add("E", "FORBIDDEN", d, ln, "còn TODO/TBD/???/xxx")
            for m in MARK_CONFIRM_RE.finditer(line):
                if not m.group(1):
                    add("E", "MARKER", d, ln, "[CẦN XÁC NHẬN] phải kèm Q-xxx")
                else:
                    open_markers.append((d.rel, ln, m.group(0)))
                    add("E" if final else "W", "OPEN-MARKER", d, ln, f"còn {m.group(0)}" + (" trong tài liệu trạng thái " + status if final else ""))
            for m in MARK_PROPOSE_RE.finditer(line):
                if not m.group(1):
                    add("E", "MARKER", d, ln, "[ĐỀ XUẤT] phải kèm → Q-xxx (hỏi khách hàng xác nhận)")
                else:
                    open_markers.append((d.rel, ln, m.group(0)))
                    add("E" if final else "W", "OPEN-MARKER", d, ln, f"còn {m.group(0)}")
            for m in MARK_ASSUME_RE.finditer(line):
                if not m.group(1):
                    add("E", "MARKER", d, ln, "[GIẢ ĐỊNH] phải kèm ASM-xxx")
            bare = PLACEHOLDER_RE.sub(" ", line)
            if not in_fence and NA_RE.search(bare) and not NA_OK_RE.search(bare):
                cells = split_row(bare)
                if cells is None or any(NA_RE.fullmatch(c.strip()) for c in cells):
                    add("E", "NA-REASON", d, ln, "N/A phải kèm lý do: 'N/A – <lý do>'")

        # mục rỗng
        hs = headings(d.lines)
        for k, (idx, lvl, title) in enumerate(hs):
            nxt = hs[k + 1] if k + 1 < len(hs) else None
            end = nxt[0] if nxt else len(d.lines)
            body = [l for l in d.lines[idx + 1:end] if l.strip()]
            if not body and (nxt is None or nxt[1] <= lvl) and lvl >= 2:
                add("E", "EMPTY-SECTION", d, idx + 1, f"mục rỗng: {title[:60]}")

        # cấu trúc theo template
        tmpl = {"function-spec": "function-spec.md", "report-spec": "report-spec.md"}.get(d.kind)
        if tmpl:
            have = sections_by_number(d.lines)
            for sec in required_sections(tmpl):
                if sec not in have:
                    add("E", "STRUCTURE", d, 1, f"thiếu mục '## {sec}.' theo template {tmpl}")
        elif d.kind:
            tp = None
            for _r, cand in all_templates():
                if frontmatter(read(cand)).get("doc") == d.kind:
                    tp = cand
                    break
            if tp:
                want = sections_by_number(strip_comments(read(tp)).split("\n")).keys()
                have = sections_by_number(d.lines)
                for sec in want:
                    if sec not in have:
                        add("E", "STRUCTURE", d, 1, f"thiếu mục '## {sec}.' theo template {tp.name}")

        # mermaid
        blocks = mermaid_blocks(d.lines)
        for start, _end, block in blocks:
            errs, _ = check_mermaid_block(start, block)
            for lv, code, msg in errs:
                add(lv, code, d, start + 1, msg)

        # sơ đồ bắt buộc trong đặc tả chức năng
        if d.kind == "function-spec":
            secs = sections_by_number(d.lines)

            def blocks_in(sec):
                if sec not in secs:
                    return []
                a, b = secs[sec]
                res = []
                for start, _e, block in blocks:
                    if a <= start < b:
                        _, dt = check_mermaid_block(start, block)
                        res.append((dt, "\n".join(block)))
                return res

            def has_na(sec):
                if sec not in secs:
                    return False
                a, b = secs[sec]
                return any(NA_OK_RE.search(l) for l in d.lines[a:b])

            b4 = blocks_in("4")
            if not any(dt in ("flowchart", "graph") and "subgraph" in src for dt, src in b4):
                add("E", "DIAGRAM", d, secs.get("4", (0,))[0] + 1, "mục 4 thiếu sơ đồ swimlane (flowchart có subgraph theo vai trò)")
            b5 = blocks_in("5")
            if not any(dt in ("flowchart", "graph") and re.search(r"\{[^{}]*\}", src) for dt, src in b5) and not has_na("5"):
                add("E", "DIAGRAM", d, secs.get("5", (0,))[0] + 1, "mục 5 thiếu sơ đồ quyết định (flowchart có hình thoi {…})")
            if not any(dt == "sequenceDiagram" for dt, _ in blocks_in("6")):
                add("E", "DIAGRAM", d, secs.get("6", (0,))[0] + 1, "mục 6 thiếu sequenceDiagram")
            if not any(dt and dt.startswith("stateDiagram") for dt, _ in blocks_in("7")) and not has_na("7"):
                add("E", "DIAGRAM", d, secs.get("7", (0,))[0] + 1, "mục 7 thiếu stateDiagram-v2 (hoặc ghi N/A – lý do)")
            if not any(dt == "erDiagram" for dt, _ in blocks_in("10")) and not has_na("10"):
                add("E", "DIAGRAM", d, secs.get("10", (0,))[0] + 1, "mục 10 thiếu erDiagram (hoặc ghi N/A – lý do)")

        # bảng: nguồn, AC, MSG, từ mơ hồ, NFR có số đo
        for t in d.tables:
            h = t["header"]
            src_i = col_index(h, "Nguồn")
            ac_i = col_index(h, r"re:\bAC\b")
            msg_i = col_index(h, "Thông báo", "MSG")
            type_i = col_index(h, "Loại")
            for ln, cells in t["rows"]:
                if not cells or PLACEHOLDER_RE.search(" ".join(cells)):
                    continue
                first = cells[0].strip("*` ")
                kind = first.split("-")[0] if ID_RE.fullmatch(first) else ""
                if kind in ("FR", "BR", "NFR"):
                    stmt = " ".join(cells[1:3])
                    for m in VAGUE_RE.finditer(stmt):
                        add("W", "VAGUE", d, ln, f"{first}: từ mơ hồ '{m.group(0)}' — thay bằng định nghĩa/số đo cụ thể")
                if kind in ("FR", "BR") and src_i is not None and src_i < len(cells):
                    s = cells[src_i]
                    if not (ids_in(s) or re.search(r"references/|TT\s?\d|NĐ|Luật|chuẩn|VAS|Điều", s)):
                        add("E", "NO-SOURCE", d, ln, f"{first}: cột Nguồn trống hoặc không trỏ về REQ/DEC/chuẩn/luật")
                if kind == "FR" and ac_i is not None and ac_i < len(cells) and not re.search(r"AC-", cells[ac_i]):
                    add("E", "FR-NO-AC", d, ln, f"{first}: chưa có AC kiểm chứng")
                if kind == "US" and ac_i is not None and ac_i < len(cells) and not re.search(r"AC-", cells[ac_i]):
                    add("E", "US-NO-AC", d, ln, f"{first}: user story chưa có AC")
                if kind == "BR" and type_i is not None and type_i < len(cells) and "validation" in cells[type_i].lower():
                    if msg_i is not None and msg_i < len(cells) and not re.search(r"MSG-", cells[msg_i]):
                        add("E", "BR-NO-MSG", d, ln, f"{first}: quy tắc Validation chưa có MSG")
                if kind == "NFR" and not re.search(r"\d", " ".join(cells[1:])):
                    add("W", "NFR-NO-METRIC", d, ln, f"{first}: NFR không có con số đo")
        # AC bullets
        for idx, line in enumerate(d.lines):
            if re.match(r"^\s*-\s*\*\*(Cho trước|Khi|Thì)\*\*", line):
                for m in VAGUE_RE.finditer(line):
                    add("W", "VAGUE", d, idx + 1, f"AC: từ mơ hồ '{m.group(0)}'")

    # ID trùng / thiếu định nghĩa
    for i, lst in defs.items():
        if len(lst) > 1:
            where = ", ".join(f"{d.rel}:{ln}" for d, ln in lst)
            add("E", "DUP-ID", lst[0][0], lst[0][1], f"{i} được định nghĩa {len(lst)} lần ({where})")
    for i, lst in refs.items():
        if i not in defs:
            d, ln = lst[0]
            locs = " hoặc ".join(DEF_LOC.get(id_kind(i), ["?"]))
            add("E", "UNDEFINED-ID", d, ln, f"{i} được tham chiếu nhưng chưa định nghĩa trong {locs} ({len(lst)} lần)")

    issues += [dict(level=l, code=c, file=f, line=ln, msg=m) for (l, c, f, ln, m) in catalog_consistency(root, docs, defs)]
    return issues


def catalog_consistency(root, docs, defs):
    out = []
    by_rel = {d.rel: d for d in docs}
    # 1) Bộ trạng thái chứng từ: FN §7 ⊆ catalog
    dt = by_rel.get(SPEC + "/catalogs/document-types.md")
    doc_status = {}
    if dt:
        for t in dt.tables:
            si = col_index(t["header"], "Bộ trạng thái")
            for ln, cells in t["rows"]:
                m = ID_RE.fullmatch(cells[0].strip("*` ")) if cells else None
                if m and si is not None and si < len(cells):
                    doc_status[m.group(1)] = set(re.findall(r"\b[A-Z_]{4,}\b", cells[si]))
    for d in fn_docs(docs):
        secs = sections_by_number(d.lines)
        fn = fn_id_of(d)
        docs_used = set()
        if "0" in secs:
            a, b = secs["0"]
            for l in d.lines[a:b]:
                if "Loại chứng từ" in l:
                    docs_used |= {i for i in ids_in(l) if i.startswith("DOC-")}
        if "7" in secs and len(docs_used) == 1:
            a, b = secs["7"]
            used = set()
            for l in d.lines[a:b]:
                for tok in re.findall(r"\b[A-Z][A-Z_]{3,}\b", l):
                    if tok in CANONICAL_STATUSES:
                        used.add(tok)
                for tok in re.findall(r"state\s+\"[^\"]*\"\s+as\s+([A-Za-z_]+)", l):
                    used.add(tok)
            dname = next(iter(docs_used))
            for tok in sorted(used):
                if tok not in CANONICAL_STATUSES:
                    out.append(("W", "STATUS", d.rel, a + 1, f"trạng thái '{tok}' không thuộc bộ trạng thái chuẩn (conventions §6)"))
            if dname in doc_status and doc_status[dname]:
                extra = used - doc_status[dname]
                if extra:
                    out.append(("E", "STATUS-CONFLICT", d.rel, a + 1, f"{fn} dùng trạng thái {sorted(extra)} không có trong bộ trạng thái của {dname} ở document-types.md"))
    # 2) Vai trò: FN §2.1 ↔ ma trận tổng hợp
    rp = by_rel.get(SPEC + "/catalogs/roles-permissions.md")
    matrix = {}
    if rp:
        for t in rp.tables:
            roles = [c.strip("*` ") for c in t["header"][1:]]
            if not roles or not all(ID_RE.fullmatch(r or "-") and r.startswith("ROLE-") for r in roles):
                continue
            for ln, cells in t["rows"]:
                m = ID_RE.fullmatch(cells[0].strip("*` ")) if cells else None
                if m and m.group(1).startswith("FN-"):
                    matrix[m.group(1)] = {roles[k]: (cells[k + 1] if k + 1 < len(cells) else "") for k in range(len(roles))}
    for d in fn_docs(docs):
        fn = fn_id_of(d)
        secs = sections_by_number(d.lines)
        if "2" not in secs or fn not in matrix:
            if matrix and fn and fn not in matrix:
                out.append(("W", "ROLE-MATRIX", d.rel, 1, f"{fn} chưa có dòng trong ma trận tổng hợp roles-permissions.md §2"))
            continue
        a, b = secs["2"]
        listed = set()
        for t in iter_tables(d.lines[a:b]):
            for _, cells in t["rows"]:
                c0 = cells[0].strip("*` ") if cells else ""
                if c0.startswith("ROLE-") and ID_RE.fullmatch(c0):
                    listed.add(c0)
        for r in listed:
            v = matrix[fn].get(r)
            if v is None or v.strip() in ("", "—", "-", "✖"):
                out.append(("E", "ROLE-CONFLICT", d.rel, a + 1, f"{fn}: {r} tham gia ở §2.1 nhưng ma trận tổng hợp ghi '{v or 'không có cột'}'"))
        for r, v in matrix[fn].items():
            if v.strip() not in ("", "—", "-", "✖") and r not in listed:
                out.append(("E", "ROLE-CONFLICT", d.rel, a + 1, f"{fn}: ma trận tổng hợp cho {r} quyền '{v}' nhưng §2.1 không liệt kê vai trò này"))
    return out


def print_issues(issues, as_json=False):
    if as_json:
        print(json.dumps(issues, ensure_ascii=False, indent=1))
        return
    errs = [i for i in issues if i["level"] == "E"]
    warns = [i for i in issues if i["level"] == "W"]
    for i in sorted(issues, key=lambda x: (x["level"] != "E", x["file"], x["line"])):
        print(f"[{'ERROR' if i['level'] == 'E' else 'WARN '}] {i['code']:<15} {i['file']}:{i['line']}  {i['msg']}")
    print(f"\nTổng: {len(errs)} lỗi (Error), {len(warns)} cảnh báo (Warning)")


def write_lint_report(root, issues):
    errs = [i for i in issues if i["level"] == "E"]
    lines = ["<!-- SINH TỰ ĐỘNG bởi scripts/ba.py lint — không sửa tay -->", "# Báo cáo lint", "",
             f"Ngày chạy: {today()} · Lỗi: {len(errs)} · Cảnh báo: {len(issues) - len(errs)}", "",
             "| Mức | Mã | Vị trí | Nội dung |", "|---|---|---|---|"]
    for i in sorted(issues, key=lambda x: (x["level"] != "E", x["file"], x["line"])):
        lines.append(f"| {'Error' if i['level'] == 'E' else 'Warning'} | {i['code']} | {i['file']}:{i['line']} | {i['msg'].replace('|', '/')} |")
    (Path(root) / "lint-report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- trace -----
def trace(root):
    root = Path(root)
    docs = load_docs(root)
    defs, refs = collect_ids(docs)
    by_rel = {d.rel: d for d in docs}
    res = {"req": {}, "fn": {}, "errors": [], "warnings": []}

    reg = by_rel.get("02-requirements/requirement-register.md")
    if reg:
        for t in reg.tables:
            si, ti, mi = col_index(t["header"], "Trạng thái"), col_index(t["header"], "Loại"), col_index(t["header"], "Module")
            for ln, cells in t["rows"]:
                c0 = cells[0].strip("*` ") if cells else ""
                if c0.startswith("REQ-") and ID_RE.fullmatch(c0):
                    st = cells[si] if si is not None and si < len(cells) else ""
                    res["req"][c0] = {"status": st, "type": cells[ti] if ti is not None and ti < len(cells) else "",
                                      "module": cells[mi] if mi is not None and mi < len(cells) else "",
                                      "summary": cells[1] if len(cells) > 1 else "", "covered_by": set()}

    fns = fn_docs(docs)
    listed = set()
    srs = by_rel.get(SPEC + "/srs-overview.md")
    if srs:
        for t in srs.tables:
            if col_index(t["header"], "File") is None:
                continue
            for ln, cells in t["rows"]:
                c0 = cells[0].strip("*` ") if cells else ""
                if c0.startswith("FN-") and ID_RE.fullmatch(c0):
                    listed.add(c0)

    for d in docs:
        if not d.rel.startswith(SPEC + "/"):
            continue
        fn = fn_id_of(d) if d in fns else None
        text = d.text
        if srs is not None and d is srs:
            secs = sections_by_number(d.lines)
            if "3" in secs:
                a3, b3 = secs["3"]
                text = "\n".join(d.lines[:a3] + d.lines[b3:])
        for i in set(ids_in(text)):
            if i in res["req"]:
                res["req"][i]["covered_by"].add(fn or d.rel)

    for d in fns:
        fn = fn_id_of(d)
        ids = set(ids_in(d.text))
        info = {"file": d.rel, "name": d.fm.get("name", ""), "type": d.fm.get("type", ""), "status": d.fm.get("status", ""),
                "reqs": sorted(i for i in ids if i.startswith("REQ-")),
                "feats": sorted(i for i in ids if i.startswith("FEAT-")),
                "decs": sorted(i for i in ids if i.startswith("DEC-")),
                "fr": [], "us": [], "ac_defined": [], "br": [], "msg": []}
        proposal = bool(MARK_PROPOSE_RE.search(d.text))
        for t in d.tables:
            ac_i = col_index(t["header"], r"re:\bAC\b")
            for ln, cells in t["rows"]:
                c0 = cells[0].strip("*` ") if cells else ""
                if not ID_RE.fullmatch(c0 or "-"):
                    continue
                acs = sorted(set(re.findall(r"AC-[A-Z]{2,5}-\d{2,}-\d{2,}", cells[ac_i]))) if ac_i is not None and ac_i < len(cells) else []
                if c0.startswith("FR-"):
                    info["fr"].append((c0, acs))
                elif c0.startswith("US-"):
                    info["us"].append((c0, acs))
                elif c0.startswith("BR-"):
                    info["br"].append(c0)
                elif c0.startswith("MSG-"):
                    info["msg"].append(c0)
        for _, lvl, title in headings(d.lines):
            m = ID_RE.match(title)
            if m and m.group(1).startswith("AC-"):
                info["ac_defined"].append(m.group(1))
        res["fn"][fn] = info
        # nguồn
        if not info["reqs"] and not info["decs"]:
            if info["feats"] and proposal:
                res["warnings"].append(f"{fn}: chỉ có nguồn FEAT, đang chờ khách hàng xác nhận ([ĐỀ XUẤT → Q])")
            elif info["feats"]:
                res["errors"].append(f"{fn}: chỉ có nguồn FEAT (research) mà không có DEC xác nhận hay marker [ĐỀ XUẤT → Q] — nguy cơ THỪA chức năng")
            else:
                res["errors"].append(f"{fn}: không có nguồn REQ/DEC — chức năng THỪA hoặc thiếu truy vết")
        for r in info["reqs"]:
            if r in res["req"] and "loại" in res["req"][r]["status"].lower():
                res["warnings"].append(f"{fn}: tham chiếu {r} đang ở trạng thái '{res['req'][r]['status']}'")
        for fr, acs in info["fr"]:
            if not acs:
                res["errors"].append(f"{fn}: {fr} không có AC kiểm chứng")
            for a in acs:
                if a not in defs:
                    res["errors"].append(f"{fn}: {fr} trỏ tới {a} chưa được định nghĩa")
        for us, acs in info["us"]:
            if not acs:
                res["errors"].append(f"{fn}: {us} không có AC")
        linked = {a for _, acs in info["fr"] + info["us"] for a in acs}
        for a in info["ac_defined"]:
            if a not in linked:
                res["warnings"].append(f"{fn}: {a} không được FR/US nào trỏ tới")
        for b in info["br"]:
            if len([1 for dd, _ in refs.get(b, []) if dd is d]) == 0:
                res["warnings"].append(f"{fn}: {b} chỉ được định nghĩa, không xuất hiện trong luồng/sơ đồ/bảng nào khác")
        for mmsg in info["msg"]:
            if not refs.get(mmsg):
                res["warnings"].append(f"{fn}: {mmsg} không được tham chiếu từ luồng/quy tắc nào")
        if fn not in listed and srs:
            res["errors"].append(f"{fn}: có file đặc tả nhưng chưa có trong danh sách chức năng srs-overview §3")
    for fn in sorted(listed - set(res["fn"])):
        res["errors"].append(f"{fn}: có trong danh sách chức năng srs-overview §3 nhưng chưa có file đặc tả")

    for r, info in res["req"].items():
        if "loại" in info["status"].lower():
            continue
        if not info["covered_by"] and (fns or srs):
            res["errors"].append(f"{r}: chưa được phủ trong 03-specification — THIẾU ({info['summary'][:80]})")

    # Biên bản họp: dòng nguyên văn chưa xử lý
    ext_refs = {}
    for d in docs:
        for m in re.finditer(r"(MTG-\d{3,})\s+(L\d+)(?:\s*[–\-]\s*(L\d+))?", d.text):
            a0 = int(m.group(2)[1:])
            b0 = int(m.group(3)[1:]) if m.group(3) else a0
            for k in range(a0, b0 + 1):
                ext_refs.setdefault(m.group(1), set()).add(k)
    for d in docs:
        if d.kind != "meeting-notes":
            continue
        secs = sections_by_number(d.lines)
        if "3" not in secs:
            continue
        a, b = secs["3"]
        lines_def = set()
        for t in iter_tables(d.lines[a:b]):
            for _, cells in t["rows"]:
                if cells and re.fullmatch(r"L\d+", cells[0].strip()):
                    lines_def.add(cells[0].strip())
        used = set()
        for m in re.finditer(r"\b(L\d+)(?:\s*[–\-]\s*(L\d+))?", "\n".join(d.lines[b:])):
            a0 = int(m.group(1)[1:])
            b0 = int(m.group(2)[1:]) if m.group(2) else a0
            used |= {f"L{k:02d}" for k in range(a0, b0 + 1)} | {f"L{k}" for k in range(a0, b0 + 1)}
        mid = next((h for _, lv, h in headings(d.lines) if lv == 1), "")
        mm = re.match(r"(MTG-\d{3,})", mid)
        if mm:
            used |= {f"L{k:02d}" for k in ext_refs.get(mm.group(1), set())} | {f"L{k}" for k in ext_refs.get(mm.group(1), set())}
        for L in sorted(lines_def - used, key=lambda x: int(x[1:])):
            res["errors"].append(f"{d.rel}: dòng {L} chưa được xử lý (chưa thành yêu cầu/quyết định/câu hỏi/không phải yêu cầu)")
    return res


def write_trace(root, res):
    L = ["<!-- SINH TỰ ĐỘNG bởi scripts/ba.py trace — không sửa tay -->", "# Ma trận truy vết", "",
         f"Ngày chạy: {today()}", ""]
    reqs = res["req"]
    active = {k: v for k, v in reqs.items() if "loại" not in v["status"].lower()}
    covered = [k for k, v in active.items() if v["covered_by"]]
    L += ["## Tóm tắt", "", "| Chỉ số | Giá trị |", "|---|---|",
          f"| REQ còn hiệu lực | {len(active)} |",
          f"| REQ đã được phủ | {len(covered)} |",
          f"| REQ chưa phủ (THIẾU) | {len(active) - len(covered)} |",
          f"| Số chức năng | {len(res['fn'])} |",
          f"| Lỗi truy vết | {len(res['errors'])} |",
          f"| Cảnh báo | {len(res['warnings'])} |", ""]
    L += ["## REQ → nơi đặc tả", "", "| REQ | Trạng thái | Module | Được phủ bởi |", "|---|---|---|---|"]
    for k in sorted(reqs):
        v = reqs[k]
        cov = ", ".join(sorted(v["covered_by"])) or "**CHƯA PHỦ**"
        L.append(f"| {k} | {v['status']} | {v['module']} | {cov} |")
    L += ["", "## Chức năng → nguồn & kiểm chứng", "", "| FN | Loại | Trạng thái | REQ | DEC | FEAT | Số FR | FR thiếu AC | Số US | Số AC |", "|---|---|---|---|---|---|---|---|---|---|"]
    for fn in sorted(res["fn"]):
        i = res["fn"][fn]
        miss = sum(1 for _, a in i["fr"] if not a)
        L.append(f"| {fn} | {i['type']} | {i['status']} | {', '.join(i['reqs'])} | {', '.join(i['decs'])} | {', '.join(i['feats'])} | {len(i['fr'])} | {miss} | {len(i['us'])} | {len(i['ac_defined'])} |")
    L += ["", "## Lỗi", ""] + ([f"- {e}" for e in res["errors"]] or ["- Không có"])
    L += ["", "## Cảnh báo", ""] + ([f"- {w}" for w in res["warnings"]] or ["- Không có"])
    (Path(root) / "traceability.md").write_text("\n".join(L) + "\n", encoding="utf-8")


# ------------------------------------------------------------ checklist -----
STEP_FILES = {"1": ["C1-research.md"], "2": ["C2-requirements.md"], "3": ["C3-specification.md"],
              "3F": ["C3F-function.md"], "3R": ["C3R-report.md"], "4": ["C4-verification.md"], "5": ["C5-review.md"]}


def load_checklist(name):
    d = strip_comments(read(find_checklist(name))).split("\n")
    items = []
    for t in iter_tables(d):
        for _, cells in t["rows"]:
            if cells and re.fullmatch(r"C\d[A-Z]?(?:-[A-Z]+)?-\d{2}", cells[0].strip()):
                items.append({"id": cells[0].strip(), "q": cells[1] if len(cells) > 1 else "",
                              "how": cells[2] if len(cells) > 2 else "", "applies": cells[3] if len(cells) > 3 else "Tất cả"})
    return items


def applies(item, fn_type):
    a = item["applies"].strip()
    if a.startswith("Tất cả") or a.startswith("Khi"):
        return True
    types = [x.strip().lower() for x in a.split(",")]
    return fn_type.strip().lower() in types


def checklist_table(items, note=None):
    L = []
    if note:
        L += [note, ""]
    L += ["| ID | Câu hỏi | Kết quả (Yes/No/N/A) | Bằng chứng (file §/ID) hoặc lý do N/A | Hành động nếu No |", "|---|---|---|---|---|"]
    for it in items:
        q = it["q"] + (f" *(Điều kiện: {it['applies']})*" if it["applies"].startswith("Khi") else "")
        L.append(f"| {it['id']} | {q} |  |  |  |")
    return L


def build_checklist(root, step, rnd, only_fn=None):
    root = Path(root)
    docs = load_docs(root) if root.exists() else []
    out = [f"<!-- Sinh bởi scripts/ba.py checklist --step {step} --round {rnd} ngày {today()} -->", ""]
    steps = [step]
    if step == "3":
        steps = ["3", "3F", "3R"]
    if step == "all":
        steps = []
        rels = {d.rel for d in docs}
        if "01-research/research-report.md" in rels:
            steps.append("1")
        if "02-requirements/requirement-register.md" in rels:
            steps.append("2")
        if SPEC + "/srs-overview.md" in rels:
            steps += ["3", "3F", "3R"]
        steps.append("4")
    for s in steps:
        for f in STEP_FILES[s]:
            items = load_checklist(f)
            title = read(find_checklist(f)).split("\n", 1)[0].lstrip("# ").strip()
            if s in ("3F", "3R"):
                for d in fn_docs(docs):
                    fn = fn_id_of(d)
                    if only_fn and fn not in only_fn:
                        continue
                    is_report = d.kind == "report-spec" or d.fm.get("type", "") == "Báo cáo"
                    if (s == "3R") != is_report:
                        continue
                    t = d.fm.get("type", "")
                    sel = [it for it in items if s == "3R" or applies(it, t)]
                    out += [f"### {title} — {fn} {d.fm.get('name', '')} (`{d.rel}`, loại: {t})", ""] + checklist_table(sel) + [""]
            else:
                out += [f"### {title}", ""] + checklist_table(items) + [""]
    return "\n".join(out)


# --------------------------------------------------------------- status -----
def status(report_path):
    d = Doc(Path(report_path).parent, report_path)
    counts = {"yes": 0, "no": 0, "na": 0, "empty": 0, "invalid": 0}
    problems = []
    for t in d.tables:
        ri = col_index(t["header"], "Kết quả")
        ei = col_index(t["header"], "Bằng chứng")
        if ri is not None and col_index(t["header"], "ID") == 0:
            for ln, cells in t["rows"]:
                v = cells[ri].strip().lower() if ri < len(cells) else ""
                ev = cells[ei].strip() if ei is not None and ei < len(cells) else ""
                cid = cells[0]
                if v in ("yes", "có", "y", "đạt"):
                    if not ev:
                        counts["invalid"] += 1
                        problems.append(f"{cid}: Yes nhưng thiếu bằng chứng (dòng {ln})")
                    else:
                        counts["yes"] += 1
                elif v in ("no", "không", "n", "không đạt"):
                    counts["no"] += 1
                    problems.append(f"{cid}: No (dòng {ln})")
                elif v.startswith("n/a"):
                    if not ev and not NA_OK_RE.search(cells[ri]):
                        counts["invalid"] += 1
                        problems.append(f"{cid}: N/A nhưng thiếu lý do (dòng {ln})")
                    else:
                        counts["na"] += 1
                else:
                    counts["empty"] += 1
                    problems.append(f"{cid}: chưa trả lời (dòng {ln})")
        si = col_index(t["header"], "Mức độ")
        xi = col_index(t["header"], "Xử lý", "Đã sửa")
        if si is not None and xi is not None:
            for ln, cells in t["rows"]:
                sev = cells[si].strip().lower() if si < len(cells) else ""
                x = cells[xi].strip().lower() if xi < len(cells) else ""
                if PLACEHOLDER_RE.search(" ".join(cells)):
                    continue
                is_open = (not x) or x.startswith(("chưa", "mở")) or x in ("không", "no")
                if is_open and sev.startswith(("critical", "major")):
                    problems.append(f"{cells[0]}: phát hiện mức {cells[si]} chưa xử lý (dòng {ln})")
                    counts["invalid"] += 1
    ok = counts["no"] == 0 and counts["empty"] == 0 and counts["invalid"] == 0 and (counts["yes"] + counts["na"]) > 0
    return ok, counts, problems


# ---------------------------------------------------------------- init etc --
def cmd_init(a):
    root = Path(a.root)
    for sub in ["00-inputs/meetings", "00-inputs/files", SPEC + "/functions", "04-verification", "05-review"]:
        (root / sub).mkdir(parents=True, exist_ok=True)
    created = skipped = 0
    for troot, t in all_templates():
        r = rel(troot, t)
        if r in NON_INIT_TEMPLATES:
            continue
        dst = root / r
        if dst.exists() and not a.force:
            skipped += 1
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        txt = read(t).replace("{{PROJECT}}", a.project).replace("{{DATE}}", today())
        dst.write_text(txt, encoding="utf-8")
        created += 1
    print(f"Đã tạo {created} file, bỏ qua {skipped} file đã tồn tại trong {root}")
    print("Tiếp theo: đăng ký nguồn vào 00-inputs/source-register.md; tạo biên bản họp bằng 'new-meeting'.")
    return 0


def next_num(root, prefix, width=3):
    nums = [0]
    for p in Path(root).rglob("*.md"):
        for m in re.finditer(prefix + r"-(\d+)", PLACEHOLDER_RE.sub(" ", p.read_text(encoding="utf-8", errors="ignore"))):
            nums.append(int(m.group(1)))
        m = re.match(prefix + r"-(\d+)", p.name)
        if m:
            nums.append(int(m.group(1)))
    return f"{prefix}-{max(nums) + 1:0{width}d}"


def project_name(root):
    p = Path(root) / "00-inputs" / "source-register.md"
    if p.exists():
        return frontmatter(read(p)).get("project", "")
    return ""


def cmd_new_meeting(a):
    root = Path(a.root)
    mid = next_num(root / "00-inputs", "MTG")
    date = a.date or today()
    d = _dt.date.fromisoformat(date)
    dst = root / "00-inputs" / "meetings" / f"{mid}-{date}.md"
    dst.parent.mkdir(parents=True, exist_ok=True)
    txt = read(find_template("00-inputs/meeting-notes.md"))
    txt = txt.replace("{{MTG-001}}", mid).replace("{{PROJECT}}", project_name(root)).replace("{{DATE}}", today())
    txt = txt.replace("({{dd/MM/yyyy}})", f"({d.strftime('%d/%m/%Y')})", 1)
    dst.write_text(txt, encoding="utf-8")
    print(f"Đã tạo {dst}\nNhớ thêm dòng {mid} vào 00-inputs/source-register.md §1.")
    return 0


def slugify(s):
    s = unicodedata.normalize("NFD", s.replace("đ", "d").replace("Đ", "D"))
    s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn").lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:50]


def cmd_new_function(a):
    m = re.fullmatch(r"FN-([A-Z]{2,5})-(\d{2,})", a.id)
    if not m:
        print("--id phải có dạng FN-<MOD>-<NN>, ví dụ FN-PUR-03", file=sys.stderr)
        return 2
    mod, nn = m.group(1), m.group(2)
    root = Path(a.root)
    report = a.type.strip().lower() == "báo cáo"
    tpl = find_template("03-specification/" + ("report-spec.md" if report else "function-spec.md"))
    dst = root / SPEC / "functions" / mod / f"{a.id}-{a.slug or slugify(a.name)}.md"
    if dst.exists():
        print(f"Đã tồn tại: {dst}", file=sys.stderr)
        return 1
    txt = read(tpl)
    txt = txt.replace("{{FN_ID}}", a.id).replace("{{FN_NAME}}", a.name).replace("{{MOD}}", mod)
    txt = txt.replace("{{DATE}}", today()).replace("{{PROJECT}}", project_name(root))
    txt = re.sub(r"\{\{(US|AC|FR|BR|MSG|NFR)-MOD-NN-(\d+)\}\}", lambda mm: f"{mm.group(1)}-{mod}-{nn}-{mm.group(2)}", txt)
    txt = re.sub(r"(?<=[ (,])(US|AC|FR|BR|MSG|NFR)-MOD-NN-(\d+)", lambda mm: f"{mm.group(1)}-{mod}-{nn}-{mm.group(2)}", txt)
    if not report:
        txt = re.sub(r"^type: .*$", f"type: {a.type}", txt, count=1, flags=re.M)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(txt, encoding="utf-8")
    print(f"Đã tạo {dst}\nNhớ thêm {a.id} vào bảng danh sách chức năng trong {SPEC}/srs-overview.md §3 và ma trận roles-permissions.md §2.")
    return 0


def cmd_lint(a):
    issues = lint(a.root)
    if not a.no_write:
        write_lint_report(a.root, issues)
    print_issues(issues, a.json)
    return 1 if any(i["level"] == "E" for i in issues) else 0


def cmd_trace(a):
    res = trace(a.root)
    if not a.no_write:
        write_trace(a.root, res)
    if a.json:
        out = dict(res)
        out["req"] = {k: dict(v, covered_by=sorted(v["covered_by"])) for k, v in res["req"].items()}
        print(json.dumps(out, ensure_ascii=False, indent=1))
    else:
        active = [k for k, v in res["req"].items() if "loại" not in v["status"].lower()]
        unc = [k for k in active if not res["req"][k]["covered_by"]]
        print(f"REQ còn hiệu lực: {len(active)} · chưa phủ: {len(unc)} · chức năng: {len(res['fn'])}")
        for e in res["errors"]:
            print(f"[ERROR] {e}")
        for w in res["warnings"]:
            print(f"[WARN ] {w}")
        print(f"\nTổng: {len(res['errors'])} lỗi, {len(res['warnings'])} cảnh báo" + ("" if a.no_write else f" — đã ghi {Path(a.root) / 'traceability.md'}"))
    return 1 if res["errors"] else 0


def cmd_checklist(a):
    only = set(a.fn) if a.fn else None
    txt = build_checklist(a.root, a.step, a.round, only)
    if a.out:
        out = Path(a.out)
        if out.exists():
            cur = read(out)
            marker = "## 4. Kết quả checklist"
            alt = "## 5. Kết quả checklist C5"
            if re.search(r"\|\s*(Yes|No|N/A|Có|Không)\s*\|", cur) and not a.force:
                print(f"{out} đã có câu trả lời checklist — dùng --force để ghi đè, hoặc chỉ định --out file mới", file=sys.stderr)
                return 1
            if marker in cur:
                cur = re.sub(r"(## 4\. Kết quả checklist\n)(.*?)(?=\n## 5\.)", lambda m: m.group(1) + "\n" + txt + "\n", cur, flags=re.S)
            elif alt in cur:
                cur = re.sub(r"(## 5\. Kết quả checklist C5\n)(.*?)(?=\n## 6\.)", lambda m: m.group(1) + "\n" + txt + "\n", cur, flags=re.S)
            else:
                cur += "\n" + txt
            out.write_text(cur, encoding="utf-8")
        else:
            tname = "05-review/review-report.md" if a.step == "5" else "04-verification/verify-report.md"
            base = read(find_template(tname)).replace("{{N}}", str(a.round)).replace("{{DATE}}", today())
            base = base.replace("{{PROJECT}}", project_name(a.root))
            if a.step == "5":
                base = re.sub(r"(## 5\. Kết quả checklist C5\n)(.*?)(?=\n## 6\.)", lambda m: m.group(1) + "\n" + txt + "\n", base, flags=re.S)
            else:
                base = re.sub(r"(## 4\. Kết quả checklist\n)(.*?)(?=\n## 5\.)", lambda m: m.group(1) + "\n" + txt + "\n", base, flags=re.S)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(base, encoding="utf-8")
        print(f"Đã ghi checklist vào {out}")
    else:
        print(txt)
    return 0


def cmd_status(a):
    ok, counts, problems = status(a.report)
    print(f"Yes: {counts['yes']} · No: {counts['no']} · N/A: {counts['na']} · Chưa trả lời: {counts['empty']} · Không hợp lệ: {counts['invalid']}")
    for p in problems[:200]:
        print(f" - {p}")
    print("KẾT LUẬN: " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main(argv=None):
    p = argparse.ArgumentParser(description="Công cụ kiểm soát chất lượng tài liệu BA ERP (erp-ba-core)")
    sp = p.add_subparsers(dest="cmd")
    x = sp.add_parser("init"); x.add_argument("root"); x.add_argument("--project", required=True); x.add_argument("--force", action="store_true")
    x = sp.add_parser("new-meeting"); x.add_argument("root"); x.add_argument("--date")
    x = sp.add_parser("new-function"); x.add_argument("root"); x.add_argument("--id", required=True); x.add_argument("--name", required=True)
    x.add_argument("--type", default="Chứng từ"); x.add_argument("--slug")
    x = sp.add_parser("lint"); x.add_argument("root"); x.add_argument("--json", action="store_true"); x.add_argument("--no-write", action="store_true")
    x = sp.add_parser("trace"); x.add_argument("root"); x.add_argument("--json", action="store_true"); x.add_argument("--no-write", action="store_true")
    x = sp.add_parser("checklist"); x.add_argument("root"); x.add_argument("--step", required=True, choices=["1", "2", "3", "3F", "3R", "4", "5", "all"])
    x.add_argument("--round", type=int, default=1); x.add_argument("--fn", nargs="*"); x.add_argument("--out"); x.add_argument("--force", action="store_true")
    x = sp.add_parser("status"); x.add_argument("report")
    a = p.parse_args(argv)
    if not a.cmd:
        p.print_help()
        return 2
    return {"init": cmd_init, "new-meeting": cmd_new_meeting, "new-function": cmd_new_function, "lint": cmd_lint,
            "trace": cmd_trace, "checklist": cmd_checklist, "status": cmd_status}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
