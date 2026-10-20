---
doc: master-data
project: Minh An ERP
status: Ready
version: 1.0
updated: 2026-10-20
---

# Danh mục (master data) — Minh An ERP

| ID | Tên danh mục | Module sở hữu | Mô tả | Quy tắc mã | Trường chính | Ngừng dùng / xóa | Duyệt khi tạo-sửa? | Nhập Excel? | FN quản lý | Nguồn |
|---|---|---|---|---|---|---|---|---|---|---|
| MD-VENDOR | Nhà cung cấp | PUR | Đối tác bán hàng hóa cho công ty | Tự sinh NCC-00001, duy nhất toàn công ty | Mã, tên, mã số thuế, địa chỉ, điện thoại, email, người liên hệ, trạng thái (Đang dùng / Khóa) | Không xóa khi đã có đơn mua; khóa thay cho xóa | Không | Có | FN-PUR-01 | REQ-003, REQ-008, REQ-009, REQ-010, DEC-017, SRC-002 |
| MD-ITEM | Hàng hóa | INV | Thiết bị điện công ty mua bán | Theo SRS module Kho | Mã, tên, đơn vị tính, thuế suất GTGT mặc định, trạng thái | Theo SRS module Kho | Theo SRS module Kho | Theo SRS module Kho | Ngoài phạm vi tài liệu này — quản lý trong SRS module Kho | REQ-004 |
| MD-BRANCH | Chi nhánh | SYS | Chi nhánh Hà Nội, Hồ Chí Minh | Theo SRS Hệ thống | Mã, tên, kho mặc định | Theo SRS Hệ thống | Theo SRS Hệ thống | Không | Ngoài phạm vi tài liệu này — quản lý trong SRS Hệ thống | REQ-022 |
| MD-WAREHOUSE | Kho | INV | Kho Hà Nội, kho Hồ Chí Minh | Theo SRS module Kho | Mã, tên, chi nhánh | Theo SRS module Kho | Theo SRS module Kho | Không | Ngoài phạm vi tài liệu này — quản lý trong SRS module Kho | REQ-022 |
| MD-TAXRATE | Thuế suất GTGT | TAX | Danh sách thuế suất GTGT có hiệu lực theo ngày | Theo SRS module Thuế | Mã, tỷ lệ, hiệu lực từ ngày | Theo SRS module Thuế | Theo SRS module Thuế | Không | Ngoài phạm vi tài liệu này — quản lý trong SRS module Thuế | REQ-019 |
