# Tri thức từ 4 cuốn sách ERP — áp dụng khi viết tài liệu BA

Mỗi ý kết thúc bằng tham chiếu chương trong skill sách tương ứng. Sách xuất bản 2000–2017: đối chiếu luật và thực tiễn hiện hành trước khi áp dụng.

| Skill sách | Sách | Mạnh về |
|---|---|---|
| `parthasarathy-erp-fundamentals` | S. Parthasarathy (2007), Enterprise Resource Planning | Khái niệm ERP, MRP/MRP II, module, chọn phần mềm, triển khai, UML |
| `oleary-erp-systems-lifecycle` | D. O'Leary (2000), ERP Systems | Vòng đời ERP, best practice vs tùy biến, rủi ro, sau go-live |
| `wallace-erp-implementation` | T. Wallace & M. Kremzar (2001), ERP: Making It Happen | Proven Path, S&OP, MPS/MRP, toàn vẹn dữ liệu, định nghĩa quy trình |
| `elbardan-erp-governance-audit` | H. Elbardan & A. Kholeif (2017) | Kiểm soát nội bộ, quản trị, kiểm toán nội bộ trong ERP |

## parthasarathy-erp-fundamentals

Kiến thức rút ra để BA thiết kế chức năng ERP-standard và viết tài liệu đủ chi tiết để code. Mỗi insight kết thúc bằng tham chiếu chương trong skill `parthasarathy-erp-fundamentals`.

### erp-concepts (khái niệm & phạm vi ERP)
- Khi viết tài liệu ERP, luôn mô tả tính tích hợp (một giao dịch tự động cập nhật mọi nghiệp vụ liên quan) như đặc trưng nhận diện, vì đó là điểm phân biệt ERP với một tập phần mềm rời rạc (parthasarathy-erp-fundamentals ch01).
- Khi gán phạm vi yêu cầu, cần phân biệt rõ back-office (ERP) và front-office (CRM) để không nhét nhầm chức năng, tránh tài liệu thừa/thiếu phạm vi (parthasarathy-erp-fundamentals ch01).
- Khi đặc tả chức năng dự báo/tối ưu, cần ghi rõ nó thuộc module SCM chứ không phải ERP lõi, vì ERP lõi chỉ sinh giao dịch (parthasarathy-erp-fundamentals ch07).

### planning-mrp (hoạch định vật tư/sản xuất)
- Khi đặc tả hoạch định vật tư, cần theo chuẩn MPS → BOM explosion → purchase/production order và gắn lead-time + lot-size cho từng item, vì đây là luồng hoạch định chuẩn ERP (parthasarathy-erp-fundamentals ch02).
- Khi thiết kế chức năng hoạch định, cần phân biệt independent demand (thành phẩm, dự báo) với dependent demand (linh kiện, tính từ BOM), vì mô tả nhầm cả hai cùng kiểu là lỗi nghiệp vụ (parthasarathy-erp-fundamentals ch02).

### modules (bao phủ chức năng theo module chuẩn)
- Khi kiểm tra độ bao phủ, cần dùng danh mục chức năng con của 4 module (Finance 5 phân hệ; HR Managerial+Operative; MM 7 chức năng; SD 6 key element) làm checklist, vì thiếu mục nào nghĩa là tài liệu hụt chức năng so với chuẩn ERP (parthasarathy-erp-fundamentals ch03).
- Khi đặc tả CRM, cần tách rõ 3 thành phần Operational/Analytical/Collaborative và ánh xạ từng chức năng, vì nếu không sẽ bỏ sót (báo cáo phân tích thuộc Analytical, email/chat thuộc Collaborative) (parthasarathy-erp-fundamentals ch08).
- Khi làm ERP sản xuất, cần mượn danh mục chức năng chuẩn (Planning, Inventory, Engineering, Purchasing, Manufacturing, Finance, Quality, Order Processing...) làm khung kiểm tra đủ chức năng (parthasarathy-erp-fundamentals ch09).
- Khi xác định phạm vi một ERP đầu ngành, cần dùng cấu trúc 4 vùng của mySAP ERP (Financials/HCM/Operations/Corporate Services) làm bản đồ để spec phủ đủ các vùng chức năng chuẩn (parthasarathy-erp-fundamentals ch10).

### process-design (thiết kế luồng & quy trình)
- Khi đặc tả chức năng bán hàng, cần vẽ luồng liên module SD → Shipping (MM) → Billing (Finance) kèm điểm bàn giao dữ liệu, vì đặc tả SD cô lập sẽ làm mất tính tích hợp chuẩn ERP (parthasarathy-erp-fundamentals ch03).
- Khi đặc tả nghiệp vụ logistics, cần mô tả rõ 3 dòng chảy (product/information/financial) và lưu ý dòng thông tin chảy ngược chiều dòng hàng, vì đó là cơ sở thiết kế luồng cập nhật trạng thái đơn hàng (parthasarathy-erp-fundamentals ch07).
- Khi đặc tả quyết định trong chuỗi cung ứng, cần phân loại theo cấp strategic/tactical/operational để xác định role nào ra quyết định và với tần suất nào (parthasarathy-erp-fundamentals ch07).
- Khi có khác biệt giữa quy trình hiện tại và gói, cần viết Gap Analysis thành artifact rõ (mỗi gap kèm phương án lấp: third-party / chương trình tùy biến / sửa source + quyết định giữ-bỏ), vì để mơ hồ ở chỗ "khác biệt quy trình" là nguồn tranh cãi (parthasarathy-erp-fundamentals ch05).
- Khi có yêu cầu customization, cần ghi lý do kèm 3 tham số (end-user req, technical req, vision lãnh đạo) và cảnh báo mặc định "customize cao = lợi ích thấp + bảo trì tốn", vì sửa base làm mất lợi ích ERP (parthasarathy-erp-fundamentals ch05).
- Khi đặc tả nghiệp vụ, cần tách bạch validation rules và processing rules để hỗ trợ điều phối động, vì rule tách bạch giúp tài liệu đủ rõ để code mà không cần BA giải thích thêm (parthasarathy-erp-fundamentals ch09).
- Khi đặc tả một chức năng ERP, cần kèm đủ bộ sơ đồ UML (Use Case, Activity + swimlanes, Class, Sequence), vì đó là mức "chi tiết để code ngay" (parthasarathy-erp-fundamentals ch12).

### controls-permissions (kiểm soát & phân quyền)
- Khi viết NFR, cần đặc tả audit trail, control procedure và cơ chế kiểm soát, vì ERP có thể không để lại chứng từ, sinh dữ liệu tự động và khiến lỗi lan rộng khó phát hiện (parthasarathy-erp-fundamentals ch05).
- Khi đặc tả tích hợp ERP↔CRM (Quote-to-Cash, Requisition-to-Pay), cần kèm phân quyền (user chỉ thấy dữ liệu được phép) như một business rule bảo mật (parthasarathy-erp-fundamentals ch08).
- Khi liệt kê vai trò của một chức năng, cần phân biệt business actor (bên ngoài) và business worker/role (bên trong) để nêu đủ role nào có chức năng và role nào chỉ thao tác một phần (parthasarathy-erp-fundamentals ch12).

