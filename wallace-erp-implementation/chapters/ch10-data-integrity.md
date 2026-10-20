# Chương 10: Tính toàn vẹn dữ liệu (Data Integrity)

## Ý tưởng cốt lõi (Core Idea)
"Garbage in, garbage out" vẫn đúng: phải xây nền dữ liệu chính xác **trước** khi bật các công cụ planning/scheduling của ERP — "accurate numbers before, not during or after". Dữ liệu chia hai loại: **unforgiving** (không khoan nhượng, cần độ chính xác cao) và **forgiving** (khoan nhượng, chỉ cần hợp lý). Dồn công sức vào loại unforgiving.

## Framework được giới thiệu (Frameworks Introduced)
- **Forgiving vs Unforgiving Data** — dữ liệu khoan nhượng vs không khoan nhượng.
  - Unforgiving (cần chính xác cao): inventory balances, production orders, purchase orders, allocations, bills of material, routings (trừ standards).
  - Forgiving (chỉ cần hợp lý): lead times, order quantities, safety stocks, standards, demonstrated capacities, forecasts.
- **4 yếu tố đạt độ chính xác tồn kho** — (1) **zero-defects attitude** (con người: người kho hiểu mình quan trọng); (2) **limited access** (phần cứng: khoanh vùng/khóa — mục đích chính là "giữ accountability bên trong", không phải chặn người); (3) **good transaction system** (phần mềm: đơn giản, <một tá loại giao dịch, phản ánh thực tế, xử lý trong 24h); (4) **cycle counting** (cơ chế).
- **Cycle Counting** — đếm xoay vòng, kiểm tra chất lượng liên tục "hộp đen có khớp thực tế không". 4 mục tiêu: (a) tìm & loại nguyên nhân lỗi (ngừa hơn chữa — "rotten apple"); (b) đo kết quả (% chính xác); (c) sửa bản ghi sai (đếm lại để xác nhận); (d) bỏ kiểm kê toàn bộ hằng năm (annual physical inventory). Có **control group** ~100 item đếm mỗi tuần.
- **Ba phương pháp tính độ chính xác BOM** — **tight** (sai một quan hệ = cả BOM = 0); **loose** (tính từng quan hệ 1-1); **middle-of-the-road** (tính theo quan hệ component-to-parent ở từng cấp) — phổ biến nhất, nhất quán là then chốt.
- **Change-only-what's-necessary** — khi triển khai chỉ thay đổi những gì tuyệt đối cần để chạy được; đừng cải tiến phụ, vì (1) change đã khó với con người, (2) càng thay nhiều càng khó chẩn đoán khi lỗi.

## Khái niệm chính (Key Concepts)
- **Counting tolerance** — dung sai đếm cho hàng cân/đong (fasteners, chất lỏng); tiêu chí: giá trị item, tần suất/khối lượng dùng, lead time, mức trọng yếu (criticality); Class A dùng 0–5%, không vượt 5%.
- **95% accuracy (inventory)** — 95% số dư trong máy khớp thực tế về item number + quantity + location (trong counting tolerance). Là mức tối thiểu, nên đẩy lên 98–99% (95→98 = giảm 60% rủi ro lỗi).
- **Shipment stopper test** — tiêu chí BOM completeness: item nào thiếu sẽ chặn giao hàng thì phải có trong BOM trước go-live; hàng tiêu chuẩn mua ngoài thì thêm sau, không để trên critical path.
- **Modular / Planning Bills** — BOM dạng module cho sản phẩm nhiều option, phục vụ forecasting, master scheduling, order promising; cho phép forecast ở cấp model thay vì từng SKU.
- **Integrated BOM** — một BOM hợp nhất cho cả engineering/manufacturing/cost, không mỗi phòng một "quyển thánh ca".
- **Range and pain** — cách đặt planned queue cho work center: range (biến động việc đến) và pain (thiệt hại khi hết việc).

## Mô hình tư duy (Mental Models)
- "Scratch where it itches" — dồn nguồn lực vào đúng chỗ đau: công ty ít part/nhiều volume thì khổ với production order accuracy; nhiều part/ít volume thì khổ với on-hand balance (A Tale of Two Companies).
- Limited access là để "keep accountability in": trao cho người kho quyền kiểm soát ra/vào thì mới quy trách nhiệm được.
- Đơn vị đếm quan trọng: độ chính xác tính theo units, không theo dollars (lỗi dollar cộng trừ triệt tiêu, lỗi unit đứng một mình).
- Forecast sẽ không bao giờ siêu chính xác (không ai đoán được tương lai); nên tăng khả năng chịu lỗi dự báo bằng demand management tốt hơn, lead time ngắn hơn, forecast ở cấp cao hơn.

## Điều cần tránh (Anti-patterns)
- **Bật master scheduling/MRP/DRP khi dữ liệu chưa đạt ngưỡng** → kế hoạch sai lan truyền qua BOM explosion → mất niềm tin → quay lại hot list → thất bại.
- **Lắp limited access mà không báo trước** → người expedite mất công cụ làm việc, tinh thần sụp đổ.
- **Dùng quá nhiều transaction type** chỉ vì phần mềm có → hệ thống phức tạp, khó giữ chính xác.
- **Giữ annual physical inventory khi đã ≥95%** → thường làm bản ghi kém chính xác hơn, phá accountability và tinh thần người kho.
- **Thay đổi không cần thiết lúc triển khai** → khó chẩn đoán lỗi, triển khai thêm khó.
- **BOM tách rời theo phòng ban** → không thể "hát cùng một bản nhạc".

