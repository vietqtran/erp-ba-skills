# Quy ước chung (nguồn sự thật duy nhất về định dạng)

Mọi template, checklist và script `scripts/ba.py` đều dựa trên file này. Khi có mâu thuẫn giữa file khác và file này, file này thắng.

## Mục lục
1. Cấu trúc thư mục workspace tài liệu
2. Hệ thống mã định danh (ID)
3. Nơi định nghĩa từng loại ID
4. Marker bắt buộc (đánh dấu chưa rõ / đề xuất / giả định)
5. Trạng thái tài liệu
6. Bộ trạng thái chứng từ chuẩn & hành động phân quyền chuẩn
7. Quy tắc viết yêu cầu
8. Định dạng số, ngày, tiền tệ
9. Sơ đồ
10. Ngôn ngữ & thuật ngữ

---

## 1. Cấu trúc thư mục workspace tài liệu

Mỗi dự án/sản phẩm có một thư mục gốc (gọi là `<root>`, ví dụ `docs/ba/ABC-ERP/`). Tạo bằng `python3 scripts/ba.py init <root> --project "<tên>"`.

```
<root>/
├── 00-inputs/
│   ├── source-register.md          # Sổ đăng ký nguồn đầu vào (SRC-xxx, MTG-xxx)
│   ├── meetings/MTG-001-<yyyy-mm-dd>.md   # Biên bản họp (1 file / buổi)
│   └── files/                      # File gốc khách hàng gửi (Excel, PDF, ảnh, email...)
├── 01-research/
│   ├── research-report.md          # Bước 1 — báo cáo research
│   └── feature-catalog.md          # Bước 1 — danh mục tính năng ứng viên (FEAT)
├── 02-requirements/
│   ├── requirements-overview.md    # Bước 2 — tài liệu tổng quan + quy trình tổng quan (BP)
│   ├── requirement-register.md     # Bước 2 — sổ yêu cầu gốc (REQ)
│   └── issue-log.md                # Câu hỏi (Q), giả định (ASM), quyết định (DEC), mâu thuẫn (CFL), thay đổi (CHG)
├── 03-specification/
│   ├── srs-overview.md             # Bước 3 — SRS tổng: module, danh sách chức năng, BR chung, NFR
│   ├── catalogs/
│   │   ├── roles-permissions.md    # ROLE + ma trận quyền tổng + SoD + hạn mức duyệt
│   │   ├── master-data.md          # MD — danh mục
│   │   ├── document-types.md       # DOC — loại chứng từ, đánh số, bộ trạng thái
│   │   ├── system-parameters.md    # PRM — tham số hệ thống
│   │   ├── reports.md              # RPT — danh sách báo cáo
│   │   ├── integrations-notifications.md  # INT, NTF
│   │   └── glossary.md             # Thuật ngữ dự án
│   └── functions/<MOD>/FN-<MOD>-<NN>-<slug>.md   # Đặc tả từng chức năng / báo cáo
├── 04-verification/verify-report-r<N>.md        # Bước 4 — tự kiểm vòng N
├── 05-review/review-report-r<N>.md              # Bước 5 — review độc lập vòng N
├── traceability.md                 # SINH TỰ ĐỘNG bởi `ba.py trace` — không sửa tay
└── lint-report.md                  # SINH TỰ ĐỘNG bởi `ba.py lint`
```

Không tự đổi tên/di chuyển các file trên: script dựa vào đường dẫn để biết đâu là nơi định nghĩa ID.

## 2. Hệ thống mã định danh (ID)

