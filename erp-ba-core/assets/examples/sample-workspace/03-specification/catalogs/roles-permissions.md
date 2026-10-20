---
doc: roles-permissions
project: Minh An ERP
status: Ready
version: 1.0
updated: 2026-10-20
---

# Vai trò, phân quyền, phân tách nhiệm vụ, hạn mức duyệt — Minh An ERP

## 1. Danh sách vai trò

| ID | Tên vai trò | Phòng ban | Trách nhiệm chính | Phạm vi dữ liệu mặc định | Số người dùng ước tính | Nguồn |
|---|---|---|---|---|---|---|
| ROLE-PUR-STAFF | Nhân viên mua hàng | Phòng Mua hàng (theo chi nhánh) | Lập, theo dõi đơn mua; tạo, sửa nhà cung cấp | Chi nhánh | 8 | MTG-001 L07, DEC-017 |
| ROLE-PUR-MGR | Trưởng phòng Mua hàng | Phòng Mua hàng | Duyệt cấp 1, đóng, hủy đơn mua; khóa, mở khóa nhà cung cấp | Công ty | 1 | MTG-001 L03, DEC-003, DEC-007, DEC-017 |
| ROLE-DIRECTOR | Giám đốc | Ban giám đốc | Duyệt cấp 2 đơn mua từ ngưỡng | Công ty | 1 | MTG-001 L03 |
| ROLE-ACC | Kế toán | Phòng Kế toán | Xem đơn mua và nhà cung cấp để đối chiếu công nợ | Công ty | 4 | MTG-001 L04 |

## 2. Ma trận tổng hợp chức năng × vai trò

| FN | ROLE-PUR-STAFF | ROLE-PUR-MGR | ROLE-DIRECTOR | ROLE-ACC |
|---|---|---|---|---|
| FN-PUR-01 | Chính | Chính | Xem | Xem |
| FN-PUR-02 | Chính | Duyệt | Duyệt | Xem |
| FN-PUR-03 | Xem | Xem | Xem | Xem |

## 3. Quy tắc phân tách nhiệm vụ (SoD)

| ID | Hai nhiệm vụ không được do cùng một người thực hiện | Rủi ro | Cách hệ thống kiểm soát (chặn / cảnh báo / báo cáo) | Nguồn |
|---|---|---|---|---|
| SOD-01 | Tạo đơn mua hàng ↔ Duyệt đơn mua hàng đó ở bất kỳ cấp nào | Tự đặt hàng không qua kiểm soát | Chặn: người duyệt khác người tạo; Trưởng phòng tự tạo đơn thì cấp 1 chuyển cho Giám đốc | DEC-012 |

## 4. Hạn mức phê duyệt

| Loại chứng từ | Điều kiện (giá trị / loại / phòng ban) | Cấp duyệt 1 | Cấp duyệt 2 | Cấp duyệt 3 | Tham số ngưỡng | Nguồn |
|---|---|---|---|---|---|---|
| DOC-PO | Tổng thanh toán quy đổi VND nhỏ hơn PRM-PUR-001 | ROLE-PUR-MGR | — | — | PRM-PUR-001 | REQ-005, DEC-002 |
| DOC-PO | Tổng thanh toán quy đổi VND từ PRM-PUR-001 trở lên | ROLE-PUR-MGR | ROLE-DIRECTOR | — | PRM-PUR-001 | REQ-006, DEC-002 |

## 5. Chính sách tài khoản & bảo mật đăng nhập

| Hạng mục | Quy định | Nguồn |
|---|---|---|
| Mật khẩu | N/A – theo chính sách chung của nền tảng (SRS Hệ thống), không thuộc phạm vi module Mua hàng | requirements-overview §2.1 |
| Khóa tài khoản | N/A – theo chính sách chung của nền tảng (SRS Hệ thống) | requirements-overview §2.1 |
| Đăng nhập một lần / 2 lớp | N/A – theo chính sách chung của nền tảng (SRS Hệ thống) | requirements-overview §2.1 |
| Phiên làm việc | N/A – theo chính sách chung của nền tảng (SRS Hệ thống) | requirements-overview §2.1 |
