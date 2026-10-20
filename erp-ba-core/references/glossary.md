# Thuật ngữ ERP Việt – Anh

Một khái niệm = một tên. Dự án dùng tên khách hàng quen dùng và ghi ánh xạ sang tên chuẩn ở đây vào `catalogs/glossary.md` của dự án.

## Mục lục
1. Tài chính – kế toán – thuế – tiền – tài sản – giá thành – ngân sách
2. Thuật ngữ ngành: xây dựng, logistics, thương mại – phân phối
3. Chuỗi cung ứng – mua bán – kho – sản xuất – dự án – CRM – nhân sự
4. ERP tổng quát, hệ thống, BA & triển khai (gồm thuật ngữ từ 4 cuốn sách)

## Tài chính – kế toán – thuế – tiền – tài sản – giá thành – ngân sách

> Phạm vi: GL (kế toán tổng hợp), AP (công nợ phải trả), AR (công nợ phải thu), CB (tiền – ngân hàng), FA (tài sản cố định), TAX (thuế & hóa đơn điện tử), COST (giá thành & định giá tồn kho), BUD (ngân sách), và thuật ngữ chế độ/quy định kế toán.
> Chuẩn áp dụng (hiệu lực 2026-10-20): **Thông tư 99/2025/TT-BTC** (thay TT200/2014 từ 01/01/2026); doanh nghiệp nhỏ và vừa có thể vẫn dùng **TT133/2016** (nêu khác biệt khi trọng yếu). Số hiệu tài khoản trong file theo TT99/2025. "Xem thêm" dẫn tới file tham chiếu (và § nếu hữu ích) nơi giải thích khái niệm. Một khái niệm = một thuật ngữ ưu tiên; đồng nghĩa ghi ở cột "Tên khác".

### Chế độ, chuẩn mực & nguyên tắc kế toán (Accounting regime, standards & principles)

| Thuật ngữ (VI) | Tiếng Anh | Viết tắt | Tên khác / tên khách hàng hay dùng | Định nghĩa ngắn | Module | Xem thêm |
|---|---|---|---|---|---|---|
| Báo cáo kết quả hoạt động kinh doanh | Income Statement | B02-DN | Báo cáo lãi lỗ, P&L | Báo cáo phản ánh doanh thu, chi phí và kết quả lãi/lỗ trong kỳ. | GL | regulations/vn-accounting.md §7 |
| Báo cáo lưu chuyển tiền tệ | Cash Flow Statement | B03-DN | Báo cáo dòng tiền, LCTT | Báo cáo dòng tiền từ hoạt động kinh doanh, đầu tư và tài chính; lập theo phương pháp trực tiếp hoặc gián tiếp. | GL | regulations/vn-accounting.md §7 |
| Báo cáo tài chính | Financial Statements | BCTC | — | Bộ báo cáo tổng hợp tình hình tài chính, kết quả kinh doanh và dòng tiền; theo TT99 gồm B01, B02, B03, B09 (và bộ B01-DNKLT…B09-DNKLT cho đơn vị không hoạt động liên tục). | GL | regulations/vn-accounting.md §7 |
| Báo cáo tình hình tài chính | Statement of Financial Position | B01-DN | **Bảng cân đối kế toán** (tên cũ TT200) | Báo cáo phản ánh tài sản, nợ phải trả và vốn chủ sở hữu tại một thời điểm; TT99 đổi tên từ "Bảng cân đối kế toán". | GL | regulations/vn-accounting.md §7 |
| Bản thuyết minh báo cáo tài chính | Notes to the Financial Statements | B09-DN | Thuyết minh BCTC | Bản thuyết minh chính sách kế toán áp dụng và chi tiết các chỉ tiêu trên BCTC. | GL | regulations/vn-accounting.md §7 |
| Chế độ kế toán doanh nghiệp | Enterprise Accounting Regime | — | Chế độ kế toán | Bộ quy định hướng dẫn hạch toán (tài khoản, chứng từ, sổ, BCTC); hiện hành TT99/2025 cho DN, TT133/2016 cho SME, TT58/2026 cho DN siêu nhỏ. | GL | regulations/vn-accounting.md §2 |
| Chi phí | Expense | — | — | Giá trị nguồn lực tiêu hao để tạo ra doanh thu trong kỳ (tài khoản loại 6, 8); ghi nhận theo cơ sở dồn tích và nguyên tắc phù hợp. | GL | regulations/vn-accounting.md §4 |
| Chuẩn mực báo cáo tài chính quốc tế | International Financial Reporting Standards | IFRS | — | Hệ chuẩn mực quốc tế; VN áp dụng theo lộ trình QĐ 345/QĐ-BTC (tự nguyện rồi bắt buộc cho DN niêm yết/DNNN lớn/FDI); đa số DN vẫn dùng VAS + TT99 làm nền. | GL | regulations/vn-accounting.md §8 |
| Chuẩn mực kế toán Việt Nam | Vietnamese Accounting Standards | VAS | — | Hệ thống 26 chuẩn mực (số 01–30, bỏ 09/12/13/20) quy định nguyên tắc ghi nhận, đo lường và trình bày. | GL | regulations/vn-accounting.md §8 |
| Chứng từ điện tử | Electronic Voucher | — | Chứng từ số | Chứng từ ở dạng dữ liệu điện tử, có giá trị như chứng từ giấy khi thể hiện đầy đủ, tra cứu được trong suốt thời hạn lưu trữ và được ký điện tử hợp lệ. | GL | regulations/vn-accounting.md §5.3 |
| Chứng từ kế toán | Accounting Voucher | — | Chứng từ gốc, source document | Giấy tờ/dữ liệu phản ánh nghiệp vụ kinh tế làm căn cứ ghi sổ; phải đủ nội dung bắt buộc theo Điều 16 Luật Kế toán. | GL | regulations/vn-accounting.md §5 |
| Chữ ký số | Digital Signature | CKS | Chữ ký điện tử | Chữ ký điện tử dùng thuật toán khóa không đối xứng, bảo đảm xác thực, toàn vẹn và chống chối bỏ; dùng cho chứng từ kế toán và hóa đơn điện tử (ký chậm nhất ngày làm việc kế tiếp). | GL | regulations/vn-accounting.md §5.3 |
| Cơ sở dồn tích | Accrual Basis | — | Kế toán dồn tích | Nguyên tắc ghi nhận nghiệp vụ tại thời điểm phát sinh, không căn cứ thời điểm thu/chi tiền (VAS 01). | GL | regulations/vn-accounting.md §8 |
| Doanh thu | Revenue | — | — | Tổng giá trị lợi ích kinh tế thu được từ bán hàng, cung cấp dịch vụ và hoạt động khác (TK 511, 515, 711); ghi nhận theo điều kiện VAS 14. | GL | regulations/vn-accounting.md §8 |
| Dự phòng | Provision / Allowance | — | Trích lập dự phòng | Khoản ước tính trước tổn thất: giảm giá hàng tồn kho, nợ phải thu khó đòi, tổn thất đầu tư, bảo hành (TT48/2019; TK 229, 352). | GL | regulations/vn-accounting.md §11 |
| Đồng tiền hạch toán | Functional (Accounting) Currency | — | Đồng tiền ghi sổ, local currency | Đơn vị tiền tệ kế toán của pháp nhân (VND tại VN); DN thu chi chủ yếu ngoại tệ có thể chọn 1 ngoại tệ ghi sổ nhưng phải quy đổi VND khi lập BCTC (Luật KT Điều 10). | GL | regulations/vn-accounting.md §3 |
| Ghi sổ kép | Double-entry | — | Bút toán kép | Nguyên tắc mỗi nghiệp vụ được ghi đồng thời bên Nợ và bên Có với tổng tiền bằng nhau. | GL | processes/r2r-general-ledger.md §7 |
| Hệ thống tài khoản | Chart of Accounts | COA / CoA | Danh mục tài khoản, hệ thống TK chuẩn | Danh mục mã số tài khoản dùng để phân loại và ghi nhận nghiệp vụ; mặc định theo Phụ lục II TT99/2025, DN được mở thêm TK chi tiết không sai bản chất TK cấp 1. | GL | regulations/vn-accounting.md §4 |
| Hình thức kế toán | Bookkeeping Form | — | Hình thức sổ kế toán | Cách tổ chức hệ thống sổ: Nhật ký chung, Nhật ký–Sổ Cái, Chứng từ ghi sổ, Nhật ký–Chứng từ, hoặc Kế toán trên máy vi tính; ERP thuộc nhóm trên máy theo logic Nhật ký chung. | GL | regulations/vn-accounting.md §6 |
| Hoạt động liên tục | Going Concern | — | — | Giả định DN tiếp tục hoạt động bình thường trong tương lai gần; chi phối cách phân loại và đo lường trên BCTC (VAS 01). | GL | regulations/vn-accounting.md §8 |
| Kế toán trưởng | Chief Accountant | KTT | — | Người đứng đầu bộ máy kế toán; phải có chứng chỉ bồi dưỡng KTT và kinh nghiệm theo NĐ174; là cấp duyệt cấu hình hạch toán và khóa sổ. | GL | regulations/vn-accounting.md §3 |
| Kiểm soát nội bộ | Internal Control | KSNB | — | Quy trình bảo đảm hợp lý về hiệu quả vận hành, độ tin cậy báo cáo tài chính và tuân thủ pháp luật (khung COSO); trong ERP gồm phân quyền, SoD, hạn mức duyệt, audit trail. | Chung | security-and-parameters.md |
| Kỳ kế toán | Accounting Period | — | Kỳ sổ | Khoảng thời gian lập sổ và chốt số liệu: tháng, quý hoặc năm. | GL | regulations/vn-accounting.md §3 |
| Lưu trữ tài liệu kế toán | Accounting Records Retention | — | Thời hạn lưu trữ | Nghĩa vụ lưu chứng từ, sổ, BCTC tối thiểu 5 năm / 10 năm / vĩnh viễn theo loại (NĐ174); cấm hủy trước hạn, lưu điện tử phải tra cứu được suốt thời hạn. | GL | regulations/vn-accounting.md §14 |
| Năm tài chính | Fiscal Year | FY | Niên độ kế toán | Kỳ kế toán năm 12 tháng, theo năm dương lịch hoặc năm riêng của DN (ví dụ 01/4–31/3). | GL | regulations/vn-accounting.md §3 |
| Nguyên tắc giá gốc | Historical Cost Principle | — | — | Tài sản được ghi nhận theo chi phí thực tế tại thời điểm phát sinh, không ghi theo giá thị trường trừ khi pháp luật cho phép đánh giá lại (VAS 01). | GL | regulations/vn-accounting.md §8 |
| Nợ phải trả | Liabilities | — | — | Nghĩa vụ hiện tại của DN phát sinh từ giao dịch quá khứ mà DN phải thanh toán bằng nguồn lực (tài khoản loại 3). | GL | regulations/vn-accounting.md §4 |
| Phân hệ tài chính | Finance Module | — | Phân hệ kế toán – tài chính | Nhóm phân hệ lõi của ERP: kế toán tài chính, kế toán quản trị/kiểm soát chi phí, quản lý ngân quỹ, đầu tư, lập kế hoạch & dự báo; là "pool" trung tâm nhận bút toán từ mọi phân hệ. | Chung | SKILL.md |
| Sổ kế toán | Accounting Book | — | — | Sổ ghi chép và hệ thống hóa nghiệp vụ theo thời gian và theo tài khoản; mở theo kỳ, ghi liên tục, khóa cuối kỳ (Sổ Nhật ký chung, Sổ Cái, sổ chi tiết, Bảng cân đối số phát sinh là bắt buộc tối thiểu). | GL | regulations/vn-accounting.md §6 |
| Sửa chữa sổ kế toán | Accounting-record Correction | — | — | Việc chỉnh sai số liệu đã ghi; không được tẩy xóa làm mất dấu vết, dùng 1 trong 3 cách: ghi cải chính, ghi số âm (ghi đỏ), ghi bổ sung (Luật KT Điều 27). | GL | regulations/vn-accounting.md §3 |
| Tài khoản kế toán | Ledger Account | TK | — | Đơn vị phân loại để ghi nhận và theo dõi một đối tượng kế toán; có số hiệu, cấp, tính chất Nợ/Có, cờ cho ghi sổ (lá) hay tổng hợp (cha). Chỉ ghi sổ vào TK chi tiết. | GL | processes/r2r-general-ledger.md §3 |
| Tài sản | Assets | — | — | Nguồn lực do DN kiểm soát, dự tính mang lại lợi ích kinh tế tương lai (tài khoản loại 1 – ngắn hạn, loại 2 – dài hạn). | GL | regulations/vn-accounting.md §4 |
| Vốn chủ sở hữu | Owners' Equity | — | Nguồn vốn chủ sở hữu | Phần còn lại của tài sản sau khi trừ nợ phải trả (tài khoản loại 4): vốn góp, các quỹ, lợi nhuận chưa phân phối. | GL | regulations/vn-accounting.md §4 |

### Kế toán tổng hợp & sổ sách (General Ledger / Record-to-Report)

| Thuật ngữ (VI) | Tiếng Anh | Viết tắt | Tên khác / tên khách hàng hay dùng | Định nghĩa ngắn | Module | Xem thêm |
|---|---|---|---|---|---|---|
| Ánh xạ chỉ tiêu báo cáo tài chính | FS Line Mapping | — | Map chỉ tiêu BCTC | Bảng cấu hình gộp số dư/phát sinh của các tài khoản vào từng mã chỉ tiêu B01/B02/B03; phải rà lại khi đổi chế độ kế toán. | GL | processes/r2r-general-ledger.md §3 |
| Bảng cân đối số phát sinh | Trial Balance | TB | Bảng cân đối tài khoản | Bảng tổng hợp số dư đầu kỳ, phát sinh Nợ/Có và số dư cuối kỳ của mọi tài khoản để kiểm tra cân đối (mẫu S06-DN). | GL | processes/r2r-general-ledger.md §4 |
| Bỏ ghi sổ | Unpost | — | Hủy ghi sổ | Đưa chứng từ đã ghi sổ trở lại trạng thái Nháp để sửa; chỉ cho phép khi kỳ còn mở và chưa dùng cho báo cáo đã phát hành. | GL | design-patterns.md |
| Bút toán | Journal Entry | JE | Định khoản | Một ghi chép kế toán với cặp Nợ–Có cân bằng phản ánh nghiệp vụ. | GL | processes/r2r-general-ledger.md §4 |
| Bút toán điều chỉnh | Adjusting Entry | — | Bút toán điều chỉnh cuối kỳ | Bút toán cuối kỳ ghi trích trước, phân bổ, dồn tích, ước tính để số liệu phản ánh đúng kỳ trước khi lập BCTC. | GL | processes/r2r-general-ledger.md §5 |
| Bút toán định kỳ | Recurring Entry | — | Bút toán lặp | Bút toán lặp lại theo kỳ sinh từ mẫu, dùng cho trích trước (335), phân bổ chi phí chờ phân bổ (242). | GL | processes/r2r-general-ledger.md §4 |
| Bút toán đảo | Reversal | — | Đảo bút toán, bút toán ngược | Bút toán ngược dấu (đổi Nợ↔Có hoặc ghi âm) để hủy hiệu lực chứng từ đã ghi sổ mà vẫn giữ dấu vết, tham chiếu chứng từ gốc; không xóa gốc. | GL | design-patterns.md |
| Bút toán tự động từ phân hệ | Auto-posting (Subledger Integration) | — | Tích hợp sổ phụ – sổ cái | Bút toán hệ thống tự sinh và đẩy từ AP/AR/CB/INV/FA/PAY vào sổ cái theo quy tắc định khoản khi ghi sổ chứng từ nguồn. | GL | processes/r2r-general-ledger.md §4 |
| Chênh lệch tỷ giá hối đoái | Exchange Rate Difference | FX diff | Lãi/lỗ tỷ giá | Chênh lệch phát sinh khi thanh toán hoặc đánh giá lại khoản mục tiền tệ gốc ngoại tệ; theo dõi qua TK 413 rồi kết chuyển 515 (lãi)/635 (lỗ). | GL | regulations/vn-accounting.md §12 |
| Chiều phân tích | Accounting Dimension | — | Đối tượng kế toán, chiều quản trị | Thuộc tính phân loại bút toán: phòng ban, trung tâm chi phí, công trình/dự án, hợp đồng, đối tác, vật tư, khoản mục; cấu hình chiều bắt buộc theo nhóm TK. | GL | processes/r2r-general-ledger.md §3 |
| Chuyển đổi dữ liệu | Data Migration | — | Nạp số dư đầu, go-live data | Nạp số dư và dữ liệu lịch sử từ hệ thống cũ sang ERP, dùng tài khoản treo trung gian cân về 0; cần đối chiếu khớp trước khi go-live. | GL | processes/r2r-general-ledger.md §4 |
| Công trình | Project / Job | — | Dự án, đối tượng tập hợp | Đối tượng tập hợp chi phí và doanh thu theo dự án/công trình, đặc biệt trong xây lắp; là một chiều phân tích. | GL | processes/r2r-general-ledger.md §3 |
| Dấu vết kiểm toán | Audit Trail | — | Vết kiểm toán, nhật ký thay đổi | Nhật ký không sửa được ghi ai/khi nào/giá trị trước–sau của mọi thay đổi dữ liệu kế toán; là NFR bắt buộc theo Luật KT. | Chung | security-and-parameters.md |
| Định khoản | Journalizing | — | Hạch toán, lên bút toán | Việc xác định tài khoản Nợ và tài khoản Có cho một nghiệp vụ. | GL | processes/r2r-general-ledger.md §8 |
| Định khoản tự động | Account Determination | — | Posting rules, quy tắc sinh bút toán | Bảng cấu hình ánh xạ dữ liệu nghiệp vụ (nhóm vật tư/khách/kho/thuế) → cặp tài khoản Nợ/Có để hệ thống tự sinh bút toán; phải được KTT duyệt. | GL | processes/r2r-general-ledger.md §3 |
| Đánh giá lại ngoại tệ | Foreign Currency Revaluation | FX reval | Đánh giá lại tỷ giá cuối kỳ | Quy đổi lại số dư gốc ngoại tệ của khoản mục tiền tệ cuối kỳ theo tỷ giá hiện hành; chênh lệch ghi qua TK 413 rồi 515/635. | GL | regulations/vn-accounting.md §12 |
| Ghi sổ | Posting | — | Post, hạch toán vào sổ | Thao tác đưa chứng từ/bút toán vào sổ kế toán chính thức; sau khi POSTED không được xóa, chỉ Bỏ ghi sổ (kỳ mở) hoặc Đảo/điều chỉnh. | GL | processes/r2r-general-ledger.md §6 |
| Hợp nhất báo cáo | Consolidation | — | BCTC hợp nhất | Gộp BCTC các đơn vị trong tập đoàn và loại trừ giao dịch/số dư nội bộ (VAS 25). | GL | processes/r2r-general-ledger.md §12 |
| Kết chuyển | Closing Entry | — | Bút toán kết chuyển | Bút toán cuối kỳ chuyển doanh thu, chi phí sang TK 911 để xác định kết quả, rồi chuyển lãi/lỗ sang TK 421. | GL | regulations/vn-accounting.md §13 |
| Khóa kỳ / Khóa sổ | Period Lock / Period Close | — | Đóng kỳ, chốt sổ | Chốt số liệu một kỳ kế toán, chặn ghi/sửa vào kỳ đã khóa (có thể khóa riêng từng phân hệ); mở lại phải có phê duyệt và lưu vết. | GL | processes/r2r-general-ledger.md §6 |
| Loại chứng từ / Sổ nhật ký | Document Type / Journal | — | Journal, sổ nhật ký nguồn | Phân loại chứng từ theo nguồn (phiếu kế toán, kết chuyển, phân bổ, auto-post AP/AR…) với tiền tố và dải số riêng để truy vết và đánh số liên tục. | GL | processes/r2r-general-ledger.md §3 |
| Lợi nhuận sau thuế chưa phân phối | Retained Earnings | — | Lãi chưa phân phối | TK 421 phản ánh lợi nhuận tích lũy chưa phân phối (4211 năm trước, 4212 năm nay). | GL | processes/r2r-general-ledger.md §5 |
| Ngày hạch toán | Posting Date | — | Ngày ghi sổ | Ngày quyết định chứng từ thuộc kỳ kế toán nào; phải nằm trong kỳ đang mở (phân biệt với ngày chứng từ). | GL | design-patterns.md |
| Nhật ký chung | General Journal | — | Sổ Nhật ký chung (S03a-DN) | Sổ ghi toàn bộ bút toán theo trình tự thời gian rồi vào Sổ Cái; là hình thức ghi sổ chuẩn cho ERP. | GL | regulations/vn-accounting.md §6 |
| Nợ / Có | Debit / Credit | Dr / Cr | Bên Nợ / bên Có | Hai vế của mỗi bút toán kép; quy ước ghi tăng/giảm tùy tính chất tài khoản (tài sản & chi phí tăng bên Nợ; nguồn vốn, nợ phải trả & doanh thu tăng bên Có). | GL | processes/r2r-general-ledger.md §7 |
| Phải thu / phải trả nội bộ | Intercompany Receivable/Payable | IC | Công nợ nội bộ | Công nợ giữa các đơn vị trong cùng tập đoàn/pháp nhân, theo dõi trên TK 136/336; bị loại trừ khi hợp nhất. | GL | processes/r2r-general-ledger.md §12 |
| Phân bổ | Allocation (Distribution) | — | Phân bổ chi phí | Phân chia chi phí hoặc giá trị cho nhiều đối tượng/chiều phân tích theo tiêu thức định trước (hệ số, doanh thu, diện tích…). | GL | processes/r2r-general-ledger.md §4 |
| Phiếu kế toán | Journal Voucher | JV | Phiếu hạch toán, bút toán thủ công | Chứng từ ghi bút toán thủ công vào sổ cái cho nghiệp vụ không thuộc phân hệ con (điều chỉnh, trích lập, phân loại lại). | GL | processes/r2r-general-ledger.md §4 |
| Quy trình ghi nhận đến báo cáo | Record-to-Report | R2R | Chu trình đóng sổ | Quy trình từ ghi nhận giao dịch kế toán đến khóa sổ và lập báo cáo tài chính. | GL | processes/r2r-general-ledger.md §1 |
| Số dư đầu kỳ | Opening Balance | OB | Số dư go-live, chuyển số dư | Số dư tài khoản tại đầu kỳ hoặc thời điểm go-live; cuối năm được chuyển sang năm sau (carry-forward), 4212 → 4211. | GL | processes/r2r-general-ledger.md §5 |
| Sổ Cái | General Ledger | GL | Sổ Cái tài khoản (S03b-DN) | Sổ tổng hợp số phát sinh và số dư của từng tài khoản. | GL | regulations/vn-accounting.md §6 |
| Sổ chi tiết tài khoản | Account Detail Ledger | — | Sổ chi tiết | Sổ theo dõi phát sinh chi tiết theo đối tượng/chiều phân tích của một tài khoản. | GL | processes/r2r-general-ledger.md §11 |
| Sổ con | Subledger | — | Sổ phụ | Sổ chi tiết của phân hệ (AP/AR/kho/TSCĐ) sinh bút toán rồi đẩy sang sổ cái; số dư phải đối chiếu khớp với tài khoản đối ứng công nợ trên GL. | GL | processes/r2r-general-ledger.md §5 |
| Tách biệt chức năng | Segregation of Duties | SoD | Phân tách nhiệm vụ, phân tách trách nhiệm | Phân tách các quyền nhập – duyệt – ghi sổ – khóa kỳ (và giữ tiền – ghi sổ) cho các cá nhân khác nhau để ngừa gian lận, sai sót; ERP tự dò xung đột. | Chung | security-and-parameters.md |
| Trung tâm chi phí | Cost Center | CC | Bộ phận chịu chi phí | Đơn vị tổ chức dùng để tập hợp chi phí phục vụ quản trị; là chiều lập/kiểm soát ngân sách và xác định TK chi phí cho khấu hao. | GL | processes/r2r-general-ledger.md §3 |
| Tỷ giá giao dịch thực tế | Actual Transaction Exchange Rate | — | Tỷ giá thực tế | Tỷ giá quy đổi nghiệp vụ ngoại tệ tại ngày phát sinh (tỷ giá mua/bán của NHTM theo loại khoản mục); được dùng tỷ giá xấp xỉ nếu chênh lệch không trọng yếu. | GL | regulations/vn-accounting.md §12 |
| Tỷ giá hối đoái | Exchange Rate | FX rate | Tỷ giá | Tỷ lệ quy đổi nguyên tệ sang đồng tiền hạch toán; là tham số có ngày hiệu lực, hỗ trợ nhiều loại (mua/bán/bình quân/cuối kỳ). | GL | processes/r2r-general-ledger.md §3 |
| Xác định kết quả kinh doanh | Income Summary | — | Kết quả kinh doanh | TK 911 tổng hợp doanh thu trừ chi phí để xác định lãi/lỗ trong kỳ, cuối kỳ kết chuyển sang 421. | GL | regulations/vn-accounting.md §13 |

### Công nợ phải trả (Accounts Payable)

| Thuật ngữ (VI) | Tiếng Anh | Viết tắt | Tên khác / tên khách hàng hay dùng | Định nghĩa ngắn | Module | Xem thêm |
|---|---|---|---|---|---|---|
| Công nợ phải trả | Accounts Payable | AP | Phải trả người bán | Nghĩa vụ phải trả nhà cung cấp do mua hàng hóa, dịch vụ chưa thanh toán; theo dõi trên TK 331 theo từng đối tượng. | AP | processes/ap-accounts-payable.md §8 |
| Đối chiếu ba chiều | Three-way Match | — | Đối chiếu 3 bên, 3-way matching | So khớp Đơn mua hàng (PO) – Phiếu nhập kho (GRN) – Hóa đơn mua về người bán, số lượng, giá trị, thuế suất trong dung sai trước khi duyệt thanh toán. | AP | processes/ap-accounts-payable.md §7 |
| Giấy báo Nợ | Debit Note | — | — | Chứng từ giảm công nợ phải trả do trả lại hàng mua hoặc được nhà cung cấp giảm giá. | AP | processes/ap-accounts-payable.md §4 |
| Giữ thanh toán khi lệch đối chiếu | Hold on Mismatch | — | Treo thanh toán | Việc hệ thống giữ/treo chứng từ thanh toán khi lệch đối chiếu giá/số lượng vượt dung sai cho phép. | AP | security-and-parameters.md |
| Hóa đơn mua hàng | Vendor Invoice (Bill) | — | Hóa đơn đầu vào, hóa đơn NCC | Chứng từ ghi nhận nghĩa vụ phải trả và thuế GTGT đầu vào; đối chiếu với PO/GRN trước khi ghi sổ. | AP | processes/ap-accounts-payable.md §4 |
| Nhà cung cấp | Vendor (Supplier) | NCC | Nhà cung ứng | Đối tác bán hàng hóa, dịch vụ cho DN; đối tượng theo dõi công nợ phải trả. | AP | processes/ap-accounts-payable.md §3 |
| Phiếu nhập kho | Goods Receipt Note | GRN | Phiếu nhập, biên bản giao nhận | Chứng từ xác nhận thực nhận hàng, làm cơ sở đối chiếu ba chiều và ghi tăng kho / GR-IR (định nghĩa chi tiết thuộc phân hệ kho). | AP | processes/ap-accounts-payable.md §4 |
| Tài khoản trung gian hàng – hóa đơn | Goods Received / Invoice Received | GR/IR | TK chờ hóa đơn | TK trung gian theo dõi lệch thời điểm giữa nhận hàng và nhận hóa đơn; phải tất toán khi đủ cặp hàng–hóa đơn. | AP | processes/ap-accounts-payable.md §8 |
| Tạm ứng nhà cung cấp | Vendor Advance (Down Payment) | — | Trả trước người bán | Khoản trả trước cho NCC trước khi nhận hàng/hóa đơn; dư Nợ 331, cấn trừ khi có hóa đơn. | AP | processes/ap-accounts-payable.md §8 |
| Thuế nhà thầu | Foreign Contractor Tax | FCT | Thuế nhà thầu nước ngoài | Thuế áp với nhà cung cấp nước ngoài có thu nhập phát sinh tại VN, thường khấu trừ tại nguồn khi thanh toán. | AP | processes/ap-accounts-payable.md §8 |

### Công nợ phải thu (Accounts Receivable)

| Thuật ngữ (VI) | Tiếng Anh | Viết tắt | Tên khác / tên khách hàng hay dùng | Định nghĩa ngắn | Module | Xem thêm |
|---|---|---|---|---|---|---|
| Chiết khấu thương mại | Trade Discount | — | Giảm giá theo doanh số | Giảm giá cho khách theo doanh số/chính sách; là khoản giảm trừ doanh thu (TK 5211) kèm giảm thuế GTGT đầu ra. Với TT133, ghi giảm trực tiếp vào 511 (không có 521). | AR | processes/ar-accounts-receivable.md §8 |
| Công nợ phải thu | Accounts Receivable | AR | Phải thu khách hàng | Quyền thu tiền từ khách hàng do bán chịu hàng hóa, dịch vụ; theo dõi trên TK 131 theo từng đối tượng. | AR | processes/ar-accounts-receivable.md §8 |
| Dư nợ rủi ro | Credit Exposure | — | Dư nợ chịu rủi ro | Tổng dư nợ 131 mở cộng đơn hàng, hàng đã giao chưa xuất hóa đơn và hóa đơn chưa thu; dùng kiểm tra hạn mức tín dụng. | AR | processes/ar-accounts-receivable.md §7 |
| Dự phòng nợ phải thu khó đòi | Doubtful-debt Provision | — | Trích lập dự phòng công nợ | Trích chi phí cho nợ khó thu theo thời gian quá hạn 30/50/70/100% (TT48/2019); ghi Nợ 642 / Có 2293 cuối năm trước khi lập BCTC. | AR | regulations/vn-accounting.md §11 |
| Giấy báo Có | Credit Note | — | Credit memo | Chứng từ giảm công nợ phải thu do hàng bán bị trả lại hoặc giảm giá cho khách (khác "giấy báo Có ngân hàng"). | AR | processes/ar-accounts-receivable.md §4 |
| Hàng bán bị trả lại | Sales Return | — | Trả lại hàng bán | Khách trả lại hàng đã mua; ghi giảm trừ doanh thu (TK 5212), giảm thuế GTGT đầu ra và nhập lại kho. | AR | processes/ar-accounts-receivable.md §8 |
| Hạn mức tín dụng | Credit Limit | — | Hạn mức công nợ | Giá trị bán chịu tối đa cho phép với một khách hàng; vượt hạn mức thì cảnh báo/chặn đơn/chặn giao tùy tham số. | AR | processes/ar-accounts-receivable.md §7 |
| Hóa đơn bán hàng | Sales Invoice | — | Hóa đơn đầu ra | Chứng từ ghi nhận doanh thu (511), phải thu (131) và thuế GTGT đầu ra (33311). | AR | processes/ar-accounts-receivable.md §4 |
| Khách hàng | Customer | KH | — | Đối tác mua hàng của DN; đối tượng theo dõi công nợ phải thu. | AR | processes/ar-accounts-receivable.md §3 |
| Khách ứng trước | Customer Advance | — | Khách trả trước, tiền đặt cọc | Khoản khách trả trước khi giao hàng/xuất hóa đơn; dư Có 131, trình bày ở bên nợ phải trả. | AR | processes/ar-accounts-receivable.md §8 |
| Kiểm soát tín dụng | Credit Control (Management) | — | Quản lý công nợ | Cơ chế so dư nợ rủi ro với hạn mức, khóa/giải phóng đơn hàng khi vượt hạn mức. | AR | processes/ar-accounts-receivable.md §7 |
| Kỳ thu tiền bình quân | Days Sales Outstanding | DSO | Số ngày thu tiền | Số ngày bình quân để thu hồi công nợ phải thu = (phải thu bình quân / doanh thu bán chịu) × số ngày kỳ; chỉ số kiểm soát rủi ro công nợ. | AR | processes/ar-accounts-receivable.md §11 |
| Nhắc nợ | Dunning (Collections) | — | Thu hồi công nợ | Gửi thư nhắc nợ theo cấp độ tăng dần dựa trên số ngày (hoặc số tiền) quá hạn. | AR | processes/ar-accounts-receivable.md §5 |
| Nợ phải thu khó đòi | Doubtful Debt | — | Nợ khó đòi, nợ xấu | Khoản phải thu quá hạn hoặc khó thu hồi, đủ điều kiện trích dự phòng theo thời gian quá hạn (TT48). | AR | regulations/vn-accounting.md §11 |
| Phân bổ thu tiền | Receipt Allocation | — | Cấn trừ thu tiền, matching | Gán tiền thu vào từng hóa đơn (theo FIFO, theo hạn, hoặc thủ công) để tính đúng số dư và tuổi nợ. | AR | processes/ar-accounts-receivable.md §7 |
| Xóa sổ nợ khó đòi | Bad-debt Write-off | — | Xóa nợ không thu hồi được | Ghi giảm khoản nợ không thu hồi được (Nợ 2293 phần đã lập, 642 phần thiếu / Có 131); theo dõi ngoài sổ vì TT99 bỏ TK 004. | AR | processes/ar-accounts-receivable.md §8 |

