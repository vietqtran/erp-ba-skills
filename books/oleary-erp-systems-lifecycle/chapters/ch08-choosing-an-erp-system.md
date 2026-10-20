# Chương 8: Lựa chọn hệ thống ERP (Choosing an ERP System)

## Ý tưởng cốt lõi (Core Idea)
Có hai cách tiếp cận chính để chọn ERP — **requirements analysis** (phân tích yêu cầu) và **gap analysis** (phân tích khoảng cách) — nhưng cả hai đều chỉ tập trung vào chức năng (functionality) và bỏ qua hàng loạt yếu tố khác (chi phí, thời gian cài đặt, nhân sự triển khai, bảo trì). Một cách tiếp cận mới đang nổi lên là bỏ bước "as is", đi thẳng tới "to be" trên một gói ERP cụ thể; và cách "evaluation" dùng tiêu chí có trọng số tuy cho ra một con số duy nhất nhưng dễ bị thao túng.

## Framework được giới thiệu (Frameworks Introduced)
- **Requirements Analysis** — phân tích yêu cầu: rà soát yêu cầu đối với **models, artifacts, and processes (MAPs)** — mô hình, chứng từ/tạo tác, quy trình của tổ chức.
  - Khi nào dùng: khi cần một danh sách chuẩn để benchmark các gói phần mềm, tạo buy-in cho người dùng, và hiểu giới hạn của MAPs hiện tại.
  - Cách làm: (1) chọn người viết yêu cầu — người làm việc hằng ngày cho ra yêu cầu bám sát thực tế, quản lý cho ra yêu cầu "lẽ ra phải có"; đội tốt nhất trộn cả hai cộng với một consultant độc lập; (2) phân loại theo mức quan trọng (required/optional, hoặc rank 1–3); (3) tổng hợp thành tài liệu yêu cầu (**request for proposal, RFP**) gửi nhà cung cấp; (4) chọn định dạng: danh sách chi tiết, hoặc tiếp cận **"scripted"** (demo gần như cố định do vendor dựng ở pha 1; pha 2 demo chặt chẽ dùng chính dữ liệu và nghiệp vụ của khách hàng để lộ ra các gap).
- **Gap Analysis ("As Is" vs "To Be")** — so sánh hiện trạng và trạng thái mục tiêu để tìm khoảng cách.
  - "To be" có hai dạng: **clean slate** (độc lập với gói phần mềm → trùng với requirements model) hoặc **technology enabled** (dựa trên một gói ERP cụ thể, còn gọi là **best practices analysis**).
  - Gap xác định các modification cần thiết và chi phí thực sự ngoài tiền phần mềm.
- **Emerging Approach** — không làm "as is", xem triển khai ERP là tái cấu trúc do công nghệ dẫn dắt, đi thẳng tới "to be" trên gói đã chọn. Bốn lập luận: (1) các gói ERP tốt đều có tập best practices tương đương; (2) sao chép quy trình cũ là vô ích; (3) best practices analysis chỉ nên làm trong bối cảnh gói ERP đã chọn; (4) chi phí tối thiểu khi ít thay đổi phần mềm nên chỉ chọn best practice có sẵn trong gói.
- **Evaluation (weighted criteria)** — mở rộng ra ngoài chức năng: liệt kê các factor + weight, cộng điểm, gói có tổng cao nhất thắng (ví dụ Timberjack).

## Khái niệm chính (Key Concepts)
- **MAPs (Models, Artifacts, Processes)**: ba đối tượng mà yêu cầu hệ thống nhắm tới.
- **Requirements granularity / "fineness"**: độ mịn của yêu cầu — một yêu cầu có thể là cả một bộ best practice, hoặc chỉ một trường dữ liệu đơn lẻ.
- **"Available to promise"**: một tính năng khác biệt có thể quyết định lựa chọn (trường hợp Quantum chọn Oracle).
- **Software taker**: doanh nghiệp nhỏ/vừa chấp nhận phần mềm như nó vốn có, không đủ lực buộc vendor sửa riêng.

## Mô hình tư duy (Mental Models)
- Xem "as is" là cần thiết **khi** giữ nguyên quy trình; nếu định tái cấu trúc mạnh thì "as is" mất giá trị.
- Xem factor + weight là công cụ vừa để **chọn** vừa để **giải thích/biện minh**: chọn trước khi xem demo thì là cơ sở quyết định; chọn sau khi xem thì chỉ là hợp lý hóa.
- Để lựa chọn được, phải tìm chỗ **khác biệt** (variation) giữa các gói — tập trung vào feature tạo khác biệt, không phải mọi feature.

## Điều cần tránh (Anti-patterns)
- **Đếm số yêu cầu được đáp ứng để quyết định**: vì không chuẩn hóa granularity, một trường dữ liệu bị tính ngang một quy trình.
- **Bỏ qua chi phí tới tận khi đã chọn xong phần mềm**: đánh giá thường làm ở cấp dưới trong khi ngân sách ở cấp trên, nên cost/benefit không gặp nhau.
- **Thao túng factor và weight**: Timberjack chỉ cho functionality 30/160 điểm — gói mạnh chức năng không được lợi, lựa chọn bị lái.
- **Để RFP khóa cứng quy trình lỗi thời** thay vì tận dụng cơ hội tái cấu trúc.
- **RFP quá lớn**: vendor bận có thể bỏ không phản hồi, chỉ còn vendor rảnh (ít người, ít việc) trả lời.

