---
name: erp-ba-step3-specification
description: "Bước 3 của bộ skill BA ERP — phân rã nghiệp vụ thành module và chức năng theo chuẩn ERP (hệ thống, danh mục, nghiệp vụ, phân quyền & tham số, báo cáo) rồi viết đặc tả từng chức năng đủ để dev code ngay, gồm truy vết nguồn, vai trò kể cả vai trò thao tác một phần, ma trận phân quyền, user story + tiêu chí nghiệm thu Given/When/Then, luồng chính/thay thế/ngoại lệ, sơ đồ swimlane, sơ đồ quyết định (if-else, hình thoi), sequence, state, FR, NFR, business rule, trường dữ liệu + ER, màn hình, tham số hệ thống, hạch toán, tích hợp, thông báo lỗi, tình huống biên; cùng các catalog dùng chung. Template 21 mục, nghiệm thu bằng checklist C3/C3F/C3R. Dùng khi người dùng muốn viết SRS, đặc tả chức năng/màn hình/báo cáo, user story, use case, phân rã module, thiết kế phân quyền hay tham số cho ERP/phần mềm quản trị doanh nghiệp — kể cả khi chỉ nói “viết spec”, “viết tài liệu cho dev”. English — code-ready ERP functional specifications."
---

# Bước 3 — Phân rã nghiệp vụ thành chức năng & đặc tả chi tiết

Thuộc bộ skill BA ERP: `erp-ba-core` → `erp-ba-step1-research` → `erp-ba-step2-requirements` → **bước 3 (skill này)** → `erp-ba-step4-verify` → `erp-ba-step5-review`.

Đường dẫn: `<skill-dir>` = thư mục chứa file SKILL.md này; `<core>` = thư mục `erp-ba-core` nằm cạnh (`<skill-dir>/../erp-ba-core`). Không thấy `<core>` → báo người dùng cài đủ bộ skill.

## Mục lục
1. Mục tiêu, đầu ra & định nghĩa "đủ để code"
2. Nguyên tắc bắt buộc
3. Thứ tự làm việc
4. Phân rã: module → chức năng
5. Catalog dùng chung
6. Quy tắc chung (BR-GEN) & NFR
7. Viết đặc tả một chức năng — hướng dẫn từng mục
8. Đặc tả báo cáo
9. Phạm vi lớn & quản lý thay đổi
10. Nghiệm thu & chuyển bước

---

## 1. Mục tiêu, đầu ra & định nghĩa "đủ để code"

Một đặc tả "đủ để code" khi dev và QA **không cần hỏi BA câu nào** để:
- tạo bảng dữ liệu (trường, kiểu, độ dài, bắt buộc, mặc định, ràng buộc, khóa ngoại tới danh mục);
- lập trình mọi hành động trên màn hình, mọi chuyển trạng thái, mọi kiểm tra, mọi công thức (kể cả làm tròn);
- biết ai được làm gì trên dữ liệu nào (vai trò × hành động × phạm vi dữ liệu × trạng thái);
- biết chức năng làm thay đổi gì ở module khác (tồn kho, công nợ, sổ cái, ngân sách) và hoàn tác ra sao khi hủy/đảo;
- biết thông báo hiển thị gì trong từng tình huống lỗi;
- viết được test case từ AC, BR, MSG và tình huống biên.

**Mẫu đã điền đầy đủ ở mức này — đọc trước khi viết chức năng đầu tiên:** `<core>/assets/examples/sample-workspace/03-specification/functions/PUR/FN-PUR-02-don-mua-hang.md` (chứng từ có duyệt 2 cấp); cùng thư mục: `FN-PUR-01` (danh mục), `FN-PUR-03` (báo cáo); catalog mẫu ở `.../03-specification/catalogs/`.

| Đầu ra (trong workspace) | Template (trong `<skill-dir>/assets/templates/03-specification/`) |
|---|---|
| `03-specification/srs-overview.md` | `srs-overview.md` |
| `03-specification/catalogs/*.md` (7 file) | `catalogs/*.md` |
| `03-specification/functions/<MOD>/FN-*.md` | `function-spec.md`; báo cáo dùng `report-spec.md` |

