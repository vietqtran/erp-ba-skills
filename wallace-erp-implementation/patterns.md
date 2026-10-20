# Patterns — ERP: Making It Happen (Wallace & Kremzar)

Các kỹ thuật/thủ pháp triển khai ERP có thể tái dùng. Mỗi pattern: **When** (khi nào) · **How** (cách làm) · **Trade-offs** (đánh đổi).

## Phạm vi & tổ chức dự án

### Schedule by Business Function, Not Software Modules
- **When**: Khi lập kế hoạch/backlog cho một dự án ERP.
- **How**: Mô tả và sắp xếp công việc theo nghiệp vụ cần làm + phụ thuộc giữa chúng, rồi mới ánh xạ sang module/switch phần mềm; không lấy trình tự module theo vendor làm xương sống.
- **Trade-offs**: Đòi hiểu nghiệp vụ sâu hơn, nhưng tránh sai trình tự (MRP trước master schedule) và thông điệp "ERP là dự án máy tính".

### Three-Phase Serial + Simultaneous
- **When**: "Nuốt con voi" ERP toàn công ty trong ~18 tháng.
- **How**: Chia dự án thành vài phase lớn làm tuần tự (I→II→III); trong mỗi phase chạy nhiều task song song. Chỉ nhận "have-to's" của Basic ERP vào Phase I.
- **Trade-offs**: Kiểm soát phụ thuộc tốt, chống scope creep; nhưng cần kỷ luật giữ Phase I gọn.

### Staggered Multiplant Rollout
- **When**: Triển khai cho tổ chức nhiều nhà máy, nguồn lực tập trung hạn chế.
- **How**: Lệch pha các nhà máy (không serial quá dài, không simultaneous quá tải); mỗi thời điểm chỉ 1 nhà máy pilot/cutover MS+MRP; nhà máy sau học từ nhà máy trước. S&OP vẫn làm đồng loạt và sớm.
- **Trade-offs**: Tổng thời gian dài hơn simultaneous nhưng ngắn hơn serial nhiều, giảm rủi ro/tải.

### Run-over-by-a-Train Test
- **When**: Lãnh đạo nói "không thể giải phóng ai làm project leader toàn thời gian".
- **How**: Giả định quản lý giỏi nhất "bị tàu tông", cử họ làm project leader, thuê người ngoài lấp vị trí vận hành trống.
- **Trade-offs**: Đau ngắn hạn cho ưu tiên #1 (chạy business), nhưng là phép thử cam kết thật.

### Spin-Off Task Force
- **When**: Project team gặp một vấn đề điểm cần nghiên cứu sâu mà không nên sa lầy cả nhóm.
- **How**: Lập tổ liên phòng ban có thời hạn, giao nghiên cứu + đề xuất phương án, báo cáo rồi giải tán (đôi khi "one-person task force").
- **Trade-offs**: Giảm tải cho trưởng bộ phận; cần đảm bảo khuyến nghị thực sự vào lịch thực thi.

## Chuẩn bị & biện minh

### Learn-First-Then-Justify
- **When**: Quyết định có làm ERP và cấp vốn cho nó.
- **How**: Hoàn thành first-cut education (+ audit/assessment) TRƯỚC khi làm cost/benefit; không cost-justify khi chưa hiểu ERP.
- **Trade-offs**: Tốn thời gian học ban đầu, nhưng tránh ước thấp cả chi phí lẫn lợi ích → thiếu vốn, thiếu ưu tiên.

### Joint-Venture Cost/Benefit
- **When**: Lập cost/benefit cho quyết định Go/No-Go.
- **How**: Những người sẽ chịu trách nhiệm đạt lợi ích (top + operating management từng phòng) tự làm số sau khi học first-cut, rồi hợp nhất; ước bảo thủ (chi phí cao, lợi ích thấp).
- **Trade-offs**: Tốn công phối hợp hơn "decree"/"middle sells up", nhưng tạo đồng thuận trên-dưới và chéo chức năng.

### ABC Budgeting (People / Data / Computer)
- **When**: Lập ngân sách/phạm vi chi phí và khi phải cắt giảm.
- **How**: Nhóm mọi chi phí vào A=People, B=Data, C=Computer; nếu buộc cắt thì cắt C trước, giữ A.
- **Trade-offs**: Cắt C có thể làm chậm tự động hoá, nhưng bảo vệ yếu tố con người — yếu tố quyết định thành/bại.

