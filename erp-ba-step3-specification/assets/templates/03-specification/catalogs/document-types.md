---
doc: document-types
project: {{PROJECT}}
status: Draft
version: 0.1
updated: {{DATE}}
---

# Loại chứng từ, đánh số, bộ trạng thái — {{PROJECT}}

<!-- HƯỚNG DẪN (xem erp-ba-core/references/conventions.md mục 6, erp-ba-core/references/design-patterns.md — P02, P04, P06)
- Mỗi loại chứng từ giao dịch có đúng một dòng. Bộ trạng thái chỉ dùng mã chuẩn: DRAFT, PENDING, RETURNED, REJECTED, APPROVED, IN_PROGRESS, PARTIAL, COMPLETED, POSTED, CLOSED, CANCELLED, REVERSED.
- Chuyển trạng thái chi tiết nằm ở mục 7 của file FN tương ứng và PHẢI khớp bộ trạng thái ở đây.
-->

| ID | Tên chứng từ | Module | Mẫu đánh số | Bộ trạng thái | Ảnh hưởng khi hoàn tất (kho / công nợ / sổ cái / ngân sách) | Cần duyệt? | Tạo từ | Sinh ra | FN | Mẫu in | Nguồn |
|---|---|---|---|---|---|---|---|---|---|---|---|
| {{DOC-PO}} | {{Đơn mua hàng}} | {{PUR}} | {{PO-{CN}-{YYYY}-{#####}, reset theo năm}} | {{DRAFT, PENDING, RETURNED, REJECTED, APPROVED, PARTIAL, COMPLETED, CLOSED, CANCELLED}} | {{Không ghi sổ; ghi nhận cam kết ngân sách}} | {{Có – theo hạn mức}} | {{DOC-PR}} | {{DOC-GRN, DOC-APINV}} | {{FN-PUR-03}} | {{Mẫu đơn đặt hàng}} | {{REQ-…}} |
