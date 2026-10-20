---
doc: report-spec
id: FN-PUR-03
name: Báo cáo tình hình thực hiện đơn mua hàng
module: PUR
type: Báo cáo
priority: Must
status: Ready
version: 1.0
updated: 2026-10-20
project: Minh An ERP
---

# FN-PUR-03 — Báo cáo tình hình thực hiện đơn mua hàng

## 0. Thông tin & truy vết

| Mục | Giá trị |
|---|---|
| Báo cáo | RPT-PUR-01 (catalogs/reports.md) |
| Nguồn yêu cầu | REQ-016 đơn sắp đến hạn giao mà chưa nhận, xem cuối ngày · REQ-002 biết đơn đã giao, chưa giao · REQ-007, REQ-011 phạm vi xem · DEC-008 "sắp đến hạn" = 3 ngày |
| Mẫu khách hàng cung cấp | N/A – khách hàng chưa có báo cáo này (đang theo dõi thủ công, MTG-001 L01) |
| Bắt buộc theo luật | Không |
| Chức năng sinh dữ liệu nguồn | FN-PUR-02 |

## 1. Mục đích & người dùng

- **Câu hỏi quản trị mà báo cáo trả lời:** đến hôm nay, những dòng hàng nào của đơn mua đã duyệt còn chưa nhận đủ, dòng nào đã quá hạn giao, dòng nào sắp đến hạn trong PRM-PUR-002 ngày tới, để nhắc nhà cung cấp.
- **Người dùng & tần suất:** ROLE-PUR-STAFF, ROLE-PUR-MGR xem cuối mỗi ngày; ROLE-DIRECTOR, ROLE-ACC xem khi cần.

## 2. Phân quyền & phạm vi dữ liệu

| Vai trò | Xem | Xuất file | Phạm vi dữ liệu | Trường bị ẩn |
|---|---|---|---|---|
| ROLE-PUR-STAFF | ✔ | ✖ | Chi nhánh của người dùng | Không |
| ROLE-PUR-MGR | ✔ | ✖ | Công ty | Không |
| ROLE-DIRECTOR | ✔ | ✖ | Công ty | Không |
| ROLE-ACC | ✔ | ✖ | Công ty | Không |

Xuất file: N/A – khách hàng chưa yêu cầu (MTG-001); xem trên màn hình.

## 3. Tham số lọc

| # | Tham số | Kiểu | Bắt buộc | Mặc định | Giá trị / lookup | Kiểm tra |
|---|---|---|---|---|---|---|
| 1 | Ngày xem | Ngày | Có | Hôm nay | — | Bắt buộc; để trống báo MSG-PUR-03-02 |
| 2 | Chi nhánh | Danh sách chọn | Có | Chi nhánh của người dùng (ROLE-PUR-STAFF, khóa không đổi được); "Tất cả" (vai trò phạm vi Công ty) | MD-BRANCH | Theo phạm vi mục 2 |
| 3 | Nhà cung cấp | Chọn một | Không | Tất cả | MD-VENDOR (mọi trạng thái) | — |
| 4 | Tình trạng giao | Chọn nhiều | Có | Quá hạn, Sắp đến hạn | Quá hạn · Sắp đến hạn · Chưa đến hạn | Ít nhất 1 giá trị; lỗi báo MSG-PUR-03-02 |

## 4. Bố cục & cột

| # | Cột | Nguồn dữ liệu (bảng.trường) | Công thức / cách tính | Định dạng | Tổng cộng? |
|---|---|---|---|---|---|
| 1 | Tình trạng giao | Tính | Theo mục 5 "Phân loại tình trạng" | Chữ, tô đỏ "Quá hạn", vàng "Sắp đến hạn" | Không |
| 2 | Số đơn | PURCHASE_ORDER.doc_no | — | Chữ, là liên kết mở đơn | Không |
| 3 | Ngày đơn | PURCHASE_ORDER.doc_date | — | dd/MM/yyyy | Không |
| 4 | Chi nhánh | MD-BRANCH.name qua PURCHASE_ORDER.branch_id | — | Chữ | Không |
| 5 | Nhà cung cấp | MD-VENDOR.code, name qua PURCHASE_ORDER.vendor_id | "mã – tên" | Chữ | Không |
| 6 | Mã hàng, Tên hàng, ĐVT | MD-ITEM qua PURCHASE_ORDER_LINE.item_id; PURCHASE_ORDER_LINE.uom | — | Chữ | Không |
| 7 | Số lượng đặt | PURCHASE_ORDER_LINE.quantity | — | #.##0,### | Không |
| 8 | Đã nhận | PURCHASE_ORDER_LINE.received_qty | — | #.##0,### | Không |
| 9 | Còn lại | Tính | max(Số lượng đặt − Đã nhận, 0) | #.##0,### | Không |
| 10 | Ngày giao dự kiến | PURCHASE_ORDER.expected_date | — | dd/MM/yyyy | Không |
| 11 | Số ngày còn lại | Tính | Ngày giao dự kiến − Ngày xem (số âm = số ngày quá hạn) | Số nguyên | Không |
| 12 | Trạng thái đơn | PURCHASE_ORDER.status | Nhãn tiếng Việt của mã | Chữ | Không |