### Cost-of-One-Month-Delay Metric
- **When**: Giữ ưu tiên và biện minh tăng nguồn lực thay vì kéo dài lịch.
- **How**: Tính Tổng lợi ích/12 thành một con số duy nhất, làm nổi bật suốt dự án; so chi phí trễ với chi phí thuê trợ giúp tạm thời.
- **Trade-offs**: Là ước lượng, nhưng rất hiệu quả chống tâm lý "chỉ có thể tăng thời gian".

## Giáo dục & quy trình

### Business Meeting (1/4 Fact Transfer, 3/4 Discussion)
- **When**: Tạo team of experts rồi lan tới critical mass trong giáo dục ERP.
- **How**: 20–40 buổi ~2 giờ; agenda: fact transfer → tóm tắt → thảo luận ứng dụng → đồng thuận → phân công → **ghi lại quyết định**; dành 3/4 thời gian thảo luận.
- **Trade-offs**: Tốn nhiều thời gian quản lý, nhưng là cỗ máy tạo behavior change & ownership.

### Just-in-Time Education
- **When**: Lên lịch đào tạo cho các nhóm chức năng khác nhau.
- **How**: Đào tạo mỗi nhóm ngay trước khi chức năng của họ được triển khai (top management & sales sớm, production associates muộn hơn).
- **Trade-offs**: Tránh quên kiến thức, nhưng đòi lịch đào tạo bám sát tiến độ.

### Five Bedrock Policies Drafting
- **When**: Định nghĩa quy trình vận hành ERP.
- **How**: Project team xác định policy cần → spin-off task force soạn → revise/approve → steering committee duyệt → GM ký, hiệu lực từ ngày cụ thể. Mỗi policy có roles, parameters, feedback, performance measurements.
- **Trade-offs**: Phải thực sự thi hành (không chỉ ký giấy) và tinh chỉnh theo kinh nghiệm.

### Rolling 90-Day Schedule (Chris Gray)
- **When**: Quản lý lịch dự án ERP dài 12–18 tháng.
- **How**: Chốt major milestones + 300–600 activities; 90 ngày gần làm chi tiết, xa hơn phác thảo; tái tạo lịch chi tiết 90 ngày mỗi ~60 ngày; "name names, not job titles".
- **Trade-offs**: Không dự liệu hết việc xa, nhưng giữ lịch sống, bám thực tế.

## Dữ liệu

### Cycle Counting + Limited Access (trình tự đạt độ chính xác)
- **When**: Cần đạt/giữ độ chính xác bản ghi tồn kho (nền cho MRP/DRP).
- **How**: Đo baseline trên mẫu (~100 item) → giới hạn truy cập kho ("chicken wire stockroom" hoặc vạch sơn) → thiết lập cycle counting (control group ~100 item/tuần, confirming recount, %accuracy = hits/total) → đếm ongoing → song song giáo dục + đào tạo nhân viên kho. Loại bỏ nguyên nhân lỗi, không chỉ sửa bản ghi.
- **Trade-offs**: Thay annual physical inventory; giới hạn truy cập gây ma sát ngắn hạn; cần kỷ luật liên tục.

### BOM Accuracy — Middle-of-the-Road Method
- **When**: Đo độ chính xác bill of material (mục tiêu ≥98%).
- **How**: Tính hit/miss theo quan hệ component-to-parent ở từng cấp (không phải cả bill như tight, không phải từng dòng như loose).
- **Trade-offs**: Cân bằng nhất; quan trọng là chọn một phương pháp và giữ nhất quán để biết đang cải thiện hay thụt lùi.

### Change-Only-What's-Necessary
- **When**: Suốt quá trình triển khai, khi nạp item/work-center data.
- **How**: Dùng lại số đang có, chỉ sửa cái rõ ràng sai; hoãn mọi cải tiến phụ tới sau go-live.
- **Trade-offs**: Giảm kháng cự con người và dễ chẩn đoán lỗi; bỏ lỡ vài cải tiến sớm (chấp nhận được).

## Go-live, pilot & chuyển đổi

### Three Kinds of Pilots (Pilot thay vì Big Bang)
- **When**: Đưa master scheduling/MRP (planning/scheduling) vào vận hành.
- **How**: Computer pilot (kiểm thử HW/SW, dummy→real→volume) → Conference room pilot (education/training, data giả, "play Murphy") → Live pilot (chạy thật, lấy user sign-off). Chọn live pilot theo 5 tiêu chí (<500 items, product orientation, cross-section, self-contained, best planner).
- **Trade-offs**: Chậm hơn bật toàn bộ, nhưng loại rủi ro sụp đổ vận hành; không vượt live pilot cho tới khi works + sign-off.

