# Chương 8: Hoạch định bán hàng & vận hành (Sales & Operations Planning)

## Ý tưởng cốt lõi (Core Idea)
**Sales & Operations Planning (S&OP)** — hoạch định bán hàng & vận hành, "tay nắm của ban lãnh đạo lên business" (top management's handle on the business), có thể là phần quan trọng nhất của ERP. Nó cân bằng demand và supply ở cấp **volume** (tổng lượng/tốc độ), theo chu kỳ tháng, cross-functional, và nối kế hoạch chiến lược/business plan với các quy trình thực thi chi tiết. Rất nhiều ERP thất bại vì bỏ qua S&OP (do phần mềm thường không có).

## Framework được giới thiệu (Frameworks Introduced)
- **Sales & Operations Planning (S&OP)** — quy trình quyết định hằng tháng: cân bằng demand/supply ở mức volume; hoạt động bằng cả đơn vị (units) và tiền (dollars); liên phòng (GM, sales, operations, finance, product development); nối strategic/business plan với master scheduling và các lịch downstream.
- **Volume vs Mix** — khối lượng vs cơ cấu: Volume = tốc độ/tổng lượng bán, sản xuất, tồn kho tổng, backlog (địa hạt của S&OP); Mix = từng sản phẩm/đơn cụ thể (địa hạt của master scheduling). Làm tốt volume thì mix dễ đi hơn.
- **The Monthly S&OP Process (5 bước)** — chu trình tháng (Figure 8-3): Step 1 Run Sales Forecast Reports → Step 2 Demand Planning Phase (management forecast, first-pass spreadsheets) → Step 3 Supply Planning Phase (capacity constraints, second-pass spreadsheets) → Step 4 Pre-S&OP Meeting (khuyến nghị + agenda) → Step 5 Executive S&OP Meeting (quyết định, "authorized game plan").
- **Single-Number Forecast** — dự báo một con số: chỉ một forecast duy nhất được công nhận chính thức (do lãnh đạo sales & marketing phê duyệt), không phải mỗi phòng một con số.
- **Product Families / Resources** — họ sản phẩm (cho sales/marketing dễ dự báo, ~6–12 họ cho họp top management) vs resources (góc nhìn operations); **rough-cut capacity planning** "dịch" từ families sang resources.

## Khái niệm chính (Key Concepts)
- **Executive S&OP Meeting** — họp điều hành ~2 giờ/tháng, thay thế nhiều cuộc họp khác; quyết định cho từng product family: đổi Sales Plan / đổi Operations Plan / đổi inventory-backlog plan / không đổi.
- **Stewardship & Leadership** — hai lý do GM phải tham gia: top management "sở hữu" Business Plan (stewardship) và sự tham gia của họ phát tín hiệu S&OP là quy trình quản lý chính (leadership).
- **One set of numbers** — "best in class" nghĩa là toàn doanh nghiệp quản lý bằng một và chỉ một bộ số; Business Plan phải được cập nhật theo Sales & Operations Plan, nếu không sẽ "disconnect".
- **Window into the future** — S&OP cho tầm nhìn sớm, giúp thấy và xử lý vấn đề trước vài tháng.
- **S&OP Policy** — tài liệu chính sách do GM ký: mục tiêu, các bước, người tham gia mỗi bước, hành động mỗi bước, tần suất họp, quy tắc đổi kế hoạch, product families.

## Mô hình tư duy (Mental Models)
- Nếu quy trình "S&OP" của bạn không có GM và phần lớn staff của họ, thì bạn **không** thực sự làm S&OP.
- Dù logic S&OP đơn giản, triển khai lại khó — vì nó buộc người ta (kể cả GM) đổi cách làm; kinh nghiệm chỉ tăng mỗi tháng một lần nên cần ~8 tháng.
- S&OP chạy stand-alone, phụ thuộc phần mềm thấp, hồi vốn lớn → "The Nike approach: Just do it" (làm cả khi chỉ cài ES, hoặc trong Quick-Slice).
- Metrics S&OP tạo accountability rõ ràng: so actual với plan cho cả Sales/Marketing (có single-number forecast) lẫn Operations (có một production plan).

## Điều cần tránh (Anti-patterns)
- **Loại S&OP khỏi phạm vi ERP** vì phần mềm vendor không hỗ trợ: "preordained to less than total success".
- **Nhiều forecast song song** (Sales một con số, Marketing một con số, Finance dùng con số thứ ba): phá vỡ S&OP.
- **Không cập nhật Business Plan theo Sales & Operations Plan**: gây "surprises" cuối năm tài chính.
- **Tự nhận "đang làm S&OP" nhưng chỉ làm vài mảnh**: không có forecast thống nhất, Sales/Marketing chưa duyệt production plan, Finance chưa duyệt inventory plan.
- **Chọn family pilot quá khó hoặc quá nhỏ (<2% business)**: khó cất cánh hoặc không đủ sức hút sự quan tâm.

## Bảng tham chiếu (Reference Tables)
8 bước triển khai S&OP:

| # | Bước | Điểm then chốt |
|---|------|----------------|
| 1 | Confirm/modify sales forecasting | Yêu cầu single-number forecast |
| 2 | Establish product families & subfamilies | ~6–12 họ cho họp top mgmt |
| 3 | Develop S&OP spreadsheet | Tự làm (DIY), phần mềm hiếm khi có |
| 4 | Develop S&OP policy | GM ký; nêu mục tiêu, bước, người, hành động |
| 5 | Pilot 1–2 families | Chọn mức trung bình, lên pilot trong 90 ngày |
| 6 | Develop capacity reports | Gộp tải sản xuất theo resources |
| 7 | Bring all families onto S&OP | 3–4 họ/tháng, xong trong ~90 ngày sau pilot |
| 8 | Add supply/financial planning, new product | Chỉ chạy tốt khi mọi family đã lên S&OP |

## Ví dụ minh họa (Worked Example)
Chu trình S&OP một tháng (Figure 8-3), từ cuối tháng: Step 1 — chạy báo cáo forecast (statistical forecasts + field sales worksheets); Step 2 Demand Planning — middle management cập nhật forecast, gom theo product family, ra first-pass spreadsheets; Step 3 Supply Planning — xác định ràng buộc năng lực (capacity constraints), ra second-pass spreadsheets; Step 4 Pre-S&OP Meeting — thống nhất khuyến nghị và agenda cho top management, chỉ rõ chỗ chưa đồng thuận; Step 5 Executive S&OP Meeting — GM và staff quyết định từng family, ra "authorized game plan" rồi phổ biến toàn tổ chức. Phần lớn "heavy lifting" nằm ở các bước sớm nên họp điều hành chỉ ≤2 giờ, GM chuẩn bị gần như bằng 0.

## Điểm cần nhớ (Key Takeaways)
1. S&OP là bắt buộc trong phạm vi ERP; đừng để việc phần mềm không hỗ trợ khiến nó bị bỏ qua.
2. Phân biệt rõ volume (S&OP) và mix (master scheduling); quản volume tốt thì mix nhẹ đi.
3. Thiết lập single-number forecast và "one set of numbers" cho toàn doanh nghiệp; Business Plan phải đồng bộ với Sales & Operations Plan.
4. Chu trình tháng 5 bước kết thúc bằng Executive S&OP Meeting ≤2 giờ có GM tham gia.
5. Triển khai theo 8 bước, bắt đầu bằng pilot 1–2 family trong 90 ngày (early win); đủ 8 tháng cho S&OP cơ bản.
6. Viết S&OP policy do GM ký làm "bedrock policy" quản trị quy trình.

## Ứng dụng cho BA ERP (BA Application)
- Khi viết spec module planning, phải mô hình hóa hai tầng tách bạch: tầng volume (S&OP: Sales Plan, Operations Plan, inventory/backlog theo product family) và tầng mix (master schedule theo từng sản phẩm) — nhiều tài liệu bị conflict do trộn lẫn hai tầng này.
- Đặc tả single-number forecast như một business rule: hệ thống chỉ cho phép một forecast "official" được duyệt; chặn tình trạng mỗi phòng một bản.
- Mỗi quy trình S&OP cần một tài liệu "policy" đi kèm nêu rõ: mục tiêu, trình tự bước, participants/role mỗi bước, hành động và tiêu chí ra quyết định — khớp với yêu cầu "mỗi function có đủ role và tham số" của tài liệu chuẩn.
- Thiết kế metric chuẩn: "actual vs plan" cho cả demand (so với single-number forecast) và supply (so với production plan) — đưa vào mục báo cáo (reports) của tài liệu.
- Mô tả vòng lặp hằng tháng như một workflow 5 bước có đầu vào/đầu ra rõ (spreadsheets các pass, agenda, authorized game plan) để tài liệu đủ chi tiết để code.

## Liên hệ (Connects To)
- **Ch 2**: S&OP là "top management's handle"; three knobs.
- **Ch 7**: top management cần đào tạo sâu về S&OP vì đó là "phần tàu" của họ (early win).
- **Ch 9**: Process Definition — S&OP là một trong các quy trình được định nghĩa chi tiết; master scheduling là downstream.
- **Ch 12 / DRP, supplier scheduling**: các lịch downstream do master schedule dẫn dắt.
- **Master Scheduling / MRP**: S&OP (volume) cấp nguồn cho master schedule (mix) rồi tới MRP, plant/supplier scheduling.
