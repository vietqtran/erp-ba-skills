---
doc: report-spec
id: {{FN_ID}}
name: {{FN_NAME}}
module: {{MOD}}
type: Báo cáo
priority: {{Must | Should | Could}}
status: Draft
version: 0.1
updated: {{DATE}}
project: {{PROJECT}}
---

# {{FN_ID}} — {{FN_NAME}}

<!-- HƯỚNG DẪN (xem skill `erp-ba-step3-specification` mục "Báo cáo" và erp-ba-core/references/reports-catalog.md)
- Một file có thể chứa một báo cáo, hoặc một nhóm báo cáo cùng nguồn dữ liệu (mỗi báo cáo lặp lại mục 3–8 với tiêu đề RPT-…).
- Logic lấy số liệu phải đủ để dev viết câu truy vấn: chứng từ nào, trạng thái nào được tính, theo ngày nào (ngày chứng từ hay ngày ghi sổ), quy đổi tỷ giá ra sao.
- Có ví dụ số liệu (mục 8) để QA đối chiếu.
-->

## 0. Thông tin & truy vết

| Mục | Giá trị |
|---|---|
| Báo cáo | {{RPT-… (catalogs/reports.md)}} |
| Nguồn yêu cầu | {{REQ-…}} |
| Mẫu khách hàng cung cấp | {{SRC-… hoặc N/A – lý do}} |
| Bắt buộc theo luật | {{Mẫu số …, căn cứ … / Không}} |
| Chức năng sinh dữ liệu nguồn | {{FN-…}} |

## 1. Mục đích & người dùng

- **Câu hỏi quản trị mà báo cáo trả lời:** {{…}}
- **Người dùng & tần suất:** {{ROLE-… — hằng ngày/tháng/quý}}

## 2. Phân quyền & phạm vi dữ liệu

| Vai trò | Xem | Xuất file | Phạm vi dữ liệu | Trường bị ẩn |
|---|---|---|---|---|
| {{ROLE-…}} | {{✔}} | {{✔}} | {{Chi nhánh}} | {{—}} |

## 3. Tham số lọc

| # | Tham số | Kiểu | Bắt buộc | Mặc định | Giá trị / lookup | Kiểm tra |
|---|---|---|---|---|---|---|
| 1 | {{Từ ngày – Đến ngày}} | {{Ngày}} | {{Có}} | {{Đầu tháng – hôm nay}} | {{—}} | {{Từ ngày ≤ Đến ngày, khoảng tối đa PRM-…}} |

## 4. Bố cục & cột

| # | Cột | Nguồn dữ liệu (bảng.trường) | Công thức / cách tính | Định dạng | Tổng cộng? |
|---|---|---|---|---|---|
| 1 | {{…}} | {{…}} | {{…}} | {{#.##0}} | {{Có}} |

- **Nhóm / tổng phụ:** {{nhóm theo …, tổng phụ theo …}}
- **Sắp xếp:** {{…}}
- **Tiêu đề, chân trang, chữ ký (nếu mẫu luật):** {{…}}

## 5. Logic lấy số liệu

| Mục | Quy tắc |
|---|---|
| Chứng từ được tính | {{DOC-… ở trạng thái POSTED; loại trừ CANCELLED/REVERSED}} |
| Ngày dùng để lọc | {{Ngày ghi sổ}} |
| Số dư đầu kỳ | {{cách tính}} |
| Quy đổi tiền tệ | {{theo tỷ giá ghi sổ / đánh giá lại}} |
| Xử lý dữ liệu đặc biệt | {{…}} |

## 6. Tương tác

| Hành vi | Đặc tả |
|---|---|
| Xem chi tiết (drill-down) | {{bấm vào … mở …}} |
| Xuất file | {{Excel / PDF; giữ định dạng mẫu}} |
| Lưu bộ lọc / lập lịch gửi | {{…}} |

## 7. Hiệu năng & khối lượng

| Mục | Yêu cầu |
|---|---|
| Khối lượng dữ liệu dự kiến | {{…}} |
| Thời gian chạy tối đa | {{…}} |
| Chạy trực tuyến hay nền / snapshot | {{…}} |

## 8. Ví dụ số liệu kiểm tra

| Dữ liệu đầu vào (chứng từ mẫu) | Kết quả mong đợi trên báo cáo |
|---|---|
| {{…}} | {{…}} |

## 9. Thông báo & lỗi

| ID | Điều kiện | Nội dung | Loại |
|---|---|---|---|
| {{MSG-MOD-NN-01}} | {{Không có dữ liệu}} | "{{Không có dữ liệu phù hợp điều kiện lọc}}" | {{Thông tin}} |

## 10. Câu hỏi mở, giả định, quyết định liên quan

| ID | Nội dung | Trạng thái |
|---|---|---|
| {{Q-…}} | {{…}} | {{Mở}} |

## 11. Lịch sử thay đổi

| Phiên bản | Ngày | Người sửa | Nội dung | CHG / vòng review |
|---|---|---|---|---|
| 0.1 | {{DATE}} | {{…}} | Tạo mới | — |