| Tiền tố | Ý nghĩa | Định dạng | Ví dụ |
|---|---|---|---|
| SRC | Nguồn đầu vào (tài liệu KH, email, file Excel, ảnh chụp) | SRC-NNN | SRC-004 |
| MTG | Biên bản họp | MTG-NNN | MTG-002 |
| FEAT | Tính năng ứng viên từ research | FEAT-<MOD>-NN | FEAT-PUR-07 |
| REQ | Yêu cầu gốc của khách hàng (nguyên tử) | REQ-NNN | REQ-031 |
| BO | Mục tiêu kinh doanh đo được | BO-NN | BO-01 |
| BP | Quy trình nghiệp vụ đầu-cuối | BP-NN | BP-02 |
| MOD | Module | MOD-<MOD> | MOD-PUR |
| FN | Chức năng (1 file đặc tả) | FN-<MOD>-NN | FN-PUR-03 |
| FR | Yêu cầu chức năng (thuộc 1 FN) | FR-<MOD>-NN-NN | FR-PUR-03-02 |
| BR | Quy tắc nghiệp vụ của FN / toàn hệ thống | BR-<MOD>-NN-NN / BR-GEN-NN | BR-PUR-03-05, BR-GEN-04 |
| US | User story | US-<MOD>-NN-NN | US-PUR-03-01 |
| AC | Tiêu chí nghiệm thu | AC-<MOD>-NN-NN | AC-PUR-03-04 |
| MSG | Thông báo / lỗi hiển thị | MSG-<MOD>-NN-NN | MSG-PUR-03-02 |
| NFR | Yêu cầu phi chức năng chung / riêng FN | NFR-<CAT>-NN / NFR-<MOD>-NN-NN | NFR-PERF-01 |
| ROLE | Vai trò người dùng | ROLE-<CODE> | ROLE-PUR-MGR |
| SOD | Quy tắc phân tách nhiệm vụ | SOD-NN | SOD-01 |
| PRM | Tham số hệ thống | PRM-<MOD>-NNN | PRM-PUR-004 |
| MD | Danh mục (master data) | MD-<CODE> | MD-VENDOR |
| DOC | Loại chứng từ | DOC-<CODE> | DOC-PO |
| RPT | Báo cáo | RPT-<MOD>-NN | RPT-INV-02 |
| INT | Tích hợp hệ thống ngoài | INT-NN | INT-03 |
| NTF | Thông báo tự động | NTF-<MOD>-NN | NTF-PUR-01 |
| Q | Câu hỏi mở | Q-NNN | Q-012 |
| ASM | Giả định | ASM-NNN | ASM-003 |
| DEC | Quyết định đã chốt | DEC-NNN | DEC-007 |
| CFL | Mâu thuẫn giữa các nguồn | CFL-NNN | CFL-002 |
| CHG | Yêu cầu thay đổi | CHG-NNN | CHG-001 |
| VF | Phát hiện khi tự kiểm (bước 4) | VF-R<N>-NN | VF-R1-08 |
| RV | Phát hiện khi review độc lập (bước 5) | RV-R<N>-NN | RV-R2-03 |

- `<MOD>`: 2–5 chữ in hoa, khai báo trong `srs-overview.md` mục 2. Gợi ý: SYS (hệ thống), GL, AP, AR, CB (tiền mặt-ngân hàng), FA, TAX, COST, BUD, PUR, SAL, INV, MFG, QC, PRJ, HR, PAY, CRM, SVC, và mã ngành (CTR hợp đồng, EST dự toán, SUB thầu phụ, EQP thiết bị, FWD giao nhận, TMS vận tải, WMS kho 3PL, DMS phân phối, POS...).
- `<CAT>` của NFR: PERF, AVAIL, SEC, AUDIT, DATA, USAB, COMP, INTG, MAINT, LEGAL, LOC.
- ID **không bao giờ dùng lại** sau khi xóa (ghi "Bị loại" thay vì xóa dòng). Giữ nguyên ID khi sửa nội dung.
- **Mã trong thư viện tham chiếu (`references/`) không phải ID dự án.** Các mã như `BR-PUR-04`, `PRM-PUR-004`, `RPT-AP-03`, `SOD-05`, `ROLE-SAL-MGR` trong file tham chiếu là mã minh họa của thư viện chuẩn. Khi đưa nội dung vào dự án: cấp ID mới theo đánh số của dự án (catalog dự án), giữ nguyên ý nghĩa, và ghi nguồn dạng `references/processes/p2p-procure-to-pay.md §7 (BR-PUR-04)`. Không chép mã thư viện làm ID dự án — `ba.py lint` sẽ báo lỗi nếu mã đó chưa được định nghĩa trong catalog dự án.

## 3. Nơi định nghĩa từng loại ID

Một ID được **định nghĩa** khi nó là ô đầu tiên của một dòng bảng, hoặc đứng đầu một tiêu đề (`#`…`######`), **trong file được chỉ định dưới đây**. Xuất hiện ở mọi nơi khác là **tham chiếu**. `ba.py lint` báo lỗi khi: một ID được định nghĩa 2 lần, hoặc được tham chiếu mà không được định nghĩa ở đâu.

| Loại ID | File định nghĩa |
|---|---|
| SRC, MTG | `00-inputs/source-register.md` (MTG còn có file biên bản riêng: tiêu đề `# MTG-NNN …`) |
| FEAT | `01-research/feature-catalog.md` |
| REQ | `02-requirements/requirement-register.md` |
| BO, BP | `02-requirements/requirements-overview.md` |
| Q, ASM, DEC, CFL, CHG | `02-requirements/issue-log.md` |
| MOD, BR-GEN, NFR-<CAT> | `03-specification/srs-overview.md` |
| ROLE, SOD | `03-specification/catalogs/roles-permissions.md` |
| MD | `03-specification/catalogs/master-data.md` |
| DOC | `03-specification/catalogs/document-types.md` |
| PRM | `03-specification/catalogs/system-parameters.md` |
| RPT | `03-specification/catalogs/reports.md` |
| INT, NTF | `03-specification/catalogs/integrations-notifications.md` |
| FN, FR, BR-<MOD>, US, AC, MSG, NFR-<MOD> | `03-specification/functions/**` (FN: tiêu đề `# FN-… — Tên` của file đặc tả) |
| VF | `04-verification/**` |
| RV | `05-review/**` |

