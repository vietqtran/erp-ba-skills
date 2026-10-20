# Chương 1: Hoạch định Nguồn lực Doanh nghiệp (Enterprise Resource Planning)

## Ý tưởng cốt lõi (Core Idea)
**Enterprise Resource Planning (ERP)** — hoạch định nguồn lực doanh nghiệp — *không phải là phần mềm*. Nó là một tập hợp các **quy trình nghiệp vụ (business processes)** toàn doanh nghiệp để cân bằng cung–cầu và ra quyết định. Phần mềm gọi là **Enterprise System / Enterprise Software (ES)**. Mua phần mềm tốt không làm công ty giỏi hơn; giống như mua bộ gậy golf đắt tiền không biến bạn thành tay golf giỏi.

## Framework được giới thiệu (Frameworks Introduced)
- **Định nghĩa ERP (theo APICS)**: tập công cụ dự báo – hoạch định – lập lịch (forecasting, planning, scheduling) toàn doanh nghiệp, dự báo và cân bằng cung–cầu, liên kết khách hàng và nhà cung cấp thành chuỗi cung ứng hoàn chỉnh, tích hợp chéo chức năng (sales, marketing, operations, logistics, purchasing, finance, product development, HR).
  - Khi dùng: khi cần một "ngôn ngữ" quản trị vận hành chuẩn cho mọi loại hình sản xuất.
  - Cách: phát triển kế hoạch/lịch để đúng nguồn lực (manpower, materials, machinery, money) sẵn sàng đúng lượng, đúng lúc.
- **Bốn bước tiến hóa (Evolution of ERP)**: 1) **MRP (Material Requirements Planning)** → 2) **Closed-Loop MRP** → 3) **MRP II (Manufacturing Resource Planning)** → 4) **ERP**. Mỗi bước là mở rộng trực tiếp của bước trước, không thay thế.
  - **MRP**: mô phỏng "universal manufacturing equation" qua 4 câu hỏi.
  - **Closed-Loop MRP**: thêm hoạch định năng lực (capacity) + vòng phản hồi (feedback) từ execution về planning.
  - **MRP II**: thêm 3 yếu tố — Sales & Operations Planning, giao diện tài chính (financial interface), và mô phỏng (simulation/what-if).
  - **ERP**: phạm vi rộng hơn, đa đơn vị kinh doanh, tích hợp tài chính mạnh hơn, công cụ chuỗi cung ứng xuyên biên giới doanh nghiệp.
- **Universal Manufacturing Equation** — 4 câu hỏi nền tảng của MRP: (1) Chúng ta sẽ làm gì? (master schedule) (2) Cần gì để làm? (bill of material) (3) Chúng ta đang có gì? (inventory records) (4) Chúng ta phải mua/làm thêm gì?
- **ABCs of Implementation** (từ phân tích ABC/định luật Pareto): **A = People** (con người, quan trọng nhất), **B = Data** (dữ liệu: tồn kho, BOM, routing), **C = Computer** (phần cứng+phần mềm, thiết yếu nhưng ít quan trọng nhất). Đừng để "đuôi máy tính vẫy con chó công ty".
- **Class ABCD Classification** (Oliver Wight): thang đo mức độ dùng ERP hiệu quả tới đâu, cho ra điểm chữ A/B/C/D qua **Oliver Wight ABCD Checklist for Operational Excellence** (bộ câu hỏi tự đánh giá).

## Khái niệm chính (Key Concepts)
- **ERP vs ES**: ERP là quy trình/con người; ES là phần mềm giao dịch toàn doanh nghiệp. Có ERP process không nằm trong ES (vd Sales Forecasting, S&OP, APS) và có ES process không thuộc ERP (vd Accounts Receivable/Payable, General Ledger, HR, CRM, Data Warehousing).
- **Priority vs Capacity**: priority = "cái nào trước" (sequence/scheduling); capacity = "đủ không" (volume/loading). MRP giải quyết priority; cần công cụ riêng cho capacity.
- **Priority planning**: giữ cho due date (ngày đến) luôn khớp need date (ngày cần) khi điều kiện thay đổi.
- **Re-implementers**: công ty đã làm ERP ra kết quả Class C/D, nay làm lại cho đúng; các bước gần như giống lần đầu.
- **Dilemma companies**: công ty đang/sắp cài ES và không đủ nguồn lực làm ERP song song.

## Mô hình tư duy (Mental Models)
- **ERP là "logistics analog of GAAP"**: giống như kế toán có một bộ chuẩn (double-entry, GAAP) ai cũng theo, ERP là bộ tri thức chuẩn best-practice cho phần logistics/vận hành. Đừng "phát minh lại" nó.
- **Golf clubs analogy**: công cụ (phần mềm) tự nó không tạo lợi thế; nhưng muốn thi đấu đỉnh cao vẫn cần đủ bộ công cụ hoàn chỉnh.
- **ERP là nền móng (foundation)**: các sáng kiến khác (Lean Manufacturing, Six Sigma, Factory Automation) chỉ phát huy hết tiềm năng khi đi kèm dự báo–hoạch định–lập lịch hiệu quả. Hiệu quả mà làm sai thứ → vô ích.
- **Ba hình thức cải tiến quy trình (Chris Gray)**: (1) tăng độ tin cậy quy trình → Six Sigma/TQM; (2) giảm độ phức tạp → Lean; (3) phối hợp các cấu phần của toàn bộ quy trình → ERP sống ở đây.