### requirements-elicitation (thu thập & đối chiếu yêu cầu)
- Khi bắt đầu dự án, cần dựng requirements profile sớm (bảng hỏi + phỏng vấn) và coi nó là nguồn chuẩn để đối chiếu mọi tiêu chí demo và so sánh sản phẩm — đúng tinh thần "đối chiếu với yêu cầu ban đầu" (parthasarathy-erp-fundamentals ch04).
- Khi chuẩn bị demo/nghiệm thu, cần liệt kê 50–100 chức năng bắt buộc phải trình diễn để biến yêu cầu thành tiêu chí kiểm thử rõ ràng, thay vì để vendor "diễn" tránh né chức năng khó (parthasarathy-erp-fundamentals ch04).
- Khi nghiệm thu yêu cầu CRM, cần dùng khung 3 góc nhìn Business/Technology/Customer làm checklist: mỗi yêu cầu phải trả lời được nó phục vụ góc nhìn nào (parthasarathy-erp-fundamentals ch08).
- Khi lập tài liệu chọn vendor, cần xây ma trận vendor × tiêu chí (ngành dọc, nền tảng, chiều sâu chức năng, mức tùy biến, lộ trình nâng cấp, địa phương hóa ngôn ngữ/tiền tệ/thuế) và ưu tiên "least customization" (parthasarathy-erp-fundamentals ch10).
- Khi phân tích nghiệp vụ, cần vẽ business model (UML) trước để elicit yêu cầu tốt hơn và phát hiện cơ hội reengineering, tránh chỉ tự động hóa quy trình cũ (parthasarathy-erp-fundamentals ch12).

### master-data (dữ liệu danh mục)
- Khi đặc tả module SD, cần đưa Master Data Management (customer, order, supplier details) vào như một key element bắt buộc, không được bỏ sót phần master data trong spec (parthasarathy-erp-fundamentals ch03).

### reports (báo cáo)
- Khi đặc tả báo cáo tài chính, cần nêu rõ nguồn dữ liệu và chiều phân tích (trial balance, lãi/lỗ theo phòng ban và sản phẩm, ratio analysis, báo cáo đa tiền tệ), vì Finance module nhấn mạnh báo cáo phục vụ ra quyết định (parthasarathy-erp-fundamentals ch03).
- Khi đặc tả báo cáo CRM, cần đưa phân quyền báo cáo và tính toàn vẹn/bảo mật dữ liệu khách hàng thành tham số hệ thống rõ ràng, không để ngầm định (parthasarathy-erp-fundamentals ch08).

### nfr (yêu cầu phi chức năng & nền tảng)
- Khi viết NFR, cần ghi rõ ràng buộc nền tảng (OS máy chủ hỗ trợ, single/multi-user, khả năng mở rộng cho CSDL giao dịch lớn) và TCO, thay vì để mơ hồ hoặc chỉ tối ưu giá mua (parthasarathy-erp-fundamentals ch06).

### implementation-lifecycle (vòng đời triển khai & nghiệm thu)
- Khi lập tài liệu triển khai, cần dùng vòng đời 11 bước (Project Planning → ... → Gap Analysis → Reengineering → Customization → ... → Maintenance) làm mục lục, mỗi bước có đầu ra và checklist nghiệm thu riêng (parthasarathy-erp-fundamentals ch05).
- Khi viết phần giả định/ràng buộc, cần nêu Critical Success Factors và mức cam kết của lãnh đạo, vì thiếu cam kết lãnh đạo và mục tiêu mơ hồ là rủi ro thất bại hàng đầu (parthasarathy-erp-fundamentals ch05).
- Khi spec có yêu cầu đổi/nâng cấp nền tảng, cần mô tả nó như một dự án sáu pha kèm mục Change Management, không coi là thay đổi cấu hình đơn giản (parthasarathy-erp-fundamentals ch06).
- Khi tư vấn phạm vi triển khai, cần khuyến nghị module-wise nếu chỉ thay một phần và nêu rõ đánh đổi (giảm chi phí/rủi ro/kháng cự nhưng chỉ đạt lợi ích tích hợp từng phần) (parthasarathy-erp-fundamentals ch05).
- Khi định nghĩa tiêu chí nghiệm thu, cần yêu cầu khách lập bộ KPI đo trước/sau (ví dụ >10 KPI về tồn kho, giao đúng hạn, hiệu suất nhà cung cấp), thay vì mô tả lợi ích chung chung (parthasarathy-erp-fundamentals ch11).

### data-migration-integrity (chuyển đổi dữ liệu & quản lý thay đổi)
- Khi lập spec triển khai, cần thêm mục Change Management và kế hoạch đào tạo, đồng thời dự trù khối lượng chuyển đổi dữ liệu BOM lớn, vì các case thất bại đều do thiếu quản lý thay đổi/đào tạo và đánh giá thấp mức thay đổi quy trình (parthasarathy-erp-fundamentals ch11).

## oleary-erp-systems-lifecycle

Kiến thức rút ra để BA thiết kế chức năng ERP-standard và viết tài liệu đủ chi tiết để code. Mỗi insight kết thúc bằng tham chiếu chương trong skill `oleary-erp-systems-lifecycle`.

### erp-concepts (khái niệm & giá trị ERP)
- Khi biện minh một yêu cầu/chức năng, cần gắn nó với một trong tám cơ chế tạo giá trị ERP (tích hợp, nhập một lần, chuẩn hóa, xóa bất đối xứng thông tin, real-time, truy cập đồng thời, cộng tác nội bộ, cộng tác liên tổ chức), vì chức năng không hiện thực hóa cơ chế nào là dấu hiệu "thừa chức năng"/"lệch yêu cầu" (oleary-erp-systems-lifecycle ch01).
- Khi tài liệu một chức năng, cần nêu tác động lên tích hợp liên module/liên phòng ban thay vì mô tả cô lập theo silo, vì giá trị ERP nằm ở tích hợp chứ không ở số lượng tính năng (oleary-erp-systems-lifecycle ch01).
- Khi gắn độ chi tiết cho tài liệu, cần định vị nó trong vòng đời ERP (quyết định → chọn → thiết kế → triển khai → sau go-live), vì giai đoạn Designing mới đòi mức chi tiết "đủ để code" (oleary-erp-systems-lifecycle ch01).

### requirements-elicitation (thu thập & đối chiếu yêu cầu)
- Khi khảo sát yêu cầu, cần dựng mô hình "as is" và "to be" rồi lấy khoảng cách giữa chúng để quyết đổi phần mềm hay đổi quy trình, vì đây là căn cứ chống lệch yêu cầu ngay từ đầu (oleary-erp-systems-lifecycle ch02).
- Khi lập business case, cần phân loại rationale (technology/business process/strategic/competitive); nếu dự án chỉ dựa Y2K hoặc "đối thủ có" thì bổ sung rationale process/strategic và chuyển thành mục tiêu đo được, vì chỉ hai loại sau cho đặc tả thiết kế và benchmark nghiệm thu (oleary-erp-systems-lifecycle ch07).
- Khi viết tài liệu yêu cầu/RFP, cần gắn nhãn mức ưu tiên (bắt buộc/tùy chọn hoặc rank 1-3) và chú thích độ mịn (granularity) cho từng yêu cầu, vì nếu không một trường dữ liệu sẽ bị đếm ngang một quy trình khi so khớp vendor (oleary-erp-systems-lifecycle ch08).
- Khi đánh giá vendor, cần dùng demo scripted hai pha và ở pha chặt bắt vendor dùng chính dữ liệu/nghiệp vụ thật của khách, rồi ghi gap thành danh sách kèm ước tính chi phí, vì demo cố định dễ che giấu chức năng yếu (oleary-erp-systems-lifecycle ch08).
- Khi ngành có ràng buộc pháp lý, cần đưa các MAPs bắt buộc theo quy định (vd biểu mẫu/báo cáo hợp đồng chính phủ) thành yêu cầu cứng không thương lượng (bài học Litton) (oleary-erp-systems-lifecycle ch10).