### Công nợ chung (AP & AR)

| Thuật ngữ (VI) | Tiếng Anh | Viết tắt | Tên khác / tên khách hàng hay dùng | Định nghĩa ngắn | Module | Xem thêm |
|---|---|---|---|---|---|---|
| Bù trừ công nợ | Netting (Clearing) | — | Cấn trừ công nợ | Cấn trừ số dư phải trả (331) với phải thu (131) của cùng một đối tác theo biên bản thỏa thuận. | AP/AR | processes/ap-accounts-payable.md §13 |
| Chiết khấu thanh toán | Settlement (Cash) Discount | — | Chiết khấu trả sớm | Giảm trừ khi trả/thu tiền sớm; bên bán ghi chi phí tài chính (635), bên mua ghi doanh thu tài chính (515); không giảm doanh thu và không chịu VAT. | AP/AR | processes/ar-accounts-receivable.md §8 |
| Dung sai | Tolerance | — | Ngưỡng chênh lệch cho phép | Ngưỡng chênh lệch giá/số lượng cho phép khi đối chiếu hóa đơn; vượt ngưỡng thì treo chứng từ. | AP/AR | processes/ap-accounts-payable.md §7 |
| Điều khoản thanh toán | Payment Terms | — | Term thanh toán, Net 30 | Quy định số ngày Net và chiết khấu trả sớm, xác định ngày đến hạn của hóa đơn. | AP/AR | processes/ar-accounts-receivable.md §3 |
| Đối chiếu công nợ | Statement Reconciliation | — | Xác nhận công nợ | Lập biên bản xác nhận số dư công nợ giữa DN và NCC/khách hàng định kỳ. | AP/AR | processes/ar-accounts-receivable.md §7 |
| Phân tích tuổi nợ | Aging Analysis | — | Báo cáo tuổi nợ, aging | Phân nhóm công nợ theo số ngày quá hạn (bucket) để quản trị dòng tiền và rủi ro thu hồi. | AP/AR | processes/ar-accounts-receivable.md §11 |
| Tài khoản đối ứng công nợ | Reconciliation Account | — | TK tổng hợp công nợ | TK sổ cái tổng hợp (131/331) gắn với từng đối tượng công nợ chi tiết; số dư phải khớp sổ con. | AP/AR | processes/ap-accounts-payable.md §8 |

### Tiền & ngân hàng (Cash & Bank Management)

| Thuật ngữ (VI) | Tiếng Anh | Viết tắt | Tên khác / tên khách hàng hay dùng | Định nghĩa ngắn | Module | Xem thêm |
|---|---|---|---|---|---|---|
| Bảng đối chiếu số dư ngân hàng | Bank Reconciliation Statement | — | Bảng đối chiếu ngân hàng | Báo cáo giải thích chênh lệch giữa số dư sổ sách và số dư sao kê bằng các khoản treo. | CB | processes/cash-bank.md §11 |
| Danh mục tài khoản ngân hàng | Bank Account Master (House Bank) | — | House bank, danh mục TK ngân hàng | Khai báo các tài khoản ngân hàng của DN, ánh xạ tới TK chi tiết 112. | CB | processes/cash-bank.md §3 |
| Dự báo dòng tiền | Cash-flow Forecast | — | Dự báo thu chi | Dự kiến thu/chi và thanh khoản theo kỳ dựa trên khoản mục dòng tiền và cam kết. | CB | processes/cash-bank.md §12 |
| Đề nghị thanh toán | Payment Request (Proposal) | — | Đề nghị chi, payment proposal | Chứng từ xin chi tiền trả nhà cung cấp/chi phí, khởi đầu luồng phê duyệt chi (dùng chung AP và CB). | CB | processes/cash-bank.md §5A |
| Điều chuyển nội bộ | Internal Transfer | — | Chuyển quỹ, chuyển tiền nội bộ | Chuyển tiền giữa quỹ và ngân hàng hoặc giữa các tài khoản ngân hàng của cùng DN. | CB | processes/cash-bank.md §8 |
| Đối chiếu ngân hàng | Bank Reconciliation | — | Khớp sao kê | So khớp số dư và giao dịch giữa sổ sách kế toán và sao kê ngân hàng. | CB | processes/cash-bank.md §7 |
| Giấy báo Có (ngân hàng) | Bank Credit Advice | — | Báo Có | Thông báo của ngân hàng về việc ghi tăng tiền vào tài khoản DN. | CB | processes/cash-bank.md §4 |
| Giấy báo Nợ (ngân hàng) | Bank Debit Advice | — | Báo Nợ | Thông báo của ngân hàng về việc ghi giảm tiền khỏi tài khoản DN. | CB | processes/cash-bank.md §4 |
| Hạn mức duyệt | Approval Limit | — | Hạn mức phê duyệt | Mức tiền tối đa mỗi cấp được phép phê duyệt chi; vượt mức thì leo thang lên cấp cao hơn. | Chung | security-and-parameters.md |
| Khoản mục dòng tiền | Cash-flow Item | — | Mã dòng tiền | Phân loại thu/chi (kinh doanh/đầu tư/tài chính) phục vụ dự báo và Báo cáo lưu chuyển tiền tệ. | CB | processes/cash-bank.md §3 |
| Khoản treo | Outstanding Item | — | Mục chưa khớp | Giao dịch chưa khớp khi đối chiếu, ví dụ séc chưa xuất trình hoặc phí ngân hàng chưa ghi sổ. | CB | processes/cash-bank.md §7 |
| Kiểm kê quỹ | Cash Count | — | Kiểm quỹ | Đối chiếu tồn quỹ tiền mặt thực tế với số dư sổ sách tại một thời điểm. | CB | processes/cash-bank.md §7 |
| Kết nối ngân hàng | Bank Connectivity | — | Tích hợp ngân hàng | Mô hình trao đổi dữ liệu với ngân hàng: file (MT940/CAMT.053), host-to-host/SFTP, hoặc API. | CB | processes/cash-bank.md §12 |
| Phiếu chi | Cash Payment | — | Phiếu chi tiền mặt (02-TT) | Chứng từ ghi nhận chi tiền mặt xuất quỹ sau khi được phê duyệt đúng thẩm quyền. | CB | processes/cash-bank.md §5B |
| Phiếu thu | Cash Receipt | — | Phiếu thu tiền mặt (01-TT) | Chứng từ ghi nhận thu tiền mặt nhập quỹ, do kế toán tiền lập và thủ quỹ thực thu. | CB | processes/cash-bank.md §5B |
| Quản lý ngân quỹ | Treasury Management | — | Treasury, quản trị dòng tiền | Mảng quản lý tiền mặt, quan hệ ngân hàng, tài trợ ngắn/dài hạn, tín dụng và đầu tư của DN. | CB | processes/cash-bank.md §1 |
| Quỹ tiền mặt | Cash on Hand (Cash Desk) | — | Tồn quỹ, két | Tiền mặt do thủ quỹ nắm giữ tại két; theo dõi ở TK 111. | CB | processes/cash-bank.md §3 |
| Quyết toán tạm ứng / Hoàn ứng | Advance Settlement | — | Thanh toán tạm ứng | Tất toán khoản tạm ứng bằng chứng từ chi tiêu thực tế và nộp lại phần tiền thừa. | CB | processes/cash-bank.md §8 |
| Sao kê ngân hàng | Bank Statement | — | Sổ phụ ngân hàng | Bảng kê giao dịch và số dư tài khoản do ngân hàng cung cấp, cơ sở để đối chiếu. | CB | processes/cash-bank.md §4 |
| Sổ quỹ tiền mặt | Cash Book | — | Sổ quỹ | Sổ kế toán bắt buộc theo dõi thu/chi/tồn quỹ tiền mặt theo thời gian. | CB | processes/cash-bank.md §11 |
| Sổ tiền gửi ngân hàng | Bank Book | — | Sổ ngân hàng | Sổ kế toán bắt buộc theo dõi biến động của từng tài khoản ngân hàng. | CB | processes/cash-bank.md §11 |
| Tạm ứng | Employee Advance | — | Tạm ứng nhân viên | Khoản ứng trước tiền cho nhân viên đi công tác/mua sắm; theo dõi ở TK 141. | CB | processes/cash-bank.md §8 |
| Thấu chi | Overdraft | — | — | Chi vượt số dư tài khoản trong hạn mức ngân hàng cấp; phản ánh như khoản vay (TK 341), không ghi âm 112. | CB | processes/cash-bank.md §13 |
| Thanh toán không dùng tiền mặt | Non-cash Payment | TTKDTM | Chuyển khoản | Chuyển khoản/ủy nhiệm chi/thẻ/ví; là điều kiện khấu trừ VAT và tính chi phí TNDN với hóa đơn từ 5 triệu đồng (từ 01/7/2025). | CB | regulations/vn-tax-einvoice.md §2.4 |
| Thủ quỹ | Cashier (Treasurer) | — | — | Người giữ và thực hiện thu/chi tiền mặt thực tế; phải tách biệt với kế toán ghi sổ (SoD). | CB | processes/cash-bank.md §2 |
| Tiền đang chuyển | Cash in Transit | — | — | Tiền đã nộp/chuyển nhưng chưa nhận được giấy báo Có; theo dõi ở TK 113. | CB | processes/cash-bank.md §8 |
| Tiền gửi không kỳ hạn | Demand Deposit | — | **Tiền gửi ngân hàng** (tên TT200) | Số dư tiền gửi ngân hàng không kỳ hạn; TK 112 theo TT99/2025 (TT200 gọi là "Tiền gửi Ngân hàng"). | CB | processes/cash-bank.md §3 |
| Tỷ giá ghi sổ bình quân gia quyền di động | Moving Weighted-average Book Rate | — | Tỷ giá ghi sổ | Tỷ giá áp dụng cho bên Có khi xuất quỹ/chi ngoại tệ theo TT99 (bình quân di động của số dư gốc ngoại tệ). | CB | processes/cash-bank.md §8 |
| Ủy nhiệm chi | Payment Order | UNC | Lệnh chi | Lệnh của chủ tài khoản yêu cầu ngân hàng trích tiền trả cho người thụ hưởng. | CB | processes/cash-bank.md §4 |

### Tài sản cố định, công cụ dụng cụ & chi phí trả trước (Fixed Assets)

| Thuật ngữ (VI) | Tiếng Anh | Viết tắt | Tên khác / tên khách hàng hay dùng | Định nghĩa ngắn | Module | Xem thêm |
|---|---|---|---|---|---|---|
| Bộ phận sử dụng tài sản | Asset Cost Center | — | Nơi sử dụng tài sản | Đơn vị quản lý và tiếp nhận chi phí khấu hao của tài sản; quyết định TK chi phí ghi khấu hao (627/641/642/623). | FA | processes/fixed-assets.md §3 |
| Chi phí đi vay vốn hóa | Capitalized Borrowing Cost | — | Vốn hóa lãi vay | Lãi vay liên quan trực tiếp đến tài sản dở dang đủ điều kiện được tính vào nguyên giá thay vì chi phí kỳ (VAS 16). | FA | regulations/vn-accounting.md §8 |
| Chi phí trả trước | Prepaid Expenses | — | **Chi phí chờ phân bổ** (tên TT99) | Chi phí đã phát sinh liên quan nhiều kỳ, phân bổ dần vào chi phí; TK 242 (TT99/2025 đổi tên thành "Chi phí chờ phân bổ"). | FA | processes/fixed-assets.md §8.3 |
| Công cụ dụng cụ | Tools and Supplies | CCDC | — | Tư liệu lao động không đủ tiêu chuẩn TSCĐ (dưới 30 triệu hoặc dưới 1 năm); TK 153, xuất dùng phân bổ 1 lần hoặc nhiều kỳ (tối đa 36 tháng cho mục đích thuế). | FA | processes/fixed-assets.md §8.3 |
| Đánh giá lại tài sản | Asset Revaluation | — | Đánh giá lại TSCĐ | Xác định lại giá trị TSCĐ, chênh lệch ghi qua TK 412; chỉ thực hiện khi pháp luật cho phép (góp vốn, cổ phần hóa, điều chuyển theo quyết định nhà nước). | FA | processes/fixed-assets.md §8.4 |
| Điều chuyển tài sản | Asset Transfer | — | Luân chuyển tài sản | Chuyển tài sản giữa bộ phận/địa điểm; nội bộ cùng pháp nhân giữ nguyên nguyên giá và hao mòn, khác pháp nhân ghi giảm cộng ghi tăng. | FA | processes/fixed-assets.md §6 |
| Giá trị còn lại | Net Book Value | NBV | GTCL | Nguyên giá trừ hao mòn lũy kế; phản ánh giá trị tài sản còn lại trên sổ sách. | FA | processes/fixed-assets.md §8.2 |
| Giá trị thu hồi ước tính | Estimated Salvage Value | — | Giá trị thanh lý ước tính | Giá trị dự kiến thu được khi thanh lý tài sản cuối thời gian sử dụng; dùng trong một số mô hình tính khấu hao của ERP. | FA | processes/fixed-assets.md §9 |
| Hao mòn lũy kế | Accumulated Depreciation | — | Khấu hao lũy kế | Tổng khấu hao đã trích của TSCĐ đến thời điểm báo cáo (TK 214); là tài khoản điều chỉnh giảm nguyên giá. | FA | processes/fixed-assets.md §8.2 |
| Khấu hao | Depreciation | — | Trích khấu hao | Việc phân bổ có hệ thống nguyên giá TSCĐ vào chi phí trong suốt thời gian sử dụng hữu ích (đường thẳng, số dư giảm dần, theo sản lượng). | FA | regulations/vn-accounting.md §9 |
| Khung thời gian khấu hao | Useful Life Frame | — | Khung khấu hao | Khoảng thời gian trích khấu hao tối thiểu–tối đa cho từng nhóm tài sản (Phụ lục 1 TT45/2013); thời gian khai báo phải nằm trong khung. | FA | processes/fixed-assets.md §9 |
| Kiểm kê tài sản | Asset Physical Count | — | Kiểm kê TSCĐ | Đối chiếu tài sản trên sổ sách với hiện vật, xử lý chênh lệch thừa/thiếu; bắt buộc tối thiểu cuối năm trước khi lập BCTC. | FA | processes/fixed-assets.md §6 |
| Nguyên giá | Historical (Acquisition) Cost | — | Giá trị ghi sổ ban đầu | Toàn bộ chi phí để đưa tài sản vào trạng thái sẵn sàng sử dụng: giá mua trừ chiết khấu, cộng thuế không hoàn lại và chi phí trực tiếp (vận chuyển, lắp đặt, chạy thử). | FA | processes/fixed-assets.md §8.1 |
| Phương pháp đường thẳng | Straight-line Method | — | Khấu hao đều | Khấu hao mức đều mỗi kỳ = nguyên giá / thời gian sử dụng; phổ biến nhất và là mặc định. | FA | processes/fixed-assets.md §7 |
| Phương pháp số dư giảm dần có điều chỉnh | Declining Balance Method | — | Khấu hao nhanh | Khấu hao nhanh theo tỷ lệ = tỷ lệ đường thẳng × hệ số 1,5/2,0/2,5; phần vượt 2 lần đường thẳng không được trừ thuế. | FA | processes/fixed-assets.md §7 |
| Phương pháp theo số lượng, khối lượng sản phẩm | Units of Production Method | — | Khấu hao theo sản lượng | Mức khấu hao kỳ = sản lượng kỳ × (nguyên giá / tổng sản lượng ước tính theo công suất thiết kế). | FA | processes/fixed-assets.md §7 |
| Sổ tài sản cố định | Fixed Asset Register | — | Sổ TSCĐ | Sổ liệt kê và theo dõi biến động của toàn bộ TSCĐ theo nhóm, bộ phận, nguồn hình thành. | FA | processes/fixed-assets.md §11 |
| Tài sản cố định | Fixed Asset | TSCĐ / FA | — | Tư liệu lao động có thời gian sử dụng trên 1 năm và nguyên giá từ 30 triệu đồng (TT45/2013); gồm hữu hình (211), thuê tài chính (212), vô hình (213); TT133 gộp vào 211. | FA | regulations/vn-accounting.md §9 |
| Tài sản cố định hữu hình | Tangible Fixed Asset | — | TSCĐ hữu hình | TSCĐ có hình thái vật chất: nhà cửa, máy móc, thiết bị, phương tiện vận tải; TK 211. | FA | processes/fixed-assets.md §8.1 |
| Tài sản cố định thuê tài chính | Finance-lease Fixed Asset | — | TSCĐ thuê tài chính | Tài sản thuê mà bên thuê chịu phần lớn rủi ro và lợi ích gắn với quyền sở hữu; TK 212, trích khấu hao như tài sản sở hữu (VAS 06). | FA | processes/fixed-assets.md §8.1 |
| Tài sản cố định vô hình | Intangible Fixed Asset | — | TSCĐ vô hình | TSCĐ không có hình thái vật chất nhưng xác định được giá trị: quyền sử dụng đất, phần mềm, bản quyền; TK 213. Quyền sử dụng đất lâu dài không trích khấu hao. | FA | processes/fixed-assets.md §8.1 |
| Thanh lý, nhượng bán tài sản | Asset Disposal / Liquidation | — | Thanh lý TSCĐ | Ghi giảm tài sản không còn dùng: xóa sổ Nợ 214 (hao mòn) và 811 (giá trị còn lại) / Có 211; thu thanh lý ghi 711 và thuế GTGT đầu ra 3331. | FA | processes/fixed-assets.md §8.5 |
| Thẻ tài sản cố định | Fixed Asset Card | — | Thẻ TSCĐ | Hồ sơ gốc theo dõi từng tài sản: nguyên giá, hao mòn, giá trị còn lại, bộ phận sử dụng, lịch sử biến động; là sổ kế toán chi tiết tài sản. | FA | processes/fixed-assets.md §4 |
| Trích khấu hao | Depreciation Run | — | Chạy khấu hao, job khấu hao | Tác vụ tính và ghi khấu hao TSCĐ theo kỳ; phân bổ vào 627/641/642/623 theo bộ phận sử dụng. | FA | processes/fixed-assets.md §8.2 |
| Vùng khấu hao / Sổ khấu hao | Depreciation Area / Book | — | Depreciation book | Tập giá trị song song để tính khấu hao cho nhiều mục đích (kế toán, thuế, quản trị) trên cùng một tài sản (SAP, Dynamics 365). | FA | processes/fixed-assets.md §9 |
| Vốn hóa | Capitalization | — | Ghi tăng nguyên giá | Ghi một khoản chi vào nguyên giá tài sản (thay vì chi phí kỳ) khi làm tăng lợi ích kinh tế tương lai; phân biệt với chi phí sửa chữa thường xuyên. | FA | processes/fixed-assets.md §8.4 |
| Xây dựng cơ bản dở dang | Construction in Progress | XDCB / CIP | Đầu tư XDCB dở dang | Chi phí mua sắm, xây dựng, nâng cấp TSCĐ chưa hoàn thành; tập hợp trên TK 241 rồi kết chuyển sang 211/213 khi quyết toán. | FA | processes/fixed-assets.md §4 |

### Thuế & hóa đơn điện tử (Tax & E-invoice)

| Thuật ngữ (VI) | Tiếng Anh | Viết tắt | Tên khác / tên khách hàng hay dùng | Định nghĩa ngắn | Module | Xem thêm |
|---|---|---|---|---|---|---|
| Bảng kê hóa đơn | Invoice Listing | — | Bảng kê mua vào/bán ra | Bảng tổng hợp hóa đơn bán ra/mua vào phục vụ kê khai và đối chiếu; không còn nộp kèm tờ khai nhưng vẫn lập nội bộ. | TAX | processes/tax-einvoice.md §5.3 |
| Bảng tổng hợp dữ liệu hóa đơn điện tử | E-invoice Data Summary | 01/TH-HĐĐT | Bảng tổng hợp HĐĐT | Phương thức chuyển dữ liệu hóa đơn không mã theo kỳ, chỉ cho ngành đặc thù (viễn thông, bảo hiểm, tài chính–ngân hàng, hàng không, chứng khoán, điện, nước). | TAX | regulations/vn-tax-einvoice.md §4.5 |
| Chi phí được trừ | Deductible Expense | — | Chi phí hợp lệ | Khoản chi thực tế phát sinh phục vụ SXKD, có đủ hóa đơn/chứng từ hợp pháp và chứng từ không dùng tiền mặt (hóa đơn từ 5 triệu) được trừ khi tính thuế TNDN. | TAX | regulations/vn-tax-einvoice.md §3.2 |
| Chứng từ khấu trừ thuế thu nhập cá nhân | PIT Withholding Voucher | — | Chứng từ khấu trừ TNCN | Chứng từ điện tử tổ chức chi trả cấp cho người bị khấu trừ thuế TNCN; bắt buộc điện tử từ 01/6/2025. | TAX | regulations/vn-tax-einvoice.md §5 |
| Chứng từ thanh toán không dùng tiền mặt | Non-cash Payment Document | — | Chứng từ chuyển khoản | Chứng từ chuyển tiền từ tài khoản người mua sang người bán; bắt buộc với hóa đơn từ 5 triệu để được khấu trừ GTGT và tính chi phí TNDN. | TAX | regulations/vn-tax-einvoice.md §2.4 |
| Doanh nghiệp rủi ro về hóa đơn | High-risk Enterprise | — | DN bỏ trốn, DN ma | DN trong danh sách cảnh báo của cơ quan thuế; hóa đơn phát sinh sau ngày bỏ trốn bị loại khấu trừ và chi phí. | TAX | processes/tax-einvoice.md §7 |
| Giảm thuế GTGT 8% | 8% VAT Reduction | — | Giảm 2% thuế GTGT | Chính sách giảm thuế suất 10% xuống 8% cho nhóm đủ điều kiện, hiệu lực 01/7/2025 đến hết 31/12/2026 (NQ 204/2025, NĐ 174/2025); thiết kế theo ngày hiệu lực, không hard-code. | TAX | regulations/vn-tax-einvoice.md §2.2 |
| Hoàn thuế giá trị gia tăng | VAT Refund | — | Hoàn thuế GTGT | Việc ngân sách hoàn lại thuế GTGT đầu vào chưa khấu trừ hết trong các trường hợp xuất khẩu, dự án đầu tư, chấm dứt hoạt động. | TAX | regulations/vn-tax-einvoice.md §2.5 |
| Hóa đơn bán hàng | Sales Invoice (direct method) | — | Hóa đơn thông thường | Hóa đơn cho tổ chức, cá nhân khai thuế theo phương pháp trực tiếp hoặc trong khu phi thuế quan (ký hiệu mẫu số 2). | TAX | regulations/vn-tax-einvoice.md §4.1 |
| Hóa đơn có mã của cơ quan thuế | Tax-authority-coded Invoice | — | Hóa đơn có mã | Hóa đơn phải gửi cơ quan thuế để được cấp mã xác thực trước khi gửi người mua; ký tự đầu của ký hiệu là C. | TAX | regulations/vn-tax-einvoice.md §4.5 |
| Hóa đơn điện tử | Electronic Invoice | HĐĐT | E-invoice | Hóa đơn ở dạng dữ liệu điện tử do người bán lập, ký số và chuyển tới cơ quan thuế/người mua; khung hiện hành NĐ 254/2026 + TT 91/2026. | TAX | regulations/vn-tax-einvoice.md §4 |
| Hóa đơn điện tử khởi tạo từ máy tính tiền | Cash-register E-invoice | POS | Hóa đơn máy tính tiền | Hóa đơn bán lẻ/ăn uống phát từ máy tính tiền kết nối chuyển dữ liệu với cơ quan thuế; không bắt buộc chữ ký số; bắt buộc với hộ KD doanh thu từ 1 tỷ/năm. | TAX | regulations/vn-tax-einvoice.md §4.7 |
| Hóa đơn điều chỉnh | Adjustment Invoice | — | — | Hóa đơn lập để điều chỉnh tăng/giảm sai sót trọng yếu của hóa đơn gốc, ghi rõ số hóa đơn bị điều chỉnh (không hủy hóa đơn gốc). | TAX | regulations/vn-tax-einvoice.md §4.6 |
| Hóa đơn giá trị gia tăng | VAT Invoice | — | Hóa đơn đỏ, hóa đơn GTGT | Hóa đơn cho tổ chức khai thuế GTGT theo phương pháp khấu trừ, thể hiện riêng tiền thuế đầu ra (ký hiệu mẫu số 1). | TAX | regulations/vn-tax-einvoice.md §4.1 |
| Hóa đơn không mã của cơ quan thuế | Uncoded E-invoice | — | Hóa đơn không mã | Hóa đơn do DN đủ điều kiện tự phát hành rồi chuyển dữ liệu tới cơ quan thuế; ký tự đầu của ký hiệu là K. | TAX | regulations/vn-tax-einvoice.md §4.5 |
| Hóa đơn thay thế | Replacement Invoice | — | — | Hóa đơn lập mới thay cho hóa đơn gốc sai sót; bắt buộc với hóa đơn máy tính tiền và tài sản đăng ký quyền sở hữu (không điều chỉnh). | TAX | regulations/vn-tax-einvoice.md §4.6 |
| Hóa đơn thương mại điện tử | Electronic Commercial Invoice | — | Commercial invoice | Hóa đơn dùng cho xuất khẩu khi đáp ứng yêu cầu truyền dữ liệu. | TAX | regulations/vn-tax-einvoice.md §4.1 |
| Idempotency phát hành hóa đơn | Issuance Idempotency | — | Chống phát hành trùng | Cơ chế bảo đảm mỗi hóa đơn chỉ phát hành một lần dù retry gửi, dựa trên khóa duy nhất (ký hiệu + số + kỳ) và trạng thái gửi. | TAX | processes/tax-einvoice.md §6.2 |
| Khấu trừ thuế GTGT đầu vào | Input VAT Credit | — | Khấu trừ thuế đầu vào | Trừ thuế GTGT mua vào vào thuế đầu ra; cần hóa đơn hợp pháp và chứng từ không dùng tiền mặt với hóa đơn từ 5 triệu đồng. | TAX | regulations/vn-tax-einvoice.md §2.4 |
| Không chịu thuế | VAT-exempt (Non-taxable) | KCT | Đối tượng không chịu thuế | Hàng/dịch vụ không có thuế đầu ra VÀ thuế đầu vào không được khấu trừ (tính vào chi phí/giá vốn); Điều 5 Luật 48/2024. | TAX | regulations/vn-tax-einvoice.md §2.1 |
| Không phải kê khai, tính nộp thuế | Out-of-scope VAT | KKKNT | — | Khoản thu không có thuế đầu ra NHƯNG thuế đầu vào liên quan VẪN được khấu trừ (bồi thường, góp vốn, thu hộ chi hộ…); khác bản chất với "không chịu thuế". | TAX | regulations/vn-tax-einvoice.md §2.1 |
| Kỳ tính thuế | Tax Period | — | Kỳ thuế | Khoảng thời gian xác định nghĩa vụ thuế (tháng/quý/năm tùy sắc thuế và doanh thu). | TAX | regulations/vn-tax-einvoice.md §2.6 |
| Ký hiệu hóa đơn | Invoice Symbol | — | Serial hóa đơn | Chuỗi 6 ký tự: C/K (có/không mã) + 2 số năm + ký tự loại hình (T/D/L/M) + 2 ký tự quản lý nội bộ (ví dụ C25TAA); số hóa đơn phải liên tục theo từng ký hiệu. | TAX | regulations/vn-tax-einvoice.md §4.2 |
| Ký hiệu mẫu số hóa đơn | Invoice Template Number | — | Mẫu số hóa đơn | Một chữ số thể hiện loại hóa đơn (1 = GTGT, 2 = bán hàng, 5 = loại khác…). | TAX | regulations/vn-tax-einvoice.md §4.2 |
| Mã số thuế | Tax Identification Number | MST | — | Mã định danh người nộp thuế do cơ quan thuế cấp (tổ chức 10/13 chữ số); cá nhân/hộ dần thay bằng số định danh cá nhân. | TAX | regulations/vn-tax-einvoice.md §6 |
| Mã thuế giá trị gia tăng | VAT Tax Code | — | Mã thuế suất, tax code | Master data gắn cho từng dòng hàng, xác định thuế suất, cờ được khấu trừ, nhóm kê khai và tài khoản thuế; có ngày hiệu lực. | TAX | regulations/vn-tax-einvoice.md §2.1 |
| Nhà cung cấp dịch vụ hóa đơn điện tử | E-invoice Service Provider | TVAN | Đơn vị cung cấp HĐĐT | Tổ chức trung gian (VNPT, Viettel, MISA, FPT…) kết nối ERP với cổng thuế để ký, cấp mã và truyền hóa đơn. | TAX | regulations/vn-tax-einvoice.md §4.8 |
| Phương pháp khấu trừ | Credit Method | — | PP khấu trừ | Cách tính thuế GTGT phải nộp = thuế đầu ra − thuế đầu vào được khấu trừ; mặc định cho DN có đủ sổ sách, hóa đơn. | TAX | regulations/vn-tax-einvoice.md §2.3 |
| Phương pháp trực tiếp | Direct Method | — | PP trực tiếp | Cách tính thuế GTGT = tỷ lệ % × doanh thu; áp dụng cho hộ kinh doanh, một số ngành đặc thù, DN không đủ điều kiện khấu trừ. | TAX | regulations/vn-tax-einvoice.md §2.3 |
| Quyết toán thuế TNDN | CIT Finalization | 03/TNDN | Quyết toán thuế TNDN | Tờ khai quyết toán thuế TNDN năm, chuyển lợi nhuận kế toán sang thu nhập tính thuế qua các khoản điều chỉnh và lỗ được chuyển (tối đa 5 năm). | TAX | regulations/vn-tax-einvoice.md §3.3 |
| Số định danh cá nhân | Personal Identification Number | SĐDCN | Số CCCD | Số 12 chữ số trên CCCD, dùng thay mã số thuế cho cá nhân/hộ gia đình/hộ kinh doanh từ 01/7/2025. | TAX | regulations/vn-tax-einvoice.md §6 |
| Thông báo hóa đơn điện tử có sai sót | E-invoice Error Notice | 04/SS-HĐĐT | Mẫu 04/SS | Mẫu gửi cơ quan thuế khi hóa đơn sai sót nhỏ (tên, địa chỉ) không ảnh hưởng MST/tiền/thuế suất, không phải lập lại hóa đơn. | TAX | regulations/vn-tax-einvoice.md §4.6 |
| Thời điểm lập hóa đơn | Invoice Issuance Time | — | Ngày lập hóa đơn | Mốc bắt buộc lập hóa đơn, suy từ sự kiện nghiệp vụ (giao hàng, hoàn thành/thu tiền dịch vụ, nghiệm thu xây lắp, thông quan xuất khẩu); ký số & gửi chậm nhất ngày làm việc kế tiếp. | TAX | regulations/vn-tax-einvoice.md §4.4 |
| Thuế bảo vệ môi trường | Environmental Protection Tax | BVMT | — | Thuế gián thu trên hàng hóa gây tác động xấu đến môi trường (xăng dầu, than…); ở khâu nhập khẩu tính vào trị giá tính thuế GTGT. | TAX | processes/tax-einvoice.md §8 |
| Thuế giá trị gia tăng | Value-Added Tax | GTGT / VAT | — | Thuế gián thu tính trên giá trị tăng thêm của hàng hóa, dịch vụ; mức phổ thông 10%, ưu đãi 5%, xuất khẩu 0%, giảm tạm thời 8% đến hết 31/12/2026. | TAX | regulations/vn-tax-einvoice.md §2 |
| Thuế GTGT đầu ra | Output VAT | — | VAT đầu ra | Thuế GTGT tính trên hàng/dịch vụ bán ra; hạch toán Có TK 33311. | TAX | regulations/vn-tax-einvoice.md §7 |
| Thuế GTGT đầu vào được khấu trừ | Deductible Input VAT | — | VAT đầu vào | Số thuế GTGT trên hàng/dịch vụ mua vào được trừ khỏi thuế đầu ra khi đủ điều kiện; theo dõi ở TK 133 (1331 hàng hóa dịch vụ, 1332 TSCĐ). | TAX | regulations/vn-tax-einvoice.md §2.4 |
| Thuế GTGT hàng nhập khẩu | Import VAT | — | VAT nhập khẩu | Thuế GTGT khâu nhập khẩu tính trên (trị giá tính thuế NK + thuế NK + TTĐB + BVMT); nếu được khấu trừ ghi Nợ 133 / Có 33312. | TAX | regulations/vn-tax-einvoice.md §7 |
| Thuế nhập khẩu | Import Duty | — | Thuế NK | Thuế đánh trên hàng nhập khẩu tính trên trị giá hải quan; hạch toán Có TK 3333 và tính vào giá gốc hàng nhập. | TAX | processes/tax-einvoice.md §8 |
| Thuế suất 0% | Zero-rated | — | — | Áp cho xuất khẩu, vận tải quốc tế…; thuế đầu ra 0% nhưng thuế đầu vào được khấu trừ và được hoàn (khác "không chịu thuế"). | TAX | regulations/vn-tax-einvoice.md §2.1 |
| Thuế thu nhập cá nhân | Personal Income Tax | TNCN / PIT | — | Thuế trên thu nhập cá nhân; tổ chức chi trả có nghĩa vụ khấu trừ tại nguồn (chi tiết chính sách & bảng lương xem file lương). | TAX | regulations/vn-labor-payroll.md |
| Thuế thu nhập doanh nghiệp | Corporate Income Tax | TNDN / CIT | — | Thuế trực thu trên thu nhập chịu thuế của DN; thuế suất 15% (<3 tỷ), 17% (3–50 tỷ), 20% phổ thông theo Luật 67/2025 (TK 3334, 821). | TAX | regulations/vn-tax-einvoice.md §3.1 |
| Thuế thu nhập hoãn lại | Deferred Income Tax | — | Thuế hoãn lại | Chênh lệch tạm thời giữa cơ sở kế toán và cơ sở thuế của tài sản/nợ, ghi nhận tài sản thuế hoãn lại (TK 243) hoặc thuế hoãn lại phải trả (TK 347), chi phí qua 8212 (VAS 17). | TAX | regulations/vn-accounting.md §8 |
| Thuế tiêu thụ đặc biệt | Special Consumption Tax | TTĐB / SCT | — | Thuế trên một số hàng/dịch vụ đặc biệt; ở khâu nhập khẩu tính vào giá gốc (Có 3332), phần được khấu trừ theo TT99 ghi vào TK 1383. | TAX | processes/tax-einvoice.md §8 |
| Thuế tối thiểu toàn cầu | Global Minimum Tax (Pillar 2) | — | Thuế bổ sung tối thiểu | Cơ chế thuế TNDN bổ sung bảo đảm thuế suất hiệu lực tối thiểu 15% cho tập đoàn đa quốc gia lớn; chi phí ghi TK 82112 theo TT99. | TAX | regulations/vn-accounting.md §4 |
| Tờ khai thuế giá trị gia tăng | VAT Return | 01/GTGT | Tờ khai GTGT | Tờ khai thuế GTGT theo phương pháp khấu trừ, kỳ tháng (doanh thu năm trước > 50 tỷ) hoặc quý, nộp cơ quan thuế. | TAX | regulations/vn-tax-einvoice.md §2.6 |
| Trị giá hải quan | Customs Value | — | Trị giá tính thuế NK | Giá làm căn cứ tính thuế hàng nhập khẩu, xác định ưu tiên theo trị giá giao dịch (giá thực tế phải trả đến cửa khẩu nhập đầu tiên). | TAX | processes/tax-einvoice.md §8 |
| Ủy nhiệm lập hóa đơn | Invoice Issuance Authorization | — | Ủy nhiệm xuất hóa đơn | Việc bên bán ủy nhiệm bên thứ ba lập hóa đơn; hóa đơn phải thể hiện thông tin của cả bên ủy nhiệm và bên nhận ủy nhiệm. | TAX | regulations/vn-tax-einvoice.md §4.3 |

