# Prompt one-shot: RSD cho người đọc nghiệp vụ của một quy trình BPMN → Word, Google Docs, Confluence

Mở Claude Code tại **thư mục gốc repo**, đổi mã quy trình ở dòng đầu, dán cả khối vào.

Hai dòng sau có sẵn mặc định: dự án mẫu, và space lấy từ `~/.config/rsd-kit/config.json` nếu để trống.
Cách kết nối Google và Confluence trên từng máy: `rsd-kit/README.md`, mục "Connections". Không có kết nối nào thì vẫn ra file Word.

```text
Quy trình: BP-13
Dự án: examples/tour-operator
Confluence space: [key hoặc id | để trống]
---
Viết tài liệu đặc tả yêu cầu (RSD) của quy trình trên cho người đọc nghiệp vụ (BA, key user, khách hàng), bằng tiếng Việt.
Xuất Word, rồi đăng Google Docs (ai có link đều xem) và Confluence. Làm trọn một lượt, không hỏi lại.
Công cụ cố định là rsd-kit/ (đường dẫn tính từ gốc repo). Không viết script mới. Kết quả ở <Dự án>/rsd/<Quy trình>/.

1. Đọc rsd-kit/README.md, rsd-kit/references/writing-guide.md, rsd-kit/templates/rsd-template.md và mẫu đã duyệt
   examples/tour-operator/rsd/BP-13/ (RSD-BP-13.md, book-notes.md và diagrams/).
2. Song song:
   - Đọc <Dự án>/docs/<Quy trình>-*.md, file defs/ tương ứng và tài liệu các quy trình nó gọi tới / được gọi từ.
   - Chuẩn ERP từ sách (bắt buộc), 1 subagent đọc theo 3 tầng của books/TOPICS.md, không đọc thừa:
     (1) python3 books/read.py index — mục lục tóm tắt mọi chương;
     (2) chọn loại quy trình → chủ đề → 8–12 chương, tối đa 15 (luôn gồm nhóm "Every process"), ghi danh sách và lý do vào đầu book-notes.md;
     (3) python3 books/read.py <P|W|O|E> chNN cho từng chương đã chọn; chỉ thêm --add "<mục>" hoặc --full khi một quy tắc cụ thể cần.
     Ghi <thư mục>/book-notes.md theo rsd-kit/templates/book-notes.md (≥ 8 dòng từ ≥ 3 cuốn, mỗi dòng kèm file chương).
3. Viết RSD-<Quy trình>.md theo template, đủ mục 1–11, cùng mức chi tiết với mẫu BP-13.
   Áp book-notes.md vào tài liệu: mỗi điểm kiểm soát ở mục 7 ghi chương sách ở cột "Căn cứ", quy tắc trỏ về KS-xx hoặc chương,
   mục 11 liệt kê đúng các chương đã dùng. Điều BPMN chưa có thì bổ sung kèm [Đề xuất: CH-xx];
   con số không có nguồn ghi [Cần xác nhận: CH-xx].
4. Chép <Dự án>/png/<Quy trình>-*.png thành images/h01-bpmn.png; viết diagrams/h02…hNN-<tên tiếng Anh>.mmd theo mẫu
   (nhãn tiếng Việt). Chạy rsd-kit/scripts/render-diagrams.sh, mở PNG, sơ đồ nào rối thì sửa.
5. python3 rsd-kit/scripts/check.py <thư mục> — sửa đến khi in "OK".
6. rsd-kit/scripts/export-docx.sh <thư mục>
7. python3 rsd-kit/scripts/connect.py — xem máy này đăng được bằng cách nào.
8. python3 rsd-kit/scripts/publish-gdocs.py <thư mục>
9. python3 rsd-kit/scripts/publish-confluence.py <thư mục> [--space <Confluence space>]
   Đích nào báo "manual": nếu phiên này có tool MCP Atlassian/Google thì đăng theo rsd-kit/references/publish-with-agent-tools.md;
   nếu không, chép nguyên hướng dẫn script in ra vào báo cáo.

Cuối cùng báo cáo ngắn bằng ngôn ngữ nghiệp vụ:
- link Google Docs và Confluence (hoặc hướng dẫn đăng tay);
- kết quả kiểm tra;
- những gì đã bổ sung so với BPMN;
- 5 câu hỏi quan trọng nhất cần doanh nghiệp trả lời.
```
