# Cheatsheet — Phán đoán chuẩn ERP cho BA

Trang tham chiếu nhanh: quy tắc quyết định, bảng đánh đổi, ngưỡng, dấu hiệu cảnh báo. Số chương theo skill này.

## Quy tắc quyết định (Khi X → làm Y, vì Z)

| Khi... | Làm | Vì |
|---|---|---|
| Viết spec một chức năng | Tách **mục tiêu kiểm soát** (giữ nguyên) khỏi **cơ chế** (đổi theo hệ thống) | Giữ tài liệu không lệch khỏi yêu cầu gốc (Ch 01) |
| Khách ở nước đang phát triển | Đánh dấu best practice ERP cần bản địa hóa | Logic cài sẵn bắt nguồn từ nước phát triển, có thể không hợp (Ch 01) |
| Tái thiết kế quy trình (reengineering) | Không xóa kiểm soát cũ khi chưa có cái thay thế | Dễ tạo lỗ hổng kiểm soát & sai báo cáo tài chính (Ch 02) |
| Mở rộng phạm vi công việc của một user | Rà lại **SoD** | ERP mở rộng việc dễ phá vỡ phân tách nhiệm vụ (Ch 02) |
| Dữ liệu chuyển bước sau với "chấp nhận ngầm" | Chèn bước **re-verification** | ERP thường "không kiểm tra dọc đường" (Ch 02) |
| Phân loại một feature | Truy về **coercive** (bắt buộc) / normative / mimetic (trend) | Phân biệt "bắt buộc do luật" với "theo trend" để ưu tiên đúng (Ch 04) |
| Quy trình khách không customise được / bất hợp lệ | **Reengineer** về chuẩn (auditable), không workaround | Chỉ quy trình chuẩn mới để lại vết & kiểm toán được (Ch 06, 10) |
| Lệch chuẩn do luật địa phương (thuế) | **Customise/localise** có kiểm soát | Là khác biệt hợp pháp bắt buộc, không phải thói quen cần bỏ (Ch 06) |
| Viết spec kiểm soát | Phân loại **inherent / configurable / security / reporting** | Dev cần biết cái nào code, cái nào config, cái nào phân quyền/báo cáo (Ch 06) |
| Thiết kế một vùng rủi ro | Gắn ≥1 **compensating control** | Kiểm soát chính có thể hỏng theo thời gian (Ch 06) |
| Đặc tả giao dịch tài chính/ngân hàng | Luôn thêm **maker-checker** (không đi tiếp đến khi approval+validation) | ERP mặc định có thể thiếu checker; ngành NH không cho qua giao dịch chưa có bên thứ hai kiểm (Ch 08) |
| Cutover | Cấm chạy song song thủ công+ERP không kiểm soát; bắt buộc nhập ERP + đào tạo thật | Parallel-run lỏng lẻo gây hàng ngàn lỗi phải kiểm toán lại nhiều tháng (Ch 08) |
| Bắt đầu dự án ERP | Đưa kiểm soát/kiểm toán vào ngay **gathering & mapping requirements** | Đây là lúc gắn SoD, access rights, risk framework trước khi lan vào mọi giai đoạn sau (Ch 09, 11) |
| Đặc tả dữ liệu | Áp **CAVAIR** (Complete, Accurate, Valid, Restricted Access) | Đây chính là tiêu chí kiểm toán viên dùng để nghiệm thu dữ liệu (Ch 09) |
| Gán quyền truy cập | Review user profile↔access rights, authority↔job description; giám sát liên tục khi luân chuyển nhân sự | Thay đổi quyền theo luân chuyển là rủi ro truy cập cao nhất (Ch 09) |
| Mô tả kiểm soát cho quy trình đa chức năng | Đặc tả **horizontal** end-to-end, không rời rạc theo địa điểm | Chỉ phân tích ngang mới gom được các kiểm soát liên kết cùng một rủi ro (Ch 11) |
| IAF/khâu kiểm soát vốn đã yếu trước ERP | Đầu tư con người song song, đừng kỳ vọng ERP tự nâng cấp | ERP chỉ khuếch đại: mạnh thì "cách mạng", yếu thì tan rã (Ch 10) |
| Tổ chức buổi elicitation | Gửi agenda trước, phỏng vấn đủ vai trò, triangulate ≥2 nguồn + member check | Vấn đề quá phức tạp để lấy từ một người; bắt lệch/thiếu sớm (Ch 05, 12) |

