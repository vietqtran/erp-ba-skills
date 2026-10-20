# Chương 5: Triển khai ERP (ERP Implementation)

## Ý tưởng cốt lõi (Core Idea)
Triển khai ERP khác hẳn phát triển phần mềm từ đầu: phần mềm đã tồn tại dưới dạng gói, việc chính là **customize vừa đủ** và **đưa tổ chức khớp quanh phần mềm**, không phải ngược lại. Triển khai nên được hiểu là một **vòng học hỏi liên tục** (không chỉ là cài đặt), nặng về con người và tổ chức hơn là công nghệ; "going live is not the end" — còn "second wave" sau đó.

## Framework được giới thiệu (Frameworks Introduced)
- **Three approaches to implementation** — ba cách tiếp cận: **Big Bang** (triển khai tất cả module cùng lúc — lợi ích đầy đủ nhưng rủi ro cao), **Location-wise** (theo địa điểm — giảm chi phí/rủi ro, có feedback trước khi mở rộng), **Module-wise** (theo từng module — chọn Finance/HR/MM... tùy nhu cầu).
- **Three perspectives** — ba góc nhìn khi triển khai: **Organizational** (phát triển tổ chức, con người, quyền lực, văn hóa, bối cảnh), **Business** (ERP dẫn tới BPR và Change Management, bám IT/IS strategy & tầm nhìn), **Technological** (kiến trúc, hạ tầng, configuration, customization, project management).
- **Phases in ERP Implementation (11 bước)** — vòng đời triển khai: Project Planning → Identification of ERP Vendor → Evaluation of ERP Package → **Gap Analysis** → Reengineering → Customization → ERP Team Training → Testing → Going Live → Training to End-Users → Maintenance.
- **Critical Success Factors (CSF)** — các vấn đề lãnh đạo phải giải quyết: trạng thái legacy systems; tác động lên business processes; các quy trình đã định nghĩa rõ chưa; chọn hệ tích hợp đầy đủ hay một module; thời lượng dự án; mức hợp tác của lãnh đạo; sẵn có nguồn lực; lịch dự án & change management.
- **BPR (Business Process Reengineering)** — theo **Dr. Michael Hammer**: "fundamental rethinking and radical redesign" các business process nhằm cải thiện đột phá về cost, quality, service, speed.

## Khái niệm chính (Key Concepts)
- **Gap Analysis**: bước "thương lượng" giữa yêu cầu công ty và chức năng gói có sẵn — tìm khoảng trống rồi lấp bằng: sản phẩm bên thứ ba, viết chương trình tùy biến, hoặc sửa mã nguồn ERP.
- **Customization**: quá trình điều chỉnh phần mềm cho khớp tổ chức; phải tính 3 tham số — **end-users' requirements, technical requirements, vision of top management**. Nguyên tắc: **không bao giờ sửa base của hệ thống**.
- **SDLC vs ERP implementation**: SDLC gồm Analysis–Design–Coding–Testing (xây từ đầu); triển khai ERP không code từ đầu mà chọn–đánh giá–customize gói.
- **ERP implementation team**: Project Management Team gồm technical leader + executive committee head (có thể thêm đại diện cấp cao của vendor).
- **Software Configuration Management (SCM)**: quản lý thay đổi — vừa quản lý *quá trình* thay đổi vừa quản lý *mọi artifact* của hệ thống đang tiến hóa. (Lưu ý: cùng viết tắt "SCM" nhưng khác Supply Chain Management.)
- **Characteristics of ERP (so với non-ERP)**: nhiều control procedure **không để lại bằng chứng chứng từ**; thông tin ghi ở dạng chỉ đọc được bằng máy; dữ liệu sinh tự động; lỗi có thể lan rộng mà không bị phát hiện; nhưng với control đúng thì tin cậy hơn non-ERP; rất khó thay đổi sau khi đã triển khai.

## Mô hình tư duy (Mental Models)
- **"Fit the organization around the software"**: process change là tất yếu với ERP; lãnh đạo thường muốn đổi nền tảng công nghệ nhưng không muốn đổi quy trình — đó là sai lầm.
- Coi **"Failure to plan is equivalent to planning to fail"**: đa số dự án thất bại vì planning kém và thiếu phối hợp từ lãnh đạo; khi trễ lịch, đội thường "crash & compress" các hoạt động để kịp go-live — đây là lúc dự án yếu đi.
- **Customization càng cao, lợi ích ERP càng thấp**: gói mua về là để chuẩn hóa/tinh gọn quy trình; customize nhiều biến ERP thành non-ERP.

## Điều cần tránh (Anti-patterns)
- **Sửa "base" hệ thống / customize quá mức**: tốn kém, phải re-implement cho mỗi bản phát hành, tăng chi phí bảo trì dài hạn, trễ lịch.
- **Mục tiêu mơ hồ, kỳ vọng không rõ**: nguyên nhân thất bại hàng đầu.
- **Thiếu cam kết của lãnh đạo** (do không hiểu giá trị CNTT) và **project manager không hóa giải được kháng cự/xung đột**.
- **Coi nhẹ change management, training, BPR** so với các vấn đề kỹ thuật (project management, configuration, IT architecture).
- **Xem go-live là đích**: "an ERP is a commitment to a new way of doing business", không thể "triển khai xong rồi quay lại làm việc như cũ".

