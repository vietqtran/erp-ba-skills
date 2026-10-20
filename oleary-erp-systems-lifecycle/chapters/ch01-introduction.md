# Chương 1: Giới thiệu (Introduction)

## Ý tưởng cốt lõi (Core Idea)
Hệ thống **ERP (Enterprise Resource Planning)** — hoạch định nguồn lực doanh nghiệp — là phần mềm đóng gói chạy trên kiến trúc client server, tích hợp phần lớn các quy trình nghiệp vụ của doanh nghiệp quanh một cơ sở dữ liệu duy nhất. Giá trị cốt lõi của ERP không nằm ở từng chức năng riêng lẻ mà ở sự **tích hợp (integration)** và dữ liệu thời gian thực; đây chính là tiêu chí định hình mọi yêu cầu khi viết tài liệu ERP.

## Framework được giới thiệu (Frameworks Introduced)
- **Eight Value-Creation Mechanisms** — tám cơ chế ERP tạo ra giá trị. Đây là khung lý giải *tại sao* một yêu cầu ERP quan trọng:
  - Khi nào dùng: đánh giá lợi ích của bất kỳ chức năng/quy trình ERP nào — đối chiếu nó tạo giá trị qua cơ chế nào.
  - Tám cơ chế: (1) tích hợp hoạt động toàn doanh nghiệp, phá bỏ silo chức năng và địa điểm; (2) nhúng **best practices** — thông lệ tốt nhất (SAP R/3 có hơn 1.000); (3) chuẩn hóa tổ chức (**organizational standardization**) giữa các địa điểm; (4) loại bỏ **information asymmetries** — bất đối xứng thông tin; (5) cung cấp thông tin trực tuyến và thời gian thực; (6) cho phép truy cập đồng thời cùng một dữ liệu để lập kế hoạch và kiểm soát; (7) thúc đẩy giao tiếp/cộng tác nội bộ; (8) thúc đẩy giao tiếp/cộng tác liên tổ chức qua "xương sống thông tin".
- **ERP Life-Cycle Model** — mô hình vòng đời ERP: Deciding to Go ERP (quyết định có làm ERP) → Choosing an ERP System (chọn hệ thống) → Designing (thiết kế: đổi quy trình hay đổi phần mềm; chọn mô hình/artifact/quy trình chuẩn) → Implementing (Big Bang vs Phased) → After Going Live (sau golive) → Training (xuyên suốt).
  - Khi nào dùng: định vị công việc viết tài liệu của BA nằm ở giai đoạn nào trong vòng đời.

## Khái niệm chính (Key Concepts)
- **ERP system**: hệ thống xử lý giao dịch tích hợp, dùng cơ sở dữ liệu toàn doanh nghiệp, lưu mỗi dữ liệu thường chỉ một lần, truy cập thời gian thực.
- **Best practices**: cách làm quy trình được coi là tốt nhất, được nhúng sẵn trong ERP dưới dạng các lựa chọn phải quyết khi triển khai.
- **Information asymmetry**: tình trạng cùng một sự kiện nhưng các nhóm chức năng/địa điểm có báo cáo khác nhau, thông tin bị "mắc kẹt" cục bộ.
- **Information agile**: doanh nghiệp "nhanh nhạy thông tin" — xử lý và tích hợp thông tin vào quy trình/quyết định tốt hơn, buộc cả đối tác phải thích nghi (ví dụ phải hoạt động thời gian thực theo).

## Mô hình tư duy (Mental Models)
- Hãy coi ERP là **"electronic embodiment of reengineering"** (hiện thân điện tử của tái cấu trúc): chọn ERP đồng nghĩa với việc buộc phải tái thiết kế quy trình theo best practices nhúng sẵn.
- Dùng tư duy "một dữ liệu nhập một lần" (enter once): nếu một thông tin bị nhập lại ở nhiều nơi trong spec, đó là dấu hiệu chưa đạt chuẩn ERP.
- Khi mua ERP là "mua luôn tầm nhìn của nhà cung cấp" — doanh nghiệp giao phó phần lớn việc bảo trì/tiến hóa phần mềm cho vendor.

## Điều cần tránh (Anti-patterns)
- **Coi ERP như phần mềm chức năng rời rạc**: thiết kế theo silo chức năng làm mất đi giá trị tích hợp — lý do chính để chọn ERP.
- **Bỏ qua tác động tổ chức**: ERP làm thay đổi bản chất công việc ở mọi phòng ban (kể cả nhân sự IT và kế toán); spec chỉ mô tả màn hình mà bỏ qua thay đổi vai trò sẽ thiếu hụt.

## Điểm cần nhớ (Key Takeaways)
1. ERP tạo giá trị nhờ tích hợp + dữ liệu một nguồn + thời gian thực, không phải nhờ số lượng tính năng.
2. Tám cơ chế tạo giá trị là bộ tiêu chí để biện minh cho mỗi yêu cầu/chức năng.
3. Mọi tài liệu BA nằm trong một mắt xích của vòng đời ERP (quyết định → chọn → thiết kế → triển khai → sau golive → đào tạo).
4. "Best practices" nhúng sẵn vừa là cơ hội (học cách làm chuẩn) vừa là ràng buộc (quy trình riêng có thể bị san phẳng).
5. Cuốn sách tập trung vào các vấn đề *đặc thù ERP*, không phải quản trị dự án phần mềm nói chung.

## Ứng dụng cho BA ERP (BA Application)
- Trước mỗi yêu cầu/chức năng, viết rõ nó hiện thực hóa cơ chế tạo giá trị nào trong tám cơ chế — đây là cách chống "thừa chức năng" và "lệch yêu cầu".
- Áp dụng nguyên tắc "mỗi dữ liệu nhập một lần": trong spec phải chỉ ra nguồn dữ liệu gốc (single source of truth) cho từng trường, tránh định nghĩa nhập trùng ở nhiều chức năng.
- Khi tài liệu một chức năng, luôn nêu tác động lên tích hợp liên module/liên phòng ban, không mô tả chức năng cô lập.
- Gắn mỗi tài liệu với giai đoạn vòng đời để biết độ chi tiết cần đạt (ví dụ giai đoạn Designing cần đủ chi tiết để code).

## Liên hệ (Connects To)
- **Chương 2**: nền tảng công nghệ (client server, CSDL quan hệ, best practices vs obliteration).
- **Chương 3**: hệ thống ERP, modules, và khung **MAPs**.
- **Chương 7–13**: triển khai chi tiết từng giai đoạn vòng đời.