### Giá thành & định giá tồn kho (Costing & Inventory Valuation)

| Thuật ngữ (VI) | Tiếng Anh | Viết tắt | Tên khác / tên khách hàng hay dùng | Định nghĩa ngắn | Module | Xem thêm |
|---|---|---|---|---|---|---|
| Bảng tính giá thành | Cost Sheet / Costing Run | — | Chạy giá thành | Chứng từ/báo cáo tính tổng và đơn vị giá thành của kỳ, kết chuyển 154 sang 155 và xử lý chênh lệch. | COST | processes/costing.md §6 |
| Bình quân gia quyền | Weighted Average Cost | BQGQ / WAC | Bình quân | Tính đơn giá xuất kho theo giá trung bình của tồn đầu kỳ và nhập trong kỳ; có hai biến thể (cả kỳ và tức thời). | COST | regulations/vn-accounting.md §10 |
| Bình quân gia quyền cả kỳ dự trữ | Periodic Weighted Average | — | BQGQ cuối kỳ | Một đơn giá bình quân duy nhất cho toàn bộ lượng xuất, chỉ tính được vào cuối kỳ. | COST | processes/costing.md §7.1 |
| Bình quân gia quyền tức thời | Moving Average | — | BQGQ liên hoàn, moving average | Tính lại đơn giá bình quân sau mỗi lần nhập; giá xuất lấy theo đơn giá bình quân hiện hành. | COST | processes/costing.md §7.1 |
| Chạy tính lại giá vốn / khóa kỳ kho | Cost Recalculation / Inventory Close | — | Tính lại giá vốn | Quy trình cuối kỳ chốt đơn giá xuất kho (BQGQ cả kỳ, FIFO) và điều chỉnh chênh lệch giá tạm tính. | COST | processes/costing.md §5 |
| Chênh lệch (giá thành) | Variance | — | Biến động chi phí | Khoản chênh giữa chi phí thực tế và định mức, bóc tách theo giá và lượng (NVL, nhân công, SX chung). | COST | processes/costing.md §7.4 |
| Chi phí nguyên vật liệu trực tiếp | Direct Material | — | NVL trực tiếp | Chi phí NVL trực tiếp cấu thành sản phẩm, ghi TK 621 rồi kết chuyển 154. | COST | processes/costing.md §7.3 |
| Chi phí nhân công trực tiếp | Direct Labor | — | NCTT | Lương và các khoản trích theo lương của công nhân trực tiếp sản xuất, ghi TK 622. | COST | processes/costing.md §7.3 |
| Chi phí sản xuất chung | Manufacturing Overhead | — | CP SX chung | Chi phí gián tiếp của phân xưởng (khấu hao, điện, lương quản đốc…), ghi TK 627, phân bổ vào 154 theo công suất bình thường. | COST | processes/costing.md §7.3 |
| Chi phí sản xuất kinh doanh dở dang | Work in Process | WIP | Sản phẩm dở dang, CP dở dang | Giá trị sản phẩm/công trình chưa hoàn thành đang trong quá trình sản xuất, tập hợp tại TK 154. | COST | processes/costing.md §7.3 |
| Chi phí sử dụng máy thi công | Construction Machinery Cost | — | CP máy thi công | Chi phí vận hành máy thi công trong xây lắp, ghi TK 623 rồi kết chuyển 154. | COST | processes/costing.md §7.3 |
| Chi phí thu mua / phân bổ chi phí mua | Landed Cost | — | Chi phí mua hàng | Các chi phí để đưa hàng về kho (vận chuyển, bảo hiểm, thuế nhập khẩu, bốc xếp) cộng vào giá gốc, phân bổ theo trị giá/số lượng/trọng lượng/thể tích. | COST | processes/costing.md §7.2 |
| Công suất bình thường | Normal Capacity | — | — | Sản lượng trung bình đạt được trong điều kiện bình thường; căn cứ phân bổ chi phí SX chung cố định (VAS 02). | COST | processes/costing.md §7.3 |
| Dự phòng giảm giá hàng tồn kho | Inventory Write-down / Provision | — | Dự phòng giảm giá HTK | Khoản ghi giảm giá trị tồn khi giá gốc lớn hơn giá trị thuần có thể thực hiện, ghi Nợ 632 / Có 2294 (TT48/2019). | COST | regulations/vn-accounting.md §11 |
| Định giá tồn kho | Inventory Valuation | — | Tính giá tồn kho | Việc xác định giá trị bằng tiền của hàng tồn kho tại một thời điểm theo phương pháp đã chọn. | COST | processes/costing.md §7.1 |
| Đối tượng tập hợp chi phí và tính giá thành | Cost Object / Cost Collector | — | Đối tượng tính giá thành | Đơn vị để gom chi phí và tính giá thành (sản phẩm, nhóm, phân xưởng, đơn hàng, công đoạn, dự án). | COST | processes/costing.md §3 |
| Giá gốc | Historical Cost / Cost Basis | — | Trị giá gốc | Giá trị ghi nhận ban đầu của hàng tồn kho = giá mua + thuế không hoàn lại + chi phí thu mua − chiết khấu/giảm giá (VAS 02). | COST | processes/costing.md §7.2 |
| Giá thành định mức | Standard Cost | — | Giá thành kế hoạch | Giá thành xây dựng theo định mức, dùng ghi nhận trong kỳ và so sánh với thực tế. | COST | processes/costing.md §7.4 |
| Giá thành sản phẩm | Product Cost | — | — | Toàn bộ chi phí sản xuất (NVL trực tiếp, nhân công trực tiếp, chi phí sản xuất chung) quy về một đơn vị hoặc một lô sản phẩm hoàn thành. | COST | processes/costing.md §1 |
| Giá thành thực tế | Actual Cost | — | — | Giá thành tính theo chi phí thực tế phát sinh trong kỳ. | COST | processes/costing.md §7.4 |
| Giá trị thuần có thể thực hiện được | Net Realizable Value | NRV | — | Giá bán ước tính trừ chi phí ước tính để hoàn thành và tiêu thụ; mốc so sánh để lập dự phòng giảm giá HTK. | COST | processes/costing.md §7.1 |
| Giá vốn hàng bán | Cost of Goods Sold | GVHB / COGS | — | Giá trị tồn kho được kết chuyển thành chi phí khi hàng được bán, ghi vào TK 632 đồng thời với ghi nhận doanh thu. | COST | processes/costing.md §8 |
| Khoản mục chi phí | Cost Element / Component | — | Yếu tố chi phí | Phân loại chi phí (NVL 621 / nhân công 622 / máy thi công 623 / SX chung 627 / thầu phụ) để bóc tách cấu thành giá thành. | COST | processes/costing.md §7.3 |
| Kiểm kê định kỳ | Periodic Inventory System | — | KKĐK | Phương pháp chỉ xác định tồn cuối kỳ qua kiểm kê; theo TT99 không còn dùng TK 611/631 mà dồn vào 154. | COST | regulations/vn-accounting.md §10 |
| Kê khai thường xuyên | Perpetual Inventory System | — | KKTX | Phương pháp theo dõi liên tục số lượng và giá trị tồn kho sau mỗi giao dịch; mặc định trong ERP. | COST | regulations/vn-accounting.md §10 |
| Nhập trước – xuất trước | First-In First-Out | FIFO | — | Giả định hàng nhập trước được xuất trước; giá xuất lấy theo lô nhập cũ nhất còn tồn (LIFO không còn được áp dụng theo VAS 02). | COST | regulations/vn-accounting.md §10 |
| Phương pháp giản đơn | Direct / Simple Costing | — | PP trực tiếp | Giá thành = (dở dang đầu kỳ + chi phí phát sinh − dở dang cuối kỳ − giá trị SP phụ) / số lượng hoàn thành; dùng khi ít mặt hàng, khối lượng lớn. | COST | processes/costing.md §7.3 |
| Phương pháp hệ số | Coefficient Method | — | PP hệ số | Quy đổi nhiều loại sản phẩm về sản phẩm tiêu chuẩn qua hệ số rồi tính giá thành đơn vị chuẩn. | COST | processes/costing.md §7.3 |
| Phương pháp phân bước | Step / Process Costing | — | PP phân bước | Tính giá thành cho quy trình nhiều giai đoạn, có thể tính (kết chuyển tuần tự) hoặc không tính (song song) giá thành bán thành phẩm từng bước. | COST | processes/costing.md §7.3 |
| Phương pháp theo đơn đặt hàng | Job Order Costing | — | PP đơn hàng | Mỗi đơn hàng là một đối tượng tập hợp chi phí và tính giá thành riêng; tính khi đơn hoàn thành. | COST | processes/costing.md §7.3 |
| Phương pháp tỷ lệ | Ratio Method | — | PP tỷ lệ | Tính giá thành từng loại theo tỷ lệ giữa tổng chi phí thực tế và tổng chi phí định mức/kế hoạch. | COST | processes/costing.md §7.3 |
| Sản phẩm hoàn thành tương đương | Equivalent Units | — | SP tương đương | Quy đổi sản phẩm dở dang về số lượng hoàn thành tương đương theo mức độ hoàn thành để đánh giá WIP. | COST | processes/costing.md §7.3 |
| Sản phẩm phụ | By-product | — | Phế liệu thu hồi | Sản phẩm thu được kèm sản phẩm chính, giá trị nhỏ; được loại trừ khỏi tổng chi phí khi tính giá thành SP chính. | COST | processes/costing.md §7.3 |
| Sổ Nhập – Xuất – Tồn theo giá trị | Stock Ledger | N-X-T | Thẻ kho giá trị | Sổ theo dõi biến động số lượng và giá trị tồn kho theo giá vốn, đối chiếu với sổ cái. | COST | processes/costing.md §11 |
| Thẻ tính giá thành | Cost Card | — | Thẻ giá thành | Báo cáo chi tiết cấu thành giá thành theo khoản mục của một đối tượng/đơn hàng. | COST | processes/costing.md §11 |
| Thực tế đích danh | Specific Identification | — | Đích danh | Gán đúng đơn giá thực tế của từng lô/serial được xuất; dùng cho mặt hàng ít chủng loại, giá trị lớn. | COST | regulations/vn-accounting.md §10 |
| Tồn âm | Negative Stock | — | Xuất âm kho | Trạng thái số lượng xuất vượt tồn hiện có; làm sai giá bình quân, cần chính sách và điều chỉnh khi tính lại giá vốn. | COST | processes/costing.md §7.5 |

### Ngân sách (Budgeting & Budget Control)

| Thuật ngữ (VI) | Tiếng Anh | Viết tắt | Tên khác / tên khách hàng hay dùng | Định nghĩa ngắn | Module | Xem thêm |
|---|---|---|---|---|---|---|
| Bản gốc ngân sách | Baseline | — | Ngân sách gốc | Ngân sách đã duyệt và chốt, không được sửa trực tiếp; số hiện hành = bản gốc + thay đổi đã duyệt. | BUD | processes/budgeting.md §6 |
| Bổ sung ngân sách | Budget Supplement | — | Cấp bổ sung | Thêm trần ngân sách lấy từ dự phòng/nguồn được duyệt, làm tăng tổng ngân sách. | BUD | processes/budgeting.md §5A |
| Cam kết | Commitment | — | Cam kết chi | Nghĩa vụ chi dự kiến phát sinh khi duyệt đơn mua hàng/hợp đồng; giữ chỗ ngân sách nhưng chưa ghi sổ tài chính. | BUD | processes/budgeting.md §5B |
| Cảnh báo | Warning / Soft Stop | — | Chặn mềm | Hành vi kiểm soát hiển thị cảnh báo vượt ngân sách nhưng vẫn cho chứng từ đi tiếp. | BUD | processes/budgeting.md §5B |
| Cấu trúc ngân sách | Budget Structure | — | — | Tổ hợp các chiều lập và kiểm soát ngân sách: khoản mục × đơn vị gánh chịu (cost center/dự án) × kỳ × phiên bản. | BUD | processes/budgeting.md §3 |
| Chặn cứng | Hard Stop | — | Chặn hẳn | Hành vi kiểm soát dừng hẳn chứng từ khi vượt ngân sách khả dụng, không cho đi tiếp. | BUD | processes/budgeting.md §5B |
| Chuyển nguồn | Carryforward | — | Chuyển ngân sách sang kỳ sau | Chuyển phần ngân sách chưa dùng và/hoặc cam kết mở cuối kỳ sang kỳ/năm sau theo tham số (CAPEX thường cho, OPEX thường không). | BUD | processes/budgeting.md §7 |
| Dự báo cuốn chiếu | Rolling Forecast | — | Dự báo lăn | Dự báo liên tục cho 12–18 tháng tới, cập nhật định kỳ; không thay bản gốc, dùng để điều hành. | BUD | processes/budgeting.md §5A |
| Dự chi | Pre-encumbrance | — | Giữ chỗ mềm | Số ngân sách bị giữ chỗ mềm khi tạo/duyệt đề nghị mua hàng (PR), chưa phải cam kết chắc chắn. | BUD | processes/budgeting.md §5B |
| Duyệt vượt cấp | Approval Escalation / Override | — | Duyệt ngoại lệ | Định tuyến chứng từ vượt ngân sách tới người có quyền override để duyệt ngoại lệ, có lưu vết. | BUD | processes/budgeting.md §5B |
| Điểm kiểm soát ngân sách | Budget Control Point | — | Điểm check ngân sách | Chứng từ nơi hệ thống gọi kiểm tra ngân sách: PR, PO, hợp đồng, đề nghị thanh toán, đề nghị hoàn/tạm ứng. | BUD | processes/budgeting.md §5B |
| Điều chỉnh ngân sách | Budget Revision | — | Sửa ngân sách | Thay đổi trần của một khoản mục bằng cách tạo phiên bản mới có duyệt, giữ bản gốc bất biến. | BUD | processes/budgeting.md §6 |
| Điều chuyển ngân sách | Budget Transfer / Virement | — | Chuyển trần ngân sách | Chuyển trần giữa các khoản mục/đơn vị/kỳ với tổng không đổi (net-zero). | BUD | processes/budgeting.md §7 |
| Giữ chỗ ngân sách | Budget Commitment | — | Reservation | Số ngân sách tạm giữ khi tạo PR/PO để tránh chi vượt; được nhả khi hủy chứng từ hoặc chuyển thành thực chi khi có hóa đơn. | BUD | processes/budgeting.md §5B |
| Kế toán quản trị | Management Accounting | — | Kế toán quản trị nội bộ | Mảng kế toán phục vụ điều hành nội bộ (gồm lập dự toán/ngân sách), không bắt buộc theo luật và không ảnh hưởng BCTC. | BUD | processes/budgeting.md §1 |
| Khoản mục ngân sách | Budget Line Item / Commitment Item | — | Budgetary position | Đơn vị phân loại ngân sách (vd chi phí văn phòng, lương), ánh xạ tới một/nhiều tài khoản sổ cái để lấy số thực tế. | BUD | processes/budgeting.md §3 |
| Kiểm soát ngân sách | Budget Control | — | — | Cơ chế so giá trị chứng từ chi với số ngân sách khả dụng tại điểm phát sinh và quyết định cho đi tiếp, cảnh báo hay chặn. | BUD | processes/budgeting.md §5B |
| Kiểm tra ngân sách | Budget Check | — | Check ngân sách | Kiểm tra tổng (đã chi + đã cam kết + chứng từ hiện tại) không vượt ngân sách khả dụng theo chiều phòng ban/khoản mục/kỳ. | BUD | processes/budgeting.md §5B |
| Lập ngân sách từ dưới lên | Bottom-up Budgeting | — | — | Các bộ phận tự lập dự toán rồi tổng hợp, thương lượng lên trên. | BUD | processes/budgeting.md §5A |
| Lập ngân sách từ trên xuống | Top-down Budgeting | — | — | Cấp trên rải chỉ tiêu/mục tiêu xuống các bộ phận. | BUD | processes/budgeting.md §5A |
| Mô hình ngân sách | Budget Model | — | — | Tập hợp chiều, kỳ và khoản mục được gom thành một khối để nhập liệu và kiểm soát ngân sách. | BUD | processes/budgeting.md §3 |
| Ngân sách | Budget | — | Dự toán | Dự toán tài chính đã được duyệt, thể hiện trần chi hoặc mục tiêu thu theo khoản mục và kỳ; là nền để kiểm soát chi tiêu. | BUD | processes/budgeting.md §1 |
| Ngân sách tiền mặt | Cash Budget | — | Dự toán dòng tiền | Dự toán dòng thu–chi tiền theo kỳ phục vụ quản trị thanh khoản. | BUD | processes/budgeting.md §5A |
| Ngân sách tăng dần | Incremental Budgeting | — | — | Phương pháp lấy số kỳ trước điều chỉnh tăng/giảm theo tỷ lệ. | BUD | processes/budgeting.md §5A |
| Ngân sách từ số 0 | Zero-based Budgeting | ZBB | — | Phương pháp lập lại ngân sách từ đầu mỗi kỳ, biện minh từng khoản chi thay vì dựa vào kỳ trước. | BUD | processes/budgeting.md §5A |
| Ngân sách vs cam kết vs thực tế | Budget vs Commitment vs Actual | BvCvA | — | Báo cáo tách ba đại lượng và số khả dụng còn lại. | BUD | processes/budgeting.md §11 |
| Ngân sách vs thực tế | Budget vs Actual | BvA | — | Báo cáo so sánh ngân sách với số thực hiện, tính chênh lệch và tỷ lệ. | BUD | processes/budgeting.md §11 |
| Nhóm ngân sách | Budget Group / Pool | — | Quỹ ngân sách | Tập tổ hợp chiều được gộp chung để kiểm tra ngân sách lần hai ở cấp quỹ sau kiểm tra chi tiết. | BUD | processes/budgeting.md §5B |
| Phân bổ ngân sách | Budget Allocation / Distribution | — | Rải ngân sách | Rải ngân sách năm xuống từng kỳ và từng đơn vị con. | BUD | processes/budgeting.md §5A |
| Phân tích chênh lệch | Variance Analysis | — | Phân tích biến động | Diễn giải lệch giữa thực tế và ngân sách; dương ở chi phí là bất lợi, dương ở doanh thu là thuận lợi. | BUD | processes/budgeting.md §11 |
| Phiên bản ngân sách | Budget Version / Scenario | — | Kịch bản ngân sách | Một bản ngân sách (Gốc, Điều chỉnh, Dự báo, What-if); chỉ một phiên bản được chọn làm phiên bản kiểm soát tại một thời điểm. | BUD | processes/budgeting.md §6 |
| Phong tỏa | Encumbrance | — | Khóa ngân sách | Phần ngân sách bị khóa cho một cam kết (PO/hợp đồng); được tất toán dần khi chuyển thành thực chi. | BUD | processes/budgeting.md §5B |
| Số khả dụng | Funds Available / Budget Available | — | Ngân sách còn lại | Số còn được chi = Ngân sách điều chỉnh × (1 + dung sai) − (Thực tế + Cam kết + Dự chi), tùy cấu hình thành phần. | BUD | processes/budgeting.md §7 |
| Tất toán cam kết | Commitment Liquidation / Relieve | — | Nhả cam kết | Việc giảm cam kết/phong tỏa khi nó chuyển thành thực chi, tránh trừ ngân sách hai lần. | BUD | processes/budgeting.md §7 |
| Thực tế | Actual | — | Số thực hiện | Số đã ghi sổ cái ở module nguồn (hóa đơn, lương, khấu hao, giá vốn) mà ngân sách đối chiếu để đánh giá. | BUD | processes/budgeting.md §5B |
| Tốc độ tiêu ngân sách | Burn Rate | — | — | Mức độ và nhịp độ sử dụng ngân sách so với tiến độ thời gian. | BUD | processes/budgeting.md §11 |
| Tỷ giá kế hoạch | Planning Rate | — | Tỷ giá ngân sách | Tỷ giá cố định dùng khi lập và đối chiếu ngân sách ngoại tệ, tách biệt với tỷ giá thực tế. | BUD | processes/budgeting.md §7 |

## Thuật ngữ ngành: xây dựng, logistics, thương mại – phân phối

> Phần này của glossary tổng chuẩn hóa thuật ngữ **đặc thù ba ngành**: xây dựng (construction), logistics (giao nhận – vận tải – kho/3PL – hải quan) và thương mại – phân phối (trading & distribution). Thuật ngữ nền dùng chung (kế toán, thuế–hóa đơn, mua hàng, bán hàng, kho, công nợ) nằm ở các phần khác của glossary — ở đây chỉ nêu phần đặc thù ngành.
>
> **Quy ước:** tiếng Việt có dấu; tên tiếng Anh chuẩn để ở cột *Tiếng Anh* (tương đương việc chú tiếng Anh ở lần dùng đầu — xem `references/conventions.md` §10). Một khái niệm = một tên tiếng Việt ưu tiên; tên gọi khác / tên khách hàng hay dùng để ở cột *Tên khác*. Cột *Xem thêm* trỏ tới file tham chiếu (và § khi hữu ích) nơi khái niệm được giải thích.
>
> **Chế độ kế toán (regime in force) tại 2026-10-20:** Thông tư 99/2025/TT-BTC (hiệu lực 01/01/2026, thay TT200/2014); doanh nghiệp nhỏ và vừa có thể vẫn dùng TT133/2016. Số hiệu tài khoản trong định nghĩa theo TT99/2025; khác biệt TT133 được ghi chú ngay trong định nghĩa khi có ảnh hưởng. Chi tiết: `references/regulations/vn-accounting.md`.

### Xây dựng (Construction)

| Thuật ngữ (VI) | Tiếng Anh | Viết tắt | Tên khác / tên khách hàng hay dùng | Định nghĩa ngắn (1–2 câu, dùng được trong tài liệu dự án) | Module | Xem thêm |
|---|---|---|---|---|---|---|
| Ban quản lý dự án | Project Management Unit | PMU | Ban QLDA | Đơn vị thay chủ đầu tư quản lý dự án đầu tư xây dựng (phổ biến với dự án vốn nhà nước). | PRJ | references/industries/construction.md §1.1 |
| Bản vẽ thi công | Construction / Shop Drawing |  |  | Bản vẽ dùng để thi công, quản lý theo phiên bản (chỉ bản for-construction mới nhất có hiệu lực). | DCTRL | references/industries/construction.md §4.10 |
| Bảng tiên lượng / khối lượng | Bill of Quantities | BOQ |  | Danh mục công tác và khối lượng mời thầu/thi công. | EST | references/industries/construction.md §4.1 |
| Bảo lãnh bảo hành | Warranty Guarantee |  |  | Bảo lãnh ngân hàng trong thời gian bảo hành, có thể thay cho tiền giữ lại bảo hành. | CTR | references/industries/construction.md §4.3 |
| Bảo lãnh tạm ứng | Advance Payment Guarantee |  |  | Bảo lãnh cho khoản tạm ứng; theo NĐ 210/2026 duy trì đến khi thu hồi hết tạm ứng. | CTR | references/industries/construction.md §4.3 |
| Bảo lãnh thực hiện hợp đồng | Performance Guarantee |  |  | Bảo lãnh ngân hàng đảm bảo nhà thầu thực hiện hợp đồng. | CTR | references/industries/construction.md §4.3 |
| Biên bản bàn giao đưa vào sử dụng | Handover Record |  | Biên bản bàn giao | Chứng từ bàn giao công trình/hạng mục đưa vào sử dụng; là mốc bắt đầu thời hạn bảo hành. | STL | references/industries/construction.md §4.11 |
| Ca máy | Machine Shift |  |  | Đơn vị đo mức sử dụng máy thi công (một ca). | EQP | references/industries/construction.md §4.5 |
| Cấp công trình | Construction Grade |  |  | Phân cấp công trình quyết định thời hạn bảo hành, yêu cầu quản lý chất lượng và thẩm quyền. | QHSE | references/industries/construction.md §4.10 |
| Chỉ huy trưởng công trường | Site Commander / Construction Manager |  | CHT công trường | Người điều hành thi công tại công trường, duyệt yêu cầu vật tư và nghiệm thu nội bộ. | PRJ | references/industries/construction.md §4.2 |
| Chi phí chung | Overhead / Indirect Cost |  | Chi phí gián tiếp | Chi phí gián tiếp của công trình; trong thi công tập hợp vào TK 627 và phân bổ về hạng mục theo tiêu thức cấu hình. | COST | references/industries/construction.md §4.1, §4.9 |
| Chi phí sản xuất kinh doanh dở dang | Work in Progress | WIP | Chi phí dở dang; WIP công trình | Chi phí thi công chưa kết chuyển giá vốn, treo ở TK 154 theo công trình (TT133: mọi chi phí tập hợp thẳng vào 154). | COST | references/industries/construction.md §4.9 |
| Chi phí sử dụng máy thi công | Construction Machinery Cost |  | Chi phí máy thi công (TK 623) | Chi phí vận hành máy thi công, tập hợp vào TK 623 (tiểu khoản 6231-6238). | EQP | references/industries/construction.md §4.5 |
| Chi phí trực tiếp | Direct Cost |  |  | Chi phí vật liệu + nhân công + máy thi công trực tiếp cho công tác xây dựng trong dự toán. | EST | references/industries/construction.md §4.1 |
| Chỉ số giá xây dựng | Construction Price Index |  |  | Hệ số điều chỉnh giá hợp đồng theo biến động giá thị trường. | CTR | references/industries/construction.md §4.3 |
| Chủ đầu tư | Investor / Owner (Party A) |  | Phía A; chủ dự án | Bên bỏ vốn, ký và thanh toán hợp đồng cho nhà thầu; vốn hóa chi phí đầu tư vào TK 241 rồi kết chuyển TSCĐ/BĐS khi quyết toán. | PRJ | references/industries/construction.md §1.1, §4.11.2 |
| Chuẩn mực kế toán số 15 — Hợp đồng xây dựng | Construction Contracts (VAS 15) | VAS 15 |  | Chuẩn mực ghi nhận doanh thu/chi phí hợp đồng xây dựng theo mức độ hoàn thành và dự phòng khoản lỗ hợp đồng. | PROG | references/industries/construction.md §2; references/regulations/vn-accounting.md §8 |
| Cơ cấu phân rã công việc | Work Breakdown Structure | WBS |  | Phân rã công trình thành các công tác quản lý được. | PRJ | references/industries/construction.md §4.2 |
| Cơ điện công trình | Mechanical, Electrical & Plumbing | MEP | Hệ cơ điện | Nhóm công tác hệ thống cơ, điện, cấp thoát nước của công trình. | PRJ | references/industries/construction.md §1.2 |
| Dự báo chi phí hoàn thành | Estimate at Completion | EAC |  | Dự báo tổng chi phí khi hoàn thành công trình để cảnh báo vượt ngân sách và ước tính lãi lỗ dự kiến. | COST | references/industries/construction.md §4.9 |
| Dự phòng bảo hành công trình | Construction Warranty Provision |  | Quỹ bảo hành | Trích trước chi phí bảo hành theo tỷ lệ (TK 352–3524), sử dụng dần và hoàn nhập phần còn thừa cuối hạn. | STL | references/industries/construction.md §4.11.1 |
| Dự phòng khoản lỗ hợp đồng | Provision for Foreseeable Loss |  |  | Trích trước khi dự kiến tổng chi phí hợp đồng vượt tổng doanh thu (VAS 15); ghi Nợ 632/Có 352. | STL | references/industries/construction.md §4.11.1 |
| Dự toán xây dựng | Construction Cost Estimate |  | Dự toán công trình | Chi phí dự tính để xây dựng công trình/hạng mục, lập từ định mức và đơn giá. | EST | references/industries/construction.md §4.1 |
| Định mức | Norm |  |  | Hao phí chuẩn vật liệu/nhân công/máy cho một đơn vị khối lượng công tác (Bộ Xây dựng ban hành theo TT 38/2026). | EST | references/industries/construction.md §4.1 |
| Đo bóc khối lượng | Quantity Take-off |  |  | Bóc tách khối lượng từng công tác từ bản vẽ để nhân với đơn giá. | EST | references/industries/construction.md §4.1 |
| Đơn giá xây dựng | Unit Price |  |  | Giá cho một đơn vị công tác = định mức × giá vật liệu/nhân công/ca máy theo khu vực và thời điểm. | EST | references/industries/construction.md §4.1 |
| Giá dự thầu | Bid Price |  | Giá bỏ thầu | Giá nhà thầu bỏ thầu; có thể khác dự toán do chiến lược đấu thầu, nhưng không nên thấp hơn chi phí trực tiếp + thuế. | EST | references/industries/construction.md §4.1 |
| Giao khoán | Labor Package / Piecework |  | Khoán đội; khoán nhân công | Khoán khối lượng hoặc hạng mục cho đội/tổ theo đơn giá khoán. | SUB | references/industries/construction.md §4.7 |
| Giao thẳng chân công trình | Direct Delivery to Site |  |  | Vật tư rời giao thẳng tới công trình không qua kho nhưng vẫn ghi nhận chi phí theo hạng mục. | SITE | references/industries/construction.md §4.4 |
| Giữ lại | Retention |  | Tiền giữ lại; phần giữ lại | Phần giữ lại mỗi kỳ hoặc sau bàn giao để đảm bảo nghĩa vụ của nhà thầu. | CTR | references/industries/construction.md §4.3 |
| Hạng mục công trình | Work Item |  |  | Bộ phận công trình dùng để quản lý chi phí và tiến độ. | PRJ | references/industries/construction.md §4.2 |
| Hồ sơ thanh toán / Phiếu giá | Interim Payment Certificate | IPC | Phiếu giá; bảng xác định giá trị khối lượng hoàn thành | Chứng từ đề nghị thanh toán giá trị khối lượng hoàn thành trong kỳ với chủ đầu tư. | PROG | references/industries/construction.md §4.8 |
| Hợp đồng đơn giá điều chỉnh | Adjustable Unit Price Contract |  |  | Hợp đồng theo đơn giá được điều chỉnh theo chỉ số giá/biến động giá vật liệu. | CTR | references/industries/construction.md §4.3 |
| Hợp đồng EPC / chìa khóa trao tay | EPC / Turnkey Contract | EPC | Chìa khóa trao tay | Một nhà thầu thực hiện cả thiết kế, cung cấp thiết bị và thi công, bàn giao công trình vận hành được. | CTR | references/industries/construction.md §4.3 |
| Hợp đồng trọn gói | Lump-sum Contract |  | HĐ trọn gói | Hợp đồng giá cố định cho toàn bộ phạm vi công việc, ít cơ chế điều chỉnh giá. | CTR | references/industries/construction.md §4.3 |
| Kho công trường | Site Warehouse |  | Kho công trình | Kho đặt tại công trình để quản lý nhập–xuất–tồn vật tư theo hạng mục; có thể điều chuyển giữa các công trường. | SITE | references/industries/construction.md §4.4 |
| Khoản mục chi phí | Cost Element |  |  | Nhóm chi phí: vật liệu (621), nhân công (622), máy thi công (623), chung (627), thầu phụ — kết chuyển về 154 (TT133: không tách 621/622/623/627, gộp vào 154). | COST | references/industries/construction.md §4.9 |
| Khối lượng phát sinh | Variation / Change |  |  | Khối lượng hoặc đơn giá tăng/giảm so với hợp đồng, phải lập phụ lục được duyệt. | CTR | references/industries/construction.md §4.3 |
| Kỹ sư khối lượng / dự toán | Quantity Surveyor | QS | Kỹ sư QS; kỹ sư dự toán | Người bóc khối lượng, lập dự toán và tổng hợp khối lượng nghiệm thu làm căn cứ thanh toán. | EST | references/industries/construction.md §4.1, §4.8 |
| Lãi lỗ công trình | Project P&L |  | Hiệu quả công trình | Doanh thu trừ giá vốn tập hợp theo từng công trình, dùng đánh giá hiệu quả. | COST | references/industries/construction.md §4.9 |
| Mô hình thông tin công trình | Building Information Modeling | BIM |  | Mô hình số công trình; NĐ 207/2026 bổ sung điều khuyến khích ứng dụng trong thi công/nghiệm thu. | DCTRL | references/industries/construction.md §4.10 |
| Ngân sách gốc | Baseline Budget |  | Ngân sách baseline; dự toán trúng thầu | Dự toán trúng thầu được chốt làm ngân sách gốc của dự án; thay đổi sau đó phải qua phụ lục/điều chỉnh có vết. | PRJ | references/industries/construction.md §4.2 |
| Nghiệm thu chất lượng / công việc | Quality Inspection & Acceptance |  | Nghiệm thu nội bộ | Nghiệm thu công việc theo hồ sơ quản lý chất lượng; là điều kiện để lập phiếu giá và quyết toán. | QHSE | references/industries/construction.md §4.10 |
| Nghiệm thu khối lượng | Volume / Work Acceptance |  | Nghiệm thu khối lượng hoàn thành | Xác nhận khối lượng và chất lượng hoàn thành làm căn cứ thanh toán. | PROG | references/industries/construction.md §4.8 |
| Nhà phát triển bất động sản | Real Estate Developer |  | Chủ đầu tư BĐS | DN xây để bán: chi phí vào 154→155/156, doanh thu bán BĐS theo VAS 14 (không dùng VAS 15/TK 337), vốn hóa lãi vay theo VAS 16. | PRJ | references/industries/construction.md §1.1, §4.11.2 |
| Nhật ký / bảng kê ca máy | Machine Shift Log |  | Bảng kê ca máy | Chứng từ ghi nhận ca máy theo công trình × hạng mục, làm căn cứ tính chi phí máy thi công (TK 623). | EQP | references/industries/construction.md §4.5 |
| Nhật ký thi công | Site Diary / Construction Log |  |  | Ghi chép hằng ngày tại công trường, là căn cứ pháp lý (NĐ 207/2026). | QHSE | references/industries/construction.md §4.10 |
| Phân tích đơn giá chi tiết | Detailed Unit Price Analysis |  |  | Tách đơn giá một công tác thành hao phí vật liệu/nhân công/máy theo định mức và giá tại thời điểm. | EST | references/industries/construction.md §4.1 |
| Phụ lục hợp đồng | Contract Appendix (Variation Order) |  | Phụ lục; variation order | Văn bản điều chỉnh giá trị/khối lượng/đơn giá hợp đồng; phải được duyệt trước khi nghiệm thu, thanh toán phần phát sinh. | CTR | references/industries/construction.md §4.3 |
| Quản lý an toàn, sức khỏe, môi trường | Health, Safety & Environment | HSE | An toàn lao động | Quản lý an toàn lao động, sự cố và môi trường tại công trường (checklist, sự cố, khắc phục). | QHSE | references/industries/construction.md §4.10 |
| Quyết toán hợp đồng (A-B) | Contract Final Settlement |  |  | Đối chiếu và chốt giá trị thực hiện giữa chủ đầu tư (A) và nhà thầu (B) khi kết thúc hợp đồng. | STL | references/industries/construction.md §4.11 |
| Quyết toán vốn đầu tư | Investment Final Account |  |  | Chốt tổng chi phí dự án phía chủ đầu tư (bắt buộc với dự án vốn nhà nước). | STL | references/industries/construction.md §4.11 |
| Tạm ứng hợp đồng | Contract Advance |  |  | Khoản ứng trước theo hợp đồng, thu hồi dần theo tiến độ thanh toán. | CTR | references/industries/construction.md §4.3 |
| Tập hợp chi phí theo công trình | Job Costing (Project Costing) |  | Kế toán chi phí công trình | Tập hợp mọi chi phí theo Công trình × Hạng mục × Khoản mục và kết chuyển về TK 154 (WIP công trình). | COST | references/industries/construction.md §4.9; references/processes/costing.md |
| Thanh toán theo tiến độ hợp đồng xây dựng | Progress Billing (VAS 15) |  | Ghi nhận doanh thu theo tiến độ (VAS 15) | Ghi nhận doanh thu hợp đồng xây dựng theo mức độ hoàn thành (VAS 15): (a) theo tiến độ kế hoạch — Nợ 337/Có 511; (b) theo khối lượng nghiệm thu — Nợ 131/Có 511 (không dùng 337). | PROG | references/industries/construction.md §4.8 |
| Thầu phụ | Subcontractor |  | Nhà thầu phụ | Nhà thầu nhận lại một phần công việc từ nhà thầu chính; có tạm ứng, nghiệm thu, giữ lại riêng. | SUB | references/industries/construction.md §4.7 |
| Thu hồi tạm ứng | Advance Recovery |  |  | Khấu trừ dần tiền tạm ứng trên mỗi hồ sơ thanh toán khối lượng. | CTR | references/industries/construction.md §4.3 |
| Thu nhập chịu thuế tính trước | Pre-determined Taxable Income |  | Lãi định mức | Khoản lợi nhuận định mức cộng vào dự toán xây dựng theo tỷ lệ quy định trước thuế GTGT. | EST | references/industries/construction.md §4.1 |
| Tiền bảo hành | Warranty Retention |  |  | Khoản giữ lại hoặc bảo lãnh trong thời gian bảo hành công trình. | STL | references/industries/construction.md §4.11 |
| Tổng mức đầu tư | Total Investment | TMĐT | TMĐT | Toàn bộ chi phí dự tính của dự án phía chủ đầu tư (gồm xây dựng, thiết bị, QLDA, tư vấn, GPMB, dự phòng). | EST | references/industries/construction.md §4.1 |
| Tổng thầu | General Contractor | GC | Nhà thầu chính | Nhà thầu ký hợp đồng chính với chủ đầu tư, chịu trách nhiệm toàn bộ công trình và có thể giao lại một phần cho thầu phụ. | PRJ | references/industries/construction.md §1.1 |
| Tư vấn giám sát | Construction Supervision Consultant | CSC |  | Đơn vị giám sát xác nhận khối lượng và chất lượng làm căn cứ nghiệm thu, thanh toán. | QHSE | references/industries/construction.md §4.10 |
| Xây dựng cơ bản dở dang | Construction in Progress | CIP (XDCB dở dang) | XDCB dở dang | Chi phí đầu tư xây dựng bên chủ đầu tư treo ở TK 241 trước khi kết chuyển sang TSCĐ/BĐS khi quyết toán được duyệt. | PRJ | references/industries/construction.md §4.11.2 |
| Yêu cầu thông tin | Request for Information | RFI |  | Yêu cầu làm rõ thiết kế/thi công, có thời hạn trả lời và ảnh hưởng tiến độ. | DCTRL | references/industries/construction.md §4.10 |
| Yêu cầu vật tư công trường | Site Material Request | MR | Phiếu đề nghị vật tư | Đề nghị cấp vật tư suy từ khối lượng × định mức của hạng mục sắp thi công; cảnh báo khi lũy kế vượt định mức. | SITE | references/industries/construction.md §4.4 |

