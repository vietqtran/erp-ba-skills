---
doc: integrations-notifications
project: {{PROJECT}}
status: Draft
version: 0.1
updated: {{DATE}}
---

# Tích hợp hệ thống ngoài & thông báo tự động — {{PROJECT}}

## 1. Tích hợp (INT)

<!-- Mỗi tích hợp phải nói rõ: trigger, dữ liệu, định dạng, xử lý lỗi (thử lại, ghi log, đối soát), ai xử lý khi lỗi. Xem erp-ba-core/references/design-patterns.md — P16. -->

| ID | Hệ thống ngoài | Hướng | Dữ liệu trao đổi | Trigger / tần suất | Phương thức | Xử lý lỗi & đối soát | FN | Nguồn |
|---|---|---|---|---|---|---|---|---|
| {{INT-01}} | {{Nhà cung cấp hóa đơn điện tử}} | {{Ra / Vào / Hai chiều}} | {{…}} | {{Khi phát hành hóa đơn}} | {{API REST}} | {{Thử lại 3 lần, ghi log, màn hình theo dõi lỗi}} | {{FN-…}} | {{REQ-…}} |

## 2. Thông báo tự động (NTF)

| ID | Sự kiện kích hoạt | Người nhận | Kênh | Nội dung mẫu | Thời điểm / lặp lại | FN | Nguồn |
|---|---|---|---|---|---|---|---|
| {{NTF-PUR-01}} | {{Đơn mua hàng chuyển sang Chờ duyệt}} | {{Người duyệt cấp hiện tại}} | {{Trong ứng dụng + email}} | {{"Đơn mua hàng {số} của {người tạo} cần bạn duyệt"}} | {{Ngay khi sự kiện; nhắc lại sau PRM-…}} | {{FN-PUR-03}} | {{REQ-…}} |
