---
doc: review-report
project: {{PROJECT}}
round: {{N}}
reviewer: {{independent agent / người review}}
status: Draft
updated: {{DATE}}
---

# Báo cáo review độc lập — vòng {{N}} — {{PROJECT}}

<!-- HƯỚNG DẪN (xem erp-ba-step5-review/agents/independent-reviewer.md và skill `erp-ba-step5-review`)
- Reviewer KHÔNG sửa tài liệu đặc tả; chỉ ghi phát hiện. Người viết sửa và điền cột "Xử lý".
- Mức độ: Critical (sai nghiệp vụ/luật, thiếu chức năng được yêu cầu, dev không thể code) / Major (mơ hồ, mâu thuẫn, thiếu quy tắc/trường/luồng quan trọng) / Minor (trình bày, thuật ngữ, thiếu sót nhỏ) / Info (gợi ý).
- Mỗi phát hiện phải có bằng chứng cụ thể (trích dẫn file §, ID, câu gốc của khách hàng).
-->

## 1. Thông tin review

| Mục | Nội dung |
|---|---|
| Phạm vi | {{file / chức năng}} |
| Đầu vào được cung cấp | {{nguồn gốc, tài liệu, checklist}} |
| Góc nhìn đã áp dụng | Dev · QA · Khách hàng/PO · Chuyên gia ERP · Kiểm toán/Bảo mật · Nhất quán |

## 2. Tóm tắt

| Mức độ | Số lượng |
|---|---|
| Critical | {{…}} |
| Major | {{…}} |
| Minor | {{…}} |
| Info | {{…}} |

**Kết luận:** {{PASS (0 Critical, 0 Major) / FAIL}}

## 3. Phát hiện

| ID | Mức độ | Góc nhìn | Vị trí | Vấn đề | Bằng chứng | Đề xuất sửa | Checklist | Xử lý (người viết điền) |
|---|---|---|---|---|---|---|---|---|
| {{RV-R1-01}} | {{Major}} | {{Dev}} | {{functions/PUR/FN-PUR-03….md §9}} | {{…}} | {{…}} | {{…}} | {{C5-DEV-03}} | {{Đã sửa v0.3 / Từ chối – lý do / Chuyển Q-…}} |

## 4. Truy vết mẫu (đi từ yêu cầu gốc tới đặc tả)

| REQ (trích nguyên văn) | Tìm thấy ở | Đúng ý? | Ghi chú |
|---|---|---|---|
| {{REQ-…}} | {{FN-… FR-…}} | {{Có / Lệch / Không thấy}} | {{…}} |

## 5. Kết quả checklist C5

{{Sinh bởi: python3 scripts/ba.py checklist <root> --step 5 --round N}}

## 6. Câu hỏi đề nghị gửi khách hàng

| # | Câu hỏi | Lý do | Đề xuất ghi vào |
|---|---|---|---|
| 1 | {{…}} | {{…}} | {{Q mới}} |
