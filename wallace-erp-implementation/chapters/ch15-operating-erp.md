# Chương 15: Vận hành ERP (Operating ERP)

## Ý tưởng cốt lõi (Core Idea)
Không process ERP Class A hay B nào tự duy trì được; nó cần sự chú ý liên tục. Vận hành ERP có hai mục tiêu: **(1) đừng để nó tụt** và **(2) làm nó tốt hơn mãi**. Có năm yếu tố để đạt điều đó: Understanding, Organization, Measurements, Education, và Lean Manufacturing.

## Framework được giới thiệu (Frameworks Introduced)
- **Năm yếu tố vận hành ERP**: Understanding (hiểu biết, không kiêu ngạo) · Organization (tổ chức) · Measurements (đo lường) · Education (giáo dục liên tục) · Lean Manufacturing/JIT.
- **ERP Operating Committee** — tiến hóa của project team sau triển khai:
  - Không còn thành viên full-time; gần 100% là trưởng bộ phận (department heads).
  - Đổi tên từ "project team" vì ERP nay là operational chứ không còn là project.
  - Họp ~mỗi quý (thay vì mỗi tuần).
  - Ghế chủ tịch **luân phiên** giữa các thành viên 1-2 lần/năm (marketing → kế toán → kỹ thuật/mua hàng...) để củng cố cảm giác sở hữu chung — ERP là tập process của *toàn công ty*.
- **ABCD Checklist for Operational Excellence** (Oliver Wight): Section 5 là thước đo vận hành cốt lõi ("how we're doing"); ERP operating committee rà soát chính thức ít nhất 2 lần/năm, thống nhất từng câu trong 22 câu hỏi tổng quan; mỗi câu trả lời "no" phải xác định nguyên nhân, cách sửa, và *thời hạn sửa* (đặt ngày, đừng để trôi).
- **Re-certification hằng năm**: chứng nhận Class A chỉ có giá trị một năm, phải "tái giành"; giúp tập trung lại sự chú ý mỗi năm một lần.

## Khái niệm chính (Key Concepts)
- **Operational vs Financial measurements**: đo hiệu quả ERP cần cả hai; tối thiểu mỗi năm một lần so kết quả bằng tiền với lợi ích đã dự kiến trong cost justification.
- **Half-life của kiến thức**: người ta quên; nếu half-life là 1 năm thì năm sau còn nhớ ~50%, hai năm trước còn ~25% → cần giáo dục nhắc lại.
- **Ongoing education dệt vào "operational fabric"**: đặt chuẩn giáo dục ERP tối thiểu cho *mỗi vị trí*, viết vào job specification; nhân sự mới phải đạt chuẩn trong thời gian ngắn. Giao HR quản lý (lập lịch lớp, theo dõi điểm danh, báo cáo no-show).
- **Giáo dục cho lãnh đạo mới là tuyệt đối**: thay CEO hay nhân sự cấp cao là "điểm hiểm" cho ERP; executive mới cần giáo dục ERP hơn bất kỳ ai — ghi thẳng vào job specification, không có ngoại lệ.

## Mô hình tư duy (Mental Models)
- Ẩn dụ đội Super Bowl hủy training camp: thành công hôm nay không đảm bảo thành công ngày mai; kiêu ngạo + thiếu hiểu biết = mất hạng. Class A có thể tụt xuống B; B có thể tụt xuống C rất nhanh.
- **Creative discontent with the status quo**: công ty xuất sắc luôn "bất mãn sáng tạo" — "năm nay tốt, năm sau phải tốt hơn, nâng high bar thêm 6 inch".
- **Lean Manufacturing là "điều tốt nhất từng xảy ra với ERP"**: vì khi làm đúng, Lean *không cho phép* bỏ bê ERP — khi không còn tồn kho/queue/safety stock che đậy lịch tồi, stockout trở nên đau đớn và Lean sẽ "bắn pháo sáng" đòi đưa ERP về Class A.

## Điều cần tránh (Anti-patterns)
- **Giải tán project team và steering committee sau triển khai**: giữ chúng lại (đã tiến hóa thành operating committee); chúng gần như quan trọng sau cũng như trước.
- **Coi Class A chỉ là mục tiêu "nhân tạo, theo dự án"**: (Mike) rào cản lớn nhất khi giữ Class A là thiếu hiểu biết về lợi ích kinh doanh của ERP; phải nối Class A với lợi ích thực (customer service, cash, profit, sales).
- **"Lấy mắt khỏi quả bóng"**: giả định ERP tự duy trì → mất một bậc hạng → quá trình đảo ngược rất nhọc nhằn.
- **Bỏ qua câu hỏi thứ hai "How can we do it better?"**: chỉ hỏi "How are we doing?" là chưa đủ.

