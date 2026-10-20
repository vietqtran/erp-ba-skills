---
doc: feature-catalog
project: {{PROJECT}}
status: Draft
version: 0.1
updated: {{DATE}}
---

# Danh mục tính năng ứng viên (Feature catalog) — {{PROJECT}}

<!-- HƯỚNG DẪN (xem skill `erp-ba-step1-research`)
- Mỗi dòng = một tính năng có thể kiểm chứng. Không ghi chung chung "quản lý kho".
- "Thành phần ERP": HT (hệ thống/nền tảng), DM (danh mục), NV (nghiệp vụ), PQ (phân quyền & tham số), BC (báo cáo), TI (tiện ích/tích hợp).
- "Loại": Chuẩn ERP (mọi ERP đều có) / Đặc thù ngành / Khác biệt cạnh tranh.
- Cột đối thủ: Có / Một phần / Không / Không rõ — kèm số nguồn. Không có nguồn thì ghi "Không rõ", không suy đoán.
- MoSCoW: M (Must) / S (Should) / C (Could) / W (Won't lần này). Ghi lý do ngắn.
- Trạng thái: Đề xuất (mặc định) / Đã xác nhận (có DEC) / Bị loại (có DEC). FEAT chỉ được dùng làm nguồn cho FN khi đã có DEC, hoặc FN phải mang marker [ĐỀ XUẤT → Q-…].
-->

## 1. Danh sách đối thủ dùng trong so sánh

| Mã | Sản phẩm – Hãng | Nguồn chính |
|---|---|---|
| C1 | {{…}} | [{{n}}] |
| C2 | {{…}} | [{{n}}] |

## 2. Tính năng

| ID | Module | Tính năng | Mô tả ngắn | Thành phần ERP | Loại | C1 | C2 | C3 | C4 | C5 | Nguồn | Demo | Sản phẩm | Lý do ưu tiên | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| {{FEAT-PUR-01}} | {{PUR}} | {{…}} | {{…}} | {{NV}} | {{Chuẩn ERP}} | {{Có [3]}} | {{Không rõ}} | {{…}} | {{…}} | {{…}} | [{{n}}] | {{M}} | {{M}} | {{…}} | Đề xuất |

## 3. Kiểm tra độ phủ theo module × thành phần ERP

| Module | HT | DM | NV | PQ | BC | TI | Ghi chú thiếu |
|---|---|---|---|---|---|---|---|
| {{PUR}} | {{số FEAT}} | {{…}} | {{…}} | {{…}} | {{…}} | {{…}} | {{…}} |

## Nguồn tham khảo

[1] {{Tiêu đề — URL (truy cập dd/MM/yyyy)}}
