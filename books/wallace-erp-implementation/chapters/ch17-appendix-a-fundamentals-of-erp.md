# Chương 17: Phụ lục A — Nền tảng của Enterprise Resource Planning (Appendix A — The Fundamentals of Enterprise Resource Planning)

## Ý tưởng cốt lõi (Core Idea)
ERP là một **hệ phân cấp hoạch định** (planning hierarchy) liên kết kế hoạch tổng hợp dài hạn với kế hoạch chi tiết ngắn hạn, từ general manager xuống tới công nhân, theo quan hệ "rack-and-pinion" (bánh răng – thanh răng): kế hoạch cấp trên dẫn động lịch cấp dưới, và feedback đi ngược từ dưới lên *theo ngoại lệ* (exception basis) để giữ mọi kế hoạch hợp lệ. ERP quản lý mọi nguồn lực (vật tư, lao động, thiết bị, dụng cụ, đặc tả kỹ thuật, không gian, tiền) bằng cách trả lời ba câu cho mỗi nguồn lực: *cần gì, khi nào, bao nhiêu*.

## Framework được giới thiệu (Frameworks Introduced)
**ERP Planning Hierarchy** (Figure A-1) — từ trên xuống, với phía DEMAND (trái) và SUPPLY/CAPACITY (phải):
- **Strategic Planning** — hoạch định chiến lược: xác định mission, goals, objectives tổng thể.
- **Business Planning** — hoạch định kinh doanh: kế hoạch tổng thể bằng *dollars*, dài hạn; do general manager và staff phụ trách; tính tới thị trường, năng lực nội bộ, mục tiêu tài chính, mục tiêu chiến lược.
- **Sales & Operations Planning (S&OP)** — hoạch định bán hàng & vận hành: phần business plan về sales/production/inventory/backlog; stated bằng *đơn vị* (pieces, standard hours) chứ không phải dollars; mức **VOLUME** (tổng hợp theo product family), không phải mix; gồm Sales Plan và Operations Plan.
- **Demand Management** — quản lý nhu cầu: gồm **Forecasting/Sales Planning** (dự báo + cam kết của sales/marketing theo rate hằng tháng cho family) và **Customer Order Entry & Promising** (nhận đơn, xác định tồn kho/cấu hình, net với forecast, hứa ngày giao = customer commitment).
- **Rough-Cut Capacity Planning (RCCP)** — hoạch định năng lực sơ bộ: xác định nguồn lực (supply của capacity) cần để đạt production plan (demand của capacity); dùng thông tin tổng hợp để phát hiện vấn đề *trước khi* duyệt lịch.
- **Master Scheduling** — lập lịch chủ đạo: mức **MIX** (sản phẩm cụ thể, đơn khách cụ thể); nêu "bao nhiêu" và "khi nào"; chia theo tuần hoặc nhỏ hơn; *tổng của master schedule phải khớp với S&OP* cùng kỳ; horizon phải phủ tổng lead time để có đủ nguồn lực.
- **Material Requirements Planning (MRP)** — hoạch định nhu cầu vật tư: từ master schedule (+ service/spare parts) xác định component cần; cần **bill of material** + dữ liệu tồn kho; tính đơn nào cần dời sớm/muộn và vật tư mới nào phải đặt.
- **Capacity Requirements Planning (CRP)** — hoạch định nhu cầu năng lực: lấy nhu cầu item sản xuất từ MRP, chuyển thành dự đoán *bao nhiêu capacity, khi nào*; cần routing + thời gian mỗi nguyên công; tổng hợp theo key work center theo kỳ, so cần vs sẵn có.
- **Plant Scheduling** — lập lịch xưởng: từ master schedule + MRP tạo thời điểm bắt đầu/hoàn thành job; đơn giản (list từ master schedule) hoặc phức tạp (finite scheduling). Kèm **input-output control**: so sánh output lẽ ra hoàn thành vs thực tế hoàn thành.
- **Supplier Scheduling** — lập lịch nhà cung cấp: thay chu trình requisition/PO; output MRP cho hàng mua được tổng hợp và gửi thẳng tới nhà cung cấp (Internet, intranet, EDI, fax, mail); hợp đồng dài hạn định giá/điều khoản/tổng lượng; horizon vượt xa lead time.
- **Execution and Feedback** — thực thi & phản hồi: đỉnh của mọi bước hoạch định; feedback *chỉ khi* một phần kế hoạch không thực thi được (nêu nguyên nhân + ngày hoàn thành mới tốt nhất). Chỉ thay master schedule khi mọi lựa chọn khác đã cạn.
- **Financial Integration** — tích hợp tài chính: thêm giá bán & chi phí, ERP chuyển mọi kế hoạch đơn vị thành dollars → one set of numbers (cùng dữ liệu, chỉ khác đơn vị đo).
- **Simulation** — mô phỏng: khả năng thứ ba của ERP; trả lời "what-if" (nếu cầu tăng nhanh hơn? mix đổi? chi phí tăng mà giá không?).