Nghiệm thu: `<skill-dir>/references/checklists/C3-specification.md` (toàn bộ), `C3F-function.md` (mỗi chức năng), `C3R-report.md` (mỗi báo cáo).
Workspace chưa có → `python3 <core>/scripts/ba.py init <root> --project "<Tên dự án>"`; chưa có sổ yêu cầu → làm `erp-ba-step2-requirements` tối thiểu cho phạm vi cần đặc tả trước. Quy ước ID/marker/trạng thái: `<core>/references/conventions.md`.

## 2. Nguyên tắc bắt buộc

1. **Không có nguồn thì không viết.** Mỗi chức năng, FR, BR, con số truy được về REQ/DEC hoặc chuẩn/luật cụ thể (cột Nguồn). Thông tin thiếu → `[CẦN XÁC NHẬN: Q-…]` + Q trong issue-log; không đoán. Lý do: một chỗ trống được đánh dấu rẻ hơn nhiều so với một quy tắc bịa mà dev code theo.
2. **Đề xuất phải lộ diện.** Chức năng/quy tắc "nên có theo chuẩn" mà khách hàng chưa yêu cầu → gắn `[ĐỀ XUẤT → Q-…]` để khách hàng quyết — chặn "thừa chức năng" mà vẫn giữ giá trị tư vấn.
3. **Định nghĩa một lần, tham chiếu bằng ID.** Vai trò, tham số, danh mục, chứng từ, trạng thái chỉ định nghĩa trong `catalogs/`; file chức năng chỉ dùng ID — chặn mâu thuẫn.
4. **Chuẩn ERP trước, tùy biến sau.** Trước mỗi chức năng đọc file quy trình chuẩn (`<core>/references/processes/`), pattern (`<core>/references/design-patterns.md`), ngành (`<core>/references/industries/`). Chỗ khác chuẩn phải có REQ/DEC.
5. **Giá trị có thể thay đổi là tham số**, không viết cứng (ngưỡng, tỷ lệ, số ngày, bật/tắt bước) — định nghĩa trong `catalogs/system-parameters.md`.
6. **Không xóa mục template**; `N/A – <lý do>`.

## 3. Thứ tự làm việc

1. Đọc lại `requirement-register.md`, `requirements-overview.md`, `issue-log.md` (câu trả lời mới nhất).
2. Lập danh sách module & chức năng (srs-overview §2–§3) — mục 4 dưới đây.
3. Lập catalog — mục 5.
4. Viết BR-GEN, NFR, chế độ kế toán, chuyển đổi dữ liệu — mục 6.
5. Viết từng chức năng theo thứ tự quy trình (danh mục trước, rồi chứng từ theo luồng: đề nghị → đơn → nhận → hóa đơn → thanh toán), tạo file bằng:
   ```bash
   python3 <core>/scripts/ba.py new-function <root> --id FN-PUR-03 --name "<Tên>" --type "<Chứng từ|Danh mục|Phê duyệt|Cấu hình|Tích hợp|Tác vụ nền|Tiện ích|Báo cáo>"
   ```
   (ID con FR/US/AC/BR/MSG được đánh số sẵn). Xong mỗi module: `ba.py lint` + `ba.py trace`.
6. Cập nhật catalog khi chức năng phát hiện thêm vai trò/tham số/trạng thái — luôn định nghĩa ở catalog, không trong file chức năng.

## 4. Phân rã module → chức năng

### 4.1 Năm thành phần của một sản phẩm ERP (kiểm cho từng module)

| Thành phần | Gồm những chức năng gì | Ví dụ (module Mua hàng) |
|---|---|---|
| Hệ thống / nền tảng | Thiết lập module, đánh số chứng từ, cấu hình luồng duyệt, mẫu in, nhập/xuất dữ liệu, nhật ký | Thiết lập tham số mua hàng; cấu hình luồng duyệt đơn mua |
| Danh mục | Một chức năng quản lý cho mỗi danh mục module dùng | Nhà cung cấp, nhóm NCC, bảng giá mua, điều khoản thanh toán |
| Nghiệp vụ | Một chức năng cho mỗi loại chứng từ (trọn vòng đời) + tác vụ nền + tiện ích | Đề nghị mua hàng, yêu cầu báo giá, đơn mua hàng, trả hàng NCC |
| Phân quyền & tham số | Vai trò, ma trận quyền, hạn mức duyệt, tham số hệ thống | Hạn mức duyệt đơn mua theo giá trị |
| Báo cáo | Báo cáo vận hành, quản trị, bắt buộc theo luật, dashboard | Tình hình thực hiện đơn mua; phân tích giá mua |

