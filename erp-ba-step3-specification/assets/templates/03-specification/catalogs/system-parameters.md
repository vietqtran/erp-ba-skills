---
doc: system-parameters
project: {{PROJECT}}
status: Draft
version: 0.1
updated: {{DATE}}
---

# Tham số hệ thống — {{PROJECT}}

<!-- HƯỚNG DẪN (xem erp-ba-core/references/security-and-parameters.md — Phần B)
- Mọi giá trị nghiệp vụ có thể thay đổi theo khách hàng/thời gian (ngưỡng, tỷ lệ, chính sách, bật/tắt bước) PHẢI là tham số ở đây, không viết cứng trong FR/BR.
- "Hiệu lực theo ngày" = Có khi giá trị thay đổi theo luật/thời điểm (thuế suất, mức đóng bảo hiểm…): hệ thống lưu lịch sử giá trị và áp dụng theo ngày chứng từ.
- Cột "Ảnh hưởng" mô tả hành vi theo TỪNG giá trị.
-->

| ID | Tên tham số | Module | Phạm vi | Kiểu | Giá trị cho phép | Mặc định | Hiệu lực theo ngày? | Ai được sửa | Ảnh hưởng (theo từng giá trị) | FN liên quan | Nguồn |
|---|---|---|---|---|---|---|---|---|---|---|---|
| {{PRM-PUR-001}} | {{Ngưỡng giá trị đơn mua hàng cần duyệt cấp 2}} | {{PUR}} | {{Công ty}} | {{Số tiền (VND)}} | {{≥ 0}} | {{50.000.000 [CẦN XÁC NHẬN: Q-…]}} | {{Không}} | {{ROLE-ADMIN}} | {{Tổng tiền > giá trị → thêm cấp duyệt ROLE-DIRECTOR}} | {{FN-PUR-03}} | {{REQ-…}} |
