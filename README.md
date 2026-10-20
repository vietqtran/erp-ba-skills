# ERP BA — bộ quy trình BPMN chuẩn ERP

Dùng để vẽ nhanh bộ quy trình nghiệp vụ chuẩn ERP (sơ đồ BPMN 2.0 kèm tài liệu) cho một doanh nghiệp **trước buổi khảo sát**,
dựa trên 4 cuốn sách ERP. Kết quả gồm sơ đồ, tài liệu từng quy trình và bộ câu hỏi mang đi gặp khách.

## Bắt đầu

1. Cài một lần: Python 3, Node.js ≥ 18, Chrome (hoặc Edge), Claude Code.
2. Mở Claude Code tại thư mục gốc repo này.
3. Mở [`bpmn-kit/PROMPT.md`](bpmn-kit/PROMPT.md), điền 5 dòng đầu, dán cả khối vào Claude Code.
4. Kết quả nằm ở `projects/<tên dự án>/`:
   - `README.md`: danh mục quy trình, ký hiệu, nguyên tắc, các điểm cần chốt.
   - `docs/`: tài liệu từng quy trình, có ảnh sơ đồ ở đầu.
   - `CAU-HOI-KHAO-SAT.md`: câu hỏi và các con số đề xuất cần khách xác nhận.
   - `bpmn/`: file BPMN mở bằng Camunda Modeler, bpmn.io hoặc draw.io; `png/`, `svg/`: ảnh để chèn vào tài liệu.
   - `viewer.html`: xem tương tác (chạy `python3 -m http.server` ở gốc repo, mở `http://localhost:8000/projects/<tên>/viewer.html`).

Xem trước một bộ hoàn chỉnh: [`examples/tour-operator`](examples/tour-operator/README.md) — công ty điều hành tour, 17 quy trình.

## Cấu trúc

| Thư mục | Nội dung |
|---|---|
| `books/` | Tóm lược 4 cuốn sách ERP (Parthasarathy, Wallace & Kremzar, O'Leary, Elbardan & Kholeif) — nguồn chuẩn ERP |
| `bpmn-kit/` | Prompt, công cụ sinh sơ đồ dùng chung (không cần sửa), mẫu định nghĩa quy trình |
| `examples/` | Bộ đã làm để tham khảo |
| `projects/` | Nơi chứa các dự án mới |

## Sửa sau khi đã sinh

Không sửa tay file trong `bpmn/` hay `docs/` — lần sinh sau sẽ ghi đè. Nói với Claude Code điều cần đổi
(vd "BP-06 thêm bước duyệt của Giám đốc"); nó sửa `projects/<tên>/defs/` và chạy lại `bpmn-kit/scripts/build.sh projects/<tên>`.
