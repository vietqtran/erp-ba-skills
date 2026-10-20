---
doc: issue-log
project: Minh An ERP
status: Ready
version: 1.0
updated: 2026-10-20
---

# Nhật ký câu hỏi – giả định – quyết định – mâu thuẫn – thay đổi — Minh An ERP

## 1. Câu hỏi mở (Q)

| ID | Câu hỏi | Ngữ cảnh & ảnh hưởng (REQ/FN/BR liên quan) | Phương án gợi ý (nếu có) | Hỏi ai | Mức ảnh hưởng | Hạn | Trạng thái | Câu trả lời | Nguồn trả lời |
|---|---|---|---|---|---|---|---|---|---|
| Q-001 | Giai đoạn 1 có dùng đề nghị mua hàng trước khi lập đơn mua không? | Quyết định chức năng đứng trước đơn mua (FN-PUR-02) | A: lập đơn trực tiếp; B: bắt buộc từ đề nghị mua | TP Mua hàng | Chặn | 10/10/2026 | Đã trả lời | Lập đơn trực tiếp | SRC-003 |
| Q-002 | Ngưỡng 100 triệu tính trước hay sau thuế; đơn ngoại tệ quy đổi thế nào? | REQ-005, REQ-006, PRM-PUR-001 | A: trước thuế; B: tổng thanh toán | TP Mua hàng, Kế toán trưởng | Chặn | 10/10/2026 | Đã trả lời | Tổng thanh toán gồm thuế, quy đổi theo tỷ giá trên đơn | SRC-003 |
| Q-003 | Ai được đóng đơn khi nhà cung cấp báo không giao nữa? | REQ-014, FN-PUR-02 | A: người tạo đơn; B: Trưởng phòng | TP Mua hàng | Cao | 10/10/2026 | Đã trả lời | Trưởng phòng Mua hàng, phải ghi lý do | SRC-003 |
| Q-004 | "Dễ dùng" được đo bằng tiêu chí nào? | REQ-018, NFR-USAB-01 | Thời gian tạo đơn mẫu; tìm hàng theo mã/tên | TP Mua hàng | Trung bình | 10/10/2026 | Đã trả lời | Tạo đơn 20 dòng không quá 5 phút; tìm hàng theo mã hoặc tên | SRC-003 |
| Q-005 | Duyệt trên điện thoại bằng trình duyệt web có đáp ứng không, hay cần ứng dụng riêng? | REQ-021, NFR-COMP-01 | A: web trên trình duyệt điện thoại; B: ứng dụng riêng | TP Mua hàng | Cao | 10/10/2026 | Đã trả lời | Trình duyệt điện thoại là được | SRC-003 |
| Q-006 | Tỷ giá trên đơn ngoại tệ lấy từ đâu? | REQ-012, FN-PUR-02 | A: nhập tay; B: lấy từ bảng tỷ giá | Kế toán trưởng | Cao | 10/10/2026 | Đã trả lời | Nhân viên nhập tay tỷ giá bán của ngân hàng giao dịch ngày lập đơn, bắt buộc với đơn không phải VND | SRC-003 |
| Q-007 | Đề xuất: cho phép hủy đơn đã duyệt khi chưa nhận hàng? | Chuẩn ERP (erp-ba-core/references/processes/p2p-procure-to-pay.md §6), FN-PUR-02 | Trưởng phòng hủy, bắt buộc lý do | TP Mua hàng | Trung bình | 10/10/2026 | Đã trả lời | Đồng ý | SRC-003 |
| Q-008 | "Sắp đến hạn" là trong vòng bao nhiêu ngày? | REQ-016, PRM-PUR-002 | 3 ngày | TP Mua hàng | Trung bình | 10/10/2026 | Đã trả lời | 3 ngày | SRC-003 |
| Q-009 | Người duyệt cần cả "Trả lại để sửa" và "Từ chối" không? | Chuẩn ERP (erp-ba-core/references/design-patterns.md P03), FN-PUR-02 | Cả hai | TP Mua hàng | Trung bình | 10/10/2026 | Đã trả lời | Cần cả hai | SRC-003 |
| Q-010 | Xác nhận chỉ tiêu hiệu năng đề xuất: danh sách ≤ 2 giây, lưu đơn 200 dòng ≤ 3 giây, 30 người dùng đồng thời? | REQ-020, NFR-PERF-01, NFR-PERF-02 | Như đề xuất | TP Mua hàng, Kế toán trưởng | Trung bình | 10/10/2026 | Đã trả lời | Đồng ý | SRC-003 |
| Q-011 | Ai được sửa, gửi duyệt, thu hồi, xóa đơn — người tạo hay mọi nhân viên cùng chi nhánh? | REQ-011, FN-PUR-02 §2 | A: chỉ người tạo; B: cả chi nhánh | TP Mua hàng | Cao | 10/10/2026 | Đã trả lời | Chỉ người tạo | SRC-003 |
| Q-012 | Đề xuất: người duyệt không được duyệt đơn do chính mình tạo? | Chuẩn kiểm soát nội bộ (erp-ba-core/references/security-and-parameters.md), SOD-01 | Trưởng phòng tự tạo đơn thì chuyển Giám đốc | TP Mua hàng | Cao | 10/10/2026 | Đã trả lời | Đồng ý như phương án | SRC-003 |
| Q-013 | Sau khi duyệt, sửa những thông tin nào thì không cần duyệt lại? | REQ-015, FN-PUR-02 | Chỉ ngày giao dự kiến và ghi chú | TP Mua hàng | Cao | 10/10/2026 | Đã trả lời | Ngày giao dự kiến và ghi chú không cần duyệt lại; thông tin khác phải duyệt lại | SRC-003 |
| Q-014 | Đề xuất: gửi thông báo cho người duyệt khi có đơn chờ duyệt và cho người tạo khi đơn được xử lý? | Chuẩn ERP (erp-ba-core/references/design-patterns.md P10), REQ-021, NTF-PUR-01, NTF-PUR-02 | Trong ứng dụng và email | TP Mua hàng | Trung bình | 10/10/2026 | Đã trả lời | Đồng ý | SRC-003 |
| Q-015 | Khi người duyệt từ chối một lần điều chỉnh đơn đã duyệt, đơn quay về phiên bản đã duyệt trước đó hay kết thúc? | REQ-015, FN-PUR-02 §7 | A: quay về phiên bản trước; B: kết thúc đơn | TP Mua hàng | Cao | 10/10/2026 | Đã trả lời | Quay về phiên bản đã duyệt trước đó | SRC-003 |
| Q-016 | Ai được tạo, sửa, khóa nhà cung cấp; danh sách dùng chung hay theo chi nhánh? | REQ-008, REQ-010, FN-PUR-01 | A: nhân viên tạo/sửa, Trưởng phòng khóa; B: chỉ Trưởng phòng | TP Mua hàng | Cao | 10/10/2026 | Đã trả lời | Dùng chung cả công ty; nhân viên tạo, sửa; Trưởng phòng khóa, mở khóa | SRC-003 |