### process-design (thiết kế luồng & quy trình)
- Khi đặc tả bất kỳ chức năng ERP nào, cần cấu trúc theo khung MAPs — Models (mô hình dữ liệu/tổ chức), Artifacts (chứng từ, danh mục), Processes (luồng liên chức năng) — vì đó là cách mô tả map được sang gói ERP thực tế (oleary-erp-systems-lifecycle ch03).
- Khi thiết kế theo một model, cần ghi tường minh giả định của model (vd R/3 buộc mỗi đơn vị phải là cost center hoặc profit center) như một ràng buộc, vì làm trái giả định gây xung đột khi code (oleary-erp-systems-lifecycle ch03).
- Khi mở đầu tài liệu quy trình, cần ghi rõ dự án nghiêng technology enabled (chọn trong danh mục best practices, có bounds) hay clean slate (thiết kế tự do), vì điều này quyết định mức tự do thiết kế và chống "thừa chức năng" ngoài khả năng gói (oleary-erp-systems-lifecycle ch06).
- Khi viết tài liệu dự án, cần tách bạch phần "tái cấu trúc quy trình" và phần "triển khai công nghệ" để nghiệm thu rõ ràng, vì gộp hai phần khiến không tách được nguyên nhân khi dự án bị chê quá đắt/quá lâu (oleary-erp-systems-lifecycle ch06).
- Khi quyết đổi quy trình hay đổi phần mềm, cần đánh dấu rõ quy trình nào "tạo giá trị, khác biệt" (giữ/tùy biến) và quy trình nào "generic" (theo chuẩn phần mềm, small-r), vì chỉ quy trình khác biệt mới đáng chi phí sửa phần mềm (oleary-erp-systems-lifecycle ch09).
- Khi một yêu cầu đòi sửa phần mềm, cần ghi kèm cảnh báo chi phí ba lần (lúc sửa/nâng cấp/hỗ trợ) và tác động tới roll-out, đồng thời ghi các compromise cấu hình (profit/cost center thay "phòng ban") thành quyết định thiết kế có chủ đích (oleary-erp-systems-lifecycle ch09).
- Khi viết tài liệu hỗ trợ, cần dùng dạng script-based dẫn user từng bước qua trọn một giao dịch, vì đó cũng là nguồn tốt để viết user story có ngữ cảnh nghiệp vụ thay vì chỉ liệt kê thao tác (oleary-erp-systems-lifecycle ch13).

### master-data (danh mục & chuẩn hóa dữ liệu)
- Khi thiết kế master data, cần chuẩn hóa theo bảng + khóa tham chiếu để mỗi thực thể (khách hàng, vật tư, nhà cung cấp) chỉ định nghĩa một lần (enter once), thay vì liệt kê trường phẳng lặp lại (oleary-erp-systems-lifecycle ch02).
- Khi đặc tả một danh mục dùng chung (vendor, customer, product, chart of accounts, numbering scheme), cần coi nó là quyết định chuẩn hóa cấp doanh nghiệp: ghi nguồn chuẩn được chọn, đơn vị nào chịu chi phí thay đổi, và tỷ lệ tham số local tự cấu hình vs chốt cứng toàn cục (mô hình Microsoft ~3.000/30 bảng) (oleary-erp-systems-lifecycle ch10).
- Khi chốt độ dài mã/danh mục, cần cảnh báo đánh đổi: mã dài hơn mức cần gây nhập liệu chậm và tăng lỗi, và common view có thể không tối ưu cho từng division (oleary-erp-systems-lifecycle ch10).

### modules (đặt tên & bao phủ theo module chuẩn)
- Khi đặt tên chức năng, cần dùng thuật ngữ module chuẩn (FI, CO, GL, AR, AP, MM, PP, SOP, MRP, CRP, SD, HR, QM, PM, PS), vì tên chuẩn giúp tài liệu nhất quán và map được sang gói ERP thực tế (oleary-erp-systems-lifecycle ch03).

### planning-mrp (hoạch định sản xuất/vật tư)
- Khi đặc tả nghiệp vụ sản xuất, cần nhận diện khối hoạch định chuẩn trong module PP gồm SOP (sales & operations planning), MRP (materials requirements planning) và CRP (capacity requirements planning) và dùng đúng tên (oleary-erp-systems-lifecycle ch03).
- Khi một yêu cầu phụ thuộc tính năng cross-module như available-to-promise (ATP), cần ghi rõ ràng buộc tính năng chỉ có khi các module liên quan cùng go-live, vì điều này ảnh hưởng tới lựa chọn big bang/phased (oleary-erp-systems-lifecycle ch11).

### controls-permissions (kiểm soát đầu vào & phân quyền)
- Khi đặc tả màn hình nhập liệu, cần ghi rõ data input controls (ràng buộc, kiểm tra, bắt buộc xác nhận), vì khi "nhập một lần" hệ không còn dự phòng và dữ liệu sai sẽ lan toàn hệ, có thể không bao giờ bị phát hiện (oleary-erp-systems-lifecycle ch04).
- Khi đặc tả luồng nhập liệu, cần ghi rõ AI nhập (vai trò ở điểm phát sinh, không mặc định là kế toán), nhập Ở ĐÂU và BAO NHIÊU LẦN, vì đây chính là thông tin role/quyền mà tài liệu ERP cần có (oleary-erp-systems-lifecycle ch04).
- Khi rà soát hậu triển khai, cần ghi rõ các implementation compromise về security (đừng để lâu dài ở mức group thay vì individual) và quy tắc ai được xem báo cáo nào, để chúng không âm thầm biến thành engagement compromise (oleary-erp-systems-lifecycle ch12).
- Khi phân định thẩm quyền thiết kế, cần ghi rõ process owner/management quyết các lựa chọn thiết kế quy trình chứ không phải project team, vì để project team tự quyết dễ làm quy trình lệch kỳ vọng và không khớp quy trình khác (oleary-erp-systems-lifecycle ch15).

### nfr (yêu cầu phi chức năng)
- Khi viết NFR nền tảng, cần ghi kiến trúc client server/ba lớp, DBMS được hỗ trợ, firewall/encryption và ưu tiên switch setting/tham số thay vì tùy biến mã, vì các ràng buộc này cố định sau go-live và tùy biến cản nâng cấp phiên bản (oleary-erp-systems-lifecycle ch02).
- Khi đặc tả nhập liệu khối lượng lớn, cần ước tính số màn hình và thời gian nhập mỗi giao dịch; nếu tỉ lệ màn hình so hệ cũ cao (Hydro Agri 6:1) thì đề xuất gộp màn hình/lớp UI trung gian và ghi thời gian nhập như tiêu chí nghiệm thu (oleary-erp-systems-lifecycle ch04).
- Khi thiết kế đầu ra, cần thêm NFR về output capacity planning (ước tính số người truy vấn, tần suất), vì nhiều ERP xử lý query như transaction và truy vấn nặng là "đám cháy công nghệ số một" sau go-live (oleary-erp-systems-lifecycle ch05).
- Khi viết spec lựa chọn hệ thống, cần có một mục non-functional riêng (cost, installation time, flexibility, UI, upgradability, computing environment, implementation personnel, maintenance), vì requirements/gap analysis chỉ tập trung chức năng và bỏ sót chúng (oleary-erp-systems-lifecycle ch08).
- Khi mở truy cập ERP ra ngoài hoặc tích hợp e-commerce, cần thêm NFR về security (bảo vệ hệ/dữ liệu/truyền tin), về tải query ảnh hưởng hiệu năng nội bộ, về mức dữ liệu được phép lộ, và đặc tả volume requirement cụ thể cùng network/computing capacity khớp (FoxMeyer thất bại vì 10.000 so với 420.000 invoice line item/đêm) (oleary-erp-systems-lifecycle ch15).

### reports (báo cáo & đầu ra)
- Khi đặc tả một module/chức năng, cần liệt kê báo cáo chuẩn đi kèm và các báo cáo ad hoc dự kiến, và ưu tiên view/data warehouse hơn customized report cứng, vì report cứng tốn kém, ngắn hạn và cản nâng cấp (oleary-erp-systems-lifecycle ch05).
- Khi thiết kế màn hình chính, cần tổ chức theo vai trò công việc (role-specific desktop/portal) gom báo cáo, module con và tác vụ cá nhân mà vai trò cần, và phân tầng expert (ERP trực tiếp) vs casual (intranet/portal) gắn với ma trận phân quyền (oleary-erp-systems-lifecycle ch05).
- Khi đặc tả vận hành báo cáo, cần ghi quy trình duyệt request báo cáo mới qua process owner để chống nghẽn hệ thống, và quy tắc phân quyền output (ai được xem báo cáo nào) (oleary-erp-systems-lifecycle ch12).

