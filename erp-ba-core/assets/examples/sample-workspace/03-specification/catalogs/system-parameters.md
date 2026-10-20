---
doc: system-parameters
project: Minh An ERP
status: Ready
version: 1.0
updated: 2026-10-20
---

# Tham số hệ thống — Minh An ERP

| ID | Tên tham số | Module | Phạm vi | Kiểu | Giá trị cho phép | Mặc định | Hiệu lực theo ngày? | Ai được sửa | Ảnh hưởng (theo từng giá trị) | FN liên quan | Nguồn |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRM-PUR-001 | Ngưỡng tổng thanh toán (VND) của đơn mua cần Giám đốc duyệt | PUR | Công ty | Số tiền VND | Số nguyên ≥ 1 | 100.000.000 | Không | ROLE-PUR-MGR | Tổng thanh toán quy đổi VND nhỏ hơn giá trị: duyệt 1 cấp (ROLE-PUR-MGR). Từ giá trị trở lên: thêm cấp 2 (ROLE-DIRECTOR) | FN-PUR-02 | REQ-005, REQ-006, DEC-002 |
| PRM-PUR-002 | Số ngày cảnh báo trước ngày giao dự kiến | PUR | Công ty | Số nguyên | 0 đến 30 | 3 | Không | ROLE-PUR-MGR | Đơn còn dòng chưa nhận đủ và ngày giao dự kiến nằm trong khoảng [hôm nay; hôm nay + giá trị] được báo là "Sắp đến hạn"; giá trị 0 chỉ báo đơn đến hạn hôm nay | FN-PUR-03 | REQ-016, DEC-008 |
| PRM-PUR-003 | Danh sách tiền tệ được phép trên đơn mua | PUR | Công ty | Danh sách mã tiền tệ ISO 4217 | Mã ISO 4217 hợp lệ, bắt buộc có VND | VND, USD | Không | ROLE-PUR-MGR | Chỉ các mã trong danh sách xuất hiện ở ô Tiền tệ của đơn mua | FN-PUR-02 | REQ-012 |