Danh sách chức năng chuẩn từng module: `<core>/references/erp-modules-catalog.md`. Bảng độ phủ srs-overview §3.1 không được có ô trống không giải thích — ô trống thường là dấu hiệu **thiếu** (có chứng từ mà không có báo cáo theo dõi; có danh mục được dùng mà không có chức năng quản lý).

### 4.2 Độ mịn (một chức năng = một file đặc tả)

- **Một loại chứng từ = một chức năng** bao trọn vòng đời (tạo, sửa, gửi duyệt, duyệt, hủy, đóng, in…). Không tách "Tạo đơn" và "Sửa đơn" — dùng chung dữ liệu, trạng thái, quy tắc; tách ra sinh mâu thuẫn.
- Tách chức năng riêng khi một bước có **màn hình, vai trò và logic riêng đáng kể**: "Hộp duyệt chung", "Đối chiếu 3 chiều hóa đơn mua", "Chạy MRP".
- **Một danh mục = một chức năng**; danh mục rất đơn giản cùng cấu trúc (đơn vị tính, nhóm khách hàng…) có thể gộp, mỗi danh mục một bảng trường.
- **Mỗi tác vụ nền** (tính giá xuất kho, khấu hao, kết chuyển cuối kỳ, đồng bộ hóa đơn) là một chức năng loại "Tác vụ nền". **Mỗi báo cáo** (hoặc nhóm cùng nguồn dữ liệu) một chức năng loại "Báo cáo". **Mỗi tích hợp** (INT) một chức năng loại "Tích hợp" (hoặc nằm trong chức năng nghiệp vụ nếu chỉ là một lời gọi đơn giản — vẫn đặc tả đủ mục 14).
- Tên chức năng là danh từ đối tượng nghiệp vụ, theo thuật ngữ khách hàng ("Đơn mua hàng", "Danh mục nhà cung cấp"); mã `FN-<MOD>-<NN>` theo thứ tự quy trình.
- Mỗi chức năng có Nguồn: REQ, DEC, hoặc chuẩn/FEAT kèm `[ĐỀ XUẤT → Q-…]`. Chức năng hay bị quên (chỉ thêm khi REQ cần hoặc dưới dạng đề xuất): hộp duyệt chung & ủy quyền duyệt; cấu hình đánh số; khóa kỳ; nhập số dư đầu kỳ; mẫu in; nhật ký thao tác; quản lý người dùng & vai trò; nhập danh mục từ Excel; thông báo & nhắc hạn; đính kèm; dashboard; đối chiếu công nợ; kiểm kê; đóng/mở kỳ kho.

## 5. Catalog dùng chung (định nghĩa một lần)

