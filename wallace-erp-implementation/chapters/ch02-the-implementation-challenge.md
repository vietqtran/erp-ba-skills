# Chương 2: Thách thức khi Triển khai (The Implementation Challenge)

## Ý tưởng cốt lõi (Core Idea)
Triển khai ERP khó vì một **catch-22** cố hữu, nhưng gần như chắc thắng nếu làm đúng hai điều: (1) một **lịch triển khai quyết liệt (aggressive schedule)** nhắm lợi ích tối đa trong thời gian tối thiểu, và (2) đi theo **the Proven Path** — bộ bước đã được chứng minh. "Pay the bill now or pay more later": bỏ bước nào rồi cũng phải quay lại làm, tốn kém hơn.

## Framework được giới thiệu (Frameworks Introduced)
- **Catch-22 of ERP** — ba lý do khiến triển khai khó:
  1. **It's a lot of work** — thay đổi cách cả công ty xử lý cung–cầu.
  2. **It's a do-it-yourself project** — không thể khoán cho tư vấn/nhà cung cấp; từ đó có nguyên tắc **IMPLEMENTERS = USERS** (người triển khai phải là người sẽ vận hành).
  3. **It's not priority number one** — việc số 1 luôn là điều hành kinh doanh; ERP nên là ưu tiên số 2.
  - Các lý do bổ sung: people-intensive; cần lãnh đạo cấp cao tham gia; liên quan hầu hết mọi phòng ban; buộc người ta làm việc khác đi (massive behavior change).
- **Aggressive Implementation Schedule**: một business unit cỡ trung nên hoàn tất ERP trong **hơn 1 năm, dưới 2 năm** (quy ước **18 tháng**). Dài hơn 2 năm, xác suất thành công giảm mạnh. Lý do cần quyết liệt: giữ nhiệt huyết, giữ ưu tiên, chống thay đổi ngoài dự kiến (nhân sự/môi trường), chống trượt lịch, và thu lợi sớm.
- **The Three Knobs** — ba biến của quản lý dự án: **Work** (khối lượng), **Time** (thời gian lịch, không phải người-năm), **Resources** (nguồn lực). Giữ cố định 2, điều chỉnh biến còn lại. Company-wide: cố định work+time, xoay resource. Quick-Slice: cố định resource+time (ngắn), xoay work (phạm vi).
- **Hai lộ trình trong Proven Path**: **Company-Wide** (toàn công ty, mọi chức năng, 1–2 năm) và **Quick-Slice** (một/vài dòng sản phẩm Pareto tác động cao, hầu hết nhưng không phải tất cả chức năng, 3–5 tháng).
- **The Proven Path** — xem Key Concepts; là bộ bước rời rạc, đi theo "faithfully and with dedication" (không chọn-bỏ, không skip bước).

## Khái niệm chính (Key Concepts)
Các bước Proven Path (Figure 2-2), theo trình tự logic:
- **Audit/Assessment I**: phân tích hiện trạng, vấn đề, cơ hội; ERP có phải bước đúng? company-wide hay Quick-Slice?
- **First-cut Education**: lãnh đạo+quản lý vận hành học tổng quan ERP là gì, vận hành ra sao, cần gì để triển khai.
- **Cost/Benefit Analysis**: văn bản nêu chi phí và lợi ích → quyết định làm/không.
- **Go/No-Go Decision**: quyết định chính thức từ cấp cao nhất.
- **Vision Statement**: văn bản mô tả môi trường vận hành mong muốn sau ERP.
- **Performance Goals**: thống nhất hạng mục nào sẽ cải thiện và đạt mức cụ thể nào.
- **Project Organization**: lập Executive Steering Committee, project team, full-time project leader.
- **Initial Education and Training**: lý tưởng 100%, tối thiểu 80% nhân sự được đào tạo.
- **Implementing Sales & Operations Planning (S&OP)**: "top management's handle on the business"; làm sớm, win sớm.
- **Demand Management, Planning, and Scheduling Processes**: xử lý mix (sản phẩm, KH, đơn, thiết bị cụ thể) qua định nghĩa quy trình + pilot/cutover.
- **Data Integrity**: inventory records, BOM, công thức, routing... phải chính xác, đầy đủ, cấu trúc đúng.
- **Finance & Accounting Processes**: định nghĩa+triển khai với độ chặt như quy trình cầu/hoạch định (thường dễ hơn vì tri thức tài chính chín muồi hơn).
- **Software Selection + Configuration/Installation**.
- **Audit/Assessment II/III**, **Ongoing Education**: duy trì và nâng cấp Class A sau triển khai.

