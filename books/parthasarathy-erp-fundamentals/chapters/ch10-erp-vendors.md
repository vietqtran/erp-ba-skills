# Chương 10: Các nhà cung cấp ERP (ERP Vendors)

## Ý tưởng cốt lõi (Core Idea)
Thị trường ERP có một "ông lớn" áp đảo (**SAP**), một nhóm vendor lớn và rất nhiều vendor nhỏ. Các vendor khác biệt nhau theo thị trường dọc (vertical), nền tảng (AS/400, Unix, Windows NT) và chiều sâu/rộng chức năng. ERP đã tiến hóa từ "công nghệ tân tiến" thành "thực hành đã được thể chế hóa" (institutionalized component of enterprise infrastructure).

## Framework được giới thiệu (Frameworks Introduced)
- **mySAP ERP — four individual solutions** — bốn giải pháp cấu thành của SAP.
  - **mySAP ERP Financials**: kế toán, báo cáo tài chính, quản trị hiệu năng, quản trị doanh nghiệp (corporate governance), treasury, kiểm soát nội bộ.
  - **mySAP ERP Human Capital Management (HCM)**: quản trị vốn con người, payroll cho 50+ quốc gia, vòng đời nhân viên.
  - **mySAP ERP Operations**: mua sắm & logistics, phát triển sản phẩm & sản xuất, bán hàng & dịch vụ, phân tích.
  - **mySAP ERP Corporate Services**: bất động sản, quản lý dự án & danh mục, công tác phí, EH&S, quản lý chất lượng.
- **Vendor-to-specialization mapping** — ánh xạ vendor theo thế mạnh/nền tảng (xem Bảng tham chiếu): tiêu chí chọn vendor cốt lõi là *lĩnh vực chuyên môn hóa* của vendor.

## Khái niệm chính (Key Concepts)
- **SAP R/2 vs R/3**: R/2 cho môi trường mainframe; **R/3** là ERP client/server ba tầng đầu tiên ra thị trường (1993), đưa SAP lên số một.
- **Best practices / business templates**: SAP cung cấp template theo thị trường dọc để R/3 dễ thích ứng.
- **Configurable Network Computing (CNC)**: triết lý "One World" của J.D. Edwards cho phép chạy đa nền tảng.
- **Object-oriented ERP**: BPCS 6.0 (SSA), On/Q (QAD), MFG/NT (QAD) dùng công nghệ hướng đối tượng.
- **Open source ERP**: Compiere mang chức năng "Fortune 500" tới SME, miễn phí theo định nghĩa.

## Mô hình tư duy (Mental Models)
- Chọn vendor theo "độ phù hợp thị trường dọc" của bạn: nhiều vendor mạnh ở ngành cụ thể (ô tô, thực phẩm & đồ uống, dược/y tế, giấy...) hơn là mạnh toàn diện.
- "Ít tùy biến hơn = tốt hơn": sản phẩm càng ít phải tùy biến thì người dùng càng hưởng trọn lợi ích và triển khai càng nhanh/rẻ.
- Nhìn bức tranh thị phần: một actor áp đảo + vài vendor lớn + rất nhiều vendor không đáng kể.

## Điều cần tránh (Anti-patterns)
- **Đánh đồng mọi vendor**: mỗi vendor có thế mạnh nền tảng và ngành khác nhau; xếp hạng điểm mạnh/yếu trước khi chọn.
- **Bỏ qua lộ trình nâng cấp của vendor**: chọn vendor không hợp với kế hoạch tương lai (PLM, CRM) dẫn tới mắc kẹt.

## Bảng tham chiếu (Reference Tables)
Top-5 thị phần doanh thu license ERP toàn cầu (Nguồn: IJEIS, trong sách):

