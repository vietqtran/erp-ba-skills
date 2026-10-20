# Checklist C3R — Nghiệm thu từng đặc tả báo cáo

Trả lời **Yes / No / N/A** cho từng file `type: Báo cáo`.

| ID | Câu hỏi (Yes/No) | Cách kiểm | Áp dụng cho |
|---|---|---|---|
| C3R-01 | Có nguồn REQ (hoặc mẫu khách hàng SRC), RPT trong catalog, mục đích & câu hỏi quản trị, người dùng, tần suất? | Mục 0–1 | Báo cáo |
| C3R-02 | Phân quyền xem/xuất và phạm vi dữ liệu theo vai trò đã nêu? | Mục 2 | Báo cáo |
| C3R-03 | Mọi tham số lọc có kiểu, bắt buộc, mặc định, giá trị/lookup, kiểm tra? | Mục 3 | Báo cáo |
| C3R-04 | Mọi cột có nguồn dữ liệu (bảng.trường) hoặc công thức, định dạng, có/không tổng cộng; nhóm, tổng phụ, sắp xếp đã rõ? | Mục 4 | Báo cáo |
| C3R-05 | Logic lấy số liệu đủ để viết truy vấn: chứng từ & trạng thái được tính, ngày lọc, số dư đầu kỳ, quy đổi tiền tệ, loại trừ? | Mục 5 | Báo cáo |
| C3R-06 | Báo cáo theo mẫu luật: đúng mẫu số, căn cứ còn hiệu lực, đủ chỉ tiêu và chữ ký? | Mục 0, 4 ↔ erp-ba-core/references/regulations | Khi bắt buộc theo luật |
| C3R-07 | Drill-down, xuất file, lưu bộ lọc/lập lịch đã đặc tả (hoặc N/A có lý do)? | Mục 6 | Báo cáo |
| C3R-08 | Khối lượng dữ liệu, thời gian chạy tối đa, chạy trực tuyến/nền đã nêu bằng con số? | Mục 7 | Báo cáo |
| C3R-09 | Có ví dụ số liệu (chứng từ mẫu → kết quả) để QA đối chiếu? | Mục 8 | Báo cáo |
| C3R-10 | Đóng vai dev/QA: viết được truy vấn và test case mà không cần hỏi lại? | Tự thử | Báo cáo |
| C3R-11 | Không còn placeholder/TODO/marker chưa đóng? | `ba.py lint` | Báo cáo |