## Bảng đánh đổi: xử lý quy trình lệch chuẩn ERP

| Lựa chọn | Dùng khi | Rủi ro |
|---|---|---|
| **Reengineer** (về chuẩn) | Quy trình cũ sai/bất hợp lệ hoặc không customise được | Kháng cự thay đổi; cần change management |
| **Customise/localise** | Lệch do luật/thuế địa phương, hoặc thiếu bước kiểm soát (vd maker-checker) | Khó nâng cấp, lệch best-practice, tốn chi phí |
| **Workaround** | (Gần như không bao giờ) | Phá minh bạch & tính kiểm toán được — tránh |

## Bảng: 4 loại kiểm soát ERP → việc của dev

| Loại | Dev làm gì |
|---|---|
| **Inherent** | Không code — có sẵn, chỉ xác nhận |
| **Configurable** | Cấu hình lúc customise |
| **Security** | Phân quyền + SoD (RBAC 2 lớp) |
| **Reporting** | Xây báo cáo chuẩn/ad hoc (phần lớn khối lượng customise) |

## Checklist nghiệm thu "đã chuẩn ERP chưa" — 11 giả định kiểm soát (Ch 10)
Mỗi chức năng trả lời yes/no + nêu cơ chế: integration · standardisation · automation · multiple methods of control · preventive · compensating · continuous monitoring · data security (RBAC) · centralisation · data consistency · transparency & visibility.
(Dùng tập con theo rủi ro: IC 9, NC/NB/IB 10 — đừng ép đủ 11 cho chức năng nhỏ.)

## Ngưỡng & mặc định
- ERP tối thiểu = module **tài chính–kế toán** + **một CSDL** dùng chung; mức tích hợp là continuum. (Ch 02)
- Ưu tiên **preventive > detective**; ERP cho dời việc từ "ký duyệt từng giao dịch" sang "giám sát kiểm soát đang chạy đúng". (Ch 06, 07)
- Mỗi giao dịch soát **1–3 lần** (một người nhập / một người duyệt / một người xác nhận). (Ch 07)
- Dữ liệu an ninh = 4 thuộc tính: **confidentiality, authentication, integrity, non-repudiation**; dữ liệu đã nhập không sửa được; thẻ tuân **PCI DSS**. (Ch 08)
- IB (ca thành công): mỗi đợt kiểm toán **5 auditor + 1 IT auditor**; **40 giờ** đào tạo/kiểm toán viên/năm; ERP hợp nhất giảm đội (vd 30 → 15 + 3 IT) dù phạm vi tăng. (Ch 09)
- Rủi ro truy cập **cao nhất** = thay đổi quyền theo luân chuyển nhân sự. (Ch 09)

## Dấu hiệu cảnh báo (tells & smells)
- Thấy "pay code" riêng cho lao động thời vụ / sổ tay thủ công chạy song song → đang **workaround**, kiểm soát bị vô hiệu. (Ch 07)
- Chỉ giữ 1 kiểm toán viên "biểu tượng" / ủy ban kiểm toán "không kích hoạt" → **decoupling**, chính danh đã mất. (Ch 07, 10)
- IT team thiết kế báo cáo kiểm toán *sau* go-live → IAF đứng ngoài, sẽ mất vai trò vào tay IT. (Ch 08)
- Ban lãnh đạo từ chối đưa giá mua/công thức/lợi nhuận/khách hàng lên hệ thống → **anti-transparency**, ERP sẽ vô dụng dù cài đủ. (Ch 07)
- Phần lớn yêu cầu customise rơi vào vùng **báo cáo** → bình thường; đặc tả report kiểm soát (discrepancy/reconciliation, exception, red-alert, xung đột SoD) ngay từ đầu. (Ch 06)
- Nhãn nào trong coding scheme 5 nhóm còn trống → nghi ngờ **thiếu chức năng**. (Ch 12)