| Catalog | Điền gì | Kiểm tra |
|---|---|---|
| `roles-permissions.md` | Vai trò (theo cơ cấu tổ chức ở bước 2), ma trận tổng hợp FN × ROLE (Chính / Duyệt / Một phần / Xem / —), SoD, hạn mức duyệt, chính sách tài khoản | Mọi ROLE dùng ở FN có ở đây; mức trong ma trận khớp FN §2.1 (lint kiểm) |
| `master-data.md` | Mỗi danh mục: quy tắc mã, trường chính, quy tắc ngừng dùng/xóa, có duyệt không, nhập Excel không, FN quản lý | Mỗi MD có FN quản lý hoặc nguồn đồng bộ |
| `document-types.md` | Mỗi chứng từ: mẫu đánh số, **bộ trạng thái chuẩn** (chỉ mã ở conventions §6), ảnh hưởng khi hoàn tất, cần duyệt, tạo từ / sinh ra, FN, mẫu in | Trạng thái ở FN §7 ⊆ bộ trạng thái ở đây (lint kiểm) |
| `system-parameters.md` | Mỗi giá trị nghiệp vụ có thể thay đổi: phạm vi, kiểu, giá trị cho phép, mặc định, hiệu lực theo ngày, ai sửa, **ảnh hưởng theo từng giá trị** | Không có ngưỡng/tỷ lệ "viết cứng" trong FR/BR |
| `reports.md` | Mỗi báo cáo: mục đích, người dùng, bắt buộc theo luật (mẫu số, căn cứ), tần suất, FN đặc tả | Mỗi RPT có FN |
| `integrations-notifications.md` | Tích hợp: hướng, dữ liệu, trigger, phương thức, xử lý lỗi & đối soát. Thông báo: sự kiện, người nhận, kênh, nội dung | Không có tích hợp "chung chung" |
| `glossary.md` | Thuật ngữ dự án ↔ thuật ngữ chuẩn (`<core>/references/glossary.md`) | Một khái niệm một tên |

Nội dung chuẩn để gợi ý: vai trò, SoD, tham số theo module — `<core>/references/security-and-parameters.md`; danh mục & chứng từ — `<core>/references/erp-modules-catalog.md` và các file quy trình; báo cáo — `<core>/references/reports-catalog.md`. Mã trong thư viện (ví dụ `PRM-PUR-004`) chỉ là gợi ý: trong dự án luôn cấp ID theo catalog dự án và ghi nguồn tham chiếu.

## 6. Quy tắc chung (BR-GEN) & NFR

- BR-GEN tối thiểu các nhóm: làm tròn (từng dòng hay tổng), tiền tệ & tỷ giá, đánh số chứng từ, ngày chứng từ vs ngày ghi sổ, khóa kỳ, xóa/hủy/đảo, lưu vết, múi giờ & định dạng, đa công ty/chi nhánh, đính kèm (nếu có yêu cầu). Gợi ý: `<core>/references/design-patterns.md` (P02, P05, P06, P07, P08, P14), `<core>/references/regulations/vn-accounting.md`.
- NFR đo được (`<core>/references/nfr-catalog.md`). Con số mặc định do BA đề xuất phải có Q để khách hàng xác nhận.
- srs-overview §12: chốt chế độ kế toán (TT99/2025/TT-BTC cho doanh nghiệp nói chung từ 01/01/2026; doanh nghiệp nhỏ và vừa có thể dùng TT133/2016 — xem `<core>/references/regulations/vn-accounting.md`), phương pháp tính giá xuất kho, hóa đơn điện tử, đồng tiền hạch toán — chưa chốt thì Q.

## 7. Viết đặc tả một chức năng — hướng dẫn từng mục

Trước khi viết: mở file quy trình chuẩn liên quan, pattern liên quan, và các REQ nguồn. Mục tiêu là **chuẩn ERP + đúng yêu cầu khách hàng**, chênh lệch nào cũng có nguồn.

