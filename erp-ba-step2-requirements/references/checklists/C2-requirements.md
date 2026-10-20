# Checklist C2 — Nghiệm thu bước 2: Thu thập yêu cầu & tài liệu tổng quan

Trả lời **Yes / No / N/A** kèm bằng chứng. Bước 2 đạt khi không còn "No" (câu hỏi mở được phép tồn tại nếu đã ghi Q đầy đủ — C2-15).

| ID | Câu hỏi (Yes/No) | Cách kiểm | Áp dụng cho |
|---|---|---|---|
| C2-01 | Mọi nguồn (biên bản họp, file khách hàng, email) đã đăng ký trong source-register với ID? | So thư mục 00-inputs với source-register | Tất cả |
| C2-02 | MỌI ý trong biên bản/tài liệu nguồn đã được xử lý: thành REQ, hoặc Q/DEC/ASM, hoặc ghi "không phải yêu cầu" kèm lý do? | Đi từng dòng L.. của từng MTG | Tất cả |
| C2-03 | Mỗi REQ là nguyên tử (một ý), có trích nguyên văn và nguồn (MTG Lnn / SRC vị trí)? | Soát requirement-register | Tất cả |
| C2-04 | Cột "Yêu cầu" diễn đạt lại đúng ý trích dẫn — không thêm, không bớt, không đổi nghĩa? | So từng REQ với trích dẫn | Tất cả |
| C2-05 | Mỗi REQ đã phân loại (BUS/STK/FR/NFR/DATA/RPT/INT/CON/MIG), gán module và BP? | Không có ô trống | Tất cả |
| C2-06 | Không có REQ nào do AI/BA tự thêm; đề xuất từ research/chuẩn ERP đều mang [ĐỀ XUẤT → Q-…]? | Mọi REQ có trích dẫn khách hàng | Tất cả |
| C2-07 | Mâu thuẫn giữa các nguồn/người nói (và yêu cầu trái chuẩn ERP/luật) đã ghi CFL, không tự chọn một bên? | issue-log §4 | Tất cả |
| C2-08 | Phạm vi trong/ngoài, đơn vị tổ chức áp dụng, giai đoạn đã rõ và có nguồn? | requirements-overview §2 | Tất cả |
| C2-09 | Có danh sách luồng tổng quan (BP) ở §5, và mỗi BP có sơ đồ TO-BE swimlane theo khung chuẩn (erp-ba-core/references/processes, industries) cùng bảng luồng chi tiết (FL) ghi vai trò, bắt đầu → kết thúc, chứng từ, module, REQ? | requirements-overview §5–§6 | Tất cả |
| C2-19 | Mỗi REQ chức năng thuộc ít nhất một luồng chi tiết, và mỗi nhánh nghiệp vụ khách hàng mô tả đều là (hoặc nằm trong) một luồng chi tiết? | Đối chiếu sổ yêu cầu và biên bản với bảng FL | Tất cả |
| C2-10 | Điểm khác quy trình ERP chuẩn đã nêu rõ kèm lý do/nguồn (khách hàng yêu cầu), hoặc ghi "không khác chuẩn"? | Dòng "Khác biệt so với chuẩn" của mỗi BP | Tất cả |
| C2-11 | Bảng 5 thành phần ERP (§8) không có ô trống: mỗi ô có REQ hoặc Q? | requirements-overview §8 | Tất cả |
| C2-12 | Cơ cấu tổ chức, các bên liên quan, cấp duyệt đã xác định (hoặc có Q)? | requirements-overview §3 | Tất cả |
| C2-13 | NFR tổng quan (quy mô người dùng, khối lượng giao dịch, hạ tầng, bảo mật, pháp lý) đã ghi nhận hoặc có Q? | requirements-overview §9 | Tất cả |
| C2-14 | Tích hợp & chuyển đổi dữ liệu đã nêu (hoặc ghi rõ không có, có nguồn)? | requirements-overview §10 | Tất cả |
| C2-15 | Mỗi Q có người cần hỏi, mức ảnh hưởng, hạn; các Q mức "Chặn" đã được liệt kê ở §12? | issue-log §1 | Tất cả |
| C2-16 | Chế độ kế toán / quy định pháp lý áp dụng đã xác định hoặc có Q? | requirements-overview §9, issue-log | Khi có module tài chính/HR |
| C2-17 | Thuật ngữ khách hàng dùng đã ghi vào glossary và ánh xạ sang thuật ngữ chuẩn? | catalogs/glossary.md | Tất cả |
| C2-18 | `ba.py lint` không còn Error trong 00-inputs và 02-requirements? | Chạy lint | Tất cả |