### Play Murphy / Make It Fail
- **When**: Trong conference room pilot, kiểm thử sẵn sàng.
- **How**: Một người đóng Murphy gây sự cố (scrap lô, supplier trễ, máy hỏng, ECN khẩn) để kiểm cả software lẫn luồng feedback con người — như flight simulator.
- **Trade-offs**: Cố ý làm hỏng trong môi trường an toàn; cần người dẫn pilot chủ động.

### Multiple-Group Cutover
- **When**: Chuyển nốt các item còn lại lên MS/MRP sau live pilot.
- **How**: Chia item còn lại thành nhiều nhóm, cutover từng nhóm; planner B/C giúp planner A khi nhóm A lên, luân phiên.
- **Trade-offs**: Ít rủi ro, dễ cho người; nhưng common parts nhiều hoặc tổng item ít thì one-group lại tốt hơn.

### Interim Plant Scheduling During Cutover
- **When**: Job shop cutover khi MS/MRP đã lên nhưng plant floor control/CRP (Phase II) chưa có.
- **How**: Dựng hệ scheduling tạm (thường thủ công) dùng order due date + back scheduling; cử một người nhà máy toàn thời gian giữ liên lạc planner-foreman, sinh anticipated delay report, phá bottleneck.
- **Trade-offs**: Giữ order date hợp lệ, tránh "starve the sources"; là giải pháp tạm tới Phase II.

## Chuỗi cung ứng (Phase II)

### Job Shop Plant Scheduling Sequence
- **When**: Lên sóng lập lịch xưởng cho môi trường job shop.
- **How**: Theo thứ tự cứng: (1) Shop floor control/dispatching (khẩn cấp nhất) → (2) CRP → (3) Input-output control (phải sau CRP). Pilot 2–3 tuần bằng các job chạy qua nhiều work center.
- **Trade-offs**: Pilot không test được dispatch list (chỉ sau cutover khi mọi job lên hệ thống).

### Supplier Scheduling 8-Step Rollout
- **When**: Triển khai lập lịch nhà cung cấp ở Phase II, sau khi hầu hết sản phẩm đã lên MS/MRP.
- **How**: Thiết lập cách tiếp cận (hợp đồng, báo cáo, số PO) → có phần mềm (có thể tự viết, chủ yếu retrieval-and-display) → giáo dục nhà cung cấp (1 ngày) → pilot 1–vài nhà cung cấp, cut over ngay → tinh chỉnh + đo → cut over ~20% nhà cung cấp lớn (Pareto) theo nhóm 3–6/ngày → đo hai phía → cut over phần còn lại, mục tiêu 100%.
- **Trade-offs**: Đạt 100% mất lâu hơn mốc Proven Path; nhà cung cấp kháng cự cần leo thang cấp president hoặc thay nhà cung cấp.

### DRP Pilot-Within-a-Pilot
- **When**: Triển khai DRP cho hệ thống nhiều distribution center.
- **How**: Pilot = một DC; mini-pilot = ~một tá sản phẩm trong DC đó để chứng minh little DRP; rồi cut over tất cả sản phẩm sang little DRP, chạy big DRP cho DC pilot, cuối cùng cut over các DC còn lại.
- **Trade-offs**: Yêu cầu inventory records (95%+) và bill of distribution (98%+) rất chính xác — phần khó nhất.

## Quick-Slice

### Quick-Slice (120-Day Slice)
- **When**: Khách đã có ES nhưng chưa cải tiến, re-implementers, cần payback nhanh, công ty cực lớn, hoặc nguy cơ sống còn — và có một slice tách được + urgency.
- **How**: Chọn một product family tác động cao; triển khai đầy đủ chức năng ERP cho nó theo Proven Path nén (tuần thay tháng); bỏ finance/accounting, thêm physical process improvement; pilot = cutover; S&OP làm cho tất cả family.
- **Trade-offs**: Phải chạy hai hệ thống; lý thuyết lâu hơn mới tới Class A; không có slice/flow hoặc thiếu urgency thì không dùng được.

