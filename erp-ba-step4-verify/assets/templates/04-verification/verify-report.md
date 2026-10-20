---
doc: verify-report
project: {{PROJECT}}
round: {{N}}
status: Draft
updated: {{DATE}}
---

# Báo cáo tự kiểm — vòng {{N}} — {{PROJECT}}

<!-- HƯỚNG DẪN (xem skill `erp-ba-step4-verify`)
- Tạo khung bằng: python3 scripts/ba.py checklist <root> --step <1|2|3|4> --round <N>  (sinh sẵn mục 4 với đủ câu hỏi checklist)
- Mỗi câu checklist trả lời Yes / No / N/A. "Yes" phải có bằng chứng (file + mục/ID). "N/A" phải có lý do. Không được trả lời Yes khi chưa kiểm.
- Mục 3 là 4 câu hỏi bắt buộc của BA — trả lời bằng nội dung cụ thể, không trả lời chung chung.
-->

## 1. Phạm vi kiểm

| Mục | Nội dung |
|---|---|
| Bước được kiểm | {{1 / 2 / 3 / toàn bộ}} |
| File / chức năng | {{…}} |
| Nguồn gốc đã đọc lại | {{MTG-…, SRC-…}} |

## 2. Kết quả công cụ tự động

| Công cụ | Lỗi (Error) | Cảnh báo (Warning) | Ghi chú |
|---|---|---|---|
| `ba.py lint` | {{…}} | {{…}} | {{…}} |
| `ba.py trace` — REQ chưa được phủ | {{…}} | — | {{danh sách}} |
| `ba.py trace` — FN không có nguồn | {{…}} | — | {{danh sách}} |
| Marker còn mở ([CẦN XÁC NHẬN] / [ĐỀ XUẤT]) | {{…}} | — | {{danh sách Q}} |

## 3. Bốn câu hỏi bắt buộc

### 3.1 Bạn có thắc mắc hay chưa rõ chỗ nào không?

| # | Chỗ chưa rõ (file §) | Vì sao chưa rõ | Đã ghi Q |
|---|---|---|---|
| 1 | {{…}} | {{…}} | {{Q-…}} |

### 3.2 Có chỗ nào cần xác nhận lại với khách hàng không?

| # | Nội dung cần xác nhận | Loại (Đề xuất / Giả định / Mâu thuẫn / Con số) | ID |
|---|---|---|---|
| 1 | {{…}} | {{…}} | {{Q-… / ASM-… / CFL-…}} |

### 3.3 Đối chiếu với yêu cầu ban đầu: có lệch, thiếu, thừa không?

**Thiếu** (yêu cầu gốc chưa được phản ánh):

| REQ / ý trong biên bản | Hiện trạng | Hành động |
|---|---|---|
| {{…}} | {{…}} | {{…}} |

**Thừa** (nội dung không có nguồn khách hàng):

| Vị trí | Nội dung | Hành động (gắn [ĐỀ XUẤT → Q] / xóa) |
|---|---|---|
| {{…}} | {{…}} | {{…}} |

**Lệch** (ý nghĩa khác trích dẫn gốc):

| Vị trí | Trích dẫn gốc | Nội dung trong tài liệu | Hành động |
|---|---|---|---|
| {{…}} | {{…}} | {{…}} | {{…}} |

### 3.4 Checklist đã xong hết chưa? Template đã điền đủ chưa?

{{Tổng hợp từ mục 4 và lint: số câu Yes/No/N/A; các mục template còn trống.}}

## 4. Kết quả checklist

{{Sinh bởi ba.py checklist — điền cột Kết quả / Bằng chứng / Hành động.}}

## 5. Phát hiện & xử lý

| ID | Mức độ | Vị trí | Vấn đề | Đã sửa? | Ghi chú |
|---|---|---|---|---|---|
| {{VF-R1-01}} | {{Critical / Major / Minor}} | {{…}} | {{…}} | {{Có / Không – lý do}} | {{…}} |

## 6. Kết luận

- **Kết quả:** {{PASS / FAIL}}
- **Điều kiện PASS:** lint 0 Error; trace 0 REQ chưa phủ & 0 FN không nguồn; mọi câu checklist Yes hoặc N/A có lý do; mọi Q chặn đã được trả lời hoặc tài liệu giữ trạng thái In Review kèm danh sách câu hỏi gửi khách hàng.
- **Việc cho vòng sau / chuyển bước 5:** {{…}}