### implementation-lifecycle (chiến lược triển khai & nghiệm thu)
- Khi viết tài liệu triển khai, cần ghi rõ chiến lược (big bang/phased/waved/parallel) kèm căn cứ theo size, complexity, hierarchy/control, số module và module fit, thay vì mặc định một cách (oleary-erp-systems-lifecycle ch11).
- Khi chọn phased, cần đặc tả rõ các temporary interface tới legacy ở mỗi pha và kế hoạch gỡ bỏ, vì chúng là hạng mục công việc và rủi ro thực chứ không phải chi tiết ngầm (oleary-erp-systems-lifecycle ch11).
- Khi lập kế hoạch test, cần có hạng mục test interface giữa các module riêng biệt (SVT/conference room pilot) với khối lượng giao dịch mô phỏng tải thật và test phần cứng, vì các mảnh chạy riêng được vẫn có thể không chạy cùng nhau (oleary-erp-systems-lifecycle ch11).
- Khi định nghĩa benefit, cần biến mỗi con số mong muốn thành metric có baseline + owner + quy được về chính ERP (không chỉ ghi goal), và đưa Deloitte Post-Implementation Checklist dạng Yes/No vào bộ acceptance criteria hậu triển khai (oleary-erp-systems-lifecycle ch12).
- Khi lập kế hoạch đào tạo, cần làm riêng cho từng module (timing sát go-live, số giờ, hình thức, super users, tiêu chí job-based), dự trù ngân sách training ≥10% tổng dự án, và yêu cầu đào tạo implementor đúng phiên bản trước khi thiết kế quy trình để tránh customization oan (bài học Dow Corning) (oleary-erp-systems-lifecycle ch13).

### data-migration-integrity (chuyển đổi & toàn vẹn dữ liệu)
- Khi đặc tả data conversion, cần gồm bước reconcile (số tồn kho/sản phẩm/vendor có khớp không, vì sao không) và mapping từng trường giữa hai CSDL, vì lỗi conversion ngụy trang thành triệu chứng kinh doanh (tồn kho phình, thiếu linh kiện) và chỉ lộ dần theo thời gian (oleary-erp-systems-lifecycle ch12).

### processes-ecommerce (business rule tích hợp & thương mại điện tử)
- Khi đặc tả đặt hàng qua web/EDI, cần thiết kế configuration engine như một business rule bắt lỗi đầu vào (sai part number, cấu hình không hợp lệ) với quy tắc "không cho đặt nếu còn lỗi", vì chính xác đầu vào loại bỏ 25-33% lỗi và chi phí xử lý (oleary-erp-systems-lifecycle ch14).
- Khi đặc tả tích hợp ERP-to-ERP (VMI, BTO), cần đưa điều kiện tiên quyết "chung một phần MAPs cho các giao dịch liên quan" vào spec, nếu không phải đặc tả thêm một lớp tích hợp (oleary-erp-systems-lifecycle ch14).
- Khi chọn kênh trao đổi với đối tác, cần chọn EDI khi khối lượng giao dịch lớn/đối tác lớn và WFT khi originator ít giao dịch, kèm cảnh báo WFT gây nhập liệu gấp đôi nếu originator nhiều giao dịch (oleary-erp-systems-lifecycle ch14).
- Khi đặc tả merge-in-transit, cần business rule một purchase order và một invoice dù hàng xuất từ nhiều nơi, và ERP phải hạch toán bán hàng không bao giờ "nhập kho" (oleary-erp-systems-lifecycle ch14).

### risk (quản trị rủi ro dự án ERP)
- Khi lập risk register, cần tổ chức theo Risk Matrix (giai đoạn vòng đời × technical/business/organizational) và mỗi rủi ro ghi mặt success nếu xử lý tốt / mặt failure nếu hỏng, ưu tiên organizational > business > technical vì rủi ro con người/cơ cấu/văn hóa cao nhất còn technical dễ sửa nhất (oleary-erp-systems-lifecycle ch15).
- Khi viết phần tổ chức của tài liệu, cần đưa yêu cầu top-management & domain buy-in, culture-change effort và kế hoạch giữ nhân sự "hot skills" sau triển khai, vì thiếu chúng là nhóm failure factor hàng đầu (oleary-erp-systems-lifecycle ch15).

## wallace-erp-implementation

Tri thức rút từ skill `wallace-erp-implementation` để giúp BA ERP thiết kế chức năng chuẩn ERP và viết spec code được. Đã gộp trùng lặp giữa 3 phần sách; nhóm theo `applies_to`. Mỗi gạch đầu dòng kết thúc bằng tham chiếu chương trong skill.

### erp-concepts
- Khi mở đầu tài liệu, tách bạch **ERP (quy trình + con người)** với **ES (phần mềm)**, vì phần lớn "ERP failure" thực chất chỉ là cài phần mềm mà không đổi quy trình — spec phải mô tả quy trình/nghiệp vụ, không chỉ cấu hình phần mềm. (wallace-erp-implementation ch01)
- Khi đánh giá "độ chuẩn ERP" của một yêu cầu, chiếu vào thang **Class A** (một bộ số thống nhất, tích hợp chéo chức năng) thay vì chỉ cải tiến cục bộ. (wallace-erp-implementation ch01)
- Khi thiết kế tài chính, cho financial planning dùng chung dữ liệu vận hành (**one set of numbers**, chỉ khác đơn vị đo), tránh yêu cầu hai bộ sổ — ERP chuyển mọi kế hoạch đơn vị thành dollars bằng cách thêm giá bán và chi phí. (wallace-erp-implementation ch17)
- Khi thiết kế phân phối, phân biệt **warehouse** (kho chứa) với **distribution center** (điểm cross-dock) và tính tồn kho trên toàn chuỗi (của mình + khách + nhà cung cấp), không coi warehouse đầy hàng là mặc định. (wallace-erp-implementation ch16)

### process-design
- Khi viết mỗi chức năng, mô tả **business function** (nghiệp vụ cần làm + luồng) trước, rồi mới ánh xạ sang module/switch phần mềm — tránh spec kiểu "triển khai module X" vì dễ sai trình tự và lệch trọng tâm. (wallace-erp-implementation ch03)
- Khi đặc tả một chức năng, truyền cả **what/why** (lý do/mục tiêu kinh doanh) chứ không chỉ **how** (thao tác), vì không có phần "tại sao" thì người dùng không sở hữu quy trình. (wallace-erp-implementation ch07)
- Khi viết spec, tách nội dung theo **need-to-know**: theo role (ai cần biết sâu phần nào) và theo company characteristics (make-to-stock / make-to-order / custom), để tránh tài liệu thừa hoặc thiếu so với bối cảnh khách hàng. (wallace-erp-implementation ch07)
- Khi đặc tả một process definition statement, bắt buộc trả lời: **customer meeting point** (DTO/MTO/FTO/MTS), cách promising đơn (**available-to-promise**), kênh trao đổi với đối tác (EDI/Internet/fax), và công cụ liên quan (DRP/CRP/supplier scheduling) — bộ câu hỏi khung chống thiếu chức năng. (wallace-erp-implementation ch09)
- Khi thiết kế kịch bản UAT, dùng kiểu **"play Murphy / Make It Fail"**: mỗi chức năng kèm các tình huống lỗi (scrap, supplier trễ, ECN khẩn, máy hỏng) để kiểm cả hệ thống lẫn luồng phản hồi — tránh tài liệu chỉ mô tả happy path. (wallace-erp-implementation ch11)
- Khi đặc tả **Customer Order Entry & Promising**, mô tả rõ nguồn dữ liệu (tồn kho/backlog/capacity/lead time) và logic net với forecast để sinh promise date (ATP) — đây là chức năng cốt lõi rất dễ bị đặc tả sơ sài. (wallace-erp-implementation ch17)
- Khi làm bài toán common-parts giữa slice và non-slice, ghi một business rule rõ ràng về quy ước đánh dấu item thuộc slice (ví dụ hậu tố mã "S") kèm điều chỉnh BOM tương ứng, vì nó ảnh hưởng tới cấu trúc dữ liệu và mã hóa item. (wallace-erp-implementation ch14)

