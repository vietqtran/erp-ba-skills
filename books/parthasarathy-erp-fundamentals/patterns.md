# Patterns — Kỹ thuật & quy trình chuẩn ERP (Parthasarathy)

Các kỹ thuật/khuôn mẫu rút từ sách, dạng áp dụng được. Thuật ngữ gốc giữ tiếng Anh.

## MRP component explosion (MPS → BOM → orders)
**When to use**: Hoạch định vật tư cho sản xuất khi sản phẩm có cấu trúc nhiều cấp (Ch 2).
**How**: Lấy **MPS** (lượng thành phẩm mỗi kỳ) làm đầu vào → dùng **BOM** "nổ" thành nhu cầu linh kiện cấp dưới → sinh production order và purchase order, có tính **lead-time** và **lot-size** cho từng item.
**Trade-offs**: MPS phải khả thi trong năng lực mỗi kỳ; phải cân mục tiêu mâu thuẫn giữa tồn kho thấp và tận dụng năng lực. Nhu cầu linh kiện là dependent demand (tính toán), không dự báo độc lập.

## Four-phase ERP selection process
**When to use**: Chọn một gói ERP từ hàng trăm sản phẩm trên thị trường (Ch 4).
**How**: Phase 1 — dựng **requirements profile** (bảng hỏi + phỏng vấn) → "Top Ten List" (< 3 tuần). Phase 2 — đặt high-level differentiators định lượng + định tính, lọc còn **2–4** ứng viên (< 1 tháng). Phase 3 — demo do khách điều khiển + đàm phán, chọn cuối (1–2 tháng). Phase 4 — implementation planning.
**Trade-offs**: Tốn ~3–6 tháng; chất lượng phụ thuộc hoàn toàn vào độ tốt của requirements profile.

## Demo control via function checklist
**When to use**: Giai đoạn demo sản phẩm (Phase 3 của quy trình chọn) (Ch 4).
**How**: Khách gửi trước cho vendor danh sách **50–100 chức năng bắt buộc** phải trình diễn, dựa trên high-level requirements; khách tự điều phối buổi demo thay vì để vendor dẫn dắt.
**Trade-offs**: Biến yêu cầu thành tiêu chí kiểm thử rõ ràng; nhưng nếu requirements profile thiếu thì danh sách demo không đáng tin.

## ABC (Always Better Control) inventory analysis
**When to use**: Kiểm soát nhiều mặt hàng tồn kho, cân bằng tồn kho và dịch vụ khách hàng (Ch 3).
**How**: Lập danh mục mặt hàng → phân loại ABC → duy trì stock level cho mọi mặt hàng → giám sát liên tục → đánh giá qua inventory ratios.
**Trade-offs**: Giữ tối ưu giữa carrying cost (tồn dư đóng băng vốn) và nguy cơ stock-out gây dừng sản xuất.

## Gap Analysis with fill options
**When to use**: Sau khi đánh giá gói, trước reengineering/customization (Ch 5).
**How**: Liệt kê từng **gap** giữa quy trình hiện tại và chức năng gói; mỗi gap chọn phương án lấp: (a) sản phẩm bên thứ ba, (b) viết chương trình tùy biến, (c) sửa source ERP; mời consultant trung lập hóa giải xung đột.
**Trade-offs**: Sửa source hoặc bolt-on tăng chi phí bảo trì, khó nâng cấp; third-party thêm điểm tích hợp.

## Minimizing customization
**When to use**: Suốt giai đoạn customize của triển khai (Ch 5).
**How**: Không bao giờ sửa **base** hệ thống; tránh interface tới legacy và bolt-on trừ khi bất khả kháng; cân 3 tham số (end-user req, technical req, vision lãnh đạo); giữ customize thấp nhất.
**Trade-offs**: Ít customize = ít khớp thói quen cũ (gây kháng cự) nhưng giữ được lợi ích ERP, giảm chi phí re-implement mỗi bản phát hành và dễ nâng cấp.

## Choosing an implementation approach
**When to use**: Quyết định cách rollout ERP (Ch 5).
**How**: Chọn **Big Bang** (mọi module cùng lúc), **Location-wise** (theo địa điểm), hoặc **Module-wise** (từng module) dựa trên rủi ro, chi phí, thời lượng, yêu cầu.
**Trade-offs**: Big Bang đạt lợi ích đầy đủ nhưng rủi ro cao; Location/Module ít rủi ro–chi phí–thời lượng, có feedback trước khi mở rộng nhưng chỉ lợi ích từng phần.

