# Chương 8: Kết quả từ Tình huống nghiên cứu 3 — Ngân hàng Quốc gia (Findings from Case Study 3 — National Bank (NB))

## Ý tưởng cốt lõi (Core Idea)
NB là ngân hàng quốc doanh lớn của Ai Cập (thành lập 1920, >470 chi nhánh, >12.000 nhân viên, ngân hàng đầu tiên ở Ai Cập/Bắc Phi đạt chuẩn **PCI DSS**). Năm 2010 triển khai **Oracle E-Business Suite** làm hệ thống **ERP** *back-office* (module: financial accounting; inventory & purchasing; HR) tích hợp với lõi ngân hàng *front-office* **FLEXCUBE** — theo khuyến nghị của Ngân hàng Trung ương Ai Cập. Đây là ca **trưởng thành kỹ thuật nhưng thích nghi kiểm toán kém**: ERP cung cấp bộ kiểm soát tự động mạnh (RBAC, maker-checker, phê duyệt theo cấp, self-review) nhưng không có kế hoạch quản lý thay đổi, chạy song song thủ công + ERP gây "thảm họa" hàng ngàn lỗi, và **IAF** (chức năng kiểm toán nội bộ) bám vào vai trò "thanh tra" (inspector/watchdog) nên chỉ giữ chính danh theo kiểu *bảo toàn công việc*, không tạo giá trị mới.

## Khái niệm chính (Key Concepts)
- **Role-Based Access Control (RBAC)**: kiểm soát truy cập theo vai trò, gồm 2 lớp — **function security** (giới hạn user truy cập menu/chức năng) và **data security** (kiểm soát bổ sung trên dữ liệu: ai được xem/sửa dữ liệu nào).
- **Approval hierarchy / Submit for Approval**: cây phê duyệt theo cấp; chọn "Submit for Approval" tự chuyển chứng từ tới người duyệt đúng cấp.
- **Automatic submission check**: kiểm tra tự động trước khi gửi duyệt — xác minh mọi trường bắt buộc đã nhập và mọi dữ liệu nằm trong khoảng cho phép (prescribed ranges); nếu sai → chuyển sang *approval errors window*; chứng từ tự in khi được duyệt.
- **Maker-checker**: người lập — người kiểm; mỗi màn hình được 2 người nhìn (người lập giao dịch + người kiểm duyệt). Oracle mặc định không có → NB phải *customise* để thêm bước này.
- **Self-review / self-control**: tự soát — mỗi chi nhánh tự chịu trách nhiệm kiểm soát và sửa lỗi trong chi nhánh; checker ngăn lỗi lan ra.
- **Processing constraints**: ràng buộc xử lý — chặn user thêm/sửa/xóa/hủy dữ liệu vượt quá một số thời điểm nhất định.
- **Audit trail / query access**: dấu vết kiểm toán và quyền truy vấn hiển thị mọi giao dịch đã nhập (ERP có nhưng auditor NB không dùng).
- **Business Objects**: phần mềm báo cáo tương tác (drag-drop) nằm giữa CSDL và người dùng cuối, truy xuất dữ liệu không cần biết cấu trúc DB.
- **Comprehensive auditor**: kiểm toán viên toàn diện — nắm mọi quy tắc, kiểm toán được nhiều quy trình (khái niệm mới xuất hiện sau ERP).

## Bảng tham chiếu (Reference Tables)
NB dùng cùng bộ **10 Control Assumptions** như Ch 7 (Automation, Centralisation, Continuous Monitoring, Data Consistency, Data Security, Integration, Multiple Methods of Control, Preventive Controls, Standardisation, Transparency). Các kiểm soát/thực hành **cụ thể, code-able** đặc trưng của NB:

| Kiểm soát (EN) | Cơ chế cụ thể |
|---|---|
| **RBAC 2 lớp** | function security (menu/chức năng) + data security (dữ liệu được xem/sửa) — "chỉ thấy thông tin liên quan công việc" để chống thông đồng |
| **Approval workflow** | Submit for Approval theo approval hierarchy; submission check (trường bắt buộc + prescribed ranges); tự in khi duyệt |
| **Maker-checker** | 2 cặp mắt mỗi màn hình; là yêu cầu customisation bắt buộc cho ngành ngân hàng |
| **Automated SoD** | ngăn một người kiểm soát cả hai đầu giao dịch; chặn breaches truy cập |
| **Processing constraints** | chặn add/update/delete/cancel vượt điểm kiểm soát |
| **Payroll tự động** | tính lương, khấu trừ tự động, chặn can thiệp tay |
| **Two currency fields** | tách trường ngoại tệ + nội tệ (tùy biến kiểm soát cho giao dịch ngoại tệ) |
| **Audit trail + Business Objects** | truy vết giao dịch + báo cáo tương tác cho mục đích kiểm toán |

**3 mục tiêu kiểm soát nội bộ (COSO, ERP tác động cả ba)**: (1) hiệu lực & hiệu quả vận hành; (2) độ tin cậy báo cáo tài chính; (3) tuân thủ luật và quy định.

