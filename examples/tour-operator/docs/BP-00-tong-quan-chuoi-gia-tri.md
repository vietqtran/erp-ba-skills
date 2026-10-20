# BP-00 — Tổng quan chuỗi giá trị của doanh nghiệp điều hành tour

> Sinh tự động từ `defs/bp00_tong_quan.py` bằng bpmn-kit — sửa định nghĩa rồi chạy lại, không sửa tay file này.

![BP-00](../svg/BP-00-tong-quan-chuoi-gia-tri.svg)

File BPMN 2.0: [`bpmn/BP-00-tong-quan-chuoi-gia-tri.bpmn`](../bpmn/BP-00-tong-quan-chuoi-gia-tri.bpmn) · Ảnh: [`png/BP-00-tong-quan-chuoi-gia-tri.png`](../png/BP-00-tong-quan-chuoi-gia-tri.png)

## 1. Thông tin chung

| Mục | Nội dung |
|---|---|
| Mục tiêu | Cho thấy các quy trình BP-01 → BP-16 nối với nhau thế nào: dòng hoạch định (sản phẩm, nguồn cung), dòng đơn hàng của từng đoàn (bán → điều hành → thực hiện → quyết toán → chăm sóc), và dòng tài chính định kỳ. |
| Sự kiện kích hoạt | Ba điểm khởi động: chu kỳ hoạch định hằng tháng; khách có nhu cầu; cuối tháng kế toán. Dòng hoạch định và dòng khách hàng có nhịp khác nhau (tháng / từng yêu cầu) nên không nối bằng mũi tên tuần tự mà nối qua dữ liệu dùng chung: S&OP công bố lịch khởi hành, quỹ chỗ, giá → Kinh doanh chỉ bán trên đó; booking và số liệu bán quay về làm đầu vào cho kỳ S&OP sau. |
| Kết quả đầu ra | Sản phẩm và chỗ sẵn sàng bán; mỗi đoàn được phục vụ và quyết toán; kỳ kế toán được khóa. |
| Phạm vi | Mức tổng quan: mỗi ô là một quy trình chi tiết (call activity), bấm vào tên để xem sơ đồ chi tiết. |
| Module ERP | Toàn bộ |
| Quy trình chuẩn ERP tương ứng | Chuỗi giá trị: Plan (S&OP) → Source (hợp đồng NCC) → Make (thiết kế, điều hành) → Sell/Deliver (bán, thực hiện) → Settle (quyết toán, công nợ) → Report (khóa sổ). |

## 2. Vai trò (làn)

| Làn | Vai trò | Trách nhiệm trong quy trình |
|---|---|---|
| `DIR` | Ban Giám đốc | Hoạch định mùa vụ (S&OP). |
| `PROD` | Sản phẩm & Hợp đồng NCC | Nguồn cung và sản phẩm. |
| `SALES` | Kinh doanh (Sales / Booking) | Bán tour ghép và tour thiết kế riêng. |
| `OPS` | Điều hành (Operator) | Chốt chuyến, đặt dịch vụ, chuẩn bị đoàn. |
| `GUIDE` | Hướng dẫn viên | Thực hiện tour. |
| `ACC` | Kế toán công nợ | Quyết toán, công nợ, khóa sổ. |
| `CS` | Chăm sóc khách hàng | Chăm sóc khách hàng sau tour. |

Bên ngoài (pool hộp đen, trao đổi bằng luồng thông điệp): **Khách hàng / Đại lý / OTA**.

## 3. Các bước