| Mục | Cách điền | Lỗi hay gặp |
|---|---|---|
| 0. Truy vết | REQ nguồn (1 dòng mỗi REQ), BP, pattern (P01…P18), file quy trình chuẩn, upstream/downstream, DOC/MD/PRM/RPT/INT/NTF | Bỏ trống upstream/downstream → luồng chứng từ đứt |
| 1. Mô tả | Mục đích, trong/ngoài phạm vi (nói rõ chức năng nào lo phần ngoài phạm vi), trigger, tiền/hậu điều kiện | Hậu điều kiện chỉ nói ở module hiện tại |
| 2. Vai trò & quyền | 2.1 liệt kê **cả vai trò thao tác một phần** (kế toán chỉ sửa tài khoản hạch toán; thủ kho chỉ xem) và "Hệ thống" (job tự động). 2.2 ma trận hành động chuẩn × vai trò, mỗi ô có phạm vi dữ liệu và điều kiện trạng thái. 2.3 quyền theo trường. 2.4 SoD & hạn mức (SOD/PRM) | "Admin có toàn quyền"; quên phạm vi dữ liệu |
| 3. User story & AC | Mỗi vai trò chính ≥ 1 story; mỗi story ≥ 1 AC Cho trước/Khi/Thì với **giá trị cụ thể**; có AC cho luồng thay thế, ngoại lệ, phân quyền (vai trò không có quyền bị chặn) | AC chung chung "hệ thống hoạt động đúng" |
| 4. Luồng | 4.1 swimlane (subgraph theo vai trò + "Hệ thống"); 4.2 bảng bước (vai trò, hành động, xử lý hệ thống, BR, trạng thái sau); 4.3 thay thế; 4.4 ngoại lệ (mỗi cái có MSG) | Sơ đồ và bảng mô tả hai luồng khác nhau |
| 5. Sơ đồ quyết định | Gom mọi điều kiện rẽ nhánh trong BR thành hình thoi; mỗi nhánh có nhãn; mỗi lá là kết quả cụ thể (MSG / trạng thái / hành động) — "biểu đồ if-else" để dev chuyển thẳng thành code | Hình thoi thiếu nhánh "Không" |
| 6. Sequence | Người dùng → Giao diện → Dịch vụ module → CSDL → module khác / duyệt / thông báo / hệ thống ngoài; kiểm tra, ghi, ghi sổ, phát sự kiện, nhánh lỗi (`alt`), phạm vi giao dịch | Chỉ vẽ đường thành công |
| 7. Trạng thái | stateDiagram-v2 (ID trạng thái là mã chuẩn), bảng chuyển trạng thái (từ, hành động, đến, vai trò, điều kiện, tác động), ma trận sửa trường theo trạng thái; không có trạng thái cụt; hủy/đảo được định nghĩa | Tên trạng thái khác catalog |
| 8. FR | Mỗi dòng một yêu cầu kiểm thử được, PHẢI/KHÔNG ĐƯỢC/NÊN/ĐƯỢC PHÉP, có Nguồn và AC | Gộp nhiều yêu cầu trong một dòng |
| 9. BR | "Khi [điều kiện] thì [kết quả]"; loại; nguồn; MSG nếu là Validation. Bảng công thức: đại lượng, công thức, làm tròn, thứ tự | Ngưỡng viết cứng thay vì PRM |
| 10. Dữ liệu | ER diagram; bảng trường cho mọi bảng: tên, tên kỹ thuật (snake_case), kiểu, độ dài/độ chính xác, bắt buộc, mặc định, lookup, kiểm tra, trạng thái được sửa; dữ liệu sinh ra ở module khác & cách hoàn tác | Thiếu trường hệ thống (người tạo, ngày tạo, phiên bản, chi nhánh) |
| 11. Giao diện | Danh sách: cột, lọc mặc định, tìm kiếm, sắp xếp, phân trang, hành động đơn lẻ/hàng loạt, xuất file. Chi tiết: vùng/tab, thứ tự trường, nút theo trạng thái × vai trò và hành vi từng nút. Phác thảo/link Figma; mẫu in | Không nói nút nào hiện khi nào |
| 12. Tham số | Mỗi PRM: hành vi theo **từng** giá trị | "Theo tham số hệ thống" mà không nói tham số nào |
| 13. Hạch toán | Bút toán từng sự kiện (ghi sổ, hủy, đảo, điều chỉnh) theo chế độ kế toán dự án; đối tượng chi tiết; Nợ = Có. Tham khảo mục 8 của file quy trình chuẩn | Quên bút toán hủy/đảo; ghi doanh thu sai thời điểm |
| 14. Tích hợp | Sự kiện liên chức năng (đồng bộ/bất đồng bộ, khi lỗi); hệ thống ngoài (INT: dữ liệu, định dạng, thử lại, đối soát); thông báo (NTF) | "Đồng bộ với kế toán" mà không nói dữ liệu gì, khi nào |
| 15. Báo cáo | RPT nào dùng dữ liệu này và cách xuất hiện | — |
| 16. NFR riêng | Đồng thời (khóa lạc quan theo phiên bản), khối lượng, hiệu năng, audit, lưu trữ — có số đo | "Hệ thống phải nhanh" |
| 17. MSG | Mọi validation, ngoại lệ, xác nhận: mã, điều kiện, nội dung tiếng Việt có tham số ({số chứng từ}, {giá trị}), loại, chặn/không chặn | "Có lỗi xảy ra" |
| 18. Biên & kiểm thử | 0/âm, vượt hạn mức/tồn, trùng, đồng thời, kỳ đã khóa, danh mục ngừng dùng, đổi quyền giữa chừng, sửa sau duyệt, đa tiền tệ; kịch bản kiểm thử gắn AC | Bỏ qua đồng thời và kỳ đã khóa |
| 19. Câu hỏi mở | Q/ASM/DEC liên quan (định nghĩa ở issue-log) | Ghi câu hỏi ở đây mà không đưa vào issue-log |
| 20. Lịch sử | Phiên bản, ngày, người, nội dung, CHG/vòng review | — |

