# Chương 12: Lên sóng — Tích hợp chuỗi cung ứng (Phase II) (Going on the Air — Supply Chain Integration (Phase II))

## Ý tưởng cốt lõi (Core Idea)
Phase II mở rộng ERP ra toàn bộ **supply chain** — chuỗi cung ứng: nhà máy, nhà cung cấp, trung tâm phân phối (DC) và khách hàng, triển khai theo đúng trình tự đó. Khác với Phase I, thứ tự các process ở đây linh hoạt hơn, nhưng quy tắc **ABCs of implementation** vẫn tuyệt đối: con người là hạng mục A, dữ liệu là B, phần cứng/phần mềm là C — nên giáo dục và toàn vẹn dữ liệu vẫn là điều kiện sống còn.

## Framework được giới thiệu (Frameworks Introduced)
- **Supply Chain Integration sequence** — trình tự tích hợp chuỗi cung ứng: (1) trong nội bộ nhà máy → (2) ngược về nhà cung cấp → (3) xuôi tới DC → (4) xuôi tới khách hàng.
  - Khi dùng: lập kế hoạch triển khai giai đoạn 2, sau khi Basic ERP (Phase I) đã chạy ổn.
- **Plant scheduling cho flow shop vs job shop** — lập lịch xưởng:
  - Flow shop: lấy đơn trực tiếp từ MS/MRP, chuyển thành lịch (finishing/final assembly schedule). Pilot ngắn theo một line/cell. Có thể "tăng tốc" (opportunity to accelerate) đưa vào Phase I.
  - Job shop: triển khai theo thứ tự cố định **(1) Shop floor control (dispatching) → (2) Capacity Requirements Planning (CRP) → (3) Input-output control**. Lý do: dispatching khẩn cấp nhất (truyền priority thay đổi xuống xưởng); input-output phải theo sau CRP vì nó đo thực tế so với kế hoạch năng lực.
- **Finite scheduling** — lập lịch hữu hạn: kết hợp lập lịch chi tiết và hoạch định năng lực thành một công cụ, mô phỏng tương tác để người lập lịch chọn phương án tốt nhất. Khi dùng: khi bài toán lập lịch phức tạp. **Luôn triển khai ở Phase III**, không phải II hay I, vì nó ngốn thời gian/nguồn lực và dễ làm trễ cả dự án ERP.
- **Purchased Item Characteristics matrix** — ma trận đặc tính hàng mua (xem Bảng tham chiếu): quyết định hàng nào mua qua đối tác dài hạn, hàng nào mua spot/Web.
- **Supplier Scheduling** — lập lịch nhà cung cấp: thay thế chu trình purchase requisition + hard-copy PO bằng lịch giao hàng hằng tuần dựa trên MRP.
- **DRP (Distribution Requirements/Resource Planning)**: "little DRP" lập lịch bổ sung tồn kho tại DC; "big DRP" thêm lập kế hoạch cước vận tải, không gian và nhân lực tại DC.
- **VMI (Vendor Managed Inventories)** / Continuous Replenishment (CR): "supplier scheduling đảo ngược" — nhà cung cấp tự chịu trách nhiệm bổ sung tồn kho hàng của mình tại kho khách hàng.

## Khái niệm chính (Key Concepts)
- **"Silence is approval"** — im lặng nghĩa là đồng ý: khi không thể đạt lịch, người thực thi *phải* chủ động phản hồi (feedback) lên trên; im lặng = cam kết đạt lịch. Đây không phải module phần mềm mà là quá trình giao tiếp người-với-người (anticipated delay report, họp trạng thái hằng ngày).
- **Plant data collection** — thu thập dữ liệu xưởng: không nhất thiết phải tự động hóa; giấy-bút vẫn chạy được closed-loop MRP. Bar coding hấp dẫn vì đơn giản, đã kiểm chứng.
- **Bill of distribution** — danh mục phân phối: tương tự bill of material, cho biết sản phẩm nào tồn tại DC nào (dữ liệu nền cho DRP).
- **Forgiving vs unforgiving data**: trong DRP, bản ghi tồn kho và các bill phải cực chính xác (unforgiving).
- **Collaborative forecasting** — dự báo cộng tác: chia sẻ dự báo giữa nhà cung cấp và khách hàng để đạt một dự báo thống nhất, dẫn dắt kế hoạch bổ sung; là bước trung gian giữa "làm như cũ" và VMI.
- **Audit/Assessment III**: điểm vào Phase III, trả lời "tiếp theo nên làm gì?" (đối xứng với Audit I "nên làm gì trước?").

