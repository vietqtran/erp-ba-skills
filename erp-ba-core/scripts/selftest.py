#!/usr/bin/env python3
"""Tự kiểm công cụ ba.py: workspace mẫu phải sạch; mỗi lỗi cố ý cài vào bản sao phải bị phát hiện.

Chạy: python3 scripts/selftest.py   (mã thoát 0 = mọi kiểm tra đạt)
"""
import shutil
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ba  # noqa: E402

SAMPLE = HERE.parent / "assets" / "examples" / "sample-workspace"
PO = "03-specification/functions/PUR/FN-PUR-02-don-mua-hang.md"
VEN = "03-specification/functions/PUR/FN-PUR-01-danh-muc-nha-cung-cap.md"


def codes(root):
    return {(i["code"], i["file"]) for i in ba.lint(root) if i["level"] == "E"}


def edit(root, rel, old, new):
    p = Path(root) / rel
    s = p.read_text(encoding="utf-8")
    assert old in s, f"không tìm thấy đoạn cần sửa trong {rel}: {old[:60]}"
    p.write_text(s.replace(old, new, 1), encoding="utf-8")


CASES = [
    ("Placeholder còn sót", PO, "| Luồng tổng quan / luồng chi tiết | BP-01 /", "| Luồng tổng quan / luồng chi tiết | {{BP-…}} /", "lint", "PLACEHOLDER"),
    ("Marker thiếu Q", PO, "- **Mục đích nghiệp vụ:**", "- **Mục đích nghiệp vụ:** [CẦN XÁC NHẬN]", "lint", "MARKER"),
    ("Marker mở trong tài liệu Ready", PO, "- **Mục đích nghiệp vụ:**", "- **Mục đích nghiệp vụ:** [CẦN XÁC NHẬN: Q-001]", "lint", "OPEN-MARKER"),
    ("ID trùng giữa hai file", VEN, "| FR-PUR-01-05 |", "| FR-PUR-02-01 |", "lint", "DUP-ID"),
    ("Tham chiếu vai trò chưa định nghĩa", PO, "| ROLE-ACC | Chỉ xem |", "| ROLE-ACC | Chỉ xem | ROLE-WAREHOUSE |", "lint", "UNDEFINED-ID"),
    ("FR thiếu AC", PO, "| Must | REQ-001 | AC-PUR-02-01 |", "| Must | REQ-001 | — |", "lint", "FR-NO-AC"),
    ("BR Validation thiếu MSG", PO, "| Validation | `erp-ba-core/references/design-patterns.md` P02 | MSG-PUR-02-02 |", "| Validation | `erp-ba-core/references/design-patterns.md` P02 | — |", "lint", "BR-NO-MSG"),
    ("FR không có nguồn", PO, "| Must | REQ-001 | AC-PUR-02-01 |", "| Must | — | AC-PUR-02-01 |", "lint", "NO-SOURCE"),
    ("Trạng thái lệch catalog", PO, "    PARTIAL --> CLOSED : Đóng", "    PARTIAL --> CLOSED : Đóng\n    CLOSED --> POSTED : Ghi sổ", "lint", "STATUS-CONFLICT"),
    ("Vai trò lệch ma trận tổng hợp", "03-specification/catalogs/roles-permissions.md", "| FN-PUR-02 | Chính | Duyệt | Duyệt | Xem |", "| FN-PUR-02 | Chính | Duyệt | Duyệt | — |", "lint", "ROLE-CONFLICT"),
    ("Mermaid nhãn chưa trích dẫn", PO, 'S(["Có nhu cầu đặt hàng"])', "S([Có nhu cầu (gấp)])", "lint", "MERMAID"),
    ("Thiếu mục template", PO, "## 15. Báo cáo / truy vấn liên quan", "## Báo cáo / truy vấn liên quan", "lint", "STRUCTURE"),
    ("Thiếu sequence diagram", PO, "sequenceDiagram", "flowchart LR", "lint-all", "DIAGRAM"),
    ("N/A không lý do", VEN, "N/A – chức năng không dùng tham số hệ thống.", "N/A", "lint", "NA-REASON"),
    ("REQ không được phủ", "02-requirements/requirement-register.md", "| REQ-022 |", "| REQ-022 |", "trace-req", "REQ-023"),
    ("FN không nguồn", None, None, None, "trace-fn", "FN-PUR-09"),
    ("Luồng chi tiết chưa phân rã", "03-specification/srs-overview.md", "FL-01-02, FL-01-03, FL-01-04", "FL-01-02, FL-01-04", "trace-fl", "FL-01-03"),
    ("Dòng biên bản chưa xử lý", "00-inputs/meetings/MTG-001-2026-10-06.md", "| L18 | Lan |", "| L19 | Hùng | Câu thử nghiệm chưa được xử lý ở đâu. |\n| L18 | Lan |", "trace-mtg", "L19"),
]


def run():
    failures = 0
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp) / "base"
        shutil.copytree(SAMPLE, base)
        errs = [i for i in ba.lint(base) if i["level"] == "E"]
        tr = ba.trace(base)
        ok = not errs and not tr["errors"]
        print(("PASS" if ok else "FAIL") + " — workspace mẫu sạch (lint 0 lỗi, trace 0 lỗi)")
        for e in errs[:5] + [{"msg": x} for x in tr["errors"][:5]]:
            print("     ", e.get("file", ""), e.get("line", ""), e["msg"])
        failures += 0 if ok else 1

        for k, (name, rel, old, new, kind, expect) in enumerate(CASES):
            ws = Path(tmp) / f"case{k}"
            shutil.copytree(SAMPLE, ws)
            if kind == "trace-req":
                p = ws / rel
                p.write_text(p.read_text(encoding="utf-8").replace(
                    "\n## Thống kê",
                    "| REQ-023 | Yêu cầu thử nghiệm chưa được đặc tả | \"thử\" | MTG-001 L01 | Thử | FR | PUR | BP-01 | Must | Đã xác nhận | — |\n\n## Thống kê", 1),
                    encoding="utf-8")
            elif kind == "trace-fn":
                f = ws / "03-specification/functions/PUR/FN-PUR-09-thu.md"
                f.write_text("---\ndoc: function-spec\nid: FN-PUR-09\nname: Thử\ntype: Tiện ích\nstatus: Draft\n---\n\n# FN-PUR-09 — Thử\n\n## 0. Thông tin & truy vết\n\nKhông có nguồn.\n", encoding="utf-8")
            elif kind == "trace-fl":
                edit(ws, rel, old, new)
                edit(ws, PO, old, new)
            elif kind == "lint-all":
                p = ws / rel
                p.write_text(p.read_text(encoding="utf-8").replace(old, new), encoding="utf-8")
            else:
                edit(ws, rel, old, new)
            if kind in ("lint", "lint-all"):
                got = {c for c, _ in codes(ws)}
                hit = expect in got
            else:
                t = ba.trace(ws)
                hit = any(expect in e for e in t["errors"])
                if kind == "trace-fn":
                    hit = any("FN-PUR-09" in e and "không có nguồn" in e for e in t["errors"])
            print(("PASS" if hit else "FAIL") + f" — phát hiện: {name} ({expect})")
            failures += 0 if hit else 1
    print(f"\n{len(CASES) + 1 - failures}/{len(CASES) + 1} kiểm tra đạt")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(run())
