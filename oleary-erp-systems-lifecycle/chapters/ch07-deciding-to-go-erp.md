# Chương 7: Quyết định triển khai ERP (Deciding to Go ERP)

## Ý tưởng cốt lõi (Core Idea)
Quyết định "có làm ERP không" được biện minh bằng bốn nhóm **business case rationale** — lý do nghiệp vụ. Điểm then chốt cho BA: *loại rationale* quyết định mức độ nó có thể dẫn dắt thiết kế và đo lường thành công. Rationale theo quy trình/chiến lược cho ra đặc tả thiết kế cụ thể và chuẩn nghiệm thu; rationale công nghệ/cạnh tranh thì không.

## Framework được giới thiệu (Frameworks Introduced)
- **Four Business Case Rationales** — bốn nhóm lý do nghiệp vụ chọn ERP:
  - **Technology rationale**: Y2K, hệ thống rời rạc (disparate), chất lượng kém, khó tích hợp sáp nhập, hệ lỗi thời. Đo kiểu **yes–no**; mạnh để biện minh thay thế hệ thống *nhưng ít hướng dẫn cấu hình*.
  - **Business process rationale**: giảm nhân sự, giảm tồn kho, giảm chi phí IT, tăng năng suất, rút ngắn financial close... Có *mục tiêu đo được cụ thể* (ví dụ "giảm 40% tồn kho dở dang") ⇒ dự báo được cost-benefit và hướng dẫn thiết kế/đánh giá.
  - **Strategic rationale**: cải thiện phản hồi khách hàng, chất lượng, làm xương sống cho thương mại điện tử — vượt khỏi hiệu quả thuần túy.
  - **Competitive rationale**: "đối thủ có nó" — có thể phải làm "chỉ để tồn tại"; nhưng nên hỏi *tại sao* quan trọng và lợi ích cụ thể là gì.
  - Khi nào dùng: phân loại lý do dự án để biết nó có đủ cụ thể dẫn dắt spec không.
- **Rationale → Design & Success Linkage** — liên kết lý do với thiết kế và nghiệm thu: lý do business process/strategic cho đặc tả cụ thể và benchmark đo thành công; lý do technology/competitive thì không có tiêu chí thiết kế rõ.
- **Wagle's Five-Step NPV Approach** — năm bước tính giá trị hiện tại ròng (McKinsey, Wagle 1998):
  - (1) dựng base case tiết kiệm nếu *không* có ERP; (2) dựng ERP case tiết kiệm nếu *có* ERP (gồm cả phần không phụ thuộc ERP); (3) lấy hiệu hai dòng rồi tính NPV phần dư — NPV dương thì nên làm; (4) nếu NPV dương, chạy phân tích độ nhạy chịu được trượt tiến độ/vượt chi phí; (5) phân bổ ngược chi phí về từng đơn vị và buộc họ chịu trách nhiệm tạo ra thay đổi đã hứa.

## Khái niệm chính (Key Concepts)
- **Hard vs soft data**: dữ liệu "cứng" (ví dụ chi phí sửa Y2K theo dòng mã) được lãnh đạo tin; dữ liệu "mềm" (ROI dự phóng về năng suất) khó tạo buy-in.
- **Decision explanation vs decision making**: cost-benefit analysis đôi khi chỉ là *giải thích* quyết định đã có, không phải *ra* quyết định.
- **Available to Promise (ATP)**: năng lực cam kết phân bổ tồn kho cho khách hàng (ví dụ Quantum) — một lợi thế chiến lược.
- **Role of top management**: quyết định ~15 triệu USD thường do CEO/CFO/chief production officer/board; tiếng nói đổi thay phải từ các *domain area* (sản xuất, tài chính), không chỉ IT.

## Mô hình tư duy (Mental Models)
- Phân loại rationale rồi hỏi: "Lý do này có cho tôi con số mục tiêu đo được không?" Nếu có (process/strategic) thì dùng nó làm xương sống cho thiết kế và nghiệm thu.
- Đo kiểu yes-no cho technology rationale; đo bằng mục tiêu định lượng cho business process rationale.
- "Competition has it" nên được bóc tách thành lợi ích cụ thể, không dừng ở việc đối thủ có.
- SAP bán cho "economic buyers" (CEO/CFO) chứ không "bán công nghệ" cho phòng IS — nhớ rằng quyết định ERP là quyết định của lãnh đạo domain.

## Điều cần tránh (Anti-patterns)
- **Chỉ dựa vào technology/competitive rationale rồi kỳ vọng nó dẫn dắt thiết kế**: hai loại này không có tiêu chí thiết kế ⇒ tài liệu dễ mơ hồ, thiếu cơ sở nghiệm thu.
- **Phân tích chi tiết a priori với dữ liệu kém**: lợi ích "fuzzy", chi phí bị ẩn ⇒ số liệu không đáng tin, có thể phản tác dụng.
- **Để IT quyết một mình**: dự án đổi việc của nhiều người, IT executive đơn độc không tạo được thay đổi.