### controls-permissions
- Khi đặc tả mỗi chức năng, ghi rõ **role vận hành thực tế** (ai dùng chính, ai thao tác một phần, ai duy trì dữ liệu), vì nguyên tắc **IMPLEMENTERS = USERS** gắn trách nhiệm triển khai với người vận hành. (wallace-erp-implementation ch02)
- Khi đặc tả chức năng, kèm mục **policy** nêu roles (ai được đổi gì ở time zone nào), parameters hệ thống (order quantity, safety stock/time, scrap/shrinkage, time fences, hedges), feedback flows và performance measurements — đúng cấu phần "phân quyền/tham số hệ thống" của tài liệu ERP chuẩn. (wallace-erp-implementation ch09)
- Khi đặc tả forecasting, viết **single-number forecast** như một business rule: hệ thống chỉ cho phép một forecast "official" được duyệt, chặn tình trạng mỗi phòng (Sales/Marketing/Finance) một con số. (wallace-erp-implementation ch08)
- Khi mô tả feedback, viết **"silence is approval"** như business rule bắt buộc: mỗi role (plant, purchasing, planner, customer service) phải sinh anticipated delay report khi biết sẽ trễ, với role gửi/nhận và chuỗi leo thang rõ ràng. (wallace-erp-implementation ch11)
- Khi thêm mục change-control vào tài liệu, đặt gate "thay đổi này có cần để điều hành kinh doanh / để ERP chạy đúng không, và có bắt buộc dùng máy tính không?" làm cơ chế chống tài liệu thừa chức năng. (wallace-erp-implementation ch04)

### master-data
- Khi đặc tả chức năng hoạch định, dùng **4 câu hỏi universal manufacturing equation** làm bộ kiểm master data: có master schedule? có BOM? có inventory records? có logic sinh nhu cầu mua/làm? Thiếu một mục là chức năng chưa đủ dữ liệu để code. (wallace-erp-implementation ch01)
- Khi đặc tả master data (item master, BOM, routing, work center), phân loại rõ field nào **unforgiving** (verify kỹ) vs **forgiving** (chỉ cần hợp lý), tránh yêu cầu độ chính xác quá mức cho dữ liệu forgiving. (wallace-erp-implementation ch10)
- Khi liệt kê phụ thuộc dữ liệu, ghi rõ: **MRP** cần bill of material + dữ liệu tồn kho; **CRP** cần routing + work center/thời gian nguyên công — thiếu các thực thể này thì chức năng không code được. (wallace-erp-implementation ch17)
- Khi làm DRP, mô hình hóa **bill of distribution** (sản phẩm × DC) như một thực thể dữ liệu riêng, với field cho little DRP (forecast, lead time bổ sung, safety stock, on-hand, in-transit) và big DRP (trọng lượng, kích thước, số sản phẩm/pallet, nhân lực DC, thời gian nhận/pick-pack-ship). (wallace-erp-implementation ch12)
- Khi đặt business rule nền về dữ liệu, yêu cầu **BOM hợp nhất toàn công ty** (một nguồn sự thật) và cấm bật planning/scheduling nếu dữ liệu dưới ngưỡng. (wallace-erp-implementation ch10)

### planning-mrp
- Khi sắp xếp chức năng, tuân đúng phụ thuộc hoạch định **S&OP → master schedule → MRP → supplier/plant scheduling**; đảo thứ tự sẽ làm tài liệu mâu thuẫn và chức năng downstream vô hiệu (vd supplier scheduling cần due date hợp lệ từ MRP). (wallace-erp-implementation ch03)
- Khi đặc tả module planning, mô hình hóa tách bạch hai tầng: **volume** (S&OP — Sales Plan/Operations Plan theo product family) và **mix** (master schedule theo từng sản phẩm/đơn); trộn lẫn hai tầng là nguồn gây conflict trong tài liệu. (wallace-erp-implementation ch08)
- Khi đặc tả quan hệ các cấp hoạch định, viết ràng buộc "**tổng master schedule phải reconcile với S&OP cùng kỳ**" như một business rule/kiểm tra toàn vẹn, không để ngầm. (wallace-erp-implementation ch17)
- Khi mô hình hóa feedback, đặc tả luồng theo **exception** (anticipated delay) với chuỗi leo thang role cụ thể (planner → master scheduler → sales → customer) và điều kiện kích hoạt (chỉ khi không thực thi được) — đây là nơi nhiều spec bị thiếu. (wallace-erp-implementation ch17)

### modules
- Khi đặc tả, tách **tham số cấu hình (switch)** khỏi **yêu cầu enhancement/code** và phân loại minor/major; đây là điều giúp tài liệu "code được ngay" và là nền cho quy trình change-control. (wallace-erp-implementation ch04)
- Khi đề xuất **bolt-on**, nêu rõ loại (resource-planning enabler / front-back-end / supply-chain APS) và đánh đổi mất tích hợp + tăng bảo trì; ưu tiên giữ "pockets of excellence" hiện có thay vì thay thế vô cớ. (wallace-erp-implementation ch04)
- Khi lập phạm vi một sản phẩm ERP đầy đủ, phủ cả phía chuỗi cung ứng — supplier scheduling, DRP, VMI, collaborative forecasting — mỗi cái là một luồng vượt ranh giới công ty cần đặc tả quyền xem tồn kho/nhu cầu của đối tác và ai sở hữu tồn kho ở thời điểm nào. (wallace-erp-implementation ch12)
- Khi thiết kế transaction system, theo "less is more": chỉ đặc tả các transaction type thực sự cần (in/out × planned/unplanned, transfer, adjustment, backflush) và xử lý trong 24h — tránh spec thừa chức năng từ danh mục mặc định của phần mềm. (wallace-erp-implementation ch10)

### processes
- Khi đặc tả module Mua hàng, phân biệt rõ **purchase requisition/PO truyền thống** với **supplier scheduling** (lịch giao theo MRP, hợp đồng dài hạn) — supplier scheduling nhằm *loại bỏ* requisition và hard-copy PO, không tự động hóa chúng; đừng nhầm module "purchasing" của ES là supplier scheduling. (wallace-erp-implementation ch12)
- Khi lập thứ tự ưu tiên tài liệu, làm sớm **S&OP** và **data integrity** vì là early wins ít tốn nguồn lực và là nền cho các chức năng xử lý mix phía sau. (wallace-erp-implementation ch03)
- Khi xác định bộ chức năng lập lịch, nhận diện sớm khách là **job shop** hay **flow shop** (hoặc hỗn hợp theo khu): job shop cần routing nhiều công đoạn + back scheduling + dispatch list + CRP + input-output; flow shop dùng lịch trình tự đơn giản và có thể không cần routing chính thức. (wallace-erp-implementation ch18)

### requirements-elicitation
- Khi gặp chức năng đặc thù ngành không có sẵn trong package (lot traceability của dược, shelf life FMCG, contract accounting quốc phòng), bắt buộc trả lời **bộ 4 câu hỏi tailoring** (còn làm sau ERP? thiết yếu? trong hay ngoài ERP? nếu ngoài xử lý sao) và ghi vào tài liệu thay vì bỏ qua. (wallace-erp-implementation ch03)
- Khi verify tài liệu, áp dụng **bulletproofing**: chủ động hỏi "còn chỗ nào mơ hồ / bị bắn thủng không?" và không đóng checklist khi còn câu hỏi chưa có đáp án hợp lệ — khớp đúng các câu BA hay hỏi agent. (wallace-erp-implementation ch07)
- Khi lập phạm vi, dùng **Vision Statement** 1 trang, đo lường được, làm neo chống lệch phạm vi: mọi yêu cầu mới phải đối chiếu lại vision + performance goals để phát hiện chức năng thừa, thiếu hoặc mâu thuẫn. (wallace-erp-implementation ch05)
- Khi viết phần vision/benefit, dùng kỹ thuật **factoid** (đổi %/$ thành con số-hình ảnh cụ thể gắn với nỗi đau stakeholder) để tài liệu "bán" được giá trị, đồng thời tránh bẫy "either/or" khi stakeholder ép đánh đổi (service vs inventory, EDI vs Internet). (wallace-erp-implementation ch16)

