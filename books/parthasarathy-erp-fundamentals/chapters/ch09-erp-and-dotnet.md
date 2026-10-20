# Chương 9: ERP và .NET (ERP and .NET)

## Ý tưởng cốt lõi (Core Idea)
ERP là giải pháp chưa hoàn chỉnh: nó xử lý giao dịch tốt nhưng khó kết nối với thế giới bên ngoài (tài liệu, email, fax, web content) và không bao hết mọi "touch-point" nghiệp vụ. **Microsoft .NET** — nền tảng tính toán thế hệ mới dựa trên **XML Web services** là tầng công nghệ giúp ERP "bước ra khỏi bốn bức tường", tích hợp qua Internet bằng **managed code** (mã được quản lý). Kiến trúc ERP hiện đại thực chất là việc triển khai hiệu quả các quy tắc nghiệp vụ.

## Framework được giới thiệu (Frameworks Introduced)
- **Characteristic features of a perfect ERP system** — đặc trưng của một hệ ERP hoàn hảo.
  - Khi nào dùng: làm checklist kiến trúc khi xây/chọn ERP.
  - Gồm: 100% managed code; **standardized business rules**; gói validation rules cùng processing rules; **dynamic choreography of business rules** (điều phối động quy tắc nghiệp vụ); distributed processing; dễ tùy biến; hỗ trợ kết nối theo chuẩn; **loosely coupled** (ghép lỏng); phơi bày tập dữ liệu theo chuẩn ra ngoài; một điểm hội tụ cho dữ liệu đầu vào; giao tiếp theo sự kiện; dễ bảo trì; toàn vẹn dữ liệu.
- **Managed code benefits** — lợi ích của managed code: mạnh mẽ hơn, chạy song song nhiều phiên bản (side-by-side versions), bảo mật tốt hơn, kết nối tốt hơn, nhanh và dễ triển khai hơn, chi phí sở hữu thấp hơn.
- **.NET architecture (CLI / CLR / CIL)** — kiến trúc .NET: **Common Language Infrastructure (CLI)** (đặc tả môi trường runtime), **Common Language Runtime (CLR)** (lõi thực thi), mã trung gian **Common Intermediate Language (CIL/IL)**; lập trình viên viết bằng ngôn ngữ yêu thích → compiler .NET biên dịch sang IL → CLR thực thi; đối tượng chạy trên mọi OS hỗ trợ CLR + Framework.

## Khái niệm chính (Key Concepts)
- **Managed code**: mã nhẹ, nhanh, kháng hacker, dễ cài/gỡ; tránh xung đột kiểu cũ của **Component Object Model (COM)**; cho phép hai phiên bản chạy song song không xung đột.
- **SOAP (Simple Object Access Protocol)**: giao thức để các Web services giao tiếp qua Internet; đi qua firewall vì dùng HTTP.
- **XML Web services model**: nền tảng cho tích hợp ứng dụng hiện có (email, CRM, ERP, mainframe) thay vì viết mới toàn bộ.
- **Platform-independent target**: .NET là đích phát triển độc lập nền tảng, dựa hoàn toàn trên lập trình hướng thành phần.

## Mô hình tư duy (Mental Models)
- Coi .NET như "tầng software nằm trên OS" cách ly lập trình viên và người dùng khỏi khiếm khuyết/không tương thích của các hệ điều hành.
- Phát triển ứng dụng ngày nay chủ yếu là **tích hợp** ứng dụng sẵn có, không phải viết nhiều mã mới → chọn công nghệ hỗ trợ tích hợp cao.
- Kiến trúc ERP hiện đại = "cách đóng gói, gọi và phơi bày business rules"; đó là lý do .NET đáng để thiết kế lại ERP từ gốc.

## Điều cần tránh (Anti-patterns)
- **Để thông điệp cốt lõi chìm trong hype marketing**: khi mọi sản phẩm đều dán nhãn ".NET-this, .NET-that", ý nghĩa kỹ thuật thực sự (CLR + Framework) dễ bị pha loãng.
- **Nâng cấp "bộ mặt" lên công nghệ cũ**: mọi phần mềm vẫn phải được cài đặt ở đâu đó; cần hỏi vendor chính xác thành phần nào sẽ cài trên hạ tầng của mình.

