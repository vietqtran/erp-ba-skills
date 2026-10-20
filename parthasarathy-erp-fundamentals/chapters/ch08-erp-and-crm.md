# Chương 8: ERP và CRM (ERP and CRM)

## Ý tưởng cốt lõi (Core Idea)
**Customer Relationship Management (CRM)** — quản trị quan hệ khách hàng là phần "front-office" mở rộng của ERP, hướng ra bên ngoài tới khách hàng. Lý thuyết nền tảng của CRM: nhận diện khách hàng sinh lời, thu hút và giữ chân họ, tối đa hóa vòng đời hữu ích và lợi nhuận từ họ — đồng thời loại bỏ khách hàng không mong muốn. ERP làm back-office, CRM làm front-office; ghép lại mang lại giá trị lớn hơn.

## Framework được giới thiệu (Frameworks Introduced)
- **Three components of CRM** — ba thành phần CRM.
  - **Operational CRM**: tự động hóa quy trình nghiệp vụ, tích hợp front-office và back-office.
  - **Analytical CRM**: phân tích dữ liệu, sinh báo cáo ra quyết định; dùng data mining và data warehousing.
  - **Collaborative CRM**: các kênh cộng tác (email, chat, website, e-community, e-commerce, e-business).
- **Three dimensions/perspectives of CRM** — ba góc nhìn: **Business** (nhận diện, hiểu, dự đoán hành vi khách để xây chiến lược), **Technology** (nền tảng Data Mining/Data Warehousing/OLAP), **Customer** (tập trung vào mọi điểm tương tác, mức tùy biến dịch vụ).
- **Customer requirement classification** — phân loại yêu cầu khách hàng: **Normal**, **Expected**, **Exciting requirements** (bình thường / kỳ vọng / gây thích thú).
- **CRM success factors** — các yếu tố thành công: xây chiến lược lấy khách hàng làm trọng tâm *trước* khi chọn công nghệ; làm prototype & business model; kiến trúc khả mở rộng; nhìn CRM từ ba góc Business–Technology–Customer.

## Khái niệm chính (Key Concepts)
- **Data Warehouse** — kho dữ liệu: tập dữ liệu hướng chủ đề, tích hợp, biến thiên theo thời gian, không biến đổi, phục vụ quyết định quản lý; dành cho phân tích "off-line", không phải giao dịch hằng ngày.
- **Data Mining** — khai phá dữ liệu: quá trình phát hiện hiệu quả các mẫu giá trị, không hiển nhiên, từ khối dữ liệu lớn.
- **OLAP (Online Analytical Processing)**: nền tảng phân tích cho analytical CRM.
- **360-degree view / touch points**: góc nhìn toàn cảnh khách hàng qua mọi điểm chạm.
- **Operational CRM vs Analytical CRM vs Collaborative CRM**: ba lớp bổ sung nhau để giữ khách cũ, thêm khách mới, định hình chiến lược marketing/giá.

## Mô hình tư duy (Mental Models)
- Coi CRM như "mặt tiền" của ERP: ERP là back-office xử lý giao dịch, CRM là front-office quản lý tiếp xúc trước–trong–sau bán hàng.
- "Không phải khách hàng nào cũng ngang nhau": ưu tiên nguồn lực cho khách sinh lời (tối ưu profitability), đây là mục tiêu tối thượng của CRM.
- Ghi nhận nhu cầu khách thôi là chưa đủ: phải phân tích → truyền đạt tới các cấp nhân viên → sinh kế hoạch hành động khắc phục.

## Điều cần tránh (Anti-patterns)
- **Chọn công nghệ trước, chiến lược sau**: phải có chiến lược lấy khách hàng làm trọng tâm trước khi quyết định công nghệ.
- **Bỏ qua văn hóa và tổ chức**: "CRM sẽ thất bại nếu văn hóa và tổ chức doanh nghiệp không nằm trong kế hoạch".
- **Lưu dữ liệu vô dụng**: tích trữ dữ liệu không cần thiết gây lãng phí thời gian và tiền bạc.

## Bảng tham chiếu (Reference Tables)
Kỹ thuật thường dùng trong Data Mining (bối cảnh CRM):

