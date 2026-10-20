# Prompt one-shot: bộ BPMN chuẩn ERP trước khảo sát

Mở AI (Claude Code) tại **thư mục gốc của repo**. Điền 5 dòng đầu, giữ nguyên phần còn lại, dán cả khối vào.

```text
Ngành / doanh nghiệp: [vd: công ty điều hành tour du lịch]
Bán gì, cho ai, qua kênh nào: [vd: tour ghép theo lịch và tour thiết kế riêng; khách lẻ, doanh nghiệp, đại lý, OTA]
Điểm đặc thù cần thể hiện: [vd: tour riêng có hai cách dựng chương trình — thủ công và bằng trợ lý AI | không có]
Tài liệu tham khảo: [đường dẫn file/thư mục khách hàng gửi, đặt trong projects/<tên>/inputs/ | không có]
Tên dự án: [vd: tour-abc → kết quả nằm ở projects/tour-abc]
---
Vẽ bộ sơ đồ BPMN 2.0 TO-BE chuẩn ERP cho doanh nghiệp trên. Đây là bản vẽ TRƯỚC khảo sát: chưa có gì được xác nhận,
mọi bước, vai trò, tham số là đề xuất theo chuẩn ERP; điều gì cần khách quyết thì ghi vào questions. Làm trọn một lượt, không hỏi lại.
Mọi đường dẫn dưới đây tính từ gốc repo.

Công cụ cố định là bpmn-kit/. Không viết script, không dùng công cụ vẽ nào khác.
1. Đọc bpmn-kit/README.md và bpmn-kit/templates/vi_du_bp05.py. Bộ hoàn chỉnh để tham khảo cách làm: examples/tour-operator/.
2. Song song:
   - Chuẩn ERP từ sách (bắt buộc), 1 subagent đọc theo 3 tầng của books/TOPICS.md, không đọc thừa:
     (1) python3 books/read.py index — mục lục tóm tắt mọi chương;
     (2) chọn chủ đề cho từng nhóm quy trình của chuỗi trên (luôn gồm nhóm "Every process") → 12–15 chương, ghi danh sách và lý do;
     (3) python3 books/read.py <P|W|O|E> chNN cho từng chương đã chọn; chỉ thêm --add "<mục>" hoặc --full khi thật cần.
     Ghi projects/<tên>/book-notes.md: chủ đề | ý chính | áp vào quy trình/kiểm soát nào | file chương.
   - 1 subagent tóm tắt tài liệu tham khảo ở trên nếu có (cách làm thực tế, trạng thái chứng từ, ngưỡng). Không đọc nguồn khác.
3. Chạy bpmn-kit/scripts/build.sh --init projects/<tên>. Sửa projects/<tên>/defs/_common.py: vai trò, bên ngoài, và chốt danh mục
   BP-00 tổng quan + 12–18 quy trình theo chuỗi: dữ liệu gốc → hợp đồng NCC → sản phẩm, giá → S&OP → bán hàng → vận hành →
   quyết toán → công nợ thu, trả → đổi/hủy → CSKH → khóa sổ (+ quy trình đặc thù ngành). Không đánh số lại sau đó.
4. Mỗi quy trình một file projects/<tên>/defs/bpNN_*.py, đủ các khóa như file mẫu. Lấy chuẩn từ book-notes.md: mỗi kiểm soát
   ghi nguồn là chương sách (vd "Elbardan ch08"), mỗi quy trình có ≥ 2 references book('P'|'W'|'O'|'E', 'chNN-<tên file đúng>.md', …).
5. Chạy bpmn-kit/scripts/build.sh projects/<tên>; sửa defs đến khi in "OK". Chỉ xem PNG của sơ đồ sửa nhiều.
   Kiểm trích sách: grep -n ', ch[0-9][0-9]\*\* —' projects/<tên>/docs/*.md phải không ra dòng nào
   (trích sách mà không có link [nguồn] là sai tên file chương).

Quy tắc vẽ:
- Điểm đặc thù là nhánh song song TRONG cùng sơ đồ, gộp lại trước các kiểm soát chung; không tách sơ đồ riêng.
- BP-00 nối các dòng khác nhịp (hoạch định tháng / từng đơn hàng / khóa sổ) qua kho dữ liệu dùng chung.
- Ánh xạ khái niệm sách (BOM, ATP, MPS, nhận hàng, giá thành theo đơn, supplier scheduling) sang ngành; ghi bảng ánh xạ vào README.
- Kiểm soát (người lập ≠ người duyệt, chặn theo quy tắc, lưu vết, khóa kỳ) ghi trên sơ đồ; hạn và ngoại lệ là sự kiện hẹn giờ / đường lui.
- Một mã phân tích chính (đơn hàng / dự án / tour…) xuyên suốt tới sổ cái. Bút toán, thuế ghi "cần kế toán xác nhận".

Cuối cùng viết projects/<tên>/README.md theo mẫu examples/tour-operator/README.md (danh mục, ký hiệu, nguyên tắc kèm trích sách,
bảng ánh xạ, cách xem) và báo cáo ngắn bằng ngôn ngữ nghiệp vụ: danh mục quy trình, kết quả build, 5 câu hỏi quan trọng nhất
cho buổi khảo sát (bộ đầy đủ ở projects/<tên>/CAU-HOI-KHAO-SAT.md).
```
