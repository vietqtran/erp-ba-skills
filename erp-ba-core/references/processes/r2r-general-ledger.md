# R2R — Kế toán tổng hợp (Record-to-Report / General Ledger)

> **Phạm vi:** Quy trình Record-to-Report (R2R) bao trùm phân hệ Kế toán tổng hợp (General Ledger – GL / Sổ cái): hệ thống tài khoản và các chiều phân tích, phiếu kế toán thủ công, bút toán định kỳ/phân bổ, định khoản tự động từ các phân hệ con (account determination), quản lý năm tài chính & kỳ, khóa kỳ theo phân hệ, kết chuyển cuối kỳ (→ 911 → 421), đánh giá lại tỷ giá, hợp nhất & nội bộ tập đoàn, số dư đầu kỳ & chuyển đổi dữ liệu, lập Báo cáo tài chính và ánh xạ chỉ tiêu ↔ tài khoản, đảo bút toán, dấu vết kiểm toán. **Module liên quan:** GL (trung tâm), nhận dữ liệu từ AP, AR, CB (tiền mặt/ngân hàng), INV, FA, PAY, COST, TAX. **Chuẩn tham chiếu:** SAP S/4HANA Finance (General Ledger), Oracle Fusion/EBS General Ledger, Odoo Accounting, Microsoft Dynamics 365 Finance [15][16][17][18]; chế độ kế toán doanh nghiệp Việt Nam: **Thông tư 99/2025/TT-BTC** (thay thế Thông tư 200/2014/TT-BTC từ 01/01/2026) [1][2], Thông tư 133/2016/TT-BTC cho doanh nghiệp nhỏ và vừa [11][12].

> **Cập nhật đến: 2026-10-20 — quy định thay đổi thường xuyên; BA phải kiểm tra lại hiệu lực khi dùng cho dự án.**

> **Chế độ kế toán đang có hiệu lực (xác định tại 2026-10-20):** Với doanh nghiệp nói chung áp dụng **Thông tư 99/2025/TT-BTC** (ban hành 27/10/2025, hiệu lực 01/01/2026, áp dụng cho năm tài chính bắt đầu từ hoặc sau 01/01/2026; thay thế TT200/2014/TT-BTC trừ các nội dung chuyển tiếp tại Điều khoản chuyển tiếp) [1][2][6]. TT200 chỉ còn áp dụng cho kỳ kế toán bắt đầu trước 01/01/2026 (ví dụ năm tài chính 01/4/2025–31/3/2026) [13]. Doanh nghiệp nhỏ và vừa được **chọn** TT133/2016/TT-BTC hoặc TT99/2025 [10][11]; doanh nghiệp siêu nhỏ: TT132/2018/TT-BTC (⚠️ **CHƯA XÁC MINH** mốc chuyển tiếp 30/6/2026 và **Thông tư 58/2026/TT-BTC** thay TT132 — chưa đối chiếu được văn bản gốc; TT58 không thay TT133) [11]. **Các số hiệu tài khoản dùng trong file này theo TT99/2025; khác biệt với TT133 được ghi chú.** Chi tiết chế độ, danh mục tài khoản đầy đủ: xem `references/regulations/vn-accounting.md`.

---

