# Bộ skill BA ERP

Bộ skill cho Claude Code giúp BA/AI agent viết tài liệu nghiệp vụ ERP theo 5 bước, bám sát yêu cầu gốc (không lệch, không thừa, không thiếu, không mâu thuẫn), đủ chi tiết để dev code ngay.

| Skill | Vai trò |
|---|---|
| `erp-ba-step1-research` | Research ngành, luật, đối thủ → danh mục tính năng, câu hỏi khảo sát (checklist C1) |
| `erp-ba-step2-requirements` | Biên bản họp → sổ yêu cầu có trích dẫn, tài liệu & quy trình tổng quan TO-BE (C2) |
| `erp-ba-step3-specification` | Phân rã module → chức năng; đặc tả 21 mục đủ để code (C3, C3F, C3R) |
| `erp-ba-step4-verify` | Tự kiểm có bằng chứng, 4 câu hỏi bắt buộc của BA, điều phối vòng lặp (C4) |
| `erp-ba-step5-review` | Review độc lập bằng agent khác theo 6 góc nhìn (C5) |
| `erp-ba-core` | Quy ước dùng chung, công cụ `scripts/ba.py`, kho kiến thức ERP, workspace mẫu |
| `parthasarathy-erp-fundamentals`, `oleary-erp-systems-lifecycle`, `wallace-erp-implementation`, `elbardan-erp-governance-audit` | Kiến thức ERP tóm lược từ 4 cuốn sách (phương pháp book-to-skill) |

## Cài đặt

```bash
cp -r erp-ba-* *-erp-* ~/.claude/skills/
python3 ~/.claude/skills/erp-ba-core/scripts/selftest.py   # kiểm tra công cụ
```

Các skill bước tìm `erp-ba-core` ở thư mục cạnh chúng — luôn cài đủ bộ trong cùng một thư mục skill.

## Lưu ý

- Các skill sách là bản tóm lược và diễn giải lại (không chép nguyên văn) từ sách có bản quyền — chỉ dùng nội bộ, không công khai repo.
- Luật trong `erp-ba-core/references/regulations/` cập nhật đến 20/10/2026 — kiểm tra lại hiệu lực khi dùng cho dự án.
- `erp-ba-workspace/evals/` chứa kịch bản đánh giá (chưa chạy).
