# Chương 14: ERP và Thương mại điện tử (ERP and Electronic Commerce)

## Ý tưởng cốt lõi (Core Idea)
ERP là một trong những **building block** (khối nền tảng) chính của thương mại điện tử: nó là kho dữ liệu real-time trung tâm (tồn kho, giá, cấu hình sản phẩm). Ba khối nền là **ERP (thông tin) + mạng truyền thông (EDI/WFT) + user access (Internet/browser)**; chúng gắn chặt nhau. ERP đóng vai trò trong hàng loạt sáng kiến e-commerce: tra cứu/đặt hàng của khách, vendor-managed inventories, build to order, liên kết reseller, merge in transit.

## Framework được giới thiệu (Frameworks Introduced)
- **Ba building block của e-commerce**:
  - **ERP = kho thông tin trung tâm**: "clearing house" real-time; cung cấp tồn kho, giá, cấu hình sản phẩm cho MRP (từ x thành phẩm suy ra toàn bộ vật tư cần). "ERP is a building block of E-business" (3Com).
  - **Communication networks — EDI vs WFT**: **EDI (Electronic Data Interchange)** trao đổi "chunk" chuẩn (invoice) theo định dạng chuẩn, qua **VAN (value-added network)**; dùng khi nhiều giao dịch, cho firm lớn; bền nhưng cứng (ép process/artifact, nối tiếp, đắt). **WFT (Web Forms Technology)** khách điền form trên Internet/intranet/extranet; dùng khi ít giao dịch; nhưng nếu originator nhiều giao dịch thì WFT gây nhập liệu gấp đôi.
  - **Widely available, easy-to-use user access**: truy cập ERP qua Internet/browser; giải pháp **time-shared client** (user chỉ cần browser + Internet, client chạy trên server chuẩn) + **ERP portals** (J.D. Edwards ActiveEra, SAP) cá nhân hóa truy cập.
- **ERP và đặt hàng của khách** — mô hình Cisco ba mức: (1) khách **tra cứu** giá/cấu hình/trạng thái đơn 24/7 (chuyển customer support sang khách); (2) khách **đặt hàng qua Internet** với **configuration engine (CE)** bắt lỗi (sai part number) — không cho đặt nếu có lỗi; (3) **download thông tin vào hệ purchasing** của khách lớn (1 lần/ngày) để khỏi nhập đôi.
- **Vendor-Managed Inventories (VMI)** — chuyển việc đặt hàng từ khách sang nhà cung cấp (P&G giữ hàng trên kệ). Hai giải pháp: **integrating via common data** (cho vendor truy cập data warehouse/EDI feed) và **direct ERP-to-ERP connection** (Colgate cắm R/3 vào hệ nhà cung cấp) — nhưng cần chung một phần MAPs mới tích hợp thật.
- **Build to Order (BTO)** vs **Build to Forecast (BTF)** — BTF dự báo rồi sản xuất (dễ lỗi thời với sản phẩm thay nhanh); BTO chỉ sản xuất khi có đơn, giữ tồn kho ở dạng nguyên vật liệu, "thay tồn kho bằng công nghệ IT"; cần configuration engine + ERP real-time; đích đến là ERP-to-ERP không có con người.
- **Merge in Transit (MIT)** — gom hàng từ nhiều điểm xuất, hợp nhất **khi đang vận chuyển** thành một lô giao khách (merging/forwarding hoặc synchronization). Dell: màn hình từ nhà sản xuất tới điểm UPS trùng lúc với máy tính → một lô, Dell không bao giờ ôm tồn kho màn hình.

## Khái niệm chính (Key Concepts)
- **Configuration engine (CE)**: cỗ máy kiểm tra đơn hàng, chặn lỗi phổ biến (sai part number), liệt kê linh kiện cần để build (bộ nhớ, ổ cứng); lõi của cả web-ordering lẫn BTO.
- **Premier Pages (Dell)**: view có mật khẩu cho khách doanh nghiệp, nằm giữa website công khai và giải pháp ERP tích hợp hoàn toàn.
- **Time-shared client / Citrix**: cửa sổ trên máy khách chạy client đặt ở server; khôi phục mô hình time-sharing, bỏ chuẩn hóa client, chỉ cần browser.
- **MAPs chung để tích hợp**: hai ERP chỉ tích hợp thật nếu dùng chung một phần MAPs cho các giao dịch liên quan.

## Mô hình tư duy (Mental Models)
- Chọn EDI khi khối lượng giao dịch lớn và đối tác lớn; chọn WFT khi originator ít giao dịch còn bên nhận nhiều; kết hợp EDI-over-Internet để giảm chi phí VAN.
- Xem mở quyền truy cập ERP là đánh đổi: tăng độ chính xác và quan hệ khách hàng (84% IT manager thấy cải thiện) đổi lấy rủi ro security, lộ "cửa sổ" vào quy trình (khách thấy mình phản hồi nhanh/chậm), và tải query làm tụt hiệu năng ERP.
- "Dùng hệ thống cho việc giao dịch, để dành con người cho quan hệ và hỗ trợ" — chi phí biên mỗi query gần bằng 0.

