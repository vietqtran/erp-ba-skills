# Thư viện mẫu chức năng ERP chuẩn (ERP Function Design Patterns)

> Cập nhật đến: 2026-10-20 — quy định thay đổi thường xuyên; BA phải kiểm tra lại hiệu lực khi dùng cho dự án.
> File tra cứu trong skill `erp-ba-core`. Mục tiêu: để **mọi chức năng** trong spec đi theo một mẫu chuẩn đã biết, nhờ đó không thiếu hành vi, không mâu thuẫn, không mơ hồ và **code-ready**. Quy ước ID/trạng thái/quyền: xem `references/conventions.md`. Pháp lý kế toán & số hiệu tài khoản: xem `references/regulations/vn-accounting.md`. Quy trình đầu–cuối: xem `references/processes/*`.

## Mục lục
- [Cách dùng file này](#cách-dùng-file-này)
- [Bảng tra nhanh: pattern nào cho chức năng nào](#bảng-tra-nhanh-pattern-nào-cho-chức-năng-nào)
- [P01 — Danh mục / Dữ liệu chủ (Master Data CRUD)](#p01--danh-mục--dữ-liệu-chủ-master-data-crud)
- [P02 — Chứng từ giao dịch header–lines (Transaction Document)](#p02--chứng-từ-giao-dịch-headerlines-transaction-document)
- [P03 — Quy trình duyệt nhiều cấp (Multi-level Approval)](#p03--quy-trình-duyệt-nhiều-cấp-multi-level-approval)
- [P04 — Luồng chứng từ / tạo từ chứng từ nguồn (Document Flow / Copy-from)](#p04--luồng-chứng-từ--tạo-từ-chứng-từ-nguồn-document-flow--copy-from)
- [P05 — Ghi sổ & đảo bút toán (Posting & Reversal)](#p05--ghi-sổ--đảo-bút-toán-posting--reversal)
- [P06 — Đánh số chứng từ (Document Numbering)](#p06--đánh-số-chứng-từ-document-numbering)
- [P07 — Khóa sổ / đóng kỳ (Period Close & Lock)](#p07--khóa-sổ--đóng-kỳ-period-close--lock)
- [P08 — Đa công ty · chi nhánh · tiền tệ · ngôn ngữ (Multi-org / Multi-currency / Multi-language)](#p08--đa-công-ty--chi-nhánh--tiền-tệ--ngôn-ngữ-multi-org--multi-currency--multi-language)
- [P09 — Đính kèm, bình luận, lịch sử hoạt động (Attachments / Comments / Activity Log)](#p09--đính-kèm-bình-luận-lịch-sử-hoạt-động-attachments--comments--activity-log)
- [P10 — Thông báo & nhắc việc (Notifications & Reminders)](#p10--thông-báo--nhắc-việc-notifications--reminders)
- [P11 — Mẫu in (Print Layouts)](#p11--mẫu-in-print-layouts)
- [P12 — Nhập/Xuất Excel (Excel Import/Export)](#p12--nhậpxuất-excel-excel-importexport)
- [P13 — Màn hình danh sách & tìm kiếm (List & Search Screen)](#p13--màn-hình-danh-sách--tìm-kiếm-list--search-screen)
- [P14 — Nhật ký kiểm toán field-level (Audit Trail)](#p14--nhật-ký-kiểm-toán-field-level-audit-trail)
- [P15 — Tác vụ nền / định kỳ (Background & Scheduled Jobs)](#p15--tác-vụ-nền--định-kỳ-background--scheduled-jobs)
- [P16 — Tích hợp (Integration: API / File / Event)](#p16--tích-hợp-integration-api--file--event)
- [P17 — Phạm vi dữ liệu theo tổ chức / người sở hữu (Data Scope / Access Control)](#p17--phạm-vi-dữ-liệu-theo-tổ-chức--người-sở-hữu-data-scope--access-control)
- [P18 — Dashboard & KPI](#p18--dashboard--kpi)
- [Nguồn tham khảo](#nguồn-tham-khảo)

---

## Cách dùng file này

1. **Mỗi chức năng (FN) khi đặc tả phải được "gắn nhãn" bằng một hoặc nhiều pattern.** Ví dụ `FN-PUR-01 Quản lý nhà cung cấp` = P01 + P12 + P13 + P14; `FN-PUR-03 Đơn mua hàng` = P02 + P03 + P04 + P06 + P09 + P11 + P13.
2. **Với mỗi pattern đã gắn, spec PHẢI trả lời được toàn bộ câu hỏi trong "Checklist đặc tả".** Nếu chưa trả lời được → ghi `[CẦN XÁC NHẬN: Q-NNN]`, không được đoán (xem `references/conventions.md` §4).
3. Pattern mô tả **hành vi chuẩn + điểm phải quyết định**, không phải yêu cầu cứng. Dự án có thể khác, nhưng mọi khác biệt phải ghi rõ lý do (DEC) thay vì bỏ qua một mục.
4. **Không chép lại** số hiệu tài khoản, số văn bản luật, quy trình đầu–cuối vào file chức năng — tham chiếu tới file nguồn (`vn-accounting.md`, `processes/*`).
5. Cột **Nguồn** của mọi FR/BR trỏ về: REQ/DEC của dự án, hoặc pattern này (`references/design-patterns.md §P0x`), hoặc file process/regulation cụ thể.
6. Thứ tự đọc khi viết 1 FN: xác định loại (danh mục? chứng từ? báo cáo? job?) → lấy pattern chính → bổ sung pattern phụ (đính kèm, thông báo, audit, Excel, list screen) → chạy checklist.

### Bảng tra nhanh: pattern nào cho chức năng nào

| Loại chức năng | Pattern bắt buộc | Pattern thường kèm |
|---|---|---|
| Quản lý danh mục (nhà cung cấp, vật tư, khách hàng, TK…) | P01 | P12, P13, P14, P17 |
| Chứng từ nghiệp vụ (PO, phiếu nhập, hóa đơn, phiếu kế toán…) | P02, P06 | P03, P04, P05, P09, P10, P11, P13, P14, P17 |
| Chức năng duyệt | P03 | P10, P14 |
| Chứng từ sinh từ chứng từ khác | P04 | P02, P06 |
| Bút toán / ảnh hưởng sổ | P05 | P07 |
| Job chạy nền (MRP, khấu hao, tính giá, kết chuyển) | P15 | P05, P07, P14 |
| Màn hình tra cứu / danh sách | P13 | P12, P17 |
| Tích hợp hệ thống ngoài | P16 | P14 |
| Báo cáo / dashboard | P18 | P13, P17 |

---

## P01 — Danh mục / Dữ liệu chủ (Master Data CRUD)

**Khi nào dùng:** mọi đối tượng được khai báo một lần rồi dùng lại ở nhiều chứng từ — nhà cung cấp (Vendor/Supplier – `MD-VENDOR`), khách hàng (Customer), vật tư/hàng hóa (Material/Item), tài khoản kế toán (GL Account), kho (Warehouse), đơn vị tính (UoM), trung tâm chi phí (Cost Center), nhân viên, dự án… SAP gọi là *Master Data*, Odoo là *master/configuration records*.

**Hành vi chuẩn (bắt buộc đặc tả):**
1. CRUD: Tạo / Xem / Sửa / Vô hiệu hóa; **không xóa cứng** bản ghi đã phát sinh tham chiếu.
2. **Mã (code)**: quy tắc sinh (thủ công / tự động theo P06), độ dài, ký tự cho phép, **duy nhất** trong phạm vi (toàn hệ thống hay theo công ty — xem P08).
3. Phân nhóm/phân cấp: nhóm vật tư, nhóm nhà cung cấp, cây tài khoản (cha–con), trạng thái nút lá/nút tổng hợp.
4. **Trường bắt buộc vs tùy chọn** khai báo rõ từng trường; trường mặc định (default) khi tạo.
5. **Active/Inactive** (Hiệu lực/Ngừng hoạt động) thay cho xóa; bản ghi Inactive không hiện trong danh sách chọn của chứng từ mới nhưng vẫn hiển thị ở chứng từ cũ và báo cáo.
6. Nhập Excel hàng loạt (theo P12), xuất Excel (P13).
7. **Audit thay đổi** từng trường (theo P14) — bắt buộc với dữ liệu chủ tài chính (nhà cung cấp, khách hàng, số tài khoản ngân hàng, tài khoản kế toán).
8. **Duyệt thay đổi dữ liệu chủ (master-data change approval)** — tùy chọn, bật cho trường nhạy cảm (STK ngân hàng người thụ hưởng, hạn mức công nợ, giá bán): thay đổi vào trạng thái PENDING tới khi được Duyệt.
9. Hợp nhất/khử trùng (merge/de-dup): phát hiện trùng theo MST/CCCD/tên + xử lý gộp (nâng cao — chỉ đặc tả nếu khách hàng yêu cầu, gắn `[ĐỀ XUẤT → Q-NNN]`).

**Trạng thái & chuyển trạng thái:** (chỉ khi bật duyệt thay đổi; không bật thì chỉ có Active/Inactive)

```mermaid
stateDiagram-v2
    state "Nháp" as DRAFT
    state "Chờ duyệt" as PENDING
    state "Hiệu lực" as APPROVED
    state "Ngừng hoạt động" as INACTIVE
    [*] --> DRAFT
    DRAFT --> PENDING: Gửi duyệt
    PENDING --> APPROVED: Duyệt
    PENDING --> DRAFT: Trả lại
    APPROVED --> PENDING: Sửa trường nhạy cảm
    APPROVED --> INACTIVE: Ngừng hoạt động
    INACTIVE --> APPROVED: Kích hoạt lại
    DRAFT --> [*]: Xóa khi chưa dùng
```

**Quy tắc chuẩn:**
- `BR-P01-01` — Mã danh mục **PHẢI duy nhất** trong phạm vi quy định; **KHÔNG ĐƯỢC** cho sửa mã sau khi bản ghi đã phát sinh tham chiếu ở bất kỳ chứng từ nào. *Lý do: mã là khóa liên kết.*
- `BR-P01-02` — **KHÔNG ĐƯỢC xóa** bản ghi đang được tham chiếu; chỉ cho **Ngừng hoạt động**. Hệ thống PHẢI kiểm tra tham chiếu trước khi cho xóa.
- `BR-P01-03` — Xóa cứng **chỉ** áp dụng cho bản ghi chưa từng dùng ở đâu (giống chứng từ Nháp).
- `BR-P01-04` — Mọi trường bắt buộc PHẢI được validate trước khi lưu; thông báo lỗi chỉ rõ trường thiếu (dùng mã `MSG-…`).
- `BR-P01-05` — Thay đổi trường tài chính nhạy cảm PHẢI được ghi log field-level (ai, khi nào, giá trị cũ→mới) và (nếu bật) qua duyệt.
- `BR-P01-06` — Khi Ngừng hoạt động, hệ thống NÊN cảnh báo nếu còn chứng từ mở tham chiếu (PO chưa nhận, công nợ chưa tất toán).

**Phân quyền điển hình:**

| Hành động | Vai trò điển hình | Phạm vi |
|---|---|---|
| Xem | Mọi vai trò nghiệp vụ liên quan | Theo P17 |
| Tạo, Sửa | Nhân viên nghiệp vụ sở hữu danh mục (vd Nhân viên mua hàng – Purchasing Staff với nhà cung cấp) | Công ty |
| Duyệt (thay đổi nhạy cảm) | Trưởng phòng / Kế toán trưởng (Chief Accountant) với STK, hạn mức | Công ty |
| Xóa (chưa dùng) | Người tạo hoặc Quản trị hệ thống (System Administrator) | Của mình / Công ty |
| Nhập file, Xuất file | Người được giao, có kiểm soát | Công ty |
| Cấu hình (quy tắc mã, trường bắt buộc) | Quản trị hệ thống | Toàn hệ thống |

**Tham số điển hình:**

| Mã | Tên | Kiểu | Mặc định | Tác dụng |
|---|---|---|---|---|
| `PRM-SYS-001` | Quy tắc sinh mã danh mục | Chuỗi/mẫu | Thủ công | Tự động theo P06 hay người dùng nhập |
| `PRM-SYS-002` | Bật duyệt thay đổi dữ liệu chủ | Luận lý | Tắt | Bật PENDING khi sửa trường nhạy cảm |
| `PRM-SYS-003` | Danh sách trường nhạy cảm cần duyệt/log | Bảng | STK ngân hàng, hạn mức | Phạm vi audit & duyệt |
| `PRM-SYS-004` | Cho sửa mã sau khi phát sinh | Luận lý | Không | Khóa mã |

**Màn hình chuẩn:**
- **List:** cột Mã, Tên, Nhóm, Trạng thái (Hiệu lực/Ngừng), Người tạo, Ngày cập nhật. Bộ lọc: Trạng thái, Nhóm, từ khóa (mã/tên/MST). Nút: Thêm, Nhập Excel, Xuất Excel, Bật/Tắt hoạt động (bulk). (chi tiết P13)
- **Detail/Form:** tab Thông tin chung · Thông tin kế toán/thuế · Liên hệ/địa chỉ · Đính kèm (P09) · Lịch sử thay đổi (P14). Nút theo trạng thái: Nháp → Lưu, Gửi duyệt, Xóa; Hiệu lực → Sửa, Ngừng hoạt động, In; Ngừng → Kích hoạt lại.

**Lỗi đặc tả thường gặp:**
- Chỉ ghi "CRUD nhà cung cấp" mà không liệt kê **từng trường** và trường nào bắt buộc.
- Không nói rõ xử lý khi mã trùng / khi xóa bản ghi đang dùng.
- Dùng xóa thay cho Ngừng hoạt động → vỡ liên kết chứng từ cũ, sai số liệu lịch sử.
- Bỏ quên audit field-level cho STK ngân hàng (rủi ro gian lận chuyển tiền).
- Không phân biệt "ẩn khỏi danh sách chọn mới" vs "vẫn hiển thị ở chứng từ cũ".

**Checklist đặc tả (Yes/No — spec phải trả lời được):**
- [ ] Đã liệt kê đầy đủ trường, đánh dấu bắt buộc/tùy chọn/mặc định?
- [ ] Mã sinh thủ công hay tự động? Phạm vi duy nhất là gì?
- [ ] Có cho sửa mã sau khi phát sinh không?
- [ ] Xử lý khi xóa bản ghi đang được tham chiếu đã rõ chưa?
- [ ] Ngừng hoạt động có chặn chọn ở chứng từ mới, giữ ở chứng từ cũ không?
- [ ] Có bật duyệt thay đổi cho trường nhạy cảm không? Trường nào?
- [ ] Những trường nào ghi audit field-level?
- [ ] Có nhập/xuất Excel không (→ P12)?

---

## P02 — Chứng từ giao dịch header–lines (Transaction Document)

**Khi nào dùng:** mọi chứng từ có **1 đầu (header)** và **nhiều dòng (lines/items)**: đơn mua hàng (Purchase Order – PO), phiếu nhập kho (Goods Receipt Note – GRN), hóa đơn bán (Sales Invoice), phiếu kế toán (Journal Entry), đơn bán hàng (Sales Order – SO)…

**Hành vi chuẩn (bắt buộc đặc tả):**
1. **Header:** số chứng từ (P06), **ngày chứng từ (document date)** vs **ngày hạch toán/ghi sổ (posting date)** — có thể khác nhau; đối tác, kho/bộ phận, diễn giải, điều khoản thanh toán, loại chứng từ.
2. **Lines:** vật tư/dịch vụ/tài khoản, số lượng, đơn vị tính, đơn giá, % chiết khấu, thuế suất, thành tiền, tài khoản/đối tượng hạch toán, ghi chú dòng.
3. **Tiền tệ & tỷ giá (currency & exchange rate):** tiền giao dịch (transaction/document currency), tỷ giá quy đổi về **tiền hạch toán (local/functional currency = VND)**; nguồn tỷ giá, ngày lấy tỷ giá, cho sửa tay hay không. Tỷ giá cho thuế xem `references/regulations/vn-tax-einvoice.md`.
4. **Tính toán & làm tròn (rounding):** thành tiền dòng = SL × đơn giá × (1 − CK); thuế theo dòng hay theo nhóm thuế; tổng trước thuế, tổng thuế, tổng sau thuế; **quy tắc làm tròn phải nêu rõ** (làm tròn từng dòng rồi cộng, hay cộng rồi làm tròn — xem `references/conventions.md` §8).
5. Chiết khấu: theo dòng (%/số tiền) và/hoặc chiết khấu tổng (header) phân bổ xuống dòng.
6. **Đính kèm (P09), bình luận, lịch sử (P09, P14).**
7. Copy/nhân bản chứng từ; tạo từ chứng từ nguồn (P04).
8. In (P11); gửi duyệt (P03); ghi sổ (P05).

**Trạng thái & chuyển trạng thái:** (tập con tùy loại; dùng đúng mã trạng thái chuẩn)

```mermaid
stateDiagram-v2
    state "Nháp" as DRAFT
    state "Chờ duyệt" as PENDING
    state "Trả lại để sửa" as RETURNED
    state "Từ chối" as REJECTED
    state "Đã duyệt" as APPROVED
    state "Đã ghi sổ" as POSTED
    state "Đã hủy" as CANCELLED
    state "Đã đảo" as REVERSED
    [*] --> DRAFT
    DRAFT --> PENDING: Gửi duyệt
    DRAFT --> CANCELLED: Hủy
    PENDING --> APPROVED: Duyệt
    PENDING --> RETURNED: Trả lại
    PENDING --> REJECTED: Từ chối
    RETURNED --> PENDING: Gửi lại
    APPROVED --> POSTED: Ghi sổ
    APPROVED --> CANCELLED: Hủy
    POSTED --> REVERSED: Đảo
    REJECTED --> [*]
```

**Quy tắc chuẩn:**
- `BR-P02-01` — Chứng từ **PHẢI có ≥ 1 dòng** hợp lệ mới cho Gửi duyệt/Ghi sổ.
- `BR-P02-02` — Chỉ **Nháp** mới được Sửa tự do và Xóa; từ PENDING trở đi phải Thu hồi/Trả lại mới sửa được.
- `BR-P02-03` — Ngày hạch toán PHẢI nằm trong **kỳ đang mở** (xem P07); mặc định = ngày chứng từ nếu không nhập.
- `BR-P02-04` — Chứng từ ngoại tệ PHẢI lưu đồng thời: giá trị nguyên tệ, tỷ giá, giá trị quy đổi VND; tỷ giá theo `PRM`.
- `BR-P02-05` — Quy tắc làm tròn PHẢI nhất quán toàn hệ thống và nêu rõ trong BR-GEN; tổng chứng từ = tổng các dòng đã làm tròn (hoặc ngược lại — chọn một).
- `BR-P02-06` — Thuế GTGT đầu ra/đầu vào tính theo từng dòng theo thuế suất của dòng; tổng thuế = Σ thuế dòng.
- `BR-P02-07` — Đã ghi sổ thì **không sửa/không xóa**; sửa bằng Bỏ ghi sổ (kỳ mở) hoặc Đảo (kỳ khóa) — xem P05.

**Phân quyền điển hình:** Xem / Tạo / Sửa / Xóa (chỉ Nháp) / Gửi duyệt — Nhân viên nghiệp vụ; Duyệt / Từ chối / Trả lại — Trưởng phòng (theo P03); Ghi sổ / Bỏ ghi sổ / Đảo — Kế toán phụ trách; Hủy — người tạo (khi chưa ghi sổ) hoặc Trưởng phòng; In / Xuất file — theo vai trò. Mỗi quyền kèm **phạm vi dữ liệu** (P17).

**Tham số điển hình:**

| Mã | Tên | Kiểu | Mặc định | Tác dụng |
|---|---|---|---|---|
| `PRM-SYS-010` | Nguồn tỷ giá & cho sửa tay | Chọn | Bảng tỷ giá nội bộ, cho sửa | Quy đổi ngoại tệ |
| `PRM-SYS-011` | Phương pháp làm tròn | Chọn | Làm tròn dòng rồi cộng | Tính tổng |
| `PRM-SYS-012` | Số chữ số thập phân SL / đơn giá | Số | 3 / 4 | Nhập liệu |
| `PRM-SYS-013` | Bắt buộc ngày hạch toán trong kỳ mở | Luận lý | Có | Chặn ghi sai kỳ |
| `PRM-SYS-014` | Cho phép ngày chứng từ ≠ ngày ghi sổ | Luận lý | Có | Lệch kỳ hợp lệ |

**Màn hình chuẩn:**
- **List:** Số CT, Ngày CT, Đối tác, Tổng tiền, Tiền tệ, Trạng thái, Người tạo. Lọc: khoảng ngày, trạng thái, đối tác, loại CT, số tiền. (P13)
- **Form:** vùng Header (trên) + lưới Lines (grid, thêm/xóa/sắp dòng, nhập nhanh) + vùng Tổng (totals) + tab Đính kèm/Lịch sử. Nút theo trạng thái: Nháp → Lưu, Gửi duyệt, Xóa, In nháp; Đã duyệt → Ghi sổ, Hủy, In; Đã ghi sổ → Đảo, In, Xem bút toán.

**Lỗi đặc tả thường gặp:**
- Gộp ngày chứng từ và ngày ghi sổ làm một → sai kỳ kế toán.
- Không nêu quy tắc làm tròn → lệch tổng vài đồng giữa UI, in, và sổ.
- Quên lưu nguyên tệ + tỷ giá + quy đổi (chỉ lưu VND) → không tái lập được, không đánh giá lại tỷ giá được.
- Không định nghĩa thuế theo dòng khi các dòng khác thuế suất.
- Cho sửa chứng từ đã ghi sổ.

**Checklist đặc tả:**
- [ ] Đã tách ngày chứng từ và ngày hạch toán chưa?
- [ ] Công thức thành tiền, thuế, chiết khấu, làm tròn, tổng đã viết tường minh chưa?
- [ ] Đa tiền tệ: lưu gì (nguyên tệ/tỷ giá/VND)? Tỷ giá lấy ở đâu, cho sửa không?
- [ ] Trường bắt buộc ở header và line là gì?
- [ ] Mỗi trạng thái cho làm gì, nút nào hiện?
- [ ] Số chứng từ sinh thế nào (→ P06)? Duyệt thế nào (→ P03)? Ghi sổ ra bút toán gì (→ P05)?

---

## P03 — Quy trình duyệt nhiều cấp (Multi-level Approval)

**Khi nào dùng:** chứng từ cần phê duyệt trước khi thực hiện — PO, đề nghị thanh toán, phiếu chi, hợp đồng, nghỉ phép, điều chỉnh giá… SAP: *Release Strategy* [3]; Oracle: *Approvals Management (AME)*; Odoo: *double validation*; Dynamics: *Workflow*.

**Hành vi chuẩn (bắt buộc đặc tả):**
1. **Điều kiện kích hoạt & định tuyến:** theo **số tiền (hạn mức)**, phòng ban, loại chứng từ, nhóm hàng, trung tâm chi phí. (SAP dùng đặc trưng như loại chứng từ, tổ chức mua, tổng giá trị để xác định chiến lược duyệt [3].)
2. **Số cấp duyệt & kiểu:** tuần tự (sequential) hay song song (parallel); mỗi cấp = một người/nhóm người duyệt (SAP: *release code* = một người duyệt [3]).
3. **Ủy quyền (delegation):** người duyệt vắng mặt ủy quyền cho người khác trong khoảng thời gian; log rõ "duyệt thay".
4. **Leo thang (escalation):** quá hạn X giờ/ngày → nhắc, rồi chuyển lên cấp trên hoặc người thay.
5. **Thu hồi (recall):** người tạo rút chứng từ về Nháp khi chưa ai duyệt (hoặc theo quy tắc).
6. **Từ chối (reject) vs Trả lại (return):** Từ chối = kết thúc (REJECTED); Trả lại = về người tạo sửa rồi gửi lại (RETURNED → PENDING).
7. **Gửi lại sau khi bị trả lại:** bắt đầu lại từ cấp 1 hay tiếp tục cấp đang dở — phải quyết định.
8. **Lịch sử duyệt (approval history):** ai, cấp nào, thời điểm, hành động, ý kiến — bất biến.
9. Thông báo mỗi bước (P10).

**Trạng thái & chuyển trạng thái:**

```mermaid
flowchart TD
    A["Gửi duyệt (Submit)"] --> B{"Tổng tiền vượt hạn mức cấp 1?"}
    B -->|"Không"| C["Chờ duyệt cấp 1 (Trưởng phòng)"]
    B -->|"Có"| D["Chờ duyệt cấp 1 rồi cấp 2 (Giám đốc)"]
    C --> E{"Kết quả duyệt"}
    D --> E
    E -->|"Duyệt hết cấp"| F["Đã duyệt (APPROVED)"]
    E -->|"Trả lại"| G["Trả lại để sửa (RETURNED)"]
    E -->|"Từ chối"| H["Từ chối (REJECTED)"]
    G --> A
    C --> I{"Quá hạn SLA?"}
    I -->|"Có"| J["Nhắc và leo thang"]
```

**Quy tắc chuẩn:**
- `BR-P03-01` — Định tuyến duyệt PHẢI dựa trên dữ liệu chứng từ tại thời điểm gửi (số tiền, phòng ban…); đổi số tiền sau khi gửi PHẢI tính lại luồng (hoặc buộc thu hồi–gửi lại).
- `BR-P03-02` — Người **tạo KHÔNG ĐƯỢC tự duyệt** chứng từ của mình (SoD — tách biệt trách nhiệm), trừ cấu hình đặc biệt có kiểm soát.
- `BR-P03-03` — Mỗi hành động duyệt PHẢI ghi lịch sử bất biến (append-only): người, cấp, thời điểm, ý kiến.
- `BR-P03-04` — Ủy quyền PHẢI có thời hạn và được log; hành động hiển thị "A duyệt thay B".
- `BR-P03-05` — Khi bị Trả lại rồi gửi lại, quy tắc quay vòng (bắt đầu lại từ cấp 1 hay tiếp tục) PHẢI cấu hình được.
- `BR-P03-06` — Hạn mức duyệt là dữ liệu cấu hình (ma trận hạn mức theo vai trò/phòng/loại CT), không hard-code — định nghĩa ở `03-specification/catalogs/roles-permissions.md`.

**Phân quyền điển hình:** Gửi duyệt — người tạo; Duyệt / Từ chối / Trả lại — người duyệt theo cấp (Trưởng phòng mua hàng – Purchasing Manager, Kế toán trưởng – Chief Accountant, Giám đốc – Director); Thu hồi — người tạo; Cấu hình luồng & hạn mức — Quản trị hệ thống.

**Tham số điển hình:**

| Mã | Tên | Kiểu | Mặc định | Tác dụng |
|---|---|---|---|---|
| `PRM-SYS-020` | Ma trận hạn mức duyệt | Bảng | Theo dự án | Định tuyến theo số tiền |
| `PRM-SYS-021` | Kiểu duyệt | Chọn | Tuần tự | Tuần tự / song song |
| `PRM-SYS-022` | SLA mỗi cấp (giờ) | Số | 24 | Mốc nhắc & leo thang |
| `PRM-SYS-023` | Quy tắc gửi lại sau trả lại | Chọn | Lại từ cấp 1 | Quay vòng |
| `PRM-SYS-024` | Cho ủy quyền | Luận lý | Có | Delegation |
| `PRM-SYS-025` | Chặn tự duyệt (SoD) | Luận lý | Có | Kiểm soát |

**Màn hình chuẩn:**
- **Hộp công việc (Approval Inbox):** danh sách chứng từ chờ tôi duyệt; cột Số CT, Loại, Đối tác, Số tiền, Người gửi, Chờ từ, Hạn. Nút: Duyệt, Từ chối, Trả lại (bulk cho phép với ghi chú bắt buộc khi Từ chối/Trả lại).
- **Trong chứng từ:** panel "Luồng duyệt" hiển thị các cấp, người, trạng thái từng cấp; tab "Lịch sử duyệt".

**Lỗi đặc tả thường gặp:**
- Không phân biệt Từ chối (kết thúc) và Trả lại (sửa lại) → lập trình sai vòng đời.
- Hard-code hạn mức/cây duyệt trong code thay vì cấu hình.
- Bỏ quên ủy quyền, leo thang, thu hồi → quy trình kẹt khi người duyệt vắng.
- Không xử lý thay đổi số tiền sau khi đã gửi duyệt.
- Không có lịch sử duyệt bất biến (không truy được ai duyệt).

**Checklist đặc tả:**
- [ ] Điều kiện kích hoạt duyệt và tiêu chí định tuyến là gì (số tiền? phòng? loại)?
- [ ] Bao nhiêu cấp, tuần tự hay song song, ai ở mỗi cấp?
- [ ] Có ủy quyền / leo thang / thu hồi không? Quy tắc mỗi cái?
- [ ] Trả lại vs Từ chối xử lý khác nhau thế nào?
- [ ] Gửi lại sau trả lại thì bắt đầu từ đâu?
- [ ] Người tạo có được tự duyệt không (SoD)?
- [ ] Lịch sử duyệt lưu gì, có bất biến không?

---

## P04 — Luồng chứng từ / tạo từ chứng từ nguồn (Document Flow / Copy-from)

**Khi nào dùng:** chứng từ sinh ra từ chứng từ trước và cần theo dõi phần đã/chưa thực hiện — PR→PO→GRN→Hóa đơn (P2P), Báo giá→SO→Phiếu giao→Hóa đơn (O2C). SAP: *Copy Control* (VTAA/VTLA/VTFL) + *Document Flow* [5]; Odoo: *bill control* theo SL đặt/SL nhận [8]. Khớp 3 bên PO–nhập kho–hóa đơn với dung sai và chặn thanh toán khi lệch: SAP *Logistics Invoice Verification* (3-way match) [4].

**Hành vi chuẩn (bắt buộc đặc tả):**
1. **Copy-from / tạo tham chiếu:** chọn chứng từ nguồn → kéo dữ liệu header + dòng sang chứng từ đích; trường nào copy, trường nào nhập mới (SAP copy control định nghĩa ở mức header/dòng/lịch giao hàng, có routine quyết định trường được copy [5]).
2. **Thực hiện một phần (partial fulfilment):** mỗi dòng theo dõi **SL đặt / SL đã nhận / SL đã xuất hóa đơn / SL còn lại** (ordered / received / invoiced / remaining).
3. **Nhiều–nhiều:** một nguồn sinh nhiều đích (giao nhiều lần) và một đích gộp nhiều nguồn (1 hóa đơn cho nhiều phiếu nhập).
4. **Đóng sớm (short-close):** đóng phần còn lại không thực hiện nữa dù chưa đủ SL → nguồn = CLOSED, phần dư = 0.
5. **Liên kết ngược (back-links / document flow):** từ bất kỳ chứng từ nào xem được cả chuỗi trước–sau.
6. Kiểm soát vượt: cho nhận/xuất hóa đơn vượt SL đặt bao nhiêu % (over-delivery/over-billing tolerance).

**Trạng thái & chuyển trạng thái:** (ví dụ chuỗi mua hàng)

```mermaid
flowchart LR
    A["Đề nghị mua hàng (PR)"] --> B["Đơn mua hàng (PO) - APPROVED"]
    B --> C{"Giao hàng"}
    C -->|"Một phần"| D["Phiếu nhập kho (GRN) - PO = PARTIAL"]
    C -->|"Đủ"| E["Phiếu nhập kho (GRN) - PO = COMPLETED"]
    D --> F["Hóa đơn mua (Vendor Bill)"]
    E --> F
    D --> G{"Xử lý phần dư"}
    G -->|"Short-close"| H["PO = CLOSED"]
    G -->|"Chờ giao tiếp"| C
```

**Quy tắc chuẩn:**
- `BR-P04-01` — SL/giá trị trên chứng từ đích **KHÔNG ĐƯỢC vượt** phần còn lại của nguồn, trừ khi trong ngưỡng dung sai cấu hình (`PRM`).
- `BR-P04-02` — Mỗi dòng nguồn PHẢI cập nhật SL đã nhận/đã hóa đơn/còn lại ngay khi chứng từ đích được ghi nhận; trạng thái nguồn tự chuyển PARTIAL/COMPLETED theo công thức rõ ràng.
- `BR-P04-03` — Short-close PHẢI có quyền riêng, ghi lý do, và **không xóa** phần đã thực hiện; phần dư về 0.
- `BR-P04-04` — Phải lưu **liên kết hai chiều** nguồn↔đích để tra document flow và truy vết.
- `BR-P04-05` — Hủy/đảo chứng từ đích PHẢI hoàn lại SL còn lại cho nguồn (mở lại trạng thái tương ứng).
- `BR-P04-06` — Trường copy từ nguồn mà người dùng được phép sửa trên đích PHẢI liệt kê rõ; sửa giá/SL có thể đưa đích vào trạng thái "Ngoại lệ" cần kiểm soát (Odoo: *Exception* khi tăng SL/đổi giá so với nhận thực tế [8]).

**Phân quyền điển hình:** Tạo từ nguồn — nhân viên nghiệp vụ; Short-close / đóng dư — Trưởng phòng; Cấu hình dung sai & quy tắc copy — Quản trị hệ thống.

**Tham số điển hình:**

| Mã | Tên | Kiểu | Mặc định | Tác dụng |
|---|---|---|---|---|
| `PRM-SYS-030` | Dung sai nhận/giao vượt (%) | Số | 0 | Cho vượt SL đặt |
| `PRM-SYS-031` | Dung sai xuất hóa đơn vượt (%) | Số | 0 | Over-billing |
| `PRM-SYS-032` | Cho gộp nhiều nguồn vào 1 đích | Luận lý | Có | Hóa đơn gộp |
| `PRM-SYS-033` | Bắt buộc tạo đích từ nguồn | Luận lý | Tùy loại | Chặn tạo tự do |

**Màn hình chuẩn:**
- **Form chứng từ đích:** nút "Tạo từ…" / "Chọn chứng từ nguồn"; lưới dòng hiện cột SL đặt / SL còn lại / SL lần này; panel "Luồng chứng từ" (sơ đồ nguồn–đích).
- **List nguồn:** cột % hoàn thành, SL còn lại; lọc "còn hàng chưa nhận", "chưa xuất hóa đơn".

**Lỗi đặc tả thường gặp:**
- Chỉ mô tả "tạo PO từ PR" mà bỏ theo dõi SL còn lại → không làm được giao nhiều lần.
- Không có cơ chế short-close → PO treo mãi.
- Không hoàn SL khi hủy/đảo chứng từ đích.
- Không lưu back-link → không truy vết được.
- Không định nghĩa dung sai vượt.

**Checklist đặc tả:**
- [ ] Chứng từ đích tạo từ nguồn nào? Trường nào copy, trường nào sửa được?
- [ ] Theo dõi SL đặt/nhận/hóa đơn/còn lại ở mức dòng chưa?
- [ ] Hỗ trợ giao nhiều lần và gộp nhiều nguồn không?
- [ ] Có short-close không? Ai được làm, ghi gì?
- [ ] Hủy/đảo đích có hoàn SL cho nguồn không?
- [ ] Dung sai vượt là bao nhiêu?
- [ ] Xem document flow ở đâu?

---

## P05 — Ghi sổ & đảo bút toán (Posting & Reversal)

**Khi nào dùng:** chứng từ phát sinh bút toán kế toán hoặc ảnh hưởng sổ con (kho, công nợ, TSCĐ). Số hiệu tài khoản dùng **Thông tư 99/2025/TT-BTC** (chế độ kế toán DN đang hiệu lực từ 01/01/2026, thay TT200/2014) [1] — xem đầy đủ `references/regulations/vn-accounting.md`. Cơ chế posting/đảo/khóa kỳ: xem `references/processes/r2r-general-ledger.md` (không chép lại ở đây).

**Hành vi chuẩn (bắt buộc đặc tả):**
1. **Định khoản tự động (account determination):** từ loại nghiệp vụ + dữ liệu chứng từ → sinh bút toán; bảng cấu hình ánh xạ (vật tư/nhóm KH/kho → tài khoản). SAP: *Subledger* + account determination; Oracle: *Subledger Accounting (SLA)* với account derivation rules & journal line types, gán *accounting method* cho ledger [13].
2. **Sổ con → Sổ cái (subledger → GL):** bút toán sinh ở phân hệ (AP/AR/INV/FA) rồi chuyển/kết nối GL; chạy nháp (draft) để kiểm tra trước khi ghi chính thức (Oracle *Create Accounting*: draft vs final, bản nháp không chuyển GL [13]).
3. **Ghi sổ (Post):** kiểm tra kỳ mở (P07), cân Nợ=Có, đủ trường; chuyển trạng thái POSTED; sinh số bút toán (P06).
4. **Bỏ ghi sổ (Unpost):** chỉ khi **kỳ còn mở** và chứng từ chưa dùng cho báo cáo đã phát hành → về Nháp để sửa.
5. **Đảo (Reverse):** khi kỳ gốc đã khóa hoặc cần giữ dấu vết → sinh bút toán ngược dấu (đổi Nợ↔Có hoặc ghi âm theo tham số), tham chiếu chứng từ gốc; **không xóa** gốc.
6. **Khóa kỳ (period lock):** chặn ghi/sửa/bỏ ghi vào kỳ đã đóng (P07).

**Trạng thái & chuyển trạng thái:**

```mermaid
stateDiagram-v2
    state "Đã duyệt" as APPROVED
    state "Đã ghi sổ" as POSTED
    state "Nháp" as DRAFT
    state "Đã đảo" as REVERSED
    APPROVED --> POSTED: Ghi sổ
    POSTED --> DRAFT: Bỏ ghi sổ (kỳ mở)
    DRAFT --> POSTED: Ghi sổ lại
    POSTED --> REVERSED: Đảo (kỳ khóa hoặc giữ dấu vết)
```

**Quy tắc chuẩn:**
- `BR-P05-01` — Bút toán PHẢI cân Nợ = Có (theo từng tiền tệ) mới cho ghi sổ.
- `BR-P05-02` — **Sau POSTED KHÔNG ĐƯỢC Xóa**; chỉ Bỏ ghi sổ (kỳ mở) hoặc Đảo (kỳ khóa). *Lý do: dấu vết kiểm toán, không ghi đè lịch sử* (xem `r2r-general-ledger.md` BR-GL-09).
- `BR-P05-03` — Ngày ghi sổ PHẢI thuộc kỳ mở; nếu kỳ khóa → chặn, gợi ý ghi kỳ kế tiếp.
- `BR-P05-04` — Bút toán đảo PHẢI tham chiếu số chứng từ gốc và ngược dấu đúng giá trị (gồm cả nguyên tệ & tỷ giá gốc).
- `BR-P05-05` — Định khoản PHẢI từ **bảng cấu hình**, không hard-code; thay đổi bảng để lại audit.
- `BR-P05-06` — Số dòng bút toán sinh ra, tài khoản, đối tượng (công nợ/khế ước/khoản mục) PHẢI nêu rõ cho **từng loại nghiệp vụ**.

**Bút toán ví dụ (số hiệu TT99/2025 — xem `vn-accounting.md`):**

| Nghiệp vụ | Nợ | Có | Ghi chú |
|---|---|---|---|
| Nhập kho hàng mua (kê khai thường xuyên) | 152/153/156 | 331 | Giá chưa thuế; theo TT99 TK 156 bỏ tiểu khoản 1561/1562 — chi phí thu mua tính vào giá gốc hàng (ghi thẳng 156) hoặc ghi 632 nếu giá trị nhỏ/liên quan nhiều mặt hàng |
| Thuế GTGT đầu vào được khấu trừ | 133 | 331 | Theo hóa đơn |
| Ghi nhận doanh thu bán chịu | 131 | 511, 3331 | 3331 = thuế GTGT đầu ra |
| Giá vốn hàng bán | 632 | 156 | Đồng thời với doanh thu |
| Thanh toán cho nhà cung cấp qua NH | 331 | 112 | Giảm công nợ |
| Đảo bút toán ghi sổ sai (kỳ đã khóa) | (ngược dấu bút toán gốc) | | Tham chiếu số CT gốc; không xóa gốc |

> Khi dự án áp dụng TT133/2016 (SME) hoặc TT58/2026 (siêu nhỏ) phải ánh xạ lại số hiệu tài khoản — xem `vn-accounting.md` §4.2.

**Phân quyền điển hình:** Ghi sổ / Bỏ ghi sổ / Đảo — Kế toán phụ trách phân hệ (Kế toán kho – Inventory Accountant, Kế toán công nợ phải trả – AP Accountant, Kế toán tổng hợp – General Ledger Accountant); duyệt bút toán vượt hạn mức & cấu hình định khoản — Kế toán trưởng (Chief Accountant).

**Tham số điển hình:**

| Mã | Tên | Kiểu | Mặc định | Tác dụng |
|---|---|---|---|---|
| `PRM-SYS-040` | Bảng định khoản tự động | Bảng | Theo dự án | Account determination |
| `PRM-SYS-041` | Phương pháp đảo | Chọn | Đổi Nợ↔Có | Hoặc ghi số âm |
| `PRM-SYS-042` | Cho Bỏ ghi sổ | Luận lý | Có (kỳ mở) | Unpost |
| `PRM-SYS-043` | Ghi sổ nháp trước (draft posting) | Luận lý | Có | Kiểm tra trước |

**Màn hình chuẩn:** nút "Ghi sổ" / "Bỏ ghi sổ" / "Đảo" trên form chứng từ; màn "Xem bút toán" (các dòng Nợ/Có + đối tượng); list "Chứng từ chờ ghi sổ"; list "Bút toán" lọc theo kỳ/tài khoản/nguồn.

**Lỗi đặc tả thường gặp:**
- Cho **Xóa** chứng từ đã ghi sổ thay vì Đảo/Bỏ ghi sổ → sai dấu vết kiểm toán.
- Không nêu bút toán cụ thể cho từng nghiệp vụ → dev tự đoán định khoản.
- Lẫn lộn Bỏ ghi sổ (kỳ mở) và Đảo (kỳ khóa).
- Đảo không tham chiếu gốc, không ngược dấu nguyên tệ.
- Dùng số hiệu tài khoản TT200 cũ.

**Checklist đặc tả:**
- [ ] Mỗi nghiệp vụ sinh bút toán nào (Nợ/Có/đối tượng)? Dùng số TK TT99 chưa?
- [ ] Định khoản lấy từ bảng cấu hình hay hard-code?
- [ ] Có ghi sổ nháp trước không?
- [ ] Bỏ ghi sổ áp dụng khi nào, Đảo khi nào?
- [ ] Đảo tham chiếu gốc & ngược dấu đúng chưa?
- [ ] Chặn ghi vào kỳ khóa chưa (→ P07)?

---

## P06 — Đánh số chứng từ (Document Numbering)

**Khi nào dùng:** mọi chứng từ/bản ghi cần số định danh theo quy tắc. SAP: *Number Ranges* (phụ thuộc company code & năm tài chính) [2]; Oracle: *Document Sequences* kiểu Automatic/Gapless/Manual [12]; Dynamics: *Number Sequences* (scope + cờ continuous) [11]; Odoo: *ir.sequence* (prefix/padding/reset).

**Hành vi chuẩn (bắt buộc đặc tả):**
1. **Cấu trúc số:** tiền tố + (mã công ty/chi nhánh) + (năm/tháng) + số tự tăng có đệm 0; ví dụ `PO-HN-2026-000123`.
2. **Phạm vi đánh số:** theo **loại chứng từ**, theo **chi nhánh/công ty** (P08), theo **năm/kỳ**; mỗi tổ hợp một bộ đếm riêng (SAP: number range theo company code & năm [2]; Dynamics: scope quyết định tổ chức dùng chung bộ số [11]).
3. **Reset bộ đếm:** đầu năm/tháng về 1 hay chạy liên tục.
4. **Chính sách khoảng trống (gap policy):** liên tục không nhảy cách (gapless) vs cho phép có lỗ (khi hủy chứng từ). Gapless đắt về hiệu năng và chỉ cấp số khi tạo thành công (Oracle khuyến cáo chỉ dùng gapless sau khi cân nhắc hiệu năng [12]).
5. **Thủ công vs tự động:** tự động (hệ cấp) hay người dùng nhập (chỉ kiểm tra duy nhất — Oracle Manual [12]).
6. Không đổi số sau khi cấp; số đã hủy không tái sử dụng (trừ chính sách rõ ràng).

**Trạng thái & chuyển trạng thái:** N/A – đây là quy tắc sinh khóa, không có vòng đời trạng thái.

**Quy tắc chuẩn:**
- `BR-P06-01` — Số chứng từ PHẢI **duy nhất** trong phạm vi (loại + công ty/chi nhánh + năm).
- `BR-P06-02` — Với chứng từ kế toán & hóa đơn, số PHẢI **liên tục, không trùng, không nhảy cách** theo loại/kỳ (yêu cầu pháp lý về sổ kế toán — Luật Kế toán; xem `vn-accounting.md`). Hóa đơn điện tử theo quy định riêng — xem `references/regulations/vn-tax-einvoice.md`.
- `BR-P06-03` — Bộ đếm năm-mới PHẢI thiết lập trước khi sang năm (SAP yêu cầu khai báo khoảng số cho năm tài chính mới [2]); hệ thống cảnh báo khi sắp hết dải số.
- `BR-P06-04` — Khoảng số các loại **KHÔNG ĐƯỢC chồng lấn** [2].
- `BR-P06-05` — Khi hủy chứng từ đã cấp số: giữ số (CANCELLED) hay cho dùng lại — PHẢI nêu rõ; mặc định giữ số.
- `BR-P06-06` — Nếu dùng gapless, PHẢI mô tả cơ chế cấp số chỉ khi lưu thành công và ảnh hưởng hiệu năng/khóa (locking).

**Phân quyền điển hình:** Cấu hình quy tắc & dải số — Quản trị hệ thống; người dùng nghiệp vụ không sửa được số đã cấp.

**Tham số điển hình:**

| Mã | Tên | Kiểu | Mặc định | Tác dụng |
|---|---|---|---|---|
| `PRM-SYS-050` | Mẫu số theo loại CT | Chuỗi mẫu | `{LOẠI}-{CN}-{YYYY}-{######}` | Cấu trúc số |
| `PRM-SYS-051` | Chu kỳ reset | Chọn | Theo năm | Reset đầu năm/tháng/không |
| `PRM-SYS-052` | Chính sách gap | Chọn | Liên tục | Gapless / cho lỗ |
| `PRM-SYS-053` | Thủ công hay tự động | Chọn | Tự động | Nguồn cấp số |
| `PRM-SYS-054` | Ngưỡng cảnh báo sắp hết dải | Số | 95% | Cảnh báo |

**Màn hình chuẩn:** màn "Cấu hình dải số" (loại CT, chi nhánh, năm, tiền tố, từ số–đến số, số hiện tại, trạng thái); log cấp số.

**Lỗi đặc tả thường gặp:**
- Nói "số tự tăng" mà không nói phạm vi (chung toàn hệ thống hay tách chi nhánh/năm).
- Không có chính sách khi sang năm → trùng số hoặc kẹt.
- Yêu cầu gapless nhưng không lường hiệu năng/khóa.
- Không quyết định giữ số hay dùng lại khi hủy.
- Nhầm số chứng từ nội bộ với số hóa đơn điện tử (hai hệ khác nhau).

**Checklist đặc tả:**
- [ ] Cấu trúc số gồm những thành phần nào?
- [ ] Đánh số theo loại/chi nhánh/năm thế nào? Mỗi tổ hợp một bộ đếm?
- [ ] Reset khi nào? Liên tục hay cho phép lỗ?
- [ ] Thủ công hay tự động? Ai được nhập tay?
- [ ] Sang năm xử lý ra sao? Cảnh báo hết dải?
- [ ] Hủy thì giữ số hay dùng lại?

---

## P07 — Khóa sổ / đóng kỳ (Period Close & Lock)

**Khi nào dùng:** kiểm soát kỳ kế toán (tháng/quý/năm) mở–đóng để chặn ghi sai kỳ. Cơ chế kết chuyển & khóa sổ cuối kỳ: xem `references/processes/r2r-general-ledger.md`; chế độ kế toán: `vn-accounting.md`. Odoo: *Lock dates* (Lock Sales/Purchases/Everything/Hard Lock) [9].

**Hành vi chuẩn (bắt buộc đặc tả):**
1. **Lịch kế toán:** năm tài chính, các kỳ; trạng thái kỳ: Mở / Khóa mềm / Đã đóng.
2. **Khóa theo phân hệ (period lock per module):** AP, AR, CB, INV, FA, GL có trạng thái kỳ riêng; nghiệp vụ đóng trước, GL đóng sau cùng.
3. **Khóa mềm vs khóa cứng:** khóa mềm chặn người dùng thường nhưng cho vai trò đặc biệt ghi; khóa cứng chặn tất cả (Odoo *Hard Lock* không thể đảo ngược [9]).
4. **Thao tác cuối kỳ trước khi khóa:** đối chiếu sổ con–sổ cái, đánh giá lại tỷ giá, trích khấu hao (P15), phân bổ, kết chuyển 511/515/711→911 và 632/635/641/642/811/821→911 → 4212.
5. **Mở lại kỳ (reopen):** có kiểm soát, ghi lý do, quyền riêng; chặn nếu BCTC đã phát hành.
6. Chuyển số dư sang kỳ/năm sau (carry-forward).

**Trạng thái & chuyển trạng thái:**

```mermaid
stateDiagram-v2
    state "Mở" as OPEN
    state "Khóa mềm" as SOFT
    state "Đã đóng" as CLOSED
    [*] --> OPEN
    OPEN --> SOFT: Khóa mềm (chặn nghiệp vụ)
    SOFT --> CLOSED: Khóa cứng sau đối chiếu
    SOFT --> OPEN: Mở lại
    CLOSED --> OPEN: Mở lại kỳ có kiểm soát
```

**Quy tắc chuẩn:**
- `BR-P07-01` — Mọi nghiệp vụ Tạo/Sửa/Ghi sổ/Bỏ ghi sổ có ngày hạch toán thuộc kỳ **đã đóng** PHẢI bị chặn, kèm thông báo rõ.
- `BR-P07-02` — Khóa PHẢI theo phân hệ; thứ tự đóng: các phân hệ nghiệp vụ trước, GL sau.
- `BR-P07-03` — Mở lại kỳ PHẢI có quyền riêng + ghi lý do + log; không mở lại kỳ đã phát hành BCTC/quyết toán thuế trừ trường hợp đặc biệt.
- `BR-P07-04` — Khóa cứng PHẢI chặn cả vai trò đặc biệt (chỉ mở lại được nếu chưa khóa cứng vĩnh viễn).
- `BR-P07-05` — Trước khi cho đóng, hệ thống NÊN kiểm tra còn chứng từ Nháp/chờ duyệt/lệch đối chiếu trong kỳ không và cảnh báo.

**Phân quyền điển hình:** Đóng / Mở lại kỳ — Kế toán trưởng (Chief Accountant); đóng kỳ phân hệ — kế toán phân hệ (trong phạm vi phân hệ); cấu hình lịch kế toán — Quản trị hệ thống.

**Tham số điển hình:**

| Mã | Tên | Kiểu | Mặc định | Tác dụng |
|---|---|---|---|---|
| `PRM-SYS-060` | Loại kỳ | Chọn | Tháng | Tháng/quý |
| `PRM-SYS-061` | Khóa theo phân hệ | Luận lý | Có | Period lock per module |
| `PRM-SYS-062` | Cho vai trò đặc biệt ghi khi khóa mềm | Luận lý | Có | Soft lock exception |
| `PRM-SYS-063` | Cho mở lại kỳ đã đóng | Luận lý | Có (log) | Reopen |

**Màn hình chuẩn:** màn "Quản lý kỳ kế toán" — lưới năm × phân hệ × kỳ với trạng thái; nút Khóa mềm / Khóa cứng / Mở lại theo quyền; màn "Checklist cuối kỳ".

**Lỗi đặc tả thường gặp:**
- Khóa cả hệ thống một trạng thái thay vì theo phân hệ.
- Không có khóa mềm → không xử lý được điều chỉnh cuối kỳ hợp lệ.
- Mở lại kỳ không log, không hạn chế.
- Không chặn ghi lùi kỳ đã đóng.

**Checklist đặc tả:**
- [ ] Kỳ theo tháng hay quý? Trạng thái kỳ gồm những gì?
- [ ] Khóa theo phân hệ chưa? Thứ tự đóng?
- [ ] Khóa mềm/cứng khác nhau thế nào, ai được ghi khi khóa mềm?
- [ ] Mở lại kỳ: ai, điều kiện, log gì?
- [ ] Thao tác cuối kỳ bắt buộc trước khi khóa là gì?

---

## P08 — Đa công ty · chi nhánh · tiền tệ · ngôn ngữ (Multi-org / Multi-currency / Multi-language)

**Khi nào dùng:** hệ thống dùng cho nhiều pháp nhân/chi nhánh, giao dịch nhiều tiền tệ, hiển thị nhiều ngôn ngữ. SAP: *Company Code / Controlling Area*, document/local/group currency, texts đa ngữ; Oracle: *Ledger / Legal Entity*.

**Hành vi chuẩn (bắt buộc đặc tả):**
1. **Cây tổ chức:** Tập đoàn → Công ty (pháp nhân) → Chi nhánh/Đơn vị → Kho/Bộ phận; dữ liệu chủ dùng chung hay riêng từng cấp (P17).
2. **Đa tiền tệ:** tiền giao dịch, tiền hạch toán (VND), tiền báo cáo/tập đoàn; bảng tỷ giá, loại tỷ giá (mua/bán/bình quân), đánh giá lại số dư gốc ngoại tệ cuối kỳ (413).
3. **Đánh số & chứng từ** tách theo công ty/chi nhánh (P06).
4. **Hợp nhất nội bộ:** loại trừ giao dịch nội bộ (intercompany) — nâng cao, link `r2r-general-ledger.md`.
5. **Đa ngôn ngữ:** nhãn giao diện và **dữ liệu** (tên vật tư, mẫu in) song ngữ; chọn ngôn ngữ theo người dùng.
6. **Múi giờ & định dạng:** mặc định Asia/Ho_Chi_Minh (UTC+7), `dd/MM/yyyy` (xem `conventions.md` §8).

**Trạng thái & chuyển trạng thái:** N/A – đặc điểm cấu trúc dữ liệu, không có vòng đời.

**Quy tắc chuẩn:**
- `BR-P08-01` — Mọi chứng từ PHẢI gắn công ty (pháp nhân) và chi nhánh; dữ liệu không rò rỉ giữa pháp nhân trừ khi có quyền hợp nhất (P17).
- `BR-P08-02` — Mọi giá trị tiền PHẢI lưu kèm mã tiền tệ; giá trị ngoại tệ lưu cả nguyên tệ + tỷ giá + quy đổi VND.
- `BR-P08-03` — Số dư gốc ngoại tệ cuối kỳ PHẢI đánh giá lại theo tỷ giá cuối kỳ (chênh lệch vào 413/635/515 — xem `vn-accounting.md`).
- `BR-P08-04` — Chuỗi dịch (translation) PHẢI tách khỏi code; thiếu bản dịch thì fallback về ngôn ngữ gốc, không để trống.
- `BR-P08-05` — Mã danh mục dùng chung đa pháp nhân PHẢI thống nhất; nếu khác chế độ kế toán (TT99 vs TT133) phải map tài khoản khi hợp nhất.

**Phân quyền điển hình:** người dùng gắn với một/nhiều công ty–chi nhánh; xem liên công ty chỉ cho vai trò tổng hợp (Kế toán trưởng tập đoàn, Giám đốc); cấu hình cây tổ chức & tỷ giá — Quản trị hệ thống.

**Tham số điển hình:**

| Mã | Tên | Kiểu | Mặc định | Tác dụng |
|---|---|---|---|---|
| `PRM-SYS-070` | Tiền tệ hạch toán | Chọn | VND | Local currency |
| `PRM-SYS-071` | Tiền tệ báo cáo tập đoàn | Chọn | N/A | Group currency |
| `PRM-SYS-072` | Loại tỷ giá mặc định | Chọn | Bình quân | Quy đổi |
| `PRM-SYS-073` | Ngôn ngữ hỗ trợ | Danh sách | vi, en | Đa ngữ |
| `PRM-SYS-074` | Chia sẻ danh mục giữa pháp nhân | Chọn | Theo loại | Dùng chung/riêng |

**Màn hình chuẩn:** bộ chọn Công ty/Chi nhánh ở thanh trên; cột Công ty/Chi nhánh/Tiền tệ trong list; form hiển thị song ngữ tên dữ liệu; màn cấu hình tỷ giá theo ngày.

**Lỗi đặc tả thường gặp:**
- Thiết kế một công ty rồi mới "chắp" đa pháp nhân → vỡ đánh số, phân quyền, hợp nhất.
- Chỉ lưu VND, mất nguyên tệ/tỷ giá.
- Dịch cứng trong code.
- Không xử lý khác chế độ kế toán giữa các pháp nhân.

**Checklist đặc tả:**
- [ ] Cây tổ chức mấy cấp? Chứng từ gắn cấp nào?
- [ ] Danh mục dùng chung hay riêng theo pháp nhân?
- [ ] Lưu những loại tiền tệ nào? Tỷ giá lấy đâu, đánh giá lại ra sao?
- [ ] Đánh số tách theo công ty/chi nhánh chưa (→ P06)?
- [ ] Đa ngôn ngữ ở nhãn và/hoặc dữ liệu? Fallback thế nào?
- [ ] Ai xem được dữ liệu liên công ty (→ P17)?

---

## P09 — Đính kèm, bình luận, lịch sử hoạt động (Attachments / Comments / Activity Log)

**Khi nào dùng:** gần như mọi danh mục & chứng từ. Odoo: *Chatter* (mixin `mail.thread`: log note, message, followers, schedule activity, field tracking) [10].

**Hành vi chuẩn (bắt buộc đặc tả):**
1. **Đính kèm (attachments):** upload nhiều file; loại file cho phép, kích thước tối đa, số lượng; xem trước, tải về, xóa (có quyền); lưu người tải lên + thời điểm.
2. **Bình luận/Ghi chú (comments / log note):** nội bộ (internal) vs gửi đối tác; @mention người dùng → sinh thông báo (P10).
3. **Người theo dõi (followers):** ai nhận cập nhật về bản ghi.
4. **Nhật ký hoạt động (activity log):** dòng thời gian các sự kiện nghiệp vụ (tạo, gửi duyệt, duyệt, ghi sổ, đính kèm…) — khác với audit field-level (P14): activity log là tường thuật nghiệp vụ, P14 là old/new từng trường.
5. **Việc cần làm (scheduled activity):** giao việc/nhắc hạn gắn vào bản ghi (gọi lại, kiểm tra).

**Trạng thái & chuyển trạng thái:** N/A.

**Quy tắc chuẩn:**
- `BR-P09-01` — File đính kèm PHẢI giới hạn loại & dung lượng theo `PRM`; quét mã độc nếu yêu cầu bảo mật (link `references/nfr-catalog.md`).
- `BR-P09-02` — Bình luận và activity log **chỉ thêm, không sửa/không xóa** (append-only) để giữ dấu vết.
- `BR-P09-03` — Phân biệt rõ ghi chú nội bộ vs nội dung gửi ra ngoài.
- `BR-P09-04` — Xóa đính kèm PHẢI log (ai, khi nào) và chỉ cho khi chứng từ chưa khóa/chưa ghi sổ, theo quyền.

**Phân quyền điển hình:** Xem/Thêm đính kèm & bình luận — người có quyền xem bản ghi; Xóa đính kèm — người tải lên hoặc quản trị; cấu hình loại/dung lượng — Quản trị hệ thống.

**Tham số điển hình:**

| Mã | Tên | Kiểu | Mặc định | Tác dụng |
|---|---|---|---|---|
| `PRM-SYS-080` | Loại file cho phép | Danh sách | pdf, jpg, png, xlsx, docx | Kiểm soát upload |
| `PRM-SYS-081` | Dung lượng tối đa/file (MB) | Số | 10 | Giới hạn |
| `PRM-SYS-082` | Số file tối đa/bản ghi | Số | 20 | Giới hạn |

**Màn hình chuẩn:** panel bên phải/khung dưới form: tab Đính kèm (danh sách file + nút tải lên), ô Bình luận + @mention, dòng thời gian hoạt động, danh sách người theo dõi, nút Lên lịch việc.

**Lỗi đặc tả thường gặp:**
- Không giới hạn loại/dung lượng file.
- Cho sửa/xóa bình luận & log → mất dấu vết.
- Lẫn activity log (nghiệp vụ) với audit trail field-level (P14).
- Không phân biệt ghi chú nội bộ và nội dung gửi đối tác.

**Checklist đặc tả:**
- [ ] Loại file & dung lượng tối đa là gì?
- [ ] Bình luận/log có append-only không?
- [ ] Có @mention sinh thông báo không (→ P10)?
- [ ] Phân biệt nội bộ/gửi ra ngoài chưa?
- [ ] Ai được xóa đính kèm, có log không?

---

## P10 — Thông báo & nhắc việc (Notifications & Reminders)

**Khi nào dùng:** báo sự kiện cần hành động — chờ duyệt, bị trả lại, quá hạn, sắp hết hạn hợp đồng, tồn kho dưới định mức. Kênh: in-app, email, **Zalo OA/ZNS**, SMS.

**Hành vi chuẩn (bắt buộc đặc tả):**
1. **Sự kiện kích hoạt (trigger):** theo thay đổi trạng thái (gửi duyệt, duyệt, từ chối) hoặc theo lịch (quá hạn SLA P03, sắp đến hạn).
2. **Người nhận:** theo vai trò/cấp duyệt/người theo dõi/người tạo.
3. **Kênh & mẫu (template):** mỗi loại thông báo chọn kênh; nội dung theo mẫu có biến (số CT, số tiền, hạn). **Zalo ZNS** chỉ dành cho công ty tại VN, chỉ gửi cho khách đã đồng ý & cung cấp SĐT, **một tin/một giao dịch**, phải dùng **mẫu đã được Zalo duyệt**, không nội dung quảng cáo, phải có ít nhất một biến giao dịch (mã đơn/số tiền/tên SP) [14].
4. **Gộp & chống spam:** gộp nhiều sự kiện, giới hạn tần suất; tránh gửi trùng.
5. **Nhắc lại (reminder/escalation):** nhắc theo chu kỳ tới khi xử lý; leo thang lên cấp trên.
6. **Theo dõi gửi:** trạng thái gửi/thất bại/đã đọc; thử lại (retry) khi lỗi (lưu ý: ZNS thường tính phí theo mỗi tin gửi thành công — đối chiếu bảng giá ZNS/ZCA, ⚠️ CHƯA XÁC MINH).

**Trạng thái & chuyển trạng thái:** N/A (có trạng thái gửi: Chờ gửi → Đã gửi → Đã đọc / Thất bại → Thử lại).

**Quy tắc chuẩn:**
- `BR-P10-01` — Mỗi loại thông báo PHẢI khai báo: sự kiện, người nhận, kênh, mẫu, điều kiện lặp lại (định nghĩa ở `03-specification/catalogs/integrations-notifications.md` — `NTF-…`).
- `BR-P10-02` — Gửi qua ZNS PHẢI tuân thủ ràng buộc nền tảng: mẫu đã duyệt, có biến giao dịch, không quảng cáo, có đồng ý của người nhận [14]. Vi phạm có thể bị chặn kênh.
- `BR-P10-03` — Thông báo PHẢI bất đồng bộ (queue) để không chặn nghiệp vụ; thất bại không làm hỏng giao dịch gốc.
- `BR-P10-04` — PHẢI có cơ chế chống gửi trùng (idempotency theo sự kiện) và giới hạn tần suất.
- `BR-P10-05` — Người dùng NÊN tùy chọn bật/tắt kênh cho từng loại (notification preference), trừ thông báo bắt buộc.

**Phân quyền điển hình:** cấu hình mẫu & quy tắc — Quản trị hệ thống; người dùng quản lý tùy chọn nhận của mình.

**Tham số điển hình:**

| Mã | Tên | Kiểu | Mặc định | Tác dụng |
|---|---|---|---|---|
| `PRM-SYS-090` | Kênh bật | Danh sách | In-app, Email | Thêm Zalo/SMS nếu có |
| `PRM-SYS-091` | Chu kỳ nhắc quá hạn | Số (giờ) | 24 | Reminder |
| `PRM-SYS-092` | Giới hạn tần suất/người/ngày | Số | 50 | Chống spam |
| `PRM-SYS-093` | Cấu hình ZNS (OA, template) | Bảng | Theo dự án | Zalo |

**Màn hình chuẩn:** chuông thông báo in-app (danh sách, đánh dấu đã đọc); màn "Cấu hình thông báo" (loại × kênh × người nhận × mẫu); màn "Nhật ký gửi" (trạng thái, thử lại); trang tùy chọn cá nhân.

**Lỗi đặc tả thường gặp:**
- Nói "gửi email/Zalo" mà không nêu sự kiện, người nhận, mẫu, tần suất.
- Gửi đồng bộ làm chậm/khóa giao dịch.
- Bỏ qua ràng buộc ZNS (mẫu duyệt, đồng ý, một tin/giao dịch) → bị chặn kênh.
- Không chống gửi trùng.

**Checklist đặc tả:**
- [ ] Mỗi thông báo: sự kiện nào, ai nhận, kênh nào, mẫu gì?
- [ ] Có nhắc lại/leo thang không? Chu kỳ?
- [ ] ZNS: mẫu đã duyệt? có biến giao dịch? có đồng ý người nhận?
- [ ] Gửi bất đồng bộ, lỗi có chặn nghiệp vụ không?
- [ ] Chống gửi trùng & giới hạn tần suất thế nào?
- [ ] Người dùng tùy chọn kênh được không?

---

## P11 — Mẫu in (Print Layouts)

**Khi nào dùng:** chứng từ cần bản in/PDF — PO, phiếu nhập/xuất, hóa đơn, phiếu thu/chi, biên bản. (Hóa đơn GTGT điện tử theo chuẩn riêng — xem `references/regulations/vn-tax-einvoice.md`, không tự thiết kế mẫu thuế.)

**Hành vi chuẩn (bắt buộc đặc tả):**
1. **Nhiều mẫu/một chứng từ:** chọn mẫu khi in; mẫu mặc định theo loại/công ty.
2. **Nội dung:** header (logo, pháp nhân, MST, địa chỉ), thân (bảng dòng), chân (tổng, **số tiền bằng chữ** cho phiếu thu/chi theo Luật Kế toán — xem `vn-accounting.md`), khối chữ ký.
3. **Song ngữ** (P08); khổ giấy, hướng, lề.
4. **Xuất PDF / in trực tiếp; đánh dấu "Bản sao / Reprint"** và đếm số lần in.
5. **Dữ liệu động:** QR/mã vạch, số chứng từ, trang x/y.
6. Mẫu cấu hình được (không hard-code) để đổi không cần sửa code.

**Trạng thái & chuyển trạng thái:** N/A.

**Quy tắc chuẩn:**
- `BR-P11-01` — Bản in PHẢI khớp số liệu chứng từ tại thời điểm in (đặc biệt sau làm tròn — P02).
- `BR-P11-02` — Phiếu thu/chi PHẢI in **số tiền bằng chữ**.
- `BR-P11-03` — In lại chứng từ đã ghi sổ NÊN đánh dấu "Bản sao" và log số lần in nếu yêu cầu kiểm soát.
- `BR-P11-04` — Mẫu in PHẢI tách khỏi code (template engine) và hỗ trợ đa ngôn ngữ/đa pháp nhân.

**Phân quyền điển hình:** In — vai trò nghiệp vụ liên quan; thiết kế/sửa mẫu — Quản trị hệ thống.

**Tham số điển hình:**

| Mã | Tên | Kiểu | Mặc định | Tác dụng |
|---|---|---|---|---|
| `PRM-SYS-100` | Mẫu in mặc định theo loại CT | Bảng | Theo dự án | Chọn mẫu |
| `PRM-SYS-101` | Khổ giấy | Chọn | A4 | Layout |
| `PRM-SYS-102` | Đánh dấu bản sao khi in lại | Luận lý | Có | Kiểm soát |

**Màn hình chuẩn:** nút In/Xuất PDF trên form (chọn mẫu, ngôn ngữ, số bản); trình thiết kế mẫu (quản trị); xem trước trước khi in.

**Lỗi đặc tả thường gặp:**
- Bản in lệch số với màn hình do làm tròn khác nhau.
- Quên số tiền bằng chữ cho phiếu thu/chi.
- Hard-code mẫu → đổi logo/địa chỉ phải sửa code.
- Nhầm mẫu in nội bộ với hóa đơn điện tử hợp lệ thuế.

**Checklist đặc tả:**
- [ ] Mỗi chứng từ có bao nhiêu mẫu? Mẫu mặc định?
- [ ] Có số tiền bằng chữ (phiếu thu/chi) không?
- [ ] Song ngữ & đa pháp nhân trên mẫu?
- [ ] Đánh dấu bản sao/đếm số lần in?
- [ ] Mẫu cấu hình được không cần sửa code?

---

## P12 — Nhập/Xuất Excel (Excel Import/Export)

**Khi nào dùng:** nhập liệu hàng loạt (danh mục, số dư đầu kỳ, bảng giá) và xuất dữ liệu. Áp cho hầu hết danh mục (P01) và nhiều chứng từ.

**Hành vi chuẩn (bắt buộc đặc tả):**
1. **Tải mẫu chuẩn (template):** cột đúng thứ tự, có chú thích, danh sách giá trị hợp lệ (dropdown), ví dụ mẫu.
2. **Validate:** kiểm tra định dạng, bắt buộc, tồn tại mã tham chiếu, trùng lặp, quy tắc nghiệp vụ; kiểm ở mức dòng.
3. **File lỗi (error file):** trả về đúng các dòng lỗi + cột "Lý do lỗi" để người dùng sửa và nhập lại.
4. **Nhập một phần (partial import):** dòng hợp lệ được nhận, dòng lỗi bị bỏ (hoặc tất-cả-hoặc-không — phải chọn chính sách).
5. **Idempotency / chống nhập trùng:** nhập lại cùng file không nhân đôi dữ liệu (theo khóa tự nhiên hoặc mã lô import).
6. **Chế độ:** Thêm mới / Cập nhật / Thêm-hoặc-cập-nhật (upsert); xem trước (preview) trước khi ghi.
7. **Giới hạn & nền:** số dòng tối đa/lần; file lớn chạy nền (P15) với báo tiến độ.
8. **Xuất:** theo bộ lọc hiện tại (P13), chọn cột, định dạng (xlsx/csv), mã hóa UTF-8.

**Trạng thái & chuyển trạng thái:** phiên import: Tải lên → Kiểm tra → Xem trước → Đang nhập → Hoàn tất/Hoàn tất một phần/Lỗi.

**Quy tắc chuẩn:**
- `BR-P12-01` — Mẫu import PHẢI là nguồn chuẩn; thừa/thiếu/sai cột PHẢI báo lỗi rõ, không nhập bừa.
- `BR-P12-02` — Validate PHẢI chạy **trước khi ghi**; có xem trước; dòng lỗi xuất ra error file kèm lý do.
- `BR-P12-03` — Chính sách nhập một phần vs toàn-bộ-hoặc-không PHẢI nêu rõ.
- `BR-P12-04` — Import PHẢI **idempotent**: xác định khóa để chống trùng; nhập lại file đã nhập không tạo bản ghi đôi.
- `BR-P12-05` — Mỗi lô import PHẢI log (ai, khi nào, file, số dòng nhận/lỗi) và truy được dữ liệu sinh ra từ lô nào (để hoàn tác nếu cần).
- `BR-P12-06` — Import vào dữ liệu có bút toán (số dư đầu kỳ) PHẢI kiểm soát kỳ mở (P07) và cân đối.

**Phân quyền điển hình:** Nhập file / Xuất file — vai trò được giao riêng (không mặc định cho mọi người); import số dư/giá — vai trò kế toán/quản trị.

**Tham số điển hình:**

| Mã | Tên | Kiểu | Mặc định | Tác dụng |
|---|---|---|---|---|
| `PRM-SYS-110` | Số dòng tối đa/lần nhập | Số | 5000 | Giới hạn; trên ngưỡng chạy nền |
| `PRM-SYS-111` | Chính sách nhập lỗi | Chọn | Nhập phần hợp lệ | Partial / all-or-nothing |
| `PRM-SYS-112` | Chế độ mặc định | Chọn | Thêm mới | Add/Update/Upsert |
| `PRM-SYS-113` | Mã hóa xuất | Chọn | UTF-8 | Tránh lỗi font |

**Màn hình chuẩn:** nút "Tải mẫu", "Nhập Excel" (chọn file → xem trước kết quả kiểm tra: số dòng hợp lệ/lỗi → tải error file → xác nhận nhập); "Xuất Excel" (chọn cột/bộ lọc); màn "Lịch sử import".

**Lỗi đặc tả thường gặp:**
- Không có file lỗi trả về → người dùng mò từng dòng.
- Không idempotent → nhập lại nhân đôi dữ liệu.
- Không nói rõ Add vs Update vs Upsert.
- Validate sau khi đã ghi một nửa → dữ liệu bẩn.
- Không giới hạn kích thước, file lớn làm treo.

**Checklist đặc tả:**
- [ ] Có mẫu chuẩn với cột & giá trị hợp lệ không?
- [ ] Validate những gì? Xem trước trước khi ghi?
- [ ] Có file lỗi kèm lý do không?
- [ ] Nhập một phần hay toàn-bộ-hoặc-không?
- [ ] Idempotent chống trùng bằng khóa nào?
- [ ] Add/Update/Upsert? Log lô import & hoàn tác được không?
- [ ] File lớn chạy nền, giới hạn dòng?

---

## P13 — Màn hình danh sách & tìm kiếm (List & Search Screen)

**Khi nào dùng:** mọi danh mục/chứng từ đều có màn danh sách để tra cứu, lọc, thao tác.

**Hành vi chuẩn (bắt buộc đặc tả):**
1. **Bộ lọc (filters):** theo trường quan trọng (trạng thái, khoảng ngày, đối tác, số tiền, chi nhánh); tìm nhanh (quick search) nhiều trường.
2. **Lưu bộ lọc (saved views):** người dùng lưu & đặt tên điều kiện lọc + cột + sắp xếp; chia sẻ view.
3. **Phân trang (paging) & tải thêm; sắp xếp (sorting) đa cột.**
4. **Chọn cột hiển thị, đổi thứ tự, ghim cột.**
5. **Thao tác hàng loạt (bulk actions):** duyệt/ghi sổ/đổi trạng thái/xóa/xuất nhiều bản ghi — tuân thủ quyền & trạng thái từng bản ghi.
6. **Xuất (export)** theo bộ lọc (P12); tổng phụ (subtotal) cuối lưới.
7. **Hiệu năng:** lọc/sắp ở phía server; mặc định có điều kiện để không tải toàn bộ.

**Trạng thái & chuyển trạng thái:** N/A.

**Quy tắc chuẩn:**
- `BR-P13-01` — Danh sách PHẢI áp **phạm vi dữ liệu** của người dùng (P17) — chỉ thấy bản ghi được phép.
- `BR-P13-02` — Lọc, sắp, phân trang PHẢI xử lý phía server; mặc định giới hạn (vd kỳ hiện tại) để tránh tải nặng.
- `BR-P13-03` — Bulk action PHẢI kiểm tra quyền & trạng thái **từng** bản ghi; bản ghi không hợp lệ bị bỏ qua và báo rõ (thành công/ bỏ qua/ lỗi).
- `BR-P13-04` — Export PHẢI theo đúng bộ lọc đang áp và chỉ cột người dùng được xem.

**Phân quyền điển hình:** Xem danh sách — theo P17; Bulk Duyệt/Ghi sổ — theo quyền hành động tương ứng; cấu hình view mặc định toàn hệ thống — Quản trị.

**Tham số điển hình:**

| Mã | Tên | Kiểu | Mặc định | Tác dụng |
|---|---|---|---|---|
| `PRM-SYS-120` | Kích thước trang | Số | 25 | Paging |
| `PRM-SYS-121` | Bộ lọc mặc định | Chọn | Kỳ hiện tại | Giảm tải |
| `PRM-SYS-122` | Cho lưu & chia sẻ view | Luận lý | Có | Saved views |

**Màn hình chuẩn:** thanh lọc trên + lưới dữ liệu + thanh công cụ (Thêm, Nhập/Xuất, Bulk actions) + phân trang dưới + vùng tổng phụ; cột cuối là menu hành động theo dòng (theo trạng thái).

**Lỗi đặc tả thường gặp:**
- Lọc/sắp phía client trên toàn bộ dữ liệu → chậm, sai khi phân trang.
- Bulk action bỏ qua quyền/trạng thái từng dòng.
- Không áp phạm vi dữ liệu → lộ dữ liệu.
- Không có saved view → người dùng lọc lại mỗi lần.

**Checklist đặc tả:**
- [ ] Cột hiển thị mặc định & cột cho chọn thêm là gì?
- [ ] Bộ lọc gồm trường nào? Có saved view không?
- [ ] Phân trang/sắp xếp phía server chưa? Bộ lọc mặc định?
- [ ] Bulk action nào? Kiểm tra quyền/trạng thái từng dòng ra sao?
- [ ] Có áp phạm vi dữ liệu (→ P17) không?
- [ ] Nút theo dòng thay đổi theo trạng thái thế nào?

---

## P14 — Nhật ký kiểm toán field-level (Audit Trail)

**Khi nào dùng:** dữ liệu nhạy cảm & chứng từ cần truy vết thay đổi từng trường. SAP: *Change Documents* (bảng CDHDR header ai/khi nào + CDPOS chi tiết VALUE_OLD/VALUE_NEW theo từng trường) [6]; Odoo: field tracking (`tracking=True`) ghi vào chatter [10]. Khác với activity log nghiệp vụ (P09).

**Hành vi chuẩn (bắt buộc đặc tả):**
1. **Phạm vi:** trường/bảng nào ghi audit (không nhất thiết mọi trường — chọn trường quan trọng để tránh phình dữ liệu).
2. **Nội dung mỗi bản ghi audit:** đối tượng, bản ghi, trường, **giá trị cũ → mới**, người thực hiện, thời điểm, hành động (tạo/sửa/xóa).
3. **Bất biến (append-only):** không ai sửa/xóa log, kể cả quản trị.
4. **Tra cứu:** theo bản ghi (lịch sử của 1 chứng từ) và theo người/khoảng thời gian (ai đổi gì).
5. **Đăng nhập & hành động hệ thống:** log login, phân quyền thay đổi, export dữ liệu lớn (yêu cầu bảo mật — `references/nfr-catalog.md`).
6. **Lưu trữ:** thời hạn giữ log theo quy định (dữ liệu kế toán lưu tối thiểu theo Luật Kế toán — xem `vn-accounting.md`).

**Trạng thái & chuyển trạng thái:** N/A.

**Quy tắc chuẩn:**
- `BR-P14-01` — Thay đổi trường trong phạm vi audit PHẢI ghi old/new + người + thời điểm; **không ghi đè**.
- `BR-P14-02` — Log audit **bất biến**, không có chức năng sửa/xóa trong ứng dụng.
- `BR-P14-03` — PHẢI tra được theo bản ghi và theo người dùng/khoảng thời gian.
- `BR-P14-04` — Thời hạn lưu log tối thiểu PHẢI theo quy định ngành/kế toán; không xóa trong thời hạn.
- `BR-P14-05` — Dữ liệu tài chính nhạy cảm (STK ngân hàng, hạn mức, giá) PHẢI nằm trong phạm vi audit (liên kết P01).

**Phân quyền điển hình:** Xem audit — kiểm toán nội bộ, quản trị, chủ dữ liệu (phạm vi của mình); không ai có quyền sửa/xóa log.

**Tham số điển hình:**

| Mã | Tên | Kiểu | Mặc định | Tác dụng |
|---|---|---|---|---|
| `PRM-SYS-130` | Danh sách trường ghi audit | Bảng | Theo dự án | Phạm vi |
| `PRM-SYS-131` | Thời hạn lưu log (năm) | Số | 10 | Theo Luật KT |
| `PRM-SYS-132` | Ghi log đăng nhập | Luận lý | Có | Bảo mật |

**Màn hình chuẩn:** tab "Lịch sử thay đổi" trên form (bảng trường/cũ/mới/người/thời điểm); màn "Nhật ký kiểm toán" toàn hệ thống (lọc theo đối tượng, người, thời gian, hành động); không có nút sửa/xóa.

**Lỗi đặc tả thường gặp:**
- Ghi audit "mọi thứ" → phình dữ liệu, chậm; hoặc ngược lại không ghi trường nhạy cảm.
- Log cho phép sửa/xóa → vô giá trị khi kiểm toán.
- Chỉ lưu "đã sửa" mà không lưu giá trị cũ→mới.
- Nhầm với activity log (P09).

**Checklist đặc tả:**
- [ ] Trường/bảng nào ghi audit field-level?
- [ ] Mỗi bản ghi lưu old/new/ai/khi nào/hành động chưa?
- [ ] Log có bất biến không?
- [ ] Tra được theo bản ghi và theo người/thời gian?
- [ ] Thời hạn lưu bao lâu?

---

## P15 — Tác vụ nền / định kỳ (Background & Scheduled Jobs)

**Khi nào dùng:** xử lý khối lượng lớn hoặc chạy theo lịch — chạy MRP (MRP run), trích khấu hao (depreciation run), tính giá vốn/giá thành (costing), kết chuyển cuối kỳ, đánh giá lại tỷ giá, tính lương, đồng bộ tích hợp. SAP: *background jobs* (SM36/SM37); khấu hao AFAB (planned run / repeat run / restart) [7]; Dynamics: *batch jobs*.

**Hành vi chuẩn (bắt buộc đặc tả):**
1. **Kích hoạt:** thủ công (có tham số: kỳ, phạm vi) và/hoặc theo lịch (cron); **chạy thử (test/simulation)** trước khi chạy thật (SAP khuyến cáo test run khấu hao trước [7]).
2. **Tham số đầu vào:** kỳ, công ty/chi nhánh, phạm vi đối tượng (vd chỉ một số tài sản).
3. **Nhật ký chạy (run log):** thời gian bắt đầu/kết thúc, người chạy, tham số, số bản ghi xử lý/thành công/lỗi, thông điệp lỗi từng dòng.
4. **Khóa chống chạy trùng (locking):** không cho 2 lần chạy cùng kỳ/phạm vi song song.
5. **Chạy lại (re-run / repeat):** xử lý phần thay đổi hoặc phần lỗi; **không nhân đôi** kết quả (khấu hao repeat run chỉ ghi phần chênh so với lần trước [7]).
6. **Khởi động lại (restart)** khi job gián đoạn giữa chừng, tiếp tục từ điểm dừng [7].
7. **Kết quả & hoàn tác:** job sinh bút toán (khấu hao, kết chuyển) phải liên kết P05; cho đảo/hủy kết quả nếu sai (qua đảo bút toán, không xóa).

**Trạng thái & chuyển trạng thái:**

```mermaid
stateDiagram-v2
    state "Chờ chạy" as QUEUED
    state "Đang chạy" as RUNNING
    state "Hoàn tất" as DONE
    state "Hoàn tất có lỗi dòng" as PARTIAL
    state "Thất bại" as FAILED
    [*] --> QUEUED
    QUEUED --> RUNNING: Bắt đầu
    RUNNING --> DONE: Xong không lỗi
    RUNNING --> PARTIAL: Xong còn dòng lỗi
    RUNNING --> FAILED: Gián đoạn
    FAILED --> RUNNING: Khởi động lại
    PARTIAL --> RUNNING: Chạy lại phần lỗi
```

**Quy tắc chuẩn:**
- `BR-P15-01` — Job ghi sổ/ảnh hưởng số liệu PHẢI có **chế độ chạy thử** cho ra kết quả dự kiến trước khi chạy thật.
- `BR-P15-02` — PHẢI chống chạy trùng bằng khóa theo kỳ/phạm vi; lần chạy chính thức mỗi kỳ **chỉ một lần** (các lần sau là repeat/chênh lệch).
- `BR-P15-03` — Mỗi lần chạy PHẢI ghi run log đầy đủ (tham số, số liệu, lỗi); lỗi một dòng không làm hỏng cả job (trừ job cần nguyên tử).
- `BR-P15-04` — Chạy lại PHẢI idempotent: chỉ xử lý phần còn thiếu/thay đổi, không nhân đôi.
- `BR-P15-05` — Kết quả sai PHẢI sửa bằng đảo/bỏ ghi sổ (P05), không xóa dữ liệu đã sinh.
- `BR-P15-06` — Job theo lịch PHẢI báo khi thất bại (P10) và cho xem trạng thái.

**Phân quyền điển hình:** Chạy job nghiệp vụ — kế toán/kế hoạch phụ trách (khấu hao: kế toán TSCĐ; MRP: kế hoạch sản xuất); cấu hình lịch — Quản trị hệ thống; xem run log — người phụ trách + quản trị.

**Tham số điển hình:**

| Mã | Tên | Kiểu | Mặc định | Tác dụng |
|---|---|---|---|---|
| `PRM-SYS-140` | Lịch chạy (cron) | Chuỗi | Theo job | Định kỳ |
| `PRM-SYS-141` | Cho chạy thử | Luận lý | Có | Simulation |
| `PRM-SYS-142` | Khóa chống chạy trùng | Luận lý | Có | Locking |
| `PRM-SYS-143` | Giữ run log (ngày) | Số | 365 | Lưu trữ |

**Màn hình chuẩn:** màn "Chạy tác vụ" (chọn tham số, nút Chạy thử / Chạy thật); màn "Nhật ký tác vụ" (danh sách lần chạy, trạng thái, số liệu, tải log lỗi, nút Chạy lại/Khởi động lại); lịch cấu hình job định kỳ.

**Lỗi đặc tả thường gặp:**
- Không có chạy thử → chạy thật sai phải đảo hàng loạt.
- Không khóa chống chạy trùng → nhân đôi khấu hao/bút toán.
- Chạy lại nhân đôi kết quả (không idempotent).
- Không có run log → không biết job làm gì, lỗi ở đâu.
- Lỗi một dòng làm hỏng cả mẻ không cần thiết.

**Checklist đặc tả:**
- [ ] Job chạy thủ công hay theo lịch? Tham số đầu vào?
- [ ] Có chạy thử trước không?
- [ ] Chống chạy trùng thế nào? Mỗi kỳ chạy chính thức mấy lần?
- [ ] Run log ghi gì? Xem lỗi từng dòng được không?
- [ ] Chạy lại/khởi động lại có idempotent không?
- [ ] Kết quả sai sửa bằng đảo hay xóa?

---

## P16 — Tích hợp (Integration: API / File / Event)

**Khi nào dùng:** trao đổi dữ liệu với hệ thống ngoài — hóa đơn điện tử, ngân hàng, thuế, sàn TMĐT, hệ thống khác của khách. Định nghĩa ở `03-specification/catalogs/integrations-notifications.md` (`INT-…`).

**Hành vi chuẩn (bắt buộc đặc tả):**
1. **Phương thức:** API đồng bộ (REST/SOAP), file (SFTP/CSV/XML) theo lô, hoặc event/message queue (bất đồng bộ).
2. **Chiều & kích hoạt:** đẩy (push) khi sự kiện, kéo (pull) theo lịch, hay webhook nhận về.
3. **Idempotency:** mỗi bản tin có khóa idempotent; gửi lại cùng khóa không tạo trùng (quan trọng khi retry).
4. **Thử lại (retry) & backoff:** số lần, khoảng cách; sau khi hết → hàng đợi lỗi (dead-letter) + cảnh báo (P10).
5. **Đối soát (reconciliation):** định kỳ so khớp số bản ghi/giá trị hai đầu; báo cáo lệch.
6. **Ánh xạ dữ liệu (mapping):** trường ↔ trường, mã ↔ mã (vd mã hàng nội bộ ↔ mã sàn); xử lý giá trị thiếu.
7. **Bảo mật:** xác thực (API key/OAuth/chữ ký số), mã hóa, log bản tin (che dữ liệu nhạy cảm).
8. **Xử lý lỗi & trạng thái:** mỗi giao dịch tích hợp có trạng thái (Chờ gửi/Đã gửi/Thành công/Lỗi/Đã đối soát).

**Trạng thái & chuyển trạng thái:**

```mermaid
stateDiagram-v2
    state "Chờ gửi" as PENDING
    state "Đã gửi" as SENT
    state "Thành công" as SUCCESS
    state "Lỗi" as ERROR
    state "Hàng đợi lỗi" as DEADLETTER
    [*] --> PENDING
    PENDING --> SENT: Gửi
    SENT --> SUCCESS: Nhận xác nhận
    SENT --> ERROR: Lỗi/timeout
    ERROR --> SENT: Thử lại
    ERROR --> DEADLETTER: Hết số lần thử
```

**Quy tắc chuẩn:**
- `BR-P16-01` — Mỗi giao dịch tích hợp PHẢI có **khóa idempotent**; nhận/gửi trùng khóa không xử lý lần hai.
- `BR-P16-02` — PHẢI có retry với backoff và hàng đợi lỗi; lỗi tích hợp **không được** làm hỏng/khóa nghiệp vụ gốc.
- `BR-P16-03` — PHẢI có đối soát định kỳ và báo cáo lệch; không dựa vào "gửi là xong".
- `BR-P16-04` — PHẢI log bản tin gửi/nhận (có che dữ liệu nhạy cảm) để truy vết & xử lý tranh chấp.
- `BR-P16-05` — Bảng ánh xạ mã PHẢI cấu hình được; gặp mã lạ → báo lỗi có kiểm soát, không bỏ im.
- `BR-P16-06` — Hợp đồng dữ liệu (schema, mã lỗi, phiên bản API) PHẢI nêu rõ; đổi version có chiến lược tương thích.

**Phân quyền điển hình:** cấu hình kết nối & mapping — Quản trị hệ thống; xem log & xử lý lỗi/đối soát — người phụ trách tích hợp + kế toán liên quan.

**Tham số điển hình:**

| Mã | Tên | Kiểu | Mặc định | Tác dụng |
|---|---|---|---|---|
| `PRM-SYS-150` | Số lần thử lại | Số | 5 | Retry |
| `PRM-SYS-151` | Khoảng backoff | Chuỗi | Lũy tiến | Giãn thử lại |
| `PRM-SYS-152` | Chu kỳ đối soát | Chọn | Hàng ngày | Reconciliation |
| `PRM-SYS-153` | Giữ log bản tin (ngày) | Số | 180 | Truy vết |

**Màn hình chuẩn:** màn "Kết nối" (cấu hình endpoint, xác thực); "Hàng đợi/Nhật ký tích hợp" (danh sách bản tin, trạng thái, nút Thử lại/Xem payload); "Báo cáo đối soát" (lệch hai đầu).

**Lỗi đặc tả thường gặp:**
- Không idempotent → retry sinh bản ghi/đơn trùng.
- Lỗi tích hợp làm rollback/khóa giao dịch gốc.
- Không đối soát → lệch âm thầm, phát hiện muộn.
- Không log payload → không xử lý được tranh chấp.
- Không có bảng mapping mã → vỡ khi đối tác đổi mã.

**Checklist đặc tả:**
- [ ] Phương thức & chiều tích hợp? Kích hoạt khi nào?
- [ ] Khóa idempotent là gì? Chống trùng ra sao?
- [ ] Retry/backoff/dead-letter thế nào? Lỗi có ảnh hưởng nghiệp vụ gốc không?
- [ ] Đối soát định kỳ ra sao, báo lệch thế nào?
- [ ] Mapping dữ liệu & xử lý mã lạ?
- [ ] Log bản tin, bảo mật, phiên bản API?

---

## P17 — Phạm vi dữ liệu theo tổ chức / người sở hữu (Data Scope / Access Control)

**Khi nào dùng:** kiểm soát **ai thấy/sửa dữ liệu nào** — không chỉ "có quyền hành động" mà còn "trên phạm vi nào". Ma trận quyền tổng & SoD định nghĩa ở `03-specification/catalogs/roles-permissions.md`; chi tiết tham số/bảo mật xem `references/security-and-parameters.md`.

**Hành vi chuẩn (bắt buộc đặc tả):**
1. **Chiều phạm vi (scope dimensions):** Của mình / Phòng ban / Chi nhánh / Công ty / Toàn hệ thống; hoặc theo kho/dự án/nhóm khách hàng.
2. **Gắn quyền × phạm vi:** mỗi hành động (Xem/Sửa/Duyệt…) đi kèm phạm vi (vd Nhân viên bán hàng: Xem đơn của mình; Trưởng phòng: Xem đơn cả phòng).
3. **Người sở hữu (ownership):** bản ghi gắn người tạo/người phụ trách; quy tắc chuyển giao (reassign).
4. **Lọc dữ liệu tự động:** mọi list/report/API áp phạm vi của người dùng (P13, P18).
5. **Chia sẻ ngoại lệ:** chia sẻ bản ghi cụ thể cho người ngoài phạm vi (có log).
6. **SoD (tách biệt trách nhiệm):** người tạo ≠ người duyệt ≠ người ghi sổ cho cùng giao dịch (liên kết P03, P05).

**Trạng thái & chuyển trạng thái:** N/A.

**Quy tắc chuẩn:**
- `BR-P17-01` — Mọi truy vấn danh sách/báo cáo/API PHẢI tự động áp phạm vi dữ liệu của người dùng; **không** dựa vào ẩn nút ở UI.
- `BR-P17-02` — Quyền = (hành động × phạm vi); spec PHẢI ghi cả hai, không chỉ hành động.
- `BR-P17-03` — Chuyển giao quyền sở hữu & chia sẻ ngoại lệ PHẢI log.
- `BR-P17-04` — Ràng buộc SoD PHẢI kiểm tra ở backend (vd chặn người tạo tự duyệt — P03).
- `BR-P17-05` — Vai trò & phạm vi là cấu hình; không hard-code theo tài khoản người dùng cụ thể.

**Phân quyền điển hình:** cấu hình vai trò & phạm vi — Quản trị hệ thống; chủ dữ liệu thao tác trong phạm vi được cấp; vai trò tổng hợp (Giám đốc, Kế toán trưởng) có phạm vi rộng hơn.

**Tham số điển hình:**

| Mã | Tên | Kiểu | Mặc định | Tác dụng |
|---|---|---|---|---|
| `PRM-SYS-160` | Các chiều phạm vi áp dụng | Danh sách | Chi nhánh, Phòng, Của mình | Scope |
| `PRM-SYS-161` | Cho chia sẻ ngoại lệ | Luận lý | Có (log) | Sharing |
| `PRM-SYS-162` | Ràng buộc SoD bật | Bảng | Theo dự án | Kiểm soát |

**Màn hình chuẩn:** màn "Vai trò & quyền" (hành động × phạm vi); màn "Gán người dùng vào công ty/chi nhánh/phòng"; nút "Chuyển phụ trách", "Chia sẻ" trên bản ghi.

**Lỗi đặc tả thường gặp:**
- Chỉ ghi "có quyền xem đơn hàng" mà không nói phạm vi nào.
- Áp phạm vi chỉ bằng ẩn nút ở UI, backend vẫn trả hết dữ liệu.
- Hard-code người dùng vào logic.
- Bỏ SoD → một người làm trọn vòng (rủi ro gian lận).

**Checklist đặc tả:**
- [ ] Các chiều phạm vi là gì?
- [ ] Mỗi hành động gắn phạm vi nào cho vai trò nào?
- [ ] Lọc dữ liệu áp ở backend cho list/report/API chưa?
- [ ] Quy tắc sở hữu & chuyển giao & chia sẻ ngoại lệ?
- [ ] Có ràng buộc SoD nào? Kiểm tra ở đâu?

---

## P18 — Dashboard & KPI

**Khi nào dùng:** màn tổng quan số liệu & chỉ số điều hành theo vai trò (mua hàng, bán hàng, kho, tài chính). Danh sách báo cáo định nghĩa ở `03-specification/catalogs/reports.md` (`RPT-…`).

**Hành vi chuẩn (bắt buộc đặc tả):**
1. **Định nghĩa KPI tường minh:** công thức, tử/mẫu số, nguồn dữ liệu, đơn vị, kỳ so sánh (kỳ trước/cùng kỳ năm trước/kế hoạch).
2. **Widget:** thẻ số (card), biểu đồ (line/bar/pie), bảng top-N, phễu; bộ lọc toàn trang (kỳ, chi nhánh).
3. **Drill-down:** bấm số → danh sách/chứng từ chi tiết (liên kết P13).
4. **Phạm vi dữ liệu:** áp P17 — mỗi người xem KPI theo phạm vi của mình.
5. **Thời điểm dữ liệu:** thời gian thực hay theo lô (và độ trễ); hiển thị "cập nhật lúc".
6. **Hiệu năng:** dùng bảng tổng hợp/cache cho KPI nặng; không tính trực tiếp trên bảng giao dịch lớn mỗi lần mở.

**Trạng thái & chuyển trạng thái:** N/A.

**Quy tắc chuẩn:**
- `BR-P18-01` — Mỗi KPI PHẢI có định nghĩa công thức + nguồn + kỳ; không để "doanh thu" chung chung (gross/net? gồm thuế?).
- `BR-P18-02` — Dashboard PHẢI áp phạm vi dữ liệu người dùng (P17); hai người vai trò khác nhau thấy số khác nhau là đúng.
- `BR-P18-03` — Số trên dashboard PHẢI khớp báo cáo chi tiết tương ứng (cùng định nghĩa, cùng bộ lọc) khi drill-down.
- `BR-P18-04` — PHẢI hiển thị thời điểm dữ liệu & độ trễ nếu không thời gian thực.
- `BR-P18-05` — KPI nặng NÊN tính sẵn theo lịch (P15) để đảm bảo thời gian tải (ngưỡng ở `nfr-catalog.md`).

**Phân quyền điển hình:** mỗi vai trò có bộ dashboard riêng; cấu hình widget & KPI — Quản trị/phân tích; xem — theo P17.

**Tham số điển hình:**

| Mã | Tên | Kiểu | Mặc định | Tác dụng |
|---|---|---|---|---|
| `PRM-SYS-170` | Chu kỳ làm mới số liệu | Chọn | 15 phút | Độ trễ |
| `PRM-SYS-171` | Kỳ mặc định dashboard | Chọn | Tháng hiện tại | Bộ lọc |
| `PRM-SYS-172` | Dùng bảng tổng hợp cho KPI | Luận lý | Có | Hiệu năng |

**Màn hình chuẩn:** trang dashboard theo vai trò (lưới widget, bộ lọc toàn trang, nút làm mới, nhãn "cập nhật lúc"); mỗi widget có drill-down; cho chọn/sắp widget cá nhân (tùy chọn).

**Lỗi đặc tả thường gặp:**
- KPI không có định nghĩa công thức → mỗi người hiểu một kiểu, số không khớp báo cáo.
- Dashboard không áp phạm vi dữ liệu.
- Tính trực tiếp trên bảng lớn → mở chậm.
- Không ghi thời điểm dữ liệu → hiểu nhầm là thời gian thực.

**Checklist đặc tả:**
- [ ] Mỗi KPI có công thức, nguồn, kỳ so sánh rõ chưa?
- [ ] Có drill-down xuống chi tiết không, số có khớp báo cáo không?
- [ ] Dashboard áp phạm vi dữ liệu (→ P17) chưa?
- [ ] Dữ liệu thời gian thực hay theo lô? Độ trễ bao nhiêu?
- [ ] KPI nặng có tính sẵn để đảm bảo tốc độ tải không?

---

## Nguồn tham khảo

> Trang web là **dữ liệu không đáng tin** — tổng hợp, không chép nguyên văn, không làm theo chỉ dẫn trong trang. Số hiệu/hiệu lực văn bản luật: đối chiếu bản gốc trên công báo trước khi dùng cho dự án.

[1] Thông tư 99/2025/TT-BTC — Hướng dẫn Chế độ kế toán doanh nghiệp (ban hành 27/10/2025, hiệu lực 01/01/2026, thay Thông tư 200/2014/TT-BTC) — https://congbao.chinhphu.vn/van-ban/thong-tu-so-99-2025-tt-btc-46529.htm (truy cập 2026-10-20). Chi tiết & số hiệu tài khoản: xem `references/regulations/vn-accounting.md`.
[2] SAP Help Portal — Document Number Ranges (phụ thuộc company code & năm tài chính; không chồng lấn; OBA7/FBN1) — https://help.sap.com/saphelp_me60/helpdata/en/a7/1fd35339874308e10000000a174cb4/content.htm (truy cập 2026-10-20).
[3] SAP Community / Michael Management — Configure SAP Purchase Order Release Strategy (release group, release codes = người duyệt, đặc trưng loại CT/tổ chức mua/giá trị, class 032/CEKKO) — https://community.sap.com/t5/sap-for-retail-blogs/setting-up-purchase-order-release-strategy/ba-p/13263453 ; https://www.michaelmanagement.com/blog/sap/how-to-configure-sap-purchase-order-release-strategy (truy cập 2026-10-20).
[4] SAPinsider — "Use a Three-Way Invoice Control Assessment to Reduce the Risk of Fraud": Logistics Invoice Verification / three-way match PO–nhập kho–hóa đơn; dung sai qua tolerance key (DW cho sai lệch số lượng, PP/PE cho sai lệch giá); chặn thanh toán (Payment Block R) — https://sapinsider.org/?p=16140 (truy cập 2026-10-20). (Một phần nội dung sau tường thành viên.)
[5] Copy Control & Document Flow trong SAP S/4HANA SD (VTAA sales–sales, VTLA sales–delivery, VTFL delivery–billing; mức header/dòng/lịch giao hàng; copying requirements & data transfer routines ở VOFM; create with reference) — https://open-exam-prep.com/study-guides/sap-s4hana-sd/sales-documents-orders/copying-control-document-flow (truy cập 2026-10-20). ⚠️ Học liệu bên thứ ba (trang SAP Learning cũ đã gỡ, trả 404); đối chiếu "Copying Control" trên help.sap.com theo đúng phiên bản sản phẩm của dự án.
[6] Surety Systems — Utilizing SAP CDPOS/CDHDR for change documents (CDHDR header ai/khi nào; CDPOS VALUE_OLD/VALUE_NEW theo trường; bật "Log data changes" ở SE11; SCDO/SCU3) — https://www.suretysystems.com/insights/utilizing-an-sap-cdpos-table-to-improve-document-management/ (truy cập 2026-10-20).
[7] SAP Help Portal — Executing the Depreciation Run / AFAB (planned posting run; repeat run chỉ ghi phần chênh & giới hạn theo tài sản; restart qua TABA-XBUKZ; test run; mỗi kỳ chạy chính thức một lần) — https://help.sap.com/saphelp_46c/helpdata/en/fb/f6b96c0cfd11d3b65d0000e82d962e/content.htm (truy cập 2026-10-20).
[8] Odoo Documentation (16.0) — Bill control policies / 3-way matching (ordered vs received quantities; trường "Should Be Paid" Yes/No/Exception; nhập một phần chỉ gồm SL đã nhận) — https://www.odoo.com/documentation/16.0/applications/inventory_and_mrp/purchase/manage_deals/control_bills.html (truy cập 2026-10-20).
[9] Cybrosys — Odoo 18/19 Accounting: Credit Note (reverse entry wizard: lý do + ngày đảo) & Lock Dates (Lock Sales/Purchases/Everything/Hard Lock; hóa đơn đã đối chiếu hoặc trong kỳ khóa không hủy được → phải tạo credit note) — https://www.cybrosys.com/odoo/odoo-books/odoo-19-accounting/accounting-features-and-tools/lock-dates/ (truy cập 2026-10-20).
[10] Odoo Developer Documentation — Mixins and Useful Classes (mixin `mail.thread`, chatter: log note, message, followers, `reload_on_follower`; field tracking bằng `tracking=True`; schedule activity) — https://www.odoo.com/documentation/18.0/developer/reference/backend/mixins.html (truy cập 2026-10-20).
[11] Microsoft Learn — Number sequences (Dynamics 365 Finance): scope quyết định tổ chức dùng chung; cờ continuous cho dãy không nhảy cách (SO/PO/hóa đơn) — https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/tasks/set-up-number-sequences-individual-basis (truy cập 2026-10-20).
[12] Oracle Help Center — Guidelines for Managing Document Sequences (kiểu Automatic/Gapless/Manual; gapless chỉ cấp số khi tạo thành công & cân nhắc hiệu năng; Manual chỉ kiểm tra duy nhất; không đổi kiểu khi đã dùng) — https://docs.oracle.com/en/cloud/saas/financials/24a/fafcf/document-sequences.html (truy cập 2026-10-20).
[13] Oracle — Subledger Accounting (SLA): engine quy tắc giữa sổ con và sổ cái; account derivation rules & journal line types; accounting method gán cho ledger; Create Accounting draft vs final — https://docs.oracle.com/cd/E26401_01/doc.122/e48829/T372621T464264.htm (truy cập 2026-10-20).
[14] Infobip — Zalo (ZNS) Compliance and guidelines: chỉ công ty tại VN; cần người nhận đồng ý & cung cấp SĐT; một tin/một giao dịch; dùng mẫu đã được Zalo duyệt, không quảng cáo, phải có ít nhất một biến giao dịch — https://www.infobip.com/docs/zalo/compliance-guidelines (truy cập 2026-10-20). Tài liệu của Infobip (đại lý), KHÔNG phải điều khoản chính thức của Zalo — xác nhận lại với Zalo/ZCA trước khi triển khai.

> Tham chiếu chéo trong skill (không trùng lặp nội dung): `references/conventions.md` (ID/trạng thái/quyền/định dạng), `references/regulations/vn-accounting.md` (tài khoản, Luật Kế toán), `references/regulations/vn-tax-einvoice.md` (thuế GTGT, hóa đơn điện tử), `references/processes/r2r-general-ledger.md` (ghi sổ, đảo, khóa kỳ, kết chuyển), `references/processes/p2p-procure-to-pay.md` & `o2c-order-to-cash.md` (luồng chứng từ), `references/processes/fixed-assets.md` (khấu hao), `references/security-and-parameters.md` (phạm vi & tham số), `references/nfr-catalog.md` (hiệu năng, bảo mật, lưu trữ).