### nfr
- Khi viết mục tiêu phi chức năng, mỗi mục tiêu hiệu năng phải là chỉ tiêu định lượng, vận hành (ví dụ "giao đủ 99% đơn trong 24 giờ") và truy ngược được về một lợi ích kinh doanh cụ thể — tránh mục tiêu mơ hồ không nghiệm thu được. (wallace-erp-implementation ch06)
- Khi gắn mục tiêu cho chức năng, liên kết mỗi yêu cầu với một lợi ích đo lường được trong 11 nhóm lợi ích ERP (on-time shipment, giảm purchase cost, giảm tồn kho, giảm premium freight...). (wallace-erp-implementation ch05)
- Khi nêu ràng buộc NFR, ghi rõ timebox urgency (ví dụ 120 ngày cho Quick-Slice) và cấu hình **time fence + emergency zone** cho master schedule — vì chúng ảnh hưởng trực tiếp tới thiết kế chức năng và tới nghĩa của các đo lường vận hành. (wallace-erp-implementation ch15)

### data-migration-integrity
- Khi viết tài liệu data-migration, gắn **ngưỡng chấp nhận định lượng** cho từng đối tượng dữ liệu (tồn kho ≥95%; BOM/routings/open orders ≥98%), kèm định nghĩa "accuracy" (khớp những trường nào) và counting tolerance (0–5%) — biến thành acceptance criteria. (wallace-erp-implementation ch10)
- Khi đặc tả nền dữ liệu, nêu rõ mức chính xác yêu cầu và **cách duy trì** (cycle counting với control group, cấu trúc BOM modular, routing) cho inventory/BOM/routing — không coi độ chính xác dữ liệu là mặc nhiên. (wallace-erp-implementation ch10)
- Khi đặt mục tiêu dữ liệu, theo trình tự "đo trước, cải thiện sau": đo baseline trên mẫu → giới hạn truy cập kho → thiết lập cycle counting (ongoing) → song song giáo dục/đào tạo nhân sự kho. (wallace-erp-implementation ch19)

### implementation-lifecycle
- Khi tổ chức tài liệu/backlog, chia theo **Phase I (Basic ERP) / II (Supply Chain Integration) / III (Extensions)** và chỉ nhận "have-to's" vào Phase I để chống scope creep và giữ lịch ~9–12 tháng cho Basic ERP. (wallace-erp-implementation ch03)
- Khi viết acceptance, nhúng một **Implementers' Checklist** dạng Yes/No vào cuối mỗi tài liệu chức năng; quy tắc cho phép thêm mục nhưng cấm xoá mục để không làm yếu khả năng nghiệm thu. (wallace-erp-implementation ch05)
- Khi phân loại chi phí/nguồn lực và hạng mục dự án, dùng **ABC (People/Data/Computer)** và nhấn A-item (role, đào tạo) để tài liệu không thiên lệch về phần mềm. (wallace-erp-implementation ch05)
- Khi đặc tả cutover, nêu rõ chiến lược: **pilot** là mặc định cho planning/scheduling, **parallel** chỉ cho phân hệ kế toán; cảnh báo "inadvertent big bang" (không tắt hệ cũ khi logic tương ứng chưa sẵn ở hệ mới). (wallace-erp-implementation ch11)
- Khi định "definition of done" cho mỗi chức năng, thêm cổng phê duyệt (steering committee authorization + user sign-off) và ngưỡng dữ liệu còn đạt trước go-live — biến go-live gate thành checklist Yes/No. (wallace-erp-implementation ch11)
- Khi lập phạm vi cho khách hàng lớn hoặc đã có ES, cân nhắc đề xuất **Quick-Slice** (một product family, ~120 ngày): viết spec đầy đủ cho một slice, ghi rõ ranh giới "hai hệ thống" và vấn đề common-parts sẽ phát sinh. (wallace-erp-implementation ch14)
- Khi thiết kế quản trị vận hành như một phần của hệ thống, mô hình hóa thực thể **ERP operating committee** (chủ tịch luân phiên, lịch họp quý/6 tháng) và quy trình xử lý "no answer" (nguyên nhân → owner → due date) cùng re-certification Class A hằng năm. (wallace-erp-implementation ch15)

### reports
- Khi đặc tả phần Reports/KPIs, đưa bộ đo lường vận hành chuẩn làm thước đo nghiệm thu sau go-live: reschedule-in ≈ reschedule-out, MRP exception message ≤10% (job shop), late order release ≤5%, past-due load <1 tuần, capacity-to-plan ±5%, độ chính xác inventory/BOM/routing sát 100%. (wallace-erp-implementation ch15)
- Khi thiết kế metric cho planning, đặc tả "actual vs plan" cho cả demand (so với single-number forecast) và supply (so với production plan). (wallace-erp-implementation ch08)

## elbardan-erp-governance-audit

Tri thức rút từ skill `elbardan-erp-governance-audit` để giúp BA ERP thiết kế chức năng chuẩn ERP và viết spec code được. Đã gộp trùng lặp giữa 4 phần sách; nhóm theo `applies_to`. Mỗi gạch đầu dòng kết thúc bằng tham chiếu chương trong skill.

### erp-concepts
- Khi định nghĩa phạm vi dự án, nêu rõ module nào được tích hợp, vì ERP tối thiểu chỉ cần module tài chính–kế toán + một CSDL chung và mức tích hợp là một continuum (từ rời rạc đến tích hợp hoàn toàn). (elbardan-erp-governance-audit ch02)
- Khi đặc tả mỗi module, nêu rõ nguyên lý kiểm soát (control) và ba giả định nền standardisation/visibility/integration mà nó hiện thực, vì ERP không trung lập mà mang sẵn "logic kiểm soát". (elbardan-erp-governance-audit ch04)
- Khi khách ở nước đang phát triển, đánh dấu các "best practice" cài sẵn cần bản địa hóa, vì logic/thực hành mặc định bắt nguồn từ nước phát triển có thể không phù hợp bối cảnh. (elbardan-erp-governance-audit ch01)
- Khi làm hệ ngân hàng/tài chính, phân biệt rõ back-office (ERP: financial, inventory/purchasing, assets, controlling, HR) với front-office (core-banking) và đặc tả tích hợp GL + đối soát số liệu giữa hai hệ thống. (elbardan-erp-governance-audit ch08)
- Khi khảo sát vendor, hỏi rõ: có built-in control nào, tổ chức được bật/tắt kiểm soát nào hay vendor áp đặt, kiểm soát thiên phòng ngừa hay phát hiện, công cụ kiểm toán/giám sát rủi ro nào sẵn có. (elbardan-erp-governance-audit ch12)

### modules
- Khi đặc tả luồng dữ liệu liên module, áp nguyên tắc tích hợp = một CSDL duy nhất, nhập một nơi tự chảy sang nơi khác, giảm đối soát thủ công và làm hành động mỗi người hữu hình. (elbardan-erp-governance-audit ch06)
- Khi lập danh mục module tham chiếu, dùng các thực thể lặp lại trong các ca: warehousing, cash management, accounts receivable/payable, HR, inventory, assets, purchasing, general ledger, chart of accounts. (elbardan-erp-governance-audit ch10)

