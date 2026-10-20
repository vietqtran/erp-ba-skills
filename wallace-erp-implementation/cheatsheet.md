# Cheatsheet — ERP: Making It Happen (Wallace & Kremzar)

Trang tra nhanh: ngưỡng, cây quyết định, bảng đánh đổi, quy tắc "Khi X → làm Y (vì Z)". Dùng khi thiết kế chức năng ERP chuẩn và viết spec code-ready.

## Ngưỡng & con số chuẩn (thresholds)

| Hạng mục | Ngưỡng / con số | Ghi chú |
|---|---|---|
| Lịch triển khai company-wide | >1 năm, <2 năm (≈**18 tháng**) | >2 năm: xác suất thành công giảm mạnh |
| Phase I Basic ERP | ~9–12 tháng | Phase II: 3–6 tháng; Phase III: liên tục |
| Quick-Slice pilot | ~**120 ngày** (~4 tháng) | pilot = cutover |
| Inventory on-hand accuracy | **≥95%** min (đẩy 98–99%) | item# + qty + location trong counting tolerance |
| BOM / routings / open orders | **≥98%** | unforgiving data |
| Counting tolerance (Class A) | **0–5%**, không vượt 5% | cho hàng cân/đong |
| Standards (trong routing) | ±10% | forgiving data |
| Critical mass đào tạo trước go-live | **≥80%** (lý tưởng 100%) | phần còn lại ngay sau |
| Product families cho họp S&OP | ~6–12 | S&OP ~8 tháng để chạy ổn |
| Tỷ lệ chi phí phần mềm : cài đặt | **1 : 8** | systems & programming ≈ 5× giá phần mềm |
| Supplier scheduling Pareto | ~20% nhà cung cấp = ~80% khối lượng | cut over nhóm này trước; mục tiêu 100% |
| MRP exception messages (job shop) | ≤10% | thước đo vận hành |
| Late order releases | ≤5% | |
| CRP past-due load | <1 tuần công việc | |
| Capacity-to-plan | ±5% | |
| reschedule-in vs reschedule-out | ≈ bằng nhau | lệch lớn = lịch tồi |
| Lợi ích khảo sát (TB / Class A) | CS +15%/+26%; direct labor +11%/+20%; purchase cost −7%/−13% | 11 nhóm lợi ích |

## Cây quyết định lớn

**Hướng triển khai (company-wide vs Quick-Slice)**: Đã có ES & chưa cải tiến / cần payback nhanh / công ty cực lớn / "bleeding from the neck" → **Quick-Slice** (nếu có slice tách được + tạo flow + có urgency). Ngược lại → **company-wide**.

**Phần mềm**: Muốn làm ERP? → Có ES chưa? → Muốn cài ES? → Đủ nguồn lực cho cả ERP+ES? → *Implement ERP using ES* / *ERP + ES đồng thời* (rủi ro cao) / *ERP only, ES sau*.

**Thời điểm Finance & Accounting**: Đủ nguồn lực làm đồng thời? → có: đồng thời. → không: có lý do bắt buộc F&A trước? → có: F&A trước. → không: **resource planning trước** (lợi ích cạnh tranh lớn nhất ở planning/scheduling).

**Yêu cầu thay đổi phần mềm**: minor → project team quyết (làm/Phase III). major → "cần để điều hành business / ERP chạy đúng? cần máy tính hay thủ công được?" → nếu không bắt buộc → **Phase III**. Bất đồng mạnh → steering committee.

**Chiến lược cutover**: planning/scheduling → **pilot** (computer → conference room → live), KHÔNG big bang. Accounting → **parallel** được.

## Bảng đánh đổi

**Company-Wide vs Quick-Slice** (Three Knobs)

| | Company-wide | Quick-Slice |
|---|---|---|
| Three knobs | cố định work+time, **xoay resource** | cố định resource+time, **giảm work** |
| Thời gian | ~18 tháng | ~120 ngày/slice |
| Phạm vi | mọi chức năng, toàn công ty | 1 product line, hầu hết chức năng |
| F&A | có | bỏ (dùng hệ cũ + bridge) |
| Rủi ro / payback | cao hơn / chậm hơn | thấp / sớm, self-funding |

**Job Shop vs Flow Shop**

| | Job shop | Flow shop |
|---|---|---|
| Nhóm nguồn lực theo | loại giống nhau (functional) | trình tự quy trình |
| Lập lịch | back scheduling + dispatch list + CRP + input-output | danh sách trình tự từ MS/MRP |
| Routing | riêng từng item, nhiều nguyên công | thường suy từ layout; nếu có, 1 nguyên công |
| Thời gian triển khai ERP | dài hơn | ngắn hơn (vài tháng) |

**3 loại pilot**: Computer (HW/SW, dummy→volume) → Conference room (education, data giả, "play Murphy") → Live (chạy thật, **user sign-off**).

**Forgiving vs Unforgiving data**: Unforgiving (cần chính xác cao) = inventory, open orders, allocations, BOM, routings. Forgiving (chỉ cần hợp lý) = lead time, order qty, safety stock, standards, forecasts.