## Mô hình tư duy (Mental Models)
- **Tích hợp là con dao hai lưỡi**: "once a transaction is approved, its financial impact directly affects all accounts" — lỗi ở một tài khoản/chi nhánh có thể lan khắp ngân hàng. Vì vậy tích hợp làm tăng tầm quan trọng của preventive control và self-review.
- **Back-office vs front-office**: ERP (back-office) tách khỏi lõi ngân hàng FLEXCUBE (front-office, giao dịch khách hàng). Một lý do triển khai: đưa fixed assets/receivables/payables ra khỏi core-banking để lõi chỉ còn giao dịch khách.
- **Kiểm soát trở thành việc tập thể (collective affair)**: ERP khiến các phiên bản kiểm soát phụ thuộc lẫn nhau → kiểm soát không còn là "tài sản riêng" của IAF, nhiều phòng ban cùng giám sát.

## Điều cần tránh (Anti-patterns)
- **Chạy song song không kiểm soát (parallel run disaster)**: ERP + hệ thống thủ công chạy cùng lúc; nhân viên quên/bỏ nhập liệu vào ERP; phải kiểm toán lại 3 tháng giao dịch toàn ngân hàng, lộ hàng ngàn lỗi.
- **Không có change management/đào tạo thật**: chỉ "briefing" thay cho training → nhân viên hoảng loạn, mơ hồ.
- **IAF không tham gia triển khai**: báo cáo kiểm toán bị IT thiết kế *sau* go-live; auditor nêu vấn đề kiểm soát quá muộn (lẽ ra phát hiện trước go-live sẽ tiết kiệm chi phí sửa đổi).
- **Kiểm toán viên thiếu kỹ năng IT cơ bản**: chỉ CIA có PC; một số không biết dùng bàn phím/chuột → nghỉ hưu sớm/nghỉ việc.
- **Bám vai trò thanh tra (inspector)**: IAF giữ chính danh bằng *bảo toàn công việc* và tuân theo niềm tin truyền thống, không chuyển sang assurance/risk-based.
- **IT nắm việc đảm bảo SoD**: auditor mất một phần vai trò vào tay IT team.

## Điểm cần nhớ (Key Takeaways)
1. Bộ kiểm soát ngân hàng chuẩn ERP rất cụ thể: **RBAC 2 lớp + approval hierarchy + submission check + maker-checker + processing constraints + automated SoD**.
2. Maker-checker thường *không có sẵn* trong ERP mặc định → phải tùy biến; BA phải đặc tả rõ như một yêu cầu kiểm soát.
3. Tích hợp làm lỗi lan nhanh → phải thiết kế self-review và preventive control; đồng thời quản trị rủi ro đối soát GL (core-banking vs module tài chính ERP).
4. Không có change management + chạy song song = thảm họa dữ liệu; phải đào tạo thật và có kế hoạch chuyển đổi.
5. Cho kiểm toán/kiểm soát tham gia *trước go-live* để phát hiện lỗ hổng, tiết kiệm chi phí sửa sau.

## Ứng dụng cho BA ERP (BA Application)
- Đặc tả **RBAC hai lớp**: với mỗi vai trò, liệt kê function security (menu/chức năng được truy cập) và data security (phạm vi dữ liệu được xem/sửa) — đây là phần phân quyền phải code được.
- Đặc tả **approval workflow** đầy đủ: approval hierarchy theo cấp, danh sách trường bắt buộc, prescribed ranges để submission check tự kiểm, hành vi khi sai (approval errors window), và tự in/tự chuyển trạng thái khi duyệt.
- Luôn thêm **maker-checker** cho giao dịch tài chính/ngân hàng (màn hình không đi tiếp cho đến khi có duyệt + xác nhận) và ghi chú nếu ERP mặc định không có (cần customise).
- Đặc tả **processing constraints** (chặn sửa/xóa/hủy sau điểm kiểm soát) và các kiểm soát đối soát liên hệ thống (ví dụ: đối chiếu GL giữa hệ thống lõi và module tài chính) để chặn lỗi lan.
- Khi khách cần trường/khái niệm bản địa (ví dụ 2 trường ngoại tệ/nội tệ, "negotiable instruments") không có trong chuẩn ERP, ghi rõ là *customisation/localisation* kèm lý do kiểm soát.

## Liên hệ (Connects To)
- **Ch 7**: Case 2 (NC) — cùng bộ 10 Control Assumptions nhưng NC không dùng; NB dùng nhưng IAF vẫn không thích nghi tốt.
- **Ch 9**: Case 4 (IB) — ngân hàng quốc tế, cùng nền Oracle nhưng IAF tham gia sớm và thành công.
- **Ch 10**: Phân tích chéo 4 ca.
- **COSO / PCI DSS / institutional theory**: chuẩn kiểm soát nội bộ, an toàn dữ liệu thẻ, và lý thuyết tính chính danh.
