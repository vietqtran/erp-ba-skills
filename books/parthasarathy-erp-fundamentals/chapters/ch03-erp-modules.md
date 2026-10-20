# Chương 3: Các module của ERP (ERP Modules)

## Ý tưởng cốt lõi (Core Idea)
Một gói ERP được cung cấp theo **một module hoặc một tập module** tùy nhu cầu khách hàng; số lượng module khác nhau giữa các gói. Chương mô tả chi tiết bốn module phổ biến nhất mà mọi nhà cung cấp đều có: **Finance, Human Resource Management (HR), Materials Management (MM), Sales & Distribution (SD)** — cùng các chức năng con cần có để viết đặc tả.

## Framework được giới thiệu (Frameworks Introduced)
- **Lý do chọn một module thay vì hệ tích hợp đầy đủ**: giảm chi phí, module chuyên biệt, rút ngắn thời gian dự án, ít rủi ro, ít kháng cự thay đổi, mua module từ nhiều vendor khác nhau, nhiều tính năng + ít đào tạo + dễ bảo trì.
- **Finance Module — 5 phân hệ**: Accounting; Investment management; Cost controlling; Treasury management; Planning & forecasting. (Tác giả coi **Treasury management** và **Cost controlling** là thiết yếu nhất cho ra quyết định của lãnh đạo.)
- **HR Module — functions**: hai nhóm — **Managerial functions** (Planning, Organizing, Directing, Controlling) và **Operative functions** (Employment, Human Resource Development–HRD, Compensation).
- **Materials Management (MM) Module — chức năng tích hợp**: Inventory management, MRP, Purchasing, Warehouse management, Vendor evaluation, Invoice verification, Product costing.
- **Sales & Distribution (SD) Module — key elements**: Selling, Shipping, Billing, Master Data Management, Customer's Order Management, Pricing Strategies. Ba quy trình chính: **Sales → Shipping → Billing**.

## Khái niệm chính (Key Concepts)
- **Treasury management**: quản lý hoạt động tài trợ — lập báo cáo tài chính, quan hệ ngân hàng/nhà đầu tư, tài trợ ngắn/dài hạn, quản lý tiền mặt, tín dụng, đầu tư, bảo hiểm.
- **Cost controlling**: financial accounting, internal auditing, tính thuế, đặt/giám sát tham số kiểm soát chi phí, lập ngân sách, kiểm soát cash flow/funds flow.
- **HRD vs HRM**: HRD là quá trình phát triển kỹ năng/kiến thức/thái độ theo yêu cầu công việc; HRM đã chuyển từ vai trò thụ động (payroll, tuyển dụng, hồ sơ) sang vai trò **chiến lược** (giữ chân & phát triển nhân sự).
- **Inventory control**: duy trì lượng tối ưu vừa đủ cho vận hành trơn tru.
- **Carrying costs**: chi phí lưu giữ (kho bãi, bảo hiểm, bốc dỡ, kiểm tra) tăng theo lượng tồn kho.
- **Three motives for holding inventory**: Transactions motive, Precautionary motive, Speculative motive.
- **JIT (Just-in-Time)**: MM hỗ trợ qua "disposition" — cung ứng vật tư đúng nhu cầu kỳ vọng.
- **Pricing objectives (SD)**: market penetration, price stabilization, market share, profit maximization, cash/funds flow, demand forecasting, market analysis, discounts.

## Mô hình tư duy (Mental Models)
- Coi **module là đơn vị mua và triển khai**: không nhất thiết mua cả bộ; có thể chỉ cài Finance hoặc HR trước, phần còn lại để sau.
- Coi **MM là "central point of logistics"** nối planning–sourcing–purchasing–moving–storing–controlling vật tư ở mức chi phí tối thiểu, với dịch vụ khách hàng định trước.
- Mỗi module tốt vì nó **tự động hóa + tích hợp**: ví dụ khi phát hành purchase order, hệ của nhà cung cấp được cập nhật ngay, rút ngắn lead-time.

## Điều cần tránh (Anti-patterns)
- **Quản lý vật tư kém (poor inventory management)**: tồn kho dư làm đóng băng vốn, tăng carrying cost, bào mòn lợi nhuận; tồn kho thiếu gây dừng sản xuất, mất doanh thu.
- Bỏ qua phân loại đơn hàng trong SD: không tách **Normal vs Abnormal Sales Orders** khiến không ưu tiên được đơn quan trọng/khách lớn.

## Ví dụ minh họa (Worked Example)
Luồng end-to-end của **Sales & Distribution Module** (mô tả theo Figure 6, vốn bị dẹt trong bản trích xuất) cho thấy tích hợp ba module: (1) Khách hàng **inquiry** về sản phẩm → (2) nhận **quotation** từ nhà cung cấp → (3) sau khi xem xét, **đặt order** → (4) nhà cung cấp **giao hàng qua Materials Management** (shipping liên kết MM) → (5) **billing liên kết Finance Module**. Như vậy một đơn bán hàng chạm cả ba module: SD (bán), MM (giao/xuất kho), Finance (lập hóa đơn, ghi sổ). Song song, SD phân loại đơn: đơn thường được chuyển xuống production dưới dạng sales demand; đơn tăng đột biến vượt dự báo là **abnormal sales order** và được ưu tiên hơn đơn đã lên kế hoạch.

## Điểm cần nhớ (Key Takeaways)
1. Bốn module phổ biến: Finance, HR, Materials Management, Sales & Distribution — nhớ danh mục chức năng con của từng module để kiểm tra độ bao phủ.
2. Finance: Treasury management + Cost controlling là hai phân hệ then chốt cho ra quyết định.
3. HR chia Managerial (Planning/Organizing/Directing/Controlling) và Operative (Employment/HRD/Compensation).
4. MM gắn trực tiếp với MRP, purchasing, warehouse, vendor evaluation, invoice verification; mục tiêu là cân bằng tồn kho ↔ dịch vụ khách hàng.
5. SD = Sales → Shipping (→MM) → Billing (→Finance); tích hợp liên module là điểm nhận diện chuẩn ERP.

## Ứng dụng cho BA ERP (BA Application)
- Dùng **danh mục chức năng con của mỗi module** (ví dụ 5 phân hệ Finance, 7 chức năng MM, 6 key element SD) làm **checklist "cover đủ chức năng"** — thiếu mục nào là tài liệu hụt chức năng.
- Khi đặc tả một chức năng bán hàng, luôn vẽ luồng **liên module SD↔MM↔Finance** (order → shipping → billing) kèm điểm dữ liệu bàn giao giữa các module, thay vì đặc tả SD cô lập.
- Với tồn kho, ghi rõ mục tiêu kép (đủ hàng phục vụ khách vs. giữ vốn ở mức hợp lý) và áp **ABC analysis + stock levels + inventory ratios** như tiêu chí nghiệm thu.
- Với SD, bắt buộc có quy tắc phân loại đơn (Normal vs Abnormal) và pricing objectives để tránh tài liệu mơ hồ khi xử lý đơn ưu tiên.
- Nêu rõ master data cần có cho SD (customer, order, supplier details) — Master Data Management là một key element, không được bỏ sót trong spec.

## Liên hệ (Connects To)
- **Ch 2**: bốn module hiện thực hóa sáu chức năng nghiệp vụ lõi của ERP; MM chứa chính MRP đã nêu ở Ch2.
- **Ch 1**: minh họa Business Integration (finance tra cứu warehouse) được cụ thể hóa bằng luồng SD→MM→Finance.
- **Ch 5**: module-wise approach khi triển khai dựa trên chính cách chia module này.
