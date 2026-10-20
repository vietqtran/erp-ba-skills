# Patterns — kỹ thuật & mẫu thiết kế ERP (O'Leary, 2000)

Các kỹ thuật cụ thể BA có thể áp dụng khi viết tài liệu ERP. Tên framework giữ nguyên tiếng Anh.

## MAPs decomposition cho đặc tả chức năng
**When to use**: Khi viết đặc tả bất kỳ chức năng ERP nào (Ch 3, 10).
**How**: Tách mô tả thành ba phần — **Models** (mô hình dữ liệu/tổ chức và *giả định* của nó), **Artifacts** (chứng từ và danh mục/master data), **Processes** (luồng liên chức năng).
**Trade-offs**: Có cấu trúc rõ, map được sang gói ERP; nhưng đòi hỏi BA hiểu giả định từng model, nếu không sẽ thiết kế trái giả định gây conflict.

## As Is / To Be process modeling
**When to use**: Bước khảo sát yêu cầu và chọn/cấu hình phần mềm (Ch 2, 8, 9).
**How**: Dựng mô hình quy trình hiện tại ("as is") và quy trình đích ("to be"); dùng khoảng cách để quyết đổi phần mềm hay đổi quy trình.
**Trade-offs**: Chống lệch yêu cầu; nhưng nếu định tái cấu trúc mạnh thì "as is" mất giá trị — đừng mô hình hóa chi tiết thừa.

## Relational normalization cho master data
**When to use**: Thiết kế danh mục/master data trong spec dữ liệu (Ch 2).
**How**: Chuẩn hóa thành bảng liên kết qua khóa; chỉ lưu mã tham chiếu trên giao dịch, tra chi tiết ở bảng liên quan; thêm một dòng cho mỗi mục thay vì trường cố định.
**Trade-offs**: Loại dư thừa, mỗi thực thể định nghĩa một lần; yêu cầu tư duy quan hệ thay vì tệp phẳng.

## Gather-data-once kèm input controls
**When to use**: Đặc tả màn hình/luồng nhập liệu (Ch 4).
**How**: Nhập một lần tại điểm phát sinh; bắt buộc kèm **data input controls** + process map (ai nhập, ở đâu, khi nào); thêm bước xác nhận tường minh nếu hành động không tự hoàn tất.
**Trade-offs**: Chi phí thấp, nhất quán; nhưng sai một chỗ sai toàn hệ và người nhập có thể không phải kế toán ⇒ cần đào tạo/UI.

## Screens-to-Transactions difficulty model
**When to use**: Dự báo rủi ro nhập liệu khi chuyển legacy sang ERP (Ch 4).
**How**: Tính tỉ lệ số màn hình ERP/legacy × khối lượng giao dịch; tỉ lệ cao + khối lượng lớn = vùng rất khó, đồng thời là thước đo thiếu "fit".
**Trade-offs**: Cảnh báo sớm nguy cơ mất đơn/quá tải nhân sự; là ước lượng định tính, cần số liệu khối lượng thực.

## Four output alternatives selection
**When to use**: Khi báo cáo chuẩn ERP không đủ đáp ứng (Ch 5).
**How**: Chọn giữa standard reports/queries, customized reports, intranet/Lotus Notes, data warehouse theo loại người dùng (expert vs casual) và loại truy vấn (chuẩn vs ad hoc).
**Trade-offs**: Customized report ngắn hạn và cản nâng cấp; data warehouse linh hoạt nhưng tốn chi phí dựng và nhân sự query.

## Role-specific desktop / portal design
**When to use**: Thiết kế màn hình chính và điểm truy cập cho người dùng (Ch 5).
**How**: Gom theo vai trò công việc — module con liên quan, báo cáo, help-desk, lịch/email; phân tầng expert dùng ERP trực tiếp, casual qua portal/intranet.
**Trade-offs**: Dễ dùng, tiết kiệm seat cost; cần ma trận phân quyền rõ theo vai trò.

## Technology enabled vs clean slate selection
**When to use**: Trước khi viết spec quy trình để định mức tự do thiết kế (Ch 6).
**How**: Đánh giá quy mô, ngân sách, thời gian, tính độc quyền của quy trình. Nhỏ/hạn chế/ép thời gian/chuẩn ⇒ technology enabled; lớn/deep pockets/dư thời gian/độc nhất ⇒ clean slate.
**Trade-offs**: Technology enabled khả thi và rẻ nhưng bị ràng buộc; clean slate độc nhất nhưng tốn kém và có thể không có phần mềm đáp ứng.

