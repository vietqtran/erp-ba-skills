# Checklist C3 — Nghiệm thu bước 3 (mức hệ thống): bộ đặc tả tổng

Trả lời **Yes / No / N/A** kèm bằng chứng. Áp dụng cho srs-overview, catalogs và danh sách chức năng. Từng file chức năng dùng C3F (chức năng) hoặc C3R (báo cáo).

| ID | Câu hỏi (Yes/No) | Cách kiểm | Áp dụng cho |
|---|---|---|---|
| C3-01 | Mọi REQ còn hiệu lực (không "Bị loại") được phủ bởi ít nhất một FN/catalog/NFR? | `ba.py trace`: 0 REQ chưa phủ | Tất cả |
| C3-02 | Mọi FN có nguồn REQ, hoặc FEAT/đề xuất đã có DEC xác nhận (không có chức năng "tự thêm")? | `ba.py trace`: 0 FN không nguồn, 0 FN chỉ dựa FEAT chưa có DEC | Tất cả |
| C3-03 | Mỗi module có đủ 5 thành phần: cấu hình/hệ thống, chức năng cho mọi danh mục dùng tới, chức năng cho mọi loại chứng từ, phân quyền & tham số, báo cáo? | srs-overview §3.1 không có ô trống không giải thích | Tất cả |
| C3-04 | Mỗi MD trong catalog có FN quản lý hoặc ghi nguồn đồng bộ; mỗi MD được FN dùng tới đều có trong catalog? | master-data.md ↔ mục 0 các FN | Tất cả |
| C3-05 | Mỗi DOC có mẫu đánh số, bộ trạng thái chuẩn, chỉ rõ tạo từ/sinh ra, FN xử lý; mọi chứng từ nhắc tới trong FN đều có DOC? | document-types.md | Tất cả |
| C3-06 | Mỗi ROLE dùng trong FN có trong catalog; ma trận tổng hợp khớp mục 2.1 của từng FN? | roles-permissions.md §2 ↔ FN §2 | Tất cả |
| C3-07 | Mỗi PRM được tham chiếu có trong catalog với phạm vi, kiểu, giá trị cho phép, mặc định, ảnh hưởng theo từng giá trị, người được sửa? | system-parameters.md | Tất cả |
| C3-08 | Mỗi RPT có file đặc tả (FN loại Báo cáo) qua checklist C3R? | reports.md ↔ functions | Tất cả |
| C3-09 | BR-GEN đã có đủ nhóm: làm tròn, tiền tệ & tỷ giá, đánh số, ngày chứng từ vs ngày ghi sổ, khóa kỳ, xóa/hủy/đảo, lưu vết, múi giờ & định dạng, đa công ty/chi nhánh? | srs-overview §10 | Tất cả |
| C3-10 | Mọi NFR đo được (có chỉ số, ngưỡng, cách kiểm chứng) và có nguồn hoặc Q xác nhận con số mặc định? | srs-overview §11 | Tất cả |
| C3-11 | Luồng chứng từ liên module (srs-overview §2.2) khớp mục 0 (upstream/downstream) của các FN; không có chứng từ "mồ côi"? | So sơ đồ với FN | Tất cả |
| C3-12 | Mỗi INT có trigger, dữ liệu, phương thức, xử lý lỗi & đối soát; mỗi NTF có sự kiện, người nhận, kênh, nội dung? | integrations-notifications.md | Tất cả |
| C3-13 | Chế độ kế toán, phương pháp tính giá, hóa đơn điện tử, đồng tiền hạch toán đã chốt (srs-overview §12) hoặc có Q? | srs-overview §12 | Khi có module tài chính |
| C3-14 | Hạn mức duyệt và quy tắc SoD đã định nghĩa cho mọi chứng từ có duyệt/ghi sổ/thanh toán? | roles-permissions.md §3–§4 | Tất cả |
| C3-15 | Thuật ngữ thống nhất: một khái niệm một tên, khớp glossary; tên vai trò/trạng thái/tham số dùng đúng catalog? | Tìm tên lạ không có trong glossary/catalog | Tất cả |
| C3-16 | Mọi file FN/báo cáo đã chạy checklist C3F/C3R và không còn "No"? | Báo cáo tự kiểm | Tất cả |
| C3-17 | `ba.py lint` 0 Error toàn workspace; `ba.py trace` không còn mục đỏ? | Chạy công cụ | Tất cả |
