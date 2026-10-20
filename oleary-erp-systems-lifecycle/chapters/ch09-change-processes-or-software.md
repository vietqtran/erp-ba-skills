# Chương 9: Thiết kế ERP — Nên đổi quy trình nghiệp vụ hay đổi phần mềm ERP? (Designing ERP Systems: Should Business Processes or ERP Software Be Changed?)

## Ý tưởng cốt lõi (Core Idea)
Khi thiết kế ERP, doanh nghiệp phải chọn một **reengineering policy** (chính sách tái cấu trúc): thay đổi quy trình để khớp phần mềm, sửa phần mềm để khớp quy trình, cả hai, hoặc không gì. Mức thay đổi của tổ chức và mức thay đổi của phần mềm tạo thành ma trận 2×2 — từ **small-r reengineering** (thay đổi tối thiểu cả hai) tới **big-R reengineering** (thay đổi mạnh cả hai). Xác suất triển khai thành công cao nhất khi cần ít thay đổi nhất.

## Framework được giới thiệu (Frameworks Introduced)
- **Small-r vs Big-R Reengineering** — ma trận 2×2 theo hai trục: mức thay đổi quy trình tổ chức × mức thay đổi phần mềm.
  - **Small-r** (đổi tổ chức ít + đổi phần mềm ít): tổ chức thích nghi với phần mềm khớp sẵn; nhanh, rẻ, dự đoán được; phù hợp quy trình generic (tài chính, back office, accounts payable); thường là firm nhỏ–vừa ("software takers") hoặc firm không coi IT là nguồn tạo giá trị. Rủi ro: bỏ lỡ cơ hội cải tiến, không tạo lợi thế cạnh tranh bền vững.
  - **Đổi tổ chức nhiều + đổi phần mềm ít**: ép quy trình vào những gì phần mềm có. Lợi: dễ nâng cấp về sau, chuẩn hóa quy trình. Hại: có thể phá quy trình tạo giá trị (ví dụ đổi lương theo incentive sang lương cứng để khớp phần mềm → hành vi lệch lạc); thay đổi tổ chức có thể thất bại (ngành trash hauler "mang SAP ra bãi rác"). Cần **change management** mạnh.
  - **Đổi tổ chức ít + đổi phần mềm nhiều**: tùy biến phần mềm để giữ quy trình/best practice riêng (Nestlé, Deere). Hại: khó bảo trì và nâng cấp, khó roll-out sang division khác. Cần **project management IT** mạnh.
  - **Big-R** (đổi mạnh cả hai): cần nhiều nguồn lực và thời gian (Boeing + BAAN). Lợi: có đúng phần mềm + quy trình mong muốn, thành first mover, đôi khi vendor "partner" chia sẻ chi phí/rủi ro. Hại: cực đắt, "maintenance nightmare", nâng cấp gần như bất khả.
- **Khi nào cần mô hình "as is" / "to be"** — relevance phụ thuộc vào mức thay đổi: giữ nguyên quy trình thì "as is" rất quan trọng (fit càng chặt càng tốt); tái cấu trúc mạnh thì "as is" mất giá trị. "To be": nếu chỉ sửa phần mềm ít thì "to be" là bài toán **chọn từ portfolio** quy trình có sẵn; nếu sửa nhiều thì "to be" thành bài toán **phát triển quy trình** (gần clean slate).

## Khái niệm chính (Key Concepts)
- **Reengineering policy**: chính sách về mức tùy biến phần mềm và tái cấu trúc tổ chức. Khảo sát Forrester: 37% chọn phần mềm hợp nghiệp vụ và tùy biến chút ít, 5% tùy biến phần mềm cho khớp, 41% tái cấu trúc nghiệp vụ cho khớp phần mềm, 17% không có chính sách.
- **Software as change agent**: phần mềm ERP như tác nhân thúc đẩy thay đổi nghiệp vụ.
- **Backsliding**: nguy cơ "trượt lùi" về quy trình cũ khi triển khai quy trình mới gặp khó.
- **Evolution big-R → small-r**: khi vendor sửa phần mềm cho một firm (Boeing/Nash Finch) thì best practice ngành được nhúng vào sản phẩm, firm sau dùng lại chỉ còn là small-r.
- **"Software takers"**: firm chấp nhận phần mềm như vốn có, thường làm small-r.

## Mô hình tư duy (Mental Models)
- Chọn quadrant dựa trên năng lực, ràng buộc và trade-off mà firm chấp nhận — **không có lời giải tối ưu chung**.
- Đổi người (quy trình) với nhiều consultant cho là "dễ hơn đổi phần mềm" — nhưng chỉ đúng nếu tổ chức tập quyền đủ để ép quy trình chung; firm phân tán (như trash haulers) thì đổi quy trình lại rất khó.
- Xem mỗi quadrant kèm một "yếu tố thất bại" tương ứng: đổi tổ chức nhiều → thất bại do con người/chọn sai best practice/kháng cự; đổi phần mềm nhiều → thất bại do quản trị dự án IT; đổi cả hai → cả hai loại rủi ro.