## Ví dụ minh họa (Worked Example)
Vòng đời 11 bước diễn giải đầu–cuối cho một công ty vừa và nhỏ: (1) **Project Planning** — lãnh đạo lập kế hoạch: thời điểm bắt đầu, thời lượng, chi phí, ngân sách, đội ERP nội bộ, consultant, yêu cầu đào tạo, change management. (2) **Identification of Vendor** — chấm theo reliability, khả năng đáp ứng yêu cầu, functionality, reputation, giải pháp trọn gói, chi phí, bảo trì, khả năng customize, thời lượng, đào tạo. (3) **Evaluation** — đánh giá gói theo ba góc nhìn tổ chức/kỹ thuật/nghiệp vụ. (4) **Gap Analysis** — tìm khoảng trống giữa quy trình hiện tại và gói, mời consultant trung lập hóa giải xung đột. (5) **Reengineering** — tinh chỉnh quy trình (thêm/bỏ/sửa), cần executive leader đủ quyền lực. (6) **Customization** — cân 3 tham số, giữ customize thấp nhất. (7) **ERP Team Training**. (8) **Testing** — kiểm tính nhất quán, toàn vẹn, verify/validate yêu cầu. (9) **Going Live**. (10) **Training to End-Users**. (11) **Maintenance** chạy song song. Sau vài tháng tới một năm, lợi ích mới hiện rõ theo **ba cấp benefits realization**: (a) tự động hóa quy trình hiện có → (b) thấy quy trình được cải thiện → (c) hệ hỗ trợ ra quyết định (DSS) cho quản lý cấp trung và cấp cao.

## Điểm cần nhớ (Key Takeaways)
1. Ba cách tiếp cận: Big Bang / Location-wise / Module-wise — đánh đổi giữa lợi ích đầy đủ và rủi ro/chi phí.
2. Nhìn triển khai từ ba góc: Organizational, Business, Technological — thất bại thường do xem nhẹ góc tổ chức/con người.
3. Thuộc lòng vòng đời 11 bước, đặc biệt Gap Analysis → Reengineering → Customization.
4. BPR (Hammer) là "radical redesign"; customize càng nhiều, lợi ích ERP càng ít.
5. Lãnh đạo phải: tuyên bố mọi phòng ban dùng quy trình của ERP, duyệt mọi sửa đổi lớn kèm lý do, và cân nhắc thêm/bỏ/sửa quy trình (process innovation).
6. Benefits realization qua ba cấp và mất đến ~1 năm; đừng kỳ vọng lợi ích tức thì sau go-live.

## Ứng dụng cho BA ERP (BA Application)
- Dùng **vòng đời 11 bước** làm khung mục lục tài liệu triển khai; mỗi bước có đầu ra và tiêu chí nghiệm thu riêng — khớp với ý tưởng "mỗi step có checklist".
- Viết **Gap Analysis** thành artifact rõ: liệt kê từng gap + phương án lấp (third-party / custom program / sửa source) + quyết định giữ hay bỏ — tránh tài liệu mơ hồ ở chỗ "khác biệt quy trình".
- Mỗi yêu cầu customization phải ghi đủ **3 tham số** (end-user req, technical req, vision lãnh đạo) và lý do; mặc định cảnh báo "customize cao = lợi ích thấp" ngay trong spec.
- Đưa **control/audit** vào non-functional requirements: ERP có thể không để lại chứng từ, sinh dữ liệu tự động, lỗi lan rộng → phải đặc tả audit trail, control procedure, phân quyền.
- Ghi **CSF và vai trò lãnh đạo** vào phần giả định/ràng buộc của tài liệu; thiếu cam kết lãnh đạo là rủi ro phải nêu, không bỏ qua.

## Bảng tham chiếu (Reference Tables)
Ghi chú trích xuất: các Figure 1 (hiệu năng trước/sau ERP), Figure 2 (gap analysis), Figure 3 (sơ đồ tổ chức đội triển khai), Figure 4 (benefits realization) chỉ còn caption, phần hình bị dẹt — nội dung đã được tái dựng từ phần chữ ở trên, không bịa thêm chi tiết hình.

## Liên hệ (Connects To)
- **Ch 4**: hai bước đầu (Project Planning, Vendor Identification, Evaluation) nối tiếp quy trình lựa chọn 4 giai đoạn; bảng yếu tố chọn vendor tái sử dụng tại đây.
- **Ch 3**: Module-wise approach và customization dựa trên cấu trúc module.
- **Ch 1**: anti-pattern over-customization và "best practices embedded in software" được phân tích trọn vẹn tại chương này.
- **BPR / Change Management**: liên hệ chuẩn quản trị thay đổi và tái thiết kế quy trình ngoài phạm vi ERP thuần túy.
