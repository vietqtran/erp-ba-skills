# Chương 2: Sự tiến hóa của ERP (Evolution of ERP)

## Ý tưởng cốt lõi (Core Idea)
ERP là sự tiến hóa logic của chuỗi **IC → BOM → MRP → MRP II → ERP → (ERP II/SCM)**: từ kiểm soát tồn kho và bản kê vật tư, tới hoạch định vật tư, rồi hoạch định toàn bộ nguồn lực sản xuất, và cuối cùng mở rộng hoạch định ra cả nguồn lực nhà cung cấp theo nhu cầu động của khách hàng.

## Framework được giới thiệu (Frameworks Introduced)
- **Three manufacturing strategies** — ba chiến lược sản xuất: **Make-to-Stock** (sản xuất trước khi có đơn, lấp đơn từ tồn kho), **Make-to-Order** (chỉ sản xuất khi có đơn, kết hợp hàng chuẩn + thiết kế riêng), **Assemble-to-Order** (dự trữ linh kiện, nhận đơn mới lắp ráp theo đặc tả khách).
- **MRP (Material Requirements Planning)** — hoạch định nhu cầu vật tư: kỹ thuật xác định số lượng và thời điểm mua/sản xuất **dependent items** từ **MPS**.
  - Ba mục tiêu đồng thời: đảm bảo vật tư/sản phẩm sẵn sàng; giữ tồn kho thấp nhất có thể; hoạch định hoạt động sản xuất, lịch giao hàng, mua hàng.
- **MRP II (Manufacturing Resource Planning)** — hoạch định nguồn lực sản xuất: mở rộng closed-loop MRP, hoạch định mọi nguồn lực, có khả năng mô phỏng "what-if", lập kế hoạch theo đơn vị (units) lẫn tài chính (dollars).
- **Conceptual Framework of ERP** — sáu chức năng nghiệp vụ lõi: Accounting & Controlling; HR Management; Production & Materials Management; Project Management; Quality Management & Plant Maintenance; Sales & Distribution.
- **ERP II** (do Gartner Group định nghĩa lại) — ERP được "componentized" + e-business + cộng tác chuỗi cung ứng; chạm tới ba chiến lược: business, application, technology.

## Khái niệm chính (Key Concepts)
- **Master Production Schedule (MPS)**: kế hoạch time-phased cho lượng từng thành phẩm (end item) mỗi kỳ hoạch định; phải khả thi trong năng lực sẵn có.
- **Bill of Materials (BOM)**: bộ xử lý bản kê vật tư — nguồn gốc cấu trúc ERP từ thập niên 50–60.
- **MRP component-explosion logic**: từ MPS "nổ" ra nhu cầu time-phased cho linh kiện/nguyên liệu cấp dưới.
- **Independent vs dependent demand**: điểm mấu chốt MRP (thập niên 1970) — nhu cầu linh kiện phụ thuộc được tính ra, không dự báo độc lập.
- **Khác biệt MRP II ↔ ERP**: MRP II tập trung hoạch định **nguồn lực nội bộ**; ERP hoạch định thêm **nguồn lực nhà cung cấp** theo nhu cầu/lịch động của khách hàng.
- **Transaction backbone**: ERP là "chất keo" nối các giải pháp best-of-breed cho từng quy trình/mảng nghiệp vụ.

## Mô hình tư duy (Mental Models)
- Coi ERP như **"logical extension"** của MRP (1970s) và MRP II (1980s) — hiểu lịch sử để biết chức năng nào là lõi, chức năng nào là mở rộng.
- Bản chất tích hợp của ERP **buộc tư duy theo quy trình (process-wise) thay vì theo phòng ban (department-wise)**; lợi ích bất ngờ thường đến từ cải thiện giao tiếp liên phòng ban.
- ERP là **business project, không phải technology initiative**: lợi ích thật đến từ cái được thay đổi trong nghiệp vụ, nên cần tái cấu trúc (reengineering) toàn tổ chức, phần mềm chỉ là enabler.

## Ví dụ minh họa (Worked Example)
Cơ chế MRP mà chương mô tả, diễn giải từng bước: (1) **MPS** quy định cần bao nhiêu thành phẩm mỗi kỳ — một tập yêu cầu time-phased cho end items. (2) Doanh nghiệp còn cần yêu cầu time-phased cho linh kiện/nguyên liệu tạo nên thành phẩm đó. (3) MRP dùng **BOM** để "nổ" (explosion) MPS thành **production order và purchase order** cho các component cấp dưới, có tính tới lead-time và lot-size. (4) Vì năng lực mỗi kỳ hữu hạn, MPS phải khả thi và phải tối ưu — cân bằng mục tiêu mâu thuẫn: tồn kho thấp vs. tận dụng năng lực hiệu quả. Đây chính là logic mà MRP II và sau đó ERP kế thừa và mở rộng ra toàn nguồn lực.

## Điểm cần nhớ (Key Takeaways)
1. Thứ tự tiến hóa: IC/BOM (50s–60s) → MRP (70s) → MRP II (80s) → ERP (90s, bùng nổ khi SAP ra R/3 năm 1994) → ERP II.
2. Ba chiến lược sản xuất quyết định cách thiết kế luồng đơn hàng và tồn kho trong ERP.
3. MRP = xác định số lượng + thời điểm cho dependent items từ MPS qua BOM explosion.
4. MRP II thêm mô phỏng "what-if", hoạch định theo cả đơn vị lẫn tài chính; ERP thêm cả nguồn lực nhà cung cấp.
5. Sáu chức năng lõi của ERP là khung để phân rã module khi viết tài liệu.

## Ứng dụng cho BA ERP (BA Application)
- Khi viết spec module sản xuất/kho, bắt đầu từ **MPS → BOM explosion → purchase/production orders** và luôn gắn **lead-time, lot-size** vào mỗi item — đây là luồng chuẩn ERP cho nhoạch định vật tư.
- Phân biệt rõ **independent demand** (dự báo) và **dependent demand** (tính toán) khi thiết kế chức năng hoạch định, tránh để BA mô tả nhầm cả hai cùng kiểu.
- Dùng **sáu chức năng nghiệp vụ lõi** làm checklist phạm vi: thiếu chức năng nào thì tài liệu chưa cover đủ chuẩn ERP.
- Khi mô tả tích hợp SCM/CRM, ghi rõ ERP là "transaction backbone" nối các giải pháp khác — tránh viết ERP ôm trọn mọi thứ.

## Bảng tham chiếu (Reference Tables)
Ghi chú: Figure 1 (sơ đồ tiến hóa ERP) và Figure 4 (Conceptual Framework của ERP II) trong bản trích xuất chỉ còn lại caption "Figure 1"/"Figure 4", phần hình bị dẹt (flattened). Nội dung ERP II được tái dựng từ phần chữ:

| Nhóm thành phần ERP II | Thành phần |
|---|---|
| Central | Enterprise Resource Planning (ERP) |
| Corporate | SCM, CRM, SRM (Supplier Relationship Mgmt), PLM (Product Lifecycle Mgmt), ELM (Employee Lifecycle Mgmt), CPM (Corporate Performance Mgmt) |
| Collaborative | B2C, B2B, B2E, EAI (Enterprise Application Integration) |

## Liên hệ (Connects To)
- **Ch 1**: giải thích vì sao ERP "transaction-based" và cần tích hợp.
- **Ch 3**: sáu chức năng lõi được triển khai thành các module cụ thể (Finance, HR, MM, SD).
- **Ch 7–8 (ngoài slice)**: SCM và CRM là các corporate component mở rộng của ERP II.
