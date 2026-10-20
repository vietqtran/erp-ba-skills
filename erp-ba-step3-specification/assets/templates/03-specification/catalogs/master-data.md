---
doc: master-data
project: {{PROJECT}}
status: Draft
version: 0.1
updated: {{DATE}}
---

# Danh mục (master data) — {{PROJECT}}

<!-- HƯỚNG DẪN (xem erp-ba-core/references/design-patterns.md — P01)
- Mỗi danh mục được dùng ở bất kỳ chức năng nào PHẢI có ở đây, và PHẢI có chức năng quản lý (FN loại Danh mục) hoặc ghi rõ nguồn đồng bộ.
- Chi tiết trường dữ liệu nằm trong file FN quản lý danh mục đó.
-->

| ID | Tên danh mục | Module sở hữu | Mô tả | Quy tắc mã | Trường chính | Ngừng dùng / xóa | Duyệt khi tạo-sửa? | Nhập Excel? | FN quản lý | Nguồn |
|---|---|---|---|---|---|---|---|---|---|---|
| {{MD-VENDOR}} | {{Nhà cung cấp}} | {{PUR}} | {{…}} | {{Tự sinh NCC-00001 / nhập tay, duy nhất toàn công ty}} | {{Mã, tên, MST, địa chỉ, điều khoản thanh toán, tài khoản công nợ}} | {{Không xóa khi đã phát sinh chứng từ; chỉ Ngừng dùng}} | {{Có/Không}} | {{Có}} | {{FN-PUR-01}} | {{REQ-…}} |