## Bảng tham chiếu (Reference Tables)
Các lợi ích .NET cho ngành sản xuất (theo tác giả):

| Lợi ích | Diễn giải |
|---|---|
| Lower cost of system administration | Giảm chi phí quản trị hệ thống |
| Installed by copying files | Triển khai đơn giản bằng sao chép tệp |
| Reach and Rich at the same time | Vừa tiếp cận rộng (web) vừa trải nghiệm phong phú (client) |
| Better internal systems through better tools | Hệ thống nội bộ tốt hơn nhờ công cụ tốt hơn |

Cải thiện tốc độ xử lý đặc biệt hữu ích cho **MRP** và **CRP** (Capacity Requirements Planning), giúp lập kế hoạch sản xuất, theo dõi xưởng, hứa hẹn & phân tích trạng thái đơn hàng theo thời gian thực.

## Ví dụ minh họa (Worked Example)
**Intuitive ERP 6.0** — ERP đầu tiên trên kiến trúc 100% Microsoft .NET (Intuitive Manufacturing Systems, cho nhà sản xuất rời rạc SME). Mã nguồn kèm theo chi phí hệ thống (toàn quyền tùy biến), triển khai tự động từ một CD-ROM. Danh mục chức năng minh họa một ERP sản xuất đầy đủ: **Planning, Inventory, Engineering, Purchasing, Manufacturing, Finance, Quoting/Estimating, Order Processing, Advanced Configurator, Quality, Intuitive SPC (Statistical Process Control), Return Material Authorization, Forecasting, Payroll/HR, AlertMessenger, Project Management, Intuitive Mobile**. Ví dụ: *Engineering* tạo & duy trì bill of material đa cấp trực quan, quản lý dữ liệu sản phẩm, thiết kế routing, kiểm soát thay đổi kỹ thuật; *AlertMessenger* tự động gửi email/thông báo màn hình theo sự kiện hệ thống.

## Điểm cần nhớ (Key Takeaways)
1. ERP một mình là chưa đủ; cần tầng công nghệ (.NET/XML Web services) để tích hợp ra ngoài doanh nghiệp.
2. Managed code = nhanh, bảo mật, chạy song song phiên bản, TCO thấp — nền của ERP hiện đại.
3. Kiến trúc tốt của ERP xoay quanh việc chuẩn hóa và điều phối động business rules.
4. CLR + .NET Framework cho phép mã viết bằng nhiều ngôn ngữ chạy trên mọi nền hỗ trợ CLR.
5. Khi mua ERP, hỏi rõ thành phần phần mềm nào sẽ được cài trên hạ tầng của bạn.

## Ứng dụng cho BA ERP (BA Application)
- Dùng danh sách "đặc trưng ERP hoàn hảo" (managed code, standardized business rules, loosely coupled, data integrity...) làm checklist NFR kiến trúc trong tài liệu.
- Đặc tả business rules một cách tách bạch (validation rules riêng, processing rules riêng) để hỗ trợ "dynamic choreography" — giúp tài liệu đủ rõ để code mà không cần BA giải thích thêm.
- Khi spec có tích hợp liên hệ thống, nêu rõ cơ chế (XML Web services/SOAP qua HTTP) và các hệ cần tích hợp (email, CRM, mainframe) thay vì mô tả mơ hồ "tích hợp".
- Mượn danh mục chức năng của một ERP .NET (Planning, Inventory, Engineering...) làm khung tham chiếu để đảm bảo spec bao đủ chức năng chuẩn của ERP sản xuất.

## Liên hệ (Connects To)
- **Ch 6 (Operating System)**: managed code cách ly ứng dụng khỏi OS; chạy trên mọi nền hỗ trợ CLR.
- **Ch 8 (CRM)**: Intuitive CRM, Microsoft Dynamics CRM đều tích hợp qua nền Microsoft/.NET.
- **Ch 10 (ERP Vendors)**: Intuitive là một vendor; SAP/Oracle cũng áp dụng chuẩn web/XML.
- **Ch 12 (Business Modeling UML)**: business rules & roles cần được mô hình hóa trước khi code.
