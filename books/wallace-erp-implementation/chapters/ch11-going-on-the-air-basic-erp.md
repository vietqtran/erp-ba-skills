# Chương 11: Lên sóng — ERP cơ bản, Giai đoạn I (Going on the Air — Basic ERP, Phase I)

## Ý tưởng cốt lõi (Core Idea)
"Going on the air" là bật và chạy thật các công cụ Phase I (S&OP, demand management, master scheduling, Rough-Cut Capacity Planning, MRP, và plant scheduling cho flow shop). Cách đúng để đưa master scheduling/MRP vào vận hành là **pilot approach** (thí điểm có kiểm soát), tuyệt đối tránh **big bang**; và phải chứng minh hệ thống "works" (cả kỹ thuật lẫn con người) cùng user sign-off trước khi cutover toàn bộ.

## Framework được giới thiệu (Frameworks Introduced)
- **Three Ways to Implement Systems** — ba cách triển khai: (1) **Parallel** (chạy mới song song cũ, so output, bỏ cũ khi mới đúng nhất quán) — đúng cho accounting nhưng với planning/scheduling vừa khó vừa bất khả thi (không có gì hợp lệ để so, vì hệ cũ là hot list / order point / **HARP** = Half-Baked Resource Planning); (2) **Big Bang / cold turkey / "you bet your company"** — khuyên chống tuyệt đối; (3) **Pilot** — cách đúng.
- **Three Kinds of Pilots** — ba loại pilot: (1) **Computer pilot** (kiểm thử kỹ hardware/software, dummy → real → volume testing; người làm: systems/DP); (2) **Conference room pilot** (education/training cho user, xác nhận phần mềm khớp business, dựng thủ tục, nhận diện nhu cầu policy; items thật + data giả); (3) **Live pilot** (moment of truth — MS/MRP chạy thật lần đầu, chứng minh "it works", lấy user sign-off).
- **5 tiêu chí chọn Live Pilot** — (1) Size (<500 items); (2) Product orientation (cả family / một product / một phần product); (3) Good cross-section (đủ finished, subassembly, manufactured, purchased, raw); (4) Relatively self-contained (ít common parts); (5) Best planner.
- **Silence Is Approval** — im lặng là đồng ý: phản hồi bắt buộc khi có trục trặc; khi mọi thứ ổn thì không cần nói, nhưng vừa biết một lịch sẽ trễ thì phải báo ngay (anticipated delay report) cho "khách hàng" kế tiếp.
- **Performance Measurements ở 3 cấp** — (1) performance goals (Ch6); (2) operational — ABCD Checklist; (3) technical measurements (chỉ số man/machine).

## Khái niệm chính (Key Concepts)
- **"Is it working?"** — pilot thành công khi hệ thống dự báo được thiếu hụt, ra khuyến nghị release/reschedule đúng, master schedule phản ánh cái đang làm thật, và hứa đơn tự tin qua available-to-promise.
- **Play Murphy / "Make It Fail"** — trong conference room pilot, một người (thường project leader) đóng vai Murphy gây sự cố (scrap cả lô, supplier trễ 3 tuần, máy hỏng, ECN khẩn) để kiểm tra cả software lẫn feedback của con người — một dạng bulletproofing, như "flight simulator".
- **Readiness tests** — kiểm tra sẵn sàng: (a) user đoán trước kết quả một transaction; (b) user giải thích được mọi con số trên report MS/MRP; (c) các mắt xích feedback đã sẵn sàng. Jerry Clement: chạy full business simulation với chuyên gia "hands-off" và trao end user quyền veto go-live.
- **Cutover** — chuyển nốt phần còn lại: multiple-group (ưu tiên, ít rủi ro, planner giúp nhau) hoặc one-group (khi common parts nhiều hoặc tổng item ít).
- **Inventory blip** — tồn kho có thể tăng trước khi giảm (~50-50) vì MRP reschedule được đơn mở nhưng không "reschedule out" được hàng đã nằm kho → expedite nhiều hơn de-expedite.
- **Don't starve the sources** — đừng bỏ đói nhà máy/nhà cung cấp: tồn kho tụt quá nhanh làm cạn việc, gây ấn tượng xấu dai dẳng; nếu cần, release việc sớm để giữ dòng chảy.

## Mô hình tư duy (Mental Models)
- Pilot càng nhiều process càng tốt (S&OP, MS, MRP, sales forecasting, inventory transaction, BOM) — "avoid big bangs, or even little bangs".
- Ở bước pilot, tư duy "triển khai quyết liệt" phải nhường chỗ: không vượt qua pilot cho tới khi nó chạy được và user đã ký.
- Trong cutover, ba việc quan trọng nhất là "Communicate, Communicate, Communicate"; project leader phải có mặt liên tục "xách xô nước", "đừng làm ngập planner mà hãy làm ngập vấn đề".
- Walt Goddard: "look below the surface" — đừng giả định ổn, hãy giả định chưa ổn rồi dò (sample hành động của planner), để nếu ổn thì là bất ngờ dễ chịu.

## Điều cần tránh (Anti-patterns)
- **Big bang / cold turkey**: output lần chạy đầu làm ngập user → ERP fail; mất khả năng đặt vật tư/release production vì hệ cũ đã dừng và dữ liệu không còn hợp lệ → mất khả năng giao hàng.
- **Parallel cho planning/scheduling**: bất khả thi vì không có baseline hợp lệ để so.
- **Delay cutover chờ mốc kế toán** (đầu tháng/quý/năm tài chính): thay vào đó dựng bridging program.
- **The Inadvertent Big Bang**: cài inventory transaction processor mới (không có ordering logic) rồi bỏ hệ cũ (có ordering logic) → mất khả năng đặt hàng → vá vội bằng bật MRP toàn bộ chưa kiểm thử = big bang tệ nhất.
- **Để tồn kho tụt quá nhanh** làm cạn việc nhà máy/supplier.

