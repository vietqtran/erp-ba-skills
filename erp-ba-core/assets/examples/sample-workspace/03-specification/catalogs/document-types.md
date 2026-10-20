---
doc: document-types
project: Minh An ERP
status: Ready
version: 1.0
updated: 2026-10-20
---

# Loại chứng từ, đánh số, bộ trạng thái — Minh An ERP

| ID | Tên chứng từ | Module | Mẫu đánh số | Bộ trạng thái | Ảnh hưởng khi hoàn tất (kho / công nợ / sổ cái / ngân sách) | Cần duyệt? | Tạo từ | Sinh ra | FN | Mẫu in | Nguồn |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DOC-PO | Đơn mua hàng | PUR | PO-{mã chi nhánh}-{YYYY}-{5 số}, đánh lại từ 00001 mỗi năm theo chi nhánh | DRAFT, PENDING, RETURNED, REJECTED, APPROVED, PARTIAL, COMPLETED, CLOSED, CANCELLED | Không ghi sổ kế toán, không ảnh hưởng tồn kho | Có – theo hạn mức | Không (DEC-001) | DOC-GRN | FN-PUR-02 | Đơn đặt hàng PDF có logo (theo SRC-001) | REQ-001, REQ-005, REQ-006, DEC-001 |
| DOC-GRN | Phiếu nhập kho | INV | Theo SRS module Kho | DRAFT, POSTED, REVERSED | Tăng tồn kho, ghi sổ kế toán | Theo SRS module Kho | DOC-PO | DOC-APINV | Ngoài phạm vi tài liệu này — SRS module Kho | Theo SRS module Kho | DEC-014 |
| DOC-APINV | Hóa đơn mua hàng | AP | Theo SRS module Công nợ | DRAFT, POSTED, REVERSED | Ghi nhận công nợ phải trả | Theo SRS module Công nợ | DOC-PO, DOC-GRN | Không | Ngoài phạm vi tài liệu này — SRS module Công nợ | Không | requirements-overview §2.2 |
