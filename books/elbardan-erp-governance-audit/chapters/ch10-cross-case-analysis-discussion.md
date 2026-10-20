# Chương 10: Phân tích đa tình huống và thảo luận (Cross-Case Analysis and Discussion)

## Ý tưởng cốt lõi (Core Idea)
So sánh bốn tổ chức Ai Cập để rút ra quy luật: **logic kiểm soát** (control logic) nhúng trong hệ thống ERP cộng với **áp lực quản trị** (governance pressures) bên ngoài cùng định hình cách chức năng kiểm toán nội bộ (**IAF — Internal Audit Function**) phải thích nghi; tổ chức nào hiểu và tận dụng được 11 giả định kiểm soát của ERP thì nâng cấp được IAF, tổ chức nào không hiểu thì IAF bị bào mòn và các nhóm khác (nhất là đội IT) chiếm lấy công việc kiểm soát.

## Framework được giới thiệu (Frameworks Introduced)
- **ERP control logic — logic kiểm soát của ERP**: ba tầng — ERP institutional logic → control principle → 11 control assumptions (giả định kiểm soát). Đây là "mã gen" kiểm soát mà mọi hệ ERP mang theo.
  - Dùng khi: thiết kế/đánh giá tính năng kiểm soát của một module ERP.
  - Cách dùng: kiểm từng giả định xem module đã hiện thực hóa chưa (xem Bảng tham chiếu).
- **Strategic responses (Oliver 1991) — chiến lược phản ứng trước áp lực thể chế**: acquiescence (tuân thủ), compromise (thỏa hiệp), avoidance (né tránh), defiance (chống đối), manipulation (thao túng).
  - Cách dùng: nhận diện tổ chức/phòng ban sẽ phản ứng thế nào với thay đổi do ERP mang lại để lường trước kháng cự.
- **Three institutional pressures — ba áp lực thể chế**: coercive (ép buộc bằng luật/quy định), normative (chuẩn mực nghề nghiệp, giá trị), mimetic (bắt chước mô hình thành công khi bất định).
- **Legitimacy types — các loại tính chính danh**: pragmatic (lợi ích thực dụng), moral (đúng về chuẩn mực), cognitive (được mặc nhiên thừa nhận).

## Khái niệm chính (Key Concepts)
- **IAF (Internal Audit Function)**: chức năng kiểm toán nội bộ; sau ERP phải chuyển từ dò lỗi thủ công sang đảm bảo kiểm soát dựa trên rủi ro.
- **Comprehensive auditor — kiểm toán viên toàn diện**: vai trò mới kiểm toán theo tiến trình xuyên chức năng thay vì theo từng chức năng.
- **Collective affair — kiểm soát là việc chung**: sau ERP, trách nhiệm kiểm soát nội bộ lan ra nhiều phòng ban, không còn độc quyền của kiểm toán.
- **Peer-review / self-review controls**: kiểm soát mới nảy sinh do dữ liệu tích hợp và một điểm nhập liệu — mỗi người buộc phải rà soát công việc của người khác hoặc của chính mình.
- **Decoupling — tách rời hình thức khỏi thực chất**: giữ vỏ hình thức (một kiểm toán viên làm biểu tượng) mà bỏ thực chất, để tỏ ra tuân thủ.
- **Workaround — lách hệ thống**: giữ thói quen cũ (kể cả thao tác bất hợp lệ) bằng cách đi vòng qua hệ thống thay vì tái thiết kế quy trình.

## Mô hình tư duy (Mental Models)
- Coi **ERP và quản trị như hai mặt một đồng xu**: quy định quản trị vạch ra hướng dẫn quy trình, ERP thực thi quy trình theo các hướng dẫn đó — mặc định chúng đồng hướng, nhưng vẫn cần nỗ lực căn chỉnh (alignment) khi triển khai.
- Dùng mức độ **IAF trước ERP** để dự đoán kết quả sau ERP: IAF mạnh trước đó → ERP là cú hích để "cách mạng"; IAF yếu trước đó → dễ tan rã sau ERP.
- Áp lực càng cao và môi trường càng **liên kết chặt (interconnectedness)** → càng chọn chiến lược ít chủ động (tuân thủ/thỏa hiệp) thay vì chống đối.