## Bảng tham chiếu (Reference Tables)
Ba loại pilot (Figure 11-2):

| Loại pilot | Người chính | Items / Data | Mục tiêu |
|---|---|---|---|
| Computer | Systems people, project leader | dummy→live, cuối cùng live/live | Hiểu software; tìm bug; kiểm run/response time, storage |
| Conference room | Customer service, master scheduler, MRP planners, systems analyst, project leader | items thật, data giả | Education/training; xây feedback; xác nhận software khớp business |
| Live | Customer service, master scheduler, MRP planners, project leader | live/live | Dùng thật; chứng minh works; lấy user sign-off |

Technical measurements (chọn lọc): thay đổi master schedule trong near-term zone (phải nhỏ); reschedule-in ≈ reschedule-out; số item overpromised; MRP exception volume (job shop ≤10%); late order releases ≤5%; stock outs; inventory turns; user time nhập liệu.

## Ví dụ minh họa (Worked Example)
**The Inadvertent Big Bang (bẫy vô tình)** — 5 bước dẫn tới thảm họa: (1) cần cài inventory transaction processor mới để đạt 95% chính xác tồn kho; (2) phải làm trước khi bật MS/MRP (đúng — dữ liệu phải chính xác trước); (3) nhưng hệ tồn kho cũ chứa ordering logic (báo khi nào đặt lại), còn module mới chỉ giữ số dư — ordering logic nằm trong MRP; (4) công ty bật processor mới và đồng thời bỏ cái cũ; (5) kết quả: mất khả năng đặt vật tư. Giải pháp đúng: nhận diện trước và chạy song song cả hai inventory processor tới khi MS/MRP lên, hoặc viết bridge tạm, hoặc dựng ordering logic tạm.

**Chuẩn bị Live Pilot** — project team trả lời "Yes" cho 6 mục đầu của checklist (pilot đã chọn; computer pilot xong; conference room pilot xong; dữ liệu còn đạt 95% tồn kho / 98% BOM trên MỌI item; education ≥80% toàn công ty; có chuẩn y của steering committee) → project leader báo steering committee và xin phép chính thức → chỉ khi đó mới khởi động live pilot; chạy ~1 tháng, không vượt qua pilot cho tới khi works + user sign-off.

## Điểm cần nhớ (Key Takeaways)
1. Dùng pilot approach; tránh big bang và cả "little bang". Pilot càng nhiều process càng tốt.
2. Ba loại pilot theo trình tự: computer → conference room (education/training, "Make It Fail") → live pilot (chứng minh + user sign-off).
3. Chọn live pilot theo 5 tiêu chí (<500 items, product orientation, cross-section, self-contained, best planner).
4. Cutover: ưu tiên multiple-group; đừng chờ mốc kế toán; dựng feedback (anticipated delay report) và plant scheduling tạm; lường inventory blip và tránh "starve the sources".
5. Áp dụng "silence is approval" ngay từ Phase I; đo hiệu năng ở 3 cấp (performance goals, ABCD Checklist, technical measurements), hằng tuần, theo từng planner.
6. Kết thúc bằng Audit/Assessment II làm điểm go/no-go cho Phase II, có steering committee chuẩn y.

## Ứng dụng cho BA ERP (BA Application)
- Đặc tả chiến lược cutover trong tài liệu theo đúng ba lựa chọn (parallel / big bang / pilot) và nêu rõ pilot là mặc định cho planning/scheduling; parallel chỉ cho phân hệ kế toán — giúp tài liệu migration không "khuyến nghị" cách sai.
- Viết acceptance criteria go-live dạng Yes/No theo checklist của chương (pilot chọn, các pilot hoàn tất, dữ liệu còn đạt ngưỡng, education ≥80%, steering committee chuẩn y, user sign-off) — mỗi chức năng cần một "definition of done" có cổng phê duyệt.
- Mô tả feedback loops như business rule bắt buộc: "silence is approval" → mỗi role (plant, purchasing, planner, customer service) phải sinh anticipated delay report khi biết sẽ trễ; định rõ ai báo cho ai.
- Thiết kế kịch bản kiểm thử UAT theo kiểu "play Murphy / Make It Fail": mỗi chức năng kèm các tình huống lỗi (scrap, supplier trễ, ECN khẩn, máy hỏng) để kiểm cả hệ thống lẫn luồng phản hồi — tránh tài liệu chỉ mô tả happy path.
- Đưa bộ technical measurements vào mục reports/KPI của tài liệu (reschedule-in≈out, MRP exception ≤10%, late releases ≤5%, overpromised, stock outs, inventory turns, user time) làm thước đo nghiệm thu sau go-live.
- Cảnh báo rủi ro chuyển đổi trong tài liệu: inventory blip và inadvertent big bang — đặc tả rằng module mới nào thay thế logic nào, không được tắt hệ cũ khi logic tương ứng chưa sẵn sàng ở hệ mới.

## Liên hệ (Connects To)
- **Ch 3**: trình tự Phase I/II/III và implementation sequence.
- **Ch 9**: parallel approach cho F&A; "silence is approval" và feedback nối tới policies.
- **Ch 10**: ngưỡng data integrity (95%/98%) là tiền đề bắt buộc trước live pilot/cutover.
- **Ch 6**: performance goals là cấp đo thứ nhất.
- **Ch 12**: Phase II — Supply Chain Integration, đóng vòng lặp hoàn toàn (plant floor control, CRP, supplier scheduling).
- **Cutover / UAT / go-live gate**: liên hệ chuẩn viết kế hoạch chuyển đổi, kịch bản UAT, và cổng phê duyệt go-live trong tài liệu BA.