**Phép thử cuối (C3F-30, C3F-31):** đóng vai dev rồi vai QA, liệt kê mọi câu bạn sẽ phải hỏi BA. Mỗi câu là một chỗ phải sửa hoặc một Q. Chỉ khi danh sách rỗng mới trả lời Yes.

Sơ đồ: mẫu và quy tắc cú pháp ở `<core>/references/diagram-conventions.md` (nhãn trong ngoặc kép, ID trạng thái ASCII…). `ba.py lint` kiểm cú pháp cơ bản; có Node + Chrome thì render thử bằng `<core>/scripts/mermaid_check.mjs`.

## 8. Đặc tả báo cáo (template `report-spec.md`, loại "Báo cáo")

Mấu chốt là **logic lấy số liệu** đủ để viết truy vấn: chứng từ nào, trạng thái nào được tính (thường chỉ POSTED/COMPLETED), lọc theo ngày chứng từ hay ngày ghi sổ, số dư đầu kỳ, quy đổi tiền tệ, loại trừ gì. Báo cáo theo mẫu luật ghi mẫu số và căn cứ còn hiệu lực (`<core>/references/regulations/`). Luôn có ví dụ số liệu để QA đối chiếu. Danh mục báo cáo chuẩn: `<core>/references/reports-catalog.md`.

## 9. Phạm vi lớn & quản lý thay đổi

- Chia theo BP/module; mỗi lượt làm trọn một module (catalog liên quan + mọi FN) rồi chạy lint/trace trước khi sang module khác. Nhiều agent viết song song: phân công theo module, chỉ **một** agent được sửa catalog (agent khác gửi đề nghị bổ sung). Giữ ID ổn định, không đánh số lại.
- Thay đổi sau khi đã đặc tả: ghi CHG trong issue-log → tìm mọi chỗ bị ảnh hưởng (`grep -rn "<ID>" <root>`, `traceability.md`) → sửa, giữ ID, tăng `version`, ghi mục 20 kèm CHG → REQ cũ đổi trạng thái "Đã thay đổi" (không xóa) → chạy lại `erp-ba-step4-verify` cho phạm vi bị ảnh hưởng; tài liệu `Approved` quay về `In Review` cho tới khi được duyệt lại.

## 10. Nghiệm thu & chuyển bước

```bash
python3 <core>/scripts/ba.py lint <root>
python3 <core>/scripts/ba.py trace <root>
python3 <core>/scripts/ba.py checklist <root> --step 3 --round <N> --out <root>/04-verification/verify-report-r<N>.md
python3 <core>/scripts/ba.py status <root>/04-verification/verify-report-r<N>.md
```

`--step 3` sinh C3 (toàn bộ) + C3F cho từng chức năng (lọc theo `type`) + C3R cho từng báo cáo. Trả lời từng câu Yes (kèm bằng chứng) / No (kèm việc sửa) / N/A (kèm lý do) — cho **từng** chức năng, không gộp. Sửa mọi No, chạy lại tới khi PASS.

Bước tiếp theo: `erp-ba-step4-verify` (tự kiểm chéo toàn bộ tài liệu, trả lời 4 câu hỏi bắt buộc), rồi `erp-ba-step5-review` (review độc lập). Phát hiện của bước 4–5 quay lại skill này để sửa.