## Điều cần tránh (Anti-patterns)
- **Trộn lẫn "kiểm toán" và "thanh tra/inspection"**: gây lẫn lộn vai trò (như ở NB), giữ tư duy "bắt lỗi" không tạo giá trị.
- **Không lập kế hoạch quản trị thay đổi (change management)**: ở NC và NB không có kế hoạch → người dùng kháng cự, lách hệ thống, IAF không thích nghi kịp.
- **Để kiểm toán viên đứng ngoài dự án triển khai ERP**: mất cơ hội cài kiểm soát đúng và hiểu hệ thống; hậu quả kéo dài về sau.
- **Customise để giữ quy trình cũ bất hợp lệ**: ERP chặn thao tác sai nên NC phải lách; đúng ra phải tái thiết kế để quy trình "kiểm toán được" (auditable).

## Bảng tham chiếu (Reference Tables)

Bốn tình huống (tái dựng rút gọn từ Meta-matrix 10.6):

| Mã | Ngành / Loại | ERP | Kết cục IAF | Phản ứng chiến lược | Chính danh |
|----|------|-----|-------------|---------------------|-----------|
| IC | Hàng tiêu dùng, quốc tế | SAP | Mở rộng, tích hợp toàn diện | Acquiescence + Compromise | Pragmatic + Moral |
| NC | Hàng tiêu dùng, nội địa | SAP | Bị bào mòn, còn 1 kiểm toán viên làm biểu tượng | Defiance (thất bại) → Compromise | Mất (decoupling) |
| NB | Ngân hàng, nội địa | Oracle | Thu hẹp, giữ "thanh tra", thuê ngoài IT audit | Avoidance + Defiance | Moral (bám tục lệ) |
| IB | Ngân hàng, quốc tế | Oracle | Đã tích hợp, dựa trên rủi ro | Acquiescence (imitation) | Pragmatic + Moral |

11 giả định kiểm soát của ERP (control assumptions — logic kiểm soát, Fig 10.1 & Bảng 10.2):

| Giả định | Ý nghĩa kiểm soát cho BA |
|---------|--------------------------|
| **Integration** (tích hợp) | Một điểm nhập liệu, liên kết tiến trình với báo cáo tài chính; sinh peer/self-review |
| **Standardisation** (chuẩn hóa) | Quy trình & cấu trúc kế toán chuẩn; lệch chuẩn dễ lộ |
| **Automation** (tự động hóa) | Kiểm soát tự động, giảm lỗi do con người; test SoD tự động |
| **Multiple methods of control** (đa phương thức) | Kiểm soát cùng một đối tượng từ nhiều góc: tài chính, logistics, thông tin |
| **Preventive controls** (phòng ngừa) | Chặn nhập sai/sai kỳ/vượt ngưỡng trước khi xảy ra, không chỉ phát hiện |
| **Compensating controls** (bù trừ) | Pha trộn nhiều kiểm soát để giảm cùng một rủi ro |
| **Continuous monitoring** (giám sát liên tục) | Báo cáo định kỳ/đột xuất/ngoại lệ theo thời gian thực |
| **Data security** (an ninh dữ liệu) | Phân quyền theo vai trò (role-based access), hồ sơ quyền; là một cấu phần kiểm soát mới |
| **Centralisation** (tập trung) | CSDL tập trung, truy cập toàn bộ thông tin không cần đi lại |
| **Data consistency** (nhất quán dữ liệu) | Chuẩn hóa quy trình → dữ liệu khớp giữa chi nhánh/phòng ban |
| **Transparency & visibility** (minh bạch & hiển thị) | Truy vết từ số tổng hợp xuống chứng từ; hành vi nhìn thấy được |

Nỗ lực căn chỉnh khi triển khai (aligning efforts, Bảng 10.3): **Alignment** · **Change management** · **Reengineering & customisation** · **IAF role in implementation**.

Mười chiều thích nghi IAF (Bảng 10.4): scope of services · structure · skills · tools · sourcing · relationship with IT · size · budget · relationship with external auditor · strategic response.

