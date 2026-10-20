# Chương 11: Các tình huống triển khai ERP (ERP Case Studies)

## Ý tưởng cốt lõi (Core Idea)
Chương gồm 12 case (phần lớn là nhà sản xuất SME dùng **Intuitive ERP**, hai case lớn dùng **SAP R/3**). Xuyên suốt nổi lên một khuôn mẫu lặp lại: ERP mang lại giá trị bằng cách **tích hợp dữ liệu** để loại bỏ nhập liệu trùng, tăng độ chính xác **Bill of Material (BOM)** — định mức nguyên vật liệu, tăng vòng quay tồn kho, rút ngắn thời gian chốt sổ và cải thiện giao hàng đúng hạn. Thành công phụ thuộc vào tiêu chí lựa chọn đúng và quản lý thay đổi tốt.

## Framework được giới thiệu (Frameworks Introduced)
- **Case write-up template** — mẫu trình bày tình huống (dùng cho mọi case): (1) **About the Company**, (2) **Challenges faced**, (3) **Solution**, (4) **Outcome of ERP Implementation**.
- **ERP selection criteria (cross-case)** — tiêu chí lựa chọn ERP lặp lại: functionality, ease of use, scalability, integration (kế toán + sản xuất), technical support, underlying technology (100% Microsoft/.NET), low **Total Cost of Ownership (TCO)**, ease of customization, mức đáp ứng "out of the box".
- **KPI-based outcome measurement** — đo kết quả bằng KPI: tồn kho (days on-hand, inventory turns), on-time delivery, supplier performance, financial performance, quality.
- **Big Bang approach** — triển khai một lần toàn bộ: triển khai nhiều module cùng lúc (case SAP: 11 module) thay vì theo pha.

## Khái niệm chính (Key Concepts)
- **BOM accuracy**: BOM sai gây thiếu vật tư, "panic purchasing", nghẽn xưởng, trễ giao hàng → sửa BOM là đòn bẩy đầu tiên.
- **Inventory turns**: số vòng quay tồn kho/năm (nhiều case tăng từ ~2 lên 6 lần/năm).
- **Advanced Configurator**: đặt luật để đảm bảo đơn cấu hình thực sự sản xuất được; một case giảm BOM từ 26.000 xuống 13.000 dòng.
- **Location/Lot Tracking**: truy xuất nguồn gốc lô (quan trọng với hàng không — truy ngược lô keo lỗi).
- **ETO (Engineer-to-Order)**: sản xuất theo đơn thiết kế riêng; đòi hỏi nhiều thời gian để vendor hiểu yêu cầu.

## Mô hình tư duy (Mental Models)
- "Vision without a plan is only an illusion" — tầm nhìn mà không có kế hoạch chỉ là ảo tưởng: ERP thành công cần cả tầm nhìn lẫn kế hoạch.
- Giá trị lớn nhất của tích hợp = "nhập một lần, dùng khắp hệ thống", xóa nhập liệu trùng và mâu thuẫn dữ liệu.
- Với doanh nghiệp bị quản lý phân tán: thiếu quy trình chuẩn chính là rào cản mở rộng quy mô, dù nguồn lực dồi dào.

## Điều cần tránh (Anti-patterns)
- **Đánh giá thấp mức độ thay đổi quy trình** (Case 11): các bên liên quan ở nước ngoài không nhận ra dự án thay đổi quy trình bao nhiêu → không gặt được lợi ích.
- **Đào tạo không đủ + thiếu quản lý thay đổi**: nhân viên cấp thấp không hiểu cách dùng và lý do thay đổi; "không ai được chuẩn bị cho cách làm mới".
- **Tích hợp module dở dang**: triển khai ồ ạt nhưng không tích hợp hết các module → phải dừng dự án.

## Bảng tham chiếu (Reference Tables)
KPI cải thiện điển hình trích từ các case:

| Chỉ số | Trước | Sau |
|---|---|---|
| Tồn kho (days on-hand) | 90 ngày | 15 ngày |
| On-time delivery | 75% → / 30% → | 99% / 90% |
| Supplier on-time delivery | 30% | >80% |
| Inventory turns/năm | ~2 | 6 |
| Thời gian chốt sổ | 3 tuần | <1 tuần |
| Order cycle time (sản phẩm chủ lực) | 4 tháng | 4 tuần (-80%) |
| Thời gian triển khai (SME) | — | 45–90 ngày |

## Ví dụ minh họa (Worked Example)
**Case 11 — Triển khai toàn cầu thất bại rồi phục hồi** (tập đoàn thực phẩm & dược, doanh thu ~$50 tỷ, 250.000 nhân viên, 500 cơ sở tại 90 quốc gia; tên bị ẩn danh trong sách). Vấn đề: quản lý phân tán với 80 đơn vị IT, ~1000 AS/400, thiếu quy trình chuẩn cản trở e-commerce. Giải pháp: chuẩn hóa bằng các module purchasing, financials, sales & distribution; cấu trúc công việc theo "best practices" cho 300 work roles; lập tới 5 trung tâm máy tính toàn cầu. Thất bại: stakeholder không lường hết thay đổi quy trình, đào tạo thiếu, công nhân không hiểu hệ mới. Phục hồi: **dừng dự án**, xáo lại vai trò nhóm, giáo dục về *cái gì–tại sao–như thế nào–khi nào* thay đổi, khảo sát lặp tác động lên nhân viên.

**Case 12 — SAP R/3 cho doanh nghiệp ETO** (nhà sản xuất turbine hơi, Rs 750 crore). Chọn SAP vì cần ít tùy biến nhất và hợp lộ trình PLM/CRM. Triển khai **Big Bang 11 module** (sales, distribution, project systems, financial, cost accounting, product planning, quality management, customer support, EIS, workflow, payroll). Chuyển đổi dữ liệu mất 5 tháng do BOM lớn (60.000–70.000 mục); 120 người được đào tạo; go-live sau ~2 năm. Lợi ích sau 7 tháng: truy vết vật tư online, hết trùng lặp, tính được tổng chi phí vòng đời dự án (gồm công tác phí, thay thế bảo hành).

## Điểm cần nhớ (Key Takeaways)
1. Dùng mẫu 4 phần (Company / Challenges / Solution / Outcome) để viết và đọc mọi case ERP.
2. Lợi ích ERP đến từ tích hợp: nhập một lần, xóa trùng lặp, dữ liệu nhất quán.
3. BOM chính xác là điểm khởi đầu cho cải thiện tồn kho, lịch xưởng và giao hàng.
4. Đo thành công bằng KPI trước/sau (tồn kho, giao đúng hạn, inventory turns, thời gian chốt sổ).
5. Thất bại ERP thường do quản lý thay đổi và đào tạo yếu, không phải do phần mềm.

## Ứng dụng cho BA ERP (BA Application)
- Yêu cầu khách định nghĩa bộ KPI trước/sau (như Case 3: >10 KPI) và đưa chúng thành tiêu chí nghiệm thu đo được trong tài liệu, thay vì mô tả lợi ích chung chung.
- Đặc tả tiêu chí lựa chọn ERP tường minh (functionality, ease of use, scalability, integration, TCO, mức đáp ứng out-of-the-box) để quyết định chọn gói có vết.
- Luôn thêm mục Change Management và kế hoạch đào tạo vào spec triển khai — các case thất bại đều do thiếu hai thứ này.
- Khi nghiệp vụ là ETO/làm theo đơn, cảnh báo trong spec về thời gian để vendor hiểu yêu cầu và khối lượng chuyển đổi dữ liệu (BOM lớn), để ước lượng không phi thực tế.
- Nêu rõ chiến lược triển khai (Big Bang vs theo pha) và rủi ro kèm theo trong tài liệu dự án.

## Liên hệ (Connects To)
- **Ch 5 (ERP Implementation)**: vòng đời triển khai, quản lý thay đổi.
- **Ch 9 & 10 (vendors)**: Intuitive ERP và SAP R/3 là các sản phẩm trong case.
- **Ch 12 (UML)**: nhiều câu hỏi ôn tập yêu cầu mô hình hóa quy trình doanh nghiệp bằng business model.