| # | ID | Bước | Làn | Loại | Mô tả | Chứng từ / trạng thái | Kiểm soát |
|---|---|---|---|---|---|---|---|
| 1 | `S1` | Chu kỳ hoạch định hằng tháng | Ban Giám đốc | Sự kiện bắt đầu (hẹn giờ) |  |  |  |
| 2 | `S3` | Cuối tháng | Kế toán công nợ | Sự kiện bắt đầu (hẹn giờ) |  |  |  |
| 3 | `C04` | BP-04 Hoạch định mùa vụ (S&OP) | Ban Giám đốc | Gọi quy trình khác → BP-04 |  |  |  |
| 4 | `C15` | BP-15 Khóa sổ cuối kỳ | Kế toán công nợ | Gọi quy trình khác → BP-15 |  |  |  |
| 5 | `E3` | Kỳ kế toán đã khóa | Kế toán công nợ | Sự kiện kết thúc |  |  |  |
| 6 | `C02` | BP-02 Hợp đồng NCC & quỹ chỗ | Sản phẩm & Hợp đồng NCC | Gọi quy trình khác → BP-02 |  |  |  |
| 7 | `C03` | BP-03 Thiết kế tour & tính giá | Sản phẩm & Hợp đồng NCC | Gọi quy trình khác → BP-03 |  |  |  |
| 8 | `E1` | Sản phẩm và chỗ sẵn sàng bán | Sản phẩm & Hợp đồng NCC | Sự kiện kết thúc |  |  |  |
| 9 | `S2` | Khách có nhu cầu | Kinh doanh (Sales / Booking) | Sự kiện bắt đầu (thông điệp) |  |  |  |
| 10 | `G1` | Loại tour? | Kinh doanh (Sales / Booking) | Rẽ nhánh (XOR) |  |  |  |
| 11 | `C05` | BP-05 Bán tour ghép | Kinh doanh (Sales / Booking) | Gọi quy trình khác → BP-05 |  |  |  |
| 12 | `C06` | BP-06 Bán tour thiết kế riêng | Kinh doanh (Sales / Booking) | Gọi quy trình khác → BP-06 |  |  |  |
| 13 | `C07` | BP-07 Chốt chuyến & trả chỗ | Điều hành (Operator) | Gọi quy trình khác → BP-07 |  |  |  |
| 14 | `C08` | BP-08 Đặt dịch vụ & chuẩn bị đoàn | Điều hành (Operator) | Gọi quy trình khác → BP-08 |  |  |  |
| 15 | `C09` | BP-09 Thực hiện tour & xử lý sự cố | Hướng dẫn viên | Gọi quy trình khác → BP-09 |  |  |  |
| 16 | `C10` | BP-10 Quyết toán & đóng hồ sơ tour | Kế toán công nợ | Gọi quy trình khác → BP-10 |  |  |  |
| 17 | `C14` | BP-14 CSKH & khiếu nại | Chăm sóc khách hàng | Gọi quy trình khác → BP-14 |  |  |  |
| 18 | `E2` | Đoàn đã phục vụ và quyết toán xong | Kế toán công nợ | Sự kiện kết thúc |  |  |  |

## 4. Điểm quyết định

| Cổng | Câu hỏi / điều kiện | Nhánh → bước tiếp theo |
|---|---|---|
| `G1` | Loại tour? | Tour ghép (mặc định) → `C05` BP-05 Bán tour ghép<br>Thiết kế riêng → `C06` BP-06 Bán tour thiết kế riêng |

## 5. Trao đổi với bên ngoài

| Từ | Đến | Thông điệp |
|---|---|---|
| Khách hàng / Đại lý / OTA | `S2` Khách có nhu cầu | Yêu cầu, đặt chỗ |

## 6. Danh mục quy trình