### Logistics (giao nhận – vận tải – kho/3PL – hải quan)

| Thuật ngữ (VI) | Tiếng Anh | Viết tắt | Tên khác / tên khách hàng hay dùng | Định nghĩa ngắn (1–2 câu, dùng được trong tài liệu dự án) | Module | Xem thêm |
|---|---|---|---|---|---|---|
| Bản lược khai hàng hóa | Manifest |  |  | Danh sách toàn bộ hàng hóa trên một chuyến tàu/chuyến bay. | FWD | references/industries/logistics.md §4.1 |
| Bảng kê đối chiếu công nợ | Statement of Account | SOA | Bảng đối chiếu công nợ; sao kê đại lý | Bảng đối chiếu công nợ với đại lý/đối tác làm cơ sở bù trừ (netting) và quyết toán. | BIL | references/industries/logistics.md §4.7 |
| Bên cung cấp dịch vụ logistics thứ ba | Third-Party Logistics | 3PL | 3PL; nhà cung cấp dịch vụ logistics | Doanh nghiệp cung cấp kho/vận tải/giao nhận cho chủ hàng khác; hàng giữ hộ theo dõi ngoài bảng (TK 002) và theo chủ hàng. | WMS | references/industries/logistics.md §4.4 |
| Biên bản giao hàng | Proof of Delivery | POD |  | Chứng từ xác nhận đã giao hàng có ký nhận, cơ sở để quyết toán chuyến và lập hóa đơn. | TMS | references/industries/logistics.md §4.3 |
| Biểu cước | Tariff / Rate |  | Bảng cước | Bảng giá mua (buy rate) và giá bán (sell rate) theo tuyến, hãng, loại container/trọng lượng, có hiệu lực từ–đến. | FWD | references/industries/logistics.md §4.2 |
| Bù trừ công nợ | Netting |  | Cấn trừ công nợ | Đối chiếu và bù trừ khoản phải thu và phải trả với cùng một đại lý theo kỳ (có SOA xác nhận), quyết toán số ròng. | BIL | references/industries/logistics.md §4.7 |
| Cảng đi / cảng đến | Port of Loading / Discharge | POL/POD | Cảng xếp/dỡ | Cảng hoặc sân bay xếp hàng và dỡ hàng của lô; quản lý theo mã UN/LOCODE. | FWD | references/industries/logistics.md §4.1 |
| Cất hàng vào vị trí | Putaway |  |  | Xếp hàng vào vị trí lưu trữ theo chiến lược cấu hình sau khi nhận. | WMS | references/industries/logistics.md §4.4 |
| Chặng đầu / chặng cuối | First Mile / Last Mile |  |  | Chặng gom hàng đầu nguồn và chặng giao hàng cuối tới người nhận. | TMS | references/industries/logistics.md §1 |
| Chi hộ | Disbursement |  | Chi hộ khách; disbursement; chi hộ pass-through | Khoản doanh nghiệp chi thay khách (thuế XNK, phí cảng) rồi thu lại; không phải doanh thu/chi phí, theo dõi qua TK 138. | BIL | references/industries/logistics.md §4.6 |
| Chi phí ước tính theo lô | Estimated Cost (Accrual) |  | Trích trước chi phí lô | Trích trước chi phí mua ngoài khi hãng/đại lý chưa xuất hóa đơn (TK 335) để chốt lãi lỗ lô đúng kỳ. | BIL | references/industries/logistics.md §4.6 |
| Co-loader | Co-loader |  |  | Forwarder khác nhận gom chung hàng khi mình không đủ hàng đóng nguyên container. | FWD | references/industries/logistics.md §4.2 |
| Dịch vụ giá trị gia tăng | Value-Added Services | VAS |  | Dán nhãn, đóng gói lại, kiểm đếm, lắp ráp... thực hiện trong kho, tính phí theo khối lượng công việc. | WMS | references/industries/logistics.md §4.4 |
| Đại lý làm thủ tục hải quan | Customs Broker/Agent |  |  | Thương nhân đủ điều kiện được khai thuê và làm thủ tục hải quan thay chủ hàng. | CUS | references/industries/logistics.md §4.5 |
| Đại lý nước ngoài | Overseas Agent |  | Đại lý đối tác; network agent | Đối tác forwarder ở nước ngoài phối hợp đầu kia của lô; đối soát công nợ qua SOA và bù trừ (netting). | BIL | references/industries/logistics.md §4.7 |
| Đặt chỗ | Booking |  |  | Giữ chỗ với hãng tàu/hãng bay/co-loader, có số booking và thời hạn cut-off. | FWD | references/industries/logistics.md §4.1, §4.2 |
| Địa điểm thu gom hàng lẻ | Container Freight Station | CFS |  | Khu kho/bãi gom, tách, đóng ghép hàng lẻ chung container của nhiều chủ hàng. | WMS | references/industries/logistics.md §4.4 |
| Điều kiện giao hàng quốc tế | Incoterms |  |  | Bộ quy tắc phân chia trách nhiệm, chi phí và rủi ro giữa người bán và người mua (Incoterms 2020). | FWD | references/industries/logistics.md §4.1 |
| Đóng gói | Packing |  |  | Đóng gói hàng đã soạn trước khi giao xuất. | WMS | references/industries/logistics.md §4.4 |
| Giá mua cước / giá bán cước | Buy Rate / Sell Rate |  |  | Giá mua từ hãng/đại lý và giá bán cho khách; chênh lệch tạo lợi nhuận gộp của lô. | FWD | references/industries/logistics.md §4.2 |
| Giao nhận vận tải | Freight Forwarding | FWD | Forwarding; forwarder; giao nhận | Thu xếp vận chuyển hàng cho khách mà không trực tiếp sở hữu phương tiện vận tải chính; phát hành vận đơn nhà. | FWD | references/industries/logistics.md §4.1 |
| Giấy báo có | Credit Note | C/N | Credit Note; C/N | Chứng từ giảm công nợ hoặc hoàn phí cho khách/đại lý. | BIL | references/industries/logistics.md §4.6 |
| Giấy báo hàng đến | Arrival Notice | A/N |  | Thông báo cho consignee khi hàng đến cảng/sân bay, kèm các khoản phí phải nộp. | FWD | references/industries/logistics.md §4.1 |
| Giấy báo nợ | Debit Note | D/N | Debit Note; D/N | Chứng từ liệt kê các khoản phải thu khách/đại lý, gồm cả phần chi hộ; khác hóa đơn GTGT. | BIL | references/industries/logistics.md §4.6 |
| Giới hạn trách nhiệm | Limitation of Liability |  |  | Mức bồi thường tối đa của DN logistics; nếu không thỏa thuận và khách không khai giá trị thì tối đa 500 triệu VND/yêu cầu (NĐ 163/2017). | FWD | references/industries/logistics.md §2 |
| Gom hàng / hàng ghép | Consolidation | Consol | Ghép cont; consol | Ghép nhiều lô hàng lẻ (LCL) của nhiều chủ hàng vào chung một container/chuyến. | FWD | references/industries/logistics.md §1, §4.1 |
| Hàng giữ hộ | Goods Held in Custody |  | Hàng gửi giữ hộ; consigned-in | Hàng của chủ hàng khác do 3PL giữ hộ, theo dõi ngoài bảng (TK 002) theo chủ hàng, không ghi vào 156. | WMS | references/industries/logistics.md §4.4 |
| Hàng lẻ ghép container | Less than Container Load | LCL |  | Nhiều chủ hàng ghép chung một container (consol). | FWD | references/industries/logistics.md §4.1 |
| Hãng vận chuyển | Carrier |  | Hãng tàu/hãng bay/nhà xe | Đơn vị thực hiện vận chuyển (hãng tàu, hãng bay, nhà xe); theo dõi công nợ phải trả hãng (carrier payables). | FWD | references/industries/logistics.md §5 |
| Hệ thống quản lý kho | Warehouse Management System | WMS |  | Phần mềm quản lý nhập, lưu trữ theo vị trí/lô/hạn dùng, xuất và kiểm kê. | WMS | references/industries/logistics.md §4.4 |
| Hệ thống quản lý vận tải | Transportation Management System | TMS |  | Phần mềm điều vận, quản lý chuyến, xe, tài xế và chi phí vận tải đường bộ. | TMS | references/industries/logistics.md §4.3 |
| Hệ thống thông quan tự động | VNACCS/VCIS |  |  | Hệ thống hải quan điện tử Việt Nam để tiếp nhận tờ khai, phân luồng và thông quan. | CUS | references/industries/logistics.md §4.5 |
| Kho ngoại quan | Bonded Warehouse |  |  | Kho lưu hàng chưa nộp thuế, chịu giám sát hải quan, theo dõi theo tờ khai và thời hạn lưu. | CUS | references/industries/logistics.md §4.5 |
| Khoản mục phí | Charge Code |  | Mã phí | Mã loại phí trên lô, gắn bên bán (sell) và/hoặc bên mua (buy), tiền tệ và cờ chịu VAT. | BIL | references/industries/logistics.md §4.1 |
| Khối lượng toàn bộ container | Verified Gross Mass | VGM |  | Khối lượng container khai báo bắt buộc trước khi xếp lên tàu. | FWD | references/industries/logistics.md §4.1 |
| Kiểm kê định kỳ | Cycle Count |  | Kiểm kho quay vòng | Đếm tồn kho định kỳ theo vị trí/chủ hàng và xử lý chênh lệch. | WMS | references/industries/logistics.md §4.4 |
| Lãi lỗ theo lô | Job Profit & Loss | Job P&L | Lãi gộp theo lô; profit per shipment | Chênh lệch doanh thu bán (sell) trừ chi phí mua ngoài (buy) và phân bổ chi phí chung của một lô. | BIL | references/industries/logistics.md §4.6 |
| Lệnh điều xe | Dispatch Order |  | Lệnh điều động | Chứng từ điều động xe + tài xế + tuyến cho một chuyến, hoặc chỉ định thuê xe ngoài. | TMS | references/industries/logistics.md §4.3 |
| Lệnh giao hàng | Delivery Order | D/O |  | Chứng từ cho phép nhận hàng tại cảng/kho sau khi hoàn tất nghĩa vụ. | FWD | references/industries/logistics.md §4.1 |
| Lô hàng / Hồ sơ lô | Shipment / Job File |  | Mã lô; job; hồ sơ lô hàng | Đơn vị trung tâm gắn mọi doanh thu, chi phí mua ngoài, chứng từ và mốc thời gian; có mã lô (job no.) để tính lãi lỗ theo lô. | FWD | references/industries/logistics.md §4.1 |
| Loại container | Container Type |  | 20GP/40GP/40HC/40RF | Phân loại container theo kích thước và đặc tính (khô, lạnh), ảnh hưởng cước và sức chứa. | FWD | references/industries/logistics.md §5 |
| Loại hình (hải quan) | Customs Regime / Type Code |  | Mã loại hình | Mã xác định bản chất nghiệp vụ XNK (kinh doanh, gia công, sản xuất xuất khẩu, tạm nhập tái xuất...). | CUS | references/industries/logistics.md §4.5 |
| Mã số nhân viên đại lý hải quan | Customs Broker Staff Code |  |  | Mã do cơ quan hải quan cấp cho nhân viên đủ điều kiện được khai thuê thủ tục hải quan. | CUS | references/industries/logistics.md §4.5 |
| Mốc thời gian lô hàng | Milestones | ETD/ETA | ETD/ATD, ETA/ATA, cut-off | Các mốc kế hoạch và thực tế của lô (khởi hành, đến, cut-off) để theo dõi và tracking. | FWD | references/industries/logistics.md §4.1 |
| Nguyên container | Full Container Load | FCL |  | Hàng đủ một container của một chủ hàng. | FWD | references/industries/logistics.md §4.1 |
| Nhà vận tải không tàu | Non-Vessel Operating Common Carrier | NVOCC |  | Nhà vận tải không sở hữu tàu nhưng phát hành vận đơn và mua chỗ của hãng tàu. | FWD | references/industries/logistics.md §1 |
| Nhận hàng vào kho | Receiving |  |  | Nhận và kiểm đếm hàng vào kho, đối chiếu với thông báo hàng đến (ASN). | WMS | references/industries/logistics.md §4.4 |
| Phân luồng | Customs Channel Classification |  | Luồng xanh/vàng/đỏ | Kết quả phân loại kiểm tra tờ khai: luồng xanh (thông quan ngay), vàng (kiểm hồ sơ), đỏ (kiểm thực tế). | CUS | references/industries/logistics.md §4.5 |
| Phí lưu container/lưu bãi | Demurrage / Detention | DEM/DET | DEM/DET; phí lưu cont; phí lưu bãi | Phí phát sinh khi sử dụng container/bãi quá thời hạn miễn phí. | FWD | references/industries/logistics.md §4.1 |
| Phí lưu kho | Storage Charge |  | Phí storage | Phí tính theo m²/pallet/vị trí/CBM × số ngày (hoặc bậc thang), chốt kỳ để lập hóa đơn. | WMS | references/industries/logistics.md §4.4 |
| Phí xếp dỡ tại cảng | Terminal Handling Charge | THC |  | Phí bốc dỡ container tại cảng, một khoản phụ phí phổ biến trên lô hàng. | FWD | references/industries/logistics.md §4.1 |
| Phí xử lý hàng | Handling Charge |  | Phí handling; phí in/out | Phí thao tác nhập/xuất hàng tại kho theo lần. | WMS | references/industries/logistics.md §4.4 |
| Phụ phí | Surcharges | BAF/CAF/EBS/LSS | BAF, CAF, THC, DOC, EBS, LSS | Các khoản phí cộng thêm ngoài cước cơ bản trên lô hàng (phụ phí nhiên liệu, tỷ giá, xếp dỡ, chứng từ...). | FWD | references/industries/logistics.md §4.2 |
| Quản trị chuỗi cung ứng | Supply Chain Management | SCM |  | Điều phối dòng hàng, thông tin và tài chính từ nguyên liệu tới người tiêu dùng; mạnh ở dự báo và tối ưu, bổ sung cho ERP. | FWD | references/industries/logistics.md §1; sách Parthasarathy ch07 |
| Soạn hàng | Picking |  | Nhặt hàng | Lấy hàng theo lệnh xuất, theo chiến lược FEFO/FIFO và mô hình wave/batch/zone. | WMS | references/industries/logistics.md §4.4 |
| Thiết bị giám sát hành trình | Journey Monitoring Device | GSHT |  | Thiết bị GPS bắt buộc trên xe kinh doanh vận tải, truyền dữ liệu hành trình/tốc độ cho cơ quan quản lý. | TMS | references/industries/logistics.md §4.3 |
| Thông báo hàng đến kho | Advance Shipping Notice | ASN |  | Thông báo trước về lô hàng sắp nhập kho để chuẩn bị nhận và đối chiếu. | WMS | references/industries/logistics.md §4.4 |
| Thông quan | Customs Clearance |  | Giải phóng hàng | Trạng thái hàng được phép thông qua sau khi hoàn tất thủ tục và nghĩa vụ thuế XNK. | CUS | references/industries/logistics.md §4.5 |
| Tờ khai hải quan | Customs Declaration |  |  | Chứng từ khai báo hàng xuất/nhập khẩu theo loại hình, truyền qua VNACCS/VCIS. | CUS | references/industries/logistics.md §4.5 |
| Vận đơn chủ | Master Bill of Lading | MBL | MBL | Vận đơn do hãng tàu cấp cho forwarder cho cả lô/container. | FWD | references/industries/logistics.md §4.1 |
| Vận đơn hàng không | Air Waybill | AWB | MAWB (hãng bay) / HAWB (forwarder) | Chứng từ vận chuyển hàng không; MAWB do hãng bay cấp, HAWB do forwarder cấp. | FWD | references/industries/logistics.md §4.1 |
| Vận đơn nhà | House Bill of Lading | HBL | HBL; vận đơn thứ cấp | Vận đơn forwarder cấp cho từng chủ hàng lẻ trong lô ghép (consol). | FWD | references/industries/logistics.md §4.1 |
| Vận tải đa phương thức | Multimodal Transport | MT |  | Vận chuyển bằng ít nhất hai phương thức khác nhau dưới một hợp đồng vận tải đa phương thức. | FWD | references/industries/logistics.md §4.1 |
| Xuất trước – hết hạn trước | First Expired First Out | FEFO | Xuất theo hạn dùng gần nhất; nhập trước–hết hạn trước theo HSD | Chiến lược cấp phát hàng ưu tiên lô có hạn dùng gần nhất; mặc định cho hàng có hạn dùng (kho 3PL, và bắt buộc với FMCG/dược trong phân phối). | WMS/INV | references/industries/logistics.md §4.4 |

### Thương mại – Phân phối (Trading & Distribution)