### controls-permissions
- Khi thiết kế phân quyền, liệt kê tường minh các cặp vai trò không được đồng nắm (vd nhập liệu + phê duyệt), vì ERP mở rộng phạm vi công việc dễ phá vỡ Segregation of Duties và tăng rủi ro gian lận. (elbardan-erp-governance-audit ch02)
- Khi mô tả kiểm soát cho mỗi chức năng, dùng 5 thành phần COSO (control environment, risk assessment, control activities, information, communication & monitoring) làm khung để cover đủ, tránh thiếu kiểm soát. (elbardan-erp-governance-audit ch02)
- Khi nghiệm thu thiết kế một chức năng, dùng bộ control assumptions (9/10/11 tùy vùng rủi ro) làm checklist "đã chuẩn ERP chưa", trả lời yes/no kèm cách hiện thực. (elbardan-erp-governance-audit ch10)
- Khi viết spec kiểm soát, phân loại mỗi control thành inherent/configurable/security/reporting, vì dev cần biết cái nào có sẵn, cái nào cấu hình, cái nào thuộc phân quyền, cái nào thuộc báo cáo. (elbardan-erp-governance-audit ch06)
- Khi đặc tả phân quyền, nêu cho mỗi role một authorisation profile (được xem/sửa/xóa bản ghi nào), bộ quy tắc SoD, và một report dò xung đột SoD chạy định kỳ — đủ chi tiết để code ngay. (elbardan-erp-governance-audit ch06)
- Khi thiết kế RBAC, đặc tả 2 lớp: function security (menu/chức năng được truy cập) và data security (phạm vi dữ liệu mỗi vai trò được xem/sửa), để nhân viên chỉ thấy thông tin liên quan công việc nhằm chống thông đồng. (elbardan-erp-governance-audit ch08)
- Khi đặc tả giao dịch tài chính/ngân hàng, thêm maker-checker (màn hình không đi tiếp đến khi có approval + validation) như một yêu cầu customisation có chủ đích, vì ERP mặc định có thể thiếu bước này. (elbardan-erp-governance-audit ch08)
- Khi làm chức năng rủi ro cao của ERP ngân hàng, nêu rõ access control + SoD + two-factor authentication, vì đây là bộ kiểm soát biến kiểm soát nội bộ từ detective thành preventive. (elbardan-erp-governance-audit ch09)
- Khi gán quyền, giám sát liên tục thay đổi quyền theo luân chuyển nhân sự và review định kỳ user profile ↔ access rights, levels of authority ↔ job description, vì đây là rủi ro truy cập cao nhất. (elbardan-erp-governance-audit ch09)
- Khi có mâu thuẫn giữa IT (bảo vệ dữ liệu) và kiểm toán (cần truy cập nhanh), cấp quyền truy cập dữ liệu chỉ-đọc có ghi log cho vai trò kiểm toán. (elbardan-erp-governance-audit ch03)
- Khi ưu tiên loại kiểm soát, chọn preventive (ngăn trước) hơn detective (phát hiện sau), vì tự động hóa của ERP cho dời việc từ "ký duyệt từng giao dịch" sang "giám sát kiểm soát đang chạy đúng". (elbardan-erp-governance-audit ch07)
- Khi thiết kế requirement cho kiểm soát liên tục, tách thành continuous risk assessment (theo dõi chỉ báo rủi ro) và continuous control assurance (so khớp giao dịch với bộ luật để bật ngoại lệ). (elbardan-erp-governance-audit ch12)
- Khi đặc tả an ninh dữ liệu, mô tả rõ cấp/thu hồi quyền khi nhân sự nghỉ hoặc chuyển bộ phận, và SoD cho cả tác vụ IT (ngăn người vận hành/lập lịch chạm tài liệu chương trình & CSDL). (elbardan-erp-governance-audit ch11)

### process-design
- Khi viết spec một chức năng, tách mục tiêu kiểm soát (giữ nguyên) khỏi cơ chế thực hiện (thay đổi theo hệ thống), để tài liệu không lệch khỏi yêu cầu nghiệp vụ gốc. (elbardan-erp-governance-audit ch01)
- Khi dữ liệu được chuyển sang bước sau với "chấp nhận ngầm định", chèn bước re-verification, vì ERP thường không có chỗ kiểm tra dọc đường. (elbardan-erp-governance-audit ch02)
- Khi thiết kế kiểm soát cho một chu trình, áp quy trình phân tích rủi ro 7 bước (nhận diện dải rủi ro → gắn ứng dụng → định lượng chi phí exposure → chọn kiểm soát cost-effective → phân bổ nguồn lực → ứng phó → tư vấn) để biến yêu cầu mơ hồ thành đầu ra rõ. (elbardan-erp-governance-audit ch02)
- Khi thiết kế kiểm soát vận hành, viết thành luật if/else code-able: chặn lệnh sản xuất khi tồn kho vật tư < định mức; chặn post vào kỳ kế toán đã khóa; chặn post hóa đơn sai mã khách; chặn đặt hàng nhà cung cấp từng giao lỗi. (elbardan-erp-governance-audit ch07)
- Khi tích hợp nghiệp vụ phi tài chính với kế toán, đặc tả single data entry point (dữ liệu nhập một lần tự sinh bút toán) và ghi rõ bước nào mặc nhiên chấp nhận dữ liệu bước trước (peer review nhúng trong luồng). (elbardan-erp-governance-audit ch07)
- Khi thiết kế một giao dịch trọng yếu, cho đi qua nhiều người (một người nhập, một người duyệt, một người xác nhận) để mỗi bút toán được soát 1–3 lần (multiple methods of control). (elbardan-erp-governance-audit ch07)
- Khi viết requirement quy trình, bắt quy trình "auditable" (để lại vết, gắn kiểm soát) trước khi cho "chạy", vì governance rules vẽ hướng dẫn còn ERP thực thi quy trình có tính tới các quy tắc đó. (elbardan-erp-governance-audit ch06)
- Khi quy trình khách lệch chuẩn ERP, ghi rõ trong tài liệu quyết định reengineer (về chuẩn) hay customise/localise (chỉ khi do luật địa phương như thuế) kèm lý do, vì bỏ lửng sẽ khiến khách "lách hệ thống" và phá vỡ thiết kế kiểm soát. (elbardan-erp-governance-audit ch06)
- Khi mô tả kiểm soát cho quy trình chạy qua nhiều chức năng/địa điểm, đặc tả theo chiều ngang (horizontal) end-to-end gộp tài chính + vận hành + IT, thay vì rời rạc theo màn hình/địa điểm. (elbardan-erp-governance-audit ch11)
- Khi khách muốn customise để giữ quy trình cũ, đưa quyết định reengineering vs customisation vào tài liệu kèm rủi ro mất tính kiểm soát/minh bạch, thay vì mặc nhiên chiều theo. (elbardan-erp-governance-audit ch10)
- Khi viết yêu cầu cho module kiểm toán/kiểm soát, dùng 9 khía cạnh IAF (scope, structure, skills, tools, sourcing, quan hệ với IT, size, budget, quan hệ với ngoại kiểm) làm checklist cấu trúc. (elbardan-erp-governance-audit ch03)

### nfr
- Khi đặc tả yêu cầu phi chức năng, coi bảo mật và phân quyền là NFR toàn cục, vì tính phụ thuộc lẫn nhau của ERP khiến một lỗ hổng cục bộ ở một phòng ban có thể làm gián đoạn toàn hệ thống. (elbardan-erp-governance-audit ch02)
- Khi làm chu trình nghiệp vụ trọng yếu, đưa audit trail và Continuous Auditing (embedded audit module hoặc monitoring control layer) vào spec. (elbardan-erp-governance-audit ch02)
- Khi đặc tả audit trail, bắt mọi giao dịch lưu ai/khi nào/tại sao và truy ngược được về sổ cái (GL) và sổ phụ, phục vụ minh bạch và khả năng kiểm toán. (elbardan-erp-governance-audit ch06)
- Khi viết yêu cầu bảo mật dữ liệu, nêu 4 thuộc tính confidentiality/authentication/integrity/non-repudiation, bắt dữ liệu đã nhập không sửa được, gateway quản lý user profile từ đăng ký đến kết thúc, và tuân PCI DSS với dữ liệu thẻ. (elbardan-erp-governance-audit ch08)

