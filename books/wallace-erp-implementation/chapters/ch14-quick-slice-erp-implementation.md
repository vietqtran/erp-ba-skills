# Chương 14: Quick-Slice ERP — Triển khai (Quick-Slice ERP — Implementation)

## Ý tưởng cốt lõi (Core Idea)
Các bước triển khai Quick-Slice gần giống triển khai toàn công ty trên **Proven Path** — lộ trình đã kiểm chứng, nhưng được nén lại theo *tuần* thay vì *tháng*, với ba thay đổi: (1) bỏ bước finance & accounting, (2) thêm bước **physical process improvement** (tạo flow manufacturing bằng cells), (3) pilot *chính là* cutover. Toàn bộ do urgency dẫn dắt.

## Framework được giới thiệu (Frameworks Introduced)
- **Proven Path — Quick Slice** (Figure 14-1): Audit/Assessment I → First-cut education → (Vision statement + Cost/benefit + Go/No-go + Performance goals + Project organization, gộp trong vài ngày) → Initial education → Sales & Operations Planning → Demand management/planning/scheduling + Data integrity + Physical process improvement → Software selection & installation → Pilot/Cutover → Audit/Assessment II → lặp slice tiếp hoặc chuyển company-wide.
- **Criteria for Selecting the Quick-Slice Product(s)** (Figure 14-2) — 5 tiêu chí chọn slice:
  1. **High Impact, High Visibility** — sản phẩm Pareto Class A, không phải B/C.
  2. **Largely Self-Contained** — càng ít dùng chung component/work center với sản phẩm khác càng tốt.
  3. **Good People** — kháng cự thay đổi không lớn hơn bình thường.
  4. **Stability** — không có thay đổi lớn/khiếm khuyết cấu trúc đang treo.
  5. **Applicability** — bài học áp dụng được cho phần còn lại của công ty.
- **Physical process improvement (cells)**: tạo flow từ job shop bằng cách chuyên dụng hóa thiết bị cho item cụ thể và sắp xếp liền kề theo dòng — gọi là **physical cell**; nếu không di dời được thiết bị, dùng **conceptual cell** (liên kết thiết bị bằng kanban, không di dời — xem Appendix B).
- **Pilot is the cutover**: ở Quick-Slice, pilot và cutover là một; pilot chính là lần triển khai thực.

## Khái niệm chính (Key Concepts)
- **Project charter một trang**: nêu urgency là yêu cầu chính của quá trình triển khai; ký duyệt bởi toàn bộ lãnh đạo tham gia justification.
- **Torchbearer** (Quick-Slice): khác company-wide, người giữ ngọn đuốc này phải tham gia trực tiếp, thường nhiều lần mỗi ngày.
- **Full-time project leader**: *bắt buộc* ngay cả khi đơn vị <100 người — vì nếu không, gần như chắc chắn không xong trong 4-5-6 tháng. Vấn đề là urgency.
- **"Use what you have"** (finance & accounting): giữ hệ kế toán hiện tại, chỉ *bridge* giao dịch ERP mới vào hệ cũ (lập trình tạm, hoặc nhập liệu trùng nếu buộc phải) — "least worst choice".
- **Internal supplier**: coi phần job shop còn lại như một nhà cung cấp (mua từ job shop) cho các item fabricated không đủ volume làm cell.

## Mô hình tư duy (Mental Models)
- Triển khai S&OP cho **tất cả** product family, không chỉ slice: vì dễ, có lợi ích ngay, là "early-early win", giữ cân bằng nguồn lực, và tạo động lực (lãnh đạo thấy quyết định S&OP trên slice được "rack-and-pinion" thành lịch chi tiết, còn trên non-slice thì bị "disconnect").
- "Build a fence around the slice": dù top management tham gia hay không, phải đạt ổn định lịch (schedule stability) trên item của slice — chặn nhu cầu biến động dữ dội.
- Làm slice hiển thị cao: sơn/treo cờ đánh dấu cell, dùng cùng một màu (xanh = go?) cho thiết bị slice, stockroom và giấy tờ xưởng của slice.

## Điều cần tránh (Anti-patterns)
- **Đi tiếp slice tiếp theo khi slice 1 chưa ra kết quả**: "do not, repeat, do not" vượt qua slice đầu nếu kết quả chưa đến — dừng lại sửa trước.
- **Không học đủ từ slice đầu**: (Mike) các đơn vị khác ít chú ý đơn vị làm Quick-Slice → mất learning; cần cơ chế rõ để người khác tham gia và mang bài học về.
- **Dời thiết bị gây trễ slice**: dùng conceptual cell (kanban) để khởi động trước, di dời máy sau.
- **Cố interfacing/enhancement phần mềm phức tạp**: giữ tối thiểu (hoặc zero); đừng để nằm trên critical path.