| Thuật ngữ (VI) | Tiếng Anh | Viết tắt | Tên khác / tên khách hàng hay dùng | Định nghĩa ngắn (1–2 câu, dùng được trong tài liệu dự án) | Module | Xem thêm |
|---|---|---|---|---|---|---|
| Ánh xạ mã SKU | SKU Mapping |  | Mapping SKU | Ánh xạ mã SKU trong hệ thống với mã SKU trên sàn TMĐT để đồng bộ đúng sản phẩm. | ECM | references/industries/trading-distribution.md §4.8 |
| Bán hàng hợp kênh | Omnichannel |  |  | Hợp nhất bán hàng và tồn kho qua nhiều kênh (cửa hàng, website, sàn TMĐT). | ECM | references/industries/trading-distribution.md §4.8 |
| Bán hàng theo tuyến | Route-to-Market / Journey Plan |  | Route-to-market; đi tuyến; bán tuyến | Lịch và lộ trình viếng thăm điểm bán theo tần suất do hệ thống phân cho nhân viên. | DMS | references/industries/trading-distribution.md §4.4 |
| Bán ra | Sell-out |  |  | NPP/điểm bán bán ra thị trường; đo sức khỏe thị trường thật, thu thập qua DMS. | DMS | references/industries/trading-distribution.md §4.4 |
| Bán trên xe | Van sales |  |  | Hàng để sẵn trên xe, bán và giao ngay tại điểm bán; cuối ngày đối soát tồn xe và tiền. | DMS | references/industries/trading-distribution.md §4.4 |
| Bán trước | Pre-sales |  |  | Nhân viên đi tuyến ghi đơn tại điểm bán, hàng được giao sau bằng xe giao hàng. | DMS | references/industries/trading-distribution.md §4.4 |
| Bảng giá | Price List |  |  | Tập giá theo loại giá, kênh/vùng/nhóm khách, có hiệu lực từ–đến và bậc số lượng. | PRICE | references/industries/trading-distribution.md §4.1 |
| Ca bán lẻ | POS Shift |  | Ca thu ngân | Chu kỳ mở–đóng ca bán lẻ, kiểm quỹ đầu–cuối ca và đối soát tiền mặt với doanh thu ca. | POS | references/industries/trading-distribution.md §4.7 |
| Cây đơn vị tính / quy cách đóng gói | Unit-of-Measure hierarchy | UoM | Quy cách đóng gói; lon–lốc–thùng; UoM | Hệ thống quy đổi lon–lốc–thùng với hệ số; nền tảng tính tồn kho, giá và KM theo số lượng. | INV | references/industries/trading-distribution.md §5 |
| Check-in GPS | GPS Check-in |  |  | Xác thực vị trí DSR tại điểm bán trong bán kính cho phép để ghi nhận viếng thăm hợp lệ, chống viếng thăm "ảo". | DMS | references/industries/trading-distribution.md §4.4 |
| Chỉ tiêu doanh số | Sales Target |  | Target | Mục tiêu doanh số theo DSR/tuyến/vùng/NPP để theo dõi mức đạt (target achievement). | SAL | references/industries/trading-distribution.md §7.1 |
| Chiết khấu thanh toán | Payment / Cash Discount |  |  | Thưởng do khách trả tiền sớm; là chi phí tài chính (TK 635), không phải khuyến mại, không điều chỉnh GTGT. | AR | references/industries/trading-distribution.md §4.3 |
| Chiết khấu thương mại | Trade Discount |  |  | Giảm giá do mua nhiều/đạt doanh số; là khoản giảm trừ doanh thu, hạch toán TK 521 (TT133: ghi giảm thẳng 511, không dùng 521). | PRICE | references/industries/trading-distribution.md §4.3 |
| Chương trình trưng bày | Display Program |  | Thưởng trưng bày | Chương trình thưởng trưng bày tại điểm bán theo tiêu chí, có chu kỳ audit. | DMS | references/industries/trading-distribution.md §5 |
| Cộng dồn khuyến mại | Promotion Stacking |  | Chồng KM | Quy tắc áp nhiều KM cùng lúc trên một dòng đơn; mặc định không cộng dồn, chọn ưu đãi tốt nhất cho khách. | PROMO | references/industries/trading-distribution.md §4.2 |
| Cửa hàng tiện lợi | Convenience Store | CVS |  | Loại điểm bán thuộc kênh hiện đại (MT), diện tích nhỏ, mở cửa dài giờ. | SAL | references/industries/trading-distribution.md §1.2 |
| Đại lý | Agent / Dealer |  |  | Bên bán hàng cho nhà cung cấp, có thể bán đúng giá hưởng hoa hồng (mô hình ký gửi). | SAL | references/industries/trading-distribution.md §1 |
| Đăng ký khuyến mại | Promotion Registration |  |  | Thủ tục bắt buộc với KM may rủi; phải được Sở/Bộ Công Thương xác nhận trước khi thực hiện. | PROMO | references/industries/trading-distribution.md §2.1 |
| Đẩy hàng vào | Sell-in |  |  | Bán từ nhà sản xuất/nhãn hàng vào NPP/khách; ghi nhận doanh thu của nhãn hàng. | SAL | references/industries/trading-distribution.md §1 |
| Địa bàn độc quyền | Exclusive Territory |  | Vùng độc quyền NPP | Khu vực mà một NPP được phân phối độc quyền theo thỏa thuận. | SAL | references/industries/trading-distribution.md §5 |
| Điểm bán | Outlet |  | Outlet; cửa hàng; tạp hóa | Cửa hàng/tạp hóa bán cho người tiêu dùng cuối; đối tượng viếng thăm của đội tuyến. | DMS | references/industries/trading-distribution.md §4.4 |
| Điểm bán hoạt động | Active Outlets |  |  | Số điểm bán phát sinh đơn hàng trong kỳ. | DMS | references/industries/trading-distribution.md §7.2 |
| Độ phủ | Distribution Coverage |  |  | Tỷ lệ điểm bán có bán hàng của công ty trên tổng điểm bán mục tiêu. | DMS | references/industries/trading-distribution.md §4.4 |
| Độ phủ theo số lượng / trọng số | Numeric & Weighted Distribution |  |  | Tỷ lệ điểm bán (hoặc trọng số theo doanh thu) có bán SKU trên tổng điểm bán mục tiêu. | DMS | references/industries/trading-distribution.md §7.2 |
| Đổi hàng | Exchange |  |  | Nghiệp vụ gồm một lần trả hàng và một lần bán mới, liên kết chứng từ với nhau. | RET | references/industries/trading-distribution.md §4.6 |
| Đối soát sàn | Marketplace Reconciliation |  | Đối soát sao kê sàn | Đối chiếu doanh thu bán sàn với sao kê: phí sàn, phí vận chuyển, tiền COD, đơn hoàn/hủy. | ECM | references/industries/trading-distribution.md §4.8 |
| Giá niêm yết | Listed Price |  |  | Giá công bố phải tuân thủ nghĩa vụ niêm yết giá (Luật Giá 2023); bán lẻ không được vượt giá niêm yết. | PRICE | references/industries/trading-distribution.md §4.1 |
| Giá sàn | Floor Price |  | Giá tối thiểu | Mức giá bán ra thấp nhất cho phép theo SKU/kênh; thấp hơn phải được cấp trên duyệt. | PRICE | references/industries/trading-distribution.md §4.1 |
| Giá theo bậc số lượng | Tiered (Volume) Pricing |  | Giá bậc thang | Giá giảm dần theo mốc số lượng hoặc giá trị mua. | PRICE | references/industries/trading-distribution.md §4.1 |
| Giảm giá hàng bán | Sales Allowance |  |  | Giảm giá do hàng kém phẩm chất, sai quy cách; là khoản giảm trừ doanh thu (TK 521; TT133: ghi giảm thẳng 511). | SAL | references/industries/trading-distribution.md §4.3 |
| Giám sát bán hàng | Sales Supervisor | GSBH | GSBH; supervisor | Người giám sát đội DSR theo khu vực, theo dõi tuân thủ tuyến và duyệt đơn vượt hạn mức. | DMS | references/industries/trading-distribution.md §4.4 |
| Giao đủ đúng hạn | On-Time In-Full | OTIF | OTIF | Tỷ lệ đơn được giao đủ số lượng và đúng thời hạn trên tổng số đơn. | SAL | references/industries/trading-distribution.md §7 |
| Hạn mức giá trị khuyến mại | Promotion Value Cap |  | Trần 50%/100% | Trần giá trị KM: tối đa 50% giá/đơn vị hàng, lên 100% với chương trình KM tập trung. | PROMO | references/industries/trading-distribution.md §2.1 |
| Hạn mức tín dụng | Credit Limit |  |  | Mức công nợ tối đa cho một khách/NPP; vượt hạn mức thì đơn bị chặn hoặc chờ duyệt. | AR | references/processes/ar-accounts-receivable.md |
| Hàng bán bị trả lại | Sales Return |  | Trả hàng | Hàng khách trả lại; ghi giảm trừ doanh thu trên TK 521 và hoàn giá vốn (TT133: ghi giảm thẳng 511, không dùng 521). | SAL | references/industries/trading-distribution.md §4.6 |
| Hàng gửi bán / ký gửi | Consignment |  | Hàng ký gửi; gửi bán đại lý | Giao hàng cho đại lý nhưng chưa ghi doanh thu đến khi bán được; theo dõi trên TK 157. | INV | references/industries/trading-distribution.md §4.5 |
| Hàng khuyến mại | Promotional Goods |  |  | Hàng tặng/giảm theo chương trình KM; giá tính thuế GTGT bằng 0 khi chương trình được khai báo hợp lệ, nếu không phải kê khai thuế như bán thường (giá vốn vào 641; TT133: 6421). | PRICE | references/industries/trading-distribution.md §4.2 |
| Hàng tiêu dùng nhanh | Fast-Moving Consumer Goods | FMCG | Hàng tiêu dùng nhanh | Nhóm hàng vòng quay nhanh, nhiều SKU, thường có hạn dùng và khuyến mãi dày đặc. | SAL | references/industries/trading-distribution.md §1.1 |
| Hệ thống quản lý phân phối | Distribution Management System | DMS |  | Phần mềm quản lý bán hàng thị trường: tuyến, viếng thăm, tồn NPP, trưng bày, sell-out. | DMS | references/industries/trading-distribution.md §4.4 |
| Hết hàng tại điểm bán | Out-of-Stock | OOS | OOS; cháy hàng | Tình trạng SKU không còn hàng để bán tại điểm bán/NPP; theo dõi để điều phối hàng. | INV | references/industries/trading-distribution.md §7 |
| Hóa đơn khởi tạo từ máy tính tiền | Cash-register e-invoice |  |  | HĐĐT phát hành trực tiếp từ POS, ký hiệu mẫu loại M; khi sai chỉ được lập hóa đơn thay thế. | POS | references/industries/trading-distribution.md §4.7 |
| Hoạch định nhu cầu phân phối | Distribution Requirements Planning | DRP |  | Lập lịch bổ sung tồn kho tại các trung tâm phân phối (DC); bản mở rộng gồm cả cước vận tải, kho bãi và nhân lực. | INV | references/processes/inventory-warehouse.md; sách Wallace ch12 |
| Hồi khấu theo doanh số | Volume Rebate |  | Rebate; chiết khấu theo doanh số; thưởng doanh số | Chiết khấu tính theo mốc doanh số đạt được, thường quyết toán cuối kỳ bằng hóa đơn điều chỉnh. | PRICE | references/industries/trading-distribution.md §4.1 |
| Horeca | Hotel–Restaurant–Catering | Horeca |  | Kênh khách hàng là nhà hàng, khách sạn, quán ăn. | SAL | references/industries/trading-distribution.md §1.2 |
| Kênh hiện đại | Modern Trade | MT |  | Siêu thị, đại siêu thị, cửa hàng tiện lợi; mua tập trung, có phí trưng bày và đối soát sao kê. | SAL | references/industries/trading-distribution.md §1 |
| Kênh truyền thống | General Trade | GT |  | Kênh tạp hóa, chợ, cửa hàng nhỏ; bán qua đội bán hàng đi tuyến. | SAL | references/industries/trading-distribution.md §1 |
| Khách hàng B2B / dự án | B2B / Project Customer | B2B |  | Khách mua buôn theo hợp đồng khung hoặc mua cho công trình/dự án. | SAL | references/industries/trading-distribution.md §1.1 |
| Kho xe | Van Stock |  | Tồn xe | Điểm lưu kho trên xe van sales; điều chuyển từ kho tổng không ghi doanh thu, đối soát tồn xe và tiền cuối ngày. | DMS | references/industries/trading-distribution.md §4.4 |
| Khuyến mại | Sales Promotion | KM | Khuyến mãi; KM | Hoạt động xúc tiến thương mại dành cho khách lợi ích nhất định; chịu khung Luật Thương mại. | PRICE | references/industries/trading-distribution.md §4.1 |
| Khuyến mại may rủi | Chance-based Promotion |  | Quay số, bốc thăm trúng thưởng | KM có yếu tố may rủi; phải đăng ký và xác định trúng thưởng có khách hàng chứng kiến trực tiếp/trực tuyến (NĐ 239/2026). | PROMO | references/industries/trading-distribution.md §2.1 |
| Kiểm tra trưng bày | Display Audit |  | Display audit; audit trưng bày | Việc kiểm tra và chấm điểm trưng bày tại điểm bán, thường kèm chụp ảnh có tọa độ và thời gian. | DMS | references/industries/trading-distribution.md §4.4 |
| Kỳ thu tiền bình quân | Days Sales Outstanding | DSO | DSO | Số ngày trung bình thu được tiền từ bán chịu; chỉ số kiểm soát rủi ro công nợ. | AR | references/processes/ar-accounts-receivable.md |
| Lịch viếng thăm tháng | Monthly Call Plan | MCP | MCP; kế hoạch viếng thăm | Kế hoạch viếng thăm điểm bán theo tần suất trong tháng cho từng DSR. | DMS | references/industries/trading-distribution.md §4.4 |
| Mã hàng / SKU | Stock Keeping Unit | SKU | Mã sản phẩm; mã vạch | Đơn vị hàng hóa nhỏ nhất để quản lý tồn/giá; có barcode, cây đơn vị tính, lô–HSD, serial/IMEI tùy ngành. | INV | references/industries/trading-distribution.md §5 |
| Mua X tặng Y | Buy X Get Y |  | Bán kèm; bundle; tặng hàng | Hình thức KM tặng hàng kèm điều kiện mua; bản chất là giảm giá hàng bán, phân bổ doanh thu cho cả hàng bán và hàng tặng. | PROMO | references/industries/trading-distribution.md §4.2 |
| Nhà phân phối | Distributor | NPP | NPP | Trung gian mua đứt bán đoạn từ nhà sản xuất, phân phối lại cho điểm bán trên một địa bàn. | SAL | references/industries/trading-distribution.md §1 |
| Nhân viên bán hàng tuyến | Field Salesman / Distributor Sales Rep | DSR | DSR; salesman thị trường; nhân viên thị trường | Người đi tuyến viếng thăm điểm bán, kiểm trưng bày và lấy đơn trên mobile. | DMS | references/industries/trading-distribution.md §4.4 |
| Phiếu mua hàng / voucher | Voucher / E-voucher |  | Phiếu quà tặng | Phiếu tặng dùng cho lần mua sau trong chương trình KM. | PROMO | references/industries/trading-distribution.md §4.2 |
| Quản lý lô – hạn dùng | Lot & Expiry Management |  | Quản lý số lô/HSD | Theo dõi số lô và hạn sử dụng của hàng; bắt buộc với FMCG/dược, cảnh báo hàng cận date. | INV | references/industries/trading-distribution.md §6; references/processes/inventory-warehouse.md |
| Quản lý serial / IMEI | Serial / IMEI Tracking |  |  | Theo dõi từng đơn vị hàng theo số serial/IMEI; dùng cho điện tử, gia dụng và quản lý bảo hành. | INV | references/industries/trading-distribution.md §5 |
| ROI khuyến mại | Promotion ROI / Uplift |  | Hiệu quả KM | Doanh số tăng thêm so với baseline chia cho chi phí khuyến mãi. | PROMO | references/industries/trading-distribution.md §7.2 |
| Sàn thương mại điện tử | E-commerce Marketplace | TMĐT | Sàn TMĐT; marketplace | Shopee/Lazada/Tiki/TikTok Shop...; cần đồng bộ sản phẩm–giá–tồn–đơn hai chiều và đối soát phí sàn. | ECM | references/industries/trading-distribution.md §4.8 |
| Số ngày tồn kho bình quân | Days Inventory Outstanding | DIO | Vòng quay tồn kho (ngày) | Số ngày hàng nằm tồn kho bình quân; chỉ số quản trị dòng hàng. | INV | references/industries/trading-distribution.md §7.2 |
| Thanh toán đa phương thức | Multi-tender Payment |  |  | Một hóa đơn thanh toán bằng nhiều hình thức: tiền mặt, thẻ, ví điện tử, QR, voucher, điểm thưởng. | POS | references/industries/trading-distribution.md §4.7 |
| Thông báo khuyến mại | Promotion Notification |  |  | Thủ tục gửi Sở Công Thương trước tối thiểu 3 ngày làm việc cho KM không may rủi (một số hình thức được miễn từ 01/12/2024). | PROMO | references/industries/trading-distribution.md §2.1 |
| Thu hộ khi giao | Cash on Delivery | COD | Tiền thu hộ | Thu tiền của người nhận khi giao kiện hàng, sau đó đối soát với đơn vị vận chuyển/sàn. | ECM | references/industries/trading-distribution.md §4.8 |
| Tích điểm đổi quà | Loyalty Points |  | Khách hàng thân thiết | Chương trình tích điểm theo doanh số để đổi ưu đãi/quà. | PROMO | references/industries/trading-distribution.md §4.2 |
| Tồn kho do nhà cung cấp quản lý | Vendor-Managed Inventory | VMI | Continuous Replenishment | Nhà cung cấp chịu trách nhiệm bổ sung tồn kho hàng của mình tại kho khách hàng/NPP. | INV | references/processes/inventory-warehouse.md; sách Wallace ch12 |
| Trade marketing | Trade Marketing |  | Tiếp thị thương mại | Bộ phận thiết kế giá, khuyến mãi, trưng bày và các chương trình theo kênh. | PRICE | references/industries/trading-distribution.md §4.1 |
| Tuân thủ viếng thăm | Visit Compliance |  |  | Tỷ lệ viếng thăm đúng kế hoạch, đúng tuyến của đội bán hàng tuyến. | DMS | references/industries/trading-distribution.md §7.2 |
| Tỷ lệ bán hết | Sell-through |  |  | Sell-out chia cho (tồn đầu kỳ + sell-in), đo tốc độ tiêu thụ hàng tại NPP/điểm bán. | SAL | references/industries/trading-distribution.md §7.2 |
| Tỷ lệ chốt đơn | Strike Rate |  |  | Số đơn thành công trên tổng số viếng thăm của nhân viên bán hàng tuyến. | DMS | references/industries/trading-distribution.md §7.2 |
| Vật phẩm trưng bày | Point of Sale Materials | POSM | POSM; vật phẩm quảng cáo tại điểm bán | Kệ, standee, poster… hỗ trợ bán và trưng bày tại điểm bán; gắn với chương trình trưng bày. | DMS | references/industries/trading-distribution.md §4.4 |
| Yêu cầu trả hàng | Return Merchandise Authorization | RMA | Phiếu trả hàng | Chứng từ đề nghị và duyệt trả hàng, liên kết với hóa đơn điều chỉnh/trả lại. | RET | references/industries/trading-distribution.md §4.6 |

## Chuỗi cung ứng – mua bán – kho – sản xuất – dự án – CRM – nhân sự