## Bảng tham chiếu (Reference Tables)
**Table 7.1 — Technology Motivations** (khảo sát Deloitte & Touche, % mẫu):

| Động cơ | % |
|---|---|
| Hệ thống không tuân thủ Y2K | 27 |
| Hệ thống rời rạc (disparate) | 24 |
| Chất lượng kém / khó thấy thông tin | 17 |
| Quy trình/hệ thống không tích hợp | 12 |
| Khó tích hợp các vụ sáp nhập | 8 |
| Hệ thống lỗi thời | 7 |
| Không hỗ trợ tăng trưởng | 5 |

**Table 7.2 — Anticipated Business Benefits** (% mẫu): giảm nhân sự 20; giảm tồn kho 19; giảm chi phí IT 13; tăng năng suất 11; rút ngắn chu kỳ xử lý đơn 9; quản trị tiền mặt 7; doanh thu/lợi nhuận 7; mua sắm 6; đóng sổ tài chính 5; bảo trì 4.

## Ví dụ minh họa (Worked Example)
**ERP Choice – In-House or Outsourced (Phụ lục 7-1).** Quyết định cơ bản nhất khi "go ERP" là tự làm hay thuê ngoài. Có hai dạng thuê ngoài: (1) thuê ngoài *riêng hệ ERP* (thiết kế, chọn, triển khai, hỗ trợ); (2) thuê ngoài *cả phòng xử lý dữ liệu*, trong đó quyết định ERP làm cùng đơn vị nhận outsourcing (ví dụ IBM tiếp quản phòng dữ liệu của Kodak).

Lập luận ủng hộ thuê ngoài — lời một nhà thầu 60 triệu USD chọn J.D. Edwards: "Chúng tôi cần gói kế toán mới nhưng không muốn đầu tư lớn vào phần mềm và phần cứng. Thuê ngoài giúp tránh cam kết tài chính khổng lồ và giảm nhu cầu nhân sự MIS." Lập luận phản đối — phó chủ tịch IT tại Fujitsu Microelectronics: "Vấn đề mấu chốt là khớp phần mềm với nghiệp vụ và tối ưu ứng dụng cho công ty. Tôi không chắc một bên thứ ba làm được điều đó." **Bài học cho BA**: thuê ngoài hấp dẫn doanh nghiệp muốn tránh đầu tư hạ tầng và nhân sự IT, nhưng đánh đổi là độ khớp (fit) giữa phần mềm và nghiệp vụ — phải ghi rõ trong tài liệu quyết định.

## Điểm cần nhớ (Key Takeaways)
1. Có bốn nhóm rationale: technology, business process, strategic, competitive.
2. Chỉ process và strategic rationale cho đặc tả thiết kế cụ thể và chuẩn nghiệm thu.
3. Technology rationale đo yes-no; process rationale đo bằng mục tiêu định lượng.
4. Dùng NPV năm bước (Wagle) để lượng hóa, kèm phân tích độ nhạy và phân bổ trách nhiệm.
5. Quyết định ERP thuộc về lãnh đạo domain (CEO/CFO/board), không phải riêng IT.

## Ứng dụng cho BA ERP (BA Application)
- Mở tài liệu dự án bằng việc phân loại business case rationale; nếu dự án chỉ dựa trên Y2K/"đối thủ có", chủ động bổ sung rationale process/strategic để có cơ sở thiết kế và nghiệm thu.
- Chuyển mỗi process/strategic rationale thành *mục tiêu đo được* (ví dụ đóng sổ 24→6 ngày, giảm 40% tồn kho) và dùng chính nó làm **acceptance criteria** cho tài liệu — chống tài liệu mơ hồ.
- Khi rationale là "competition has it", bóc tách thành năng lực cụ thể (ví dụ ATP) rồi đặc tả chức năng tương ứng, tránh sao chép mù.
- Ghi rõ vai trò quyết định (CEO/CFO/domain) và người ký nghiệm thu trong tài liệu để biết ai xác nhận yêu cầu.
- Với lựa chọn in-house vs outsourced, ghi đánh đổi "fit nghiệp vụ" như một rủi ro/ràng buộc trong tài liệu quyết định.

## Liên hệ (Connects To)
- **Chương 6**: predictability đo lường phụ thuộc technology enabled hay clean slate.
- **Chương 10 & 12**: dùng rationale để thiết kế và đánh giá thành công sau golive.
- **Chương 14**: strategic rationale — ERP làm xương sống cho thương mại điện tử.
- **Chương 15**: rủi ro ERP — chất lượng dữ liệu đo lường và buy-in.