### Quick-Slice Product Selection (5 Criteria)
- **When**: Chọn slice đầu tiên để triển khai.
- **How**: Chấm theo 5 tiêu chí: High Impact/High Visibility (Pareto Class A), Largely Self-Contained (ít dùng chung component/work center), Good People, Stability (không thay đổi lớn treo), Applicability (bài học áp dụng được phần còn lại). Thỏa hiệp nếu cần nhưng bám sát.
- **Trade-offs**: Hiếm khi có slice thỏa cả 5; chọn sai (quá đan xen) làm slice thất bại.

### Common-Parts Segregation
- **When**: Item dùng chung giữa sản phẩm slice và non-slice gây khó cho độ chính xác dữ liệu.
- **How**: Trữ ở hai vị trí khác nhau và thêm hậu tố mã (ví dụ chữ "S" = slice) cho item slice; kèm chỉnh sửa nhỏ BOM của slice để gọi đúng item "S".
- **Trade-offs**: Tăng số mã item và sửa BOM; chỉ là giải pháp tạm cho giai đoạn hai-hệ-thống.

### Conceptual Cells to Create Flow Fast
- **When**: Job shop cần tạo flow cho slice nhưng di dời thiết bị sẽ làm trễ.
- **How**: Không di dời máy; liên kết thiết bị theo dòng bằng kanban (conceptual cell), lên sóng slice trước, di dời máy sau; đánh dấu trực quan (sơn/cờ cùng màu).
- **Trade-offs**: Chưa đạt lợi ích vật lý đầy đủ của physical cell; là bước quá độ.

## Vận hành & nghiệm thu

### ERP Operating Committee with Rotating Chairmanship
- **When**: Sau go-live, để không để ERP tụt hạng.
- **How**: Giữ project team nhưng bỏ thành viên full-time (gần 100% trưởng bộ phận), đổi tên thành operating committee, họp ~mỗi quý, ghế chủ tịch luân phiên 1–2 lần/năm; nhiệm vụ: đo hiệu suất, báo cáo top management, triển khai cải tiến.
- **Trade-offs**: Cần kỷ luật duy trì lâu dài; dễ bị ưu tiên khác lấn át nếu không gắn Class A với lợi ích kinh doanh.

### ABCD Checklist Review Loop
- **When**: Rà soát vận hành ERP ≥2 lần/năm.
- **How**: Với mỗi "no": (1) xác định nguyên nhân, (2) chọn cách sửa (một bộ phận → trưởng bộ phận; vượt ranh giới → spin-off task force), (3) đặt ngày sửa cụ thể. Báo cáo điểm/hạng/no-answers lên steering committee; re-certify Class A hằng năm.
- **Trade-offs**: Tốn thời gian họp đồng thuận; nhưng là động cơ chống tụt hạng.

### Implementers' Checklist (nghiệm thu Yes/No)
- **When**: Cần tiêu chí nghiệm thu khách quan cho từng giai đoạn/chức năng.
- **How**: Liệt kê các task bắt buộc dưới dạng câu trả lời Yes/No; chỉ khi tất cả "Yes" mới coi là đạt; cho phép thêm task, cấm xoá task.
- **Trade-offs**: Có thể dài, nhưng biến sự tuân thủ Proven Path thành thứ kiểm được, giảm tranh cãi chủ quan.

### Change-Request Control (2 nguyên tắc + 5 bước)
- **When**: Quản lý yêu cầu sửa đổi phần mềm trong và sau triển khai.
- **How**: Nguyên tắc: cưỡng lại thay đổi cục bộ + luôn theo một quy trình công nhận. Bước: IT ước lượng & phân loại minor/major (không phán xét nghiệp vụ) → project team quyết minor → xét major bằng câu hỏi "cần để điều hành/ERP chạy đúng? cần máy tính hay thủ công?" → bất đồng mạnh đưa lên steering committee.
- **Trade-offs**: Thêm thủ tục nhưng giữ số thay đổi ở mức "important few", tránh dự án mất kiểm soát.

### Factoid Technique for Selling Strategy
- **When**: Thuyết phục lãnh đạo chuyển đổi chiến lược/đầu tư ERP.
- **How**: Đổi %/$ thành con số-hình ảnh cụ thể gắn với nỗi đau lãnh đạo ("3% missed" → "3.000 đơn/năm, 15/ngày"); bán vision bằng câu đơn giản; tránh bẫy "either/or" (chọn cả hai).
- **Trade-offs**: Factoid không phải thước đo chuẩn; dùng để tạo ấn tượng, cần hậu thuẫn bằng dữ liệu thật.