| Thuật ngữ (VI) | Tiếng Anh | Viết tắt | Định nghĩa ngắn | Module |
|---|---|---|---|---|
| Biên bản nghiệm thu dịch vụ | Service Entry Sheet | SES | Chứng từ xác nhận dịch vụ đã thực hiện theo PO dịch vụ, bắt buộc có trước khi ghi nhận hóa đơn/công nợ dịch vụ. | PUR |
| Biểu mẫu khấu trừ theo mức 10% | Flat 10% Withholding |  | Khấu trừ 10% trước khi trả cho cá nhân cư trú không ký HĐ hoặc HĐ dưới 3 tháng, mỗi lần ≥ 2 triệu (TT 111/2013). | PAY |
| Biểu thuế lũy tiến từng phần | Progressive Tax Table |  | Bảng bậc thuế TNCN; biểu cũ 7 bậc (5–35%), biểu mới 5 bậc (5/10/20/30/35%) áp dụng từ kỳ 2026. | PAY |
| Báo cáo công đoạn | Operation Confirmation |  | Ghi nhận giờ công/giờ máy và số lượng tốt/hỏng tại từng công đoạn để cập nhật tiến độ và chi phí. | MFG |
| Báo giá | Quotation | QT | Chứng từ chào giá và điều kiện bán cho khách, chưa phát sinh nghĩa vụ giao hàng. | SAL |
| Báo giá nhà cung cấp | Vendor Quotation |  | Giá và điều kiện do từng nhà cung cấp chào lại theo RFQ, là cơ sở lập bảng so sánh và lựa chọn. | PUR |
| Báo tăng/giảm lao động | SI Increase/Decrease Declaration |  | Hồ sơ điều chỉnh lao động & mức đóng gửi cơ quan BHXH khi có biến động (vào/ra, tăng lương, nghỉ không lương, thai sản). | PAY |
| Bảng chấm công | Timesheet |  | Chứng từ ghi giờ công theo công việc/WBS; cơ sở tính chi phí nhân công và xuất hóa đơn T&M. | PRJ |
| Bảng lương | Payroll Run / Payroll Register |  | Chứng từ chính tính gross→net toàn kỳ; vòng đời DRAFT→PENDING→APPROVED→POSTED→CLOSED, có REVERSED/RETURNED. | PAY |
| Bảng thanh toán tiền lương | Payroll Sheet |  | Bảng tổng hợp lương, các khoản trích và khấu trừ, số thực nhận của kỳ lương. | PAY |
| Bảo hiểm thất nghiệp | Unemployment Insurance | BHTN | NLĐ 1% + NSDLĐ 1% theo Luật Việc làm 2025; trần đóng 20× lương tối thiểu vùng. | PAY |
| Bảo hiểm xã hội | Social Insurance | BHXH | Gồm quỹ hưu trí–tử tuất, ốm đau–thai sản, TNLĐ–BNN; NLĐ đóng 8%, NSDLĐ đóng 17,5%. | PAY |
| Bảo hiểm y tế | Health Insurance | BHYT | NLĐ 1,5% + NSDLĐ 3%; trần đóng 20× mức tham chiếu. | PAY |
| Bảo trì phòng ngừa | Preventive Maintenance | PM | Dịch vụ định kỳ theo hợp đồng; hệ thống tự sinh work order theo lịch để ngăn hỏng hóc. | SVC |
| Ca làm việc | Shift / Work Schedule |  | Lịch giờ vào-ra, nghỉ giữa ca, ca ngày/đêm (22:00-06:00); xác định ngày công chuẩn và phụ trội đêm. | HR |
| Cam kết mức dịch vụ | Service Level Agreement | SLA | Cam kết thời gian phản hồi/xử lý theo mức ưu tiên và lịch làm việc; vi phạm (breach) kích hoạt leo thang. | SVC |
| Chi phí chung / phụ phí | Overhead / Burden |  | Chi phí gián tiếp cộng vào cost rate để tính giá vốn đầy đủ cho dự án. | PRJ |
| Chi phí còn phải chi | Estimate to Complete | ETC | Chi phí dự kiến còn lại để hoàn thành dự án tại thời điểm đánh giá. | PRJ |
| Chi phí cộng phí | Cost-plus |  | Mô hình doanh thu = chi phí thực tế được chấp nhận nhân (1 + tỷ lệ phí quản lý). | PRJ |
| Chi phí mua hàng | Landed Cost |  | Cước vận chuyển, bảo hiểm, thuế nhập khẩu và chi phí liên quan được phân bổ vào giá gốc hàng tồn để phản ánh đúng giá vốn. | PUR |
| Chiến dịch marketing | Marketing Campaign |  | Hoạt động tiếp thị có ngân sách, kênh, tập đối tượng; gắn lead/cơ hội để đo ROI; đối tượng phải hợp lệ về đồng ý. | CRM |
| Chiến lược duyệt | Release Strategy |  | Thuật ngữ SAP cho cơ chế định tuyến duyệt chứng từ mua hàng theo đặc trưng (loại CT, tổ chức mua, tổng giá trị) với release group và release code. | PUR |
| Chiến lược phê duyệt mua | Release strategy |  | Cơ chế SAP MM phê duyệt PR/PO qua release code/group theo đặc tính phân loại. | PUR |
| Chuyển dữ liệu xuyên biên giới | Cross-border Data Transfer |  | Chuyển DLCN ra nước ngoài (ví dụ CRM cloud đặt ngoài VN); phải lập hồ sơ theo Điều 20 Luật 91/2025/QH15. | CRM |
| Chuyển kho hai bước | Two-step Stock Transfer |  | Điều chuyển hàng giữa hai kho qua trạng thái trung gian tồn đang chuyển, tách thao tác xuất ở kho đi và nhập ở kho đến. | INV |
| Chênh lệch giá mua | Purchase Price Variance | PPV | Chênh lệch giữa giá PO và giá hóa đơn/giá chuẩn, theo dõi để phân tích hiệu quả mua và cập nhật giá vốn. | PUR |
| Chính sách bảo hành | Warranty Policy |  | Quy định thời hạn, phạm vi (linh kiện/công), loại trừ theo nhóm sản phẩm; quyết định miễn phí hay tính phí. | SVC |
| Chạy hoạch định nhu cầu vật tư | MRP Run | MRP | Job tính nhu cầu vật tư/đề xuất mua–sản xuất; cần log, chạy lại và khóa chống chạy trùng. | MFG |
| Chấm công | Timekeeping |  | Ghi nhận ngày công, giờ làm thêm, nghỉ phép làm dữ liệu đầu vào tính lương. | HR |
| Chỉ số hài lòng khách hàng | Customer Satisfaction Score | CSAT | Điểm hài lòng thu qua khảo sát sau khi đóng ticket/work order. | SVC |
| Chỉ số thiện cảm ròng | Net Promoter Score | NPS | Chỉ số đo mức độ khách sẵn sàng giới thiệu; thu qua khảo sát phản hồi. | SVC |
| Chứng từ khấu trừ thuế TNCN | PIT Withholding Certificate |  | Chứng từ điện tử xác nhận số thuế đã khấu trừ, phát hành cho NLĐ và gửi cơ quan thuế trong ngày lập. | PAY |
| Chứng từ khấu trừ thuế TNCN điện tử | E-withholding Certificate |  | Chứng từ điện tử bắt buộc cấp cho người bị khấu trừ và gửi cơ quan thuế trong ngày lập (NĐ 254/2026). | PAY |
| Cán bộ/bộ phận bảo vệ dữ liệu cá nhân | Data Protection Officer | DPO | Người/bộ phận chịu trách nhiệm quản lý tuân thủ bảo vệ DLCN (đồng ý, DPIA, yêu cầu của chủ thể). | CRM |
| Công việc / Nhiệm vụ | Task / Network Activity |  | Đơn vị việc có thời lượng, người thực hiện và nỗ lực kế hoạch; cơ sở lập lịch và đo % hoàn thành theo nỗ lực. | PRJ |
| Cơ cấu tổ chức | Organization / Org Unit |  | Cây đơn vị phân cấp (công ty/chi nhánh/phòng/tổ); mỗi đơn vị gán một vùng lương tối thiểu và trung tâm chi phí mặc định. | HR |
| Cơ hội bán hàng | Opportunity |  | Giao dịch tiềm năng đang được theo dõi qua các giai đoạn phễu, gắn giá trị, % xác suất và ngày đóng dự kiến. | CRM |
| Cấu trúc phân rã công việc | Work Breakdown Structure | WBS | Phân rã dự án thành các phần tử công việc phân cấp để lập kế hoạch, tập hợp chi phí và kiểm soát ngân sách. | PRJ |
| Danh mục vật tư hàng hóa | Item (Material) Master |  | Hồ sơ gốc khai báo thuộc tính từng mặt hàng: ĐVT cơ sở, nhóm, loại, phương pháp quản lý (lô/serial), phương pháp tính giá, min/max. | INV |
| Doanh thu chờ phân bổ | Deferred Revenue |  | Khoản đã xuất hóa đơn hoặc thu trước nhưng chưa đủ điều kiện ghi doanh thu; TK 3387 theo TT99 (TT200 gọi Doanh thu chưa thực hiện). | PRJ |
| Doanh thu thuần | Net revenue |  | Doanh thu bán hàng sau khi trừ các khoản giảm trừ doanh thu. | SAL |
| Dịch vụ hiện trường | Field Service | FSM | Dịch vụ thực hiện tại địa điểm khách; gồm xếp lịch, điều phối kỹ thuật viên và chuyến thăm hiện trường. | SVC |
| Dữ liệu cá nhân | Personal Data | DLCN | Thông tin gắn với cá nhân xác định/có thể xác định (tên, điện thoại, email...); được bảo vệ theo Luật 91/2025/QH15. | CRM |
| Dự báo nhu cầu | Demand Forecast |  | Ước lượng nhu cầu tương lai làm đầu vào cho S&OP/MPS; được đơn hàng thực tế 'tiêu thụ' để tránh đếm trùng. | MFG |
| Dự phòng bảo hành | Warranty Provision |  | Khoản trích trước chi phí bảo hành ước tính cho hàng đã bán còn bảo hành; hạch toán TK 352 (3521). | SVC |
| Ghi nhận doanh thu | Revenue Recognition |  | Quá trình ghi doanh thu và giá vốn tương ứng theo phương pháp đã chọn (POC/mốc/as-billed). | PRJ |
| Gia công ngoài | Subcontracting |  | Xuất nguyên vật liệu cho nhà cung cấp gia công và nhận lại bán thành phẩm/thành phẩm; kết hợp với module sản xuất. | PUR |
| Gia công thuê ngoài | Subcontracting |  | Thuê đơn vị ngoài gia công một công đoạn/sản phẩm; NVL gửi đi vẫn thuộc sở hữu doanh nghiệp. | MFG |
| Giai đoạn phễu | Pipeline Stage |  | Bước trong phễu (Tiếp cận, Đánh giá, Báo giá, Thương lượng...), mỗi giai đoạn gắn % xác suất thắng để dự báo; tùy biến theo doanh nghiệp. | CRM |
| Giao hàng một phần | Partial delivery |  | Giao hàng nhiều lần cho một đơn; đơn ở trạng thái Hoàn thành một phần cho tới khi giao đủ. | SAL |
| Giao nhận một phần | Partial Delivery |  | Nhà cung cấp giao làm nhiều đợt; mỗi đợt tạo một GR, PO ở trạng thái Hoàn thành một phần cho tới khi nhận đủ. | PUR |
| Giá cố định theo mốc | Fixed Price by Milestone |  | Mô hình billing trong đó giá trị hợp đồng được chia theo các mốc, xuất hóa đơn khi mốc được nghiệm thu. | PRJ |
| Giá trị vòng đời khách hàng | Customer Lifetime Value | CLV | Tổng giá trị kỳ vọng một khách mang lại trong toàn bộ quan hệ; dùng ưu tiên chăm sóc và phân khúc. | CRM |
| Giá vốn nội bộ | Cost Rate |  | Chi phí nội bộ cho một đơn vị nguồn lực (giờ/ngày công), có thể cộng overhead. | PRJ |
| Giảm trừ doanh thu | Sales deductions |  | Các khoản làm giảm doanh thu: chiết khấu thương mại, hàng bán bị trả lại, giảm giá hàng bán (TK 521). | SAL |
| Giảm trừ gia cảnh | Family Deduction | GTGC | Khoản trừ trước khi tính thuế: bản thân 15,5tr/tháng, mỗi người phụ thuộc 6,2tr/tháng từ kỳ 2026 (NQ 110/2025). | PAY |
| Giữ hàng | Stock reservation |  | Giữ chỗ số lượng tồn cho một đơn đã xác nhận, làm giảm ATP của đơn khác. | INV |
| Giữ hàng / Đặt trước tồn | Stock Reservation |  | Khóa số lượng cho đơn bán hoặc lệnh sản xuất, làm giảm tồn khả dụng nhưng chưa xuất kho thực tế. | INV |
| Hao hụt | Scrap |  | Tỷ lệ phần trăm vật tư/sản phẩm mất mát trong sản xuất, cộng vào nhu cầu linh kiện hoặc số lượng phát lệnh. | MFG |
| Hiệu suất sử dụng nguồn lực | Utilization |  | Tỷ lệ giờ có thể tính phí (billable) trên tổng giờ công của nguồn lực. | PRJ |
| Hiệu suất thiết bị tổng thể | Overall Equipment Effectiveness | OEE | Chỉ số = Khả dụng (Availability) × Hiệu suất (Performance) × Chất lượng (Quality); chuẩn world-class ≈ 85% cho sản xuất rời rạc. | MFG |
| Hoa hồng bán hàng | Sales commission |  | Khoản thưởng theo doanh số/tiền thu được của nhân viên hoặc đại lý bán hàng. | SAL |
| Hoạch định bán hàng và vận hành | Sales & Operations Planning | S&OP | Quy trình cân đối cung–cầu tổng thể theo nhóm sản phẩm ở cấp quản trị, định hướng cho MPS. | MFG |
| Hoạch định nguồn lực sản xuất | Manufacturing Resource Planning | MRP II | Mở rộng của MRP theo vòng kín (closed-loop), bổ sung phản hồi từ xưởng, hoạch định năng lực và kế toán chi phí. | MFG |
| Hoạch định nhu cầu năng lực | Capacity Requirements Planning | CRP | Kiểm tra chi tiết tải (load) so với công suất sẵn có của từng trung tâm làm việc sau khi chạy MRP. | MFG |
| Hoạch định nhu cầu vật tư | Material Requirements Planning | MRP | Phương pháp biến nhu cầu độc lập (đơn hàng, dự báo) thành nhu cầu phụ thuộc (linh kiện, bán thành phẩm) và đề xuất lệnh mua/lệnh sản xuất đúng số lượng, đúng thời điểm. | MFG |
| Hoạch định năng lực sơ bộ | Rough-Cut Capacity Planning | RCCP | Kiểm tra sơ bộ năng lực ở mức MPS để phát hiện quá tải trước khi chạy MRP. | MFG |
| Hoạt động | Activity |  | Tương tác với khách: cuộc gọi, cuộc họp, công việc; dùng để theo dõi chăm sóc và đo năng suất nhân viên. | CRM |
| Hàng gửi đi bán | Goods on consignment |  | Hàng xuất gửi đại lý/ký gửi, theo dõi TK 157, chưa ghi doanh thu cho tới khi bán được. | SAL |
| Hàng ký gửi | Consignment |  | Hàng nhà cung cấp để tại kho doanh nghiệp nhưng quyền sở hữu chưa chuyển; doanh nghiệp chỉ ghi mua khi rút ra sử dụng/bán. | PUR |
| Hàng mua đang đi đường | Goods in Transit |  | Hàng đã có hóa đơn và ghi nhận công nợ nhưng chưa về nhập kho; theo dõi trên TK 151, khi về kho kết chuyển sang 152/156. | PUR |
| Hàng rào thời gian | Time Fence |  | Khoảng thời gian gần hiện tại mà MRP không tự ý dời/sinh lệnh, nhằm ổn định kế hoạch. | MFG |
| Hàng tồn kho | Inventory | HTK | Nguyên vật liệu, công cụ, sản phẩm dở dang, thành phẩm, hàng hóa; đo lường theo VAS 02. | INV |
| Hóa đơn dịch vụ | Service Invoice |  | Hóa đơn cho phần dịch vụ có phí (công + phụ tùng); phát hành hóa đơn điện tử, ghi công nợ 131, thuế 3331. | SVC |
| Hóa đơn nhà cung cấp | Vendor Invoice |  | Chứng từ ghi nhận công nợ phải trả; chỉ ghi sổ khi khớp 2/3 chiều với PO và GR trong dung sai. | PUR |
| Hóa đơn điều chỉnh giảm | Credit note |  | Chứng từ điều chỉnh giảm doanh thu và thuế GTGT, dùng cho trả hàng hoặc chiết khấu sau hóa đơn. | SAL |
| Hạn dùng | Expiry (Shelf Life) |  | Ngày hết hạn sử dụng gắn với lô; cơ sở cho cảnh báo cận hạn và chiến lược xuất FEFO. | INV |
| Hạn mức chữ ký | Signing limit |  | Cơ chế Dynamics 365 giới hạn giá trị một người được duyệt, gắn với workflow. | PUR |
| Hồ sơ nhân viên | Employee Master |  | Dữ liệu nhân sự nền: mã NV, CCCD, mã số thuế, mã BHXH, vị trí, ngày vào/ra, tài khoản ngân hàng, tình trạng; là nguồn cho tính lương. | HR |
| Hợp đồng bán | Sales contract / agreement |  | Cam kết khung về giá, sản lượng, kỳ hạn; là căn cứ tạo nhiều đơn bán. | SAL |
| Hợp đồng dịch vụ / quyền lợi | Service Contract / Entitlement |  | Thỏa thuận xác định phạm vi dịch vụ, SLA, giá/ưu đãi áp cho work order của khách. | SVC |
| Hợp đồng lao động | Labor Contract | HĐLĐ | Thỏa thuận giữa NLĐ và NSDLĐ; chỉ còn 2 loại: không xác định thời hạn và xác định thời hạn tối đa 36 tháng (Đ.20 BLLĐ). | HR |
| Hợp đồng lỗ | Onerous Contract |  | Hợp đồng có chi phí ước tính (EAC) vượt giá trị hợp đồng; phải trích ngay toàn bộ phần lỗ dự kiến vào dự phòng 352. | PRJ |
| Khuyến mãi hàng tặng | Free goods |  | Hàng tặng kèm khi mua; vẫn phải xuất kho ghi giá vốn và xử lý thuế theo quy định. | SAL |
| Khách hàng góc nhìn bán hàng | Customer master (sales view) |  | Dữ liệu bán hàng của khách: điều khoản thanh toán, hạn mức tín dụng, bảng giá, địa chỉ giao/xuất hóa đơn, nhân viên phụ trách. | SAL |
| Khách hàng tiềm năng | Lead |  | Đầu mối quan tâm chưa đủ điều kiện mua; thu từ web, hội chợ, giới thiệu, chiến dịch; khi đủ điều kiện chuyển thành cơ hội. | CRM |
| Khóa sổ kỳ kho | Inventory Period Close |  | Chốt kỳ sau khi tính giá vốn và đối chiếu sổ kho ↔ sổ cái, chặn ghi sổ/sửa chứng từ kỳ đã đóng. | INV |
| Kinh phí công đoàn | Trade Union Fee | KPCĐ | NSDLĐ đóng 2% quỹ tiền lương đóng BHXH, bắt buộc kể cả chưa có công đoàn (Luật Công đoàn 2024). | PAY |
| Kiểm kê | Physical Inventory Count |  | Đếm thực tế hàng trong kho theo kỳ để đối chiếu với tồn sổ sách và xử lý chênh lệch. | INV |
| Kiểm kê quay vòng | Cycle Counting |  | Kiểm kê một phần tồn kho theo chu kỳ để duy trì độ chính xác tồn kho mà không phải dừng kho. | MFG |
| Kiểm kê định kỳ theo vòng | Cycle Count |  | Phương pháp kiểm kê luân phiên từng nhóm hàng theo chu kỳ thay vì đếm toàn bộ một lần. | INV |
| Kiểm soát khả dụng ngân sách | Budget Availability Control | AVAC | Cơ chế cảnh báo hoặc chặn khi cam kết (PO mở) cộng thực chi vượt ngân sách theo dung sai cấu hình. | PRJ |
| Kiểm tra chất lượng | Quality Inspection | QC | Bước kiểm tra lô hàng nhận; hàng cấu hình kiểm QC vào kho chờ kiểm, chỉ chuyển kho tốt sau khi QC chấp nhận. | PUR |
| Kiểm tra chất lượng trong chuyền | In-Process Quality Control | IPQC | Kiểm tra chất lượng tại các công đoạn trong quá trình sản xuất để chặn lỗi sớm. | MFG |
| Kiểm tra chất lượng đầu ra | Outgoing Quality Control | OQC | Kiểm tra thành phẩm trước khi nhập kho/giao hàng; quyết định đạt/không đạt. | MFG |
| Kiểm tra chất lượng đầu vào | Incoming Quality Control | IQC | Kiểm tra chất lượng NVL/linh kiện khi nhận từ nhà cung cấp trước khi nhập kho/đưa vào sản xuất. | MFG |
| Kiểm tra tín dụng | Credit check |  | Đối chiếu mức tín dụng đang dùng với hạn mức; nếu vượt thì cảnh báo hoặc chặn đơn. | SAL |
| Kênh phân phối | Distribution channel |  | Kênh bán hàng tới khách (bán lẻ, bán buôn, đại lý, online) dùng để phân tích và áp giá. | SAL |
| Kế hoạch xuất hóa đơn | Billing Plan |  | Lịch và cơ sở lập hóa đơn của dự án (theo mốc, theo kỳ, hoặc theo giờ công). | PRJ |
| Kết chuyển / quyết toán dự án | Settlement |  | Kết chuyển chi phí/doanh thu dự án để chốt lãi lỗ hoặc chuyển sang TSCĐ (dự án nội bộ). | PRJ |
| Linh kiện ảo | Phantom BOM |  | Cụm lắp ráp không nhập kho riêng; MRP xuyên qua (explode through) để lấy nhu cầu linh kiện con. | MFG |
| Làm thêm giờ | Overtime | OT | Giờ làm vượt giờ chuẩn; trần 40h/tháng, 200h/năm (300h ngành đặc thù); trả ≥150/200/300%. | PAY |
| Làm việc ban đêm | Night Shift |  | Thời gian 22:00–06:00; được trả thêm ít nhất 30%; làm thêm đêm cộng thêm 20% (Đ.98, 106 BLLĐ). | PAY |
| Lãi gộp | Gross margin |  | Doanh thu thuần trừ giá vốn hàng bán; chỉ tiêu đánh giá hiệu quả bán hàng. | SAL |
| Lãi lỗ dự án | Project P&L |  | Báo cáo doanh thu - giá vốn - chi phí - lợi nhuận theo từng dự án. | PRJ |
| Lô | Batch (Lot) |  | Nhóm hàng cùng đặc tính nhập/sản xuất, quản lý chung ngày sản xuất và hạn dùng để truy xuất. | INV |
| Lương cơ sở | Statutory Base Salary |  | Mức do Chính phủ quy định (2,34tr từ 01/7/2024; 2,53tr từ 01/7/2026) dùng làm căn cứ trần đóng BHXH/BHYT. | PAY |
| Lương gộp | Gross Salary |  | Tổng thu nhập trước khấu trừ = lương theo công + phụ cấp + bổ sung + OT + thưởng + khác. | PAY |
| Lương thực nhận | Net Salary |  | Lương nhận về = Gross − bảo hiểm phần NLĐ (≈10,5%) − đoàn phí − thuế TNCN − tạm ứng − khấu trừ khác. | PAY |
| Lương tối thiểu vùng | Regional Minimum Wage | LTTV | Mức lương sàn theo 4 vùng (NĐ 293/2025: 5,31/4,73/4,14/3,70 triệu/tháng từ 01/01/2026); cũng là căn cứ sàn/trần đóng BHTN. | PAY |
| Lưới–ròng | Gross-to-Net |  | Phép tính MRP trừ tồn dự kiến và lượng về theo lịch khỏi nhu cầu gộp (cộng tồn an toàn) để ra nhu cầu ròng. | MFG |
| Lệnh chuyển kho | Stock Transport Order | STO | Chứng từ khởi tạo điều chuyển nội bộ giữa hai kho/chi nhánh, làm căn cứ lập phiếu xuất và phiếu nhập điều chuyển. | INV |
| Lệnh công việc | Work Order | WO | Chứng từ chỉ thị và theo dõi thực hiện dịch vụ; tập hợp giờ công, phụ tùng và là đối tượng tính giá vốn dịch vụ. | SVC |
| Lệnh kế hoạch | Planned Order |  | Đề xuất (chưa chính thức) của MRP để mua hoặc sản xuất, sẽ chuyển thành PR hoặc lệnh sản xuất. | MFG |
| Lệnh sản xuất | Production Order (Manufacturing Order) | MO | Chứng từ cho phép và theo dõi sản xuất một lô; là đối tượng tập hợp chi phí và tiến độ. | MFG |
| Lịch sản xuất chính | Master Production Schedule | MPS | Kế hoạch sản xuất thành phẩm theo kỳ, chốt từ S&OP/dự báo/đơn hàng, là đầu vào chính của MRP. | MFG |
| Mẫu dự án | Project Template |  | Khung WBS/công việc/mốc/cost plan dựng sẵn, áp khi tạo dự án mới để chuẩn hóa. | PRJ |
| Mốc dự án | Milestone |  | Điểm nghiệm thu quan trọng, thường gắn với quyền xuất hóa đơn hoặc ghi nhận doanh thu theo % giá trị hợp đồng. | PRJ |
| Mức tham chiếu | Reference Level |  | Khái niệm của Luật BHXH 2024 thay dần lương cơ sở; khi chưa bãi bỏ lương cơ sở thì mức tham chiếu = lương cơ sở. | PAY |
| Mức tham chiếu / Lương cơ sở | Reference Level / Statutory Base Salary |  | Mức dùng làm trần đóng BHXH/BHYT (20× mức tham chiếu); khi chưa bãi bỏ lương cơ sở thì mức tham chiếu = lương cơ sở. | PAY |
| Mức tín dụng đang dùng | Credit exposure |  | Dư nợ phải thu + đơn đã duyệt chưa giao + đã giao chưa lập hóa đơn. | SAL |
| Nghiệm thu dịch vụ | Service Confirmation |  | Biên bản xác nhận hoàn thành dịch vụ có khách ký; căn cứ ghi nhận doanh thu và lập hóa đơn. | SVC |
| Nghỉ hằng năm | Annual Leave |  | 12/14/16 ngày phép hưởng lương tùy điều kiện công việc, cộng 1 ngày cho mỗi 5 năm thâm niên (Đ.113–114 BLLĐ). | HR |
| Nghỉ lễ, tết | Public Holidays |  | 11 ngày/năm hưởng nguyên lương theo Điều 112 BLLĐ. | HR |
| Nghỉ phép | Leave / Absence |  | Nghỉ có/không hưởng lương (phép năm, ốm, thai sản, việc riêng); phép năm trừ quỹ phép, ốm/thai sản do quỹ BHXH chi. | HR |
| Ngân sách dự án | Project Budget |  | Trần chi phí được duyệt theo WBS/kỳ, dùng để kiểm soát cam kết và thực chi. | PRJ |
| Người liên hệ | Contact |  | Cá nhân thuộc khách hàng/tổ chức; email và điện thoại là dữ liệu cá nhân, cần bản ghi đồng ý trước khi gửi marketing. | CRM |
| Người phụ thuộc | Dependant |  | Người được NLĐ nuôi dưỡng, đăng ký để giảm trừ; mỗi người chỉ tính cho một người nộp thuế. | PAY |
| Nhóm định khoản kho | Valuation Class / Account Determination |  | Ánh xạ nhóm hàng/kho tới bộ tài khoản tồn kho, giá vốn, thừa/thiếu để hệ thống tự động định khoản. | INV |
| Nhập kho | Goods Receipt | GR | Nghiệp vụ ghi nhận hàng vào kho (mua, sản xuất nhập, trả lại, thừa), làm tăng tồn số lượng và giá trị. | INV |
| Nhập kho thành phẩm | Production Receipt (Goods Receipt from Order) | GR | Nhập sản phẩm hoàn thành vào kho; ghi tăng TK 155 đối ứng TK 154. | MFG |
| Nhập trước xuất trước | First-In First-Out | FIFO | Phương pháp tính giá xuất kho theo thứ tự nhập; LIFO không còn được áp dụng theo VAS 02. | INV |
| Nợ phải trả hợp đồng | Contract Liability |  | Phần đã xuất hóa đơn hoặc thu vượt doanh thu đã ghi nhận; theo dõi ở 3387 hoặc 131 dư Có. | PRJ |
| Phiên bản đơn mua hàng | PO Version / Change |  | Bản sửa đổi PO sau khi đã duyệt; tạo phiên bản mới giữ lịch sử, thay đổi vượt ngưỡng phải phê duyệt lại. | PUR |
| Phiếu lương | Payslip |  | Bảng kê chi tiết trả lương cho từng NLĐ mỗi kỳ (bắt buộc theo Đ.95 BLLĐ). | PAY |
| Phiếu xuất kho kiêm vận chuyển nội bộ | Internal Transfer & Delivery Note |  | Chứng từ vận chuyển hàng điều chuyển nội bộ/đi gia công/giao đại lý theo NĐ123/2020 sửa đổi bởi NĐ70/2025. | INV |
| Phiếu xử lý hàng không đạt | Non-Conformance Report | NCR | Chứng từ ghi nhận và xử lý hàng lỗi theo nhánh: trả lại, sửa (rework), loại bỏ, hoặc nới lỏng (concession). | MFG |
| Phiếu yêu cầu/hỗ trợ | Service Ticket / Case |  | Chứng từ tiếp nhận sự cố, yêu cầu hoặc khiếu nại của khách; khởi đồng hồ SLA khi tạo. | SVC |
| Phân bổ chi phí chung | Overhead allocation |  | Tỷ lệ/cách phân bổ chi phí sản xuất chung (627) vào giá thành hoặc dự án. | MFG |
| Phân bổ nguồn lực | Resource Assignment |  | Gán nhân sự/vai trò vào công việc dự án, kiểm soát theo công suất và dung sai quá tải. | PRJ |
| Phân khúc khách hàng | Customer Segmentation |  | Chia khách theo tiêu chí (ngành, giá trị, hành vi) để nhắm chiến dịch và chính sách chăm sóc phù hợp. | CRM |
| Phân tách trách nhiệm | Segregation of Duties | SoD | Nguyên tắc tách người mua, người nhận hàng và người ghi sổ/thanh toán để không ai kiểm soát toàn bộ chu trình chi. | PUR |
| Phân tích thắng thua | Win/Loss Analysis |  | Phân tích lý do thắng/thua của cơ hội; cơ hội 'Thua' bắt buộc ghi lý do để cải tiến. | CRM |
| Phương pháp chi phí trên chi phí | Cost-to-cost method |  | Cách tính POC = chi phí thực tế lũy kế / tổng chi phí ước tính khi hoàn thành (EAC). | PRJ |
| Phương pháp phần trăm hoàn thành | Percentage-of-completion | POC | Ghi nhận doanh thu dự án theo tiến độ (đo bằng chi phí/khối lượng/mốc) — VAS 15. | PRJ |
| Phương pháp tính giá xuất kho | Inventory costing method |  | Cách xác định giá vốn hàng xuất: Đích danh/Bình quân gia quyền/Nhập trước xuất trước; không hỗ trợ LIFO (VAS 02). | INV |
| Phải trả người lao động | Payables to Employees | TK 334 | Tài khoản ghi nhận nghĩa vụ trả lương, thưởng, trợ cấp cho NLĐ theo TT 99/2025. | PAY |
| Phần tử WBS | WBS Element |  | Một nút trong cây WBS; là đối tượng gán ngân sách, chi phí, doanh thu và cho phép/không cho phép hạch toán. | PRJ |
| Phễu bán hàng | Sales Pipeline |  | Tập hợp các cơ hội sắp xếp theo giai đoạn; cơ sở để dự báo doanh số và quản lý hiệu quả bán. | CRM |
| Phụ tùng | Spare Part |  | Vật tư thay thế dùng trong dịch vụ; quản tồn kho, xuất theo work order, tính vào giá vốn hoặc bán cho khách. | SVC |
| Quyết toán thuế TNCN | PIT Finalization |  | Kê khai tổng hợp cuối năm; DN nộp 05/QTT-TNCN hạn tháng 3, cá nhân tự quyết toán hạn tháng 4. | PAY |
| Quỹ phép | Leave Balance |  | Số ngày phép năm còn lại: 12/14/16 ngày theo loại công việc + 1 ngày mỗi 5 năm thâm niên; tính tỷ lệ cho người vào/ra giữa năm. | HR |
| Sold-to / Ship-to / Bill-to | Sold-to / Ship-to / Bill-to party |  | Ba vai trò địa chỉ của khách: bên đặt hàng, bên nhận hàng, bên nhận hóa đơn. | SAL |
| Sản xuất theo đơn | Make-to-Order | MTO | Chiến lược chỉ sản xuất khi có đơn hàng thực tế; giảm tồn kho thành phẩm. | MFG |
| Sản xuất để tồn kho | Make-to-Stock | MTS | Chiến lược sản xuất theo dự báo và giữ tồn kho thành phẩm để đáp ứng nhanh. | MFG |
| Số serial | Serial Number |  | Định danh duy nhất cho từng đơn vị hàng, phục vụ truy xuất nguồn gốc và bảo hành. | INV |
| Sự đồng ý | Consent |  | Sự chấp thuận của chủ thể dữ liệu cho một mục đích xử lý cụ thể; bắt buộc trước khi marketing, có thể rút lại. | CRM |
| Tai nạn lao động – bệnh nghề nghiệp | Occupational Accident and Disease Insurance | TNLĐ-BNN | Quỹ do NSDLĐ đóng 0,5% (có thể 0,3% nếu đủ điều kiện theo NĐ 58/2020). | PAY |
| Theo thời gian và vật tư | Time and Materials | T&M | Mô hình tính phí theo giờ công thực tế đã duyệt nhân đơn giá bán cộng chi phí vật tư/pass-through. | PRJ |
| Thiết bị đã lắp đặt | Installed Base / Equipment |  | Danh mục thiết bị khách đang dùng theo số serial; lưu lịch sử dịch vụ, bảo hành, triệu hồi. | SVC |
| Thu nhập chịu thuế | Taxable Income |  | Tổng thu nhập có cờ chịu thuế trừ các khoản miễn thuế trong định mức (ăn ca, phụ trội OT/đêm, trang phục...). | PAY |
| Thu nhập tính thuế | Taxable Income |  | Thu nhập chịu thuế trừ bảo hiểm bắt buộc, giảm trừ gia cảnh và các khoản được trừ khác. | PAY |
| Thành phần lương | Pay Element |  | Cấu phần thu nhập (lương, phụ cấp, bổ sung, thưởng…) có cờ tính đóng bảo hiểm và chịu thuế riêng. | PAY |
| Thẻ kho (Sổ kho) | Bin (Stock) Card |  | Sổ kế toán theo dõi nhập–xuất–tồn số lượng từng mặt hàng tại kho (Mẫu S12-DN), do thủ kho ghi. | INV |
| Thỏa thuận khung | Framework Agreement |  | Cam kết dài hạn về giá/khối lượng với nhà cung cấp, từ đó phát hành nhiều PO theo nhu cầu. | PUR |
| Thời gian chờ | Lead Time |  | Khoảng thời gian từ khi phát lệnh đến khi có hàng; dùng để bù lùi ngày phát lệnh theo lịch làm việc. | MFG |
| Thời gian phản hồi | Response Time |  | Khoảng thời gian cam kết từ khi tạo ticket đến phản hồi lần đầu; tính theo lịch làm việc SLA. | SVC |
| Thời gian xử lý | Resolution Time |  | Khoảng thời gian cam kết để xử lý xong yêu cầu; đồng hồ tạm dừng khi chờ khách. | SVC |
| Thử việc | Probation |  | Giai đoạn thử việc tối đa 6–180 ngày tùy chức danh, lương ≥85%; không thuộc đối tượng BHXH bắt buộc nếu đúng luật. | HR |
| Tiền lương đóng bảo hiểm | Insurable Salary Base |  | Mức lương + phụ cấp lương + khoản bổ sung khác xác định được (Đ.7 NĐ 158/2025). | PAY |
| Trung tâm làm việc | Work Center |  | Nguồn lực (máy/tổ) thực hiện công đoạn, có công suất, lịch làm việc và đơn giá giờ máy/giờ công. | MFG |
| Trả hàng bán | Sales return |  | Khách trả lại hàng đã mua; nhập lại kho và ghi giảm doanh thu qua TK 521. | SAL |
| Trả hàng nhà cung cấp | Return to Vendor |  | Trả lại hàng không đạt sau khi đã nhận; giảm tồn, đảo bút toán nhập và điều chỉnh thuế GTGT đầu vào. | PUR |
| Trợ cấp thôi việc | Severance Allowance |  | ½ tháng lương cho mỗi năm làm việc, trừ thời gian đã tham gia BHTN (Đ.46 BLLĐ). | HR |
| Trừ lùi vật tư | Backflush |  | Tự động trừ NVL theo BOM khi hoàn thành (tại thời điểm phát lệnh/công đoạn/nhập kho) thay cho xuất kho thủ công. | MFG |
| Tuân thủ tiến độ | Schedule Adherence |  | Tỷ lệ số lệnh sản xuất hoàn thành đúng hạn so với tổng số lệnh theo kế hoạch. | MFG |
| Tài khoản trung gian hàng/hóa đơn | Goods Receipt/Invoice Receipt clearing | GR/IR | Tài khoản tạm bắc cầu chênh lệch thời điểm nhận hàng và nhận hóa đơn; kế toán VN không có TK clearing riêng mà dùng tiểu khoản 331 (hàng về chưa hóa đơn) hoặc 151. | PUR |
| Tài khoản trung gian nhận hàng–nhận hóa đơn | GR/IR Clearing Account | GR/IR | Tài khoản trung gian giữa ghi nhận nhận hàng và nhận hóa đơn; số dư còn lại là tín hiệu chưa khớp, cần đối chiếu cuối kỳ. | PUR |
| Tài sản hợp đồng | Contract Asset (Unbilled) |  | Doanh thu đã ghi nhận theo tiến độ nhưng chưa xuất hóa đơn; VAS chưa có tài khoản riêng ngoài TK 337 cho xây dựng. | PRJ |
| Tách biệt nhiệm vụ | Segregation of duties | SoD | Nguyên tắc tách người tạo đơn, duyệt, xuất kho và ghi sổ để ngừa gian lận. | SAL |
| Tính lại hồi tố | Retroactive Calculation | Retro | Tính lại kỳ cũ theo tham số đúng thời điểm khi lương/tỷ lệ/mức tối thiểu thay đổi hồi tố; sinh truy lĩnh/truy thu kỳ hiện tại. | PAY |
| Tạm ứng lương | Salary Advance |  | Khoản ứng trước trừ vào lương kỳ sau (TK 141); hạn mức cấu hình (ví dụ ≤50% lương tháng), không làm Net âm. | PAY |
| Tồn kho khả dụng | Available-to-Promise | ATP | Lượng hàng có thể cam kết giao = tồn thực tế − đã giữ chỗ − tồn an toàn + dự kiến nhập trong khung thời gian. | SAL |
| Tồn khả dụng | Available-to-Promise | ATP | Số lượng còn có thể cam kết bán = tồn thực tế − đã giữ − đã phân bổ (+ dự kiến nhập nếu cấu hình). | INV |
| Tồn tối thiểu/tối đa | Min-Max Planning |  | Phương pháp bổ sung: khi tồn ≤ min thì đặt hàng đưa tồn lên tới max. | INV |
| Tồn đang chuyển | Goods in Transit |  | Lượng hàng đã xuất khỏi kho đi nhưng chưa nhập vào kho đến; vẫn thuộc sở hữu doanh nghiệp và được theo dõi riêng. | INV |
| Tỷ lệ chuyển đổi | Conversion Rate |  | Tỷ lệ lead chuyển thành cơ hội và cơ hội chuyển thành thắng; đo hiệu quả bán và chất lượng nguồn. | CRM |
| Tỷ lệ hoàn thành | Percentage of Completion | POC | Phương pháp ghi nhận doanh thu/chi phí theo mức độ hoàn thành của hợp đồng tại ngày lập báo cáo. | PRJ |
| Tỷ lệ sửa xong lần đầu | First-Time Fix Rate | FTFR | Tỷ lệ work order xử lý xong ngay lần đầu; chỉ số hiệu quả dịch vụ hiện trường. | SVC |
| Vận chuyển | Shipment |  | Chứng từ theo dõi vận chuyển, cước phí và trạng thái giao nhận hàng. | SAL |
| Vị trí / Chức danh | Position / Job |  | Chỗ làm việc có định biên thuộc một đơn vị, gắn ngạch-bậc và người quản lý trực tiếp; nhóm chức danh quyết định thời gian thử việc. | HR |
| Xuất kho | Goods Issue | GI | Nghiệp vụ ghi nhận hàng ra khỏi kho (bán, sản xuất, nội bộ, hao hụt), làm giảm tồn và sinh giá vốn/chi phí. | INV |
| Xuất kho ghi giá vốn | Goods issue | GI | Nghiệp vụ xuất hàng khỏi kho, giảm tồn và sinh bút toán giá vốn (Nợ 632/Có 156 hoặc 157). | INV |
| Xuất theo hạn dùng gần nhất | First-Expired-First-Out | FEFO | Chiến lược chọn hàng xuất lô có hạn dùng gần nhất trước; áp dụng cho dược, thực phẩm. | INV |
| Xác định cỡ lô | Lot Sizing |  | Quy tắc gộp nhu cầu ròng thành số lượng đặt: Lot-for-Lot, FOQ, EOQ, POQ, Min-Max. | MFG |
| Yêu cầu báo giá | Request for Quotation | RFQ | Văn bản mời nhiều nhà cung cấp chào giá cho cùng một nhu cầu để so sánh cạnh tranh. | PUR |
| Yêu cầu bảo hành nhà cung cấp | Vendor Warranty Claim |  | Thu hồi chi phí bảo hành từ nhà sản xuất/NCC; theo dõi như phải thu khác, không tính vào giá vốn công ty. | SVC |
| Yêu cầu dịch vụ | Service Request |  | Đề nghị thực hiện dịch vụ/sửa chữa, thường sinh từ ticket; là căn cứ tạo lệnh công việc. | SVC |
| Yêu cầu thay đổi | Change Request / Variation |  | Đề nghị điều chỉnh phạm vi, giá trị hợp đồng hoặc ngân sách; phải duyệt trước khi áp dụng. | PRJ |
| Điều chỉnh tồn kho | Stock Adjustment |  | Bút toán xử lý chênh lệch thừa/thiếu khi kiểm kê, hàng hỏng hoặc hao hụt, kèm mã lý do. | INV |
| Điều kiện giao hàng | Incoterms |  | Bộ điều kiện thương mại quốc tế (FOB, CIF, DAP...) xác định ai chịu cước/bảo hiểm, ảnh hưởng landed cost và trị giá hải quan. | PUR |
| Điều kiện giá | Pricing condition |  | Thành phần cấu thành giá (giá gốc, chiết khấu, phụ phí, thuế) áp theo kỹ thuật điều kiện/pricing procedure. | SAL |
| Điều phối | Dispatching |  | Xếp lịch và phân công kỹ thuật viên theo kỹ năng, địa bàn, lịch làm việc để tối ưu chuyến thăm. | SVC |
| Điểm đặt hàng lại | Reorder Point | ROP | Mức tồn kích hoạt đề xuất bổ sung = nhu cầu bình quân trong thời gian giao hàng + tồn an toàn. | INV |
| Đoàn phí công đoàn | Union Membership Dues |  | Khoản đoàn viên đóng 1% (có trần), trừ vào lương; không phải chi phí doanh nghiệp. | PAY |
| Đánh giá nhà cung cấp | Vendor Evaluation |  | Chấm điểm nhà cung cấp theo giá, chất lượng, giao hàng, dịch vụ theo chu kỳ; dùng để ưu tiên hoặc loại nhà cung cấp. | PUR |
| Đánh giá tác động xử lý dữ liệu cá nhân | Data Protection Impact Assessment | DPIA | Hồ sơ phân tích rủi ro khi xử lý DLCN quy mô lớn; bắt buộc theo Điều 21 Luật 91/2025/QH15. | CRM |
| Đóng dự án | Project Closing |  | Chuyển dự án sang trạng thái CLOSED sau khi hết PO mở, timesheet đã duyệt, WIP và chênh lệch unbilled/deferred đã xử lý. | PRJ |
| Đóng lệnh & tính giá thành | Order Settlement (Close) |  | Tập hợp chi phí, tính giá thành thực tế, kết chuyển chênh lệch và đóng lệnh sản xuất. | MFG |
| Đóng sớm | Short-close |  | Đóng phần còn lại của chứng từ nguồn dù chưa đủ số lượng; phần dư về 0, không xóa phần đã thực hiện. | PUR |
| Đăng ký bảo hành | Warranty Registration |  | Kích hoạt quyền bảo hành theo số serial sau khi bán/giao hàng; xác định ngày hết hạn bảo hành. | SVC |
| Đơn bán hàng | Sales order | SO | Chứng từ cam kết bán hàng, số lượng, giá, ngày giao; giữ chỗ tồn và chiếm dụng hạn mức tín dụng. | SAL |
| Đơn giá tính phí | Bill Rate |  | Giá bán cho khách hàng của một đơn vị nguồn lực/giờ công, lấy từ bảng giá bán. | PRJ |
| Đơn hàng khung | Blanket Order |  | Một đơn tổng cho khối lượng/giá trị cố định trong kỳ, được gọi hàng (release) nhiều lần cho tới khi hết hạn mức. | PUR |
| Đơn mua hàng | Purchase Order | PO | Cam kết mua chính thức với nhà cung cấp (hàng, số lượng, giá, điều kiện); bản thân PO không sinh bút toán tài chính, chỉ giữ chỗ ngân sách. | PUR |
| Đơn vị tính | Unit of Measure | UoM | Đơn vị đo lường số lượng hàng; có ĐVT cơ sở dùng lưu kho và các ĐVT mua/bán quy đổi về ĐVT cơ sở theo hệ số cố định. | INV |
| Đặt hàng đến thu tiền | Order-to-Cash | O2C | Chu trình bán hàng khép kín từ nhận đơn/khách hàng đến khi thu được tiền và ghi nhận doanh thu. | SAL |
| Đề nghị mua hàng | Purchase Requisition | PR | Chứng từ nội bộ ghi nhận nhu cầu mua, dùng để xin ngân sách và phê duyệt chủ trương trước khi đặt hàng; không ghi sổ kế toán. | PUR |
| Định mức nguyên vật liệu | Bill of Materials | BOM | Danh sách linh kiện và định mức để sản xuất một đơn vị sản phẩm; có thể đa cấp và có nhiều phiên bản theo ngày hiệu lực. | MFG |
| Định tuyến | Routing |  | Trình tự các công đoạn và trung tâm làm việc để sản xuất một sản phẩm, kèm thời gian setup và thời gian chạy. | MFG |
| Đối chiếu hai chiều | Two-way Matching |  | Đối chiếu Hóa đơn với Đơn mua hàng (số lượng đặt và đơn giá), dùng khi không bắt buộc đối chiếu số lượng nhận thực tế. | PUR |
| Đồng sản phẩm | Co-product |  | Nhiều sản phẩm chính cùng ra từ một quá trình; chi phí được phân bổ theo hệ số. | MFG |
| Độ chính xác tồn kho | Inventory Record Accuracy | IRA | Mức khớp giữa sổ sách và thực tế tồn kho; cần đạt ≥ 95% để MRP cho kết quả tin cậy. | MFG |
| Ước tính chi phí khi hoàn thành | Estimate at Completion | EAC | Tổng chi phí dự kiến của dự án = chi phí thực tế lũy kế + chi phí còn phải chi (ETC). | PRJ |
| Ứng trước người bán | Advance to Supplier |  | Khoản trả trước cho nhà cung cấp trước khi nhận hàng; phản ánh ở số dư Nợ TK 331 và bù trừ khi có hóa đơn. | PUR |

## ERP tổng quát, hệ thống, BA & triển khai (gồm thuật ngữ từ 4 cuốn sách)