## Bảng tham chiếu (Reference Tables)
Ngưỡng chính xác trước go-live:

| Dữ liệu | Ngưỡng | Loại |
|---|---|---|
| Inventory balances (on-hand) | ≥95% (đẩy 98–99%) | Unforgiving |
| Scheduled receipts / allocations | ≥95% (open orders ≥98%) | Unforgiving |
| Bills of material | ≥98% | Unforgiving |
| Routings: operations, sequence, work centers | ≥98% | Unforgiving |
| Standards (trong routing) | ±10% | Forgiving |
| Counting tolerance | 0–5% | — |
| Item data / work center data | "reasonable" | Forgiving |
| Forecasts | không bao giờ siêu chính xác | Forgiving |

Phương pháp audit/sửa: BOM — floor audit, office/factory review, product teardown, unplanned issues/receipts. Routings — floor audit, office/factory review, order close-out.

## Ví dụ minh họa (Worked Example)
Tính độ chính xác BOM (Figure 10-2/10-3). Cấu trúc: Product X ← Assembly A (1/) + Item L (2/); Assembly A ← Item B (1/), Item C (2/), Item D (4/); Item L ← Raw material Q (10/). Giả sử chỉ một quan hệ sai: A thực ra cần 5 Item D (không phải 4).
- **Tight method**: cả BOM của X bị tính là miss → 0% accuracy cho sản phẩm đó.
- **Loose method**: 6 quan hệ 1-1 (D→A miss; B→A, C→A, A→X, Q→L, L→X hit) → 5/6 = 83%.
- **Middle-of-the-road**: xét theo nhóm component tới từng parent (A→X: miss vì A sai; L→X: hit) → 67%.
Chọn middle-of-the-road và giữ nhất quán để biết đang cải thiện hay thụt lùi.

Q&A: một công ty máy móc phức tạp, ~60.000 part number, chỉ 55% chính xác tồn kho vào tháng 1, dự kiến go-live tháng 4. Sau khi thay materials manager và tập trung xử lý, giữa tháng 3 đã đạt và duy trì >95% ở cả 4 kho; pilot và cutover đúng hạn. "It can be done."

## Điểm cần nhớ (Key Takeaways)
1. Đạt độ chính xác dữ liệu TRƯỚC go-live; không bật planning/scheduling khi chưa đạt ngưỡng.
2. Phân loại forgiving vs unforgiving và dồn công sức vào unforgiving.
3. Tồn kho: 95% min (item+qty+location trong counting tolerance), đạt bằng 4 yếu tố zero-defects / limited access / transaction đơn giản / cycle counting (control group ~100 item/tuần).
4. BOM ≥98%, chọn một phương pháp đo (ưu tiên middle-of-the-road) và giữ nhất quán; BOM phải complete (shipment-stopper), structured (modular/planning bills), integrated (một bản thống nhất).
5. Routings ≥98% cho operations/sequence/work centers; standards chỉ cần ±10%.
6. "Change only what's necessary": dùng lại số liệu đang có, chỉ sửa cái rõ ràng sai, tinh chỉnh sau go-live.

## Ứng dụng cho BA ERP (BA Application)
- Tài liệu migration/data-integrity phải gắn ngưỡng chấp nhận định lượng cho từng đối tượng dữ liệu (tồn kho ≥95%, BOM/routings/open orders ≥98%), kèm định nghĩa "accuracy" (khớp những trường nào) và counting tolerance — biến chúng thành acceptance criteria nghiệm thu được.
- Khi đặc tả master data (item master, BOM, routing, work center), phân loại rõ field nào unforgiving (bắt buộc verify kỹ) vs forgiving (chỉ cần hợp lý), tránh tài liệu yêu cầu độ chính xác quá mức cho dữ liệu forgiving.
- Đặc tả cycle counting như một chức năng chuẩn: control group, confirming recount, báo cáo %accuracy, loại bỏ nguyên nhân lỗi (không chỉ sửa bản ghi) — kèm role người kho + audit độc lập từ accounting.
- Business rule nền: planning/scheduling không được bật nếu dữ liệu dưới ngưỡng; BOM phải hợp nhất toàn công ty (một nguồn sự thật) — đưa vào mục ràng buộc dữ liệu/kiến trúc.
- Thiết kế transaction system theo "less is more": chỉ định các transaction type thực sự cần (in/out × planned/unplanned, transfer, adjustment, backflush), xử lý trong 24h — tránh spec thừa chức năng từ danh mục mặc định của phần mềm.
- Áp dụng "shipment stopper test" để phân loại ưu tiên: dữ liệu/chức năng nào chặn go-live thì bắt buộc, phần còn lại không để trên critical path — giúp tránh tài liệu thừa/trễ.

## Liên hệ (Connects To)
- **Ch 8/9**: dữ liệu chính xác là tiền đề cho S&OP, master scheduling, MRP; policies định nghĩa parameters (safety stock, order quantity...).
- **Ch 11**: go-live Basic ERP chỉ được tiến hành khi data integrity đạt ngưỡng.
- **Ch 2**: three knobs (work/time/resource) khi phải dựng modular bills hoặc routings/standards còn thiếu.
- **Ch 16**: giảm nhu cầu tồn kho qua thay đổi quy trình.
- **Data migration / master data governance**: liên hệ chuẩn kiểm thử chất lượng dữ liệu và một-nguồn-sự-thật trong tài liệu BA.
