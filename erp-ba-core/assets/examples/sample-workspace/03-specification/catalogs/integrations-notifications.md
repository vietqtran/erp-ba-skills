---
doc: integrations-notifications
project: Minh An ERP
status: Ready
version: 1.0
updated: 2026-10-20
---

# Tích hợp hệ thống ngoài & thông báo tự động — Minh An ERP

## 1. Tích hợp (INT)

N/A – giai đoạn 1 không tích hợp hệ thống ngoài (MTG-001 L18, requirements-overview §10). Cập nhật số lượng đã nhận từ phiếu nhập kho là tích hợp nội bộ giữa hai module, đặc tả tại FN-PUR-02 §14.1.

## 2. Thông báo tự động (NTF)

| ID | Sự kiện kích hoạt | Người nhận | Kênh | Nội dung mẫu | Thời điểm / lặp lại | FN | Nguồn |
|---|---|---|---|---|---|---|---|
| NTF-PUR-01 | Đơn mua chuyển sang PENDING hoặc chuyển sang cấp duyệt tiếp theo | Người dùng có vai trò của cấp duyệt hiện tại | Trong ứng dụng và email | "Đơn mua hàng {số đơn} của {người tạo}, tổng thanh toán {tổng tiền} {tiền tệ}, cần anh/chị duyệt" | Ngay khi sự kiện xảy ra, không lặp lại | FN-PUR-02 | REQ-021, DEC-015 |
| NTF-PUR-02 | Đơn mua được duyệt cấp cuối, bị trả lại, bị từ chối, bị đóng hoặc bị hủy | Người tạo đơn | Trong ứng dụng và email | "Đơn mua hàng {số đơn} đã {hành động} bởi {người thực hiện}. Lý do: {lý do}" | Ngay khi sự kiện xảy ra | FN-PUR-02 | DEC-015 |