Hệ quả thiết kế (chống mâu thuẫn): vai trò, tham số, danh mục, loại chứng từ, trạng thái chỉ được **định nghĩa một lần** trong catalog; file chức năng chỉ **tham chiếu** bằng ID và mô tả cách chức năng dùng chúng. Không định nghĩa lại tên/ý nghĩa ở file chức năng.

## 4. Marker bắt buộc

| Marker | Khi nào dùng | Quy tắc |
|---|---|---|
| `[CẦN XÁC NHẬN: Q-NNN]` | Thông tin cần cho đặc tả nhưng nguồn chưa có / mơ hồ | Q-NNN phải tồn tại trong issue-log. Không được đoán thay. Tài liệu còn marker này không được chuyển trạng thái `Ready`. |
| `[ĐỀ XUẤT → Q-NNN]` | Nội dung do BA/AI đề xuất (từ research, chuẩn ERP, kinh nghiệm) mà khách hàng **chưa** yêu cầu | Phải có Q-NNN hỏi khách hàng xác nhận. Khi KH đồng ý → thay bằng nguồn `DEC-NNN`. Khi KH từ chối → xóa nội dung, ghi DEC. Đây là cơ chế chống "thừa chức năng". |
| `[GIẢ ĐỊNH: ASM-NNN]` | Tạm thời làm việc theo một giả định có lý do | ASM ghi rõ rủi ro nếu sai và người phải xác nhận. |
| `N/A – <lý do>` | Một mục template không áp dụng | Bắt buộc có lý do. Không được xóa mục khỏi template. |
| `{{...}}` | Placeholder của template | Không được còn trong tài liệu nộp. |

Cấm trong tài liệu nộp: `TODO`, `TBD`, `???`, `xxx`, `...` đứng thay nội dung, "v.v." trong yêu cầu, "tương tự như trên" (phải viết rõ hoặc tham chiếu ID cụ thể).

## 5. Trạng thái tài liệu (frontmatter `status:`)

`Draft` → `In Review` → `Ready` → `Approved`

- `Draft`: đang viết.
- `In Review`: đang chạy bước 4/5.
- `Ready`: đã qua cổng chất lượng nội bộ (checklist PASS, lint/trace 0 lỗi, review 0 Critical/Major, 0 marker `[CẦN XÁC NHẬN]`/`[ĐỀ XUẤT]` còn mở) — dev có thể code.
- `Approved`: khách hàng/PO đã duyệt (ghi DEC + ngày).
- Mọi sửa đổi sau `Approved` phải qua CHG (xem skill `erp-ba-step3-specification` mục Quản lý thay đổi).

## 6. Bộ trạng thái chứng từ chuẩn & hành động phân quyền chuẩn

Trạng thái chứng từ (chỉ dùng các mã này trong `document-types.md`; mỗi loại chứng từ chọn tập con phù hợp):

| Mã | Nhãn | Ý nghĩa chuẩn |
|---|---|---|
| DRAFT | Nháp | Đang soạn, chưa ảnh hưởng dữ liệu nào; được xóa |
| PENDING | Chờ duyệt | Đã gửi duyệt; người tạo không sửa được (trừ khi thu hồi) |
| RETURNED | Trả lại để sửa | Người duyệt trả về; người tạo sửa và gửi lại |
| REJECTED | Từ chối | Kết thúc, không dùng tiếp; giữ lịch sử |
| APPROVED | Đã duyệt | Được phép thực hiện bước sau (tạo chứng từ tiếp theo) |
| IN_PROGRESS | Đang thực hiện | Đã có chứng từ sau liên kết, chưa xong |
| PARTIAL | Hoàn thành một phần | Đã thực hiện một phần số lượng/giá trị |
| COMPLETED | Hoàn thành | Đã thực hiện đủ |
| POSTED | Đã ghi sổ | Đã sinh bút toán / ảnh hưởng sổ (kho, công nợ, sổ cái); chỉ sửa bằng bỏ ghi sổ (nếu kỳ mở và được phép) hoặc đảo |
| CLOSED | Đã đóng | Đóng thủ công/tự động, phần còn lại không thực hiện nữa |
| CANCELLED | Đã hủy | Hủy trước khi ghi sổ; giữ lịch sử, không xóa |
| REVERSED | Đã đảo | Đã sinh bút toán đảo cho chứng từ đã ghi sổ |