| Vendor | 2002 | 2001 |
|---|---|---|
| **SAP AG** | 25.1% | 24.7% |
| **ORACLE** | 7.0% | 7.9% |
| **PEOPLESOFT** | 6.5% | 7.6% |
| **SAGE** | 5.4% | 4.6% |
| **MICROSOFT BUSINESS SOLUTIONS** | 4.9% | 4.6% |
| OTHERS | 51.1% | 50.3% |

Thế mạnh/nền tảng một số vendor:

| Vendor | Sản phẩm | Thế mạnh / nền tảng |
|---|---|---|
| SAP | R/3, mySAP ERP | Dẫn đầu, tích hợp toàn diện |
| Oracle | 35+ modules | Rộng & sâu, Windows NT |
| J.D. Edwards | OneWorld | CNC, đa nền tảng |
| Baan | Baan IV | Mạnh sản xuất hơn tài chính |
| SSA | BPCS 6.0 | Hướng đối tượng, AS/400 |
| QAD | MFG/PRO, MFG/NT | Mixed-mode, 5 ngành dọc |
| Intuitive | Intuitive ERP | SME, 100% Microsoft .NET |
| Compiere | Compiere | Open source, SME |
| Ramco | VirtualWorks | Ấn Độ, Unique & Next Practices |

## Ví dụ minh họa (Worked Example)
**mySAP ERP** minh họa cách một bộ ERP đầu ngành được cấu trúc: không phải một khối đơn, mà là bốn giải pháp theo vùng chức năng (Financials, HCM, Operations, Corporate Services) trên nền tảng công nghệ mở, tích hợp được cả hệ SAP lẫn non-SAP. HCM hỗ trợ payroll và quy định pháp lý cho hơn 50 quốc gia, được hơn 9.000 công ty dùng để quản lý 54 triệu nhân viên — cho thấy chiều sâu "industry-specific features + best practices" tích lũy ba thập kỷ. Thông điệp cho người chọn ERP: đánh giá vendor theo chiều sâu chức năng theo ngành + độ phủ địa phương (ngôn ngữ, tiền tệ, luật thuế), không chỉ theo tên tuổi.

## Điểm cần nhớ (Key Takeaways)
1. SAP dẫn đầu thị trường (R/3 ba tầng, mySAP ERP bốn giải pháp); Oracle, PeopleSoft, Sage, Microsoft theo sau.
2. Vendor khác nhau theo ngành dọc và nền tảng — chọn theo độ phù hợp, không theo danh tiếng.
3. Tiêu chí số một khi chọn vendor: lĩnh vực chuyên môn hóa của vendor so với ngành của bạn.
4. Ưu tiên giải pháp cần ít tùy biến nhất để giảm chi phí và rút ngắn triển khai.
5. ERP đã thành hạ tầng tiêu chuẩn của doanh nghiệp, mở rộng bằng công nghệ e-business.

## Ứng dụng cho BA ERP (BA Application)
- Khi lập tài liệu so sánh/lựa chọn vendor, xây ma trận vendor × tiêu chí (ngành dọc, nền tảng, chiều sâu chức năng, mức tùy biến, lộ trình nâng cấp) thay vì mô tả định tính.
- Tham chiếu cấu trúc bốn giải pháp của mySAP ERP (Financials/HCM/Operations/Corporate Services) như bản đồ phạm vi để đảm bảo spec phủ đủ các vùng chức năng chuẩn.
- Đưa yêu cầu địa phương hóa (ngôn ngữ, tiền tệ, thuế/excise) thành tiêu chí tường minh — như case ETO của SAP ở Ch11.
- Ưu tiên "least customization" trong tiêu chí nghiệm thu lựa chọn: đo tỷ lệ chức năng đáp ứng "out of the box".

## Liên hệ (Connects To)
- **Ch 4 (ERP Software Selection)**: tiêu chí & quy trình chọn vendor/gói.
- **Ch 9 (ERP và .NET)**: Intuitive ERP (vendor .NET) được mô tả chi tiết.
- **Ch 11 (Case Studies)**: phần lớn case dùng Intuitive ERP; hai case lớn dùng SAP R/3.
