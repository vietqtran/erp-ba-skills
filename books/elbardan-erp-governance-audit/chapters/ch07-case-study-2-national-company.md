# Chương 7: Kết quả từ Tình huống nghiên cứu 2 — Công ty Quốc gia (Findings from Case Study 2 — The National Company (NC))

## Ý tưởng cốt lõi (Core Idea)
NC là tập đoàn thực phẩm Ai Cập (ghee, bơ, phô mai, sữa, nước ép, >1500 nhân viên) triển khai **SAP** năm 2010 với các module *financial accounting, sales & distribution, HR*. Động cơ: củng cố hệ thống kiểm soát nội bộ yếu, giảm rủi ro gian lận/trộm cắp, kiểm soát chi phí. Đây là **ca thất bại điển hình**: ERP mang đầy đủ "logic kiểm soát" chuẩn nhưng tổ chức có văn hóa "lách luật" (rule-breaking) và ban lãnh đạo *chống minh bạch* (anti-transparency: trốn thuế, giấu lợi nhuận/công thức sản phẩm) nên lách hệ thống (work around), không có kế hoạch quản lý thay đổi, không cho kiểm toán nội bộ tham gia. Kết quả: **IAF** — chức năng kiểm toán nội bộ (Internal Audit Function) — bị thu hẹp còn 1 người mang tính hình thức và mất hoàn toàn tính chính danh.

## Khái niệm chính (Key Concepts)
- **Control assumptions of ERP**: 10 "giả định kiểm soát" mà ERP áp đặt (xem Bảng tham chiếu) — là bộ khung chuẩn ERP tái dùng được cho mọi ca.
- **Single data entry point**: nguyên tắc nhập liệu một điểm — dữ liệu nhập một lần, mọi xử lý sau đó tự động, tự lan sang mọi module liên quan.
- **Segregation of Duties (SoD)**: phân tách nhiệm vụ — ERP tự động áp đặt qua danh sách phân quyền và kiểm soát truy cập.
- **Preventive vs detective controls**: kiểm soát phòng ngừa (chặn trước khi lỗi xảy ra) đối lập kiểm soát phát hiện (tìm lỗi sau khi đã xảy ra); tự động hóa biến kiểm soát thành phòng ngừa.
- **Work around the system**: lách hệ thống — dùng giải pháp thủ công/ngoài hệ thống để giữ thực hành cũ thay vì tuân theo quy trình chuẩn ERP.
- **Decoupling / ceremonial compliance**: tách rời lõi khỏi vỏ — giữ hình thức (1 kiểm toán viên, 1 ủy ban kiểm toán "không kích hoạt") để trông có vẻ tuân thủ mà thực chất không có chức năng thật.
- **Oliver's strategic responses**: 5 chiến lược phản ứng thể chế (acquiescence, compromise, avoidance, defiance, manipulation) — NC dùng defiance/avoidance/compromise và vẫn thất bại.

## Bảng tham chiếu (Reference Tables)
**10 giả định kiểm soát của ERP (Control Assumptions)** — bộ khung chuẩn, kèm cơ chế cụ thể quan sát tại NC (SAP):

| # | Giả định (EN) | Cơ chế kiểm soát cụ thể (code-able) |
|---|---|---|
| 1 | **Automation** | Hành vi phi tài chính tự sinh bút toán tài chính (no human intervention); payroll tính theo vân tay/giờ công; tự lưu trữ (archiving); tự áp đặt SoD |
| 2 | **Centralisation** | Module tài chính là "pool" trung tâm nhận mọi giao dịch; một CSDL dùng chung cho mọi nhu cầu |
| 3 | **Continuous Timely Monitoring** | Theo dõi giao dịch theo thời gian thực; peer review (không bước nào đi tiếp nếu bước trước chưa được duyệt theo tiêu chí nhúng sẵn); báo cáo/cảnh báo real-time |
| 4 | **Data Consistency** | Dữ liệu event-driven; data warehouse; báo cáo so sánh giữa các năm; truy vết "ai nhập mảnh nào, khi nào, vì sao" |
| 5 | **Data Security** | confidentiality, authentication, integrity, non-repudiation; dữ liệu đã nhập không sửa được; gateway quản lý user profile từ đăng ký → sửa → kết thúc |
| 6 | **Control Through Integration** | CSDL đơn, không trùng lắp; lỗi bị user kế tiếp phát hiện; hợp nhất giao dịch đa công ty |
| 7 | **Multiple Methods of Control** | Kiểm soát lồng nhau: một người nhập, một người duyệt, một người xác nhận — mỗi bút toán được soát 1–3 lần |
| 8 | **Preventive Controls** | authorisation lists, SoD, duyệt cấp trên bắt buộc; chặn post sai khách hàng/kỳ đã khóa/nhà cung cấp lỗi; chặn lệnh sản xuất nếu kho thiếu vật tư; tự lập lịch bảo trì máy |
| 9 | **Standardisation** | Chuẩn hóa hạ tầng IT và quy trình giữa các địa điểm (NC từ chối chuẩn hóa các quy trình bất hợp pháp) |
| 10 | **Transparency & Visibility** | Master data tập trung; hành vi nơi làm việc hiển thị với đồng nghiệp/quản lý qua workflow dependency |

