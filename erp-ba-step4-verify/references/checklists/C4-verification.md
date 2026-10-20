# Checklist C4 — Tự kiểm chéo toàn bộ tài liệu (bước 4)

Chạy SAU khi từng file đã qua C1/C2/C3/C3F/C3R. Mục tiêu: lệch, thiếu, thừa, mâu thuẫn, mơ hồ ở mức toàn bộ tài liệu.

| ID | Câu hỏi (Yes/No) | Cách kiểm | Áp dụng cho |
|---|---|---|---|
| C4-01 | Trong vòng kiểm này đã đọc lại TOÀN BỘ nguồn gốc (biên bản, file khách hàng), không chỉ dựa vào requirement-register? | Liệt kê nguồn đã đọc ở §1 báo cáo | Tất cả |
| C4-02 | Truy vết đầy đủ: 0 REQ chưa phủ, 0 FN không nguồn, 0 FR không có AC, 0 US không có AC? | `ba.py trace` | Tất cả |
| C4-03 | Không lệch nghĩa: với mẫu ≥ 10 REQ (hoặc toàn bộ nếu < 30), nội dung đặc tả đúng ý trích dẫn gốc? | Bảng 3.3 "Lệch" của báo cáo | Tất cả |
| C4-04 | Không thừa: mọi FR/BR/màn hình/trường không có nguồn khách hàng đều mang [ĐỀ XUẤT → Q-…] hoặc đã có DEC? | Soát cột Nguồn, trace | Tất cả |
| C4-05 | Không mâu thuẫn: cùng trường/quy tắc/trạng thái/tham số/vai trò/thuật ngữ được mô tả giống nhau ở mọi file và khớp catalog? | Đối chiếu catalog; tìm cùng khái niệm khác giá trị | Tất cả |
| C4-06 | Không mơ hồ: FR/BR/NFR/AC không chứa từ cấm (nhanh, dễ dùng, linh hoạt, v.v., tương tự, phù hợp, hợp lý…) mà không có số đo/định nghĩa? | Cảnh báo từ mơ hồ của `ba.py lint` | Tất cả |
| C4-07 | Mọi con số (ngưỡng, hạn mức, tỷ lệ, thời gian) có nguồn (REQ/DEC/luật) hoặc là PRM có mặc định đã/đang được xác nhận? | Soát số trong FR/BR/NFR | Tất cả |
| C4-08 | Luồng chứng từ đầu-cuối khép kín: mỗi chứng từ có nơi tạo và nơi kết thúc; không có trạng thái cụt; hủy/đảo được xử lý ở mọi bước sau? | Ghép mục 0 & 7 của các FN theo BP | Tất cả |
| C4-09 | Hạch toán toàn quy trình cân và khớp chế độ kế toán dự án; tài khoản dùng thống nhất giữa các FN? | Tổng hợp mục 13 các FN | Khi có module tài chính |
| C4-10 | 5 thành phần ERP đủ cho mọi module (đối chiếu lại srs-overview §3.1 sau khi sửa)? | srs-overview §3.1 | Tất cả |
| C4-11 | Đã trả lời bằng nội dung cụ thể 4 câu hỏi bắt buộc của BA (mục 3 báo cáo)? | Báo cáo §3 | Tất cả |
| C4-12 | Mọi checklist của phạm vi kiểm (C1/C2/C3/C3F/C3R) đã chạy trong vòng này và không còn "No"? | Báo cáo §4 | Tất cả |
| C4-13 | Câu hỏi mở còn lại đã gom thành danh sách gửi khách hàng (người hỏi, hạn, phương án gợi ý)? | issue-log §1 | Tất cả |
| C4-14 | Sau khi sửa, đã chạy lại lint & trace: 0 Error? | Chạy công cụ | Tất cả |
