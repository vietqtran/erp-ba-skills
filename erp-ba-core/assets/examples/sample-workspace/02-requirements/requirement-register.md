---
doc: requirement-register
project: Minh An ERP
status: Ready
version: 1.0
updated: 2026-10-20
---

# Sổ yêu cầu gốc (Requirement register) — Minh An ERP

| ID | Yêu cầu (diễn đạt lại, 1 ý) | Trích nguyên văn | Nguồn | Người nêu | Loại | Module | BP | Ưu tiên | Trạng thái | Q/DEC/CHG liên quan |
|---|---|---|---|---|---|---|---|---|---|---|
| REQ-001 | Đơn mua hàng được lập và lưu trên hệ thống thay cho Excel | "Anh muốn đơn mua hàng lập trên hệ thống" | MTG-001 L02 | Trần Văn Hùng – TP Mua hàng | FR | PUR | BP-01 | Must | Đã xác nhận | DEC-001 |
| REQ-002 | Biết được đơn nào đã giao, đơn nào chưa giao | "không kiểm soát được đơn nào đã giao, đơn nào chưa" | MTG-001 L01 | Trần Văn Hùng – TP Mua hàng | FR | PUR | BP-01 | Must | Đã xác nhận | — |
| REQ-003 | Nhà cung cấp trên đơn được chọn từ danh mục, không nhập tay | "chọn nhà cung cấp và hàng hóa từ danh mục, không gõ tay" | MTG-001 L02 | Trần Văn Hùng – TP Mua hàng | FR | PUR | BP-01 | Must | Đã xác nhận | — |
| REQ-004 | Hàng hóa trên đơn được chọn từ danh mục, không nhập tay | "chọn nhà cung cấp và hàng hóa từ danh mục, không gõ tay" | MTG-001 L02 | Trần Văn Hùng – TP Mua hàng | FR | PUR | BP-01 | Must | Đã xác nhận | — |
| REQ-005 | Đơn có tổng tiền dưới 100 triệu chỉ cần Trưởng phòng Mua hàng duyệt | "Đơn dưới 100 triệu thì anh duyệt là được" | MTG-001 L03 | Trần Văn Hùng – TP Mua hàng | FR | PUR | BP-01 | Must | Đã xác nhận | Q-002, DEC-002 |
| REQ-006 | Đơn có tổng tiền từ 100 triệu trở lên phải được Giám đốc duyệt thêm sau Trưởng phòng | "từ 100 triệu trở lên phải qua Giám đốc duyệt thêm" | MTG-001 L03 | Trần Văn Hùng – TP Mua hàng | FR | PUR | BP-01 | Must | Đã xác nhận | Q-002, DEC-002 |
| REQ-007 | Kế toán xem được tất cả đơn mua nhưng không được sửa | "Kế toán cần xem được tất cả đơn mua để đối chiếu công nợ, nhưng không được sửa" | MTG-001 L04 | Nguyễn Thị Lan – Kế toán trưởng | FR | PUR | BP-01 | Must | Đã xác nhận | — |
| REQ-008 | Nhà cung cấp bắt buộc có mã số thuế | "Nhà cung cấp phải có mã số thuế" | MTG-001 L05 | Nguyễn Thị Lan – Kế toán trưởng | DATA | PUR | BP-01 | Must | Đã xác nhận | — |
| REQ-009 | Không cho tạo nhà cung cấp trùng mã số thuế | "trùng mã số thuế thì không cho tạo" | MTG-001 L05 | Nguyễn Thị Lan – Kế toán trưởng | DATA | PUR | BP-01 | Must | Đã xác nhận | — |
| REQ-010 | Nhà cung cấp đang tranh chấp bị khóa và không được chọn để đặt hàng | "Nhà cung cấp nào đang tranh chấp thì phải khóa lại, không cho đặt hàng" | MTG-001 L06 | Trần Văn Hùng – TP Mua hàng | FR | PUR | BP-01 | Must | Đã xác nhận | — |
| REQ-011 | Nhân viên mua hàng chỉ thấy đơn của chi nhánh mình | "Nhân viên mua hàng chi nhánh nào chỉ thấy đơn của chi nhánh đó" | MTG-001 L07 | Trần Văn Hùng – TP Mua hàng | FR | PUR | BP-01 | Must | Đã xác nhận | DEC-011 |
| REQ-012 | Đơn mua bằng ngoại tệ (USD) có ghi tỷ giá | "Đơn mua có cả hàng nhập khẩu tính bằng USD, cần ghi tỷ giá" | MTG-001 L08 | Nguyễn Thị Lan – Kế toán trưởng | FR | PUR | BP-01 | Must | Đã xác nhận | Q-006, DEC-006 |
| REQ-013 | Khi nhà cung cấp giao thiếu, đơn vẫn mở để nhận phần còn lại | "Khi nhà cung cấp giao thiếu thì đơn vẫn mở để giao tiếp" | MTG-001 L09 | Trần Văn Hùng – TP Mua hàng | FR | PUR | BP-01 | Must | Đã xác nhận | — |
| REQ-014 | Khi nhà cung cấp báo không giao nữa thì đóng đơn | "nếu họ báo không giao nữa thì đóng đơn" | MTG-001 L09 | Trần Văn Hùng – TP Mua hàng | FR | PUR | BP-01 | Must | Đã xác nhận | Q-003, DEC-003 |
| REQ-015 | Sửa giá hoặc số lượng của đơn đã duyệt thì phải duyệt lại từ đầu | "Đã duyệt rồi mà sửa giá hay số lượng thì phải duyệt lại từ đầu" | MTG-001 L10 | Trần Văn Hùng – TP Mua hàng | FR | PUR | BP-01 | Must | Đã xác nhận | Q-013, DEC-013 |
| REQ-016 | Báo cáo các đơn sắp đến hạn giao mà chưa nhận hàng, xem được cuối ngày | "Cuối ngày anh cần báo cáo xem đơn nào sắp đến hạn giao mà chưa nhận hàng" | MTG-001 L11 | Trần Văn Hùng – TP Mua hàng | RPT | PUR | BP-01 | Must | Đã xác nhận | Q-008, DEC-008 |
| REQ-017 | In đơn đặt hàng ra PDF có logo công ty để gửi nhà cung cấp | "In đơn đặt hàng có logo công ty để gửi nhà cung cấp, dạng PDF" | MTG-001 L12 | Nguyễn Thị Lan – Kế toán trưởng | FR | PUR | BP-01 | Must | Đã xác nhận | — |
| REQ-018 | Giao diện dễ dùng | "Giao diện thì làm sao cho dễ dùng là được" | MTG-001 L13 | Trần Văn Hùng – TP Mua hàng | NFR | PUR | BP-01 | Should | Đã xác nhận | Q-004, DEC-004 |
| REQ-019 | Hệ thống áp dụng chế độ kế toán theo Thông tư 99/2025/TT-BTC | "Công ty đang áp dụng chế độ kế toán theo Thông tư 99" | MTG-001 L14 | Nguyễn Thị Lan – Kế toán trưởng | CON | GL | BP-01 | Must | Đã xác nhận | — |
| REQ-020 | Khối lượng khoảng 300 đơn mua mỗi tháng, đơn lớn nhất khoảng 80 dòng | "Mỗi tháng bên anh khoảng 300 đơn, đơn nhiều nhất cỡ 80 dòng hàng" | MTG-001 L15 | Trần Văn Hùng – TP Mua hàng | NFR | PUR | BP-01 | Must | Đã xác nhận | Q-010, DEC-010 |
| REQ-021 | Duyệt được đơn mua trên điện thoại khi đi công tác | "đơn gấp thì phải duyệt được trên điện thoại" | MTG-001 L16 | Trần Văn Hùng – TP Mua hàng | NFR | PUR | BP-01 | Must | Đã xác nhận | Q-005, DEC-005 |
| REQ-022 | Công ty có hai chi nhánh Hà Nội và Hồ Chí Minh, mỗi chi nhánh một kho | "Bên anh có hai chi nhánh Hà Nội và Hồ Chí Minh, mỗi chi nhánh một kho" | MTG-001 L17 | Trần Văn Hùng – TP Mua hàng | CON | SYS | BP-01 | Must | Đã xác nhận | — |

## Thống kê

| Loại | Số lượng | Đã xác nhận | Cần làm rõ | Bị loại |
|---|---|---|---|---|
| FR | 14 | 14 | 0 | 0 |
| DATA | 2 | 2 | 0 | 0 |
| RPT | 1 | 1 | 0 | 0 |
| NFR | 3 | 3 | 0 | 0 |
| CON | 2 | 2 | 0 | 0 |