## Bảng tham chiếu (Reference Tables)
Bảng 8.1 — Tiêu chí & trọng số của Timberjack (tổng = 160; cột điểm QAD/Oracle bị trích xuất rỗng):

| Factor | Weight |
|---|---|
| Support | 20 |
| Functionality | 30 |
| User interface | 10 |
| Flexibility | 20 |
| Future prospects | 10 |
| Reliability | 20 |
| Integration | 30 |
| Platform | 20 |

Bảng 8.2 — Chi phí ERP (Firm B, cuối cùng chọn SAP):

| Hạng mục | Nâng cấp hệ thống hiện có | Oracle | SAP |
|---|---|---|---|
| Implementation | $3–5tr | $4–8tr | $6–10tr |
| Phát triển phần mềm cho vừa khớp | $2–4tr | $1–3tr | tối thiểu |
| Số người bảo trì | 15–20 | 10–15 | 8–10 |

Các yếu tố thường bị bỏ qua: Cost, Installation Time, Flexibility, User Interface, Upgradability, Computing Environment, Implementation Personnel, Day-to-Day Use & Maintenance, Functionality (đo như một đặc tính đơn, dễ hiểu nhầm).

## Ví dụ minh họa (Worked Example)
**Quy trình 5 bước của Chesapeake Display & Packaging (CDP)** — CIO Gary Cheimis lập:
1. Lập **blue-ribbon team (BRT)** ≤ 10 người, chọn theo hiểu biết nghiệp vụ, trộn người "nhìn tổng thể" và "nhìn chi tiết".
2. Mời vendor demo: chọn số ít vendor hạng nhất, cho BRT tiếp xúc không giới hạn tới khi demo (khoảng 3 tuần), demo gói trong 1–2 ngày, vendor tự chọn phần cứng/CSDL.
3. Yêu cầu vendor chứng minh năng lực triển khai nhanh: "chạy được nghiệp vụ của chúng tôi", "triển khai đúng thời gian yêu cầu", "hiểu ngành".
4. **Bỏ phiếu**: ba ứng viên BAAN, J.D. Edwards (JDE), SSA; mỗi người chấm theo lĩnh vực chuyên môn trên hai tiêu chí — best functional fit và best implementation personnel — thang 3–1 (3 cao nhất).
5. Chọn: JDE thắng với tổng điểm cao nhất (ưu thế tài chính, giải pháp tích hợp, có sẵn HR & payroll, bộ công cụ hướng đối tượng, module Synquest lập lịch theo chi phí).

Tương phản — **Đơn hỏi của một CFO** (Appendix 8-2): doanh nghiệp làm 3 bước "as is" → "to be" → matching với Coopers & Lybrand, kết luận module sản xuất của SAP kém hơn hệ thống tự viết hiện tại, nhiều gap → phải lập trình nhiều → nếu chỉ mua SAP cho module tài chính và mua hàng thì quá đắt. Minh họa: gap analysis có thể dẫn tới kết luận "không nên mua".

## Điểm cần nhớ (Key Takeaways)
1. Phân loại yêu cầu theo mức quan trọng và ghi rõ granularity; đừng để một trường dữ liệu bị tính ngang một quy trình.
2. Luôn kèm các yếu tố phi chức năng (chi phí, thời gian, nhân sự triển khai, bảo trì, khả năng nâng cấp) vào tiêu chí chọn — chúng thường bị bỏ sót.
3. Quyết factor và weight TRƯỚC khi xem demo, nếu không tài liệu chỉ để hợp lý hóa lựa chọn có sẵn.
4. Dùng pha demo "scripted" chặt chẽ với chính dữ liệu của mình để lộ ra các gap cần modification.
5. Một con số tổng hợp duy nhất tiện nhưng dễ bị thao túng và có thể cộng gộp các yếu tố không cùng bản chất.

## Ứng dụng cho BA ERP (BA Application)
- Khi viết tài liệu yêu cầu/RFP: gắn nhãn mức ưu tiên (bắt buộc/tùy chọn hoặc rank 1–3) cho từng yêu cầu và chú thích độ mịn, để người đọc không "đếm" nhầm.
- Bổ sung một mục non-functional riêng (cost, installation time, flexibility, UI, upgradability, computing environment, implementation personnel, maintenance) vào mọi spec lựa chọn hệ thống.
- Khi mô tả tiêu chí đánh giá vendor, ghi rõ trọng số và thời điểm chốt trọng số (trước demo) để tránh bị thao túng.
- Thiết kế kịch bản demo hai pha: pha lỏng để vendor trình bày, pha chặt dùng dữ liệu/nghiệp vụ thật của khách để phát hiện gap → ghi gap thành danh sách modification kèm ước tính chi phí.
- Nếu doanh nghiệp định tái cấu trúc mạnh, đừng dành công sức mô hình hóa "as is" chi tiết — ghi rõ phạm vi "to be" dựa trên gói đã chọn.

## Liên hệ (Connects To)
- **Ch 9**: quyết định đổi quy trình hay đổi phần mềm (reengineering policy) gắn chặt với mức độ cần "as is"/"to be".
- **Ch 10**: MAPs — cách chọn standard models, artifacts, processes.
- **Ch 3**: tái cấu trúc clean slate vs technology enabled (constrained).
- **Ch 11 & Appendix 11-1**: tình huống Quantum — yêu cầu, chọn hệ thống và tính năng "available to promise".
