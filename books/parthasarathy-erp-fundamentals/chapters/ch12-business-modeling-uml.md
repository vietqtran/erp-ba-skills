# Chương 12: Mô hình hóa nghiệp vụ bằng UML (Business Modeling Using UML)

## Ý tưởng cốt lõi (Core Idea)
Mô hình hóa nghiệp vụ là nền tảng cho phần mềm đóng gói như ERP. **Unified Modeling Language (UML)** — ngôn ngữ mô hình hóa thống nhất đóng vai trò giao diện giữa **business analyst** và **system analyst**: một ký pháp, một công cụ dùng chung cho cả nghiệp vụ lẫn hệ thống, giúp hai bên giao tiếp chính xác. Chỉ khi quy trình hiện tại được nghiên cứu–phân tích–thấu hiểu thì mới **Reengineering** (tái cấu trúc/tối ưu) được; nếu không, chỉ **tự động hóa** quy trình cũ mà không có tối ưu.

## Framework được giới thiệu (Frameworks Introduced)
- **UML Business Modeling Notation** — ký pháp mô hình hóa nghiệp vụ UML (5 phần tử).
  - **Business actor**: ai đó/thứ gì đó *bên ngoài* doanh nghiệp tương tác với doanh nghiệp.
  - **Business worker**: vai trò (role) *bên trong* doanh nghiệp, tương tác với worker khác và thao tác business entity.
  - **Business entity**: một "thứ" được business worker xử lý/sử dụng.
  - **Business use case**: chuỗi hành động doanh nghiệp thực hiện, tạo ra kết quả có giá trị quan sát được cho một business actor.
  - **Organizational unit**: tập hợp worker, entity, quan hệ và hiện thực use case — dùng để chia nhỏ mô hình.
- **Four UML diagrams → four views** — bốn sơ đồ UML, bốn góc nhìn: **Use Case Diagram** (bối cảnh nghiệp vụ), **Activity Diagram** (luồng công việc), **Class Diagram** (cấu trúc tĩnh), **Sequence Diagram** (tương tác giữa một bước quy trình và các đối tượng khác).
- **Role Activity Diagram & Swimlanes** — sơ đồ hoạt động theo vai trò: hoạt động được phân vào các cột **swimlanes**, thể hiện ai chịu trách nhiệm việc gì.

## Khái niệm chính (Key Concepts)
- **Business Model**: kỹ thuật mô hình hóa quy trình nghiệp vụ theo hoạt động và hành vi cộng tác; giúp tài liệu hóa và nắm bắt độ phức tạp.
- **Use Case**: mô tả hệ thống *được dùng thế nào* bởi các actor bên ngoài; business use case = tập các process steps liên quan; actor = vai trò tổ chức thực thi các bước đó.
- **Business worker vs Business entity**: trong class diagram, mỗi lớp là một worker (nhân sự) hoặc một entity ("thứ" doanh nghiệp thao tác).
- **Reengineering vs Automation**: hiểu quy trình → reengineering (tối ưu); không hiểu → chỉ automation (không tối ưu).

## Mô hình tư duy (Mental Models)
- Coi UML như "ngôn ngữ chung" giữa BA và dev: biểu tượng nghiệp vụ (business-specific icons) giúp phân biệt phần tử nghiệp vụ với phần tử hệ thống trong cùng mô hình trực quan.
- Lợi ích lớn nhất của mô hình hóa nghiệp vụ là **elicit được yêu cầu tốt hơn**: khi đã có business model, thiết lập quan hệ giữa system requirements và business model cho phép đưa thay đổi nghiệp vụ vào định nghĩa hệ thống.
- "UML process-oriented, không product-oriented": mô hình hóa *quy trình*, không phải sản phẩm.

## Điều cần tránh (Anti-patterns)
- **Tự động hóa mà không hiểu quy trình**: dẫn tới "bê nguyên" quy trình cũ lên hệ mới, không có tối ưu, người dùng không gặt được lợi ích của phần mềm đóng gói.
- **BA không truyền đạt được phát hiện cho đội hệ thống**: vấn đề thường gặp; UML sinh ra để giải quyết đúng khoảng cách giao tiếp này.

## Bảng tham chiếu (Reference Tables)
Ký pháp mô hình hóa nghiệp vụ UML (Table 1 trong sách):