## Điều cần tránh (Anti-patterns)
- **Dựa WFT khi originator có nhiều giao dịch**: gấp đôi thời gian nhập liệu (nhập cho vendor rồi lại cập nhật hệ của mình), tốn thêm người.
- **Khóa cứng vào EDI chuẩn**: ép process/artifact không tối ưu, hạn chế thay đổi theo thời gian, chi phí VAN cao.
- **Nối trực tiếp hai ERP mà không chuẩn hóa MAPs**: không tích hợp thật, phải làm thêm lớp tích hợp.
- **Mở truy cập mà không tính tải và security**: query Internet lớn kéo tụt hiệu năng nội bộ (chỉ 21% firm high-tech cho truy cập account online dù 97% có website).

## Ví dụ minh họa (Worked Example)
**Cisco — từ fax lỗi tới 85% đơn online**:
- Vấn đề: 25–33% đơn đặt qua fax có lỗi (sai cấu hình/part number) → trễ ship hoặc đổi giá → khách phải gọi lại → Cisco phải tăng người trả lời, chi phí tăng, giao hàng chậm.
- 1996: xây app e-commerce đầu cho khách tự tra giá/cấu hình/trạng thái đơn 24/7 → giảm nhu cầu nhân sự theo dõi đơn.
- Năm 2: cho khách tự đặt "anytime, anywhere" qua Internet; **configuration engine** chặn lỗi, không cho đặt nếu sai → Cisco **bảo đảm** giá và cấu hình chính xác nếu khách dùng web. Trong 4 tháng 10% đơn qua Internet; tới 1999 là 85%. Đơn vào ERP trong ≤15 phút sẵn sàng để khách theo dõi, và Cisco bắt đầu sản xuất ngay trong 15 phút đó.
- 1998: tích hợp thông tin đơn vào hệ purchasing của khách lớn (cập nhật 1 lần/ngày) → khách đặt từ hệ quen, không nhập đôi.

**USC Leventhal — truy cập ERP qua Citrix** (Appendix 14-1): triển khai J.D. Edwards **OneWorld** bản client server (bỏ bản demo vì dữ liệu kẹt trên một máy lab). OneWorld là phần mềm "just-in-time" trên Windows NT, **deployment server** tự tải module khi cần — nhưng trong lớp học sinh viên chạm mọi module nên thành "obese client". Vấn đề: nhiều lớp security không có đầu mối trung tâm; **ODBC driver** tĩnh, cứ nâng cấp là xung đột; chỉ có 2 máy đủ mạnh, lại giới hạn giờ thư viện. Giải pháp **Citrix server** (chạy tới 20 client trên một máy, ~$2.000/user): sinh viên chỉ cần browser + Internet (Linux/Mac/Windows 3.1 đều được), truy cập 7×24 từ bất kỳ đâu; nâng cấp chỉ sửa ở server + 1 client; hết lo kích thước client và ODBC; chỉ cần lo security cho client và server. "Cứu bàn thua" khi tòa nhà mới chưa có network.

## Điểm cần nhớ (Key Takeaways)
1. ERP là kho dữ liệu real-time trung tâm — nền tảng để e-commerce chính xác (tồn kho, giá, cấu hình).
2. EDI cho khối lượng lớn/đối tác lớn; WFT cho ít giao dịch; cả hai đang hội tụ trên Internet để giảm chi phí.
3. Configuration engine là lõi bắt lỗi của web-ordering và BTO; chính xác đầu vào loại bỏ ill-will và chi phí xử lý lỗi.
4. VMI và BTO dịch chuyển vai trò đặt hàng/giữ tồn kho; tích hợp ERP-to-ERP cần MAPs chung.
5. Time-shared client (Citrix) và ERP portal mở rộng truy cập mà giảm chuẩn hóa ở phía client.

## Ứng dụng cho BA ERP (BA Application)
- Khi đặc tả tích hợp/e-commerce, ghi rõ chọn EDI hay WFT theo khối lượng giao dịch và quy mô đối tác, kèm cảnh báo double data-entry của WFT và chi phí VAN của EDI.
- Thiết kế **configuration engine** như một thành phần bắt lỗi đầu vào (sai part number, cấu hình không hợp lệ) với quy tắc "không cho đặt nếu còn lỗi" — đây là business rule cụ thể cho module đặt hàng.
- Với yêu cầu tích hợp ERP-to-ERP (VMI, BTO), đưa điều kiện tiên quyết "chung một phần MAPs cho các giao dịch liên quan" vào spec, nếu không phải đặc tả thêm lớp tích hợp.
- Đặc tả MIT cần business rule đặc thù: một purchase order và một invoice dù hàng xuất từ nhiều nơi; ERP phải hạch toán bán hàng không bao giờ "nhập kho"; các điểm truyền tin qua EDI.
- Khi viết yêu cầu mở truy cập ERP ra ngoài, thêm mục NFR về security (bảo vệ hệ, dữ liệu, truyền tin), về tải query ảnh hưởng hiệu năng nội bộ, và về mức dữ liệu nào được phép lộ ("cửa sổ" vào quy trình).

## Liên hệ (Connects To)
- **Ch 4**: ERP portals và web access là nền của truy cập e-commerce.
- **Ch 6**: data warehouse làm nguồn dữ liệu chung cho VMI.
- **Ch 10**: MAPs chung là điều kiện để tích hợp ERP-to-ERP.
- **Ch 12**: mở truy cập làm phát sinh bottleneck hiệu năng và nhu cầu hardware sizing.
- **EDI / Merge in Transit / Build to Order**: các chuẩn và mô hình chuỗi cung ứng.