## Điều cần tránh (Anti-patterns)
- **Lách hệ thống để giữ thực hành cũ/bất hợp pháp**: NC tạo "pay code" đặc biệt cho lao động thời vụ không hợp đồng; giữ sổ tay thủ công song song — vô hiệu hóa kiểm soát chuẩn ERP.
- **Không có kế hoạch quản lý thay đổi (change management)**: nhân viên sợ bị thay thế; cơ cấu tổ chức đổi làm giảm tầm quan trọng IAF; không ai truyền đạt *lý do* thay đổi.
- **Không cho IAF tham gia triển khai**: không có IT auditor → kiểm toán viên không hiểu hệ thống, không thể đảm bảo SoD/phân quyền, không kiểm toán được output.
- **Tuân thủ hình thức (ceremonial)**: có ủy ban kiểm toán "không kích hoạt"; giữ 1 kiểm toán viên như biểu tượng — conformity by appearance rather than essence.
- **Không dùng tính năng kiểm soát/báo cáo của ERP**: auditor không dùng SAP, từ chối CAAT; IT team làm thay việc kiểm toán → IAF bị xói mòn.
- **Ban lãnh đạo chống minh bạch**: từ chối đưa công thức sản phẩm, giá mua, khách hàng, lợi nhuận lên hệ thống → triệt tiêu lợi ích quản trị của ERP.

## Điểm cần nhớ (Key Takeaways)
1. ERP chuẩn tự động hóa: **một điểm nhập liệu → tự sinh bút toán → tự áp SoD → kiểm soát phòng ngừa**. Nếu không dùng, mọi lợi ích kiểm soát biến mất.
2. Các ví dụ kiểm soát phòng ngừa của ERP rất cụ thể và lập trình được (chặn post sai khách hàng/kỳ khóa; chặn lệnh sản xuất khi thiếu vật tư).
3. Văn hóa tổ chức (chống minh bạch) quyết định việc ERP có phát huy tác dụng hay không, nhiều hơn cả bản thân phần mềm.
4. Thiếu change management + thiếu sự tham gia của kiểm soát/kiểm toán khi triển khai = chức năng kiểm soát mất chính danh.

## Ứng dụng cho BA ERP (BA Application)
- Dùng **bảng 10 Control Assumptions** làm checklist khi đặc tả bất kỳ chức năng ERP: với mỗi chức năng, ghi rõ nó hiện thực giả định kiểm soát nào và bằng cơ chế gì (single entry, auto-journal, SoD, preventive rule...).
- Viết **preventive control** thành luật if/else cụ thể, code-able: "không cho tạo lệnh sản xuất nếu tồn kho vật tư < định mức"; "chặn post vào kỳ kế toán đã khóa"; "chặn post hóa đơn cho khách khác mã đã ghi".
- Đặc tả **single data entry point** và luồng tự sinh bút toán tài chính từ nghiệp vụ phi tài chính — nêu rõ bước nào mặc nhiên chấp nhận dữ liệu bước trước (peer review nhúng trong quy trình).
- Luôn gắn mỗi chức năng với **ma trận phân quyền + SoD** (ai nhập / ai duyệt / ai xác nhận) để tài liệu đủ chi tiết, không mơ hồ.
- Cảnh báo sớm trong tài liệu các điểm **misalignment** giữa quy trình khách hàng và chuẩn ERP (ví dụ: quy trình khách muốn giữ không thể chuẩn hóa) — để không bị "lách hệ thống" phá vỡ thiết kế.

## Liên hệ (Connects To)
- **Ch 6**: Case 1 (International Company) — cùng bộ 10 giả định kiểm soát và khung Oliver, dùng để so sánh chéo.
- **Ch 8, Ch 9**: Case 3 (NB) và Case 4 (IB) — cùng cấu trúc phân tích nhưng là ca thành công/trưởng thành hơn.
- **Ch 10**: Phân tích chéo 4 ca, rút ra khác biệt về mức độ thích nghi của IAF.
- **COSO / institutional theory**: nền lý thuyết về kiểm soát nội bộ và tính chính danh.