Danh mục (master data) dùng **trạng thái bản ghi**, không dùng bộ trạng thái chứng từ: ACTIVE "Đang dùng", INACTIVE "Ngừng dùng" (không dùng cho giao dịch mới, giữ lịch sử), LOCKED "Khóa" (tạm chặn giao dịch, ví dụ nhà cung cấp đang tranh chấp). Danh mục đã phát sinh giao dịch không xóa — chuyển INACTIVE/LOCKED.

Hành động phân quyền chuẩn (dùng đúng tên này trong ma trận quyền): Xem, Tạo, Sửa, Xóa (chỉ chứng từ Nháp), Gửi duyệt, Thu hồi, Duyệt, Từ chối, Trả lại, Ghi sổ, Bỏ ghi sổ, Hủy, Đảo, Đóng, In, Xuất file, Nhập file, Cấu hình. Mỗi quyền đi kèm **phạm vi dữ liệu**: Của mình / Phòng ban / Chi nhánh / Công ty / Toàn hệ thống (hoặc theo kho/dự án).

## 7. Quy tắc viết yêu cầu

- Mỗi dòng FR/BR/NFR/AC là **một** yêu cầu kiểm thử được. Không gộp "và/hoặc" nhiều ý.
- Từ khóa chuẩn mực (viết HOA): **PHẢI** (bắt buộc), **KHÔNG ĐƯỢC** (cấm), **NÊN** (khuyến nghị, bỏ phải ghi lý do), **ĐƯỢC PHÉP** (tùy chọn). Không dùng "có thể" với nghĩa yêu cầu (mơ hồ giữa khả năng và cho phép).
- Chủ ngữ rõ: "Hệ thống PHẢI…", "Người dùng có vai trò ROLE-… ĐƯỢC PHÉP…".
- Cấm từ mơ hồ khi không kèm số đo/định nghĩa: nhanh, chậm, dễ dùng, thân thiện, linh hoạt, tối ưu, hợp lý, phù hợp, đầy đủ, v.v., tương tự, một số, nhiều, ít, thường, khi cần, nếu có thể, tự động (không nói điều kiện), real-time (không nói độ trễ). Danh sách đầy đủ: `references/ba-standards.md`.
- Mọi con số (ngưỡng, hạn mức, tỷ lệ, thời gian) phải có nguồn (REQ/DEC/luật) hoặc là tham số PRM có giá trị mặc định được KH xác nhận.
- Mỗi FR/BR có cột **Nguồn**: REQ-…, DEC-…, FEAT-… (kèm marker đề xuất), hoặc chuẩn/luật cụ thể (`references/processes/p2p-procure-to-pay.md §7`, `TT99/2025/TT-BTC Điều …`).

## 8. Định dạng số, ngày, tiền tệ (mặc định — dự án được ghi đè trong BR-GEN)

- Ngày: `dd/MM/yyyy`; ngày giờ: `dd/MM/yyyy HH:mm`; múi giờ Asia/Ho_Chi_Minh (UTC+7).
- Tiền VND: số nguyên, phân cách hàng nghìn bằng dấu chấm khi hiển thị; ngoại tệ: 2 chữ số thập phân.
- Số lượng: tối đa 3 chữ số thập phân (theo đơn vị tính); đơn giá: tối đa 4 (cấu hình được).
- Quy tắc làm tròn phải ghi rõ (làm tròn từng dòng rồi cộng, hay cộng rồi làm tròn) trong BR-GEN.

## 9. Sơ đồ

Dùng Mermaid trong khối ```` ```mermaid ````. Mỗi file chức năng bắt buộc có: (1) sơ đồ luồng nghiệp vụ swimlane, (2) sơ đồ quyết định (hình thoi), (3) sequence diagram, (4) state diagram nếu chức năng quản lý chứng từ có trạng thái, (5) ER diagram nếu chức năng có dữ liệu riêng. Mẫu và quy tắc cú pháp: `references/diagram-conventions.md`. `ba.py lint` kiểm tra cú pháp cơ bản.

## 10. Ngôn ngữ & thuật ngữ

- Viết tiếng Việt có dấu; thuật ngữ ERP chuẩn kèm tiếng Anh ở lần đầu: "Đơn mua hàng (Purchase Order – PO)".
- Thuật ngữ dùng thống nhất theo `03-specification/catalogs/glossary.md` của dự án (khởi tạo từ `references/glossary.md`). Một khái niệm = một tên. Nếu khách hàng dùng tên riêng (ví dụ "phiếu đề xuất vật tư" thay cho "đề nghị mua hàng"), dùng tên của khách hàng trong tài liệu và ghi ánh xạ sang tên chuẩn trong glossary.