## Benefits realization in three levels
**When to use**: Sau go-live, để đặt kỳ vọng và lộ trình thu lợi ích (Ch 5).
**How**: Cấp 1 — tự động hóa quy trình hiện có; cấp 2 — thấy quy trình được cải thiện/tái thiết kế; cấp 3 — hệ hỗ trợ ra quyết định (DSS) cho quản lý cấp trung và cấp cao.
**Trade-offs**: Mất vài tháng tới ~1 năm mới hiện rõ; đừng kỳ vọng lợi ích tức thì sau go-live.

## META Group six-phase ERP migration
**When to use**: Chuyển ERP từ nền tảng/OS này sang nền tảng khác (Ch 6).
**How**: Analysis (hiện trạng vs yêu cầu) → Definition (phạm vi & ngân sách, độ phù hợp kỹ năng/quy trình/văn hóa) → Coordination (phát triển, tinh chỉnh, QA) → Transition → Ongoing management → Change Management.
**Trade-offs**: Nhân lực IT dồn cao nhất ở pha triển khai; trung bình ~7 tháng; cần biện minh cả nghiệp vụ lẫn kỹ thuật, không coi là tác vụ IT thuần.

## Four-step SCM decision making
**When to use**: Thiết kế hoặc tối ưu một chuỗi cung ứng (Ch 7).
**How**: Location (vị trí cơ sở/kho/nguồn cung) → Production (sản xuất gì/khi nào/bao nhiêu) → Inventory (lưu trữ, tồn an toàn) → Transportation (phương thức vận chuyển). Mỗi bước phân theo cấp strategic/tactical/operational.
**Trade-offs**: Giữ tồn kho tốn 20–40% giá trị; chọn vận chuyển rẻ (tàu/đường sắt) buộc giữ tồn kho lớn hơn và lập kế hoạch sớm hơn.

## Three-component CRM design
**When to use**: Đặc tả hoặc đánh giá một hệ CRM tích hợp ERP (Ch 8).
**How**: Chia hệ thành **Operational CRM** (tự động hóa quy trình, nối front/back-office), **Analytical CRM** (data mining + data warehousing + OLAP sinh báo cáo), **Collaborative CRM** (email, chat, web, e-commerce). Ánh xạ mỗi chức năng vào đúng thành phần.
**Trade-offs**: Bỏ sót một thành phần làm giảm giá trị tổng thể; analytical CRM đòi hạ tầng dữ liệu phức tạp.

## Standardized + dynamically choreographed business rules
**When to use**: Thiết kế kiến trúc ERP hiện đại để tài liệu đủ rõ cho code (Ch 9).
**How**: Chuẩn hóa business rules; **gói validation rules riêng với processing rules**; cho phép điều phối động (dynamic choreography); kiến trúc loosely coupled; một điểm hội tụ cho dữ liệu đầu vào; giao tiếp theo sự kiện.
**Trade-offs**: Đòi tái thiết kế trên nền chuẩn (.NET/XML); đổi lại dễ bảo trì, dễ tùy biến, toàn vẹn dữ liệu.

## Vendor selection matrix (least customization)
**When to use**: Lập tài liệu so sánh và lựa chọn vendor/gói ERP (Ch 10).
**How**: Xây ma trận vendor × tiêu chí (ngành dọc, nền tảng, chiều sâu chức năng, mức tùy biến, lộ trình nâng cấp, địa phương hóa ngôn ngữ/tiền tệ/thuế); ưu tiên vendor phù hợp ngành dọc và cần **ít tùy biến nhất**.
**Trade-offs**: Ít tùy biến giúp triển khai nhanh/rẻ và hợp lộ trình, nhưng có thể phải điều chỉnh quy trình theo best practices của gói.

## Case write-up template + KPI before/after
**When to use**: Tài liệu hóa một tình huống triển khai, hoặc định nghĩa tiêu chí thành công (Ch 11).
**How**: 4 phần — About the Company / Challenges / Solution / Outcome. Thiết lập >10 KPI (days-on-hand, inventory turns, on-time delivery, supplier performance, thời gian chốt sổ) và đo **trước/sau**.
**Trade-offs**: KPI rõ giúp nghiệm thu đo được, nhưng cần nền dữ liệu lịch sử sạch để so sánh có ý nghĩa.

## UML business modeling (5 notations, 4 diagrams)
**When to use**: Đặc tả chi tiết một chức năng ERP để lập trình viên code được ngay (Ch 12).
**How**: Dùng 5 phần tử (business actor, worker, entity, use case, organizational unit) và 4 sơ đồ: **Use Case** (bối cảnh & actor), **Activity + swimlanes** (luồng & vai trò), **Class** (entity & quan hệ), **Sequence** (tương tác các bước).
**Trade-offs**: Tốn công vẽ đủ bộ sơ đồ, nhưng elicit yêu cầu tốt hơn, phân vai trò rõ, và cho phép reengineering thay vì chỉ automation.