## Khái niệm chính (Key Concepts)
- **Volume vs Mix**: S&OP làm việc ở mức volume (tổng hợp family); master scheduling làm việc ở mức mix (sản phẩm/đơn cụ thể). Đây là ranh giới phân cấp cốt lõi.
- **Rack-and-pinion**: quan hệ khớp chặt giữa kế hoạch cấp trên và công việc thực tế dưới xưởng; quyết định cấp trên được "dịch" xuống lịch chi tiết một cách logic, đúng đắn.
- **Exception-basis feedback**: không báo cáo mọi thứ; chỉ phản hồi khi không thực thi được kế hoạch — và chuỗi phản hồi leo thang: planner → master scheduler → sales → khách hàng.
- **One set of numbers**: vận hành và tài chính dùng chung một bộ dữ liệu; tránh việc tài chính phải lập "sổ riêng" vì không tin dữ liệu vận hành.
- **Available-to-Promise (ATP)**: phần tồn kho/sản xuất tương lai chưa cam kết, tính từ master schedule, dùng để hứa đơn (ngầm trong Customer Order Entry & Promising).

## Mô hình tư duy (Mental Models)
- Coi ERP như **cuốn sách nấu ăn**: logic rất đơn giản, cái khó là *volume và change* của sản xuất thực (nhiều sản phẩm, lead time dài, work center bận, khách đổi ý → resequencing).
- Phân cấp = "từ trên xuống dẫn động, từ dưới lên phản hồi": top-down là priority/schedule, bottom-up là exception feedback — thiếu một chiều thì không phải closed loop.
- Mỗi cấp có *đơn vị* và *chân trời thời gian* khác nhau: business plan (dollars, dài hạn) → S&OP (units, family, volume) → master schedule (units, sản phẩm, tuần) → MRP (component, order) → plant/supplier scheduling (operation/giao hàng).

## Bảng tham chiếu (Reference Tables)
Phân cấp hoạch định và đặc trưng từng cấp:

| Cấp | Trả lời câu hỏi | Mức | Đơn vị | Ai phụ trách |
|---|---|---|---|---|
| Business Planning | Hướng đi tổng thể | Tổng hợp | Dollars | GM + staff |
| Sales & Operations Planning | Bán/sản xuất/tồn kho/backlog bao nhiêu | Volume (family) | Units, std hours | Cùng nhóm business planning |
| Demand Management | Dự kiến bán gì + hứa đơn khi nào | Mix (dần) | Units & dollars | Sales/Marketing |
| Rough-Cut Capacity Planning | Đủ nguồn lực cho production plan? | Tổng hợp | Hours/units | Vận hành |
| Master Scheduling | Build sản phẩm gì, bao nhiêu, khi nào | Mix (sản phẩm/đơn) | Units, theo tuần | Master scheduler |
| MRP | Component nào cần, khi nào | Chi tiết | Component | Material planner |
| CRP | Capacity nào cần, khi nào | Chi tiết | Standard hours/work center | Vận hành |
| Plant / Supplier Scheduling | Khi nào bắt đầu/hoàn thành/giao | Thực thi | Operation / lịch giao | Xưởng / supplier scheduler |

Ba khả năng lớn của ERP: (1) operational planning, (2) financial planning, (3) simulation ("what-if").

