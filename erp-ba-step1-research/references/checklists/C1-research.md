# Checklist C1 — Nghiệm thu bước 1: Research

Trả lời từng câu bằng **Yes / No / N/A**. Yes phải kèm bằng chứng (file + mục/ID). N/A phải kèm lý do. Bước 1 đạt khi không còn câu "No".

| ID | Câu hỏi (Yes/No) | Cách kiểm | Áp dụng cho |
|---|---|---|---|
| C1-01 | Mục đích research (demo/tài liệu sản phẩm), ngành, phân khúc, phạm vi module dự kiến đã ghi rõ ở mục 0? | Đọc research-report §0 | Tất cả |
| C1-02 | Mỗi câu hỏi research (RQ) đã được trả lời ở một mục cụ thể hoặc chuyển thành câu hỏi khảo sát ở §10? | Đối chiếu bảng RQ với các mục | Tất cả |
| C1-03 | Đã phân tích ít nhất 5 sản phẩm/đối thủ liên quan (ưu tiên ≥2 Việt Nam, ≥2 quốc tế nếu tồn tại), mỗi sản phẩm có nguồn chính thức? | Đếm dòng research-report §6 và nguồn | Tất cả |
| C1-04 | Mọi khẳng định về tính năng đối thủ có nguồn; chỗ không có nguồn ghi "Không rõ" thay vì suy đoán? | Soát cột đối thủ trong feature-catalog | Tất cả |
| C1-05 | Feature catalog phủ đủ 5 thành phần ERP (hệ thống, danh mục, nghiệp vụ, phân quyền & tham số, báo cáo) cho MỖI module trong phạm vi? | Bảng độ phủ feature-catalog §3 không có ô trống không giải thích | Tất cả |
| C1-06 | Mỗi FEAT có module, mô tả kiểm chứng được, loại (chuẩn/đặc thù/khác biệt), nguồn, MoSCoW cho demo & sản phẩm kèm lý do? | Soát từng dòng FEAT | Tất cả |
| C1-07 | Quy trình đặc thù ngành đã liệt kê và đối chiếu với thư viện quy trình chuẩn (erp-ba-core/references/processes, erp-ba-core/references/industries)? | research-report §3 có cột tham chiếu chuẩn | Tất cả |
| C1-08 | Quy định pháp lý liên quan có số hiệu, hiệu lực, tình trạng, nguồn; đã kiểm tra văn bản thay thế/sửa đổi mới nhất tại thời điểm research? | research-report §4 | Tất cả |
| C1-09 | Không có số liệu/thống kê/khẳng định nào thiếu nguồn; mục chưa xác minh được đánh dấu ở §11? | Soát toàn văn, đếm [n] | Tất cả |
| C1-10 | Có bộ câu hỏi khảo sát khách hàng theo nhóm quy trình (agenda bước 2), mỗi câu nói rõ ảnh hưởng thiết kế? | research-report §10 | Tất cả |
| C1-11 | Thuật ngữ ngành (VI–EN) đã thu thập để đưa vào glossary dự án? | research-report §9 | Tất cả |
| C1-12 | Đề xuất phạm vi demo/MVP có lý do, và mọi FEAT đều ở trạng thái "Đề xuất" (chưa coi là yêu cầu khách hàng)? | research-report §8, cột Trạng thái FEAT | Tất cả |
| C1-13 | `ba.py lint` không còn Error trong 01-research (không placeholder, không TODO/TBD)? | Chạy lint | Tất cả |