## Điều cần tránh (Anti-patterns)
- **Đổi quy trình tạo giá trị thành quy trình generic chỉ để khớp phần mềm**: ví dụ đổi cơ chế lương bán hàng, gây hành vi dysfunctional.
- **Tùy biến phần mềm quá nhiều** (Boeing "vài nghìn thay đổi"): biến mỗi lần nâng cấp thành ác mộng, phải nuôi hẳn một tổ chức để đỡ phần mềm.
- **Chọn "as is" fit chặt rồi lại định tái cấu trúc mạnh**: phần mềm khớp quy trình cũ sẽ cản trở tái cấu trúc và dễ gây backsliding.

## Ví dụ minh họa (Worked Example)
**Microsoft triển khai SAP R/3 (small-r reengineering)** — Appendix 9-1:
- Bối cảnh: tài chính Microsoft "như một nước thế giới thứ ba"; hàng trăm legacy app, first close mất 3 tuần. Hai dự án client-server trước đó (D&B, rồi SAP full) đều thất bại vì phần mềm non và thiếu hậu thuẫn nghiệp vụ, tới mức Bill Gates chất vấn mục tiêu và dừng.
- Quyết định: triển khai **chỉ module tài chính** R/3, **không sửa phần mềm** — chấp nhận best practice có sẵn, lấy chính SAP làm "change agent"; lịch 9 tháng, ngân sách gọn.
- Vai trò then chốt: CIO John Connors làm người "dọn chướng ngại" và bảo đảm **business lead** (process owner Scott Boggs, dân tài chính chứ không phải IT) đứng đầu dự án — "ai hưởng lợi nếu thành công, chịu hại nếu thất bại". Thông điệp: "có làm hay không thì đã quyết, bạn chỉ góp ý *làm thế nào*".
- Compromise khi không sửa phần mềm: không có khái niệm "department" trong SAP → phải định nghĩa lại mọi phòng ban thành **profit center/cost center**; "internal orders" của SAP chỉ một trường trong khi Microsoft cần ba (phòng ban × sản phẩm × dự án) → phải cho subsidiary tự tạo tổ hợp mã, làm giảm chuẩn hóa chart of accounts ("quyết định đau đớn nhưng ít tệ nhất"). Cấu hình 3.000 bảng tham số ở HQ, giao subsidiary 33 bảng để tùy chỉnh.
- Training: ép buộc — dọa khóa tài khoản ai không đi học SAPSET; chỉ phải khóa ~20 tài khoản. Kết quả: đúng mọi milestone, "dự án ITG làm tốt nhất của Microsoft tới nay".

## Điểm cần nhớ (Key Takeaways)
1. Gắn quyết định tái cấu trúc với quyết định chọn ERP: mức thay đổi quyết định việc có cần "as is"/"to be" và cần loại nào.
2. Small-r thành công dễ nhất nhưng có thể bỏ lỡ cơ hội cải tiến; big-R cho lợi thế first mover nhưng đắt và rủi ro cao.
3. Quy trình generic (tài chính, back office) nên để small-r; quy trình tạo giá trị khác biệt mới cân nhắc sửa phần mềm.
4. Sửa phần mềm càng nhiều, chi phí phát sinh ba lần: lúc sửa, lúc nâng cấp, và lúc hỗ trợ lâu dài.
5. Đổi tổ chức nhiều cần change management; đổi phần mềm nhiều cần project management IT — đầu tư đúng chỗ dễ gây thất bại.

## Ứng dụng cho BA ERP (BA Application)
- Trước khi viết spec, xác định rõ reengineering policy của dự án (small-r hay sửa phần mềm) — nó quyết định tài liệu có cần mô hình "as is" chi tiết hay chỉ cần "to be" chọn từ portfolio.
- Khi một yêu cầu đòi sửa phần mềm, ghi kèm cảnh báo chi phí ba lần (sửa/nâng cấp/hỗ trợ) và tác động tới khả năng roll-out sang đơn vị khác.
- Đánh dấu rõ quy trình nào là "tạo giá trị, khác biệt" (giữ/tùy biến) vs "generic" (nên theo chuẩn phần mềm) — đây là tiêu chí để quyết đổi quy trình hay đổi phần mềm.
- Khi đặc tả thay đổi quy trình, kèm yêu cầu change management; khi đặc tả tùy biến phần mềm, kèm yêu cầu quản trị dự án IT.
- Ghi nhận các compromise cấu hình (như profit/cost center thay cho "phòng ban", số trường của internal order) thành quyết định thiết kế có chủ đích, kèm hệ quả lên chuẩn hóa danh mục.

## Liên hệ (Connects To)
- **Ch 8**: relevance của "as is"/"to be" bắt nguồn từ cách chọn hệ thống.
- **Ch 3**: tái cấu trúc clean slate vs technology enabled, và BPR trước/trong/sau ERP.
- **Ch 10**: chọn standard models, artifacts, processes (MAPs) — chính là nội dung "to be" chọn từ portfolio.
- **Ch 13**: training như một phần của small-r (ép học, tích hợp kiến thức nghiệp vụ).
- **Ch 15**: các yếu tố thành công/thất bại theo từng quadrant.