## Mô hình tư duy (Mental Models)
- Coi nhà cung cấp "giống như work center trong job shop": một nhà cung cấp cung nhiều item thuộc nhiều product family khác nhau → thường phải có hầu hết sản phẩm trên MS/MRP mới tạo được lịch đầy đủ cho họ. Đây là lý do supplier scheduling thuộc Phase II.
- Phân biệt **warehouse** (nơi chứa nhiều hàng — nơi hàng hư hỏng, lỗi thời) với **distribution center** (nhận rồi chuyển nhanh tới khách; lý tưởng là cross-dock).
- Quy tắc "pilot trong pilot" cho DRP: pilot = một DC; mini-pilot = khoảng một tá sản phẩm trong DC đó.

## Điều cần tránh (Anti-patterns)
- **Triển khai finite scheduling ở Phase I/II**: rủi ro làm trễ toàn bộ dự án ERP.
- **Gọi nhà cung cấp vào nói ERP tuyệt vời trong khi due date trên PO vẫn sai như cũ**: phải tự lo "nhà mình" (dữ liệu, due date hợp lệ) trước khi đòi nhà cung cấp thay đổi lớn.
- **Tưởng module "purchasing" của ES là supplier scheduling**: phần lớn ES chỉ tự động hóa requisition và in PO — mục tiêu đúng là *loại bỏ* requisition và hard-copy PO, không phải tự động hóa chúng.
- **Bỏ qua Audit/Assessment III** vì "hết đau rồi, thấy tuyệt vời rồi": là rủi ro cao, khiến đà cải tiến chết yểu.
- **Quên feedback khi lên sóng plant scheduling**: không có feedback thì không có closed loop.

## Bảng tham chiếu (Reference Tables)
Figure 12-2 — Ma trận đặc tính hàng mua (trục: Criticality cao/thấp × Cost of the item cao/thấp). Văn bản mô tả 4 góc phần tư:

| | Criticality CAO | Criticality THẤP |
|---|---|---|
| **Cost CAO** | IV: High criticality, high cost → đối tác dài hạn | II: Low criticality, high cost → có thể một phần qua Web |
| **Cost THẤP** | III: High criticality, low cost... *(xem ghi chú)* | I: Low criticality, low cost → ứng viên tự nhiên để mua qua Web |

Ghi chú: phần trích flattened khi extract nên nhãn góc III/IV bị lệch; nguyên tắc rõ ràng của tác giả là: hàng *criticality cao* (bất kể cost) cần quan hệ đối tác dài hạn, không mua "one-night stand" trên Web; hàng *criticality thấp + cost thấp* (góc I) là ứng viên tự nhiên để mua Web/spot. Cost chỉ là một trong nhiều yếu tố quyết định tầm quan trọng của item.

