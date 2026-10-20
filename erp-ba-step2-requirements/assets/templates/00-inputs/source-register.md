---
doc: source-register
project: {{PROJECT}}
status: Draft
version: 0.1
updated: {{DATE}}
---

# Sổ đăng ký nguồn đầu vào — {{PROJECT}}

<!-- HƯỚNG DẪN
- Đăng ký MỌI nguồn trước khi trích yêu cầu: biên bản họp, file Excel/biểu mẫu khách hàng gửi, email, ảnh chụp màn hình hệ thống cũ, quy trình nội bộ, hợp đồng/phụ lục phạm vi.
- Mỗi yêu cầu (REQ) sau này phải trỏ về một SRC/MTG ở đây. Không có nguồn = không có yêu cầu.
- "Độ tin cậy": Cao (văn bản chính thức/được ký), Trung bình (biên bản họp, email), Thấp (ghi chú miệng, suy luận).
-->

## 1. Biên bản họp

| ID | Ngày | Chủ đề | Thành phần phía khách hàng (vai trò) | File biên bản | Ghi chú |
|---|---|---|---|---|---|
| {{MTG-001}} | {{dd/MM/yyyy}} | {{chủ đề}} | {{Tên – chức danh}} | `meetings/{{MTG-001-yyyy-mm-dd}}.md` | {{ghi chú}} |

## 2. Tài liệu / dữ liệu khách hàng cung cấp

| ID | Tên tài liệu | Loại | Người cung cấp | Ngày nhận | Đường dẫn | Độ tin cậy | Ghi chú |
|---|---|---|---|---|---|---|---|
| {{SRC-001}} | {{tên}} | {{Biểu mẫu / Quy trình / Báo cáo mẫu / Email / Ảnh chụp / Hợp đồng}} | {{tên – chức danh}} | {{dd/MM/yyyy}} | `files/{{tên-file}}` | {{Cao/Trung bình/Thấp}} | {{ghi chú}} |

## 3. Nguồn bên ngoài dùng trong research (không phải yêu cầu khách hàng)

<!-- Nguồn research (website đối thủ, văn bản pháp luật) được trích trong 01-research; chỉ đăng ký ở đây nếu dùng làm căn cứ cho FR/BR (ví dụ văn bản luật). -->

| ID | Tên nguồn | URL | Ngày truy cập | Dùng cho |
|---|---|---|---|---|
| {{SRC-101}} | {{Thông tư …}} | {{URL}} | {{dd/MM/yyyy}} | {{BR-GEN-…}} |