## Mô hình tư duy (Mental Models)
- **IMPLEMENTERS = USERS**: nếu tách trách nhiệm triển khai khỏi trách nhiệm vận hành thì không ai chịu trách nhiệm kết quả (implementers đổ cho users dùng sai, users đổ cho implementers làm sai).
- **ERP là people system, không phải computer system**: phần mềm chỉ giúp thông tin chạy nhanh/sâu hơn; nếu quy trình không đổi thì thông tin xấu chạy nhanh hơn một cách nguy hiểm.
- **Lịch chặt ít trượt hơn lịch lỏng**: lịch quyết liệt thường ít slip hơn lịch "casual".
- **Chi phí trì hoãn**: trì hoãn 1 tháng có thể vượt $100,000 ở nhiều công ty; làm càng chậm càng mất lợi ích.

## Điều cần tránh (Anti-patterns)
- **Khoán ERP cho outsiders**: tư vấn/nhà cung cấp làm thay toàn bộ → thất bại; chỉ người trong công ty mới đủ hiểu và có quyền đổi cách làm.
- **Kéo dài 3–4 năm**: vượt sức chú ý của tổ chức, ưu tiên tụt, xác suất thành công giảm.
- **Skip bước trên Proven Path**: mọi lần bỏ bước đều phải quay lại làm lại, đắt hơn.
- **Coi thay ES là đủ để đạt kết quả lớn**: không đổi quy trình thực tế thì vô ích.

## Ví dụ minh họa (Worked Example)
**Vì sao "gần 100%" chứ không phải "<50%"**: Sách thừa nhận số công ty Class C/D nhiều hơn Class A/B, nên thoạt nhìn xác suất thành công có vẻ dưới 50%. Nhưng gần như *không có* công ty Class C/D nào đã theo Proven Path một cách nghiêm túc. Nhóm C/D gồm: công ty coi ERP là "chuyện máy tính để đặt phụ tùng/đóng sổ nhanh", công ty không đào tạo con người, không làm sạch dữ liệu, hoặc bị cuốn vào vấn đề phần mềm/chính trị nội bộ. Ngược lại, hầu hết công ty theo Proven Path nghiêm túc đều đạt Class A hoặc Class B cao. Kết luận của tác giả: xác suất thành công là *lựa chọn của bạn*, quyết định bởi việc có theo Proven Path đầy đủ hay không.

## Điểm cần nhớ (Key Takeaways)
1. Thành công = **aggressive schedule (≈18 tháng) + Proven Path đầy đủ, không skip bước**.
2. Người triển khai phải chính là người vận hành (**IMPLEMENTERS = USERS**).
3. ERP là ưu tiên **số 2**, ngay dưới "điều hành kinh doanh".
4. Dùng **Three Knobs** để hoạch định: thường cố định work+time, xoay resource; Quick-Slice thì xoay phạm vi work.
5. Chứng minh lý do qua **chi phí trì hoãn**, không chỉ ROI.

## Ứng dụng cho BA ERP (BA Application)
- Cấu trúc tài liệu/dự án theo **các bước Proven Path** và **các phase** thay vì theo danh sách module phần mềm — điều này cũng là trình tự viết spec hợp lý (hoạch định trước, thực thi sau).
- Mỗi chức năng trong spec nên ghi rõ **role vận hành thực tế** (vì implementers = users): ai sẽ dùng chính, ai thao tác một phần, ai duy trì dữ liệu.
- Ưu tiên tài liệu hoá sớm cho **S&OP** và **data integrity** vì đây là "early wins" và là nền cho các chức năng mix phía sau.
- Dùng **Performance Goals** làm tiêu chí nghiệm thu đo lường được cho tài liệu (mức dịch vụ KH, độ chính xác tồn kho, v.v.), tránh mục tiêu mơ hồ.

## Liên hệ (Connects To)
- **Chương 1**: ABCs (People/Data/Computer) và Class ABCD mà Proven Path bám theo.
- **Chương 3**: triển khai company-wide theo phase (chi tiết hoá Proven Path).
- **Chương 5**: chi tiết Audit/Assessment I, First-cut Education, Vision, Cost/Benefit, Go/No-Go.
- **Chương 8 & 10**: S&OP và Data Integrity (các early wins).
- **Chương 13–14**: lộ trình Quick-Slice.
