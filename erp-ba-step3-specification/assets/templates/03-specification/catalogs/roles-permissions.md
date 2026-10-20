---
doc: roles-permissions
project: {{PROJECT}}
status: Draft
version: 0.1
updated: {{DATE}}
---

# Vai trò, phân quyền, phân tách nhiệm vụ, hạn mức duyệt — {{PROJECT}}

<!-- HƯỚNG DẪN (xem erp-ba-core/references/security-and-parameters.md)
- Vai trò chỉ được định nghĩa ở đây. File chức năng chỉ tham chiếu ROLE-… và mô tả quyền chi tiết theo hành động (mục 2.2 của function spec).
- Ma trận tổng hợp ở mục 2 dùng mức: Chính (thao tác đầy đủ theo FN) / Duyệt / Một phần (ghi rõ ở FN) / Xem / — . Mức ở đây PHẢI khớp mục 2 của từng file chức năng.
- Tên hành động chuẩn: erp-ba-core/references/conventions.md mục 6.
-->

## 1. Danh sách vai trò

| ID | Tên vai trò | Phòng ban | Trách nhiệm chính | Phạm vi dữ liệu mặc định | Số người dùng ước tính | Nguồn |
|---|---|---|---|---|---|---|
| {{ROLE-PUR-STAFF}} | {{Nhân viên mua hàng}} | {{Phòng Mua hàng}} | {{…}} | {{Chi nhánh}} | {{…}} | {{REQ-… / MTG-…}} |

## 2. Ma trận tổng hợp chức năng × vai trò

| FN | {{ROLE-PUR-STAFF}} | {{ROLE-PUR-MGR}} | {{ROLE-ACC-AP}} | {{ROLE-ADMIN}} |
|---|---|---|---|---|
| {{FN-PUR-01}} | {{Chính}} | {{Duyệt}} | {{Xem}} | {{—}} |

## 3. Quy tắc phân tách nhiệm vụ (SoD)

| ID | Hai nhiệm vụ không được do cùng một người thực hiện | Rủi ro | Cách hệ thống kiểm soát (chặn / cảnh báo / báo cáo) | Nguồn |
|---|---|---|---|---|
| {{SOD-01}} | {{Tạo đơn mua hàng ↔ Duyệt chính đơn mua hàng đó}} | {{…}} | {{Chặn: người duyệt ≠ người tạo}} | {{chuẩn / REQ-…}} |

## 4. Hạn mức phê duyệt

<!-- Ngưỡng tiền phải là tham số (PRM) để đổi được mà không sửa code. -->

| Loại chứng từ | Điều kiện (giá trị / loại / phòng ban) | Cấp duyệt 1 | Cấp duyệt 2 | Cấp duyệt 3 | Tham số ngưỡng | Nguồn |
|---|---|---|---|---|---|---|
| {{DOC-PO}} | {{≤ PRM-PUR-001}} | {{ROLE-PUR-MGR}} | {{—}} | {{—}} | {{PRM-PUR-001}} | {{REQ-…}} |

## 5. Chính sách tài khoản & bảo mật đăng nhập

| Hạng mục | Quy định | Nguồn |
|---|---|---|
| Mật khẩu | {{độ dài, độ phức tạp, hết hạn}} | {{…}} |
| Khóa tài khoản | {{số lần sai}} | {{…}} |
| Đăng nhập một lần / 2 lớp | {{…}} | {{…}} |
| Phiên làm việc | {{thời gian chờ}} | {{…}} |