## Ví dụ minh họa (Worked Example)
Quy trình triển khai **Supplier Scheduling** 8 bước mà tác giả đi qua:
1. Thiết lập cách tiếp cận (hợp đồng mở hay cố định kỳ hạn? supplier scheduler báo cáo cho ai? còn giữ số PO không?).
2. Có được phần mềm — có thể phải tự viết (nhiều ES không có đúng chức năng); tin tốt: chủ yếu là lập trình truy xuất-và-hiển thị từ file sẵn có.
3. Phát triển giáo dục cho nhà cung cấp — chương trình thường 1 ngày: ERP, cách MRP tạo/duy trì due date hợp lệ, time fence, feedback, "silence is approval", win-win.
4. Pilot với một/vài nhà cung cấp (khối lượng lớn, hợp tác, gần). Giáo dục + đào tạo + cut over ngay trong cùng buổi.
5. Tinh chỉnh quy trình, bắt đầu đo hiệu suất giao hàng/tồn kho.
6. Giáo dục & cut over các nhà cung cấp lớn (nhóm ~20% nhà cung cấp cung ~80% khối lượng — quy tắc Pareto), theo nhóm 3-6 nhà cung cấp/ngày.
7. Đo hiệu suất (của cả nhà cung cấp lẫn của chính mình — lịch mình tồi thì không thể trách họ). Nâng "high bar" rồi nâng tiếp.
8. Giáo dục & cut over các nhà cung cấp còn lại; mục tiêu 100% hàng sản xuất trên supplier scheduling.

VMI dùng con đường 8 bước tương tự nhưng vượt ranh giới công ty và thường do *khách hàng* quyết định cách/thời điểm.

## Điểm cần nhớ (Key Takeaways)
1. Tích hợp chuỗi cung ứng theo trình tự: nội bộ nhà máy → nhà cung cấp → DC → khách hàng; ABCs vẫn chi phối (người > dữ liệu > phần mềm).
2. Job shop lập lịch theo thứ tự cứng: dispatching → CRP → input-output; flow shop lấy lịch thẳng từ MS/MRP (đơn giản hơn, có thể tăng tốc vào Phase I).
3. Finite scheduling để dành Phase III.
4. Supplier scheduling nhằm *loại bỏ* requisition/PO giấy, không tự động hóa chúng; đi 8 bước, pilot trước, Pareto 80/20.
5. DRP có little (bổ sung tồn kho DC) và big (thêm cước/không gian/nhân lực); pilot một DC, mini-pilot một tá sản phẩm.
6. Đừng bỏ Audit/Assessment III — đó là cửa vào Phase III.

## Ứng dụng cho BA ERP (BA Application)
- Khi viết spec module Mua hàng, phân biệt rõ hai mô hình: *purchase requisition/PO truyền thống* và *supplier scheduling* (lịch giao theo MRP, hợp đồng dài hạn) — và chỉ định điều kiện mỗi mô hình áp dụng cho loại item nào theo ma trận criticality × cost.
- Đặc tả quy trình feedback ("silence is approval"): anticipated delay report phải là một chức năng/luồng bắt buộc, có role gửi (xưởng, mua hàng) và role nhận (master scheduler/planner) — không coi nó là tính năng "có thì tốt".
- Với phân phối, mô hình hóa **bill of distribution** như một thực thể dữ liệu riêng (sản phẩm × DC) và chỉ rõ các field dữ liệu cho little DRP (forecast, lead time bổ sung, safety stock, on-hand, in-transit) và big DRP (trọng lượng, kích thước, số sản phẩm/pallet, nhân lực DC, thời gian nhận/pick-pack-ship).
- Thiết kế chức năng VMI/CR như luồng vượt ranh giới hai tổ chức: cần đặc tả quyền xem tồn kho/nhu cầu của đối tác và ai sở hữu tồn kho tại thời điểm nào.
- Đặt chỉ số đo lường đối xứng (reschedule-in ≈ reschedule-out; đo cả hiệu suất nhà cung cấp lẫn chất lượng lịch của chính công ty) vào phần báo cáo của spec.

## Liên hệ (Connects To)
- **Ch 11 (Phase I)**: Phase II nối tiếp Basic ERP; feedback link lập ở Phase I cần được củng cố.
- **Ch 16 (Phase III)**: Audit III dẫn vào Phase III (chiến lược, zero inventory, Internet/B2B).
- **Appendix A**: định nghĩa chuẩn supplier scheduling, DRP, plant scheduling, input-output control.
- **Appendix B**: job shop vs flow shop — nền tảng cho khác biệt lập lịch ở chương này.
