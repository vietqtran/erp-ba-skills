# Checklist C5 — Review độc lập (bước 5)

Dùng bởi agent review độc lập (erp-ba-step5-review/agents/independent-reviewer.md). Mỗi góc nhìn là một "người đọc" khác nhau; trả lời **Yes / No / N/A** kèm bằng chứng. Mỗi câu "No" sinh ít nhất một phát hiện RV.

| ID | Câu hỏi (Yes/No) | Cách kiểm | Áp dụng cho |
|---|---|---|---|
| C5-CUS-01 | (Khách hàng/PO) Mỗi yêu cầu gốc tôi đã nói đều có trong tài liệu, đúng ý tôi? | Truy vết mẫu từ trích dẫn REQ tới FN/FR | Tất cả |
| C5-CUS-02 | (Khách hàng/PO) Tài liệu không chứa chức năng/quy tắc tôi không yêu cầu, trừ các mục được đánh dấu đề xuất chờ tôi xác nhận? | Tìm nội dung không nguồn | Tất cả |
| C5-CUS-03 | (Khách hàng/PO) Tài liệu dùng thuật ngữ của doanh nghiệp tôi và mô tả đúng cơ cấu tổ chức, cấp duyệt? | glossary, roles | Tất cả |
| C5-DEV-01 | (Dev) Mô hình dữ liệu và đặc tả trường đủ để tạo bảng, ràng buộc, khóa? | FN §10 | Tất cả |
| C5-DEV-02 | (Dev) Mọi chuyển trạng thái, điều kiện, tác động phụ (kho/công nợ/sổ cái/thông báo) đã rõ, không có trạng thái cụt? | FN §7 | Chứng từ, Phê duyệt |
| C5-DEV-03 | (Dev) Mọi quy tắc tính toán có công thức, làm tròn, thứ tự áp dụng? | FN §9 | Tất cả |
| C5-DEV-04 | (Dev) Đồng thời, khóa dữ liệu, giao dịch (transaction), idempotency của tích hợp đã được nêu? | FN §14, §16 | Tất cả |
| C5-DEV-05 | (Dev) Không còn câu hỏi nào tôi phải hỏi BA trước khi code? | Liệt kê câu hỏi | Tất cả |
| C5-QA-01 | (QA) Mọi AC đo được với dữ liệu cụ thể; mọi BR validation có MSG; giá trị biên đã định nghĩa? | FN §3, §9, §17, §18 | Tất cả |
| C5-QA-02 | (QA) Viết được test case cho luồng chính, thay thế, ngoại lệ, phân quyền (vai trò không có quyền bị chặn)? | FN §2, §4, §18 | Tất cả |
| C5-ERP-01 | (Chuyên gia ERP) Luồng chứng từ, trạng thái, ghi sổ/đảo, khóa kỳ, đánh số theo chuẩn ERP (erp-ba-core/references/design-patterns.md, erp-ba-core/references/processes)? | So chuẩn | Tất cả |
| C5-ERP-02 | (Chuyên gia ERP) Danh mục được quản trị đúng chuẩn (mã duy nhất, ngừng dùng thay vì xóa khi đã phát sinh, nhập Excel có kiểm tra)? | Catalog & FN Danh mục | Tất cả |
| C5-ERP-03 | (Chuyên gia ERP) Không thiếu chức năng ERP tiêu chuẩn mà quy trình đã chọn bắt buộc phải có (ví dụ có nhập kho thì phải có kiểm kê, có công nợ thì phải có đối chiếu & tuổi nợ)? | So process library §4–§5, §11 | Tất cả |
| C5-ERP-04 | (Chuyên gia ERP) Hạch toán và báo cáo đúng chế độ kế toán, quy định hiện hành (erp-ba-core/references/regulations)? | FN §13, báo cáo luật | Khi có module tài chính |
| C5-AUD-01 | (Kiểm toán/Bảo mật) Có lưu vết đầy đủ (ai, khi nào, giá trị cũ/mới) cho dữ liệu tài chính và danh mục quan trọng? | BR-GEN, FN §16 | Tất cả |
| C5-AUD-02 | (Kiểm toán/Bảo mật) SoD, hạn mức duyệt, quyền tối thiểu được áp dụng; không có vai trò vừa tạo vừa duyệt vừa chi? | roles-permissions, FN §2 | Tất cả |
| C5-AUD-03 | (Kiểm toán/Bảo mật) Dữ liệu cá nhân/nhạy cảm được xác định và có kiểm soát truy cập theo quy định hiện hành? | NFR, FN §2.3 | Khi có dữ liệu cá nhân |
| C5-CON-01 | (Nhất quán) Không có hai nơi mô tả khác nhau cho cùng một khái niệm/trường/quy tắc/trạng thái/tham số? | Đối chiếu chéo | Tất cả |
| C5-CON-02 | (Nhất quán) Báo cáo tự kiểm (bước 4) khai đúng sự thật — mẫu ngẫu nhiên các câu "Yes" có bằng chứng thật? | Kiểm 5 câu Yes ngẫu nhiên | Tất cả |
