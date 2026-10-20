# Danh mục báo cáo ERP chuẩn

Kho báo cáo chuẩn theo module và báo cáo bắt buộc theo luật Việt Nam, dùng ở **bước 1/2** (hỏi khách hàng cần những báo cáo nào) và **bước 3** (viết đặc tả báo cáo). Mọi báo cáo ở đây là **ứng viên/đề xuất** cho tới khi khách hàng xác nhận: khi đưa một báo cáo vào phạm vi dự án mà khách hàng chưa yêu cầu, gắn marker `[ĐỀ XUẤT → Q-…]` (xem `references/conventions.md` §4). Báo cáo bắt buộc theo luật không cần marker đề xuất nhưng phải ghi căn cứ.

> Nguồn tổng hợp: §11 của 15 file `references/processes/*.md`, §7 của `references/industries/*.md`, `references/regulations/*.md`, `references/nfr-catalog.md` §3.2–3.3, và danh sách ứng viên research (260 ứng viên). Khi ứng viên mâu thuẫn, **ưu tiên bản đã xác minh trong file `references/regulations/`** — xem `## Mâu thuẫn & điểm chưa xác minh` ở cuối.

## Mục lục
1. [Cách dùng](#cách-dùng)
2. [Nguyên tắc đặc tả báo cáo](#nguyên-tắc-đặc-tả-báo-cáo)
3. [Báo cáo bắt buộc theo luật (Việt Nam)](#báo-cáo-bắt-buộc-theo-luật-việt-nam)
4. [Báo cáo theo module](#báo-cáo-theo-module)
5. [Báo cáo & KPI theo ngành](#báo-cáo--kpi-theo-ngành)
6. [Dashboard & KPI quản trị chung](#dashboard--kpi-quản-trị-chung)
7. [Câu hỏi khảo sát về báo cáo](#câu-hỏi-khảo-sát-về-báo-cáo)
8. [Mâu thuẫn & điểm chưa xác minh](#mâu-thuẫn--điểm-chưa-xác-minh)

Ký hiệu: ✅ căn cứ đã xác minh trong file `regulations/`; ⚠️ CHƯA XÁC MINH — mã mẫu/chi tiết chỉ tiêu cần đối chiếu văn bản gốc trước khi khẳng định với khách hàng.

---

## Cách dùng

**Bước 1/2 — hỏi khách hàng cần báo cáo gì.** Lấy danh mục báo cáo của module/ngành liên quan làm checklist khảo sát: với mỗi báo cáo hỏi *"anh/chị có cần báo cáo này không, ai xem, bao lâu một lần, quyết định gì?"* (bộ câu hỏi ở `## Câu hỏi khảo sát về báo cáo`). Xin **mẫu báo cáo đang dùng** của khách hàng — mỗi mẫu đăng ký một `SRC-…`; một mẫu thật thay cho mười câu hỏi. Báo cáo bắt buộc theo luật đưa vào phạm vi mặc định, chỉ xác nhận **chế độ kế toán** (TT99 hay TT133) và **ngành đặc thù** để chọn đúng bộ mẫu.

**Bước 3 — viết đặc tả báo cáo.** Mỗi báo cáo trong phạm vi → một mục `RPT-…` trong `03-specification/catalogs/reports.md` và (nếu phức tạp) một file đặc tả `functions/<MOD>/FN-…` theo template `assets/templates/03-specification/report-spec.md`, đạt checklist `C3R-report.md`. Dùng bảng module dưới đây làm điểm xuất phát cho **mục đích, chiều phân tích, chứng từ & trạng thái được tính, người dùng**; rồi bổ sung cột/công thức/logic lấy số liệu theo yêu cầu thực tế của khách hàng (có nguồn).

**Mã RPT trong file này là chỉ dẫn, gom theo nguồn** (quy trình/ngành). Mã RPT **chính thức của dự án** được định nghĩa **một lần** trong `03-specification/catalogs/reports.md` (quy ước `RPT-<MOD>-NN`, xem `references/conventions.md` §2). Một số mã trùng nhau giữa các ngữ cảnh (ví dụ `RPT-INV-01` xuất hiện cả ở kho lõi và ở phân phối) — khử trùng khi đưa vào catalog dự án.

Ba báo cáo quy trình BA (Ma trận truy vết yêu cầu, Báo cáo tự kiểm bước 4, Báo cáo review độc lập bước 5) là **tạo tác của chính skill**, không phải báo cáo của sản phẩm ERP — không đưa vào catalog sản phẩm.

---

## Nguyên tắc đặc tả báo cáo

Một đặc tả báo cáo đủ để dev viết truy vấn và QA đối chiếu **phải nêu rõ** (khớp template `report-spec.md`):

| # | Mục bắt buộc | Nội dung phải nêu |
|---|---|---|
| 1 | **Mục đích & quyết định hỗ trợ** | Câu hỏi quản trị báo cáo trả lời; quyết định nào dựa trên nó. Không viết báo cáo "để cho có". |
| 2 | **Người dùng & phạm vi dữ liệu** | Vai trò (`ROLE-…`) xem/xuất; phạm vi dữ liệu (Của mình / Phòng ban / Chi nhánh / Công ty / theo kho/dự án); trường nhạy cảm bị ẩn (giá vốn, lương, đơn giá). |
| 3 | **Tham số lọc** | Từng bộ lọc: kiểu, bắt buộc?, mặc định, lookup, ràng buộc (ví dụ Từ ngày ≤ Đến ngày, khoảng tối đa là `PRM-…`). |
| 4 | **Cột & nguồn/công thức** | Mỗi cột: nguồn (bảng.trường) hoặc công thức tính; định dạng; có cộng tổng không. |
| 5 | **Nhóm & tổng phụ, sắp xếp** | Nhóm theo gì, tổng phụ theo gì, thứ tự sắp xếp; tiêu đề/chân trang/chữ ký nếu là mẫu luật. |
| 6 | **Chứng từ & trạng thái được tính** | Loại chứng từ (`DOC-…`) và **trạng thái** nào được tính (ví dụ chỉ `POSTED`, loại trừ `CANCELLED`/`REVERSED`/`DRAFT`). Dùng đúng bộ trạng thái chuẩn ở `conventions.md` §6. |
| 7 | **Ngày dùng để lọc** | **Ngày chứng từ (document date)** hay **ngày ghi sổ (posting date)** — khác biệt này quyết định số liệu; nêu rõ từng báo cáo. |
| 8 | **Logic số dư đầu kỳ** | Cách tính dư đầu kỳ (lũy kế từ đầu đến trước Từ ngày, hay lấy từ bảng số dư kỳ). |
| 9 | **Quy đổi tiền tệ** | Báo cáo đa tiền tệ: tỷ giá ghi sổ hay đánh giá lại; quy về VND thế nào; xử lý chênh lệch tỷ giá. |
| 10 | **Drill-down** | Bấm vào dòng mở chứng từ gốc nào; tôn trọng phạm vi dữ liệu người xem. |
| 11 | **Xuất file** | Excel/PDF; giữ định dạng mẫu luật; đặt tên file; mã hóa UTF-8 (NFR-LOC-05). |
| 12 | **Hiệu năng & khối lượng** | Số dòng dự kiến; thời gian chạy tối đa; chạy trực tuyến hay nền/snapshot (NFR-PERF-05/06/07, xem dưới). |
| 13 | **Dữ liệu mẫu kiểm tra** | Ít nhất một bộ chứng từ đầu vào → kết quả mong đợi, để QA đối chiếu. |

**Hiệu năng báo cáo (từ `nfr-catalog.md` §3.2–3.3) — gắn vào mục 12:**
- `NFR-PERF-05` Báo cáo Sổ cái một kỳ (≤ 500.000† bút toán) **PHẢI** hiện trang đầu ≤ 10 giây†, xuất Excel/PDF ≤ 30 giây† (p95).
- `NFR-PERF-06` Báo cáo tài chính toàn công ty **PHẢI** hoàn tất ≤ 60 giây†; nếu hơn **PHẢI** chạy nền và thông báo khi xong.
- `NFR-PERF-07` Báo cáo nặng **NÊN** chạy trên dữ liệu kết tập/bản sao đọc (read replica) để **KHÔNG** ảnh hưởng giao dịch trực tuyến.
- `NFR-PERF-09/10` Job sinh báo cáo cuối kỳ ≤ 2 giờ†, idempotent, có log và chạy lại phần lỗi.

(† = giá trị mẫu, phải thay bằng số khách hàng xác nhận → ghi thành `PRM-…` hoặc có nguồn `DEC-…`.)

**Lưu trữ:** báo cáo/sổ bắt buộc theo luật gắn retention class theo NĐ174/2016 — sổ kế toán, BCTC năm lưu **tối thiểu 10 năm**; chặn hủy trước hạn (xem `regulations/vn-accounting.md` §14).

---

## Báo cáo bắt buộc theo luật (Việt Nam)

Chế độ kế toán đang có hiệu lực tại **2026-10-20: Thông tư 99/2025/TT-BTC** (thay TT200 từ 01/01/2026); **doanh nghiệp nhỏ và vừa** được chọn tiếp tục **TT133/2016**; siêu nhỏ TT58/2026 (xem `regulations/vn-accounting.md` §2). Bảng dưới đây xác minh theo các file `regulations/`; chỗ nào các file đó chưa chắc chắn đánh ⚠️.

### A. Báo cáo tài chính (Financial Statements)

| Báo cáo / mẫu số | Căn cứ (văn bản, điều) | Áp dụng cho | Kỳ lập / hạn nộp | Module nguồn | Ghi chú thiết kế |
|---|---|---|---|---|---|
| **B01-DN** Báo cáo tình hình tài chính (Statement of Financial Position) | ✅ TT99/2025 Điều 17 (hệ thống BCTC); Điều 25/26 (nộp) | DN theo TT99 (năm TC ≥ 2026) | Năm; hạn **90 ngày** sau cuối năm TC (năm dương lịch → 31/3) | GL | **Đổi tên** từ "Bảng cân đối kế toán"; **không đổi mã số chỉ tiêu**; có bộ giữa niên độ B01a (đầy đủ)/B01b (tóm lược) và bộ DNKLT cho DN không hoạt động liên tục; khóa & versioning khi nộp lại |
| **B02-DN** Báo cáo kết quả hoạt động kinh doanh (Income Statement) | ✅ TT99/2025 Điều 17; VAS 21 | DN theo TT99 | Năm (+ giữa niên độ) | GL | Sinh từ số phát sinh TK loại 5–9 kết chuyển 911 → 421; chỉ tiêu EPS (VAS 30) cho công ty cổ phần |
| **B03-DN** Báo cáo lưu chuyển tiền tệ (Cash Flow Statement) | ✅ TT99/2025 Điều 17; VAS 24 | DN theo TT99 | Năm (+ giữa niên độ) | GL | Trực tiếp hoặc gián tiếp (tham số); số liệu từ dòng tiền 111/112 — **không** lập ở module CB |
| **B09-DN** Bản thuyết minh báo cáo tài chính (Notes to FS) | ✅ TT99/2025 Điều 17; VAS 21 | DN theo TT99 | Năm | GL | Thuyết minh chính sách kế toán + chi tiết chỉ tiêu; lấy số từ nhiều module (TSCĐ, HTK, dự phòng, công nợ) |
| Bộ BCTC **TT133/2016** (B01a/B01b-DNN…) | ⚠️ TT133/2016 còn hiệu lực cho SME (`vn-accounting` §2) — **mã mẫu từng biểu chưa liệt kê trong file regulations** | Doanh nghiệp nhỏ và vừa chọn TT133 | Năm | GL | Nếu dự án là SME dùng TT133: xác nhận bộ mẫu TT133 (khác cấu trúc TT99); không trộn hai chế độ |

### B. Sổ kế toán (Accounting Books) — TT99/2025 Phụ lục III

TT99 còn **42 mẫu sổ** (Phụ lục III, đã xác nhận); DN **được tự thiết kế** sổ miễn đủ thông tin. Mã mẫu dưới đây là **mã TT200 dùng tham chiếu** — ⚠️ **mã mẫu TT99 chưa đối chiếu bản gốc**. Số liệu lọc theo **ngày ghi sổ**; chỉ tính bút toán `POSTED`.

| Báo cáo / mẫu số | Căn cứ (văn bản, điều) | Áp dụng cho | Kỳ lập / hạn nộp | Module nguồn | Ghi chú thiết kế |
|---|---|---|---|---|---|
| Sổ Nhật ký chung (S03a-DN ⚠️) | ✅ TT99/2025 Phụ lục III; Luật KT Điều 24–26 | Mọi DN (hình thức Nhật ký chung) | Theo kỳ; lưu ≥ 10 năm | GL | Ghi liên tục theo thời gian; drill-down về chứng từ gốc |
| Sổ Cái từng tài khoản (S03b-DN ⚠️) | ✅ TT99/2025 Phụ lục III | Mọi DN | Theo kỳ | GL | Khớp với Bảng cân đối số phát sinh |
| Sổ, thẻ kế toán chi tiết (S10-DN, S07a-DN… ⚠️) | ✅ TT99/2025 Phụ lục III; Luật KT Điều 24 | Các TK cần theo dõi chi tiết (131/331/152…) | Theo kỳ | GL/AP/AR/INV | Theo đối tượng/chiều phân tích |
| Bảng cân đối số phát sinh (S06-DN ⚠️) | ✅ TT99/2025 Phụ lục III | Mọi DN | Theo kỳ | GL | Dư đầu – phát sinh – dư cuối toàn bộ TK; kiểm tra cân đối Nợ=Có |
| Nhật ký chuyên dùng thu/chi tiền, mua/bán (S03a1–S03a4-DN ⚠️) | ✅ TT99/2025 Phụ lục III | Có điều kiện theo hình thức sổ | Theo kỳ | GL/CB | Chỉ khi DN dùng nhật ký chuyên dùng |
| Sổ quỹ tiền mặt (S07-DN ⚠️); Sổ kế toán chi tiết quỹ (S07a-DN ⚠️) | ✅ Sổ kế toán bắt buộc TT99/2025 | Mọi DN | Theo kỳ | CB | Thủ quỹ ghi; đối chiếu với sổ kế toán tiền mặt |
| Sổ tiền gửi ngân hàng (S08-DN ⚠️) | ✅ Sổ kế toán bắt buộc TT99/2025 | Mọi DN | Theo kỳ | CB | Theo từng tài khoản ngân hàng, loại tiền |
| Thẻ kho / Sổ kho (S12-DN ⚠️) | ✅ Sổ kế toán theo chế độ | DN có hàng tồn kho | Theo kỳ (thủ kho ghi hằng ngày) | INV | Chỉ **số lượng**; đối chiếu với sổ chi tiết giá trị |
| Sổ chi tiết vật tư, công cụ, sản phẩm, hàng hóa (S10-DN ⚠️) | ✅ Sổ kế toán chi tiết | DN có HTK | Theo kỳ | INV | Số lượng **và** giá trị; feed Bảng cân đối |
| Thẻ TSCĐ; Sổ tài sản cố định | ✅ Luật KT 88/2015 Điều 24–26 (sổ/thẻ chi tiết); Phụ lục III TT99 ⚠️ | DN có TSCĐ | Theo kỳ/khi biến động | FA | Nguyên giá, hao mòn lũy kế, giá trị còn lại, bộ phận sử dụng |

### C. Kê khai thuế (Tax Declarations)

| Báo cáo / mẫu số | Căn cứ (văn bản, điều) | Áp dụng cho | Kỳ lập / hạn nộp | Module nguồn | Ghi chú thiết kế |
|---|---|---|---|---|---|
| Tờ khai thuế GTGT **01/GTGT** (VAT return) | ✅ TT 89/2026/TT-BTC (từ 01/7/2026, thay TT 80/2021); Luật 48/2024 — `vn-tax-einvoice` §2.6 | DN nộp GTGT khấu trừ | **Tháng** nếu DT năm trước > 50 tỷ; **Quý** nếu ≤ 50 tỷ hoặc mới thành lập | TAX | ⚠️ Mã chỉ tiêu mẫu mới theo phụ lục TT 89/2026 **chưa đối chiếu**; **không** nộp kèm bảng kê đầu ra/đầu vào (đã bỏ từ TT 80/2021) |
| Tờ khai quyết toán thuế TNDN **03/TNDN** (CIT finalization) | ✅ Luật 67/2025/QH15; NĐ 320/2025; TT 89/2026 — `vn-tax-einvoice` §3 | Mọi DN | Năm; **tạm nộp quý**, quyết toán **ngày cuối tháng thứ 3** sau cuối năm TC | TAX | Điều chỉnh chênh lệch kế toán–thuế; theo dõi **lỗ chuyển tối đa 5 năm**; cần cờ "chi phí được/không được trừ" ở cấp hóa đơn; ⚠️ phụ lục mẫu chưa đối chiếu |
| Bảng tổng hợp dữ liệu hóa đơn điện tử **01/TH-HĐĐT** (e-invoice data summary) | ✅ NĐ 254/2026/NĐ-CP; TT 91/2026/TT-BTC — `vn-tax-einvoice` §4.5 | Chỉ ngành đặc thù dùng **hóa đơn không mã** (viễn thông, bảo hiểm, tài chính–ngân hàng, hàng không, chứng khoán; điện, nước) | Theo kỳ khai GTGT | TAX | Chỉ áp dụng khi DN thuộc nhóm chuyển dữ liệu theo bảng tổng hợp; phần lớn DN chuyển **từng hóa đơn** |
| Thông báo hóa đơn điện tử có sai sót **04/SS-HĐĐT** | ✅ TT 91/2026 (Phụ lục III); nền NĐ 70/2025 — `vn-tax-einvoice` §4.6 | DN phát hành HĐĐT | Khi có sai sót; hạn **cuối kỳ khai GTGT** phát sinh | TAX | Sai nhỏ (tên/địa chỉ) chỉ gửi 04/SS, không lập lại; CQT phản hồi Mẫu 01/TB-SSĐT; quản lý quan hệ cha–con hóa đơn gốc ↔ điều chỉnh/thay thế |

### D. Dữ liệu & chứng từ hóa đơn điện tử (E-invoice data / vouchers)

| Báo cáo / mẫu số | Căn cứ (văn bản, điều) | Áp dụng cho | Kỳ lập / hạn nộp | Module nguồn | Ghi chú thiết kế |
|---|---|---|---|---|---|
| Hóa đơn điện tử + chuyển dữ liệu tới cơ quan thuế | ✅ NĐ 254/2026; TT 91/2026 — `vn-tax-einvoice` §4 | Mọi DN phát hành hóa đơn | Theo giao dịch; ký số & gửi **chậm nhất ngày làm việc tiếp theo** | TAX/SAL | Có mã: gửi CQT cấp mã trước; không mã: tự phát hành rồi chuyển dữ liệu; qua tổ chức dịch vụ HĐĐT; retry/idempotency chống phát hành trùng |
| Hóa đơn điện tử từ máy tính tiền (cash-register e-invoice) | ✅ NĐ 254/2026 Điều 11; Luật QLT 108/2025 — `vn-tax-einvoice` §4.7 | Hộ/cá nhân KD & DN bán lẻ, ăn uống… DT ≥ 1 tỷ/năm | Theo giao dịch; dữ liệu gửi cuối ngày | TAX/POS | Không bắt buộc chữ ký số; tích hợp POS → hóa đơn; đối soát doanh thu |
| Chứng từ khấu trừ thuế TNCN điện tử (e-withholding certificate) | ✅ NĐ 254/2026 (Đ.23); Luật QLT 108/2025 — `vn-labor-payroll` §6.4 | Tổ chức chi trả thu nhập | Gửi CQT **ngay trong ngày lập** | TAX/PAY | ⚠️ mẫu (một số nguồn nêu 03/TNCN theo NĐ 70/2025) chưa đối chiếu; HĐLĐ ≥ 3 tháng: 1 chứng từ/năm |

### E. Lao động – Bảo hiểm – Thuế TNCN (Labour / Insurance / PIT)

| Báo cáo / mẫu số | Căn cứ (văn bản, điều) | Áp dụng cho | Kỳ lập / hạn nộp | Module nguồn | Ghi chú thiết kế |
|---|---|---|---|---|---|
| Phiếu lương / bảng kê trả lương (Payslip) | ✅ BLLĐ 45/2019 Điều 95 khoản 3 — `vn-labor-payroll` §4 | Mọi NSDLĐ | Mỗi kỳ trả lương | PAY | NSDLĐ **phải** cung cấp bảng kê trả lương cho NLĐ; thể hiện lương, khấu trừ, các khoản trích |
| Hồ sơ báo tăng/giảm & đối chiếu BHXH/BHYT/BHTN (D02-LT; C12-TS) | ✅ Luật BHXH 41/2024; NĐ 158/2025 — `vn-labor-payroll` §5.3 | DN có lao động đóng BHXH | **Tháng** (chậm nhất ngày cuối tháng) | PAY | ⚠️ mẫu **D02-LT** hiện hành cần kiểm tra; điều chỉnh khi biến động lao động/tiền lương |
| Tờ khai khấu trừ thuế TNCN tháng/quý **05/KK-TNCN** | ✅ Luật Quản lý thuế — `vn-labor-payroll` §6.5 | Tổ chức chi trả thu nhập | Tháng hoặc quý | PAY | Kê khai số TNCN đã khấu trừ; đồng bộ với chứng từ khấu trừ điện tử |
| Tờ khai quyết toán thuế TNCN năm **05/QTT-TNCN** (+ 05-1/BK, 05-2/BK) | ✅ Luật Quản lý thuế — `vn-labor-payroll` §6.5 | DN quyết toán thay cá nhân ủy quyền | Năm; hạn **cuối tháng thứ 3** (DN) / tháng thứ 4 (cá nhân) sau cuối năm | PAY | Giảm trừ gia cảnh **15,5 tr/tháng** (bản thân) & 6,2 tr/người phụ thuộc từ kỳ 2026; biểu thuế 5 bậc từ 2026 |
| Báo cáo tình hình sử dụng lao động (khai trình lao động) | ⚠️ NĐ 145/2020/NĐ-CP — `vn-labor-payroll`/`hr-payroll` §11 | Mọi NSDLĐ | Định kỳ (6 tháng/năm) nộp Sở LĐTBXH | HR | ⚠️ mẫu & kỳ hiện hành cần kiểm tra (có thay đổi theo văn bản mới) |
| Báo cáo/quyết toán kinh phí công đoàn (KPCĐ 2%) | ✅ Luật Công đoàn 50/2024 | DN thuộc diện nộp KPCĐ | Theo kỳ công đoàn | PAY | Trích nộp 2% quỹ lương; quyết toán với công đoàn cấp trên |

> **Hồ sơ tuân thủ bảo vệ dữ liệu cá nhân (PDPL)** — Sổ đăng ký đồng ý, hồ sơ DPIA (Mẫu 10), nhật ký chuyển dữ liệu xuyên biên giới (Mẫu 09) — là **bắt buộc theo Luật 91/2025/QH15 & NĐ 356/2025/NĐ-CP**, nhưng là **hồ sơ lưu trữ/xuất trình khi cơ quan yêu cầu**, không phải báo cáo định kỳ nộp. Căn cứ nằm ở `references/security-and-parameters.md` / `nfr-catalog.md`, **không thuộc 3 file `regulations/` fiscal** nên chưa xác minh chéo tại đây → xem nhóm SYS và `## Mâu thuẫn & điểm chưa xác minh`.

---

## Danh mục báo cáo theo module (tổng hợp từ các file quy trình, ngành, luật)

### AP

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Sổ chi tiết công nợ phải trả theo nhà cung cấp | Vendor Sub-ledger | Theo dõi phát sinh và số dư công nợ từng nhà cung cấp. | Có | Chế độ kế toán TT 99/2025/TT-BTC (sổ kế toán chi tiết) |
| Bảng tổng hợp công nợ phải trả | AP Summary | Tổng hợp số dư đầu/phát sinh/cuối của toàn bộ nhà cung cấp. | Không | — |
| Bảng phân tích tuổi nợ phải trả | AP Aging | Phân nhóm nợ theo tuổi để quản trị dòng tiền chi và nợ đến hạn. | Không | — |
| Biên bản đối chiếu công nợ nhà cung cấp | Vendor Reconciliation Statement | Xác nhận số dư công nợ với nhà cung cấp. | Không | — |
| Báo cáo GR/IR chưa khớp | GR-IR Open Items | Phát hiện hàng đã nhận chưa có hóa đơn hoặc hóa đơn chưa có hàng. | Không | — |
| Nhật ký mua hàng | Purchase Journal | Ghi nhận giao dịch mua theo trình tự thời gian. | Có | Sổ kế toán theo TT 99/2025 |
| Bảng kê/sổ theo dõi thuế GTGT đầu vào | Input VAT Ledger | Phục vụ lập Tờ khai thuế GTGT và theo dõi điều kiện khấu trừ. | Có | Luật Quản lý thuế & quy định hóa đơn điện tử; Tờ khai GTGT là bắt buộc |
| Báo cáo nợ đến hạn và dự báo dòng tiền chi | AP Due / Cash Forecast | Lập kế hoạch chi theo ngày đến hạn. | Không | — |
| Sổ cái tài khoản 331 | GL Account 331 | Khớp số liệu sổ cái với sổ chi tiết công nợ phải trả. | Có | Sổ cái theo TT 99/2025 |
| Báo cáo tạm ứng nhà cung cấp chưa tất toán | Open Vendor Advances | Kiểm soát các khoản trả trước chưa cấn trừ. | Không | — |

### AR

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Sổ chi tiết công nợ phải thu theo khách hàng | Customer Sub-ledger | Theo dõi phát sinh và số dư công nợ từng khách hàng. | Có | Chế độ kế toán TT 99/2025 (sổ kế toán chi tiết) |
| Bảng tổng hợp công nợ phải thu | AR Summary | Tổng hợp số dư công nợ của toàn bộ khách hàng. | Không | — |
| Bảng phân tích tuổi nợ phải thu | AR Aging | Theo dõi nợ quá hạn và rủi ro thu hồi theo bucket. | Không | — |
| Biên bản đối chiếu công nợ khách hàng | Customer Reconciliation Statement | Xác nhận số dư công nợ với khách hàng. | Không | — |
| Báo cáo hạn mức và rủi ro tín dụng | Credit Exposure Report | Quản trị tín dụng, % sử dụng hạn mức và đơn bị khóa. | Không | — |
| Bảng kê/sổ theo dõi thuế GTGT đầu ra | Output VAT Ledger | Phục vụ lập Tờ khai thuế GTGT đầu ra. | Có | Tờ khai GTGT bắt buộc; quy định hóa đơn điện tử |
| Nhật ký bán hàng | Sales Journal | Ghi nhận giao dịch bán theo trình tự thời gian. | Có | Sổ kế toán theo TT 99/2025 |
| Báo cáo dự phòng nợ phải thu khó đòi | Doubtful-debt Provision Report | Theo dõi trích lập, hoàn nhập và xóa sổ nợ khó đòi. | Không | Thông tư 48/2019/TT-BTC |
| Báo cáo nhắc nợ/đốc nợ | Collections / Dunning Report | Theo dõi nhắc nợ theo cấp và cam kết trả nợ. | Không | — |
| Báo cáo DSO và hiệu quả thu hồi | DSO Report | Đo kỳ thu tiền bình quân và hiệu quả thu hồi công nợ. | Không | — |
| Sổ cái tài khoản 131 | GL Account 131 | Khớp số liệu sổ cái với sổ chi tiết công nợ phải thu. | Có | Sổ cái theo TT 99/2025 |
| Công nợ & tuổi nợ (aging), DSO theo khách | AR Aging / DSO report | Kiểm soát rủi ro tín dụng và kỳ thu tiền (chi tiết tại ar-accounts-receivable.md). | Không | — |

### AUDIT

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Báo cáo/tra cứu vết kiểm toán | Audit trail report | Truy vết ai làm gì, khi nào, giá trị trước–sau theo chứng từ/người dùng/khoảng thời gian; phục vụ kiểm toán nội bộ, kiểm toán độc lập, thanh/kiểm tra thuế. | Không | Luật Kế toán 88/2015/QH13 & Nghị định 174/2016/NĐ-CP (yêu cầu bất biến & lưu trữ) [6] |

### AVAIL

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Báo cáo tính sẵn sàng / uptime | Availability / Uptime report | Theo dõi và chứng minh mức SLA uptime theo tháng, loại trừ bảo trì có kế hoạch. | Không | SLA hợp đồng |
| Nhật ký sao lưu & biên bản diễn tập phục hồi | Backup log & DR drill report | Ghi lịch sao lưu, vị trí, mã hóa và kết quả diễn tập khôi phục (RPO/RTO thực đo được). | Không | Chính sách DR nội bộ |

### BA

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Ma trận truy vết yêu cầu | Requirements Traceability Matrix | Liên kết nhu cầu→REQ→FR→AC→test; phát hiện FR mồ côi (chức năng thừa) và REQ thiếu bao phủ (chức năng thiếu) | Không | Sinh tự động bởi scripts/ba.py trace (file traceability.md); không sửa tay |
| Báo cáo tự kiểm (bước 4) | Self-verification report | Ghi phát hiện VF-* khi BA/agent tự kiểm đặc tả trước review độc lập; cổng chất lượng nội bộ | Không | 04-verification/verify-report-r<N>.md; checklist C4-verification.md |
| Báo cáo review độc lập (bước 5) | Independent review report | Ghi phát hiện RV-* theo 4 góc nhìn (dev/tester/khách hàng/kiểm toán); phân loại Critical/Major/Minor; cổng 0 Critical-Major mới Ready | Không | 05-review/review-report-r<N>.md; checklist C5-review.md; IEEE 1028; PBR (Basili et al.) |

### BIL

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Lãi lỗ theo lô | Job P&L / Profit per Shipment | Kiểm soát biên lợi nhuận từng lô = tổng sell trừ tổng buy trừ phân bổ chi phí chung. | Không | Dữ liệu phí sell/buy gắn mã lô |
| Doanh thu theo khách/tuyến/dịch vụ | Revenue by customer/lane/service | Phân tích doanh thu và khách hàng/tuyến trọng điểm. | Không | Hóa đơn/Debit Note |
| Lô chưa lập hóa đơn và tuổi nợ | Unbilled / WIP and aging | Chống thất thu, đẩy nhanh lập hóa đơn các lô đã hoàn thành. | Không | Lô COMPLETED chưa POSTED hóa đơn |
| Bảng kê công nợ đại lý (SOA) | Agent Statement of Account | Đối chiếu và bù trừ công nợ đại lý quốc tế đa tiền tệ. | Không | 131/331 theo đại lý |

### BUD

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Ngân sách vs Thực tế | Budget vs Actual (BvA) | So trần/mục tiêu với thực hiện, tính chênh lệch và % theo khoản mục, cost center, kỳ, phiên bản. | Không | Thực hành quản trị; chuẩn ERP (Odoo/Dynamics/SAP/Oracle) |
| Ngân sách - Cam kết - Thực tế và Số khả dụng | Budget vs Commitment vs Actual / Available | Xem số còn được chi sau khi trừ cam kết và dự chi; tách ba đại lượng. | Không | SAP FMAVCR01 [3]; Oracle Budget Monitor [4] |
| Sổ cam kết / Phong tỏa | Commitment / Encumbrance Register | Liệt kê PR/PO/hợp đồng đang giữ chỗ ngân sách và trạng thái cam kết. | Không | Chuẩn ERP (SAP FM/Oracle/Dynamics) |
| Phân tích chênh lệch | Variance Analysis | Diễn giải lệch thuận lợi/bất lợi theo khoản mục và đơn vị. | Không | Kế toán quản trị |
| Tiến độ sử dụng ngân sách / Burn rate | Budget Utilization / Burn Rate | Tỷ lệ đã dùng và tốc độ tiêu so với tiến độ thời gian (theoretical amount). | Không | Odoo practical vs theoretical [6] |
| Dự báo cuốn chiếu và Dự báo đến cuối năm | Rolling Forecast / Forecast to Complete | Dự báo cập nhật = thực tế lũy kế + cam kết + ước tính còn lại cho 12-18 tháng. | Không | Thực hành FP&A |
| Nhật ký điều chỉnh/điều chuyển/bổ sung ngân sách | Budget Change Log | Truy vết thay đổi ngân sách theo phiên bản, người duyệt, giá trị. | Không | Kiểm soát nội bộ (audit trail) |
| Ngân sách tiền mặt / Dòng tiền dự kiến | Cash Budget / Cash Flow Forecast | Dự báo thu-chi tiền theo kỳ để quản trị thanh khoản. | Không | Liên kết cash-bank.md |
| Ngoại lệ vượt ngân sách và Override | Over-budget & Override Exceptions | Giám sát các lần vượt trần và override phục vụ hậu kiểm. | Không | Dynamics khuyến nghị theo dõi override [5] |
| Tổng hợp ngân sách theo phân cấp | Consolidated Budget by Hierarchy | Hợp nhất ngân sách theo cây cost center/khoản mục/phiên bản. | Không | Chuẩn ERP |

### CB

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Sổ quỹ tiền mặt | Cash Book | Theo dõi thu/chi/tồn quỹ tiền mặt theo thời gian, theo quỹ và loại tiền. | Có | Sổ kế toán bắt buộc theo TT99/2025; mẫu tham chiếu S07-DN theo TT200 (mã mẫu TT99 chưa xác minh) |
| Sổ kế toán chi tiết quỹ tiền mặt | Cash Detail Ledger | Chi tiết thu/chi quỹ theo đối tượng và khoản mục. | Có | Mẫu tham chiếu S07a-DN theo TT200 (mã mẫu TT99 chưa xác minh) |
| Sổ tiền gửi ngân hàng | Bank Book | Theo dõi biến động và số dư từng tài khoản ngân hàng. | Có | Sổ kế toán bắt buộc theo TT99/2025; mẫu tham chiếu S08-DN theo TT200 (mã mẫu TT99 chưa xác minh) |
| Báo cáo tồn quỹ và số dư ngân hàng | Cash Position Report | Hiển thị tồn quỹ và số dư ngân hàng tức thời theo quỹ/tài khoản/chi nhánh. | Không | — |
| Nhật ký thu chi | Cash and Bank Journal | Liệt kê các giao dịch thu/chi theo kỳ, theo khoản mục và phương thức. | Không | — |
| Bảng đối chiếu số dư ngân hàng | Bank Reconciliation Statement | Khớp số dư sổ sách với sao kê và làm rõ các khoản treo. | Không | Không bắt buộc theo luật nhưng kiểm toán yêu cầu |
| Báo cáo công nợ tạm ứng | Advance Aging Report | Theo dõi các khoản tạm ứng chưa quyết toán theo nhân viên và tuổi nợ. | Không | — |
| Dự báo dòng tiền | Cash-flow Forecast | Dự kiến thu/chi và thanh khoản theo kỳ và kịch bản. | Không | — |

### COST

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Bảng tính giá thành sản phẩm | Production Cost Statement | Tính tổng và đơn vị giá thành theo khoản mục (621/622/627) cho từng đối tượng/sản phẩm/kỳ. | Không | VAS 02; kế toán quản trị |
| Thẻ tính giá thành | Cost Card | Chi tiết cấu thành giá thành của một đối tượng/đơn hàng theo khoản mục chi phí. | Không | Kế toán quản trị |
| Bảng phân bổ chi phí sản xuất chung | Overhead Allocation Report | Minh bạch việc phân bổ 627 theo công suất bình thường và phần không phân bổ đưa vào 632. | Không | VAS 02 Điểm 08 |
| Bảng đánh giá sản phẩm dở dang | WIP Valuation Report | Xác định giá trị TK 154 cuối kỳ theo phương pháp đánh giá đã chọn. | Không | VAS 02 |
| Báo cáo chênh lệch giá thành | Variance Report | Phân tích chênh lệch định mức – thực tế theo giá và lượng cho NVL, nhân công, SX chung. | Không | Chuẩn SAP CO-PC / kế toán quản trị |
| Sổ chi tiết và tổng hợp Nhập – Xuất – Tồn theo giá trị | Inventory Valuation / Stock Ledger | Theo dõi giá trị tồn kho theo giá vốn; đối chiếu sổ kho với sổ cái, cung cấp số liệu cho Bảng cân đối kế toán. | Có | TT99/2025; VAS 02 |
| Bảng kê phân bổ chi phí thu mua | Landed Cost Allocation Report | Kiểm tra việc phân bổ chi phí thu mua/nhập khẩu vào giá gốc theo lô nhập/chứng từ. | Không | VAS 02 |
| Báo cáo giá vốn hàng bán | COGS Report | Phân tích giá vốn theo mặt hàng/khách hàng/kênh; cung cấp số liệu cho Báo cáo kết quả kinh doanh. | Có | TT99/2025 |
| Báo cáo giá thành định mức so với thực tế | Standard vs Actual Cost Report | So sánh và theo dõi xu hướng giá thành định mức với thực tế. | Không | Kế toán quản trị |
| Báo cáo giá thành theo dự án/hợp đồng | Project / Contract Cost Report | Tổng hợp chi phí và kết quả theo dự án/hợp đồng/giai đoạn (liên kết module PRJ). | Không | VAS 15; kế toán quản trị |
| Chi phí theo khoản mục & hạng mục | Cost by Element / Work Item | Kiểm soát chi phí công trình theo 3 chiều phân tích | Không | — |
| Ngân sách so thực tế & dự báo chi phí hoàn thành (EAC) | Budget vs Actual & Estimate at Completion | Cảnh báo vượt chi, dự báo lãi lỗ | Không | — |
| Lãi lỗ công trình & dở dang | Project P&L & WIP | Đánh giá hiệu quả từng công trình | Không | — |
| Bảng kê chi phí dở dang TK 154 theo công trình | WIP Breakdown by Project | Thuyết minh WIP phục vụ khóa sổ và BCTC | Có | TT 99/2025/TT-BTC |

### CRM

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Báo cáo phễu bán hàng | Sales Pipeline Report | Theo dõi cơ hội theo giai đoạn và giá trị để quản lý bán hàng | Không | Báo cáo quản trị |
| Dự báo doanh số | Sales Forecast | Dự báo doanh thu theo % xác suất của từng giai đoạn phễu | Không | Báo cáo quản trị |
| Tỷ lệ chuyển đổi và Thắng/Thua | Conversion & Win/Loss Report | Đo hiệu quả bán và phân tích lý do thắng/thua | Không | Báo cáo quản trị |
| Hiệu quả chiến dịch marketing | Campaign ROI Report | So sánh chi phí và kết quả (lead, cơ hội, doanh thu) theo chiến dịch | Không | Báo cáo quản trị |
| Báo cáo hoạt động nhân viên kinh doanh | Sales Activity Report | Thống kê cuộc gọi/họp/công việc và kết quả theo nhân viên | Không | Báo cáo quản trị |
| Phân khúc và giá trị khách hàng | Customer Segmentation & CLV | Phân tích phân khúc và giá trị vòng đời khách hàng | Không | Báo cáo quản trị |

### CTR

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Theo dõi tạm ứng & thu hồi, giữ lại theo hợp đồng | Advance & Retention Tracking | Kiểm soát dòng tiền theo hợp đồng | Không | — |
| Theo dõi bảo lãnh & cảnh báo hết hiệu lực | Guarantee Register | Quản trị rủi ro bảo lãnh thực hiện/tạm ứng/bảo hành | Không | — |

### CUS

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Tình trạng tờ khai và thời gian thông quan | Customs declaration status & clearance time | Theo dõi phân luồng (xanh/vàng/đỏ) và SLA thông quan. | Không | Tờ khai hải quan |

### DMS

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Tuân thủ viếng thăm & tuyến | Visit Compliance report | Giám sát việc đi tuyến đúng kế hoạch của DSR. | Không | — |
| Độ phủ & điểm bán có đơn | Coverage / Active Outlets report | Đo độ phủ thị trường và số điểm bán phát sinh đơn. | Không | — |
| Năng suất nhân viên bán hàng tuyến | DSR Productivity report | Đánh giá số viếng thăm, strike rate, số SKU trên đơn. | Không | — |
| Đối soát van sales cuối ngày | Van sales reconciliation | Đối soát tồn xe và tiền mặt cuối ngày của van sales. | Không | — |

### ECM

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Đối soát doanh thu – phí sàn TMĐT | Marketplace Reconciliation report | Đối soát doanh thu, phí sàn, COD và hoàn theo kênh online. | Không | — |

### EQP

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Nhật ký & hiệu suất ca máy, chi phí máy theo công trình | Machine Shift Log & Equipment Cost | Kiểm soát cơ giới và chi phí máy thi công | Không | — |

### EST

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Tổng hợp dự toán / giá dự thầu theo khoản mục | Cost Estimate / Bid Price Summary | Cơ sở lập ngân sách và chiến lược bỏ thầu | Không | — |

### FA

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Bảng tính và phân bổ khấu hao TSCĐ | Fixed Asset Depreciation Schedule | Tính và phân bổ khấu hao kỳ làm căn cứ hạch toán chi phí. | Không | TT45/2013 (chứng từ/bảng tính hỗ trợ) |
| Thẻ tài sản cố định | Fixed Asset Card | Hồ sơ chi tiết từng tài sản: nguyên giá, hao mòn lũy kế, giá trị còn lại, bộ phận sử dụng và lịch sử biến động. | Có | Luật Kế toán 88/2015 (sổ/thẻ kế toán chi tiết); mẫu Thẻ TSCĐ theo Phụ lục TT 99/2025 (truyền thống mẫu TT 200) |
| Sổ tài sản cố định | Fixed Asset Register | Danh mục và biến động toàn bộ TSCĐ theo nhóm, bộ phận, nguồn hình thành, kỳ. | Có | Luật Kế toán 88/2015 Điều 24-26 (sổ kế toán chi tiết); Phụ lục III TT 99/2025 |
| Bảng tính và phân bổ khấu hao tài sản cố định | Depreciation Calculation and Allocation Sheet | Tính mức khấu hao kỳ theo tài sản và phân bổ chi phí khấu hao theo bộ phận sử dụng; là căn cứ ghi sổ bút toán khấu hao. | Có | Chứng từ căn cứ ghi sổ theo TT 45/2013 và TT 99/2025 (mẫu Bảng tính và phân bổ khấu hao TSCĐ) |
| Bảng phân bổ công cụ dụng cụ | Tools and Supplies Allocation Sheet | Phân bổ giá trị công cụ dụng cụ xuất dùng nhiều kỳ vào chi phí theo bộ phận. | Không | Chứng từ nội bộ; tuân trần phân bổ 36 tháng cho mục đích thuế (TT 96/2015 gốc, NĐ 320/2025) |
| Bảng phân bổ chi phí trả trước | Prepaid Expenses Allocation Sheet | Phân bổ số dư TK 242 vào chi phí từng kỳ theo thời gian được hưởng lợi ích. | Không | — |
| Biên bản kiểm kê tài sản cố định | Fixed Asset Count Minutes | Đối chiếu tài sản sổ sách với thực tế, ghi nhận và xử lý thừa/thiếu. | Không | Không bắt buộc nộp nhưng là hồ sơ bắt buộc cho kiểm toán và kiểm kê cuối năm (Luật Kế toán) |
| Báo cáo tăng giảm tài sản cố định | Fixed Asset Movement Report | Theo dõi biến động nguyên giá và hao mòn trong kỳ theo loại biến động và nhóm tài sản. | Không | — |
| Báo cáo tài sản cố định đã khấu hao hết còn sử dụng | Fully Depreciated Assets in Use Report | Kiểm soát các tài sản đã hết khấu hao nhưng vẫn đang sử dụng. | Không | — |
| Sổ theo dõi công cụ dụng cụ tại nơi sử dụng | Tools in Use Tracking Book | Quản lý hiện vật công cụ dụng cụ theo bộ phận và địa điểm. | Không | — |
| Báo cáo giá trị còn lại tài sản cố định theo bộ phận | Net Book Value by Department Report | Cung cấp giá trị còn lại phục vụ Báo cáo tình hình tài chính (B01-DN) và phân bổ chi phí. | Không | — |

### FWD

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Tình trạng lô hàng | Shipment status report | Theo dõi tiến độ, mốc thời gian (ETD/ETA) và chứng từ của từng lô. | Không | Milestones hồ sơ lô |

### GL

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Báo cáo lưu chuyển tiền tệ | Statement of Cash Flows | Một phần Báo cáo tài chính năm (trực tiếp/gián tiếp); lập tại GL/R2R, không thuộc CB. | Có | Thành phần BCTC bắt buộc theo TT99/2025; xem r2r-general-ledger.md |
| Sổ Nhật ký chung | General Journal | Ghi nhận mọi bút toán theo trình tự thời gian | Có | TT99/2025, mẫu S03a-DN |
| Sổ Cái | General Ledger | Theo dõi phát sinh và số dư từng tài khoản | Có | TT99/2025, mẫu S03b-DN |
| Sổ chi tiết tài khoản | Account Detail Ledger | Chi tiết phát sinh theo đối tượng/chiều phân tích của một tài khoản | Có | TT99/2025 |
| Bảng cân đối số phát sinh | Trial Balance | Kiểm tra dư đầu – phát sinh – dư cuối toàn bộ tài khoản, bảo đảm cân đối | Có | TT99/2025, mẫu S06-DN |
| Báo cáo tình hình tài chính | Statement of Financial Position | Phản ánh tài sản, nợ phải trả và vốn chủ sở hữu tại thời điểm báo cáo | Có | TT99/2025, mẫu B01-DN (thay tên Bảng cân đối kế toán) |
| Báo cáo kết quả hoạt động kinh doanh | Income Statement | Phản ánh doanh thu, chi phí và lợi nhuận trong kỳ | Có | TT99/2025, mẫu B02-DN |
| Bản thuyết minh Báo cáo tài chính | Notes to the Financial Statements | Thuyết minh chính sách kế toán và chi tiết số liệu | Có | TT99/2025, mẫu B09-DN |
| Sổ nhật ký chuyên dùng (thu/chi tiền, mua/bán hàng) | Special Journals | Nhật ký chuyên dùng theo hình thức Nhật ký chung | Có | TT99/2025, mẫu S03a1–S03a4-DN (có điều kiện theo hình thức sổ) |
| Bảng tổng hợp phát sinh theo đối tượng/chiều phân tích | Dimension Analysis Report | Báo cáo quản trị chi phí/doanh thu theo phòng ban, công trình, dự án | Không | Nội bộ (không bắt buộc theo luật) |
| Báo cáo tình hình tài chính (B01-DN) | Statement of Financial Position | Phản ánh tài sản, nợ phải trả, vốn chủ sở hữu tại thời điểm báo cáo; thay tên 'Bảng cân đối kế toán' theo TT99. | Có | TT99/2025 Điều 25; mẫu B01-DN (Phụ lục BCTC) |
| Báo cáo kết quả hoạt động kinh doanh (B02-DN) | Income Statement | Phản ánh doanh thu, chi phí, lợi nhuận trong kỳ. | Có | TT99/2025; mẫu B02-DN |
| Báo cáo lưu chuyển tiền tệ (B03-DN) | Cash Flow Statement | Phản ánh dòng tiền hoạt động kinh doanh, đầu tư, tài chính (trực tiếp/gián tiếp). | Có | TT99/2025; mẫu B03-DN; VAS 24 |
| Bản thuyết minh báo cáo tài chính (B09-DN) | Notes to the Financial Statements | Thuyết minh chính sách kế toán và chi tiết chỉ tiêu BCTC. | Có | TT99/2025; mẫu B09-DN; VAS 21 |
| Sổ (thẻ) kế toán chi tiết | Account Subledger | Theo dõi chi tiết theo đối tượng (khách hàng, nhà cung cấp, vật tư). | Có | TT99/2025 Phụ lục III |
| Bảng trích lập dự phòng | Provisions Schedule | Tính mức trích/hoàn nhập dự phòng nợ phải thu, giảm giá HTK, bảo hành cuối kỳ. | Không | TT48/2019 Điều 6 |
| Báo cáo tài chính (BCĐKT, KQKD, LCTT, thuyết minh) | Financial statements | Nghĩa vụ báo cáo tài chính luật định theo chế độ kế toán. | Có | Thông tư 99/2025/TT-BTC |

### HR

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Bảng chấm công | Timesheet | Tổng hợp ngày công, giờ làm thêm, ca đêm, nghỉ phép làm căn cứ tính lương. | Không | Chứng từ kế toán TT 99/2025 (mẫu 01a-LĐTL) |
| Báo cáo tình hình sử dụng lao động | Labour Usage Report | Báo cáo định kỳ số lượng, biến động lao động cho cơ quan quản lý lao động. | Có | Nghị định 145/2020/NĐ-CP |
| Báo cáo biến động nhân sự / Headcount | Headcount / Workforce Movement | Theo dõi tăng/giảm nhân sự và định biên | Không | — |
| Báo cáo tình hình sử dụng lao động (khai trình lao động) | Labor Usage Report | Báo cáo định kỳ sử dụng lao động cho Sở LĐTBXH | Có | NĐ 145/2020/NĐ-CP ⚠️ kiểm tra mẫu & kỳ hiện hành — xem vn-labor-payroll.md |
| Báo cáo tỷ lệ nghỉ việc | Turnover Report | Quản trị nhân sự, phân tích lý do nghỉ việc | Không | — |
| Bảng chấm công tổng hợp | Attendance Summary | Tổng hợp công/giờ làm thêm/nghỉ làm cơ sở tính lương | Không | — |
| Báo cáo làm thêm giờ | Overtime Report | Kiểm soát trần OT và chi phí OT; cơ sở thông báo Sở LĐ khi >200 giờ/năm | Không | — |
| Báo cáo số dư phép | Leave Balance Report | Quản lý quỹ phép và chi trả phép tồn khi nghỉ việc | Không | — |

### INTG

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Báo cáo đối soát tích hợp | Integration reconciliation report | So khớp hằng ngày giữa ERP và hóa đơn điện tử/ngân hàng để phát hiện lệch, trùng, thiếu giao dịch. | Không | Thực hành kiểm soát tích hợp; xem references/regulations/vn-tax-einvoice.md |

### INV

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Thẻ kho (Sổ kho) | Bin (Stock) Card | Theo dõi nhập–xuất–tồn số lượng từng mặt hàng tại một kho, do thủ kho ghi hằng ngày. | Có | Mẫu S12-DN theo chế độ kế toán (TT200/TT99 Phụ lục) |
| Sổ chi tiết vật tư, công cụ, sản phẩm, hàng hóa | Inventory Subledger | Theo dõi nhập–xuất–tồn cả số lượng và giá trị chi tiết theo mặt hàng và kho. | Có | Mẫu S10-DN theo chế độ kế toán |
| Bảng tổng hợp Nhập–Xuất–Tồn | Goods Received-Issued-Balance Summary | Tổng hợp biến động và tồn cuối kỳ toàn kho theo nhóm hàng; đối chiếu nhanh. | Không | Báo cáo quản trị (liên quan Bảng tổng hợp chi tiết S11-DN) |
| Báo cáo tồn kho theo lô / hạn dùng | Stock by Lot/Expiry | Kiểm soát lô và hàng cận/hết hạn để xử lý kịp thời. | Không | Báo cáo quản trị |
| Báo cáo tồn kho tức thời theo kho–vị trí | Stock on Hand by Location | Xem tồn thực tế/khả dụng theo kho, vị trí, bin theo thời gian thực. | Không | Báo cáo quản trị |
| Báo cáo hàng cận hạn / quá hạn | Near-expiry / Expired Report | Cảnh báo lô sắp/đã hết hạn để xử lý trước khi phát sinh tổn thất. | Không | Báo cáo quản trị |
| Biên bản kiểm kê & báo cáo chênh lệch | Count & Variance Report | Ghi kết quả đếm thực tế và chênh lệch so với tồn sổ sách làm căn cứ điều chỉnh. | Có | Mẫu 05-VT; kiểm kê bắt buộc cuối năm theo Luật Kế toán |
| Báo cáo hàng chậm luân chuyển / tồn lâu | Slow-moving / Aging Report | Nhận diện hàng chết, cơ sở lập dự phòng giảm giá hàng tồn kho. | Không | Báo cáo quản trị |
| Báo cáo đề xuất bổ sung tồn | Reorder / Replenishment Report | Danh sách mặt hàng cần mua/sản xuất/chuyển theo min/max/ROP. | Không | Báo cáo quản trị |
| Bảng kê phiếu nhập / xuất | Receipt / Issue Register | Liệt kê chứng từ nhập/xuất theo kỳ để đối chiếu và kiểm toán. | Không | Báo cáo quản trị |
| Báo cáo truy xuất nguồn gốc lô / serial | Lot/Serial Traceability Report | Truy ngược/xuôi đường đi của lô, serial từ nhà cung cấp đến khách hàng. | Không | Quản trị; bắt buộc theo ngành dược/thực phẩm |
| Tồn kho & cảnh báo hết hàng đa kho/NPP | Inventory & OOS report | Điều phối hàng, phát hiện hết hàng tại kho và NPP. | Không | — |
| Tồn theo lô – hạn dùng (cận/hết HSD) | Batch / Expiry report | Quản lý FEFO, cảnh báo hàng cận và hết hạn dùng. | Không | — |
| Tồn & doanh số hàng ký gửi theo đại lý | Consignment report | Theo dõi tồn ký gửi và doanh số đã bán theo từng đại lý. | Không | — |

### LEGAL

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Sổ đăng ký đồng ý dữ liệu cá nhân | Consent register | Lưu và chứng minh sự đồng ý (ai, khi nào, mục đích, phiên bản điều khoản) và việc rút đồng ý của chủ thể dữ liệu. | Có | Luật 91/2025/QH15; Nghị định 356/2025/NĐ-CP Điều 6 [1][2] |
| Hồ sơ đánh giá tác động xử lý dữ liệu cá nhân (DPIA) | DPIA register/report | Lập và cập nhật hồ sơ DPIA (Mẫu số 10), nộp cơ quan chức năng trong 60 ngày từ khi bắt đầu xử lý, cập nhật mỗi 6 tháng/khi thay đổi. | Có | Nghị định 356/2025/NĐ-CP Điều 19-20 [2] |
| Nhật ký chuyển dữ liệu cá nhân ra nước ngoài | Cross-border transfer log/report | Ghi nhận và lập hồ sơ (Mẫu số 09) cho việc chuyển/lưu trữ dữ liệu cá nhân ở nước ngoài, nộp trong 60 ngày. | Có | Nghị định 356/2025/NĐ-CP Điều 17-18 [2] |

### MFG

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Kết quả MRP / Nhu cầu vật tư | MRP Result / Planned Orders | Xem đề xuất mua/sản xuất, cảnh báo thiếu/thừa theo mặt hàng và kỳ. | Không | Báo cáo quản trị |
| Lịch sản xuất chính | Master Production Schedule | Theo dõi kế hoạch sản xuất thành phẩm theo kỳ và dây chuyền. | Không | Báo cáo quản trị |
| Tiến độ lệnh sản xuất | Production Order Status / WIP | Theo dõi trạng thái và % hoàn thành của từng lệnh sản xuất. | Không | Báo cáo quản trị |
| Tiêu hao vật tư thực tế so với định mức | Material Consumption vs Standard (Variance) | So sánh NVL thực dùng với định mức BOM để phát hiện lãng phí. | Không | Báo cáo quản trị |
| Hiệu suất thiết bị tổng thể (OEE) | Overall Equipment Effectiveness | Đo Khả dụng × Hiệu suất × Chất lượng của thiết bị theo ca/kỳ. | Không | Báo cáo quản trị / KPI |
| Tuân thủ tiến độ | Schedule Adherence / On-time | Đo tỷ lệ lệnh sản xuất hoàn thành đúng hạn so với kế hoạch. | Không | Báo cáo quản trị / KPI |
| Phế liệu & tỷ lệ lỗi | Scrap & Defect Rate | Theo dõi phế liệu và hàng hỏng theo sản phẩm, công đoạn, nguyên nhân. | Không | Báo cáo quản trị |
| Giá thành sản xuất & chênh lệch | Production Cost / Variance | So giá thành thực tế với định mức theo thành phần chi phí; chi tiết ở module COST. | Không | Báo cáo quản trị (xem costing.md) |
| Báo cáo chất lượng (QC Pass/Fail, NCR) | Quality / NCR Report | Tổng hợp kết quả IQC/IPQC/OQC và hàng không đạt theo NCC/sản phẩm/loại lỗi. | Không | Báo cáo quản trị |
| Tải năng lực | Capacity Load / CRP | So sánh tải với công suất sẵn có của từng trung tâm làm việc theo tuần. | Không | Báo cáo quản trị |
| Tồn kho dở dang (WIP) | Work-in-Process Inventory | Theo dõi giá trị và tuổi WIP theo lệnh; phục vụ thuyết minh tồn kho BCTC (gián tiếp). | Không | Hỗ trợ BCTC theo TT99/2025 (gián tiếp) |
| Tiến độ gia công ngoài | Subcontract Status | Theo dõi NVL gửi đi gia công và bán thành phẩm/thành phẩm nhận lại theo NCC. | Không | Báo cáo quản trị |

### PAY

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Bảng thanh toán tiền lương | Payroll Sheet | Tổng hợp lương gộp, các khoản trích theo lương, khấu trừ và lương thực nhận của kỳ. | Không | Chứng từ kế toán TT 99/2025 (mẫu 02-LĐTL) |
| Phiếu lương | Payslip | Thông báo bảng kê chi tiết trả lương cho từng NLĐ mỗi kỳ trả lương. | Có | Điều 95 khoản 3 BLLĐ 45/2019 |
| Bảng kê trích nộp các khoản theo lương | Statutory Deduction Remittance Sheet | Theo dõi số trích nộp BHXH, BHYT, BHTN, KPCĐ phần NLĐ và NSDLĐ. | Không | Chứng từ kế toán TT 99/2025 (mẫu 10-LĐTL) |
| Tờ khai khấu trừ thuế TNCN tháng/quý (05/KK-TNCN) | Monthly/Quarterly PIT Withholding Declaration | Kê khai số thuế TNCN đã khấu trừ của NLĐ trong kỳ. | Có | Luật Quản lý thuế; mẫu 05/KK-TNCN |
| Tờ khai quyết toán thuế TNCN năm (05/QTT-TNCN) | Annual PIT Finalization Return | Quyết toán thuế TNCN cả năm cho NLĐ ủy quyền và xác định số nộp thừa/thiếu. | Có | Luật Quản lý thuế; mẫu 05/QTT-TNCN, 05-1/BK, 05-2/BK |
| Chứng từ khấu trừ thuế TNCN điện tử | E-withholding Tax Certificate | Cấp cho người bị khấu trừ và gửi cơ quan thuế trong ngày lập. | Có | Nghị định 254/2026/NĐ-CP |
| Hồ sơ báo tăng/giảm lao động đóng BHXH | Social Insurance Increase/Decrease Declaration | Điều chỉnh danh sách và mức đóng BHXH khi có biến động lao động, tiền lương. | Có | Luật BHXH 41/2024; NĐ 158/2025 (mẫu D02-LT ⚠️) |
| Báo cáo/quyết toán kinh phí công đoàn | Trade Union Fee Report | Theo dõi trích nộp KPCĐ 2% và quyết toán với công đoàn cấp trên. | Có | Luật Công đoàn 50/2024 |
| Bảng lương chi tiết | Payroll Register / Detail | Tính và kiểm tra lương gross→net từng NLĐ, cơ sở cho mọi báo cáo pháp định | Không | — |
| Bảng tổng hợp lương theo bộ phận / cost center | Payroll Summary by Cost Center | Phân bổ và kiểm soát chi phí lương theo bộ phận, dự án | Không | — |
| Bảng kê chuyển khoản lương | Bank Payment List | Tạo file chi lương qua ngân hàng | Không | — |
| Bảng tổng hợp & hồ sơ trích nộp BHXH/BHYT/BHTN (báo tăng/giảm, đối chiếu C12-TS) | Social Insurance Contribution Report | Trích nộp và đối chiếu bảo hiểm với cơ quan BHXH | Có | Luật BHXH 2024 / NĐ 158/2025 — xem vn-labor-payroll.md §5.3 |
| Tờ khai thuế TNCN tháng/quý (05/KK-TNCN) | Monthly/Quarterly PIT Return | Kê khai số thuế TNCN đã khấu trừ | Có | Luật Quản lý thuế — xem vn-labor-payroll.md §6.5 |
| Tờ khai quyết toán thuế TNCN năm (05/QTT-TNCN + 05-1, 05-2) | Annual PIT Finalization | Quyết toán thuế TNCN năm, doanh nghiệp quyết toán thay cá nhân ủy quyền | Có | Luật Quản lý thuế — xem vn-labor-payroll.md §6.5 |
| Báo cáo chi phí nhân công | Labor Cost Report | Quản trị chi phí nhân công, đầu vào giá thành/dự án | Không | — |

### PERF

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Báo cáo hiệu năng & giám sát hệ thống | System performance & monitoring report | Theo dõi CPU/RAM/hàng đợi/lỗi và thời gian phản hồi, cảnh báo khi vượt ngưỡng. | Không | Chính sách vận hành nội bộ |

### POS

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Doanh thu bán lẻ theo cửa hàng/ca/thu ngân | Retail Sales by Shift report | Quản trị doanh thu bán lẻ và đối soát ca. | Không | — |

### PRICE

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Hiệu quả khuyến mãi (uplift vs baseline) | Promotion Effectiveness report | Đánh giá ROI và mức tăng doanh số của chương trình KM. | Không | — |
| Quyết toán ngân sách khuyến mãi | Promotion Budget report | Theo dõi chi phí KM so với ngân sách phê duyệt. | Không | — |
| Theo dõi chương trình KM & số đăng ký/thông báo | Promotion Compliance tracker | Hỗ trợ tuân thủ pháp lý: liên kết chương trình với số thông báo/đăng ký Sở–Bộ Công Thương. | Không | NĐ 81/2018/NĐ-CP (sửa đổi) [2] |
| Lịch sử & hiệu lực bảng giá | Price List History report | Truy vết thay đổi giá và hiệu lực theo phiên bản. | Không | — |
| So sánh giá theo kênh/vùng | Price Comparison report | So sánh giá áp dụng giữa các kênh và vùng. | Không | — |

### PRJ

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Báo cáo chi phí dự án (kế hoạch/thực tế/cam kết) | Project Cost Report (Plan/Actual/Commitment) | So sánh chi phí kế hoạch, thực chi và cam kết theo WBS để kiểm soát chi phí. | Không | Quản trị nội bộ |
| Ngân sách so với thực tế | Budget vs Actual | Theo dõi mức tiêu ngân sách và cảnh báo vượt chi theo WBS/kỳ. | Không | Quản trị nội bộ |
| Báo cáo lãi lỗ dự án | Project P&L | Đo doanh thu, giá vốn, chi phí và lợi nhuận từng dự án; feed số liệu BCTC ở mức công ty. | Không | Quản trị; số liệu chảy vào BCTC theo TT99/2025 |
| Báo cáo tiến độ và mốc dự án | Project Status / Milestone Report | Theo dõi % hoàn thành, mốc đạt/trễ, rủi ro tiến độ. | Không | Quản trị nội bộ |
| Báo cáo chấm công và hiệu suất | Timesheet / Utilization Report | Phân tích giờ công, tỷ lệ billable và utilization của nguồn lực. | Không | Quản trị nội bộ |
| Báo cáo WIP và doanh thu dở dang | WIP / Revenue Recognition Report | Theo dõi chi phí dở dang (154), doanh thu POC và giá vốn; cơ sở số liệu BCTC. | Không | Quản trị; cơ sở ghi nhận doanh thu theo VAS 14/15 |
| Báo cáo tình trạng xuất hóa đơn (unbilled vs deferred) | Billing Status (Unbilled vs Deferred) | Đối soát tài sản hợp đồng (chưa xuất hóa đơn) và nợ hợp đồng (3387). | Không | Quản trị nội bộ |
| Báo cáo biên lợi nhuận và EAC | Margin / EAC Report | Dự báo kết quả khi hoàn thành và nhận diện hợp đồng lỗ. | Không | Quản trị nội bộ |
| Báo cáo nguồn lực và công suất | Resource / Capacity Report | So sánh phân bổ với công suất, phát hiện quá tải. | Không | Quản trị nội bộ |
| Nhật ký yêu cầu thay đổi | Change Request Log | Truy vết lịch sử thay đổi phạm vi, giá trị hợp đồng và ngân sách. | Không | Quản trị nội bộ |
| Dòng tiền dự án | Project Cash Flow | Theo dõi dòng thu (hóa đơn/thu tiền) và chi (PO/lương) theo dự án. | Không | Quản trị nội bộ |
| Tuổi nợ phải thu theo dự án | AR Aging by Project | Theo dõi thu hồi công nợ phải thu gắn với dự án. | Không | Quản trị; chi tiết tại ar-accounts-receivable.md |

### PROG

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Bảng giá trị khối lượng hoàn thành & đề nghị thanh toán kỳ (phiếu giá) | Interim Payment Certificate | Hồ sơ thanh toán khối lượng với chủ đầu tư | Không | Theo mẫu hợp đồng / chủ đầu tư |
| Tiến độ sản lượng kế hoạch so thực tế theo hạng mục | Planned vs Actual Progress | Điều hành tiến độ thi công | Không | — |

### PUR

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Tình hình thực hiện đơn mua hàng | Open PO / PO Status Report | Theo dõi với từng PO: đã đặt, đã nhận, đã hóa đơn, còn lại, tiến độ giao và PO quá hạn. | Không | Quản trị nội bộ |
| Công nợ phải trả nhà cung cấp | AP Aging Report | Theo dõi dư nợ và tuổi nợ phải trả theo nhà cung cấp, khoản đến hạn và theo tiền tệ. | Không | Quản trị; số liệu phục vụ thuyết minh BCTC — chi tiết ở module AP |
| Phân tích giá mua | Purchase Price Analysis / PPV | So sánh giá mua theo thời gian và theo nhà cung cấp, phát hiện chênh lệch giá giữa PO và hóa đơn. | Không | Quản trị nội bộ |
| Đánh giá nhà cung cấp | Vendor Scorecard | Chấm điểm nhà cung cấp theo tiêu chí giá, chất lượng, giao hàng, dịch vụ theo chu kỳ. | Không | Quản trị nội bộ |
| Hàng đã nhận chưa có hóa đơn | Goods Received Not Invoiced | Kiểm soát công nợ tiềm tàng và phục vụ trích trước/đối chiếu khi khóa sổ cuối kỳ. | Không | Quản trị; hỗ trợ khóa sổ |
| Đề nghị mua chưa chuyển đơn | Open Purchase Requisition | Theo dõi nhu cầu đã duyệt nhưng chưa đặt hàng, tránh bỏ sót. | Không | Quản trị nội bộ |
| Sổ chi tiết mua hàng theo NCC/mặt hàng | Purchase Detail Ledger | Tra cứu phát sinh mua theo nhà cung cấp, mặt hàng, kho và kỳ. | Không | Quản trị nội bộ |

### QHSE

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Nhật ký thi công & nghiệm thu chất lượng, sự cố an toàn | Site Diary & Quality/Safety Record | Hồ sơ pháp lý quản lý chất lượng công trình | Có | NĐ 207/2026/NĐ-CP |

### SAL

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Doanh số bán hàng | Sales Revenue Report | Theo dõi doanh số theo khách hàng, mặt hàng/nhóm hàng, nhân viên bán, khu vực, kênh, kỳ. | Không | — |
| Tình hình thực hiện đơn bán | Sales Order Fulfillment / Order Book | So sánh số đã đặt vs đã giao vs còn lại vs đã xuất hóa đơn để theo dõi tiến độ thực hiện đơn. | Không | — |
| Công nợ phải thu | Accounts Receivable / Aging | Số dư và tuổi nợ phải thu khách hàng theo hạn thanh toán và nhân viên (chi tiết tại AR). | Không | Quản trị; chi tiết nghiệp vụ ở references/processes/ar-accounts-receivable.md |
| Lãi gộp bán hàng | Gross Margin Report | Tính lãi gộp = doanh thu thuần − giá vốn, theo khách/mặt hàng/nhân viên/đơn/kỳ. | Không | — |
| Chiết khấu và khuyến mãi | Discounts and Promotions Report | Theo dõi giá trị và tỷ lệ chiết khấu/khuyến mãi đã cấp theo chương trình/khách/mặt hàng. | Không | — |
| Hoa hồng bán hàng | Sales Commission Report | Tính và theo dõi hoa hồng theo chính sách (theo hóa đơn hoặc theo tiền thu) cho từng nhân viên. | Không | — |
| Bảng kê hóa đơn bán ra | Output Invoice List | Liệt kê hóa đơn GTGT đầu ra theo kỳ/thuế suất/khách phục vụ kê khai thuế GTGT. | Không | Cung cấp dữ liệu cho tờ khai thuế GTGT và truyền dữ liệu hóa đơn tới cơ quan thuế theo ND123/2020 và ND70/2025; bản thân báo cáo nội bộ không phải mẫu luật định |
| Báo cáo Sell-in / Sell-out theo NPP, kênh, vùng | Sell-in / Sell-out report | Đo lượng hàng đẩy vào NPP và lượng bán ra thực tế thị trường. | Không | — |
| Doanh số so với chỉ tiêu theo DSR/tuyến/vùng | Sales vs Target report | Theo dõi mức độ đạt mục tiêu của đội bán hàng. | Không | — |
| Quyết toán chiết khấu/rebate theo NPP/khách | Rebate Settlement report | Chốt công nợ thưởng/chiết khấu theo doanh số. | Không | — |
| Dự chi rebate đang tích lũy (accrual) | Rebate Accrual report | Theo dõi nghĩa vụ rebate đang tích lũy chưa quyết toán. | Không | — |
| Tỷ lệ & giá trị trả hàng theo lý do/khách/SKU | Returns Analysis report | Phân tích trả hàng theo nguyên nhân để cải thiện vận hành. | Không | — |

### SEC

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Báo cáo nhật ký bảo mật & truy cập | Security & access log report | Ghi đăng nhập thành công/thất bại, đổi quyền, đổi cấu hình, truy cập dữ liệu nhạy cảm; phục vụ điều tra sự cố và tuân thủ. | Không | OWASP ASVS 5.0 [5]; PDPL (an toàn dữ liệu) [1][2] |

### SITE

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Nhập-xuất-tồn vật tư công trường & đối chiếu định mức | Site Material Movement vs Norm | Chống thất thoát vật tư công trường | Không | — |

### STL

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Quyết toán hợp đồng A-B; chênh lệch dự toán - quyết toán | Contract Final Settlement | Chốt giá trị khi kết thúc hợp đồng | Không | NĐ 210/2026 / theo hợp đồng |
| Hồ sơ quyết toán vốn đầu tư (phía chủ đầu tư) | Investment Final Account | Quyết toán dự án vốn nhà nước | Có | NĐ 206/2026/NĐ-CP; pháp luật đầu tư công |

### SUB

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Công nợ, nghiệm thu & giữ lại thầu phụ | Subcontractor Payable & Retention | Quản lý nghiệm thu và công nợ thầu phụ | Không | — |

### SVC

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Báo cáo tuân thủ SLA | SLA Compliance Report | Đo % ca đúng hạn và số ca vi phạm SLA theo mức ưu tiên/hợp đồng | Không | Báo cáo quản trị |
| Khối lượng và tồn đọng phiếu hỗ trợ | Ticket Volume & Backlog Report | Theo dõi ticket mới/đóng/tồn và tuổi ticket | Không | Báo cáo quản trị |
| Work order và năng suất kỹ thuật viên | Work Order & Technician Utilization | Số work order, giờ công, tỷ lệ sửa xong lần đầu theo kỹ thuật viên/địa bàn | Không | Báo cáo quản trị |
| Doanh thu và giá vốn dịch vụ | Service P&L Report | Phân tích lãi/lỗ mảng dịch vụ theo dịch vụ/khách/kỳ | Không | Báo cáo quản trị (dữ liệu từ GL/costing) |
| Phân tích chi phí bảo hành | Warranty Cost Analysis | Chi phí bảo hành so với doanh thu và theo dõi mức dự phòng TK 352 | Không | Báo cáo quản trị hỗ trợ lập BCTC (dự phòng theo TT99/2025) |
| Tiêu hao phụ tùng | Spare Parts Consumption Report | Thống kê phụ tùng sử dụng theo work order/serial/kho | Không | Báo cáo quản trị |
| Chỉ số hài lòng khách hàng | CSAT/NPS Report | Đo điểm hài lòng và thiện cảm sau khi xử lý yêu cầu | Không | Báo cáo quản trị |

### SYS

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Nhật ký kiểm toán (field-level) | Audit Trail Report | Tra cứu thay đổi từng trường (giá trị cũ→mới, ai, khi nào, hành động) theo bản ghi hoặc theo người/khoảng thời gian; phục vụ kiểm toán nội bộ & độc lập. | Không | P14; thời hạn lưu theo Luật Kế toán — xem vn-accounting.md |
| Lịch sử duyệt | Approval History | Hiển thị bất biến ai duyệt/từ chối/trả lại ở cấp nào, thời điểm, ý kiến cho mỗi chứng từ. | Không | P03 |
| Nhật ký gửi thông báo | Notification Delivery Log | Theo dõi trạng thái gửi/đã đọc/thất bại/thử lại của thông báo in-app, email, ZNS, SMS. | Không | P10 |
| Nhật ký tác vụ nền | Background Job Run Log | Ghi thời gian, người chạy, tham số, số bản ghi xử lý/thành công/lỗi của mỗi lần chạy job (MRP, khấu hao, kết chuyển...). | Không | P15 |
| Lịch sử nhập Excel | Import Batch Log | Theo dõi từng lô import (file, số dòng nhận/lỗi, người nhập) để truy vết và hoàn tác. | Không | P12 |
| Báo cáo đối soát tích hợp | Integration Reconciliation Report | So khớp số bản ghi/giá trị giữa hệ thống và đối tác ngoài, liệt kê chênh lệch cần xử lý. | Không | P16 |
| Dashboard & KPI theo vai trò | Role-based Dashboard | Màn tổng quan chỉ số điều hành theo vai trò, có drill-down xuống chứng từ chi tiết và áp phạm vi dữ liệu người xem. | Không | P18 |
| Ma trận phân quyền hiện hành | User-Role permission matrix | Rà soát least-privilege và cung cấp bằng chứng kiểm toán ai có quyền gì. | Không | Thông lệ kiểm soát nội bộ; ISO/IEC 27001:2022 A.5.15/A.5.18 |
| Nhật ký đăng nhập | Login audit log | Phát hiện truy cập bất thường, đăng nhập sai, nguồn IP lạ. | Không | ISO/IEC 27001:2022 A.8.15/A.8.16 |
| Vết kiểm toán thay đổi dữ liệu | Data change audit trail | Truy vết người–thời điểm–giá trị trước/sau cho mọi sửa/xóa dữ liệu nhạy cảm, nhất là kế toán. | Có | Luật Kế toán Điều 13; vn-accounting.md REGREQ-05 |
| Báo cáo xung đột phân tách nhiệm vụ (SoD) | Segregation of Duties conflict report | Liệt kê người dùng/vai trò vi phạm SoD cùng kiểm soát bù để rà soát định kỳ. | Không | Thông lệ SOX/COSO; SAP GRC; Dynamics 365 SoD |
| Báo cáo rà soát quyền định kỳ | Periodic access review report | Chứng thực lại quyền của từng người dùng theo kỳ, ghi nhận kết quả rà soát. | Không | ISO/IEC 27001:2022 A.5.18 |
| Nhật ký thay đổi tham số | Parameter change log | Ghi ai đổi tham số nào, khi nào, giá trị cũ/mới để truy vết cấu hình. | Không | Thông lệ kiểm soát thay đổi |
| Nhật ký thao tác đặc quyền | Privileged activity log | Giám sát hành vi của tài khoản quản trị/đặc quyền. | Không | ISO/IEC 27001:2022 A.8.2 |

### TAX

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Tờ khai thuế giá trị gia tăng (mẫu 01/GTGT) | VAT Return | Kê khai thuế GTGT theo tháng/quý, xác định số thuế phải nộp hoặc được khấu trừ chuyển kỳ sau. | Có | TT 89/2026/TT-BTC (nền TT 80/2021/TT-BTC); Luật 48/2024 |
| Bảng kê hóa đơn, chứng từ hàng hóa dịch vụ bán ra | Output invoice listing | Liệt kê hóa đơn đầu ra làm căn cứ lập tờ khai GTGT và đối chiếu doanh thu. | Có | TT 89/2026/TT-BTC |
| Bảng kê hóa đơn, chứng từ hàng hóa dịch vụ mua vào | Input invoice listing | Liệt kê hóa đơn đầu vào, xác định thuế GTGT được khấu trừ và kiểm soát điều kiện thanh toán không dùng tiền mặt. | Có | TT 89/2026/TT-BTC |
| Tờ khai quyết toán thuế thu nhập doanh nghiệp | CIT finalization return | Quyết toán thuế TNDN năm, điều chỉnh chênh lệch kế toán-thuế, chuyển lỗ. | Có | Luật 67/2025/QH15; NĐ 320/2025; TT 89/2026 |
| Bảng tổng hợp dữ liệu hóa đơn điện tử (mẫu 01/TH-HĐĐT) | E-invoice data summary | Chuyển dữ liệu hóa đơn không mã theo kỳ cho các ngành đặc thù (viễn thông, ngân hàng, bảo hiểm, hàng không, chứng khoán, điện, nước). | Có | NĐ 254/2026/NĐ-CP; TT 91/2026/TT-BTC |
| Thông báo hóa đơn điện tử có sai sót (mẫu 04/SS-HĐĐT) | E-invoice error notification | Thông báo cơ quan thuế về hóa đơn đã lập có sai sót nhỏ hoặc đã xử lý điều chỉnh/thay thế. | Có | TT 91/2026/TT-BTC (Phụ lục III); nền NĐ 70/2025 |
| Báo cáo chi phí không được trừ khi tính thuế TNDN | Non-deductible expense report | Tổng hợp các khoản chi không đủ điều kiện được trừ phục vụ quyết toán TNDN. | Không | Luật 67/2025 Điều 9 |
| Báo cáo rà soát hóa đơn mua từ 5 triệu chưa có chứng từ thanh toán không dùng tiền mặt | Non-cash payment compliance report | Phát hiện hóa đơn đầu vào có rủi ro bị loại khấu trừ GTGT/chi phí TNDN khi đến hạn thanh toán. | Không | Điều 14 Luật 48/2024; Điều 26 NĐ 181/2025; Điều 9 Luật 67/2025 |
| Bảng kê hóa đơn hàng hóa dịch vụ bán ra | Output invoice listing | Tổng hợp hóa đơn đầu ra làm căn cứ lập tờ khai và đối chiếu doanh thu – thuế đầu ra. | Không | Nội bộ/đối chiếu; không nộp kèm 01/GTGT theo khung TT 89/2026 (bãi bỏ từ TT 80/2021) |
| Bảng kê hóa đơn hàng hóa dịch vụ mua vào | Input invoice listing | Tổng hợp hóa đơn đầu vào và thuế GTGT được khấu trừ, gắn cờ khấu trừ và người bán rủi ro. | Không | Nội bộ/đối chiếu |
| Tờ khai thuế GTGT mẫu 01/GTGT | VAT return (form 01/GTGT) | Khai thuế GTGT theo phương pháp khấu trừ theo kỳ tháng/quý, nộp cơ quan thuế. | Có | TT 89/2026 (nền TT 80/2021); xem vn-tax-einvoice.md §2.6 |
| Sổ theo dõi phát hành hóa đơn | Invoice issuance register | Theo dõi số hóa đơn đã phát hành theo ký hiệu, phát hiện trùng/ngắt quãng (gap). | Không | Nội bộ kiểm soát |
| Báo cáo đối chiếu doanh thu 511 với thuế GTGT đầu ra 33311 | Revenue vs output VAT reconciliation | Kiểm soát khớp giữa doanh thu ghi nhận và thuế đầu ra đã kê khai. | Không | Nội bộ kiểm soát |
| Báo cáo đối chiếu thuế GTGT đầu vào 133 với bảng kê | Input VAT (133) reconciliation | Kiểm soát khớp số thuế đầu vào khấu trừ giữa sổ cái và bảng kê. | Không | Nội bộ kiểm soát |
| Danh sách hóa đơn sai sót và điều chỉnh/thay thế | Error and adjustment/replacement invoice list | Theo dõi xử lý hóa đơn sai sót, quan hệ cha–con hóa đơn gốc với điều chỉnh/thay thế. | Không | Nội bộ |
| Báo cáo hóa đơn từ người bán rủi ro | Risky-seller invoice report | Cảnh báo hóa đơn đầu vào từ doanh nghiệp rủi ro/bỏ trốn ảnh hưởng khấu trừ và chi phí. | Không | Nội bộ kiểm soát; danh sách rủi ro cơ quan thuế |
| Bảng kê chi phí không được trừ (TNDN) | Non-deductible expense listing | Chuẩn bị quyết toán TNDN: tổng hợp chi phí không được trừ theo lý do. | Không | Căn cứ 03/TNDN |
| Dữ liệu tờ khai quyết toán thuế TNDN mẫu 03/TNDN | CIT finalization data (form 03/TNDN) | Quyết toán thuế TNDN năm, gồm điều chỉnh thu nhập và lỗ chuyển. | Có | Luật 67/2025, NĐ 320/2025, TT 89/2026 |
| Bảng tổng hợp dữ liệu hóa đơn điện tử | E-invoice data summary table | Chuyển dữ liệu hóa đơn không mã theo kỳ cho ngành đặc thù. | Có | NĐ 254/2026, TT 91/2026 (ngành đặc thù dùng hóa đơn không mã) |
| Báo cáo hóa đơn từ 5 triệu chưa có chứng từ thanh toán không dùng tiền mặt | Non-cash payment monitoring report | Kiểm soát điều kiện khấu trừ GTGT/chi phí TNDN khi hóa đơn trả chậm đến hạn. | Không | Nội bộ kiểm soát; Luật 48/2024 Đ14, NĐ 181/2025 |
| Bảng kê chứng từ khấu trừ thuế TNCN đã cấp | PIT withholding voucher register | Quản lý chứng từ khấu trừ thuế TNCN điện tử đã phát hành theo người nhận thu nhập. | Không | Căn cứ quyết toán TNCN; xem hr-payroll.md |

### TMS

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Hiệu suất đội xe và chi phí trên km | Fleet utilization & cost per km | Tối ưu đội xe, kiểm soát chi phí nhiên liệu/chuyến. | Không | Chuyến và chi phí chuyến |
| Giao đúng hạn và POD tồn đọng | On-time delivery & pending POD | Đo chất lượng giao hàng và tình trạng thu hồi chứng từ POD. | Không | Chuyến và POD |

### WMS

| Báo cáo | Tiếng Anh | Mục đích | Bắt buộc theo luật | Căn cứ |
|---|---|---|---|---|
| Tồn kho theo chủ hàng | Inventory by owner | Báo cáo tồn cho từng khách hàng 3PL (hàng giữ hộ, ngoài bảng TK 002). | Không | TK 002 và tồn chi tiết theo chủ hàng; theo hợp đồng 3PL |
| Năng suất kho và độ chính xác tồn | Warehouse productivity & inventory accuracy | Đo dock-to-stock, fill rate, năng suất soạn hàng, sai lệch kiểm kê. | Không | Giao dịch kho và cycle count |