### master-data
- Khi đặc tả danh mục, chuẩn hóa standard chart of accounts, sổ cái chuẩn và định dạng dữ liệu thống nhất giữa các đơn vị, vì đây là nền của nhất quán dữ liệu để hợp nhất báo cáo không ra "nhiều giá trị cho cùng một dữ liệu". (elbardan-erp-governance-audit ch06)

### reports
- Khi viết spec, luôn kèm bộ báo cáo kiểm soát (discrepancy/reconciliation, exception, red-alert, xung đột SoD) và nêu rõ format/khối lượng/phân loại, vì báo cáo chuẩn của ERP thường không đủ và chiếm phần lớn khối lượng customise. (elbardan-erp-governance-audit ch06)
- Khi đặc tả chứng từ cần phê duyệt, mô tả đầy đủ approval workflow: approval hierarchy theo cấp, danh sách trường bắt buộc + prescribed ranges cho submission check, hành vi khi sai (approval errors window), tự in/chuyển trạng thái khi duyệt. (elbardan-erp-governance-audit ch08)
- Khi đặc tả công cụ kiểm soát, kèm audit trail/log, báo cáo tích hợp (kiểu Business Objects), truy vấn AML/chống rửa tiền và black-box test; nên tích hợp sẵn CAAT (ACL, data analysis tools) với ERP. (elbardan-erp-governance-audit ch09)
- Khi đặc tả tính năng báo cáo/giám sát, bắt hệ thống cung cấp báo cáo định kỳ, đột xuất, ngoại lệ và truy vấn đa đường thời gian thực để hỗ trợ continuous monitoring/assurance. (elbardan-erp-governance-audit ch10)

### requirements-elicitation
- Khi mục tiêu nghiệp vụ còn bao trùm/mơ hồ, phân rã thành các câu hỏi đóng kiểm chứng được (theo mẫu vấn đề bao trùm → RQ1–RQ5) để làm checklist nghiệm thu từng phần tài liệu. (elbardan-erp-governance-audit ch01)
- Khi thu thập/phân tích yêu cầu, áp directed content analysis: khởi đầu từ template/checklist dựng sẵn từ chuẩn ERP rồi cho yêu cầu mới của khách nổi lên và bổ sung — vừa chống AI hallucinate, vừa không bỏ sót chức năng. (elbardan-erp-governance-audit ch05)
- Khi verify một yêu cầu trước khi chốt, triangulate qua ≥2 nguồn (phỏng vấn nhiều vai, tài liệu, quan sát) và member-check với stakeholder, để bắt lệch/thiếu sớm. (elbardan-erp-governance-audit ch05)
- Khi bắt đầu dự án ERP, đưa kiểm toán/kiểm soát (và IT auditor) vào ngay giai đoạn requirements với vai trò super users để review đủ-kiểm-soát trước go-live — đây là khác biệt lớn nhất giữa ca thành công và thất bại. (elbardan-erp-governance-audit ch09)
- Khi tổ chức buổi khai thác yêu cầu ERP, biến 6 nhóm câu hỏi + bộ câu hỏi theo vai trò thành template, gửi trước cho khách như agenda để họ chuẩn bị (giảm hallucinate và thiếu thông tin). (elbardan-erp-governance-audit ch12)
- Khi nghiệm thu độ phủ tài liệu, gắn mỗi yêu cầu/kiểm soát vào một nhãn trong coding scheme 5 nhóm (áp lực/compliance, logic ERP, căn chỉnh, thay đổi tổ chức, chính danh/giá trị); nhãn nào trống là dấu hiệu thiếu chức năng. (elbardan-erp-governance-audit ch12)
- Khi lập nguồn yêu cầu, ghi nhận các compliance driver của khách (SOX, NYSE, Basel, central bank manual, code quản trị, chuẩn nội bộ group) như yêu cầu bắt buộc, vì chúng xác định tiêu chí hợp lệ của chức năng kiểm soát. (elbardan-erp-governance-audit ch10)
- Khi phân loại một feature, truy nó về coercive/normative/mimetic, vì điều đó phân biệt cái bắt buộc do luật với cái chỉ "theo trend thị trường" và giúp xếp ưu tiên đúng. (elbardan-erp-governance-audit ch04)
- Khi lấy bối cảnh dự án đầu buổi, thu "thông tin tổ chức" chuẩn: số module ERP triển khai và là những module nào, số chi nhánh trong nước/toàn cầu và mức tích hợp, mốc bắt đầu & kết thúc triển khai. (elbardan-erp-governance-audit ch12)
- Khi mô tả mỗi kiểm soát, bắt buộc hỏi "ai chịu trách nhiệm" để điền ma trận RACI (đánh giá kiểm soát nhúng, kiểm thử giao diện, rà log, kiểm thử quyền truy cập), tránh tài liệu mơ hồ. (elbardan-erp-governance-audit ch12)
- Khi thiết kế kịch bản agent hỏi lại khách để lấp lỗ hổng, dùng trình tự dễ → khó → tích cực để kết thúc buổi trên nốt thiện chí và xin được tài liệu/giới thiệu người khác. (elbardan-erp-governance-audit ch12)
- Khi dự đoán kháng cự của người dùng, ánh xạ sang 5 chiến lược Oliver (acquiescence/compromise/avoidance/defiance/manipulation), vì mỗi chiến lược đòi hỏi một tactic change management khác nhau. (elbardan-erp-governance-audit ch04)

### implementation-lifecycle
- Khi viết tài liệu triển khai, coi ERP là dự án thay đổi tổ chức: kèm thay đổi vai trò, quy trình và cấu trúc, không chỉ mô tả chức năng phần mềm. (elbardan-erp-governance-audit ch01)
- Khi lập kế hoạch triển khai, bố trí một team change management chuyên trách (gồm cả người kiểm soát) và đào tạo thật, vì nếu người dùng dùng sai ERP thì mọi kiểm soát nhúng trong hệ thống trở nên vô dụng. (elbardan-erp-governance-audit ch06)
- Khi chuẩn bị go-live, verify toàn bộ số lượng lớn control trong ERP và căn chỉnh quy tắc SoD/authorisation với quy tắc nghiệp vụ. (elbardan-erp-governance-audit ch06)
- Khi cutover, tuyệt đối tránh chạy song song thủ công + ERP không kiểm soát, vì điều này từng gây hàng ngàn lỗi phải kiểm toán lại nhiều tháng giao dịch. (elbardan-erp-governance-audit ch08)
- Khi lập tài liệu, thêm một mục "căn chỉnh & quản trị thay đổi": kế hoạch change management + đào tạo, danh sách quyết định reengineering vs customisation kèm rủi ro, và vai trò người kiểm soát trong dự án. (elbardan-erp-governance-audit ch11)

### data-migration-integrity
- Khi tích hợp hệ thống, cho kiểm toán/kiểm soát verify data migration (dữ liệu chuyển đúng, đủ) và test interface giữa hệ thống lõi và ERP để không mất dữ liệu — một hạng mục nghiệm thu bắt buộc. (elbardan-erp-governance-audit ch09)
- Khi đặc tả validation dữ liệu, áp CAVAIR (Complete, Accurate, Valid, Restricted Access) làm tiêu chí nghiệm thu và biến thành ràng buộc cụ thể trên từng bảng/giao diện nhập liệu. (elbardan-erp-governance-audit ch09)
- Khi hợp nhất dữ liệu từ nhiều chi nhánh/hệ cũ, bắt buộc cùng định dạng và cùng chart of accounts, vì trước ERP các phòng ban từng có giá trị khác nhau cho cùng một dữ liệu nghiệp vụ, tạo cơ hội thao túng. (elbardan-erp-governance-audit ch06)
- Khi đặc tả data migration, đưa yêu cầu "không mất dữ liệu tài chính khi chuyển sang ERP" vào tài liệu như input chính của người kiểm soát. (elbardan-erp-governance-audit ch10)