| Kỹ thuật | Bản chất |
|---|---|
| **Neural networks** | Mô hình phi tuyến phức tạp mô phỏng nơ-ron người |
| **Rule induction** | Trích luật if-then hữu ích dựa trên ý nghĩa thống kê |
| **Evolutionary programming** | Tự hình thành giả thuyết về phụ thuộc biến mục tiêu |
| **Case based reasoning** | Dự báo/ra quyết định theo tình huống gần nhất (nearest neighbour) |
| **Decision trees** | Biểu diễn tập quyết định, phân lớp dữ liệu |
| **Genetic algorithms** | Sinh & kiểm thử tổ hợp tham số tìm lời giải tối ưu |
| **Nonlinear regression** | Mô hình không giả định quan hệ tuyến tính |

*Lưu ý trích xuất: tiêu đề mục 8.5 (sản phẩm SYSPRO CRM) bị mất khi trích text, dù nội dung còn.*

## Ví dụ minh họa (Worked Example)
**Giải pháp nghiệp vụ ERP-CRM Compiere** (mã nguồn mở, J2EE, chạy Windows/Linux) minh họa các chức năng một hệ ERP-CRM tích hợp cần có:
- **Authentication**: phân loại người dùng, cấp user id/password riêng, admin kiểm soát toàn bộ.
- **Quote to Cash**: báo giá → quản lý đơn → xuất hóa đơn → thu tiền, tích hợp với SCM và quản lý khách.
- **Requisition to Pay**: tạo yêu cầu mua → đơn mua → nhận hóa đơn → xử lý thanh toán.
- **Customer service / Partner Relations Management (PRM) / Supply Chain Management / Report generation / Internet enabled**.

Hai câu hỏi định hướng của một giải pháp ERP-CRM: "Chúng ta nhìn thấy khách hàng rõ đến đâu?" và "Khách hàng nhìn thấy chúng ta rõ đến đâu?" — mục tiêu là khả năng nhìn thấy nhau không rào cản (barrier-free visibility).

## Điểm cần nhớ (Key Takeaways)
1. CRM = front-office của ERP; mục tiêu là tối ưu profitability qua việc giữ khách sinh lời.
2. Ba thành phần: Operational / Analytical / Collaborative CRM — thiết kế đủ cả ba.
3. Nhìn CRM từ ba góc Business / Technology / Customer; đừng chỉ nghiêng về công nghệ.
4. Analytical CRM dựa trên Data Warehouse + Data Mining + OLAP để biến dữ liệu thành quyết định.
5. Thành công CRM bắt đầu từ chiến lược + văn hóa, không phải từ công cụ.

## Ứng dụng cho BA ERP (BA Application)
- Khi đặc tả module CRM, tách rõ ba thành phần Operational/Analytical/Collaborative và ánh xạ mỗi chức năng vào đúng thành phần để không bỏ sót (ví dụ báo cáo phân tích thuộc Analytical, email/chat thuộc Collaborative).
- Dùng khung ba góc nhìn Business/Technology/Customer làm checklist nghiệm thu: mỗi yêu cầu CRM phải trả lời được "phục vụ góc nhìn nào".
- Phân loại yêu cầu khách theo Normal/Expected/Exciting để ưu tiên tính năng trong backlog.
- Khi thiết kế tích hợp ERP↔CRM, đặc tả các quy trình xuyên suốt như Quote-to-Cash và Requisition-to-Pay với dòng dữ liệu giao dịch liền mạch, kèm phân quyền (users chỉ thấy dữ liệu được phép) như một business rule bảo mật.
- Đưa phân quyền báo cáo và tính toàn vẹn/bảo mật dữ liệu khách hàng thành tham số hệ thống rõ ràng trong spec.

## Liên hệ (Connects To)
- **Ch 7 (SCM)**: CRM và SCM đều là mở rộng hướng ngoại của ERP; Compiere tích hợp cả hai.
- **Ch 9 (ERP và .NET)**: Microsoft Dynamics CRM, tích hợp Outlook/Excel, báo cáo qua SQL Server.
- **Ch 10 (ERP Vendors)**: mySAP CRM từ SAP với 5 mảng (Marketing, Sales, Service, E-commerce, Channel management).