## Điều cần tránh (Anti-patterns)
- **Gọi ES là ERP**: nhầm phần mềm giao dịch là ERP; dẫn tới chỉ cài phần mềm mà không đổi quy trình → "bad information moves faster".
- **Hội chứng "we're unique"**: cho rằng ERP không áp dụng được cho mình; thực tế ERP áp dụng gần như phổ quát cho mọi doanh nghiệp sản xuất.
- **Để phần mềm chi phối**: biến dự án quản trị thành dự án IT; đặt C-item lên trên A-item.
- **Dừng ở Class C**: giảm tồn kho một chút nhưng không đổi cách điều hành → bỏ lỡ phần lớn lợi ích.

## Bảng tham chiếu (Reference Tables)
Phân loại Class ABCD (Figure 1-6):

| Class | Mô tả |
|---|---|
| **A** | Dùng hiệu quả toàn công ty; cải thiện đáng kể dịch vụ KH, năng suất, chi phí. Một bộ số thống nhất từ S&OP xuống lịch chi tiết; tài chính rút từ số vận hành; dùng mô phỏng nhiều. |
| **B** | Được lãnh đạo hỗ trợ; quản lý cấp trung dùng để cải thiện đo lường được (giao hàng đúng hạn, giảm thiếu hụt, giảm tồn kho). |
| **C** | Chủ yếu là công cụ đặt hàng vật tư tốt hơn; cải thiện quản lý tồn kho; chưa đổi cách điều hành. |
| **D** | Thông tin sai, người dùng không hiểu; gần như không giúp ích điều hành (thường bị đổ oan là "lỗi máy tính"). |

Ba vùng ERP/ES (Figure 1-1 — bảng bị trích xuất phẳng, tái dựng theo nội dung): ERP-không-thuộc-ES (Sales Forecasting, S&OP, APS, Supplier Rating, Performance Metrics) | ERP-trong-ES (Master Production Scheduling, Rough-Cut Capacity Planning, MRP, CRP, DRP, Customer Order Entry/Promising) | Phi-ERP-trong-ES (AR, AP, General Ledger, Cash Management, CRM, HR, Data Warehousing).

## Ví dụ minh họa (Worked Example)
**Ba loại công ty muốn làm ERP** (quyết định "Proven Path có áp dụng được không"):
1. Đã cài ES rồi, nay muốn cải tiến quy trình bằng ERP → Proven Path hợp (thường theo biến thể Quick-Slice).
2. Chưa cài đủ ES ("clean sheet of paper"), ưu tiên ERP cao hơn ES → Proven Path áp dụng trọn vẹn.
3. Đang/sắp cài ES, ES là ưu tiên → "dilemma company", thường không đủ người làm ERP song song; khuyến nghị: hoàn tất ES trước, chỉ cải tiến nhẹ (S&OP, data integrity), rồi mới chạy ERP đầy đủ.

Trong Q&A, Mike Kremzar kể tại P&G cả bốn tình huống đều có: châu Âu đã cài 80% SAP trước khi làm MRP II; Bắc Mỹ bắt đầu bằng cải tiến quy trình (S&OP) rồi mới cài SAP; Mỹ Latin gần như clean-sheet; châu Á đạt Class A trước khi biết tới SAP. Bài học: trình tự linh hoạt, nhưng con người/quy trình đi trước phần mềm.

## Điểm cần nhớ (Key Takeaways)
1. Luôn tách bạch **ERP (quy trình/con người)** khỏi **ES (phần mềm)**; đây là gốc của nhiều thất bại khi viết tài liệu.
2. ERP là bộ tri thức chuẩn, phổ quát — thiết kế chức năng nên dựa trên nó, không "sáng chế lại".
3. Thứ tự ưu tiên khi triển khai: **People > Data > Computer**.
4. Mục tiêu là Class A: một bộ số thống nhất xuyên suốt từ hoạch định tới thực thi tới tài chính.
5. ERP là nền móng cho supply chain management, e-commerce, và cho các sáng kiến Lean/Six Sigma khác.

## Ứng dụng cho BA ERP (BA Application)
- Khi viết spec, phân biệt rõ **business function** (nghiệp vụ) với **software module**: tài liệu mô tả nghiệp vụ cần làm, không chỉ "bật module X".
- Dùng **4 câu hỏi của universal manufacturing equation** làm khung kiểm tra dữ liệu master cho mọi chức năng hoạch định: có master schedule? có BOM? có inventory records? có logic sinh nhu cầu mua/làm?
- Phân loại dữ liệu theo **ABC**: khi thiết kế, đánh dấu rõ cấu phần con người (role/đào tạo), dữ liệu (BOM/tồn kho/routing cần chính xác), và máy tính — để tài liệu không thiên về mỗi phần mềm.
- Khi đánh giá độ "chuẩn ERP" của một yêu cầu, chiếu vào thang **Class A** (một bộ số, tích hợp chéo chức năng) thay vì chỉ cải tiến cục bộ.
- Map phạm vi: chức năng nào thuộc ERP-core (MPS, MRP, CRP, DRP, order promising), chức năng nào thuộc ES nhưng ngoài ERP (GL, AP/AR, HR) để khoanh vùng tài liệu đúng.

## Liên hệ (Connects To)
- **Chương 2**: catch-22 của triển khai và tổng quan Proven Path.
- **Chương 4**: chi tiết về phần mềm ES, bolt-on và ba loại công ty.
- **APICS Dictionary**: chuẩn thuật ngữ MRP II/ERP mà sách dựa vào.
- **GAAP / double-entry bookkeeping**: mô hình "bộ tri thức chuẩn" mà ERP là tương tự cho logistics.