## Rationale-to-acceptance-criteria conversion
**When to use**: Lập business case và định nghĩa tiêu chí nghiệm thu (Ch 7).
**How**: Phân loại rationale; chuyển process/strategic rationale thành mục tiêu định lượng (ví dụ đóng sổ 24→6 ngày, giảm 40% tồn kho) rồi dùng làm acceptance criteria.
**Trade-offs**: Tạo chuẩn nghiệm thu rõ; technology/competitive rationale không cho tiêu chí nên phải bổ sung.

## Wagle's Five-Step NPV
**When to use**: Lượng hóa quyết định đầu tư ERP (Ch 7).
**How**: (1) base case tiết kiệm không có ERP; (2) ERP case tiết kiệm có ERP; (3) NPV phần hiệu; (4) phân tích độ nhạy chịu trượt tiến độ/vượt chi phí; (5) phân bổ ngược chi phí về từng đơn vị kèm trách nhiệm.
**Trade-offs**: Tách được giá trị thực do ERP; nhưng lợi ích thường fuzzy và chi phí bị ẩn nên dữ liệu có thể không đáng tin.

## Scripted demo hai pha
**When to use**: Khi đánh giá vendor ERP và cần phát hiện gap cần modification (Ch 8).
**How**: Pha 1 lỏng — vendor trình diễn demo gần cố định; pha 2 chặt — bắt vendor dùng chính dữ liệu và nghiệp vụ thật của khách để thực hiện hoạt động cụ thể.
**Trade-offs**: Pha chặt tốn công chuẩn bị dữ liệu nhưng lộ gap sớm; pha lỏng dễ bị vendor dẫn dắt.

## Weighted-criteria + blue-ribbon voting (đánh giá vendor)
**When to use**: Khi cần một con số tổng hợp để so sánh các gói ERP vượt ngoài chức năng (Ch 8).
**How**: Liệt kê factor + weight, chốt TRƯỚC demo, chấm điểm từng gói rồi cộng tổng; hoặc lập blue-ribbon team ≤10 người chấm theo chuyên môn trên functional fit + implementation personnel (thang 3-1).
**Trade-offs**: Gọn, tạo buy-in; nhưng factor/weight dễ bị thao túng (Timberjack cho functionality chỉ 30/160) và chủ quan theo nhận thức.

## Small-r reengineering (không sửa phần mềm)
**When to use**: Quy trình generic (tài chính, back office) hoặc firm là "software taker" (Ch 9).
**How**: Triển khai module theo đúng best practice có sẵn, không modification; điều chỉnh tổ chức khớp phần mềm (profit/cost center thay cho "phòng ban").
**Trade-offs**: Nhanh, rẻ, dự đoán được; nhưng bỏ lỡ cơ hội cải tiến, không tạo lợi thế cạnh tranh bền vững.

## Business lead / process owner dẫn dắt dự án
**When to use**: Khi triển khai ERP có thay đổi quy trình lớn (Ch 9).
**How**: Đặt một process owner (dân nghiệp vụ, không phải IT) làm business lead — người hưởng lợi nếu thành công, chịu hại nếu thất bại; CIO dọn chướng ngại.
**Trade-offs**: Tăng buy-in nghiệp vụ; cần lãnh đạo mạnh để áp "việc đã quyết, chỉ bàn cách làm".

## Group-choice rule chọn chuẩn MAPs
**When to use**: Khi nhiều division phải thống nhất một bộ MAPs chung ("input by many, design by few") (Ch 10).
**How**: Chọn một luật công khai — **Majority Vote**, **Borda Rule** (xếp hạng → cộng điểm), **Pareto Optimality**, hoặc **Dictatorship** — và nêu rõ lý do dùng.
**Trade-offs**: Thu ý kiến nhiều bên; nhưng mỗi luật đều thất bại ở một tình huống, chọn MAPs vẫn là quá trình chính trị.

## Big bang vs phased contingency selection
**When to use**: Khi chọn chiến lược triển khai (Ch 11).
**How**: Đánh giá theo size/complexity, hierarchy/control, số module × module fit. Nhỏ/phẳng/lỏng/ít module/cần cross-module ⇒ big bang; lớn/nhiều tầng/chặt/nhiều module/nhiều modification ⇒ phased; ở giữa dùng waved.
**Trade-offs**: Big bang ngắn và rẻ nếu suôn sẻ nhưng không đường lùi; phased an toàn hơn nhưng lâu, tốn temporary interface và trì hoãn tính năng cross-module.

