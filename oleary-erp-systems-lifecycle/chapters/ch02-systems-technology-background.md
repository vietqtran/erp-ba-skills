# Chương 2: Nền tảng hệ thống và công nghệ (Systems and Technology Background)

## Ý tưởng cốt lõi (Core Idea)
ERP là phần mềm, nên hiểu ERP phải bắt đầu từ các nền tảng: điện toán (mainframe vs client server), mạng, cơ sở dữ liệu (flat file vs quan hệ), phần mềm đóng gói (package software), lựa chọn phần mềm và tái cấu trúc. Hai lựa chọn nền tảng định hình cách viết spec: **relational database** (một dữ liệu, một nơi) và **package software** cấu hình bằng tham số thay vì lập trình lại.

## Framework được giới thiệu (Frameworks Introduced)
- **"As Is" versus "To Be"** — mô hình hiện trạng so với mô hình tương lai. Khung mô hình hóa quy trình để làm cơ sở chọn phần mềm.
  - Khi nào dùng: khảo sát yêu cầu, làm rõ quy trình hiện tại ("as is") và quy trình mong muốn ("to be") trước khi chọn/cấu hình ERP.
  - Cách làm: dựng mô hình quy trình hiện tại, dựng mô hình quy trình đích, dùng khoảng cách giữa hai mô hình để quyết định đổi phần mềm hay đổi quy trình.
- **Best Practices versus Obliteration** — thông lệ tốt nhất so với "xóa sạch làm lại" (theo Hammer 1990). Hai triết lý tái cấu trúc.
  - Khi nào dùng: chọn hướng tái thiết kế quy trình. "Obliteration" (xóa bỏ rồi làm lại) thường thất bại vì không biết thay bằng gì; "best practices" được chấp nhận rộng vì tái dùng quy trình đã biết là chạy được.
- **Switch Setting (Parameterization)** — thiết lập tham số/công tắc phần mềm. Cách cấu hình package software mà không cần lập trình lại.
  - Khi nào dùng: khi spec cần nêu chức năng bật/tắt hoặc tham số hệ thống cho một module.

## Khái niệm chính (Key Concepts)
- **Client server computing**: phân tán tính toán/lưu trữ giữa máy khách (client) và máy chủ (server); kiến trúc ba lớp (**three-tier**) tách server ứng dụng, CSDL và giao diện.
- **Thin/fat client**: client yếu (xử lý chủ yếu ở server) vs client mạnh (xử lý nhiều tại chỗ).
- **Flat file database**: tệp hai chiều (hàng/cột), không liên kết, dễ dùng nhưng dư thừa dữ liệu cao.
- **Relational database**: tập bảng liên kết nhau qua khóa tham chiếu; loại bỏ dư thừa, mô hình hóa linh hoạt mọi sự kiện doanh nghiệp.
- **Data warehouse**: kho dữ liệu lớn tối ưu cho truy vấn nhanh, thường chứa nhiều năm giao dịch để phân tích xu hướng.
- **Package software**: phần mềm dựng cho nhiều tổ chức dùng chung; chọn trong danh mục năng lực bằng tham số, không lập trình lại.
- **Legacy software**: phần mềm cũ, thường tự phát triển riêng cho doanh nghiệp, chi phí bảo trì cao.
- **DBMS**: hệ quản trị CSDL cung cấp truy vấn và trình sinh báo cáo; sau triển khai gần như không đổi được DBMS.
- **LAN / Intranet / Extranet**: mạng cục bộ / WAN nội bộ doanh nghiệp / WAN cho doanh nghiệp và đối tác.

## Mô hình tư duy (Mental Models)
- Coi **relational database** là lý do kỹ thuật khiến "nhập một lần" khả thi: thiết kế dữ liệu trong spec nên chuẩn hóa theo bảng + khóa, không sao chép dữ liệu.
- Cấu hình ERP = chọn trong danh mục năng lực có sẵn qua tham số; mặc định ưu tiên "switch setting" trước khi nghĩ tới tùy biến mã.
- Chọn phần mềm nên dựa trên **cost–benefit / ROI**, nhưng lưu ý lợi ích thường "mờ" và chi phí có thể bị ẩn, dữ liệu đáng tin chỉ có sau ~1 năm chạy.