| Thuật ngữ (VI) | Tiếng Anh | Viết tắt | Định nghĩa ngắn | Module |
|---|---|---|---|---|
| Bản địa hóa | Localization | l10n | Tùy chỉnh theo đặc thù một vùng: tiền tệ VND, định dạng ngày/số, mã số thuế, mẫu biểu luật định VN. | LOC |
| Bảo mật mức trường | Field-level security |  | Ẩn/khóa/che một phần một trường nhạy cảm (lương, giá vốn, số tài khoản, PII) theo vai trò, dù vẫn cho xem chứng từ. | SYS |
| Bộ tiêu chí INVEST | INVEST criteria | INVEST | Sáu tiêu chí story tốt: Independent, Negotiable, Valuable, Estimable, Small, Testable (Bill Wake). | BA |
| Chuyển dữ liệu cá nhân ra nước ngoài | Cross-border data transfer |  | Việc lưu/xử lý dữ liệu cá nhân trên máy chủ/đám mây hoặc bên nhận ở nước ngoài; phải lập hồ sơ đánh giá (NĐ356 Điều 17-18). | LEGAL |
| Chuẩn kiểm chứng an ninh ứng dụng | Application Security Verification Standard | ASVS | Chuẩn OWASP (bản 5.0, 5/2025) với 3 mức lũy tiến L1/L2/L3 để đặt và kiểm mục tiêu bảo mật ứng dụng. | SEC |
| Chỉ số hiệu suất chính | Key Performance Indicator | KPI | Chỉ số đo hiệu quả trên dashboard; phải có công thức, nguồn dữ liệu, kỳ so sánh rõ ràng và áp phạm vi dữ liệu người xem. | SYS |
| Chống chối bỏ | Non-repudiation |  | Bảo đảm người thực hiện hành động không thể phủ nhận đã làm, nhờ log và chữ ký/xác thực. | AUDIT |
| Chứng từ giao dịch | Transaction Document |  | Chứng từ nghiệp vụ có một đầu (header) và nhiều dòng (lines), ví dụ PO, phiếu nhập, hóa đơn, phiếu kế toán. | SYS |
| Câu chuyện người dùng | User story | US | Mô tả ngắn một nhu cầu theo khuôn 'Là <vai trò>, tôi muốn <năng lực>, để <giá trị>'. | BA |
| Cú pháp Gherkin | Gherkin |  | Cú pháp Given/When/Then (Cho trước/Khi/Thì) + And/But mô tả kịch bản nghiệm thu đọc được (Cucumber). | BA |
| Cửa sổ xử lý theo lô | Batch window |  | Khoảng thời gian cho phép chạy tác vụ nền định kỳ (tính giá vốn, khấu hao, kết chuyển, đồng bộ) mà không ảnh hưởng nghiệp vụ trực tuyến. | PERF |
| Dịch vụ thông báo Zalo | Zalo Notification Service | ZNS | Kênh gửi thông báo giao dịch qua Zalo OA; chỉ công ty VN, cần người nhận đồng ý, dùng mẫu đã duyệt, một tin/một giao dịch. | SYS |
| Dữ liệu chủ / Danh mục | Master Data | MD | Đối tượng khai báo một lần rồi dùng lại ở nhiều chứng từ (nhà cung cấp, vật tư, khách hàng, tài khoản...); quản lý CRUD + active/inactive thay cho xóa cứng. | SYS |
| Dữ liệu cá nhân nhạy cảm | Personally Identifiable Information | PII | Dữ liệu định danh cá nhân (CCCD, lương, sức khỏe) cần bảo mật mức trường và kiểm soát truy cập. | SYS |
| Hiệu lực theo ngày | Effective dating |  | Lưu lịch sử giá trị tham số và áp dụng theo ngày chứng từ; dùng cho giá trị pháp lý (thuế, BHXH, tỷ giá). | SYS |
| Hướng dẫn tiếp cận nội dung web | Web Content Accessibility Guidelines | WCAG | Chuẩn W3C (bản 2.2, 2023) về khả năng tiếp cận cho người khuyết tật; mức A/AA/AAA, thường nhắm AA. | USAB |
| Hạn mức phê duyệt | Approval authority / Delegation of Authority | DOA | Quy định ai được duyệt đến mức giá trị nào, qua mấy cấp; ngưỡng tiền phải là tham số. | SYS |
| Khóa lạc quan | Optimistic locking |  | Cơ chế chống mất cập nhật: ghi theo phiên bản, người lưu sau bị cảnh báo xung đột thay vì ghi đè im lặng. | DATA |
| Khóa tài khoản | Account lockout |  | Khóa tài khoản sau N lần đăng nhập sai liên tiếp, tự mở sau khoảng khóa hoặc do admin; chống dò mật khẩu. | SYS |
| Không nhảy cách | Gapless |  | Chính sách đánh số liên tục không có lỗ; chỉ cấp số khi lưu thành công, tốn hiệu năng và cần khóa. | SYS |
| Khơi gợi yêu cầu | Elicitation |  | Kỹ thuật thu thập yêu cầu: phỏng vấn, workshop, quan sát, phân tích tài liệu, prototype, mô hình hóa quy trình, khảo sát. | BA |
| Khả năng mở rộng | Scalability |  | Năng lực tăng công suất (ngang/dọc) khi dữ liệu và người dùng tăng mà không phải viết lại kiến trúc. | DATA |
| Kiểm soát giảm thiểu | Mitigating control |  | Biện pháp bù khi buộc kiêm nhiệm vai trò xung đột: phê duyệt cấp trên, báo cáo ngoại lệ định kỳ, lưu vết. | SYS |
| Ký hiệu BPMN | Business Process Model and Notation | BPMN | Ký hiệu mô hình hóa quy trình (OMG 2.0): sự kiện, hoạt động, cổng, luồng tuần tự/thông điệp, pool/lane. | BA |
| Luật Bảo vệ dữ liệu cá nhân | Personal Data Protection Law | PDPL | Luật số 91/2025/QH15, hiệu lực 01/01/2026, khung pháp lý về xử lý và bảo vệ dữ liệu cá nhân tại VN. | LEGAL |
| Luồng chứng từ | Document Flow |  | Chuỗi liên kết các chứng từ nguồn–đích (PR→PO→nhập→hóa đơn) với liên kết hai chiều để truy vết. | SYS |
| Lưu trữ dài hạn / đóng băng dữ liệu | Archiving |  | Chuyển dữ liệu kỳ cũ sang vùng lưu trữ tách khỏi dữ liệu vận hành nhưng vẫn truy xuất đọc khi cần. | DATA |
| Ma trận truy vết yêu cầu | Requirements Traceability Matrix | RTM | Bảng liên kết yêu cầu với FR/AC/test để kiểm đủ bao phủ và phát hiện yêu cầu mồ côi; trong skill sinh tự động bởi ba.py trace. | BA |
| Mô hình 3C | Card-Conversation-Confirmation | 3C | Ba thành phần của user story: thẻ (card), đối thoại (conversation), xác nhận (confirmation) — Ron Jeffries. | BA |
| Mô hình chất lượng sản phẩm | Product quality model (ISO/IEC 25010:2023) | ISO 25010 | Chuẩn quốc tế định nghĩa 9 đặc tính chất lượng phần mềm, dùng làm khung rà soát để không bỏ sót loại NFR. | SYS |
| Mùi yêu cầu / từ cấm | Requirement smell |  | Từ/cụm mơ hồ (nhanh, dễ dùng, linh hoạt, v.v., tương tự, có thể, phù hợp, tối ưu…) khiến yêu cầu không kiểm chứng được. | BA |
| Mẫu câu EARS | Easy Approach to Requirements Syntax | EARS | Bộ mẫu câu yêu cầu (phổ quát; sự kiện KHI/WHEN; trạng thái TRONG KHI/WHILE; tùy chọn WHERE; không mong muốn NẾU-THÌ/IF-THEN; phức hợp) giảm nhập nhằng (Mavin et al., RE'09). | BA |
| Mục tiêu thời gian khôi phục | Recovery Time Objective | RTO | Thời gian tối đa chấp nhận hệ thống ngừng để khôi phục sau sự cố. | AVAIL |
| Mục tiêu điểm khôi phục | Recovery Point Objective | RPO | Lượng dữ liệu tối đa chấp nhận mất khi sự cố, tính theo thời gian lùi về bản sao lưu gần nhất. | AVAIL |
| Ngày chứng từ | Document Date |  | Ngày lập/ghi trên chứng từ; có thể khác ngày hạch toán. | SYS |
| Nhiệm vụ | Duty |  | Trong Dynamics 365: nhóm đặc quyền tương ứng một phần quy trình nghiệp vụ; gán cho vai trò. | SYS |
| Nhật ký kiểm toán field-level | Audit Trail |  | Ghi bất biến thay đổi từng trường (giá trị cũ→mới, ai, khi nào); SAP dùng change documents CDHDR/CDPOS. | SYS |
| Phân làn trách nhiệm | Swimlane |  | Phân làn sơ đồ quy trình theo vai trò/participant (pool/lane BPMN); trong Mermaid dùng một subgraph cho mỗi vai trò. | BA |
| Phân quyền theo vai trò | Role-Based Access Control | RBAC | Mô hình gán quyền theo vai trò kèm phạm vi dữ liệu; phải chặn ở tầng máy chủ, không chỉ ẩn nút giao diện. | SEC |
| Phân tách nhiệm vụ | Segregation of Duties | SoD | Nguyên tắc không để một người nắm đủ các bước nhạy cảm để tự hoàn tất và che giấu gian lận; tách Phê duyệt/Ghi chép/Giữ tài sản/Đối chiếu. | SYS |
| Phân vị 95 | 95th percentile | p95 | Ngưỡng mà 95% số lần đo nằm dưới; dùng thay giá trị trung bình để phản ánh trải nghiệm thực. | PERF |
| Phạm vi dữ liệu | Data Scope |  | Giới hạn ai thấy/sửa dữ liệu nào (Của mình/Phòng/Chi nhánh/Công ty/Toàn hệ thống); áp ở backend cho mọi list/report/API. | SYS |
| Phục hồi thảm họa | Disaster Recovery | DR | Năng lực và quy trình khôi phục hệ thống sau sự cố nghiêm trọng; được kiểm chứng bằng diễn tập (DR drill) định kỳ. | AVAIL |
| Quy trình duyệt nhiều cấp | Multi-level Approval |  | Luồng phê duyệt theo số tiền/phòng ban/loại chứng từ, tuần tự hoặc song song, có ủy quyền, leo thang, thu hồi, lịch sử duyệt bất biến. | SYS |
| Quy tắc bản ghi | Record rule |  | Cơ chế lọc từng bản ghi theo điều kiện (Odoo ir.rule): rule toàn cục giao nhau (AND), rule theo nhóm hợp nhất (OR). | SYS |
| Quy tắc nghiệp vụ | Business rule | BR | Ràng buộc của nghiệp vụ mà yêu cầu chức năng phải tuân theo; ghi là BR-* trong skill. | BA |
| Quyền | Permission |  | Khả năng thực hiện một hành động (Xem/Tạo/Duyệt/Ghi sổ...) trên một đối tượng (chức năng/chứng từ/trường), trong một phạm vi dữ liệu. | SYS |
| Quyền truy cập mô hình | Access rights |  | Quyền đọc/ghi/tạo/xóa trên cả một đối tượng dữ liệu (Odoo ir.model.access), cộng dồn từ mọi nhóm của người dùng. | SYS |
| Quốc tế hóa | Internationalization | i18n | Thiết kế hệ thống đa ngôn ngữ/đa locale, không chôn cứng chuỗi và định dạng trong mã. | LOC |
| Rà soát dẫn dắt | Walkthrough |  | Đánh giá phi hình thức do tác giả dẫn người đọc qua tài liệu để lấy phản hồi và phát hiện hiểu lầm. | BA |
| Sơ đồ phân loại yêu cầu | Requirements classification schema |  | Khung BABOK v3 chia yêu cầu thành business, stakeholder, solution (functional/non-functional) và transition. | BA |
| Sự đồng ý của chủ thể dữ liệu | Consent |  | Sự đồng ý phải chứng minh được ai đồng ý, khi nào, cho mục đích gì; hệ thống phải lưu và hỗ trợ rút lại. | LEGAL |
| Tham số hệ thống | System parameter | PRM | Giá trị cấu hình điều khiển hành vi nghiệp vụ, đổi được không cần sửa code; định nghĩa một lần trong catalog. | SYS |
| Thông lượng | Throughput |  | Số giao dịch hệ thống xử lý được trong một đơn vị thời gian dưới mức tải xác định. | PERF |
| Thẩm định | Verification |  | Kiểm 'xây đúng cách chưa': tài liệu đúng chuẩn, nhất quán, đủ — tương ứng bước 4 (tự kiểm) và bước 5 (review) của skill. | BA |
| Thực hiện một phần | Partial Fulfilment |  | Theo dõi số lượng đặt/đã nhận/đã xuất hóa đơn/còn lại ở mức dòng để giao–nhận–lập hóa đơn nhiều lần. | SYS |
| Tiêu chí nghiệm thu | Acceptance criteria | AC | Điều kiện khách quan xác nhận một chức năng/story đã thỏa; viết dạng Gherkin Cho trước/Khi/Thì. | BA |
| Truy cập đặc quyền | Privileged access |  | Quyền quản trị cao; phải tách tài khoản, cấp có thời hạn, ghi log đầy đủ (ISO 27001 A.8.2). | SYS |
| Truy vết hai chiều | Bi-directional traceability |  | Liên kết xuôi (nhu cầu→FR→AC→test) và ngược (FR→REQ→nhu cầu) để diệt chức năng thừa (mồ côi) và phát hiện thiếu bao phủ. | BA |
| Tác vụ nền / định kỳ | Background / Scheduled Job |  | Xử lý khối lượng lớn hoặc theo lịch (MRP, khấu hao, tính giá, kết chuyển) với chạy thử, run log, chống chạy trùng, chạy lại idempotent. | SYS |
| Tách biệt trách nhiệm | Segregation of Duties | SoD | Nguyên tắc người tạo ≠ người duyệt ≠ người ghi sổ cho cùng một giao dịch, nhằm chống gian lận. | SYS |
| Tính bất biến | Immutability |  | Thuộc tính không thể sửa/xóa của dữ liệu đã ghi (vết kiểm toán, chứng từ đã ghi sổ); sửa sai phải qua bút toán Đảo. | AUDIT |
| Tính bất biến khi lặp | Idempotency |  | Thuộc tính xử lý lại cùng dữ liệu/bản tin (import, tích hợp, job) không tạo kết quả trùng. | SYS |
| Tính lũy đẳng | Idempotency |  | Thuộc tính của giao dịch tích hợp: chạy lại nhiều lần cho cùng một kết quả, tránh nhân đôi (phát hành/chi trùng). | INTG |
| Tính sẵn sàng | Availability |  | Tỷ lệ thời gian hệ thống sẵn sàng phục vụ (uptime) trong khoảng đo, thường tính theo % và trừ bảo trì có kế hoạch. | AVAIL |
| Tạo từ chứng từ nguồn | Copy-from / Create with Reference |  | Sinh chứng từ đích bằng cách kéo dữ liệu từ chứng từ nguồn; SAP cấu hình bằng copy control (VTAA/VTLA/VTFL). | SYS |
| Từ khóa mức yêu cầu | Requirement level keywords (RFC 2119) | RFC2119 | Chuẩn từ khóa MUST/SHALL, SHOULD, MAY ↔ PHẢI, NÊN, ĐƯỢC PHÉP dùng để nêu mức bắt buộc của yêu cầu. | BA |
| Vai trò | Role |  | Tập hợp quyền tương ứng một chức danh/nhóm trách nhiệm; đơn vị được gán cho người dùng. | SYS |
| Vết kiểm toán | Audit trail |  | Bản ghi bất biến ai làm gì, khi nào, giá trị trước–sau trên dữ liệu nghiệp vụ; nền tảng cho kiểm toán và thanh tra thuế. | AUDIT |
| Xác nhận giá trị | Validation |  | Kiểm 'xây đúng thứ chưa': đúng nhu cầu nghiệp vụ thật của khách hàng — tương ứng khách hàng/PO duyệt. | BA |
| Xác thực đa yếu tố | Multi-Factor Authentication | MFA | Đăng nhập yêu cầu ít nhất hai yếu tố (mật khẩu + mã OTP/thiết bị); bắt buộc cho vai trò nhạy cảm. | SEC |
| Yêu cầu chuyển đổi | Transition requirement |  | Năng lực tạm thời để chuyển từ hệ cũ sang hệ mới (di trú dữ liệu, số dư đầu kỳ, đào tạo, cutover); hết vai trò sau go-live, hay bị bỏ sót. | BA |
| Yêu cầu chức năng | Functional requirement | FR | Mô tả hệ thống làm gì và xử lý thông tin gì; mỗi FR là một yêu cầu đơn nhất, kiểm thử được, có nguồn. | BA |
| Yêu cầu các bên liên quan | Stakeholder requirements | REQ | Nhu cầu của từng nhóm người dùng để đạt mục tiêu nghiệp vụ; cầu nối giữa yêu cầu nghiệp vụ và yêu cầu giải pháp. | BA |
| Yêu cầu nghiệp vụ | Business requirements |  | Mục tiêu và lý do thực hiện dự án, trả lời câu hỏi 'vì sao'; có thể ở cấp doanh nghiệp, mảng nghiệp vụ hoặc sáng kiến. | BA |
| Yêu cầu phi chức năng | Non-Functional Requirement | NFR | Yêu cầu về thuộc tính chất lượng của hệ thống (hiệu năng, bảo mật, sẵn sàng...) thay vì chức năng cụ thể; phải đo lường và kiểm chứng được. | SYS |
| Đánh giá Fagan | Fagan inspection |  | Đánh giá hình thức có vai trò (moderator, author, reader, recorder) và giai đoạn; tách việc tìm lỗi khỏi việc sửa lỗi. | BA |
| Đánh số chứng từ | Document Numbering |  | Quy tắc sinh số định danh theo loại/chi nhánh/năm; SAP number ranges, Oracle document sequences, Dynamics number sequences, Odoo ir.sequence. | SYS |
| Đánh số chứng từ liên tục | Gap-less numbering |  | Yêu cầu số chứng từ/hóa đơn liên tục, không trùng, không nhảy số kể cả khi nhiều người tạo đồng thời. | DATA |
| Đăng nhập một lần | Single Sign-On | SSO | Đăng nhập tập trung qua IdP (SAML/OIDC/LDAP); tắt tài khoản tại IdP là chặn được truy cập ERP. | SYS |
| Đặc quyền | Privilege |  | Trong Dynamics 365: nhóm quyền trên các entry point để thực hiện một tác vụ; cấu thành Duty. | SYS |
| Đặc quyền tối thiểu | Least privilege |  | Nguyên tắc chỉ cấp quyền tối thiểu đủ để làm việc (ISO 27001 A.8.3). | SYS |
| Định nghĩa Hoàn thành | Definition of Done | DoD | Điều kiện để một đặc tả được coi là xong và code được. | BA |
| Định nghĩa Sẵn sàng | Definition of Ready | DoR | Điều kiện đủ để bắt đầu viết hoặc ước lượng một đặc tả chức năng. | BA |
| Đọc theo góc nhìn | Perspective-Based Reading | PBR | Mỗi người đọc tài liệu qua một vai trò (lập trình viên/kiểm thử/khách hàng/kiểm toán) để bao phủ rộng hơn, ít trùng (Basili et al.). | BA |
| Đối soát | Reconciliation |  | So khớp dữ liệu giữa ERP và hệ thống ngoài (hóa đơn điện tử, ngân hàng) định kỳ để phát hiện lệch. | INTG |
| Đối tượng phân quyền | Authorization object |  | Trong SAP: đơn vị kiểm tra quyền gồm tối đa 10 field (vd ACTVT: 01 Tạo, 02 Sửa, 03 Xem, 06 Xóa); đạt khi tất cả field khớp. | SYS |
| Độ ưu tiên tham số | Parameter precedence |  | Khi tham số có nhiều cấp, lấy giá trị cấp cụ thể nhất: Người dùng > Chi nhánh > Công ty > Hệ thống. | SYS |
| Ưu tiên MoSCoW | MoSCoW prioritisation | MoSCoW | Ưu tiên theo mức bắt buộc trong timebox: Must have / Should have / Could have / Won't have this time (DSDM). | BA |
| 5 chiến lược phản ứng (Oliver 1991) | Oliver's Five Strategic Responses |  | acquiescence → compromise → avoidance → defiance → manipulation (kháng cự tăng dần); dùng để lường kháng cự người dùng khi lập change management. | Sách: elbardan-erp-governance-audit ch04 |
| An ninh dữ liệu | Data security |  | Lớp RBAC trên dữ liệu + giả định kiểm soát: confidentiality, authentication, integrity, non-repudiation; dữ liệu đã nhập không sửa được; gateway quản lý user profile. | Sách: elbardan-erp-governance-audit ch07 |
| Ba loại pilot / pilot thực tế | Three Kinds of Pilots / Live Pilot |  | Computer → Conference room (data giả, 'play Murphy') → Live pilot (chạy thật, chứng minh works + user sign-off) trước khi cutover. | Sách: wallace-erp-implementation ch11 |
| Ba núm điều chỉnh | Three Knobs |  | Work (khối lượng), Time (thời gian lịch), Resources (nguồn lực); giữ cố định hai, xoay núm còn lại. Company-wide xoay resource; Quick-Slice giảm work. | Sách: wallace-erp-implementation ch02 |
| Ba thành phần CRM | Operational / Analytical / Collaborative CRM |  | Tự động hóa quy trình (operational), phân tích dữ liệu & báo cáo (analytical), kênh cộng tác email/chat/web (collaborative). | Sách: parthasarathy-erp-fundamentals ch08 |
| Ba áp lực thể chế | Coercive / Normative / Mimetic pressures |  | Ép buộc bằng luật/quy định (coercive), chuẩn nghề/đào tạo (normative), bắt chước mô hình thành công (mimetic); dùng truy nguồn và xếp ưu tiên yêu cầu. | Sách: elbardan-erp-governance-audit ch04 |
| Ba động cơ giữ tồn kho | Three motives for holding inventory |  | Transactions motive (vận hành trơn tru), Precautionary motive (phòng bất định), Speculative motive (đầu cơ). | Sách: parthasarathy-erp-fundamentals ch03 |
| BOM dạng module | Modular / Planning Bills |  | BOM module cho sản phẩm nhiều option, phục vụ forecasting/master scheduling/order promising; forecast ở cấp model thay vì từng SKU. | Sách: wallace-erp-implementation ch10 |
| Bán hàng & phân phối | Sales & Distribution (SD) |  | 6 key element: Selling, Shipping, Billing, Master Data Management, Order Management, Pricing; luồng liên module Sales→Shipping→Billing. | Sách: parthasarathy-erp-fundamentals ch03 |
| Báo cáo ngoại lệ / cảnh báo đỏ | Exception / red-alert reports |  | Báo cáo khi có sử dụng/giao dịch bất thường; nền của continuous monitoring. | Sách: elbardan-erp-governance-audit ch06 |
| Báo cáo trễ dự kiến | Anticipated Delay Report |  | Báo cáo từ xưởng/mua hàng gửi planner/master scheduler khi biết một job/PO sẽ trễ, nêu lý do và ngày hoàn thành mới; cốt lõi của closed loop. | Sách: wallace-erp-implementation ch12 |
| Báo giá-thu tiền / Yêu cầu-thanh toán | Quote-to-Cash / Requisition-to-Pay |  | Hai quy trình xuyên suốt ERP↔CRM: báo giá→đơn→hóa đơn→thu tiền; và yêu cầu mua→đơn mua→nhận hóa đơn→thanh toán. | Sách: parthasarathy-erp-fundamentals ch08 |
| bên nhận phần mềm | Software taker |  | Doanh nghiệp nhỏ/vừa chấp nhận phần mềm như nó vốn có, không đủ lực buộc vendor sửa riêng. | Sách: oleary-erp-systems-lifecycle ch08, ch09 |
| Bản đồ rủi ro / kiểm toán dựa trên rủi ro | Risk map / risk-based auditing |  | Xếp hạng rủi ro cao→thấp; phạm vi và lịch kiểm toán động theo đánh giá rủi ro. Rủi ro cao nhất: thay đổi quyền truy cập theo luân chuyển nhân sự. | Sách: elbardan-erp-governance-audit ch09 |
| Bảo mật chức năng | Function security |  | Lớp RBAC giới hạn user truy cập các menu/chức năng cụ thể trong ứng dụng. | Sách: elbardan-erp-governance-audit ch08 |
| bất đối xứng thông tin | Information asymmetry |  | Cùng một sự kiện nhưng các nhóm chức năng/địa điểm có báo cáo khác nhau, thông tin mắc kẹt cục bộ; ERP xóa nhờ CSDL chung. | Sách: oleary-erp-systems-lifecycle ch01 |
| Bật toàn bộ một phát | Big Bang / Cold Turkey |  | Chuyển đổi toàn công ty cùng lúc; rủi ro cực cao (một lỗi switch có thể chặn giao hàng) — khuyến cáo tránh cho planning/scheduling. | Sách: wallace-erp-implementation ch11 |
| Bốn loại kiểm soát ERP | ERP control types (inherent/configurable/security/reporting) |  | inherent (có sẵn, không code), configurable (phải cấu hình), security (phân quyền + SoD), reporting (báo cáo chuẩn/ad hoc) — giúp phân định code vs config. | Sách: elbardan-erp-governance-audit ch06 |
| bộ cấu hình/kiểm lỗi đơn | Configuration Engine (CE) |  | Cỗ máy kiểm tra đơn hàng để chặn lỗi phổ biến (sai part number) và liệt kê linh kiện cần build; lõi của web-ordering và build-to-order. | Sách: oleary-erp-systems-lifecycle ch14 |
| cam kết giao hàng | Available to Promise (ATP) |  | Khả năng xác nhận và giữ tồn kho theo thời gian thực, cắt ngang nhiều site/module; chỉ có khi đủ hạ tầng ERP. | Sách: oleary-erp-systems-lifecycle ch07, ch11 |
| Chuẩn hóa | Standardisation |  | Standard business process + standard GL + standard chart of accounts; một cách làm duy nhất nên lệch chuẩn dễ lộ. | Sách: elbardan-erp-governance-audit ch06 |
| chính sách tái cấu trúc | Reengineering policy |  | Chính sách về mức tùy biến phần mềm và mức tái cấu trúc tổ chức khi triển khai ERP. | Sách: oleary-erp-systems-lifecycle ch09 |
| chọn tinh hoa | Best of breed |  | Chiến lược phối ghép module từ nhiều vendor; đánh đổi bằng sáu nhóm chi phí ẩn (tìm kiếm, look-and-feel, tích hợp, đội ngũ, lệch phiên bản, mất đồng nhất). | Sách: oleary-erp-systems-lifecycle ch03 |
| Chống đạn | Bulletproofing |  | Để người học đặt câu hỏi hóc búa tìm lỗ hổng ERP và nhận câu trả lời hợp lệ; câu hỏi không đáp được = lỗ hổng = mất ownership. | Sách: wallace-erp-implementation ch07 |
| chống đối người dùng | User resistance |  | Chống đối do thay đổi ai/cách nhập liệu khi tái cấu trúc; ảnh hưởng chi phí và thành bại triển khai. | Sách: oleary-erp-systems-lifecycle ch04 |
| Chức năng kiểm toán nội bộ | Internal Audit Function (IAF) |  | Đơn vị đảm bảo tính đầy đủ/hiệu quả của kiểm soát nội bộ; sau ERP phải chuyển từ 'soi lỗi' sang đảm bảo kiểm soát và quản trị rủi ro. | Sách: elbardan-erp-governance-audit ch01 |
| CSDL quan hệ | Relational database |  | Các bảng liên kết qua khóa tham chiếu, loại bỏ dư thừa; là lý do kỹ thuật khiến nguyên tắc nhập một lần khả thi. | Sách: oleary-erp-systems-lifecycle ch02 |
| Cây phê duyệt theo cấp | Approval hierarchy / Submit for Approval |  | Chọn 'Submit for Approval' tự chuyển chứng từ tới người duyệt đúng cấp theo thiết lập; nền của workflow phê duyệt. | Sách: elbardan-erp-governance-audit ch08 |
| công nghệ biểu mẫu web | Web Forms Technology (WFT) |  | Khách điền form trên Internet/intranet/extranet; dùng khi ít giao dịch, nhưng gây nhập liệu gấp đôi nếu originator nhiều giao dịch. | Sách: oleary-erp-systems-lifecycle ch14 |
| cổng theo vai trò | ERP portal |  | Cổng/desktop web gom truy cập module con, báo cáo, help-desk, lịch, email, tin tức, thương mại điện tử theo vai trò công việc. | Sách: oleary-erp-systems-lifecycle ch05, ch14 |
| Danh mục kiểm tra ABCD | ABCD Checklist for Operational Excellence |  | Bộ câu hỏi tự đánh giá Oliver Wight; Section 5 có 22 câu đo vận hành, rà ≥2 lần/năm, mỗi 'no' cần nguyên nhân + cách sửa + ngày sửa. | Sách: wallace-erp-implementation ch15 |
| Danh sách nghiệm thu | Implementers' Checklist |  | Danh sách task trả lời Yes/No cuối mỗi chương để nghiệm thu tuân thủ Proven Path; được thêm task, cấm xoá task. | Sách: wallace-erp-implementation ch05 |
| Dung sai đếm | Counting Tolerance |  | Dung sai cho hàng cân/đong; Class A dùng 0–5%, không vượt 5%; tuỳ giá trị, tần suất, lead time, mức trọng yếu của item. | Sách: wallace-erp-implementation ch10 |
| Dữ kiện gây ấn tượng | Factoid |  | Đổi %/$ thành con số-hình ảnh cụ thể gắn với nỗi đau lãnh đạo ('3% → 3.000 đơn/năm, 15 đơn/ngày') để bán vision/chiến lược; tránh bẫy 'either/or'. | Sách: wallace-erp-implementation ch16 |
| Dữ liệu khoan nhượng vs không khoan nhượng | Forgiving vs Unforgiving Data |  | Forgiving (chỉ cần hợp lý: lead time, order qty, safety stock, standards, forecasts) vs Unforgiving (cần chính xác cao: inventory, open orders, allocations, BOM, routings). | Sách: wallace-erp-implementation ch10 |
| Dự báo cộng tác | Collaborative Forecasting |  | Chia sẻ dự báo giữa nhà cung cấp và khách hàng để đạt một dự báo thống nhất; bước trung gian giữa cách cũ và VMI. | Sách: wallace-erp-implementation ch12 |
| Dự báo một con số | Single-Number Forecast |  | Chỉ một forecast duy nhất được công nhận chính thức, không phải mỗi phòng (Sales/Marketing/Finance) một con số. | Sách: wallace-erp-implementation ch08 |
| ERP II | ERP II |  | Định nghĩa lại của Gartner: ERP componentized + e-business + cộng tác chuỗi cung ứng; gồm Central/Corporate/Collaborative. | Sách: parthasarathy-erp-fundamentals ch02 |
| ERP lát cắt nhanh | Quick-Slice ERP |  | Chọn một product line tác động cao, triển khai đầy đủ chức năng ERP cho riêng nó, pilot ~120 ngày; chi phí/rủi ro thấp, payback sớm; pilot = cutover. | Sách: wallace-erp-implementation ch13 |
| giai đoạn ổn định | Stabilization period |  | 3-9 tháng sau go-live, hiệu năng thường tụt khi user làm quen quy trình/phần mềm mới; phải lập ngân sách và support organization. | Sách: oleary-erp-systems-lifecycle ch12 |
| giao diện tạm | Temporary interface |  | Cầu nối tạm giữa module ERP mới và legacy, đặc trưng của phased; là hạng mục công việc và rủi ro thực cần đặc tả. | Sách: oleary-erp-systems-lifecycle ch11 |
| Giao thức tình huống | Case Study Protocol |  | Chuẩn bị trước khi thu thập: thu gì, từ ai, bằng cách nào, vì sao; dùng làm template chuẩn hóa buổi họp elicitation giữa các dự án. | Sách: elbardan-erp-governance-audit ch12 |
| Giả định kiểm soát của ERP | Control assumptions of ERP |  | Bộ giả định vận hành hóa nguyên lý 'control'; dạng hợp nhất 11 ở ch10, mỗi tình huống dùng một tập con (IC 9; NC/NB/IB 10). Dùng làm checklist nghiệm thu 'đã chuẩn ERP chưa'. | Sách: elbardan-erp-governance-audit ch10 |
| Hiện thực hóa lợi ích | Benefits Realization |  | Lợi ích hiện theo 3 cấp: tự động hóa quy trình → cải thiện/tái thiết kế quy trình → hệ hỗ trợ ra quyết định; mất vài tháng tới ~1 năm. | Sách: parthasarathy-erp-fundamentals ch05 |
| hiện trạng / trạng thái đích | As Is / To Be |  | Mô hình quy trình hiện tại và quy trình tương lai mong muốn; khoảng cách giữa chúng là cơ sở chọn và cấu hình phần mềm. | Sách: oleary-erp-systems-lifecycle ch02, ch08, ch09 |
| Hoạch định bán hàng & vận hành | Sales & Operations Planning (S&OP) |  | Quy trình quyết định hằng tháng cân bằng cung–cầu ở mức VOLUME; 'tay nắm của ban lãnh đạo'; nối business plan với execution; là early win. | Sách: wallace-erp-implementation ch08 |
| Hoạch định nguồn lực doanh nghiệp | Enterprise Resource Planning (ERP) |  | Phần mềm đóng gói tích hợp mọi phòng ban trên một CSDL chung, chia sẻ thông tin real-time; giá trị nằm ở tính tích hợp 'enterprise'. | Sách: parthasarathy-erp-fundamentals ch01 |
| Hạng A/B/C/D | Class A/B/C/D |  | Thang đo mức dùng ERP hiệu quả (Oliver Wight): A = dùng hiệu quả toàn công ty với một bộ số thống nhất; D = dữ liệu sai, gần như vô dụng. | Sách: wallace-erp-implementation ch01 |
| hệ thống ERP | ERP system |  | Phần mềm đóng gói client server, tích hợp phần lớn quy trình quanh một CSDL toàn doanh nghiệp, lưu mỗi dữ liệu thường một lần, truy cập thời gian thực. | Sách: oleary-erp-systems-lifecycle ch01 |
| Hệ thống tài khoản chuẩn | Standard chart of accounts |  | Cấu trúc tài khoản thống nhất để giao dịch tự phân loại ngay ở cấp vận hành; nền của data consistency và consolidation. | Sách: elbardan-erp-governance-audit ch06 |
| Hồ sơ phân quyền | Authorisation profile |  | Tập quyền gắn với mỗi user, xác định được xem/sửa/xóa bản ghi nào; nền của kiểm soát phòng ngừa. | Sách: elbardan-erp-governance-audit ch06 |
| Hồ sơ yêu cầu | Requirements profile |  | Hồ sơ yêu cầu nghiệp vụ dựng ở Phase 1 (bảng hỏi + phỏng vấn); nguồn chuẩn để đánh giá mọi sản phẩm và kiểm soát demo. | Sách: parthasarathy-erp-fundamentals ch04 |
| hồ sơ yêu cầu chào thầu | RFP (Request for Proposal) |  | Tài liệu yêu cầu gửi vendor để họ đối chiếu năng lực phần mềm với nhu cầu của doanh nghiệp. | Sách: oleary-erp-systems-lifecycle ch08 |
| hợp nhất khi vận chuyển | Merge in Transit (MIT) |  | Gom hàng từ nhiều điểm xuất, hợp nhất khi đang vận chuyển thành một lô giao khách, một PO và một invoice (Dell-UPS). | Sách: oleary-erp-systems-lifecycle ch14 |
| Im lặng là đồng ý | Silence Is Approval |  | Nguyên tắc feedback: im lặng = cam kết đạt lịch; vừa biết sẽ trễ phải báo ngay (anticipated delay report). Không feedback = không closed loop. | Sách: wallace-erp-implementation ch11 |
| khai phá tri thức | Knowledge discovery |  | Khai phá quan hệ giữa các biến trong kho dữ liệu bằng thống kê/AI để tạo giá trị từ dữ liệu giao dịch. | Sách: oleary-erp-systems-lifecycle ch05 |
| Kho dữ liệu | Data Warehouse |  | Tập dữ liệu hướng chủ đề, tích hợp, biến thiên theo thời gian, không biến đổi; phục vụ phân tích off-line cho quyết định quản lý. | Sách: parthasarathy-erp-fundamentals ch08 |
| kho dữ liệu ảo | Virtual data warehouse |  | Các phần dữ liệu nằm rải ở nhiều server; chiến lược multi-server vừa giữ OLTP ổn định vừa báo cáo nhanh (Quantum: 40.000 bảng thành 4.000 business view). | Sách: oleary-erp-systems-lifecycle ch05 |
| Khung kiểm soát nội bộ COSO | COSO Internal Control–Integrated Framework |  | 5 thành phần: control environment, risk assessment, control activities, information, communication & monitoring; dùng làm khung mô tả kiểm soát cho mỗi chức năng. | Sách: elbardan-erp-governance-audit ch02 |
| khả năng thay thế | Interchangeability |  | Module ERP không thay thế lẫn nhau giữa các vendor; ít động lực để làm tương thích. | Sách: oleary-erp-systems-lifecycle ch03 |
| Khối lượng tới hạn | Critical Mass |  | Tối thiểu 80% nhân sự được đào tạo trước go-live để ERP thành 'cách chúng ta vận hành'. | Sách: wallace-erp-implementation ch07 |
| Khối lượng vs cơ cấu | Volume vs Mix |  | Volume = tốc độ/tổng lượng theo product family (địa hạt S&OP); Mix = từng sản phẩm/đơn cụ thể (địa hạt master scheduling). | Sách: wallace-erp-implementation ch08 |
| Kiểm soát bù | Compensating controls |  | Kiểm soát thứ hai phục vụ cùng mục tiêu khi kiểm soát chính hỏng; gắn ít nhất một cho mỗi vùng rủi ro. | Sách: elbardan-erp-governance-audit ch06 |
| Kiểm soát chi phí | Cost controlling |  | Phân hệ Finance: financial accounting, internal auditing, tính thuế, tham số kiểm soát chi phí, lập ngân sách, kiểm soát cash/funds flow. | Sách: parthasarathy-erp-fundamentals ch03 |
| Kiểm soát phòng ngừa vs phát hiện | Preventive vs detective controls |  | Phòng ngừa chặn vi phạm trước (SoD, authorisation, access protection); phát hiện tìm lỗi sau. ERP dịch cân bằng về phòng ngừa — ưu tiên preventive. | Sách: elbardan-erp-governance-audit ch06 |
| Kiểm soát truy cập theo vai trò | Role-Based Access Control (RBAC) |  | Hai lớp: function security (menu/chức năng) + data security (dữ liệu được xem/sửa); 'chỉ thấy thông tin liên quan công việc' để chống thông đồng. | Sách: elbardan-erp-governance-audit ch08 |
| Kiểm soát vào–ra | Input-Output Control |  | So khối lượng công việc lẽ ra hoàn thành vs thực tế hoàn thành tại work center; phải dựa trên kế hoạch năng lực từ CRP. | Sách: wallace-erp-implementation ch12 |
| kiểm soát đầu vào | Data input controls |  | Ràng buộc, kiểm tra, bắt buộc xác nhận; bắt buộc có khi nhập một lần vì hệ không còn dự phòng phát hiện lỗi. | Sách: oleary-erp-systems-lifecycle ch04 |
| Kiểm thử hộp đen | Black-box test |  | Chạy dữ liệu giả (fake data) qua hệ thống và đối chiếu kết quả để xác minh tính đúng của xử lý tự động mà không cần đọc code. | Sách: elbardan-erp-governance-audit ch09 |
| Kiểm toán liên tục | Continuous Auditing (CA) |  | Kiểm toán/báo cáo thời gian thực kiểu 'auditing by exception'; hai cách hiện thực: embedded audit module hoặc monitoring control layer. | Sách: elbardan-erp-governance-audit ch02 |
| Kiểm toán nội bộ tích hợp | Integrated internal audit |  | Gộp kiểm toán tài chính + vận hành + IT thành một kế hoạch/đội; phủ end-to-end theo vùng nghiệp vụ. | Sách: elbardan-erp-governance-audit ch11 |
| Kiểm toán viên toàn diện | Comprehensive auditor |  | Vai trò mới sau ERP: nắm mọi quy tắc, kiểm toán theo tiến trình xuyên chức năng thay vì từng chức năng rời. | Sách: elbardan-erp-governance-audit ch08 |
| Kiểm tra tự động trước khi gửi duyệt | Automatic submission check |  | Xác minh mọi trường bắt buộc đã nhập và dữ liệu nằm trong khoảng cho phép (prescribed ranges); sai thì chuyển sang approval errors window. | Sách: elbardan-erp-governance-audit ch08 |
| Kỹ thuật kiểm toán có máy tính hỗ trợ | CAAT / ACL |  | Computer-Assisted Auditing Techniques; cần để kiểm toán SoD/kiểm soát trong ERP; IB dùng ACL + audit database lưu findings/follow-up. | Sách: elbardan-erp-governance-audit ch09 |
| Logic kiểm soát | Control logic |  | Logic cài sẵn trong thiết kế ERP, định hình cách kiểm soát được thực thi; cho phép hành động này và từ chối tính chính danh của hành động khác. | Sách: elbardan-erp-governance-audit ch04 |
| luật Borda | Borda Rule |  | Luật chọn nhóm: mỗi người xếp hạng các phương án, hạng cao được nhiều điểm, cộng tổng để chọn chuẩn MAPs/vendor (Litton). | Sách: oleary-erp-systems-lifecycle ch10 |
| lý do nghiệp vụ | Business case rationale |  | Căn cứ biện minh chọn ERP, chia bốn nhóm: technology, business process, strategic, competitive; chỉ hai nhóm giữa cho tiêu chí nghiệm thu. | Sách: oleary-erp-systems-lifecycle ch07 |
| Lược đồ mã hóa | Coding scheme |  | Taxonomy 5 nhóm nhãn (áp lực quản trị, logic ERP, căn chỉnh, thay đổi IAF, chính danh) làm checklist độ phủ tài liệu; nhãn trống = nghi thiếu chức năng. | Sách: elbardan-erp-governance-audit ch12 |
| Lượng có thể hứa giao | Available-to-Promise (ATP) |  | Phần tồn kho và/hoặc sản xuất tương lai chưa cam kết, tính từ master schedule; cơ sở để hứa ngày giao đơn khách. | Sách: wallace-erp-implementation ch17 |
| Lập lịch chủ đạo | Master Scheduling |  | Làm việc ở mức MIX (sản phẩm/đơn cụ thể), 'bao nhiêu' và 'khi nào' theo tuần; tổng phải reconcile với S&OP cùng kỳ. | Sách: wallace-erp-implementation ch17 |
| Lập lịch hữu hạn | Finite Scheduling |  | Kết hợp lập lịch chi tiết và hoạch định năng lực thành một công cụ mô phỏng; nên để Phase III, chỉ hữu ích khi due date đã hợp lệ. | Sách: wallace-erp-implementation ch12 |
| Lập lịch lùi | Back Scheduling |  | Lập lịch từng nguyên công trong job shop từ ngày hoàn thành ngược về, gom theo work center, truyền xuống xưởng qua dispatch list. | Sách: wallace-erp-implementation ch18 |
| Lập lịch nhà cung cấp | Supplier Scheduling |  | Thay purchase requisition + hard-copy PO bằng lịch giao hằng tuần sinh từ MRP trên hợp đồng dài hạn; mục tiêu LOẠI BỎ requisition/PO, không tự động hóa chúng. | Sách: wallace-erp-implementation ch12 |
| Lắp ráp theo đơn | Assemble-to-Order |  | Dự trữ sẵn linh kiện theo dự báo, nhận đơn mới mới lắp ráp/hoàn thiện theo đặc tả khách. | Sách: parthasarathy-erp-fundamentals ch02 |
| Lệch chuẩn & lách hệ thống | Misalignment & workaround |  | Lệch giữa chức năng ERP và cách làm hiện hữu; nếu bỏ lửng, người dùng 'lách' bằng giải pháp ngoài hệ thống và phá vỡ kiểm soát. | Sách: elbardan-erp-governance-audit ch07 |
| Lịch sản xuất tổng thể | Master Production Schedule (MPS) |  | Kế hoạch time-phased quy định lượng từng thành phẩm cần sản xuất mỗi kỳ; phải khả thi trong năng lực sẵn có. | Sách: parthasarathy-erp-fundamentals ch02 |
| Lộ trình đã kiểm chứng | The Proven Path |  | Bộ bước triển khai đã chứng minh qua hàng nghìn công ty; đi đủ, không skip bước thì gần như chắc đạt Class A/B. | Sách: wallace-erp-implementation ch02 |
| ma trận rủi ro | Risk Matrix |  | Khung nhận diện rủi ro ERP hai chiều: giai đoạn vòng đời nhân loại rủi ro (technical/business/organizational); mỗi rủi ro có mặt success và failure. | Sách: oleary-erp-systems-lifecycle ch15 |
| MAPs dùng chung toàn cục | Common / global MAPs |  | Mô hình/chứng từ/quy trình dùng chung cho mọi đơn vị thay vì mỗi đơn vị tự chọn; tỷ lệ local tự cấu hình thường chỉ ~1%. | Sách: oleary-erp-systems-lifecycle ch10 |
| Minh bạch & hiển thị | Transparency & visibility |  | Khả nhìn toàn giao dịch; audit trail ai/khi nào/tại sao; không giấu hoặc thao túng được. | Sách: elbardan-erp-governance-audit ch06 |
| MRP vòng kín | Closed-Loop MRP |  | Bước tiến hoá thứ hai của ERP: thêm hoạch định năng lực và vòng phản hồi (feedback) từ thực thi về hoạch định. | Sách: wallace-erp-implementation ch01 |
| mySAP ERP | mySAP ERP |  | Bộ ERP của SAP gồm 4 giải pháp: Financials, Human Capital Management (HCM), Operations, Corporate Services. | Sách: parthasarathy-erp-fundamentals ch10 |
| màn hình trên giao dịch | Screens-to-Transactions |  | Mô hình độ khó triển khai = tỉ lệ số màn hình ERP/legacy nhân khối lượng giao dịch; cũng đo độ fit giữa quy trình và phần mềm. | Sách: oleary-erp-systems-lifecycle ch04 |
| Mã được quản lý | Managed code |  | Mã do .NET quản lý: nhẹ, nhanh, bảo mật, chạy song song nhiều phiên bản không xung đột, TCO thấp. | Sách: parthasarathy-erp-fundamentals ch09 |
| Mô hình 3 phase | Three-Phase Approach |  | Phase I Basic ERP → Phase II Supply Chain Integration → Phase III Extensions; các phase tuần tự, trong mỗi phase chạy nhiều task song song. | Sách: wallace-erp-implementation ch03 |
| mô hình, chứng từ, quy trình | MAPs (Models, Artifacts, Processes) |  | Khung ba thành phần tạo nên một hệ ERP được cấu hình: mô hình tổ chức/dữ liệu kèm giả định, chứng từ & danh mục, và quy trình liên chức năng. | Sách: oleary-erp-systems-lifecycle ch03, ch10 |
| Mốc/vùng thời gian | Time Fences / Time Zones |  | Trong master scheduling policy: quy định ai được phép đổi lịch ở vùng thời gian nào. | Sách: wallace-erp-implementation ch09 |
| Ngôn ngữ mô hình hóa thống nhất | Unified Modeling Language (UML) |  | Ký pháp chuẩn cho hệ hướng đối tượng; đóng vai trò giao diện chung giữa business analyst và system analyst. | Sách: parthasarathy-erp-fundamentals ch12 |
| Người cầm đuốc | Torchbearer |  | Champion/sponsor cấp cao chịu trách nhiệm tối cao cho ERP, chủ trì steering committee; lý tưởng là General Manager. | Sách: wallace-erp-implementation ch06 |
| người dùng nòng cốt | Super users |  | Thành viên tổ chức khách được đào tạo trước để huấn luyện lại người khác, tạo buy-in và lan tỏa hiểu biết. | Sách: oleary-erp-systems-lifecycle ch13 |
| Người lập–người kiểm | Maker-checker |  | Mỗi màn hình được 2 người xử lý; không đi tiếp đến khi có approval + validation; ERP mặc định có thể thiếu nên phải customise. | Sách: elbardan-erp-governance-audit ch08 |
| Người triển khai = người vận hành | IMPLEMENTERS = USERS |  | Người triển khai từng công cụ ERP phải chính là người sẽ vận hành nó; không khoán cho người ngoài. | Sách: wallace-erp-implementation ch02 |
| Nhu cầu phụ thuộc/độc lập | Dependent vs Independent demand |  | Linh kiện là dependent demand (tính từ BOM, không dự báo); thành phẩm là independent demand (dự báo) — mấu chốt của MRP. | Sách: parthasarathy-erp-fundamentals ch02 |
| nhượng bộ triển khai | Implementation compromise |  | Sai lệch so với kế hoạch để tiết kiệm thời gian/tiền (làm sau); nguy hiểm nếu cắt đúng phần cốt lõi thành engagement compromise. | Sách: oleary-erp-systems-lifecycle ch12 |
| Nhất quán dữ liệu | Data consistency |  | Cùng một định dạng dữ liệu cho mọi đơn vị; hợp nhất dễ, loại trùng lặp và dư thừa. | Sách: elbardan-erp-governance-audit ch06 |
| Nhập liệu một điểm | Single data entry point |  | Dữ liệu nhập một lần, mọi xử lý sau tự động và tự lan sang module liên quan; nghiệp vụ phi tài chính tự sinh bút toán. | Sách: elbardan-erp-governance-audit ch07 |
| nhập một lần | Gather data once |  | Nhập dữ liệu một lần tại điểm phát sinh; chi phí thấp, nhất quán, nhưng sai một chỗ sai toàn hệ nên bắt buộc input controls. | Sách: oleary-erp-systems-lifecycle ch04 |
| Năm chính sách nền | Five Bedrock Policies |  | S&OP, demand management, master scheduling, material planning, engineering change; mỗi policy nêu roles, parameters, feedback, performance measurements; GM ký. | Sách: wallace-erp-implementation ch09 |
| năm vendor ERP lớn | BOPSE |  | Năm nhà cung cấp ERP chính: BAAN, Oracle, PeopleSoft, SAP, J.D. Edwards. | Sách: oleary-erp-systems-lifecycle ch03 |
| Phân tích ABC | ABC (Always Better Control) analysis |  | Phân loại mặt hàng tồn kho để kiểm soát khác nhau theo mức quan trọng; kèm duy trì stock level và inventory ratios. | Sách: parthasarathy-erp-fundamentals ch03 |
| Phân tích chi phí-lợi ích | Cost Benefit Analysis |  | Analysis để quyết định có triển khai hay không; bất lợi thì dừng dự án — không phải justification để biện minh. | Sách: parthasarathy-erp-fundamentals ch04 |
| phân tích khoảng cách | Gap analysis |  | So sánh as is với to be để tìm khoảng cách và các modification cần thiết cùng chi phí thực ngoài tiền phần mềm. | Sách: oleary-erp-systems-lifecycle ch08 |
| Phân tích khoảng trống | Gap Analysis |  | Tìm gap giữa quy trình hiện tại và chức năng gói; lấp bằng sản phẩm bên thứ ba, chương trình tùy biến, hoặc sửa source ERP. | Sách: parthasarathy-erp-fundamentals ch05 |
| Phân tích ngang vs dọc | Horizontal vs vertical analysis |  | Ngang bám tiến trình end-to-end xuyên tổ chức (ưu tiên); dọc theo từng địa điểm/cụm kiểm soát. | Sách: elbardan-erp-governance-audit ch11 |
| Phân tích nội dung có định hướng | Directed content analysis |  | Mã hóa bắt đầu từ template/checklist chuẩn ERP rồi cho yêu cầu mới nổi lên từ dữ liệu; áp vào elicitation để vừa chống hallucinate vừa không bỏ sót. | Sách: elbardan-erp-governance-audit ch05 |
| phân tích yêu cầu | Requirements analysis |  | Rà soát yêu cầu đối với MAPs, phân loại theo mức quan trọng, tổng hợp thành RFP gửi vendor để so khớp. | Sách: oleary-erp-systems-lifecycle ch08 |
| Phép thử chặn giao hàng | Shipment Stopper Test |  | Tiêu chí completeness của BOM: item nào thiếu sẽ chặn giao hàng thì phải có trước go-live; hàng tiêu chuẩn mua ngoài thêm sau. | Sách: wallace-erp-implementation ch10 |
| Phương trình sản xuất phổ quát | Universal Manufacturing Equation |  | 4 câu hỏi nền: Sẽ làm gì? Cần gì để làm? Đang có gì? Phải mua/làm thêm gì? — tương ứng master schedule, BOM, inventory records, nhu cầu. | Sách: wallace-erp-implementation ch01 |
| Phần mềm báo cáo tương tác | Business Objects |  | Lớp báo cáo kéo-thả giữa CSDL và người dùng cuối, truy xuất dữ liệu không cần biết cấu trúc database. | Sách: elbardan-erp-governance-audit ch08 |
| phần mềm cũ | Legacy software |  | Phần mềm tự phát triển riêng cho doanh nghiệp, chi phí bảo trì cao, khó tích hợp. | Sách: oleary-erp-systems-lifecycle ch02 |
| Phần mềm cắm thêm | Bolt-on |  | Phần mềm ngoài ES chính, thường 'best of breed'; 3 loại (resource-planning enabler / front-back-end / APS); đánh đổi: giảm tích hợp, tăng bảo trì. | Sách: wallace-erp-implementation ch04 |
| Phần mềm doanh nghiệp | Enterprise System / Enterprise Software (ES) |  | Gói phần mềm giao dịch toàn doanh nghiệp quanh một central database; là 'phần mềm' mà người ta hay nhầm là ERP; thuộc C-item. | Sách: wallace-erp-implementation ch01 |
| phần mềm đóng gói | Package software |  | Phần mềm dựng cho nhiều tổ chức dùng chung; chọn năng lực bằng tham số thay vì lập trình lại, đồng nghĩa mua luôn tầm nhìn của vendor. | Sách: oleary-erp-systems-lifecycle ch02 |
| Quy trình công nghệ / lộ trình gia công | Routing |  | Trình tự nguyên công + work center + thời gian để làm một item; đầu vào của CRP; job shop cần chi tiết, flow shop có thể suy từ layout. | Sách: wallace-erp-implementation ch17 |
| Quyết định Đi/Không | Go/No-Go Decision |  | 'Moment of truth' cuối giai đoạn chuẩn bị; dùng 4 câu hỏi sẵn sàng của Jerry Clement (financial/resource/priority/emotional) — một 'no' là dừng. | Sách: wallace-erp-implementation ch05 |
| Quản lý cấu hình phần mềm | Software Configuration Management (SCM) |  | Quản lý quá trình thay đổi VÀ mọi artifact của hệ thống đang tiến hóa; trùng viết tắt nhưng KHÁC Supply Chain Management. | Sách: parthasarathy-erp-fundamentals ch05 |
| Quản lý nhu cầu | Demand Management |  | Gồm Forecasting/Sales Planning và Customer Order Entry & Promising; một trong năm bedrock policies. | Sách: wallace-erp-implementation ch17 |
| Quản lý vật tư | Materials Management (MM) |  | 'Central point of logistics': Inventory, MRP, Purchasing, Warehouse, Vendor evaluation, Invoice verification, Product costing. | Sách: parthasarathy-erp-fundamentals ch03 |
| Quản trị quan hệ khách hàng | Customer Relationship Management (CRM) |  | Front-office mở rộng của ERP: nhận diện, thu hút và giữ chân khách sinh lời, tối đa hóa vòng đời và lợi nhuận từ họ. | Sách: parthasarathy-erp-fundamentals ch08 |
| Quản trị thay đổi | Change management |  | Kế hoạch thích nghi tổ chức + đào tạo thật trước go-live; thiếu nó là nguyên nhân chính của workaround và thất bại thích nghi. | Sách: elbardan-erp-governance-audit ch08 |
| Ràng buộc xử lý | Processing constraints |  | Chặn user thêm/sửa/xóa/hủy dữ liệu vượt quá các điểm kiểm soát nhất định. | Sách: elbardan-erp-governance-audit ch08 |
| rủi ro tổ chức | Organizational risk |  | Rủi ro từ con người, cơ cấu, văn hóa; mức cao nhất trong ba loại (organizational lớn hơn business lớn hơn technical). | Sách: oleary-erp-systems-lifecycle ch15 |
| SAP R/3 | SAP R/3 |  | ERP client/server ba tầng đầu tiên ra thị trường (1993), đưa SAP lên vị trí số một; R/2 dành cho mainframe. | Sách: parthasarathy-erp-fundamentals ch10 |
| Soát chéo / tự soát | Peer-review / self-review controls |  | Kiểm soát nảy sinh do dữ liệu tích hợp + một điểm nhập liệu; mỗi đơn vị tự chịu trách nhiệm sửa lỗi, checker ngăn lỗi lan toàn tổ chức. | Sách: elbardan-erp-governance-audit ch08 |
| Sáu pha di trú (META Group) | META Group six migration phases |  | Analysis → Definition → Coordination → Transition → Ongoing management → Change Management; khung di trú ERP sang nền tảng mới, ~7 tháng. | Sách: parthasarathy-erp-fundamentals ch06 |
| Sơ đồ hoạt động theo vai trò | Role Activity Diagram (Swimlanes) |  | Activity diagram chia hoạt động vào các cột swimlanes theo vai trò, trả lời rõ 'ai chịu trách nhiệm việc gì'. | Sách: parthasarathy-erp-fundamentals ch12 |
| Sản xuất theo ô/tế bào | Cellular Manufacturing |  | Chuyển job shop sang flow bằng cách chuyên dụng hóa thiết bị và xếp liền kề theo dòng (flow lines, demand-pull lines, kanban lines). | Sách: wallace-erp-implementation ch18 |
| Sổ tay chức năng/nghiệp vụ | FIM / BIM |  | Function Instruction Manual và Business Instructions Manual: nguồn sự thật về 'điều phải được thực thi'; kiểm toán đảm bảo chúng được thực thi, không quyết định cách làm. | Sách: elbardan-erp-governance-audit ch09 |
| sự kiện kích hoạt | Event triggers |  | Các sự kiện trong SAP xác định khi nào thu thập dữ liệu (bán hàng, nhận hàng từ PO, giữ vật tư, xuất hàng, điều chuyển kho). | Sách: oleary-erp-systems-lifecycle ch04 |
| Tam giác đạc | Triangulation |  | Kiểm chứng một dữ kiện qua ≥2 nguồn/phương pháp/người để tăng độ tin cậy và giảm thiên lệch trước khi đưa vào tài liệu. | Sách: elbardan-erp-governance-audit ch05 |
| test kiểm chứng hệ thống | Systems Validation Test (SVT) |  | Test diện rộng với khoảng 100 user nhập khối lượng giao dịch lớn, mô phỏng tải tương lai và test cả phần cứng, interdependency giữa module. | Sách: oleary-erp-systems-lifecycle ch11 |
| Thay đổi hành vi | Behavior Change |  | Mục tiêu tối thượng của giáo dục ERP: người ta đổi cách làm vì tin vào formal system, không chỉ nắm dữ kiện (fact transfer). | Sách: wallace-erp-implementation ch07 |
| Thiết kế theo đơn | Engineer-to-Order (ETO) |  | Sản phẩm phát triển theo đơn thiết kế riêng từng khách; cần nhiều thời gian để vendor hiểu yêu cầu và chuyển đổi dữ liệu BOM lớn. | Sách: parthasarathy-erp-fundamentals ch11 |
| thiết lập tham số | Switch setting |  | Công tắc phần mềm để bật/tắt và chọn giữa các năng lực của gói mà không lập trình lại (parameterization); ưu tiên trước khi tùy biến mã. | Sách: oleary-erp-systems-lifecycle ch02 |
| thông lệ tốt nhất | Best practices |  | Cách làm quy trình được coi là tốt nhất, nhúng sẵn trong ERP dưới dạng các lựa chọn phải quyết khi triển khai (SAP R/3 có hơn 1.000). | Sách: oleary-erp-systems-lifecycle ch01 |
| Thẻ kanban / cơ chế kéo | Kanban |  | Tín hiệu kéo (pull) bổ sung, dùng để liên kết thiết bị thành dòng và điều độ theo nhu cầu, thay cho back scheduling. | Sách: wallace-erp-implementation ch14 |
| thẻ điểm cân bằng | Balanced Scorecard |  | Khung đánh giá 4 góc nhìn của Kaplan & Norton (financial, customer, learning & growth, internal process), ánh xạ sang 4 rationale của ERP. | Sách: oleary-erp-systems-lifecycle ch12 |
| Thời gian chu trình | Cycle time |  | Thời gian từ nhận đơn đến giao sản phẩm; ERP rút ngắn nhiều nhất với make-to-order. | Sách: parthasarathy-erp-fundamentals ch01 |
| Thứ tự ưu tiên triển khai | ABCs of Implementation |  | Ưu tiên theo Pareto: A=People (quan trọng nhất), B=Data, C=Computer (ít nhất); buộc cắt ngân sách thì cắt C trước, giữ A. | Sách: wallace-erp-implementation ch01 |
| Tiêu chí dữ liệu CAVAIR | CAVAIR |  | Complete, Accurate, Valid, Restricted Access: bộ tiêu chí kiểm toán viên dùng để nghiệm thu dữ liệu; biến thành ràng buộc validation code-able. | Sách: elbardan-erp-governance-audit ch09 |
| trao đổi dữ liệu điện tử | EDI (Electronic Data Interchange) |  | Trao đổi chunk chuẩn (invoice) định dạng chuẩn qua VAN; dùng cho khối lượng lớn/đối tác lớn; bền nhưng cứng và đắt. | Sách: oleary-erp-systems-lifecycle ch14 |
| triển khai một lần | Big Bang |  | Bật toàn bộ bộ module tại mọi địa điểm gần như cùng lúc trong vài ngày, sau một đợt test lớn; không cần temporary interface. | Sách: oleary-erp-systems-lifecycle ch11 |
| Triển khai một lần toàn bộ | Big Bang approach |  | Đưa mọi module liên quan vào vận hành cùng lúc; đạt lợi ích đầy đủ nhưng rủi ro cao khi hệ mới trục trặc. | Sách: parthasarathy-erp-fundamentals ch05 |
| triển khai theo giai đoạn | Phased implementation |  | Triển khai tuần tự từng module/nhóm module, thường từng địa điểm; cần temporary interface tới legacy ở mỗi pha. | Sách: oleary-erp-systems-lifecycle ch11 |
| triển khai theo đợt sóng | Waved |  | Triển khai nhiều đợt sóng, mỗi sóng trao functionality cho một business unit/vùng; nằm giữa big bang và phased (Tektronix). | Sách: oleary-erp-systems-lifecycle ch11 |
| Trung tâm công việc | Work Center |  | Nơi thực hiện nguyên công (một máy/nhóm máy/trạm); đơn vị gom tải của CRP và input-output control. | Sách: wallace-erp-implementation ch17 |
| Trưởng dự án | Project Leader |  | Toàn thời gian, nội bộ, nền vận hành, heavyweight, veteran, giỏi giao tiếp; chủ trì project team và gỡ vật cản cho người thực thi. | Sách: wallace-erp-implementation ch06 |
| Tuyên bố tầm nhìn | Vision Statement |  | Văn bản ~1 trang mô tả công ty sẽ ra sao sau ERP, viết sao cho đo lường được; neo chống lệch phạm vi. | Sách: wallace-erp-implementation ch05 |
| tài liệu theo kịch bản | Script-based materials |  | Tài liệu dẫn user từng bước qua trọn một giao dịch, đặt trên mạng nội bộ; context-based, kiêm tài liệu hệ thống và FAQ. | Sách: oleary-erp-systems-lifecycle ch13 |
| Tác nhân nghiệp vụ / vai trò nội bộ | Business actor vs Business worker |  | Business actor là người/vật bên ngoài tương tác với doanh nghiệp; business worker là vai trò bên trong thao tác các business entity. | Sách: parthasarathy-erp-fundamentals ch12 |
| Tách rời hình thức khỏi thực chất | Decoupling / ceremonial compliance |  | Giữ vỏ tuân thủ (một kiểm toán viên biểu tượng, ủy ban 'không kích hoạt') mà bỏ chức năng thật — dấu hiệu chính danh đã mất. | Sách: elbardan-erp-governance-audit ch07 |
| tái cấu trúc dựa trên công nghệ | Technology enabled reengineering |  | Chọn ERP/công nghệ trước rồi thiết kế quy trình trong giới hạn phần mềm; nhanh, rẻ, khả thi nhưng bị ràng buộc. | Sách: oleary-erp-systems-lifecycle ch06 |
| tái cấu trúc lớn | Big-R Reengineering |  | Thay đổi mạnh cả quy trình tổ chức lẫn phần mềm ERP; tốn nhiều nguồn lực, rủi ro cao (Boeing-BAAN). | Sách: oleary-erp-systems-lifecycle ch09 |
| tái cấu trúc nhỏ | Small-r Reengineering |  | Thay đổi tối thiểu cả tổ chức lẫn phần mềm; tổ chức thích nghi với phần mềm khớp sẵn, nhanh và rẻ (Microsoft SAP). | Sách: oleary-erp-systems-lifecycle ch09 |
| Tái cấu trúc quy trình nghiệp vụ | Business Process Reengineering (BPR) |  | Theo Michael Hammer: tư duy lại nền tảng và tái thiết kế triệt để các quy trình để cải thiện đột phá về cost/quality/service/speed. | Sách: parthasarathy-erp-fundamentals ch05 |
| tái cấu trúc từ đầu | Clean slate reengineering |  | Thiết kế quy trình tối ưu không bị ràng buộc rồi mới fit phần mềm; độc nhất nhưng tốn kém và rủi ro bất khả thi. | Sách: oleary-erp-systems-lifecycle ch06 |
| Tái thiết kế vs tùy biến | Reengineering vs Customisation |  | Tái thiết kế quy trình về chuẩn ERP (ưu tiên, cho auditable) hay tùy biến giữ quy trình cũ (chỉ khi do luật địa phương); quyết định này quyết định tính kiểm toán được. | Sách: elbardan-erp-governance-audit ch06 |
| Tích hợp | Integration |  | Một CSDL, nhập một nơi tự chảy đi nơi khác, giảm đối soát thủ công, làm hành động mỗi người hữu hình. | Sách: elbardan-erp-governance-audit ch06 |
| Tích hợp / tự động cập nhật dữ liệu | Integration (automatic data updation) |  | Ưu điểm số một của ERP: một giao dịch tự động cập nhật mọi nghiệp vụ liên quan; đặc trưng nhận diện ERP so với phần mềm rời rạc. | Sách: parthasarathy-erp-fundamentals ch01 |
| Tùy biến | Customization |  | Điều chỉnh phần mềm cho khớp tổ chức, cân 3 tham số (end-user/technical/vision lãnh đạo); không sửa base; customize cao thì lợi ích ERP thấp. | Sách: parthasarathy-erp-fundamentals ch05 |
| Tư vấn nghiệp vụ / kỹ thuật | Functional vs Technical consultant |  | Functional consultant xem xét business process của tổ chức; technical consultant xử lý lỗi kỹ thuật; solution architect phối hợp cả hai. | Sách: parthasarathy-erp-fundamentals ch04 |
| Tập trung | Centralisation |  | Module tài chính là 'pool' trung tâm nhận mọi giao dịch; một CSDL dùng chung cho mọi nhu cầu. | Sách: elbardan-erp-governance-audit ch07 |
| tối ưu Pareto | Pareto Optimality |  | Chọn phương án mà không phương án nào khác làm một division hài lòng hơn mà không làm division khác kém đi. | Sách: oleary-erp-systems-lifecycle ch10 |
| tồn kho do nhà cung cấp quản | Vendor-Managed Inventories (VMI) |  | Chuyển việc đặt hàng từ khách sang nhà cung cấp (P&G giữ hàng trên kệ); tích hợp ERP-to-ERP cần chung một phần MAPs. | Sách: oleary-erp-systems-lifecycle ch14 |
| Tổ công tác tách nhánh | Spin-Off Task Force |  | Tổ tạm thời, liên phòng ban, có thời hạn, giải quyết một vấn đề cụ thể rồi đề xuất cho project team và giải tán. | Sách: wallace-erp-implementation ch06 |
| Tổng chi phí sở hữu | Total Cost of Ownership (TCO) |  | OS 'miễn phí' như Linux đôi khi có TCO cao hơn kỳ vọng do chi phí quản trị và khan hiếm nhân lực vận hành. | Sách: parthasarathy-erp-fundamentals ch06 |
| Tự động hóa | Automation |  | Giả định kiểm soát: hệ thống tự kiểm tính hợp lệ, tự dò xung đột SoD, tự sinh audit trail. | Sách: elbardan-erp-governance-audit ch06 |
| Vòng quay tồn kho | Inventory turns |  | Số vòng quay tồn kho mỗi năm; KPI điển hình, nhiều case tăng từ ~2 lên 6 lần/năm sau khi triển khai ERP. | Sách: parthasarathy-erp-fundamentals ch11 |
| Xác thực hai yếu tố | Two-factor authentication |  | Kết hợp với kiểm soát hai vai trò (two role controls) cho giao dịch rủi ro cao. | Sách: elbardan-erp-governance-audit ch09 |
| Xưởng theo chức năng | Job Shop |  | Nhóm nguồn lực theo loại giống nhau (functional); công việc di chuyển theo routing riêng, cần back scheduling + dispatch list + CRP + input-output. | Sách: wallace-erp-implementation ch18 |
| Xưởng theo dòng | Flow Shop |  | Nhóm nguồn lực theo trình tự quy trình (process layout); FIFO, nhanh, lịch đơn giản từ MS/MRP, thường không cần routing chính thức. | Sách: wallace-erp-implementation ch18 |
| Yếu tố thành công then chốt | Critical Success Factors (CSF) |  | Vấn đề lãnh đạo phải giải quyết: trạng thái legacy, quy trình rõ, cam kết lãnh đạo, nguồn lực, lịch & change management. | Sách: parthasarathy-erp-fundamentals ch05 |
| Đa phương thức kiểm soát | Multiple methods of control |  | Nhiều kiểm soát cho một đối tượng từ nhiều góc (một người nhập, một người duyệt, một người xác nhận) — mỗi bút toán soát 1–3 lần. | Sách: elbardan-erp-governance-audit ch07 |
| Điểm gặp khách hàng | Customer Meeting Point |  | Chiến lược đáp ứng: design-to-order / make-to-order / finish-to-order / make-to-stock; quyết định cách promising và thiết kế quy trình. | Sách: wallace-erp-implementation ch09 |
| Đơn hàng bất thường | Abnormal Sales Order |  | Đơn tăng đột biến vượt dự báo (hoặc từ khách quan trọng); được ưu tiên hơn đơn đã lên kế hoạch và đã chốt. | Sách: parthasarathy-erp-fundamentals ch03 |
| Đưa kiểm toán vào từ sớm | Early IAF involvement |  | Kiểm soát/kiểm toán tham gia từ giai đoạn requirements: chọn module/vendor, user management, verify data migration, làm super users; yếu tố quyết định thành công. | Sách: elbardan-erp-governance-audit ch09 |
| Đếm xoay vòng | Cycle Counting |  | Đếm tồn kho liên tục (ongoing) thay kiểm kê năm; control group ~100 item/tuần; mục tiêu: tìm & loại nguyên nhân lỗi, đo %, sửa bản ghi, bỏ kiểm kê năm. | Sách: wallace-erp-implementation ch10 |
| Định mức vật tư | Bill of Material (BOM) |  | Danh sách component tạo nên sản phẩm; đầu vào bắt buộc của MRP; cần ≥98% chính xác, hợp nhất (integrated), modular cho sản phẩm nhiều option. | Sách: wallace-erp-implementation ch10 |
| độ khớp module | Module fit |  | Mức khớp giữa module và yêu cầu (Siemens: finance ~100%, module khác 70-80% nên cần modification). | Sách: oleary-erp-systems-lifecycle ch11 |
| độ mịn yêu cầu | Requirements granularity |  | Một yêu cầu có thể là cả một bộ best practice hoặc chỉ một trường dữ liệu; bỏ qua sẽ đếm sai khi so khớp vendor. | Sách: oleary-erp-systems-lifecycle ch08 |
| Ủy ban chỉ đạo cấp cao | Executive Steering Committee |  | GM + các phó chủ tịch + project leader; nhóm duy nhất đảm bảo được thành công và duy nhất có quyền cho phép lùi lịch dự án. | Sách: wallace-erp-implementation ch06 |
| Ủy ban vận hành ERP | ERP Operating Committee |  | Project team sau go-live: gần 100% trưởng bộ phận, họp ~quý, ghế chủ tịch luân phiên; nhiệm vụ đo hiệu suất và cải tiến, chống tụt hạng. | Sách: wallace-erp-implementation ch15 |