## Quy tắc quyết định (Khi X → Y, vì Z)

**Khái niệm & phạm vi**
- Tách **ERP (quy trình/con người)** khỏi **ES (phần mềm)** ngay đầu tài liệu — phần lớn "ERP failure" chỉ là cài ES mà không đổi quy trình.
- Lập lịch/viết spec **theo business function, không theo module** — tránh sai trình tự (MRP trước master schedule) và sai thông điệp.
- Phase I chỉ nhận **have-to's**; dồn nice-to's sang II/III — chống scope creep.
- Chức năng đặc thù ngành không có trong package → hỏi **4 câu** (còn làm sau ERP? thiết yếu? trong hay ngoài ERP? nếu ngoài xử lý sao), đừng kết luận "không cần".

**Chuẩn bị & biện minh**
- Học (first-cut education) **trước** khi cost-justify — nếu không sẽ ước thấp cả chi phí lẫn lợi ích.
- Nghi ngờ số → ước **chi phí cao, lợi ích thấp**; đừng cost-justify chỉ bằng giảm tồn kho (sai thông điệp).
- Phải cắt ngân sách → cắt **C (computer)**, giữ **A (people)**.
- Bất kỳ câu readiness nào (financial/resource/priority/emotional) = "no" → **đừng Go**, sửa trước.

**Tổ chức & con người**
- Project leader: **nội bộ, nền vận hành, toàn thời gian** (run-over-by-a-train test); không thuê ngoài, không lấy từ phòng systems.
- Consultant: chỉ chọn người có **Class A experience thật**.
- GM từ chối học ERP → chuyển **Quick-Slice** (thay đổi hiếm khi chảy ngược lên).
- **Đừng train trước khi educate** (what/why trước how).
- Lịch dự án: người chịu trách nhiệm tự lập, **ghi tên người cụ thể** (không chức danh).

**Planning & dữ liệu**
- S&OP: phần mềm không hỗ trợ **vẫn phải làm** (spreadsheet) — bỏ S&OP = "preordained to less than total success".
- Multiplant → **staggered**; nhưng S&OP làm **đồng loạt & sớm**.
- Dữ liệu dưới ngưỡng (tồn 95%, BOM/routing 98%) → **đừng bật** MS/MRP/DRP (sai số lan qua BOM explosion → mất niềm tin).
- Đạt 95% tồn kho → **bỏ annual physical inventory**.

**Go-live & chuỗi cung ứng**
- Đừng **vượt live pilot** tới khi "works" + user sign-off.
- Đừng delay cutover chờ mốc kế toán → dựng **bridging program**.
- Cutover: tồn kho tụt quá nhanh → release sớm, đừng **starve the sources**.
- Job shop: lập lịch theo thứ tự **dispatching → CRP → input-output**.
- **Finite scheduling → để Phase III** (chỉ hữu ích khi due date đã hợp lệ).
- Hàng mua **criticality cao** (bất kể cost) → đối tác dài hạn; **criticality thấp + cost thấp** → Web/spot.

**Vận hành**
- Giữ **project team (→ operating committee) + steering committee** sau go-live — không process Class A/B nào tự duy trì.
- ABCD "no" vượt ranh giới bộ phận → **spin-off task force**; luôn đặt **ngày sửa**.
- Thay lãnh đạo cấp cao → **bắt buộc** giáo dục ERP, ghi vào job spec.

## Tín hiệu cảnh báo (tells & smells)

- Gọi ES là "ERP", hoặc spec chỉ mô tả cấu hình phần mềm → thiếu phần quy trình/con người.
- Lịch dự án theo tên module vendor → sắp sai trình tự.
- Nhiều forecast song song (Sales/Marketing/Finance mỗi nơi một con số) → chưa có S&OP thật.
- Nhiều yêu cầu đổi **internal logic** phần mềm → dấu hiệu chọn sai phần mềm.
- Nhiệt tình/ownership không tăng trong business meetings → change process đang hỏng.
- "We're unique, ERP không hợp" → thường do chưa được giáo dục đúng.
- Tài liệu chỉ mô tả happy path, không có feedback/anticipated delay → thiếu closed loop.

## Dùng cho BA ERP (mapping nhanh)

- **Master data bắt buộc**: MRP cần BOM + inventory; CRP cần routing + work center/thời gian nguyên công. Thiếu → không code được.
- **Mỗi chức năng** cần: roles (ai đổi gì ở time zone nào) · parameters (order qty, safety stock/time, scrap/shrinkage, time fences, hedges) · feedback flows · performance measurements · business rules (vd "master schedule reconcile với S&OP").
- **Acceptance**: Implementers' Checklist Yes/No; ngưỡng dữ liệu định lượng; go-live gate có steering committee authorization + user sign-off.
- **Reports/KPI**: reschedule-in≈out, exception ≤10%, late release ≤5%, past-due <1 tuần, capacity-to-plan ±5%, accuracy inventory/BOM/routing.
