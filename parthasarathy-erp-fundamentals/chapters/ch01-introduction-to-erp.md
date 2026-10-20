# Chương 1: Giới thiệu về ERP (Introduction to ERP)

## Ý tưởng cốt lõi (Core Idea)
**Enterprise Resource Planning (ERP)** — hoạch định nguồn lực doanh nghiệp — là một phần mềm đóng gói (packaged software) tích hợp mọi phòng ban và chức năng của doanh nghiệp vào **một chương trình duy nhất chạy trên một cơ sở dữ liệu chung**, để các phòng ban chia sẻ thông tin theo thời gian thực. Tác giả nhấn mạnh: giá trị thật nằm ở chữ "enterprise" (tích hợp toàn doanh nghiệp), chứ không phải ở "planning" hay "resource".

## Framework được giới thiệu (Frameworks Introduced)
- **Four direct benefits of ERP** — bốn lợi ích trực tiếp: **Business Integration** (tích hợp nghiệp vụ), **Flexibility** (linh hoạt), **Better Analysis & Planning Capabilities** (năng lực phân tích/hoạch định), **Use of Latest Technology** (dùng công nghệ mới nhất).
  - Khi dùng: để lý giải vì sao triển khai ERP, và làm thang đo lợi ích.
  - Cách hiểu: *Integration* = dữ liệu của các nghiệp vụ liên quan được **tự động cập nhật ngay khi phát sinh giao dịch** (automatic data updation); *Flexibility* = một hệ thống xử lý được nhiều ngôn ngữ, tiền tệ, chuẩn kế toán, nhiều địa điểm.
- **Key traits of an ERP solution** — các đặc tính cốt lõi: Scalability (khả năng mở rộng), Vendor management, Functionality, Reliable service & support, Integrated modules.
- **What a fully integrated ERP covers** — tiêu chí một ERP tích hợp đầy đủ: giảm độ phức tạp quy trình; đáp ứng yêu cầu; có "ways of working" chung (dùng quy trình chuẩn cho giao dịch); tuân thủ bộ chuẩn tài chính và mã sản phẩm chung; tích hợp các chức năng nội bộ chính (finance, distribution, manufacturing, sales, HR).

## Khái niệm chính (Key Concepts)
- **Integration**: ưu điểm số một; dữ liệu liên nghiệp vụ tự cập nhật khi có giao dịch, cho phép nắm thông tin real-time.
- **Lead-time**: thời gian từ lúc đặt hàng đến lúc nhận hàng; then chốt cho mua hàng và kiểm soát tồn kho.
- **Cycle time**: thời gian từ lúc nhận đơn đến lúc giao sản phẩm; ERP rút ngắn nhiều nhất với make-to-order.
- **Make-to-Stock / Make-to-Order**: ERP cho phép đổi phương pháp sản xuất/hoạch định mà không phải cấu hình lại nhà máy.
- **Back-office vs front-office**: ERP là hệ back-office (không trực tiếp với khách); CRM là front-office.
- **Information system**: tối thiểu gồm ba yếu tố — **people, procedures, data** (người theo quy trình để xử lý dữ liệu tạo ra thông tin).
- **APS (Advanced Planning & Scheduling)**: hệ "thông minh" có mô hình hóa/phân tích — tương phản với ERP thiên về ghi nhận giao dịch.

## Mô hình tư duy (Mental Models)
- Coi ERP là **"suite" các module phối hợp liền mạch**, không phải các ứng dụng rời; có thể mua và triển khai từng module (modularity), nhưng khi ghép lại chúng tự động khớp nhau.
- Coi ERP là **tập hợp best practices** gắn trong phần mềm: muốn hưởng lợi thì con người phải thay đổi theo cách làm việc của phần mềm, không phải bắt phần mềm chạy theo thói quen cũ.
- ERP chủ yếu "ghi lại những gì đã xảy ra" (transaction-based), không "lập kế hoạch cho tương lai" — nên đừng kỳ vọng nó tự ra quyết định như hệ intelligence-based.

## Điều cần tránh (Anti-patterns)
- **Customize lõi ERP theo thói quen cũ**: làm phần mềm bất ổn, khó bảo trì; đây là nguyên nhân phổ biến của các "horror stories" và thất bại dự án.
- **Xem ERP chỉ là công cụ cắt giảm chi phí**: gây kháng cự trong tổ chức và không đạt cải thiện như hứa hẹn.
- **Triển khai ERP tùy tiện chỉ để "làm mới hệ thống"**: dễ biến ưu điểm thành nhược điểm.
- **Culture clash**: áp best practice không phù hợp văn hóa tổ chức khiến hệ thống bị kháng cự.

## Ví dụ minh họa (Worked Example)
Tình huống tích hợp thông tin mà sách nêu: sau khi thay các hệ thống rời rạc (finance, HR, manufacturing, warehouse) bằng một ERP thống nhất chia thành các module, **người ở phòng finance có thể tra cứu phần mềm warehouse để xem một đơn hàng đã được giao chưa** — điều không thể làm với các hệ độc lập trước đây. Với ERP web-enabled, khách hàng tự **đặt hàng, theo dõi trạng thái đơn và thanh toán tại nhà**; nhân viên technical support thấy đầy đủ thông tin sản phẩm và khách hàng nên hỗ trợ tốt hơn. Đây là minh họa trực tiếp cho lợi ích Business Integration + Use of Latest Technology.

## Điểm cần nhớ (Key Takeaways)
1. ERP = một phần mềm tích hợp + một CSDL chung phục vụ mọi phòng ban; đừng bị chữ "planning/resource" đánh lừa.
2. Bốn lợi ích trực tiếp: Business Integration, Flexibility, Better Analysis & Planning, Use of Latest Technology.
3. Giới hạn của ERP: phạm vi một doanh nghiệp, chậm, transaction-based (không thông minh), cứng nhắc với workflow riêng.
4. Rủi ro triển khai: user resistance/revolt, culture clash, cascading errors, repetition of errors, concentration of data.
5. Dự án ERP "gãy" khi doanh nghiệp sửa lõi phần mềm để chiều thói quen cũ thay vì đổi cách làm việc.

## Ứng dụng cho BA ERP (BA Application)
- Khi viết tài liệu, luôn mô tả **luồng dữ liệu tự động cập nhật liên module** (một giao dịch cập nhật mọi nghiệp vụ liên quan), vì đó mới là bản chất ERP — không mô tả từng chức năng như ốc đảo rời rạc.
- Ghi rõ chức năng hỗ trợ đa phương thức sản xuất (make-to-stock / make-to-order / assemble-to-order) thay vì cố định một kiểu, để spec linh hoạt đúng chuẩn ERP.
- Phân loại rõ mỗi yêu cầu thuộc **back-office (ERP)** hay **front-office (CRM)** để tránh nhét nhầm phạm vi.
- Mỗi yêu cầu customization phải ghi lý do; mặc định ưu tiên dùng quy trình chuẩn của phần mềm để tránh bất ổn và chi phí bảo trì — nêu cảnh báo này ngay trong tài liệu.

## Liên hệ (Connects To)
- **Ch 2**: ERP tiến hóa từ MRP → MRP II; giới hạn "transaction-based" dẫn tới ERP II và SCM.
- **Ch 3**: các module Finance, HR, MM, Sales & Distribution hiện thực hóa tính tích hợp này.
- **Ch 5**: anti-pattern over-customization được phân tích sâu trong vòng đời triển khai.