| Mã | Quy trình | Nhóm | Quy trình chuẩn ERP | Module |
|---|---|---|---|---|
| [BP-01](BP-01-quan-ly-du-lieu-goc.md) | Quản lý dữ liệu gốc | Nền tảng | Master Data Management | MDM, AR, AP |
| [BP-02](BP-02-hop-dong-ncc-quy-cho.md) | Hợp đồng NCC & quỹ chỗ | Hoạch định – nguồn cung | Procure-to-Pay (nguồn cung, hợp đồng khung); Supplier Scheduling | PUR, AP |
| [BP-03](BP-03-thiet-ke-tour-tinh-gia.md) | Thiết kế tour & tính giá | Hoạch định – sản phẩm | Thiết kế sản phẩm, định giá (BOM, costing, pricing) | Sản phẩm, COST, SAL |
| [BP-04](BP-04-hoach-dinh-mua-vu-lich-khoi-hanh.md) | Hoạch định mùa vụ (S&OP) | Hoạch định | Sales & Operations Planning | Hoạch định, BUD |
| [BP-05](BP-05-ban-tour-ghep.md) | Bán tour ghép | Bán hàng | Order-to-Cash: nhận đơn, ATP, kiểm tra tín dụng | SAL, AR, CB |
| [BP-06](BP-06-ban-tour-thiet-ke-rieng.md) | Bán tour thiết kế riêng | Bán hàng | Quote-to-Cash (thiết kế theo đơn); dựng chương trình thủ công hoặc bằng trợ lý AI | CRM, SAL, tích hợp AI |
| [BP-07](BP-07-chot-chuyen-tra-cho.md) | Chốt chuyến & trả chỗ | Điều hành | Master scheduling (mức chuyến), time fence, supplier scheduling | Lịch khởi hành, PUR |
| [BP-08](BP-08-dat-dich-vu-chuan-bi-doan.md) | Đặt dịch vụ & chuẩn bị đoàn | Điều hành | Procure-to-Pay: đặt hàng từ định mức | OPS, PUR, CB |
| [BP-09](BP-09-thuc-hien-tour-xu-ly-su-co.md) | Thực hiện tour & xử lý sự cố | Điều hành | Thực thi & phản hồi; nghiệm thu dịch vụ | OPS, SVC |
| [BP-10](BP-10-quyet-toan-dong-ho-so-tour.md) | Quyết toán & đóng hồ sơ tour | Tài chính – giá thành | Giá thành theo đơn/dự án; đóng dự án | COST, CB, GL |
| [BP-11](BP-11-thu-tien-cong-no-phai-thu.md) | Thu tiền & công nợ phải thu | Tài chính | Order-to-Cash: hóa đơn, thu tiền, đối chiếu | AR, TAX, CB |
| [BP-12](BP-12-thanh-toan-ncc-cong-no-phai-tra.md) | Thanh toán NCC & công nợ phải trả | Tài chính | Procure-to-Pay: xác minh hóa đơn, thanh toán | AP, TAX, CB |
| [BP-13](BP-13-thay-doi-huy-booking-hoan-tien.md) | Thay đổi, hủy booking & hoàn tiền | Bán hàng – ngoại lệ | Change order, trả lại/giảm trừ | SAL, OPS, AR, TAX |
| [BP-14](BP-14-cham-soc-khach-hang-khieu-nai.md) | CSKH & khiếu nại | Dịch vụ khách hàng | CRM dịch vụ: ticket, SLA, CSAT | CRM, SVC |
| [BP-15](BP-15-khoa-so-cuoi-ky.md) | Khóa sổ cuối kỳ | Tài chính | Record-to-Report (month-end close) | GL, AR, AP, COST |
| [BP-16](BP-16-hdv-cong-tac-chi-tra-thu-lao.md) | HDV cộng tác & chi trả thù lao | Nhân sự | Quản lý cộng tác viên và chi trả | HR, AP, CB |

## 7. Căn cứ từ sách

- **Wallace & Kremzar, ch17** ([nguồn](../../../books/wallace-erp-implementation/chapters/ch17-appendix-a-fundamentals-of-erp.md)) — Hệ phân cấp hoạch định ERP: kế hoạch kinh doanh → S&OP → lịch chi tiết → thực thi → phản hồi; một bộ số.
- **Wallace & Kremzar, ch03** ([nguồn](../../../books/wallace-erp-implementation/chapters/ch03-company-wide-implementation-overview.md)) — Lập lịch triển khai theo chức năng nghiệp vụ, không theo module phần mềm.
- **Parthasarathy, ch03** ([nguồn](../../../books/parthasarathy-erp-fundamentals/chapters/ch03-erp-modules.md)) — Luồng liên module Sales → Shipping → Billing; mỗi quy trình phải vẽ liên module.
- **O'Leary, ch03** ([nguồn](../../../books/oleary-erp-systems-lifecycle/chapters/ch03-erp-systems-background.md)) — MAPs: Models – Artifacts – Processes; quy trình liên chức năng là xương sống của đặc tả.
- **Elbardan & Kholeif, ch10** ([nguồn](../../../books/elbardan-erp-governance-audit/chapters/ch10-cross-case-analysis-discussion.md)) — 11 giả định kiểm soát của ERP: tích hợp, chuẩn hóa, tự động hóa, phòng ngừa, giám sát liên tục…