## Ví dụ minh họa (Worked Example)
**Ẩn dụ bữa tối Thanksgiving** ánh xạ trực tiếp các cấp ERP:
- **Sales & Operations Plan** = "Chúng ta ăn tối Thanksgiving vào thứ Năm tuần thứ ba của tháng 11" (quyết định mức volume/thời điểm).
- **Master Schedule** = *thực đơn*: gà tây, nhân nhồi, khoai tây, bí, rau, và mọi món kèm (mix sản phẩm cụ thể).
- **Bill of Material** = "Nhân nhồi gà tây cần một quả trứng, gia vị, và vụn bánh mì" (component tạo nên item trong master schedule).
- **Routing** = "Cho trứng và gia vị vào máy trộn" (các nguyên công).
- **Work Center** = *máy trộn* — nơi thực hiện gia công.

Trong sản xuất thật khác bữa tối ở chỗ: nhiều sản phẩm, lead time không ngắn như "chạy ra siêu thị", work center bận nhiều job, và khách đổi đơn khiến phải resequencing — đó chính là lý do cần cả hệ phân cấp + feedback của ERP. Khi master schedule buộc phải đổi, master scheduler nợ feedback cho sales nếu promise date trễ, và sales nợ cuộc gọi cho khách nếu ngày giao đã xác nhận bị trễ.

## Điểm cần nhớ (Key Takeaways)
1. ERP là hệ phân cấp: Strategic → Business Planning → S&OP → Demand Management → (RCCP) → Master Scheduling → MRP → (CRP) → Plant/Supplier Scheduling → Execution, với feedback theo ngoại lệ đi ngược lên.
2. Ranh giới then chốt: S&OP ở mức **volume** (family, units), Master Scheduling ở mức **mix** (sản phẩm/đơn, theo tuần); tổng master schedule phải khớp S&OP.
3. MRP cần bill of material + dữ liệu tồn kho; CRP cần routing + thời gian nguyên công.
4. Supplier scheduling thay thế requisition/PO bằng lịch từ MRP, horizon vượt lead time.
5. Financial integration cho "one set of numbers"; simulation cho "what-if".
6. Feedback chỉ theo exception, leo thang planner → master scheduler → sales → khách; chỉ đổi master schedule khi hết lựa chọn.

## Ứng dụng cho BA ERP (BA Application)
- Dùng bảng phân cấp này làm "bản đồ module chuẩn" khi viết tài liệu: mỗi cấp (S&OP, Demand Management, RCCP, Master Scheduling, MRP, CRP, Plant/Supplier Scheduling) là một nhóm chức năng với *đơn vị đo, chân trời thời gian, và vai trò (role)* riêng — nêu rõ ba thuộc tính này trong spec để tránh mơ hồ.
- Đặc tả quan hệ dữ liệu bắt buộc: Master Schedule → MRP cần **bill of material** và **inventory data**; MRP → CRP cần **routing** và **work center/thời gian nguyên công**. Thiếu các thực thể này thì chức năng không code được — BA phải liệt kê chúng như master data phụ thuộc.
- Viết quy tắc "tổng master schedule reconcile với S&OP cùng kỳ" như một business rule/kiểm tra toàn vẹn, không để ngầm.
- Mô hình hóa luồng feedback theo exception (anticipated delay) với chuỗi leo thang role cụ thể (planner → master scheduler → sales → customer) và điều kiện kích hoạt (chỉ khi không thực thi được) — đây là nơi nhiều spec bị thiếu.
- Chỉ rõ trong tài liệu khả năng **Customer Order Entry & Promising** phải truy vấn tồn kho/backlog/capacity/lead time và net với forecast để sinh promise date (ATP) — một chức năng cốt lõi dễ bị đặc tả sơ sài.
- Nhắc "one set of numbers": thiết kế để financial planning dùng chung dữ liệu vận hành (chỉ khác đơn vị đo), tránh yêu cầu hai hệ sổ.

## Liên hệ (Connects To)
- **Ch 12 & Ch 15**: định nghĩa chuẩn ở đây (plant scheduling, supplier scheduling, input-output, MRP, CRP) được dùng trong triển khai & đo lường.
- **Appendix B**: routing/back-scheduling của job shop vs flow shop — nền cho Plant Scheduling.
- **Glossary (APICS)**: ATP, allocation, action message, anticipated delay report — thuật ngữ chuẩn ngành.
- **S&OP / Master Scheduling (Oliver Wight, APICS)**: khung tham chiếu chuẩn cho hai cấp volume và mix.
