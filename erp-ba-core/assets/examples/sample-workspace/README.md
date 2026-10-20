# Workspace mẫu — Công ty CP Thiết bị Điện Minh An (hư cấu)

Bộ tài liệu mẫu **đã hoàn chỉnh** cho phạm vi nhỏ: module Mua hàng giai đoạn 1 (danh mục nhà cung cấp, đơn mua hàng có duyệt 2 cấp, báo cáo tình hình thực hiện đơn mua). Dùng để:

- Xem mức độ chi tiết "đủ để code" của một đặc tả chức năng: `03-specification/functions/PUR/FN-PUR-02-don-mua-hang.md` (chứng từ có duyệt), `FN-PUR-01-danh-muc-nha-cung-cap.md` (danh mục), `FN-PUR-03-bao-cao-tinh-hinh-thuc-hien-don-mua.md` (báo cáo).
- Xem cách truy vết từ câu nói của khách hàng (biên bản `MTG-001`) → REQ → câu hỏi/quyết định → chức năng → FR/BR/AC.
- Kiểm thử công cụ: `python3 scripts/ba.py lint assets/examples/sample-workspace` và `trace` phải ra 0 lỗi.

Phạm vi này không có bước research (bước 1) vì khách hàng đã xác định nhu cầu cụ thể; các đề xuất của BA được đánh dấu và đã được khách hàng xác nhận qua email `SRC-003`.
