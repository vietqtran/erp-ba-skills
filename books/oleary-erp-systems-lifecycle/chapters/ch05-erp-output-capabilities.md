# Chương 5: Năng lực đầu ra của ERP (ERP Output Capabilities)

## Ý tưởng cốt lõi (Core Idea)
Báo cáo ERP chuẩn thường *không đủ* đáp ứng nhu cầu người dùng. Có bốn hướng sinh đầu ra — **reports, database queries, intranet, data warehouse** — và gần đây là **portals** (desktop theo vai trò). BA phải lập kế hoạch đầu ra ngay từ đầu vì truy vấn nặng là "đám cháy công nghệ số một" sau golive.

## Framework được giới thiệu (Frameworks Introduced)
- **Four Output Alternatives** — bốn phương án tạo đầu ra khi báo cáo chuẩn không đủ:
  - (1) **Standard reports / database queries**: báo cáo dựng sẵn theo module; truy vấn ở hai cấp (trong ERP hoặc trong DBMS). Lưu ý: nhiều ERP coi query *là transaction*, truy vấn nhiều làm quá tải hệ thống.
  - (2) **Customized reports**: đúng nhu cầu nhưng ngắn hạn — nhu cầu đổi, người đổi, tốn chi phí, cản nâng cấp.
  - (3) **Intranet / Lotus Notes**: "spin off" báo cáo chuẩn ra môi trường dễ dùng cho người dùng thông thường; cùng nội dung nhưng mở rộng khả năng truy cập; tránh "seat cost".
  - (4) **Data warehouse**: kho tối ưu truy vấn; làm điểm trung chuyển (clearing house) cho ứng dụng thượng/hạ nguồn; cho phép **knowledge discovery** (phát hiện tri thức bằng thống kê/AI).
  - Khi nào dùng: chọn hướng đầu ra theo loại người dùng (expert vs casual) và loại truy vấn (chuẩn vs ad hoc).
- **ERP Portals (role-specific desktop)** — cổng/desktop theo vai trò: trang web (intranet/Internet) tập trung truy cập module con liên quan, báo cáo, help-desk, lịch, email, tin tức, và thương mại điện tử — kéo quyền kiểm soát thông tin về lại vendor.
  - Khi nào dùng: thiết kế màn hình chính theo *vai trò công việc* thay vì theo module.

## Khái niệm chính (Key Concepts)
- **Database query (hai cấp)**: truy vấn trong ERP, hoặc truy vấn trực tiếp CSDL (Oracle...) — tổ chức khai thác cấp mình mạnh.
- **Data warehouse**: kho dữ liệu tối ưu cho truy xuất, chứa nhiều năm giao dịch; có thể vật lý riêng hoặc "virtual".
- **Virtual data warehouse**: kho ảo — các phần dữ liệu nằm rải ở nhiều nơi/nhiều server, chiến lược multi-server để vừa giữ OLTP ổn định vừa báo cáo nhanh.
- **Knowledge discovery**: khai phá quan hệ giữa biến trong kho dữ liệu để tạo giá trị từ dữ liệu giao dịch (trước đây bị coi là chi phí chìm).
- **ERP portal**: website cung cấp truy cập thông tin liên quan ERP; hai dạng desktop-based và web server–based (ví dụ MySAP).

## Mô hình tư duy (Mental Models)
- Phân tầng người dùng: expert dùng trực tiếp ERP, casual/occasional dùng intranet/portal — thiết kế môi trường đầu ra khác nhau cho mỗi tầng.
- Coi query như transaction: mỗi báo cáo ad hoc là tải lên hệ thống ⇒ lập **capacity planning** cho đầu ra (phần cứng, mạng) ngay từ spec.
- Ưu tiên data warehouse/intranet hơn customized report cứng, vì nhu cầu và người dùng thay đổi liên tục.

## Điều cần tránh (Anti-patterns)
- **Xây nhiều customized report cứng vào hệ thống**: tốn kém, ngắn hạn, cản nâng cấp khi người/nhu cầu đổi.
- **Không lập kế hoạch đầu ra trước golive**: hàng trăm/nghìn người cùng kéo dữ liệu từ CSDL tích hợp gây quá tải — đám cháy số một sau golive.
- **Bắt mọi người dùng truy cập trực tiếp ERP**: tốn seat cost và khó dùng cho người dùng không chuyên.

