---
doc: issue-log
project: {{PROJECT}}
status: Draft
version: 0.1
updated: {{DATE}}
---

# Nhật ký câu hỏi – giả định – quyết định – mâu thuẫn – thay đổi — {{PROJECT}}

<!-- HƯỚNG DẪN
- Đây là nơi DUY NHẤT ghi câu hỏi mở. Marker [CẦN XÁC NHẬN: Q-…] / [ĐỀ XUẤT → Q-…] trong tài liệu phải trỏ về đây.
- Không bao giờ tự trả lời Q bằng suy đoán. Khi khách hàng trả lời: ghi câu trả lời + nguồn (MTG/email = SRC), chuyển trạng thái "Đã trả lời", tạo DEC nếu là quyết định phạm vi/quy tắc, rồi cập nhật tài liệu và gỡ marker.
- Mức ảnh hưởng: Chặn (không viết tiếp được phần liên quan) / Cao / Trung bình / Thấp.
-->

## 1. Câu hỏi mở (Q)

| ID | Câu hỏi | Ngữ cảnh & ảnh hưởng (REQ/FN/BR liên quan) | Phương án gợi ý (nếu có) | Hỏi ai | Mức ảnh hưởng | Hạn | Trạng thái | Câu trả lời | Nguồn trả lời |
|---|---|---|---|---|---|---|---|---|---|
| {{Q-001}} | {{…}} | {{…}} | {{A: … / B: …}} | {{Kế toán trưởng}} | {{Chặn}} | {{dd/MM/yyyy}} | {{Mở}} | {{…}} | {{MTG-…/SRC-…}} |

## 2. Giả định (ASM)

| ID | Giả định | Lý do đặt giả định | Rủi ro nếu sai | Người cần xác nhận | Trạng thái (Đang dùng / Đã xác nhận → DEC / Bị bác bỏ) |
|---|---|---|---|---|---|
| {{ASM-001}} | {{…}} | {{…}} | {{…}} | {{…}} | {{Đang dùng}} |

## 3. Quyết định (DEC)

| ID | Quyết định | Người quyết định | Ngày | Nguồn (MTG/SRC/Q) | Ảnh hưởng (REQ/FN/FEAT) |
|---|---|---|---|---|---|
| {{DEC-001}} | {{…}} | {{…}} | {{dd/MM/yyyy}} | {{Q-…, MTG-…}} | {{…}} |

## 4. Mâu thuẫn (CFL)

<!-- Ghi khi hai nguồn/hai người nói khác nhau, hoặc yêu cầu khách hàng trái chuẩn ERP/luật. KHÔNG tự chọn một bên. -->

| ID | Phát biểu A (nguồn) | Phát biểu B (nguồn) | Ảnh hưởng | Đề xuất xử lý | Q để hỏi | Kết quả (DEC) |
|---|---|---|---|---|---|---|
| {{CFL-001}} | {{… (MTG-001 L12)}} | {{… (SRC-003)}} | {{…}} | {{…}} | {{Q-…}} | {{DEC-…}} |

## 5. Thay đổi (CHG)

| ID | Nội dung thay đổi | Người yêu cầu – nguồn | Ngày | Phân tích ảnh hưởng (REQ/FN/catalog bị ảnh hưởng) | Quyết định | Phiên bản tài liệu áp dụng |
|---|---|---|---|---|---|---|
| {{CHG-001}} | {{…}} | {{…}} | {{dd/MM/yyyy}} | {{…}} | {{Chấp nhận/Từ chối – DEC-…}} | {{…}} |