## Điều cần tránh (Anti-patterns)
- **Thiết kế dữ liệu kiểu flat file**: lặp lại thông tin người bán/khách ở mỗi dòng giao dịch, gây dư thừa và lỗi cập nhật.
- **Tùy biến mã khi chỉ cần đặt tham số**: tùy biến làm tăng chi phí và cản trở nâng cấp phiên bản.
- **Obliteration mà không có mô hình "to be"**: phá quy trình cũ nhưng không biết thay bằng gì.

## Bảng tham chiếu (Reference Tables)
Phân biệt hai loại nền tảng phần mềm:

| Tiêu chí | Legacy software | Package software (ERP) |
|---|---|---|
| Phạm vi | Riêng cho một doanh nghiệp | Dùng chung nhiều tổ chức |
| Thay đổi năng lực | Lập trình lại | Đặt tham số / switch setting |
| Bảo trì/tiến hóa | Nội bộ, chi phí cao | Giao cho vendor (mua "tầm nhìn" của vendor) |
| Phụ thuộc | Nhân sự phân tích/lập trình riêng | Kiến thức về gói phần mềm |

## Ví dụ minh họa (Worked Example)
Sách minh họa dư thừa dữ liệu bằng hệ thống bán hàng: với flat file, mỗi lần một nhân viên bán hàng tạo đơn, toàn bộ thông tin của họ (địa chỉ, số định danh...) bị ghi lại — cùng người bán nhiều đơn thì lặp lại toàn bộ. Cách chuẩn hóa: tách bảng, chỉ lưu *số nhân viên/khách hàng* trên đơn và tra cứu chi tiết ở bảng liên kết khi cần. Khi thêm mặt hàng vào đơn, thêm một dòng mới cho mỗi mặt hàng (không cần dự trù trước số dòng). Đây là tư duy chuẩn hóa bảng mà spec dữ liệu ERP cần tuân theo.

## Điểm cần nhớ (Key Takeaways)
1. ERP dựa trên CSDL quan hệ: spec dữ liệu phải chuẩn hóa, dùng khóa tham chiếu, tránh dư thừa.
2. Ưu tiên cấu hình bằng tham số/switch setting trước khi đề xuất tùy biến mã.
3. Dùng mô hình "as is" / "to be" làm cơ sở khảo sát và chọn giải pháp.
4. Best practices thắng obliteration vì có sẵn và đã được kiểm chứng.
5. DBMS và kiến trúc ba lớp là ràng buộc kỹ thuật ảnh hưởng tới khả năng nâng cấp — ghi nhận như một NFR.

## Ứng dụng cho BA ERP (BA Application)
- Trong spec dữ liệu (danh mục/master data), mô tả quan hệ bảng và khóa tham chiếu thay vì liệt kê trường phẳng — bảo đảm mỗi thực thể (khách hàng, vật tư, nhà cung cấp) chỉ định nghĩa một lần.
- Với mỗi chức năng, liệt kê **tham số hệ thống** (switch setting) cần cấu hình và mặc định của chúng — phần "tham số hệ thống cho chức năng" mà tài liệu ERP cần có.
- Ghi mô hình "as is" và "to be" trong tài liệu khảo sát để làm căn cứ chống lệch yêu cầu.
- Ghi NFR nền tảng: kiến trúc client server/ba lớp, DBMS được hỗ trợ, bảo mật mạng (firewall, encryption) — vì các ràng buộc này cố định sau golive.

## Liên hệ (Connects To)
- **Chương 1**: tích hợp và nhập một lần là hệ quả của CSDL quan hệ.
- **Chương 4**: nhập liệu đầu vào chịu ảnh hưởng của thiết kế "từ database ra" thay vì "từ giao diện vào".
- **Chương 6**: best practices vs obliteration mở rộng thành technology enabled vs clean slate reengineering.
- **Chương 9**: đổi quy trình hay đổi phần mềm — nối tiếp "as is" / "to be".