- **Nhóm / tổng phụ:** nhóm theo Tình trạng giao theo thứ tự Quá hạn, Sắp đến hạn, Chưa đến hạn; đầu mỗi nhóm hiển thị số đơn và số dòng của nhóm.
- **Sắp xếp:** trong nhóm theo Ngày giao dự kiến tăng dần, rồi Số đơn, rồi số dòng của đơn.
- **Tiêu đề, chân trang, chữ ký (nếu mẫu luật):** tiêu đề "Tình hình thực hiện đơn mua hàng đến ngày {Ngày xem}"; chân trang: thời điểm chạy, người chạy. Không có chữ ký.

## 5. Logic lấy số liệu

| Mục | Quy tắc |
|---|---|
| Chứng từ được tính | Dòng của DOC-PO có trạng thái đơn APPROVED hoặc PARTIAL và Còn lại > 0; loại trừ DRAFT, PENDING, RETURNED, REJECTED, COMPLETED, CLOSED, CANCELLED |
| Ngày dùng để lọc | Ngày giao dự kiến của đơn so với Ngày xem |
| Phân loại tình trạng | Quá hạn: Ngày giao dự kiến < Ngày xem. Sắp đến hạn: Ngày xem ≤ Ngày giao dự kiến ≤ Ngày xem + PRM-PUR-002. Chưa đến hạn: Ngày giao dự kiến > Ngày xem + PRM-PUR-002 |
| Số dư đầu kỳ | N/A – báo cáo tình trạng tại một thời điểm, không có số dư |
| Quy đổi tiền tệ | N/A – báo cáo không có cột tiền |
| Xử lý dữ liệu đặc biệt | Số đã nhận lấy giá trị hiện hành (đã trừ phiếu nhập bị đảo); đơn đang điều chỉnh (DRAFT, PENDING) không hiển thị cho tới khi duyệt lại |
| Kết quả rỗng | Không có dòng nào thỏa bộ lọc → hiển thị MSG-PUR-03-01 |

## 6. Tương tác

| Hành vi | Đặc tả |
|---|---|
| Xem chi tiết (drill-down) | Bấm Số đơn mở màn hình chi tiết FN-PUR-02 nếu người dùng có quyền xem đơn đó |
| Xuất file | N/A – khách hàng chưa yêu cầu |
| Lưu bộ lọc / lập lịch gửi | N/A – khách hàng chưa yêu cầu |

## 7. Hiệu năng & khối lượng

| Mục | Yêu cầu |
|---|---|
| Khối lượng dữ liệu dự kiến | Khoảng 300 đơn/tháng, tối đa khoảng 80 dòng/đơn (REQ-020); số dòng còn mở thường nhỏ hơn 24.000 |
| Thời gian chạy tối đa | ≤ 2 giây ở p95 cho trang đầu kết quả, theo chỉ tiêu NFR-PERF-01 (DEC-010) |
| Chạy trực tuyến hay nền / snapshot | Trực tuyến, đọc dữ liệu hiện hành |

## 8. Ví dụ số liệu kiểm tra

Ngày xem 20/10/2026, PRM-PUR-002 = 3.

| Dữ liệu đầu vào (chứng từ mẫu) | Kết quả mong đợi trên báo cáo |
|---|---|
| PO-HN-2026-00010 APPROVED, giao dự kiến 18/10/2026, dòng 1 đặt 10 đã nhận 0 | Nhóm Quá hạn; Còn lại 10; Số ngày còn lại −2 |
| PO-HN-2026-00011 PARTIAL, giao dự kiến 23/10/2026, dòng 1 đặt 10 đã nhận 4, dòng 2 đặt 5 đã nhận 5 | Nhóm Sắp đến hạn; chỉ dòng 1 xuất hiện, Còn lại 6; Số ngày còn lại 3 |
| PO-HN-2026-00012 APPROVED, giao dự kiến 24/10/2026, dòng 1 đặt 2 đã nhận 0 | Không hiển thị với bộ lọc mặc định; hiển thị ở nhóm Chưa đến hạn khi chọn thêm "Chưa đến hạn" |
| PO-HN-2026-00013 CLOSED, giao dự kiến 15/10/2026, còn lại 3 | Không hiển thị |

## 9. Thông báo & lỗi

| ID | Điều kiện | Nội dung | Loại |
|---|---|---|---|
| MSG-PUR-03-01 | Không có dòng nào thỏa bộ lọc | "Không có dòng hàng nào phù hợp điều kiện lọc." | Thông tin |
| MSG-PUR-03-02 | Tham số lọc không hợp lệ (mục 3) | "Điều kiện lọc chưa hợp lệ: {lý do}." | Lỗi |

## 10. Câu hỏi mở, giả định, quyết định liên quan

| ID | Nội dung | Trạng thái |
|---|---|---|
| DEC-008 | "Sắp đến hạn" = trong vòng 3 ngày (PRM-PUR-002) | Đã chốt |
| DEC-010 | Chỉ tiêu hiệu năng | Đã chốt |

## 11. Lịch sử thay đổi

| Phiên bản | Ngày | Người sửa | Nội dung | CHG / vòng review |
|---|---|---|---|---|
| 0.1 | 15/10/2026 | BA | Tạo mới | — |
| 1.0 | 20/10/2026 | BA | Chuyển trạng thái Ready | — |