## Mục lục
1. [Mục đích & phạm vi](#1-mục-đích--phạm-vi-trongngoài-phạm-vi)
2. [Vai trò tham gia](#2-vai-trò-tham-gia)
3. [Danh mục (master data) tiên quyết](#3-danh-mục-master-data-tiên-quyết)
4. [Chứng từ & luồng chứng từ](#4-chứng-từ--luồng-chứng-từ-document-flow)
5. [Các bước quy trình chuẩn](#5-các-bước-quy-trình-chuẩn)
6. [Vòng đời trạng thái chứng từ chính](#6-vòng-đời-trạng-thái-chứng-từ-chính)
7. [Quy tắc nghiệp vụ & kiểm tra](#7-quy-tắc-nghiệp-vụ--kiểm-tra-validation-điển-hình)
8. [Hạch toán kế toán](#8-hạch-toán-kế-toán)
9. [Tham số hệ thống điển hình](#9-tham-số-hệ-thống-điển-hình)
10. [Kiểm soát nội bộ & phân quyền](#10-kiểm-soát-nội-bộ--phân-quyền-sod-hạn-mức-duyệt-audit)
11. [Báo cáo chuẩn](#11-báo-cáo-chuẩn)
12. [Tích hợp với module khác](#12-tích-hợp-với-module-khác-ảnh-hưởng-dữ-liệu-hai-chiều)
13. [Biến thể & ngoại lệ](#13-biến-thể--ngoại-lệ)
14. [Lỗi BA hay mắc & câu hỏi cần hỏi khách hàng](#14-lỗi-ba-hay-mắc--câu-hỏi-cần-hỏi-khách-hàng)
15. [Nguồn tham khảo](#15-nguồn-tham-khảo)

---

## 1. Mục đích & phạm vi (trong/ngoài phạm vi)

**Mục đích:** Ghi nhận, tổng hợp và báo cáo toàn bộ giao dịch tài chính của đơn vị trên một sổ cái thống nhất, bảo đảm nguyên tắc ghi sổ kép (double-entry), truy vết được (audit trail) và tạo ra Báo cáo tài chính (Financial Statements – FS) đúng chế độ kế toán, đúng hạn.

| Trong phạm vi (In scope) | Ngoài phạm vi (Out of scope) |
|---|---|
| Thiết lập & quản trị hệ thống tài khoản (Chart of Accounts – CoA) và các chiều phân tích (accounting dimensions) | Chi tiết nghiệp vụ mua hàng/bán hàng/kho → xem các file p2p, o2c, inventory-warehouse |
| Phiếu kế toán thủ công (Journal Voucher – JV / manual journal entry) | Lập hóa đơn, công nợ chi tiết AP/AR → `ap-accounts-payable.md`, `ar-accounts-receivable.md` |
| Bút toán định kỳ (recurring) & phân bổ (allocation/distribution) | Thu chi tiền, đối chiếu ngân hàng → `cash-bank.md` |
| Định khoản tự động từ phân hệ con (account determination / posting rules) | Khấu hao, tăng/giảm TSCĐ → `fixed-assets.md` |
| Quản lý năm tài chính, kỳ kế toán; khóa/mở kỳ theo phân hệ | Tính giá thành chi tiết → `costing.md` |
| Kết chuyển doanh thu/chi phí → 911 → 421; khóa sổ cuối kỳ | Khai & quyết toán thuế, hóa đơn điện tử → `tax-einvoice.md`, `references/regulations/vn-tax-einvoice.md` |
| Đánh giá lại tỷ giá cuối kỳ (FX revaluation) các khoản mục tiền tệ gốc ngoại tệ | Lập dự toán/ngân sách → `budgeting.md` |
| Số dư đầu kỳ, chuyển đổi dữ liệu (opening balances / data migration) | Lập BCTC hợp nhất đầy đủ (chỉ nêu nguyên tắc) → VAS 25, TT202/2014 ⚠️ |
| Lập Báo cáo tài chính & ánh xạ chỉ tiêu ↔ tài khoản; sổ sách kế toán | Phân tích quản trị chuyên sâu, KPI tài chính |
| Đảo bút toán (reversal), dấu vết kiểm toán, hợp nhất nội bộ cơ bản | Kế toán đơn vị hành chính sự nghiệp (khu vực công — áp dụng chế độ kế toán riêng) |

---

## 2. Vai trò tham gia

| Vai trò | Trách nhiệm | Quyền điển hình (hành động chuẩn) |
|---|---|---|
| Kế toán phần hành (Subledger/Staff Accountant) — AP, AR, CB, INV, FA, PAY | Nhập & ghi sổ chứng từ phân hệ; đối chiếu sổ phụ với sổ cái | Xem, Tạo, Sửa, Xóa (Nháp), Gửi duyệt, Ghi sổ (trong phạm vi phân hệ), In, Xuất file |
| Kế toán tổng hợp (General Ledger Accountant) | Phiếu kế toán thủ công; phân bổ, định kỳ; đánh giá lại tỷ giá; kết chuyển; lập BCTC nháp; đối chiếu tổng hợp | Xem, Tạo, Sửa, Xóa (Nháp), Gửi duyệt, Ghi sổ, Bỏ ghi sổ, Đảo, In, Xuất file, Nhập file |
| Kế toán trưởng (Chief Accountant) | Duyệt bút toán vượt hạn mức; soát xét & phê duyệt BCTC; khóa sổ kỳ/năm; quản trị CoA | Xem, Duyệt, Từ chối, Trả lại, Ghi sổ, Bỏ ghi sổ, Đảo, Đóng (khóa kỳ), Cấu hình (CoA, kết chuyển), In, Xuất file |
| Giám đốc tài chính (CFO) | Phê duyệt BCTC trước phát hành; kiểm soát bút toán trọng yếu | Xem, Duyệt, Từ chối, Xuất file |
| Giám đốc (Director) | Phê duyệt & ký BCTC phát hành ra bên ngoài | Xem, Duyệt, In, Xuất file |
| Kiểm toán nội bộ (Internal Audit) | Soát xét dấu vết, kiểm tra tuân thủ; không được sửa dữ liệu | Xem, Xuất file (chỉ đọc) |
| Quản trị hệ thống (System/Finance Admin) | Cấu hình tham số, quy tắc định khoản tự động, phân quyền | Cấu hình, Xem (không được Ghi sổ nghiệp vụ — tách biệt SoD) |

> **Lưu ý SoD:** người **Nhập** (Tạo) ≠ người **Duyệt** ≠ người **Khóa kỳ**. Quản trị hệ thống không được kiêm ghi sổ nghiệp vụ. Xem mục 10.

---

## 3. Danh mục (master data) tiên quyết

| Danh mục (VI / EN) | Trường quan trọng | Quy tắc chính |
|---|---|---|
| **Hệ thống tài khoản (Chart of Accounts – CoA)** `MD-COA` | Số hiệu TK, tên, loại (1–9 + loại 0 ngoài bảng), cấp (1/2/3…), TK cha, tính chất Nợ/Có, cho phép ghi sổ (postable) hay tổng hợp (header), theo dõi ngoại tệ, bắt buộc chiều phân tích | Theo Phụ lục II TT99/2025 [3][4]; chỉ ghi sổ vào TK chi tiết (lá), không ghi vào TK tổng hợp; không xóa TK đã phát sinh — chỉ ngừng hoạt động (deactivate). Doanh nghiệp được mở thêm TK chi tiết phục vụ quản trị nội bộ mà không cần xin phép [3] |
| **Chiều phân tích / đối tượng kế toán (Accounting dimensions / Analysis objects)** `MD-DIM` | Công ty (company), chi nhánh/đơn vị (branch/entity), phòng ban (department), trung tâm chi phí (cost center), công trình/dự án (project/job – "công trình"), hợp đồng (contract), đối tác (partner – KH/NCC), vật tư–hàng hóa (item), khoản mục chi phí (expense item), khoản mục LCTT (cash-flow item) | Tương đương financial dimensions (Dynamics), cost center/profit center/segment (SAP), CoA segments (Oracle), analytic accounts & analytic distribution (Odoo). Cấu hình "chiều nào bắt buộc theo nhóm TK nào" (xem PRM-GL-011) |
| **Năm tài chính & kỳ kế toán (Fiscal Year & Period)** `MD-PERIOD` | Năm tài chính (tháng bắt đầu), số kỳ/năm (12, có thể +1 kỳ điều chỉnh), ngày đầu/cuối kỳ, trạng thái kỳ (Mở/Đã đóng) theo từng phân hệ | Năm tài chính có thể khác năm dương lịch (ví dụ 01/4–31/3). Chốt bằng khóa kỳ (xem PRM-GL-005, mục 6) |
| **Loại tiền & tỷ giá (Currency & Exchange Rate)** `MD-CUR` | Đồng tiền hạch toán (functional – VND), ngoại tệ, loại tỷ giá (mua/bán/giao dịch/cuối kỳ), ngày áp dụng, ngân hàng tham chiếu | Đồng tiền ghi sổ & trình bày BCTC là VND. Tỷ giá đánh giá lại cuối kỳ dùng tỷ giá của ngân hàng thường giao dịch, áp dụng nhất quán [8][9] |
| **Loại chứng từ / Sổ nhật ký (Document type / Journal)** `MD-JRN` | Mã loại, tiền tố đánh số, dải số, quy tắc đánh số, phân hệ nguồn | Mỗi nguồn (phiếu kế toán, kết chuyển, phân bổ, auto-post AP/AR…) nên tách loại/sổ nhật ký để truy vết |
| **Quy tắc định khoản tự động (Posting rules / Account determination)** `MD-POST` | Nghiệp vụ nguồn → cặp TK Nợ/Có mặc định theo nhóm vật tư/khách hàng/kho/thuế | Account determination (SAP), default accounts trên sản phẩm/sổ nhật ký (Odoo). Quyết định tính đúng của bút toán tự động — phải được Kế toán trưởng duyệt cấu hình |
| **Mẫu bút toán định kỳ/phân bổ (Recurring/Allocation template)** `MD-RECUR` | Mẫu định khoản, chu kỳ, tiêu thức phân bổ (hệ số/doanh thu/diện tích…), ngày bắt đầu/kết thúc | Dùng cho trích trước, chờ phân bổ (242), phân bổ chi phí chung |
| **Ánh xạ chỉ tiêu BCTC ↔ tài khoản (FS line ↔ account mapping)** `MD-FSMAP` | Mã chỉ tiêu (mã số trên B01/B02/B03), công thức gộp TK/số dư Nợ–Có | Thay đổi theo mẫu TT99/2025 (B01-DN "Báo cáo tình hình tài chính"…) [5]. Phải rà lại khi đổi chế độ kế toán |

---

## 4. Chứng từ & luồng chứng từ (document flow)

| Chứng từ (VI / EN) | Mục đích | Tạo từ | Sinh ra | Ảnh hưởng (kho/công nợ/sổ cái) |
|---|---|---|---|---|
| Phiếu kế toán (Journal Voucher – JV / manual journal entry) | Ghi bút toán thủ công không thuộc phân hệ con (điều chỉnh, trích lập, phân loại lại) | Kế toán tổng hợp nhập tay | Bút toán sổ cái | Sổ cái (GL) |
| Bút toán tự động từ phân hệ (Auto-posting / subledger integration) | Chuyển bút toán từ AP/AR/CB/INV/FA/PAY vào sổ cái theo quy tắc định khoản | Hệ thống sinh khi ghi sổ chứng từ nguồn | Bút toán sổ cái | Công nợ, kho, tiền, sổ cái (hai chiều với sổ phụ) |
| Phiếu phân bổ (Allocation / Distribution voucher) | Phân bổ chi phí chung, chi phí chờ phân bổ (242) theo tiêu thức | Mẫu phân bổ `MD-RECUR` | Bút toán phân bổ | Sổ cái; chiều phân tích |
| Bút toán định kỳ (Recurring entry) | Lặp bút toán cố định theo kỳ (trích trước 335, phân bổ 242) | Mẫu định kỳ `MD-RECUR` | Bút toán sổ cái | Sổ cái |
| Bút toán đánh giá lại tỷ giá (FX revaluation entry) | Đánh giá lại khoản mục tiền tệ gốc ngoại tệ cuối kỳ | Chức năng đánh giá lại tỷ giá | Chênh lệch tỷ giá ghi thẳng 515/635 (TT99) | Sổ cái; 1112/1122/131/331/341 ngoại tệ |
| Phiếu kết chuyển (Closing entry voucher) | Kết chuyển doanh thu, chi phí → 911 → 421 cuối kỳ | Sơ đồ kết chuyển cấu hình sẵn | Bút toán kết chuyển | Sổ cái; đưa TK loại 5–9 về 0 |
| Chứng từ số dư đầu kỳ (Opening balance entry) | Nhập/chuyển số dư đầu kỳ khi go-live hoặc đầu năm | Chuyển đổi dữ liệu | Bút toán số dư đầu | Sổ cái; TK treo trung gian |
| Bút toán đảo (Reversal entry) | Đảo chứng từ sai đã ghi sổ (giữ dấu vết) | Chứng từ gốc đã ghi sổ | Bút toán ngược dấu | Sổ cái; tham chiếu chứng từ gốc |

```mermaid
flowchart LR
  SUB["Phân hệ nghiệp vụ (AP, AR, CB, INV, FA, PAY)"] -->|"Bút toán tự động"| GL["Sổ cái (General Ledger)"]
  JV["Phiếu kế toán thủ công (JV)"] -->|"Ghi sổ"| GL
  ALLOC["Phân bổ và bút toán định kỳ"] --> GL
  GL --> REVAL["Đánh giá lại tỷ giá cuối kỳ"]
  REVAL --> GL
  GL --> CLOSE["Bút toán kết chuyển 911 và 421"]
  CLOSE --> GL
  GL --> TB["Bảng cân đối số phát sinh (Trial Balance)"]
  TB --> FS["Báo cáo tài chính (Financial Statements)"]
```

---

## 5. Các bước quy trình chuẩn

Quy trình đóng sổ/lập báo cáo một kỳ (period-end close), từ số thứ tự thấp đến cao:

| # | Bước | Vai trò | Chứng từ | Hành động hệ thống | Trạng thái sau bước |
|---|---|---|---|---|---|
| 1 | Hoàn tất ghi sổ các phân hệ con | Kế toán phần hành | Chứng từ AP/AR/CB/INV/FA/PAY | Đẩy bút toán tự động vào sổ cái theo `MD-POST` | Phân hệ đã POSTED |
| 2 | Khóa kỳ các phân hệ nghiệp vụ (ngừng nhận chứng từ nghiệp vụ) | Kế toán trưởng | — | Đóng kỳ theo phân hệ (chỉ còn GL mở) | Kỳ phân hệ = CLOSED |
| 3 | Nhập phiếu kế toán điều chỉnh/phân loại lại | Kế toán tổng hợp | Phiếu kế toán (JV) | Kiểm tra cân Nợ=Có, kỳ mở, chiều phân tích | JV = POSTED |
| 4 | Chạy phân bổ & bút toán định kỳ (242, 335, chi phí chung) | Kế toán tổng hợp | Phiếu phân bổ / định kỳ | Sinh bút toán từ mẫu `MD-RECUR` | Đã phân bổ |
| 5 | Đánh giá lại tỷ giá khoản mục tiền tệ gốc ngoại tệ | Kế toán tổng hợp | Bút toán đánh giá lại tỷ giá | Tính chênh lệch theo tỷ giá cuối kỳ, ghi thẳng 515/635 (TT99) | Đã đánh giá lại |
| 6 | Đối chiếu sổ phụ ↔ sổ cái (131, 331, 112, 156, 211/214…) | Kế toán tổng hợp | Bảng đối chiếu | So khớp số dư phân hệ với GL | Đã đối chiếu |
| 7 | Kết chuyển giảm trừ doanh thu, doanh thu/chi phí → 911; kết chuyển lãi/lỗ → 4212 | Kế toán tổng hợp | Phiếu kết chuyển | Sinh bút toán theo sơ đồ kết chuyển | TK 5–8 về 0; 911 → 421 |
| 8 | Kết xuất BCTC nháp; soát xét hợp lý | Kế toán tổng hợp → Kế toán trưởng | BCTC nháp (B01/B02/B03/B09) | Gộp số liệu theo `MD-FSMAP` | BCTC nháp |
| 9 | Phê duyệt BCTC | Kế toán trưởng → CFO/Giám đốc | BCTC | Ghi nhận phê duyệt | BCTC APPROVED |
| 10 | Khóa sổ kỳ/năm (GL) | Kế toán trưởng | — | Khóa kỳ GL; chuyển số dư sang kỳ sau (carry-forward) | Kỳ = CLOSED |
| 11 | (Cuối năm) Chuyển số dư sang năm sau; mở số dư đầu kỳ năm mới | Kế toán tổng hợp | Chứng từ số dư đầu kỳ | Carry-forward balances; 4212 → 4211 | Năm = CLOSED, năm mới mở |

```mermaid
flowchart TD
  subgraph PH["Kế toán phần hành"]
    A["Hoàn tất ghi sổ các phân hệ con"]
  end
  subgraph TH["Kế toán tổng hợp"]
    B["Nhập phiếu kế toán điều chỉnh"]
    C["Chạy phân bổ và bút toán định kỳ"]
    D["Đánh giá lại tỷ giá cuối kỳ"]
    E["Đối chiếu sổ phụ với sổ cái"]
    F["Kết chuyển doanh thu chi phí sang 911"]
    G["Kết xuất BCTC nháp"]
  end
  subgraph KTT["Kế toán trưởng"]
    H{"BCTC hợp lý?"}
    I["Khóa sổ kỳ và chuyển số dư"]
  end
  A --> B --> C --> D --> E --> F --> G --> H
  H -->|"Chưa đạt"| B
  H -->|"Đạt"| I
```

---

## 6. Vòng đời trạng thái chứng từ chính

Áp dụng cho **Phiếu kế toán (Journal Voucher)** và các bút toán GL. Bút toán tự động từ phân hệ thường vào thẳng trạng thái POSTED theo chứng từ nguồn.

```mermaid
stateDiagram-v2
  state "Nháp" as DRAFT
  state "Chờ duyệt" as PENDING
  state "Đã duyệt" as APPROVED
  state "Trả lại để sửa" as RETURNED
  state "Đã ghi sổ" as POSTED
  state "Đã đảo" as REVERSED
  state "Đã hủy" as CANCELLED
  [*] --> DRAFT
  DRAFT --> PENDING: Gửi duyệt
  DRAFT --> CANCELLED: Hủy
  PENDING --> APPROVED: Duyệt
  PENDING --> RETURNED: Trả lại
  RETURNED --> DRAFT: Sửa
  APPROVED --> POSTED: Ghi sổ
  POSTED --> DRAFT: Bỏ ghi sổ
  POSTED --> REVERSED: Đảo
  REVERSED --> [*]
  CANCELLED --> [*]
```

| Từ | Hành động | Đến | Vai trò | Điều kiện |
|---|---|---|---|---|
| DRAFT | Gửi duyệt | PENDING | Kế toán tổng hợp | Cân Nợ=Có; kỳ mở; đủ chiều phân tích bắt buộc |
| DRAFT | Hủy | CANCELLED | Người tạo | Chỉ khi còn Nháp |
| PENDING | Duyệt | APPROVED | Kế toán trưởng | Đúng hạn mức duyệt (PRM) |
| PENDING | Trả lại | RETURNED | Kế toán trưởng | Có lý do trả lại |
| RETURNED | Sửa | DRAFT | Người tạo | — |
| APPROVED | Ghi sổ | POSTED | Kế toán tổng hợp / trưởng | Kỳ còn mở; tỷ giá tồn tại nếu có ngoại tệ |
| POSTED | Bỏ ghi sổ | DRAFT | Kế toán trưởng | Kỳ chưa khóa; chưa dùng cho BCTC đã phát hành |
| POSTED | Đảo | REVERSED | Kế toán trưởng | Dùng khi kỳ gốc đã khóa; sinh bút toán ngược, giữ dấu vết |

> **Nguyên tắc vàng:** sau khi POSTED **không được Xóa**; sửa sai bằng **Bỏ ghi sổ** (nếu kỳ chưa khóa) hoặc **Đảo** (nếu kỳ đã khóa). Đây là yêu cầu dấu vết kiểm toán (audit trail).

---

## 7. Quy tắc nghiệp vụ & kiểm tra (validation) điển hình

1. **BR-GL-01 — Cân bằng ghi sổ kép:** mọi bút toán phải có `Σ Nợ = Σ Có` (theo đồng tiền hạch toán VND). *Lý do:* nguyên tắc kế toán kép; nếu lệch do làm tròn ngoại tệ, chênh lệch đưa vào TK chênh lệch tỷ giá (635/515) hoặc TK làm tròn cấu hình sẵn.
2. **BR-GL-02 — Chỉ ghi vào TK chi tiết (postable):** cấm ghi sổ vào TK tổng hợp/TK cha. *Lý do:* bảo toàn cấu trúc tổng hợp của sổ cái và BCTC.
3. **BR-GL-03 — Ngày chứng từ thuộc kỳ đang mở:** ngày hạch toán phải nằm trong kỳ chưa khóa của phân hệ tương ứng. *Lý do:* không làm sai lệch số liệu kỳ đã chốt/đã nộp BCTC.
4. **BR-GL-04 — Chiều phân tích bắt buộc theo nhóm TK:** ví dụ TK chi phí 641/642/627 bắt buộc có trung tâm chi phí/phòng ban; TK 154 trong doanh nghiệp xây lắp bắt buộc có "công trình"; TK 131/331 bắt buộc có đối tác. *Lý do:* phục vụ báo cáo quản trị và đối chiếu công nợ/giá thành.
5. **BR-GL-05 — Tồn tại tỷ giá:** bút toán có ngoại tệ phải có tỷ giá hợp lệ tại ngày chứng từ; nếu không → chặn ghi sổ. *Lý do:* quy đổi VND chính xác.
6. **BR-GL-06 — Số dư đầu kỳ cân:** khi nhập số dư đầu kỳ, `Σ dư Nợ đầu kỳ = Σ dư Có đầu kỳ`; chênh lệch treo ở TK trung gian phải xử lý về 0 trước go-live. *Lý do:* tránh mất cân đối ngay từ đầu.
7. **BR-GL-07 — Đối chiếu sổ phụ ↔ sổ cái:** số dư/tổng phát sinh của TK có sổ phụ (131, 331, 112, 156, 211/214) phải khớp giữa phân hệ con và GL trước khi khóa kỳ. *Lý do:* phát hiện bút toán lệch, trùng, thiếu.
8. **BR-GL-08 — Duyệt trước ghi sổ theo hạn mức:** bút toán vượt hạn mức giá trị cấu hình phải được Kế toán trưởng duyệt. *Lý do:* kiểm soát bút toán trọng yếu (xem mục 10).
9. **BR-GL-09 — Không sửa/xóa sau ghi sổ:** chỉ Bỏ ghi sổ (kỳ mở) hoặc Đảo (kỳ khóa). *Lý do:* dấu vết kiểm toán, không được "ghi đè lịch sử".
10. **BR-GL-10 — Khóa kỳ chặn ghi:** khi kỳ đã khóa, mọi hành động Tạo/Sửa/Ghi sổ vào kỳ đó bị chặn; chỉ bút toán điều chỉnh kỳ sau hoặc kỳ điều chỉnh (13) nếu được bật. *Lý do:* bảo toàn số liệu đã chốt.
11. **BR-GL-11 — Đánh số chứng từ liên tục, không trùng, không nhảy cách:** theo loại chứng từ/sổ nhật ký. *Lý do:* yêu cầu pháp lý về sổ kế toán & truy vết.

**Công thức xác định kết quả kinh doanh (dùng khi kiểm tra BCTC và kết chuyển):**
- Doanh thu thuần = Doanh thu bán hàng (511) − Các khoản giảm trừ doanh thu (521)
- Lợi nhuận gộp = Doanh thu thuần − Giá vốn hàng bán (632)
- Lợi nhuận thuần từ HĐKD = Lợi nhuận gộp + (Doanh thu tài chính 515 − Chi phí tài chính 635) − Chi phí bán hàng (641) − Chi phí QLDN (642)
- Tổng lợi nhuận kế toán trước thuế = Lợi nhuận thuần HĐKD + (Thu nhập khác 711 − Chi phí khác 811)
- Lợi nhuận sau thuế TNDN = Lợi nhuận trước thuế − Chi phí thuế TNDN (821)
- Chênh lệch đánh giá lại tỷ giá = (Tỷ giá cuối kỳ − Tỷ giá ghi sổ) × Số dư gốc ngoại tệ của khoản mục tiền tệ

---

## 8. Hạch toán kế toán

> **Chế độ áp dụng: Thông tư 99/2025/TT-BTC** (số hiệu TK dưới đây đã đối chiếu: 111, 112, 131, 133, 331, 333/3331, 154, 155, 156, 242, 335, 413, 421, 511, 515, 521, 632, 635, 641, 642, 711, 811, 821, 911 — **giữ nguyên số hiệu so với TT200**; 112 đổi tên thành "Tiền gửi không kỳ hạn", 242 thành "Chi phí chờ phân bổ", 155 thành "Sản phẩm") [3][4]. **Khác biệt TT133:** gộp chi phí bán hàng + QLDN vào **642 – Chi phí quản lý kinh doanh** (6421 bán hàng, 6422 QLDN); vẫn dùng 911, 421 — xem `references/regulations/vn-accounting.md`.

**8.1 Kết chuyển cuối kỳ (closing entries → 911 → 421):**

| Nghiệp vụ | Nợ | Có | Ghi chú |
|---|---|---|---|
| Kết chuyển các khoản giảm trừ doanh thu | 511 | 521 | Trước khi xác định doanh thu thuần |
| Kết chuyển doanh thu thuần bán hàng & cung cấp DV | 511 | 911 | |
| Kết chuyển doanh thu hoạt động tài chính | 515 | 911 | |
| Kết chuyển thu nhập khác | 711 | 911 | |
| Kết chuyển giá vốn hàng bán | 911 | 632 | |
| Kết chuyển chi phí tài chính | 911 | 635 | |
| Kết chuyển chi phí bán hàng | 911 | 641 | TT133: dùng 6421 |
| Kết chuyển chi phí quản lý doanh nghiệp | 911 | 642 | TT133: dùng 6422 |
| Kết chuyển chi phí khác | 911 | 811 | |
| Kết chuyển chi phí thuế TNDN hiện hành (và hoãn lại nếu có) | 911 | 821 | 8211/8212 |
| Kết chuyển lãi sau thuế (nếu lãi) | 911 | 4212 | 4212 = LNST chưa phân phối năm nay |
| Kết chuyển lỗ (nếu lỗ) | 4212 | 911 | |
| Đầu năm sau: chuyển kết quả năm nay sang năm trước | 4212 | 4211 | 4211 "LNST chưa phân phối lũy kế đến cuối năm trước" [3] |

**8.2 Đánh giá lại tỷ giá cuối kỳ (FX revaluation) — TT99 ghi thẳng vào 515/635, không qua 413 [9][14]:**

> **Thay đổi quan trọng so với TT200:** Theo TT99/2025, chênh lệch do **đánh giá lại khoản mục tiền tệ gốc ngoại tệ cuối kỳ** được ghi **trực tiếp** vào doanh thu tài chính (515 – lãi) hoặc chi phí tài chính (635 – lỗ), **không** tập hợp trung gian qua TK 413 như TT200 [9][14]. TK 413 "Chênh lệch tỷ giá hối đoái" vẫn còn nhưng **chỉ dùng cho trường hợp đặc thù**: DN do Nhà nước sở hữu 100% vốn thực hiện dự án trọng điểm quốc gia được treo lại chênh lệch tỷ giá giai đoạn trước hoạt động, khi đi vào hoạt động mới kết chuyển 413 → 515/635 [9].

| Nghiệp vụ | Nợ | Có | Ghi chú |
|---|---|---|---|
| Đánh giá lại cuối kỳ — lãi tỷ giá do tài sản tiền tệ tăng | 1112, 1122, 131, 1288, … | 515 | Ghi thẳng doanh thu tài chính (TT99); tỷ giá cuối kỳ của NH tham chiếu |
| Đánh giá lại cuối kỳ — lãi tỷ giá do nợ phải trả ngoại tệ giảm | 331, 341, … | 515 | |
| Đánh giá lại cuối kỳ — lỗ tỷ giá do tài sản tiền tệ giảm | 635 | 1112, 1122, 131, 1288, … | Ghi thẳng chi phí tài chính (TT99) |
| Đánh giá lại cuối kỳ — lỗ tỷ giá do nợ phải trả ngoại tệ tăng | 635 | 331, 341, … | |

> **Nguyên tắc tỷ giá & lưu ý TT200:** cuối kỳ đánh giá lại theo tỷ giá chuyển khoản của NH thương mại nơi DN thường giao dịch; theo thông lệ tài sản tiền tệ dùng **tỷ giá mua**, nợ phải trả tiền tệ dùng **tỷ giá bán** — BA đối chiếu quy định tỷ giá cụ thể trong Phụ lục II TT99 cho dự án [8][9]. **Khác biệt TT200:** TT200 tập hợp chênh lệch đánh giá lại cuối năm qua TK 413 (4131) rồi mới kết chuyển thuần vào 515/635; DN còn áp dụng TT200 (kỳ bắt đầu trước 01/01/2026) vẫn dùng cách cũ. Chênh lệch tỷ giá **đã thực hiện** khi thanh toán/thu hồi trong kỳ: ghi 515/635 (cả hai chế độ).

**8.3 Phân bổ & trích trước (allocation / accrual):**

| Nghiệp vụ | Nợ | Có | Ghi chú |
|---|---|---|---|
| Phân bổ chi phí chờ phân bổ định kỳ | 627, 641, 642 | 242 | Theo số kỳ phân bổ (242 đổi tên "Chi phí chờ phân bổ") |
| Trích trước chi phí phải trả | 627, 641, 642 | 335 | Trích trước theo ước tính |
| Phân bổ chi phí chung cho các đối tượng (chiều phân tích) | TK đích theo đối tượng | TK nguồn | Theo tiêu thức `MD-RECUR` |

**8.4 Số dư đầu kỳ / chuyển đổi dữ liệu (opening balance / migration):**

| Nghiệp vụ | Nợ | Có | Ghi chú |
|---|---|---|---|
| Nhập số dư Nợ đầu kỳ của TK | TK có số dư Nợ | TK treo đầu kỳ (OBE) | TK treo là TK kỹ thuật tự định nghĩa (Opening Balance Equity), không thuộc hệ thống TK chuẩn |
| Nhập số dư Có đầu kỳ của TK | TK treo đầu kỳ (OBE) | TK có số dư Có | TK treo phải về 0 sau khi nhập đủ; nhiều hệ thống nạp thẳng số dư đầu kỳ không qua bút toán |

**8.5 Đảo bút toán (reversal):** sinh bút toán ngược dấu của chứng từ gốc (đổi Nợ↔Có hoặc ghi số âm theo PRM-GL-013), tham chiếu số chứng từ gốc; không xóa chứng từ gốc.

---

## 9. Tham số hệ thống điển hình

| Tham số | Kiểu | Giá trị gợi ý | Phạm vi | Ảnh hưởng |
|---|---|---|---|---|
| `PRM-GL-001` Tháng bắt đầu năm tài chính | Chọn | Tháng 1 | Công ty | Xác định năm tài chính; cho phép năm ≠ dương lịch |
| `PRM-GL-002` Số kỳ kế toán/năm | Số | 12 (+1 kỳ điều chỉnh) | Công ty | Có kỳ 13 để ghi bút toán điều chỉnh sau khóa tháng 12 |
| `PRM-GL-003` Chế độ kế toán áp dụng | Chọn | TT99/2025 (hoặc TT133, TT132/TT58) | Công ty | Bộ CoA, mẫu sổ, mẫu BCTC, sơ đồ kết chuyển |
| `PRM-GL-004` Hình thức sổ kế toán | Chọn | Nhật ký chung | Công ty | Bộ sổ in ra (S03a/S03b…) |
| `PRM-GL-005` Cho phép ghi vào kỳ đã khóa | Luận lý | Không | Hệ thống | Chặn ghi sổ lùi kỳ |
| `PRM-GL-006` Bắt buộc cân Nợ=Có trước ghi sổ | Luận lý | Có | Hệ thống | Chặn bút toán lệch |
| `PRM-GL-007` Đồng tiền hạch toán & làm tròn | Chọn/Số | VND, làm tròn 0 đồng | Công ty | Quy đổi, làm tròn ngoại tệ |
| `PRM-GL-008` Ngân hàng tham chiếu tỷ giá | Chọn | NH thường giao dịch | Công ty | Tỷ giá đánh giá lại cuối kỳ |
| `PRM-GL-009` Phương pháp áp tỷ giá ghi sổ khi xuất ngoại tệ | Chọn | Bình quân gia quyền / FIFO / đích danh | Công ty | Giá trị quy đổi khi giảm số dư ngoại tệ [8] |
| `PRM-GL-010` Cho phép Bỏ ghi sổ (Unpost) | Luận lý | Có (kỳ mở) | Công ty | Cho phép sửa bút toán khi kỳ chưa khóa |
| `PRM-GL-011` Chiều phân tích bắt buộc theo nhóm TK | Bảng cấu hình | 627/641/642→cost center; 154→công trình; 131/331→đối tác | Công ty/Chi nhánh | Chất lượng dữ liệu báo cáo quản trị |
| `PRM-GL-012` TK treo số dư đầu kỳ / chênh lệch | Chọn | TK OBE/clearing tự định nghĩa | Công ty | Chuyển đổi dữ liệu |
| `PRM-GL-013` Phương pháp đảo | Chọn | Đối ứng Nợ↔Có / ghi số âm | Hệ thống | Cách thể hiện bút toán đảo |
| `PRM-GL-014` Quy tắc đánh số chứng từ | Chuỗi | Tiền tố + năm + số tự tăng | Công ty/Chi nhánh | Liên tục, không trùng |
| `PRM-GL-015` Sơ đồ kết chuyển tự động cuối kỳ | Bảng cấu hình | 511/515/711→911; 632/635/641/642/811/821→911; 911→4212 | Công ty | Tự động hóa khóa sổ |
| `PRM-GL-016` Hạn mức duyệt bút toán theo giá trị | Số/Bảng | Theo chính sách | Công ty | Định tuyến phê duyệt |

---

## 10. Kiểm soát nội bộ & phân quyền (SoD, hạn mức duyệt, audit)

1. **Tách biệt chức năng (Segregation of Duties – SoD):** người **Tạo** phiếu kế toán ≠ người **Duyệt** ≠ người **Khóa kỳ**. Quản trị hệ thống (cấu hình CoA, quy tắc định khoản) **không** được kiêm ghi sổ nghiệp vụ.
2. **Maker–Checker:** bút toán điều chỉnh/trọng yếu phải qua luồng Gửi duyệt → Duyệt trước khi Ghi sổ; hạn mức duyệt theo giá trị (`PRM-GL-016`) định tuyến lên Kế toán trưởng/CFO.
3. **Khóa kỳ theo phân hệ (period lock per module):** mỗi phân hệ (AP, AR, CB, INV, FA, GL) có trạng thái kỳ riêng; nghiệp vụ đóng trước, GL đóng sau cùng. Khóa kỳ chặn Tạo/Sửa/Ghi sổ/Bỏ ghi sổ vào kỳ đó.
4. **Cấm xóa sau ghi sổ — chỉ Đảo/Bỏ ghi sổ:** mọi thay đổi để lại dấu vết (ai, khi nào, giá trị trước–sau). Bút toán đảo tham chiếu chứng từ gốc.
5. **Audit trail bắt buộc:** log tạo/sửa/duyệt/ghi sổ/đảo/khóa kỳ; nhật ký đăng nhập; không cho sửa log. Phục vụ kiểm toán nội bộ & độc lập.
6. **Kiểm soát sửa master data trọng yếu:** thêm/sửa TK trong CoA, quy tắc định khoản tự động, sơ đồ kết chuyển, chiều phân tích bắt buộc — phải được Kế toán trưởng phê duyệt; ghi log thay đổi.
7. **Đối chiếu định kỳ (reconciliation):** sổ phụ ↔ sổ cái (131, 331, 112, 156, 211/214); tiền gửi ↔ sao kê ngân hàng; thuế 133/3331 ↔ tờ khai. Đối chiếu trước khi khóa kỳ (BR-GL-07).
8. **Kiểm soát truy cập theo công ty/chi nhánh:** mỗi người dùng chỉ thấy đơn vị được phân quyền; bút toán liên công ty cần vai trò liên đơn vị.

> Nguyên tắc & tham số chung về phân quyền, audit, hạn mức: xem `references/security-and-parameters.md` và `references/design-patterns.md`.

---

## 11. Báo cáo chuẩn

| Báo cáo (VI / EN) | Mục đích | Chiều phân tích / bộ lọc | Bắt buộc theo luật? |
|---|---|---|---|
| Sổ Nhật ký chung (General Journal, mẫu S03a-DN) | Ghi nhận trình tự thời gian mọi bút toán | Kỳ, loại chứng từ, tài khoản | Có — sổ kế toán tổng hợp bắt buộc [7] |
| Sổ Cái (General Ledger, S03b-DN) | Theo dõi phát sinh & số dư từng tài khoản | Tài khoản, kỳ, đối tượng | Có [7] |
| Sổ chi tiết tài khoản (Account detail ledger) | Chi tiết phát sinh theo đối tượng/chiều của một TK | TK, đối tượng (131/331/công trình…) | Có (với TK cần theo dõi chi tiết) [7] |
| Bảng cân đối số phát sinh (Trial Balance, S06-DN) | Kiểm tra tổng dư đầu – phát sinh – dư cuối toàn bộ TK | Kỳ, cấp TK | Có [7] |
| Báo cáo tình hình tài chính (Statement of Financial Position, B01-DN) | Tài sản – nợ phải trả – vốn chủ sở hữu tại thời điểm | Công ty/hợp nhất | Có — thay tên "Bảng cân đối kế toán" theo TT99 [5] |
| Báo cáo kết quả hoạt động kinh doanh (Income Statement, B02-DN) | Doanh thu – chi phí – lợi nhuận trong kỳ | Kỳ, đơn vị | Có [5] |
| Báo cáo lưu chuyển tiền tệ (Cash Flow Statement, B03-DN) | Dòng tiền HĐKD/đầu tư/tài chính | Kỳ | Có [5] |
| Bản thuyết minh BCTC (Notes to FS, B09-DN) | Thuyết minh chính sách & số liệu | Kỳ | Có [5] |
| Sổ nhật ký thu/chi tiền, mua/bán hàng (S03a1–S03a4-DN) | Nhật ký chuyên dùng theo hình thức Nhật ký chung | Kỳ | Có điều kiện (theo hình thức sổ) [7] |
| Bảng tổng hợp phát sinh theo đối tượng/chiều phân tích | Quản trị: chi phí theo phòng ban/công trình/dự án | Đối tượng, kỳ | Không (quản trị) |

> **Lưu ý TT99/2025:** Hệ thống BCTC quy định tại **Điều 17** TT99 [5]. BCTC năm cho DN đáp ứng giả định hoạt động liên tục gồm B01/B02/B03/B09-DN; DN không đáp ứng dùng mẫu hậu tố **DNKLT** (B01-DNKLT…); có mẫu giữa niên độ đầy đủ (B01a…) và tóm lược (B01b…) [5]. **Thời hạn nộp BCTC năm: chậm nhất 90 ngày** kể từ ngày kết thúc năm tài chính [6] (mốc 90 ngày là thông lệ ổn định theo Luật Kế toán; số điều cụ thể trong TT99 chưa đối chiếu được do nguồn gốc trả HTTP 403). Biểu mẫu kèm theo TT99: hệ thống tài khoản – Phụ lục II; sổ kế toán – **Phụ lục III** (đã xác nhận [7]); biểu mẫu BCTC – kèm quy định tại Điều 17 ⚠️ số phụ lục chưa đối chiếu được với văn bản gốc [5][7].

---

## 12. Tích hợp với module khác (ảnh hưởng dữ liệu hai chiều)

| Module | Dữ liệu vào GL | Dữ liệu GL cung cấp lại | TK liên quan | File tham chiếu |
|---|---|---|---|---|
| AP – Phải trả (Accounts Payable) | Hóa đơn mua, thanh toán NCC → bút toán 331 | Số dư 331, đối chiếu công nợ | 331, 133, 331x | `ap-accounts-payable.md` |
| AR – Phải thu (Accounts Receivable) | Hóa đơn bán, thu tiền KH → 131, 511, 3331 | Số dư 131 | 131, 511, 3331 | `ar-accounts-receivable.md` |
| CB – Tiền mặt/Ngân hàng (Cash & Bank) | Phiếu thu/chi, UNC → 111, 112 | Số dư tiền, đối chiếu sao kê | 111, 112 | `cash-bank.md` |
| INV – Kho (Inventory) | Nhập/xuất kho, giá vốn → 152/155/156, 632 | Giá trị tồn, đối chiếu kho ↔ sổ cái | 152, 155, 156, 632 | `inventory-warehouse.md` |
| FA – Tài sản cố định (Fixed Assets) | Tăng/giảm TS, khấu hao → 211, 214, 627/641/642 | Nguyên giá, hao mòn lũy kế | 211, 213, 214, 242 | `fixed-assets.md` |
| PAY – Tiền lương (Payroll) | Lương, BHXH, thuế TNCN → 334, 338, 3335 | Chi phí nhân công theo đối tượng | 334, 338, 622/627/641/642 | `hr-payroll.md` |
| COST – Giá thành (Costing) | Tập hợp & phân bổ chi phí sản xuất, giá thành → 154 | Số dư dở dang, giá thành | 621, 622, 627, 154 ⚠️ (TK 611/631 cho kiểm kê định kỳ đã bỏ ở TT99) [3][4] | `costing.md` |
| TAX – Thuế & hóa đơn (Tax & e-Invoice) | Thuế GTGT, TNDN → 133, 333, 821 | Số liệu quyết toán | 133, 3331, 3334, 333, 821 | `tax-einvoice.md`, `references/regulations/vn-tax-einvoice.md` |
| BUD – Ngân sách (Budgeting) | — | Số thực hiện để so dự toán | theo chiều phân tích | `budgeting.md` |

> Quan hệ GL ↔ sổ phụ là **hai chiều**: phân hệ con đẩy bút toán lên GL; GL là nguồn số dư để đối chiếu ngược (BR-GL-07). Tài khoản có sổ phụ (131, 331, 211/214, 156…) chỉ nên ghi qua phân hệ con, hạn chế ghi tay trực tiếp ở GL để tránh lệch.

---

## 13. Biến thể & ngoại lệ

1. **Đa tiền tệ (multi-currency):** mỗi bút toán lưu đồng thời ngoại tệ gốc và VND quy đổi; đánh giá lại cuối kỳ (mục 8.2). Theo dõi số dư ngoại tệ gốc trên TK 1112/1122/131/331/341.
2. **Kỳ điều chỉnh (adjustment period / kỳ 13):** bút toán điều chỉnh/kiểm toán sau khi đã khóa tháng 12 nhưng trước phát hành BCTC → ghi vào kỳ 13 nếu `PRM-GL-002` bật.
3. **Sửa sau duyệt/ghi sổ:** nếu kỳ chưa khóa → Bỏ ghi sổ (Unpost) → Sửa → Ghi sổ lại; nếu kỳ đã khóa → Đảo (Reverse) ở kỳ mở rồi nhập lại. Không bao giờ xóa.
4. **Hủy chứng từ đã ghi sổ:** không xóa — tạo bút toán đảo (REVERSED), nêu lý do, giữ tham chiếu.
5. **Kết chuyển lỗ:** nếu 911 ra lỗ → Nợ 4212 / Có 911; theo dõi lỗ lũy kế để chuyển lỗ tính thuế TNDN (xem `references/regulations/vn-tax-einvoice.md`).
6. **Nội bộ & hợp nhất tập đoàn (intercompany & consolidation):** giao dịch liên công ty dùng TK phải thu/phải trả nội bộ (136/336) và bút toán đối ứng giữa hai đơn vị; khi hợp nhất phải **loại trừ** (elimination) công nợ, doanh thu–giá vốn nội bộ, lãi/lỗ chưa thực hiện. BCTC hợp nhất theo VAS 25 và Thông tư 202/2014/TT-BTC ⚠️ **CHƯA XÁC MINH hiệu lực sau khi TT99 ban hành — cần kiểm tra lại**. Công cụ: SAP Group Reporting, Oracle FCCS, Odoo consolidation [15][16].
7. **Đổi chế độ kế toán tại 01/01/2026 (TT200 → TT99):** ánh xạ lại CoA (TK bị bỏ 611/631/161/441/461/466/417; TK thêm 215/332 và một số TK khác; TK đổi tên 112/155/158/242/244/419…; danh mục đầy đủ xem `references/regulations/vn-accounting.md`) [3][4]; rà lại `MD-FSMAP`, sơ đồ kết chuyển, mẫu sổ & BCTC. Số dư đầu 01/01/2026 chuyển theo bảng ánh xạ.
8. **Năm tài chính khác năm dương lịch:** DN có năm tài chính 01/4–31/3… vẫn áp dụng TT200 cho kỳ bắt đầu trước 01/01/2026, chuyển TT99 từ năm tài chính bắt đầu ≥ 01/01/2026 [13].
9. **DN không hoạt động liên tục (DNKLT):** dùng bộ mẫu BCTC hậu tố DNKLT, nguyên tắc đánh giá tài sản/nợ khác (giá có thể thu hồi) [5].
10. **DN nhỏ và vừa (TT133 hoặc được chọn TT99) / siêu nhỏ (TT132; ⚠️ TT58/2026 chưa xác minh):** bộ TK, sổ, BCTC khác; SME khi đã chọn một chế độ phải áp dụng nhất quán tối thiểu một năm kế toán, nếu đổi chế độ phải trình bày lại số liệu so sánh và thuyết minh lý do [10]; cấu hình `PRM-GL-003` phù hợp — xem `references/regulations/vn-accounting.md` [10][11].

---

## 14. Lỗi BA hay mắc & câu hỏi cần hỏi khách hàng

**Lỗi thường gặp (tránh drift & thiếu/thừa chức năng):**
- Dùng số hiệu/tên tài khoản theo **TT200 cũ** cho dự án go-live ≥ 2026 (phải dùng TT99: "Báo cáo tình hình tài chính" chứ không phải "Bảng cân đối kế toán"; 242 "Chi phí chờ phân bổ"; bỏ 611/631) [1][3][5].
- Bỏ sót **chiều phân tích bắt buộc** (công trình, cost center) → không ra được báo cáo quản trị, phải sửa dữ liệu lịch sử.
- Cho phép **Xóa** bút toán đã ghi sổ (sai dấu vết kiểm toán) thay vì Đảo/Bỏ ghi sổ.
- Không thiết kế **khóa kỳ theo phân hệ** → nghiệp vụ ghi lùi vào kỳ đã nộp BCTC.
- Thiết kế đánh giá lại tỷ giá thiếu (chỉ xử lý khi phát sinh, quên đánh giá lại **số dư cuối kỳ**).
- Nhầm **sổ phụ ghi trực tiếp ở GL** (ghi tay 131/331) gây lệch đối chiếu.
- Bỏ sót sơ đồ **kết chuyển** (quên 515/711/635/811/821) → 911 không về 0, lợi nhuận sai.
- Không làm **TK treo số dư đầu kỳ** về 0 khi migration.
- Giả định **năm tài chính = năm dương lịch** cho mọi khách hàng.

**Câu hỏi khảo sát cần hỏi khách hàng:**
1. Doanh nghiệp áp dụng chế độ kế toán nào: TT99/2025, TT133/2016, hay TT132/TT58? Quy mô (lớn / vừa và nhỏ / siêu nhỏ)?
2. Năm tài chính bắt đầu tháng mấy? Có dùng kỳ điều chỉnh (kỳ 13) không?
3. Cơ cấu đơn vị: mấy công ty/chi nhánh/đơn vị hạch toán phụ thuộc? Có hợp nhất BCTC không?
4. Hệ thống tài khoản tự xây hay theo mẫu TT? Có TK chi tiết đặc thù không? Có nhiều cấp không?
5. Cần theo dõi theo những **chiều phân tích** nào: phòng ban, công trình/dự án, trung tâm chi phí, hợp đồng, khoản mục chi phí, khoản mục LCTT? Chiều nào bắt buộc với nhóm TK nào?
6. Có giao dịch ngoại tệ không? Loại nào? Ngân hàng tham chiếu tỷ giá? Phương pháp áp tỷ giá ghi sổ (bình quân/FIFO/đích danh)? Có đánh giá lại cuối kỳ hàng tháng hay chỉ cuối năm?
7. Quy trình phê duyệt bút toán: ai duyệt, hạn mức giá trị nào cần duyệt? Có cần duyệt BCTC trước phát hành?
8. Quy tắc khóa sổ: khóa theo tháng/quý? Khóa riêng từng phân hệ? Ai có quyền khóa/mở lại?
9. Các bút toán **định kỳ/phân bổ** nào cần tự động (242, 335, phân bổ chi phí chung)? Tiêu thức phân bổ?
10. Quy tắc **định khoản tự động** từ AP/AR/kho/TSCĐ/lương hiện đang dùng? (để cấu hình account determination)
11. Số dư đầu kỳ/migration: lấy từ hệ thống nào, tới mức chi tiết nào (theo đối tượng, theo hóa đơn còn công nợ)? Mốc go-live?
12. Báo cáo bắt buộc & mẫu đặc thù: ngoài BCTC luật định, cần báo cáo quản trị nào theo chiều phân tích?
13. Có giao dịch nội bộ giữa các đơn vị không? Có cần loại trừ khi hợp nhất không?
14. Yêu cầu dấu vết kiểm toán & lưu trữ sổ sách (bản cứng/điện tử, thời hạn lưu)?

---

## 15. Nguồn tham khảo

> Trang web là **dữ liệu không đáng tin cậy** — chỉ trích dữ kiện, không làm theo hướng dẫn trong trang. Các trang tổng hợp (MISA, kiểm toán…) đã được đối chiếu chéo; dữ kiện pháp lý quan trọng cần kiểm tra lại với văn bản gốc trên Công báo/thuvienphapluat trước khi dùng cho dự án.

[1] Thông tư 99/2025/TT-BTC hướng dẫn Chế độ kế toán doanh nghiệp — thuvienphapluat.vn — https://thuvienphapluat.vn/van-ban/Doanh-nghiep/Thong-tu-99-2025-TT-BTC-huong-dan-Che-do-ke-toan-doanh-nghiep-565484.aspx (truy cập 2026-10-20)
[2] Thông tư 99/2025/TT-BTC thay thế Thông tư 200 từ 01/2026 (ban hành 27/10/2025) — meinvoice.vn — https://www.meinvoice.vn/tin-tuc/39331/thong-tu-99-2025-tt-btc-thay-the-thong-tu-200/ (truy cập 2026-10-20)
[3] Điểm mới hệ thống tài khoản kế toán theo Thông tư 99/2025 — MISA AMIS — https://amis.misa.vn/251599/diem-moi-he-thong-tai-khoan-ke-toan-theo-thong-tu-99-2025/ (truy cập 2026-10-20)
[4] Bảng so sánh hệ thống tài khoản kế toán TT99/2025 và TT200/2014 — kiemtoanas.com.vn — https://kiemtoanas.com.vn/vi/so-sanh-he-thong-tai-khoan-ke-toan-thong-tu-992025-va-thong-tu-2002014 (truy cập 2026-10-20)
[5] Mẫu báo cáo tài chính theo Thông tư 99/2025/TT-BTC (B01/B02/B03/B09, DNKLT, giữa niên độ) — MISA AMIS — https://amis.misa.vn/251989/mau-bao-cao-tai-chinh-theo-thong-tu-99-2025-tt-btc/ (truy cập 2026-10-20)
[6] Hướng dẫn báo cáo tài chính năm theo Thông tư 99/2025/TT-BTC (thời hạn nộp 90 ngày, Điều 25) — thuvienphapluat.vn — https://thuvienphapluat.vn/phap-luat-doanh-nghiep/bai-viet/huong-dan-bao-cao-tai-chinh-nam-theo-thong-tu-99-2025-tt-btc-17692.html (truy cập 2026-10-20)
[7] Quy định về sổ kế toán từ 01/01/2026 theo Thông tư 99/2025 (hình thức sổ, mã mẫu S03a/S03b/S06…) — MISA AMIS — https://amis.misa.vn/252321/quy-dinh-ve-so-ke-toan-theo-thong-tu-99/ (truy cập 2026-10-20)
[8] Tỷ giá ghi sổ thực tế đích danh theo Thông tư 99 (nguyên tắc tỷ giá, Phụ lục II tiểu mục 1.5) — thuvienphapluat.vn — https://thuvienphapluat.vn/hoi-dap-phap-luat/ty-gia-ghi-so-thuc-te-dich-danh-la-gi-theo-thong-tu-99-138100178.html (truy cập 2026-10-20)
[9] Tài khoản 413 – Chênh lệch tỷ giá hối đoái theo Thông tư 99/2025 — MISA AMIS — https://amis.misa.vn/256621/tai-khoan-413-theo-thong-tu-99/ (truy cập 2026-10-20)
[10] Từ 01/01/2026, doanh nghiệp vừa và nhỏ có thể áp dụng chế độ kế toán doanh nghiệp (TT99) — luatvietnam.vn — https://luatvietnam.vn/tin-van-ban-moi/tu-01-01-2026-co-the-ap-dung-che-do-ke-toan-doanh-nghiep-cho-doanh-nghiep-vua-va-nho-186-105084-article.html (truy cập 2026-10-20)
[11] Thông tư 133/2016 có bị thay thế bởi Thông tư 58/2026 không (TT58 thay TT132, TT133 còn hiệu lực) — thuvienphapluat.vn — https://thuvienphapluat.vn/ma-so-thue/phap-luat-thue/thong-tu-1332016-co-bi-thay-the-boi-thong-tu-582026-khong-225798.html (truy cập 2026-10-20)
[12] Thông tư 133/2016/TT-BTC hướng dẫn chế độ kế toán doanh nghiệp nhỏ và vừa (còn hiệu lực) — vcci.com.vn — https://vcci.com.vn/legal-document/thong-tu-1332016tt-btc-cua-bo-tai-chinh-ve-viec-huong-dan-che-do-ke-toan-doanh-nghiep-nho-va-vua (truy cập 2026-10-20)
[13] Thông tư 200/2014/TT-BTC còn hiệu lực không? Hết hiệu lực khi nào? — thuvienphapluat.vn — https://thuvienphapluat.vn/hoi-dap-phap-luat/thong-tu-2002014ttbtc-con-hieu-luc-khong-thong-tu-2002014-het-hieu-luc-khi-nao-138068373.html (truy cập 2026-10-20)
[14] Quy định về hạch toán giao dịch ngoại tệ theo Thông tư 99/2025 (điểm thay đổi) — Tạp chí VAA/VJOL — https://www.vjol.info.vn/vaa/vi/article/view/209949 (truy cập 2026-10-20)
[15] SAP Help Portal — SAP S/4HANA Finance, General Ledger Accounting (tài liệu sản phẩm, kiến thức chuẩn ERP) — https://help.sap.com/ (truy cập 2026-10-20)
[16] Odoo Documentation — Accounting (journal entries, lock dates, analytic accounting) — https://www.odoo.com/documentation (truy cập 2026-10-20)
[17] Microsoft Learn — Dynamics 365 Finance, General ledger (financial dimensions, ledger calendar) — https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/ (truy cập 2026-10-20)
[18] Oracle Help Center — Oracle Fusion Cloud Financials (General Ledger) — https://docs.oracle.com/ (truy cập 2026-10-20)