## Bảng tham chiếu (Reference Tables)
Một số đo lường vận hành chi tiết tác giả gợi ý (ngoài ABCD Checklist):

| Chức năng | Đo gì | Mục tiêu / tần suất |
|---|---|---|
| Master scheduling | Số thay đổi trong emergency zone; rescheduled-in vs -out; vòng quay thành phẩm (MTS) | nhỏ; ~bằng nhau; hằng tuần/hằng tháng |
| MRP | Stockout (make & buy); vòng quay NVL/linh kiện; **exception message volume**; late order release; reschedule-in vs -out | exception ≤10% (fab/assembly); late release ≤5%; hằng tuần, theo planner |
| CRP | Past due load | < 1 tuần công việc; hằng tuần |
| Plant floor control | On-time completion (late jobs in vs out); capacity performance to plan | ±5%; hằng tuần, theo bộ phận |
| Purchasing | Stockout & vòng quay theo supplier/buyer/scheduler; chất lượng, giá | sát 100%/truyền thống |
| Data | Độ chính xác inventory, BOM, routing | sát 100%; hằng tuần |

## Ví dụ minh họa (Worked Example)
Cơ chế vòng lặp đo lường → sửa chữa: ERP operating committee rà ABCD Checklist 2 lần/năm. Với mỗi câu "no", nhóm trả lời ba câu hỏi: (1) nguyên nhân gì gây "no"? (dùng câu hỏi audit chi tiết của checklist để chẩn đoán); (2) cách sửa tốt nhất? (nếu vấn đề trong một bộ phận → giao trưởng bộ phận đó; nếu vượt ranh giới bộ phận → kích hoạt spin-off task force); (3) sửa nhanh thế nào? (đặt ngày cụ thể). Kết quả — điểm số, hạng (A/B/C), các "no", đang làm gì, cần gì từ top management — được chủ tịch luân phiên của operating committee báo cáo chính thức lên executive steering committee (họp ~6 tháng/lần). Vòng lặp "how we're doing / what's causing it / fix by when" chính là động cơ không để ERP tụt hạng.

## Điểm cần nhớ (Key Takeaways)
1. Hai mục tiêu vận hành: đừng để tụt + làm tốt hơn mãi; năm yếu tố: Understanding, Organization, Measurements, Education, Lean.
2. Giữ project team (đổi thành ERP operating committee, chủ tịch luân phiên) và steering committee.
3. Dùng ABCD Checklist Section 5 ≥2 lần/năm; re-certify Class A hằng năm.
4. Đo cả operational lẫn financial; đối chiếu lợi ích thực với cost justification.
5. Giáo dục liên tục là bắt buộc, dệt vào job spec; lãnh đạo mới cần giáo dục nhất.
6. Lean Manufacturing giữ ERP không tụt và còn làm nó tốt hơn (setup ↓ → lot ↓; quality ↑ → safety stock ↓; flow thay job shop → queue & lead time ↓).

## Ứng dụng cho BA ERP (BA Application)
- Đưa các đo lường vận hành (bảng trên) vào phần Reports/KPIs của spec như các báo cáo chuẩn: reschedule-in vs -out, exception message volume (ngưỡng ≤10%), late order release (≤5%), past due load (<1 tuần), capacity-to-plan (±5%), độ chính xác inventory/BOM/routing.
- Thiết kế chức năng theo dõi giáo dục/chứng nhận: liên kết chuẩn ERP tối thiểu với job specification từng vị trí; có thể là một module HR nhỏ (lịch lớp, điểm danh, no-show) — ghi như một yêu cầu hệ thống nếu khách hàng muốn duy trì Class A.
- Mô hình hóa quản trị vận hành: thực thể "operating committee" với vai trò luân phiên, lịch họp (quý/6 tháng), và quy trình xử lý "no answer" (nguyên nhân → owner → due date) — đây là business rule, không chỉ là mô tả tổ chức.
- Nhắc trong NFR: hệ thống cần cấu hình time fence, emergency zone cho master schedule để các đo lường trên có nghĩa.

## Liên hệ (Connects To)
- **Ch 16**: vận hành tốt là bệ phóng cho Phase III (chiến lược).
- **Ch 7**: behavior change — nền tảng cho giáo dục liên tục.
- **Ch 12 & Appendix A**: các chức năng được đo lường ở đây (supplier scheduling, CRP, input-output, MRP).
- **ABCD Checklist for Operational Excellence** (Oliver Wight) — công cụ đo chuẩn ngành.