| Icon/Phần tử | Định nghĩa UML |
|---|---|
| Business actor | Bên ngoài doanh nghiệp, tương tác với doanh nghiệp |
| Business worker | Vai trò bên trong, thao tác business entity |
| Business entity | "Thứ" được worker xử lý/dùng |
| Business use case | Chuỗi hành động tạo kết quả có giá trị cho actor |
| Organizational unit | Tập worker/entity/quan hệ, để chia nhỏ mô hình |

Sơ đồ UML và góc nhìn (Table 2):

| Sơ đồ | Mô tả |
|---|---|
| Use Case Diagram | Bối cảnh nghiệp vụ (business context) |
| Activity Diagram | Luồng công việc (business workflows) |
| Class Diagram | Cấu trúc tĩnh trong doanh nghiệp |
| Sequence Diagram | Tương tác giữa một bước quy trình và các đối tượng |

*Lưu ý trích xuất: Figure 1–2 (Business Use Case, Role Activity Diagram) là hình ảnh bị làm phẳng; mục 12.6 UML Sequence Diagram gần như bị cắt mất khi trích text (chỉ còn đoạn đuôi về mô tả workflow/vai trò).*

## Ví dụ minh họa (Worked Example)
**Business Use Case cho quy trình bán hàng** (Figure 1 trong sách): quy trình khởi đầu bằng *sales inquiry* (yêu cầu hỏi hàng) từ khách; nhà cung cấp đáp lại bằng *quotation* (báo giá); dẫn tới *order* (đơn hàng) từ khách; sau đó *delivery* và *invoicing* của nhà cung cấp. Quy trình có hai loại actor đóng hai vai trò khác nhau: **Customer Role** và **Supplier Role**, với chuỗi bước: **Inquire → Quote → Order → Deliver**.

Khi vẽ **Activity Diagram** cho cùng quy trình, các hoạt động được gán cho vai trò tương ứng với actor trong use case và đặt vào các **swimlanes** ngăn bởi đường gạch dọc — một diagram chia hoạt động theo vai trò như vậy chính là **Role Activity Diagram**, trả lời "ai chịu trách nhiệm làm gì".

## Điểm cần nhớ (Key Takeaways)
1. UML là cầu nối BA ↔ system analyst: một ký pháp chung cho cả nghiệp vụ và hệ thống.
2. Năm phần tử nghiệp vụ: Business actor, worker, entity, use case, organizational unit.
3. Bốn sơ đồ ↔ bốn góc nhìn: Use Case (bối cảnh), Activity (luồng), Class (cấu trúc tĩnh), Sequence (tương tác).
4. Swimlanes trong activity diagram thể hiện vai trò và trách nhiệm — ai làm gì.
5. Hiểu quy trình trước → reengineering; không hiểu → chỉ automation, không tối ưu.

## Ứng dụng cho BA ERP (BA Application)
- Với mỗi chức năng trong tài liệu ERP, kèm đủ bộ sơ đồ UML: **Use Case** (bối cảnh & actor), **Activity + swimlanes** (luồng và phân vai trò), **Class** (entity & quan hệ), **Sequence** (tương tác các bước) — đúng mức "chi tiết để code được ngay".
- Phân biệt rõ **business actor** (ngoài) và **business worker/role** (trong) để liệt kê đầy đủ vai trò nào có chức năng, vai trò nào chỉ thao tác một phần — đáp ứng yêu cầu "những role nào có chức năng đó".
- Dùng **business use case** (chuỗi bước tạo giá trị cho actor) làm đơn vị để phân tách nghiệp vụ thành các luồng nhỏ hơn.
- Vẽ business model trước để elicit yêu cầu tốt hơn và phát hiện cơ hội reengineering, tránh chỉ tự động hóa quy trình cũ.
- Mượn mẫu quy trình bán hàng Inquire→Quote→Order→Deliver làm khung chuẩn khi mô hình hóa luồng Quote-to-Cash trong ERP.

## Liên hệ (Connects To)
- **Ch 8 (CRM)**: quy trình Quote-to-Cash, các điểm chạm khách hàng cần mô hình hóa.
- **Ch 9 (.NET)**: business rules & roles cần mô hình hóa trước khi hiện thực.
- **Ch 11 (Case Studies)**: nhiều câu hỏi yêu cầu "mô tả quy trình bằng business model".
- **BPR / Reengineering**: UML hỗ trợ phân tích để tái cấu trúc, không chỉ tự động hóa.