## 2. Giả định (ASM)

| ID | Giả định | Lý do đặt giả định | Rủi ro nếu sai | Người cần xác nhận | Trạng thái (Đang dùng / Đã xác nhận → DEC / Bị bác bỏ) |
|---|---|---|---|---|---|
| ASM-001 | Phiếu nhập kho (module Kho) cập nhật số lượng đã nhận của đơn mua khi ghi sổ và khi đảo | Cần để theo dõi giao hàng (REQ-002, REQ-013); module Kho đặc tả trong SRS riêng | Trạng thái đơn mua không phản ánh đúng thực nhận | BA module Kho | Đã xác nhận → DEC-014 |

## 3. Quyết định (DEC)

| ID | Quyết định | Người quyết định | Ngày | Nguồn (MTG/SRC/Q) | Ảnh hưởng (REQ/FN/FEAT) |
|---|---|---|---|---|---|
| DEC-001 | Giai đoạn 1 không dùng đề nghị mua hàng; đơn mua lập trực tiếp | Trần Văn Hùng | 13/10/2026 | Q-001, SRC-003 | FN-PUR-02 |
| DEC-002 | Ngưỡng duyệt tính trên tổng thanh toán gồm thuế, quy đổi VND theo tỷ giá trên đơn | Trần Văn Hùng, Nguyễn Thị Lan | 13/10/2026 | Q-002, SRC-003 | REQ-005, REQ-006, PRM-PUR-001 |
| DEC-003 | Trưởng phòng Mua hàng đóng đơn khi nhà cung cấp ngừng giao, bắt buộc lý do | Trần Văn Hùng | 13/10/2026 | Q-003, SRC-003 | REQ-014, FN-PUR-02 |
| DEC-004 | Tiêu chí dễ dùng: tạo đơn 20 dòng không quá 5 phút với người đã đào tạo; tìm hàng theo mã hoặc tên | Trần Văn Hùng | 13/10/2026 | Q-004, SRC-003 | REQ-018, NFR-USAB-01 |
| DEC-005 | Duyệt trên trình duyệt web của điện thoại, không làm ứng dụng riêng | Trần Văn Hùng | 13/10/2026 | Q-005, SRC-003 | REQ-021, NFR-COMP-01 |
| DEC-006 | Tỷ giá nhập tay trên đơn, bắt buộc khi tiền tệ khác VND | Nguyễn Thị Lan | 13/10/2026 | Q-006, SRC-003 | REQ-012, FN-PUR-02 |
| DEC-007 | Trưởng phòng được hủy đơn đã duyệt chưa nhận hàng, bắt buộc lý do | Trần Văn Hùng | 13/10/2026 | Q-007, SRC-003 | FN-PUR-02 |
| DEC-008 | "Sắp đến hạn" = trong vòng 3 ngày tới ngày giao dự kiến | Trần Văn Hùng | 13/10/2026 | Q-008, SRC-003 | REQ-016, PRM-PUR-002 |
| DEC-009 | Người duyệt có hai lựa chọn: Trả lại để sửa và Từ chối | Trần Văn Hùng | 13/10/2026 | Q-009, SRC-003 | FN-PUR-02 |
| DEC-010 | Chỉ tiêu hiệu năng: danh sách ≤ 2 giây (p95), lưu đơn 200 dòng ≤ 3 giây, 30 người dùng đồng thời | Trần Văn Hùng, Nguyễn Thị Lan | 13/10/2026 | Q-010, SRC-003 | REQ-020, NFR-PERF-01, NFR-PERF-02 |
| DEC-011 | Chỉ người tạo đơn được sửa, gửi duyệt, thu hồi, xóa đơn | Trần Văn Hùng | 13/10/2026 | Q-011, SRC-003 | REQ-011, FN-PUR-02 |
| DEC-012 | Người duyệt không được duyệt đơn do mình tạo; Trưởng phòng tự tạo đơn thì Giám đốc duyệt thay cấp 1 | Trần Văn Hùng | 13/10/2026 | Q-012, SRC-003 | SOD-01, FN-PUR-02 |
| DEC-013 | Sau duyệt, sửa ngày giao dự kiến và ghi chú không cần duyệt lại; sửa thông tin khác phải duyệt lại từ đầu | Trần Văn Hùng | 13/10/2026 | Q-013, SRC-003 | REQ-015, FN-PUR-02 |
| DEC-014 | Phiếu nhập kho cập nhật số lượng đã nhận của dòng đơn mua khi ghi sổ và hoàn lại khi đảo (thống nhất với BA module Kho) | BA module Kho, BA module Mua hàng | 14/10/2026 | ASM-001 | FN-PUR-02 §14 |
| DEC-015 | Gửi thông báo trong ứng dụng và email: người duyệt khi có đơn chờ duyệt; người tạo khi đơn được duyệt cấp cuối, trả lại, từ chối, đóng, hủy | Trần Văn Hùng | 13/10/2026 | Q-014, SRC-003 | NTF-PUR-01, NTF-PUR-02 |
| DEC-016 | Từ chối một lần điều chỉnh thì đơn quay về phiên bản đã duyệt trước đó và tiếp tục thực hiện | Trần Văn Hùng | 13/10/2026 | Q-015, SRC-003 | REQ-015, FN-PUR-02 |
| DEC-017 | Danh mục nhà cung cấp dùng chung toàn công ty; ROLE-PUR-STAFF tạo, sửa; ROLE-PUR-MGR khóa, mở khóa | Trần Văn Hùng | 13/10/2026 | Q-016, SRC-003 | FN-PUR-01 |

## 4. Mâu thuẫn (CFL)

| ID | Phát biểu A (nguồn) | Phát biểu B (nguồn) | Ảnh hưởng | Đề xuất xử lý | Q để hỏi | Kết quả (DEC) |
|---|---|---|---|---|---|---|
| CFL-001 | Ngưỡng duyệt "100 triệu" (MTG-001 L03) | Mẫu SRC-001 có cột tổng trước thuế và tổng thanh toán | Không rõ so ngưỡng với tổng nào | Hỏi khách hàng | Q-002 | DEC-002 |

## 5. Thay đổi (CHG)

N/A – chưa có yêu cầu thay đổi nào sau khi tài liệu chuyển trạng thái Ready (20/10/2026).