## Color-coded readiness board
**When to use**: Khi điều phối chuẩn bị cho một đợt test/cutover lớn (big bang) (Ch 11).
**How**: Liệt kê mọi task/subtask có owner trong các nhóm (functionality, performance, data conversion, IS readiness, training, docs, site readiness); gán green=ready, yellow=cần can thiệp thủ công, red=chưa sẵn sàng; dồn sức vào đỏ.
**Trade-offs**: Trực quan, tập trung nguồn lực; cần cập nhật liên tục và owner rõ ràng.

## Systems Validation Test (SVT)
**When to use**: Trước go-live big bang để kiểm chứng toàn hệ (Ch 11).
**How**: Chạy conference room pilot từng module, rồi gom ~100 user nhập khối lượng giao dịch lớn mô phỏng tải thật và test phần cứng/interdependency giữa các module.
**Trade-offs**: Phát hiện lỗi tích hợp trước go-live; nhưng tốn thời gian (6-8 tháng ở Quantum) và nguồn lực tập trung.

## Reconcile + mapping dữ liệu chuyển đổi
**When to use**: Khi migrate dữ liệu từ legacy sang ERP (Ch 12).
**How**: Reconcile số liệu hai nguồn (tồn kho/sản phẩm/vendor có khớp không, vì sao không); mapping từng trường từ CSDL này sang CSDL kia để không trộn/bỏ sót.
**Trade-offs**: Bắt lỗi conversion trước khi chúng ngụy trang thành triệu chứng kinh doanh; nhưng tốn công và cần baseline legacy đáng tin.

## Metric-not-goal definition
**When to use**: Khi định nghĩa tiêu chí nghiệm thu benefit sau go-live (Ch 12).
**How**: Mỗi con số mong muốn phải thành metric có baseline + owner + quy được về chính ERP; đưa Deloitte Post-Implementation Checklist (Yes/No) vào acceptance criteria.
**Trade-offs**: Cho chuẩn nghiệm thu thực; nhưng cần chờ 1-2 năm và một năm dữ liệu để đo được.

## Đào tạo qua super users + script-based materials
**When to use**: Khi cần lan tỏa đào tạo ERP và viết tài liệu hỗ trợ (Ch 13).
**How**: Chỉ định **super users** trong tổ chức khách, đào tạo trước để họ huấn luyện lại; viết tài liệu **script-based** dẫn user từng bước qua trọn một giao dịch, đặt trên mạng nội bộ.
**Trade-offs**: Người quen dạy nên dễ tiếp thu; script cho ngữ cảnh nhưng user kẹt khi ra ngoài kịch bản ⇒ cần bổ sung năng lực tra cứu.

## Configuration engine chặn lỗi đặt hàng
**When to use**: Khi cho khách tự đặt hàng qua web/EDI (Ch 14).
**How**: Engine kiểm tra đơn so với account/purchase info, chặn lỗi phổ biến (sai part number, cấu hình không hợp lệ), "không cho đặt nếu còn lỗi".
**Trade-offs**: Giảm 25-33% lỗi fax và chi phí xử lý; nhưng khách vẫn phải nhập lại vào hệ của họ nếu chưa tích hợp.

## EDI vs WFT selection
**When to use**: Khi đặc tả kênh trao đổi dữ liệu với đối tác (Ch 14).
**How**: Chọn **EDI** khi khối lượng giao dịch lớn + đối tác lớn; chọn **WFT** khi originator ít giao dịch; chỉ nối ERP-to-ERP khi hai hệ chung một phần MAPs.
**Trade-offs**: EDI bền nhưng cứng và đắt (VAN); WFT rẻ nhưng gây double data-entry nếu originator nhiều giao dịch.

## Risk Matrix enumeration
**When to use**: Khi lập risk register cho dự án ERP (Ch 15).
**How**: Dựng ma trận giai đoạn vòng đời × loại rủi ro (technical/business/organizational); mỗi ô ghi mặt success nếu xử lý tốt / mặt failure nếu hỏng; ưu tiên organizational > business > technical.
**Trade-offs**: Bao phủ có hệ thống; nhưng một rủi ro có thể thuộc nhiều ô, phân loại không duy nhất.
