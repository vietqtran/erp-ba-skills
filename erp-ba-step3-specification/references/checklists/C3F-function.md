# Checklist C3F — Nghiệm thu từng file đặc tả chức năng

Trả lời **Yes / No / N/A** cho từng chức năng. Cột "Áp dụng cho" lọc theo `type` trong frontmatter của file (Danh mục, Chứng từ, Phê duyệt, Cấu hình, Tích hợp, Tác vụ nền, Tiện ích); "Tất cả" = mọi loại trừ Báo cáo (báo cáo dùng C3R). Câu cuối (C3F-30, C3F-31) là phép thử thật: tự đóng vai dev/QA và liệt kê câu hỏi sẽ phải hỏi BA — có bất kỳ câu nào thì trả lời No.

| ID | Câu hỏi (Yes/No) | Cách kiểm | Áp dụng cho |
|---|---|---|---|
| C3F-01 | Mục 0 có nguồn REQ (hoặc FEAT/DEC), pattern ERP, tham chiếu chuẩn, upstream/downstream, DOC/MD/PRM/RPT liên quan? | Mục 0 đủ dòng | Tất cả |
| C3F-02 | Phạm vi trong/ngoài rõ; không có tính năng nào không có nguồn (nếu có → [ĐỀ XUẤT → Q-…])? | Mục 1, so với REQ | Tất cả |
| C3F-03 | Trigger, tiền điều kiện, hậu điều kiện (kể cả dữ liệu module khác) đã nêu? | Mục 1 | Tất cả |
| C3F-04 | Liệt kê đủ vai trò chính VÀ vai trò thao tác một phần / chỉ xem / hệ thống, mỗi vai trò nói rõ được làm gì? | Mục 2.1 | Tất cả |
| C3F-05 | Ma trận quyền có đủ hành động liên quan (theo danh sách hành động chuẩn) kèm phạm vi dữ liệu, khớp ma trận tổng hợp trong catalog? | Mục 2.2 ↔ roles-permissions.md | Tất cả |
| C3F-06 | Phân quyền trường dữ liệu và SoD/hạn mức duyệt đã nêu (hoặc N/A có lý do)? | Mục 2.3–2.4 | Tất cả |
| C3F-07 | Mỗi vai trò chính có ít nhất một user story; mỗi user story có ít nhất một AC dạng Cho trước/Khi/Thì với giá trị cụ thể, đo được? | Mục 3 | Tất cả |
| C3F-08 | AC phủ luồng chính, các luồng thay thế và ngoại lệ quan trọng; mỗi FR có ít nhất một AC kiểm chứng? | Mục 3 ↔ mục 4, 8 | Tất cả |
| C3F-09 | Có sơ đồ swimlane (subgraph theo vai trò) và nó khớp bảng luồng chính? | Mục 4.1 ↔ 4.2 | Tất cả |
| C3F-10 | Có sơ đồ quyết định: mọi điều kiện rẽ nhánh trong BR là một hình thoi, mọi nhánh có nhãn và kết thúc ở kết quả cụ thể (MSG/trạng thái)? | Mục 5 ↔ mục 9 | Tất cả |
| C3F-11 | Có sequence diagram thể hiện người dùng → giao diện → dịch vụ → CSDL → module khác/hệ thống ngoài/thông báo, gồm kiểm tra, lưu, ghi sổ, nhánh lỗi? | Mục 6 | Tất cả |
| C3F-12 | Có sơ đồ trạng thái + bảng chuyển trạng thái (từ, hành động, đến, vai trò, điều kiện, tác động) + quyền sửa trường theo trạng thái; bộ trạng thái khớp DOC catalog; không có trạng thái cụt? | Mục 7 ↔ document-types.md | Chứng từ, Phê duyệt |
| C3F-13 | Luồng thay thế và ngoại lệ đã liệt kê; mỗi ngoại lệ có MSG? | Mục 4.3–4.4 | Tất cả |
| C3F-14 | Mọi khối Mermaid render được (lint không báo lỗi cú pháp)? | `ba.py lint` | Tất cả |
| C3F-15 | Mỗi FR là một yêu cầu kiểm thử được, dùng PHẢI/KHÔNG ĐƯỢC/NÊN/ĐƯỢC PHÉP, có nguồn và AC? | Mục 8 | Tất cả |
| C3F-16 | Mỗi BR là "điều kiện → kết quả" kiểm thử được, có loại, nguồn, và MSG khi là Validation? | Mục 9 | Tất cả |
| C3F-17 | Mọi công thức viết đầy đủ (toán hạng, đơn vị, tiền tệ, làm tròn, thứ tự làm tròn)? | Mục 9 bảng công thức | Khi có tính toán |
| C3F-18 | Đặc tả trường đủ cho mọi bảng: kiểu, độ dài/độ chính xác, bắt buộc, mặc định, nguồn lookup, kiểm tra, trạng thái được sửa? | Mục 10.2 | Danh mục, Chứng từ, Phê duyệt, Cấu hình |
| C3F-19 | Có ER diagram cho dữ liệu của chức năng (header–lines–danh mục liên quan)? | Mục 10.1 | Danh mục, Chứng từ, Phê duyệt |
| C3F-20 | Ảnh hưởng dữ liệu tới module khác (tồn kho, công nợ, sổ cái, ngân sách, cam kết) và cách hoàn tác khi hủy/đảo đã nêu? | Mục 10.3 | Chứng từ, Phê duyệt, Tác vụ nền |
| C3F-21 | Màn hình danh sách đặc tả cột, bộ lọc, tìm kiếm, sắp xếp, phân trang, hành động đơn lẻ/hàng loạt, xuất file? | Mục 11.1 | Danh mục, Chứng từ, Phê duyệt |
| C3F-22 | Màn hình chi tiết đặc tả bố cục, thứ tự trường, nút theo trạng thái × vai trò và hành vi từng nút? | Mục 11.2 | Danh mục, Chứng từ, Phê duyệt, Cấu hình |
| C3F-23 | Tham số ảnh hưởng chức năng đã liệt kê với hành vi theo TỪNG giá trị; tất cả có trong catalog tham số? | Mục 12 ↔ system-parameters.md | Tất cả |
| C3F-24 | Bút toán Nợ/Có cho từng sự kiện (kể cả hủy/đảo), đúng chế độ kế toán của dự án, Nợ = Có? | Mục 13 | Khi ảnh hưởng tài chính |
| C3F-25 | Tác động liên chức năng, tích hợp ngoài, thông báo đã đặc tả kèm xử lý lỗi/thử lại? | Mục 14 | Tất cả |
| C3F-26 | NFR riêng (đồng thời, khối lượng, hiệu năng, audit, lưu trữ) đo được hoặc tham chiếu NFR chung? | Mục 16 | Tất cả |
| C3F-27 | Bảng MSG đủ cho mọi validation, ngoại lệ, xác nhận; nội dung tiếng Việt rõ, có tham số hiển thị (số chứng từ, giá trị)? | Mục 17 ↔ 4.4, 9 | Tất cả |
| C3F-28 | Tình huống biên đã xử lý: 0/âm, vượt hạn mức/tồn, trùng, đồng thời, kỳ đã khóa, danh mục ngừng dùng, đổi quyền giữa chừng, sửa sau duyệt, đa tiền tệ (nếu có)? | Mục 18.1 | Tất cả |
| C3F-29 | Chức năng theo đúng pattern & quy trình chuẩn ERP đã tham chiếu; mọi điểm khác chuẩn có DEC/REQ làm nguồn? | So với erp-ba-core/references/design-patterns.md, erp-ba-core/references/processes | Tất cả |
| C3F-30 | Đóng vai dev: có thể lập trình mà không cần hỏi BA bất kỳ câu nào? (liệt kê câu hỏi tìm được; có câu nào → No) | Tự thử | Tất cả |
| C3F-31 | Đóng vai QA: có thể viết test case (đầu vào, kết quả mong đợi) từ AC/BR/MSG mà không cần hỏi lại? | Tự thử | Tất cả |
| C3F-32 | Không còn placeholder, TODO, [CẦN XÁC NHẬN]/[ĐỀ XUẤT] chưa đóng (hoặc tài liệu giữ trạng thái In Review và các Q đã có trong issue-log)? | `ba.py lint` | Tất cả |