## Ví dụ minh họa (Worked Example)
Đối chiếu IC và NC (cùng ngành hàng tiêu dùng, cùng SAP) cho thấy điều quyết định không phải phần mềm mà là con người và quản trị:
- **IC**: kiểm toán viên tham gia từ khâu thu thập yêu cầu và mapping; input chính của họ là vai trò & phân quyền (roles/authorisations) để đảm bảo môi trường kiểm soát khớp. Thủ tục bất hợp lệ bị ERP chặn nên quy trình được tái thiết kế thành dạng kiểm toán được. Kết quả: IAF mở rộng phạm vi (kiểm SoD tự động, quyền truy cập, an ninh thông tin, kiểm soát bù trừ), đội kiểm toán tăng người đa ngành, giữ chính danh pragmatic + moral.
- **NC**: kiểm toán viên không tham gia bất kỳ giai đoạn nào; quản lý lách hệ thống để giữ "quy trình ưa thích" (một số bất hợp lệ). Không có kế hoạch quản trị thay đổi. Đội IT tiếp quản việc giám sát và đảm bảo SoD. Kết quả: IAF mất giá trị, công ty giữ đúng một kiểm toán viên như biểu tượng (decoupling) — chính danh bị mất.
Bài học rút được: cùng một hệ ERP có thể "nâng" hoặc "giết" một chức năng kiểm soát tùy mức độ tham gia sớm và kế hoạch thay đổi.

## Điểm cần nhớ (Key Takeaways)
1. ERP mang logic kiểm soát riêng gồm 11 giả định — hãy coi đó là checklist tính năng kiểm soát khi thiết kế module.
2. Lôi kéo người làm kiểm soát/nghiệp vụ vào dự án từ sớm để cài kiểm soát đúng và làm quy trình kiểm toán được.
3. Luôn kèm kế hoạch quản trị thay đổi + đào tạo; thiếu nó là nguyên nhân chính khiến thích nghi thất bại.
4. Tái thiết kế quy trình (reengineering) thay vì lách hệ thống; ERP chặn thao tác sai là tính năng, không phải lỗi.
5. Sau ERP, kiểm soát là việc chung của nhiều phòng ban — phải nêu rõ ai chịu trách nhiệm phần nào (RACI).
6. Chuyển trọng tâm từ "phát hiện lỗi thủ công" sang "phòng ngừa tự động" và kiểm toán theo tiến trình xuyên chức năng.

## Ứng dụng cho BA ERP (BA Application)
- Dùng 11 giả định kiểm soát làm **checklist non-functional/control requirements** cho từng module: tích hợp, chuẩn hóa, tự động hóa, phòng ngừa, bù trừ, giám sát liên tục, an ninh dữ liệu, tập trung, nhất quán, minh bạch, đa phương thức.
- Với mỗi chức năng, đặc tả rõ **role-based access + hồ sơ quyền + SoD** như một cấu phần kiểm soát (data security là requirement, không phải tùy chọn).
- Viết requirement để quy trình **auditable**: một điểm nhập liệu, truy vết từ tổng hợp xuống chứng từ, log giao dịch, kiểm soát peer/self-review khi dữ liệu dùng chung.
- Khi khách muốn customise để giữ thói quen cũ, đưa quyết định reengineering vs customisation vào tài liệu kèm rủi ro mất tính kiểm soát.
- Ghi nhận các **compliance driver** (coercive/normative) của khách như một nguồn yêu cầu bắt buộc, và lường trước kháng cự (strategic response) để lập kế hoạch change management.

## Liên hệ (Connects To)
- **Ch 11 (Kết luận)**: tổng hợp khung khái niệm và các khuyến nghị thực hành suy ra từ chương này.
- **Ch 12 (Phụ lục)**: coding scheme liệt kê đúng 11 giả định và các chiều thích nghi dùng ở đây; interview agenda để thu thập chúng.
- **COSO / COBIT**: 11 giả định ánh xạ tới kiểm soát ứng dụng, phân quyền và giám sát liên tục trong các khung kiểm soát nội bộ chuẩn.
- **SoD (Segregation of Duties)**: khái niệm trung tâm được ERP tự động hóa và kiểm thử.