## Bảng tham chiếu (Reference Tables)
Bốn phương án đầu ra — chọn theo bối cảnh:

| Phương án | Hợp với | Hạn chế chính |
|---|---|---|
| Standard reports / queries | nhu cầu chuẩn, người dùng chuyên | query nặng gây quá tải; báo cáo chuẩn có thể không đủ |
| Customized reports | nhu cầu cố định, cụ thể | ngắn hạn, tốn kém, cản nâng cấp |
| Intranet / Lotus Notes | người dùng casual, phổ cập báo cáo | chỉ "spin off" nội dung chuẩn, không linh hoạt |
| Data warehouse | truy vấn ad hoc, nhiều năm, phân tích | chi phí dựng & duy trì, cần nhân sự query |

Cổng của một số vendor (Table 5.1): J.D. Edwards — MyActivEra; Lawson — Insight II Seaport; PeopleSoft — MyWorld; SAP — MySAP.

## Ví dụ minh họa (Worked Example)
**Quantum's Virtual Data Warehouse (Phụ lục 5-1)** — Quantum triển khai Oracle Applications (tài chính + sản xuất) trên CSDL quan hệ Oracle, tạo ra hơn **40.000 bảng** nền. Số bảng khổng lồ khiến môi trường back-end quá phức tạp để người dùng ra quyết định; hệ thống có nguy cơ thành "kho thông tin giao dịch không ai dùng".

Giải pháp: dựng **virtual data warehouse** với ~**4.000 business views** đơn giản, hướng nghiệp vụ, phủ "next day" toàn bộ giao dịch; chiến lược multi-server giữ OLTP chạy liên tục song song với báo cáo nhanh. Kết quả: ~250 người dùng/ca, 23 giờ/ngày, 6 ngày/tuần, toàn cầu; một báo cáo trước đây cần 15 báo cáo khác nhau và 16 giờ nay gộp còn *một*.

Cách làm triển khai (bài học tổ chức cho BA): dùng tỉ lệ **50/50 giữa IS và business users** — business systems analyst tại mỗi site hiểu nhu cầu nghiệp vụ, dựng query, dạy lớp; lập trình viên/analyst vùng hỗ trợ kỹ thuật. Đội duy trì gồm program manager + 2 lập trình viên tư vấn + 2 business analyst + 1 technical trainer + 1 desktop support. Thách thức nổi lên: đào tạo toàn cầu (ngôn ngữ), phát triển năng lực truy cập dữ liệu, tích hợp nhiều hãng phần cứng/phần mềm/tư vấn, giữ nhịp dự án.

## Điểm cần nhớ (Key Takeaways)
1. Báo cáo chuẩn ERP thường không đủ — luôn chuẩn bị sẵn phương án query/intranet/data warehouse.
2. Query = transaction; phải capacity-plan cho đầu ra trước golive.
3. Phân tầng người dùng (expert vs casual) để chọn môi trường đầu ra và tiết kiệm seat cost.
4. Data warehouse không chỉ báo cáo mà còn là clearing house và nền knowledge discovery.
5. Thiết kế đầu ra đang dịch từ "report-focus" sang "role-specific desktop/portal".

## Ứng dụng cho BA ERP (BA Application)
- Trong spec mỗi chức năng/module, liệt kê rõ *báo cáo chuẩn* đi kèm và nêu các báo cáo ad hoc dự kiến — mục "báo cáo" bắt buộc của sản phẩm ERP.
- Thêm NFR về **output capacity planning**: ước tính số người truy vấn, tần suất, và cảnh báo query nặng để tránh quá tải sau golive.
- Thiết kế màn hình chính theo *vai trò* (role-specific desktop) thay vì theo module: gom báo cáo, module con, tác vụ cá nhân mà vai trò đó cần.
- Phân tầng truy cập: expert dùng trực tiếp ERP, người dùng thông thường qua intranet/portal — gắn với ma trận phân quyền.
- Ưu tiên view/data warehouse hơn report cứng để tài liệu không bị lỗi thời khi nhu cầu đổi.

## Liên hệ (Connects To)
- **Chương 2**: data warehouse và DBMS query là nền công nghệ.
- **Chương 4**: đầu ra là mặt kia của luồng dữ liệu nhập vào.
- **Chương 14**: portal và xương sống thông tin mở đường cho thương mại điện tử.