## Bảng tham chiếu (Reference Tables)
Figure 14-3 — Các chức năng ERP được triển khai trong pilot/cutover Quick-Slice:

| Chức năng | Phạm vi trong Quick-Slice |
|---|---|
| Sales & Operations Planning | Trên **tất cả** product family |
| Demand Management | Trên sản phẩm slice |
| Master Scheduling | Trên sản phẩm slice |
| Rough-cut Capacity Planning | Trên các key resource |
| Material Requirements Planning | Trên component & material của slice |
| Plant Scheduling / Kanban | Trên sản phẩm & component của slice |
| Supplier Scheduling | Trên component & material của slice, *nơi khả thi* |

## Ví dụ minh họa (Worked Example)
**Chicken wire stockroom** — giải bài toán chính xác tồn kho on-hand (thách thức dữ liệu khó nhất của Quick-Slice): một công ty quây lưới gà một khu nhỏ trong stockroom không được bảo vệ để giới hạn truy cập và lấy bản ghi tồn kho chính xác (công ty khác chỉ cần vạch sơn trên sàn). Vấn đề common-parts (item dùng chung giữa slice và non-slice): giải pháp là trữ ở hai vị trí khác nhau và thêm hậu tố (chữ "S" = slice) vào mã item slice để tách biệt cả ngoài thực tế lẫn trong máy tính (kèm một chỉnh sửa nhỏ trên bill of material của slice). Timeline checklist thực tế: tháng 1 (audit I, first-cut education, charter, chọn slice, lập team/steering committee/leader), tháng 2 (business meetings, process definition, quyết phần mềm, khởi động S&OP), tháng 3 (data integrity: inventory 95%+, bills 98%+), tháng 4 (duyệt & chạy MS/MRP, plant schedule/kanban, feedback link), tháng 5 (supplier scheduling nơi khả thi, đo lường, Audit II).

## Điểm cần nhớ (Key Takeaways)
1. Quick-Slice = Proven Path nén lại; bỏ finance/accounting, thêm physical process improvement, pilot = cutover.
2. Chọn slice theo 5 tiêu chí (impact, self-contained, good people, stability, applicability) — chấp nhận thỏa hiệp nhưng bám sát.
3. S&OP làm cho toàn bộ family; mọi chức năng chi tiết khác chỉ cho item của slice.
4. "Use what you have" cho phần mềm và kế toán; giữ interface/enhancement ở mức tối thiểu.
5. Đo kết quả so với goal; không vượt slice đầu nếu chưa có kết quả.
6. Thiếu top management: vẫn có thể làm nếu dạy được họ S&OP hoặc ít nhất buộc họ "không thò tay" vào demand của slice; có torchbearer + consultant Class A.

## Ứng dụng cho BA ERP (BA Application)
- Khi viết tài liệu cho một pha đầu tiên, dùng "Figure 14-3" làm danh mục chức năng tối thiểu phải đặc tả cho một slice: S&OP, Demand Management, Master Scheduling, Rough-Cut Capacity Planning, MRP, Plant Scheduling/Kanban, Supplier Scheduling — và nêu rõ phạm vi (all families vs slice-only) cho từng chức năng.
- Mô hình hóa bài toán common-parts trong data model: cần field/quy ước đánh dấu item thuộc slice (ví dụ hậu tố mã), và quyết định ảnh hưởng tới bill of material — ghi đây là một business rule, không để mơ hồ.
- Đặc tả "internal supplier": khi một phần job shop được coi như nhà cung cấp, cần luồng/đơn nội bộ với due date hợp lệ và đánh dấu trực quan (màu) — BA phải nêu các điều kiện để job shop giao item slice đúng hạn.
- Ghi tiêu chí nghiệm thu đo được cho pilot (on-time shipment, lead time, inventory turns...) và quy tắc "dừng-và-sửa nếu kết quả chưa đến" vào acceptance criteria của tài liệu.

## Liên hệ (Connects To)
- **Ch 13**: tổng quan và lý do chọn Quick-Slice; three knobs.
- **Ch 5**: các bước front-end của Proven Path (audit, vision, cost/benefit, project org) được tái dùng.
- **Ch 12**: supplier scheduling, DRP, VMI đầy đủ chỉ làm được khi chuyển company-wide.
- **Appendix B**: physical vs conceptual cells, kanban, flow manufacturing.
