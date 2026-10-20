# Chương 4: Phần mềm (Software)

## Ý tưởng cốt lõi (Core Idea)
Phần mềm là **C-item** (thiết yếu nhưng ít quan trọng nhất), nhưng vẫn có những quyết định lớn. **Enterprise Software (ES)** chuyển công ty từ "nhiều hệ thống đơn giản với giao diện phức tạp" sang "một hệ thống phức tạp với giao diện đơn giản" quanh một **central database**. Chọn và cài ES phải được hoạch định cẩn thận như mọi dự án hàng triệu đô; tiêu chí số 1 là **simplicity/standardization**, không phải độ "sophisticated".

## Framework được giới thiệu (Frameworks Introduced)
- **Ba category về phần mềm** khi làm ERP:
  1. **ES đã cài** → bỏ được bước Software Selection; bước cài chủ yếu là "tweak" lại switch; ứng viên tốt cho Quick-Slice.
  2. **Cài ES đồng thời với ERP** → rất ít công ty thành công; cảnh báo: đánh giá nguồn lực kỹ, nếu không đủ thì làm ERP trước rồi ES.
  3. **Không có ES và không định mua** → dùng hệ thống hiện có nếu chạy được (tham chiếu **MRP II Standard System**), hoặc mua gói ERP/MRP II giá rẻ trên PC (<$100,000).
- **Decision tree chọn hướng (Figure 4-2)**: Muốn làm ERP? → Có ES chưa? → Muốn cài ES không? → Có đủ nguồn lực cho cả ERP+ES? → ra một trong ba kết cục: *Implement ERP using ES* / *Implement ERP and ES simultaneously* / *Implement ERP only (ES maybe later)*.
- **Vòng đời ES 4 bước**: **Selection** (chọn vendor) → **Configuration & Enhancement** (design team đặt switch, xác định enhancement) → **Installation** (chạy thực tế, pilot) → **Ongoing Support** (bảo trì, nâng cấp — không bao giờ "xong").
- **ES Design Teams**: mỗi module (thường 7–10 module: Finance & Accounting, Master Scheduling, HR, Warehouse Management...) có một design team riêng, khác với ERP project team (ERP team lo people+data; ES team lo software+hardware), nên có thành viên chung để đồng bộ.
- **Bolt-on software — 3 loại**: (1) **Resource planning enablers** (MS, MRP... cắm vào hệ thống có sẵn); (2) **Front-end/back-end** (forecasting, S&OP, VMI ở đầu; finite scheduling ở cuối — ít gây khó nhất); (3) **Supply chain optimization / APS** (tinh chỉnh quan hệ cung–cầu chi tiết, mô phỏng mạnh).
- **Managing Requests for Changes — 2 nguyên tắc + quy trình**: xem Worked Example.

## Khái niệm chính (Key Concepts)
- **Central database**: mọi giao dịch trở thành dữ liệu doanh nghiệp tức thời; sổ sách tài chính cập nhật ngay, không trễ qua từng clerk.
- **Switches**: ES chủ yếu được "cấu hình" bằng cách bật/tắt switch điều khiển luồng và bước xử lý dữ liệu; thay đổi nhỏ có thể lan rộng ("một thay đổi vài switch có thể shut down việc giao hàng").
- **Bolt-on**: phần mềm ngoài ES chính/legacy, thường "best of breed"; đánh đổi: giảm tích hợp, thêm file ngoài central DB, tốn công tích hợp + bảo trì.
- **Pockets of excellence**: hệ thống nội bộ hiện có làm tốt một việc (vd shop-floor control) — đừng mù quáng thay bằng module mới kém hơn.
- **"Big Bang"**: bật ES toàn công ty cùng lúc — rủi ro cực cao, có thể là "tiếng nổ của doanh nghiệp sụp đổ".

## Mô hình tư duy (Mental Models)
- **"ES flexible như bê tông khi đổ"** (Chris Gray): linh hoạt lúc cấu hình, nhưng "khi đông cứng thì phải dùng búa khoan mới đổi được" → quyết định cấu hình phải đúng ngay.
- **Trains to one station**: hình dung dữ liệu như hàng ngàn chuyến tàu chạy về một ga (central DB); design team quyết định đặt ghi (switch) ở đâu, dữ liệu rẽ nhánh/định tuyến lại thế nào.
- **Features ≠ Functions**: nhiều feature hơn = phức tạp hơn = nhiều rủi ro hơn, *không* phải dễ triển khai hơn.
- **Simplicity & standardization là "big hitter"**: chuẩn hoá một cách làm toàn công ty quan trọng hơn sự tinh vi.
- **"Don't pioneer"**: phần mềm chưa kiểm chứng = tên bắn vào lưng; yêu cầu thấy gói chạy ở công ty Class A/B.

## Điều cần tránh (Anti-patterns)
- **Big Bang / bật một module toàn công ty cùng lúc**: dù chỉ một module (vd Warehouse) lỗi switch cũng có thể chặn giao hàng toàn tập đoàn.
- **Để đơn vị địa phương kiểm soát IT riêng**: dần xói mòn tính toàn-doanh-nghiệp của ES → nên **central control of IT resources**.
- **Thay đổi internal logic của phần mềm**: luôn là "major", giữ tối thiểu; nhiều thay đổi ở lõi = dấu hiệu chọn sai phần mềm. Dễ nhất là đổi input/output, khó nhất là đổi logic.
- **Mua phần mềm quá sớm (premature)** trước khi học ERP; hoặc **procrastinate** tìm "gói hoàn hảo" (không tồn tại).
- **Cập nhật mọi "new release"**: bỏ qua release mới không phải là tội, trừ khi chắc chắn cần.
- **Dùng bolt-on bừa bãi**: gây hại nhiều hơn lợi; chỉ dùng có chọn lọc cho chức năng cụ thể.

## Bảng tham chiếu (Reference Tables)
Ba category phần mềm và hệ quả:

| Category | Tình huống | Hệ quả triển khai |
|---|---|---|
| 1 | ES đã cài | Bỏ Software Selection; chỉ tweak switch; ứng viên Quick-Slice |
| 2 | Cài ES + ERP đồng thời | Rủi ro cao nhất; cần đánh giá nguồn lực; cân nhắc tách ERP trước |
| 3 | Không có/không mua ES | Dùng legacy nếu chạy được, hoặc gói ERP/MRP II rẻ (<$100k) như bolt-on |

## Ví dụ minh họa (Worked Example)
**Quy trình quản lý yêu cầu thay đổi phần mềm (Managing Requests for Changes)** — hai nguyên tắc rồi năm bước:
- **Principle 1 — Resist isolated changes**: cưỡng lại thay đổi phục vụ nhu cầu cục bộ không thiết yếu.
- **Principle 2 — Always follow a recognized change process**: cách để không vi phạm Principle 1 là có quy trình thay đổi rõ ràng (ai đề xuất, xét gì, ai duyệt). "People can play the game — as long as they play by the rules."

Quy trình 5 bước:
1. IT sẵn sàng thực hiện thay đổi (nội bộ hoặc qua vendor), kinh phí đã nằm trong cost/benefit.
2. Yêu cầu nộp cho **IT trước** để ước lượng khối lượng; phân loại minor/major; IT chỉ nêu khía cạnh kỹ thuật, **không** phán xét tính hợp lệ nghiệp vụ.
3. Yêu cầu chuyển cho **project team**; nếu minor, team quyết cho làm hay dời sang Phase III.
4. Nếu major, project team xét câu hỏi then chốt: *thay đổi này có cần để điều hành kinh doanh và/hoặc để ERP chạy đúng không? Có bắt buộc dùng máy tính hay làm thủ công được?* Nếu cần và phải dùng máy tính → làm ngay/sớm; nếu không → dời Phase III.
5. Nếu người đề xuất bất đồng mạnh với việc bị từ chối → đưa lên **steering committee** nghe hai phía và quyết cuối.

(Q&A: tại P&G, lập trường ban đầu là loại bỏ mọi bolt-on để chuẩn hoá trên ES; nhưng ES vendor không cung cấp đủ chức năng, nên CIO cùng function head quyết bolt-on nào thật sự cần.)

## Điểm cần nhớ (Key Takeaways)
1. Xác định mình thuộc **category phần mềm nào** để biết bước nào bỏ được, bước nào là trọng tâm.
2. Rất ít công ty làm nổi **ERP + ES đồng thời**; nếu nguồn lực không đủ, tách ra.
3. **Pilot trước khi go-live, không Big Bang**; chọn một phần kinh doanh làm live pilot.
4. Chọn phần mềm theo **simplicity/standardization** và yêu cầu reference Class A/B; đừng pioneer.
5. Có **quy trình quản lý thay đổi** chính thức; giữ thay đổi internal logic tối thiểu; cân nhắc bolt-on có chọn lọc.
6. Phần mềm **không bao giờ "xong"**: cần ongoing support và central IT control.

## Ứng dụng cho BA ERP (BA Application)
- Trong spec, tách **tham số cấu hình (switch)** khỏi **yêu cầu enhancement code**: ghi rõ chức năng nào đạt được bằng đặt switch, chức năng nào cần sửa phần mềm (và phân minor/major) — giúp tài liệu "code được ngay".
- Với mỗi module (7–10 module chuẩn: Finance & Accounting, Master Scheduling, Warehouse Management, HR...), xác định **design team/role chủ sở hữu** và các quyết định cấu hình cần chốt.
- Thêm mục **change-control** vào tài liệu: tiêu chí phân loại minor/major và câu hỏi "có cần để điều hành/để ERP chạy đúng không?" làm gate chống thừa chức năng.
- Khi đề xuất **bolt-on**, nêu rõ loại (enabler / front-back-end / APS) và đánh đổi tích hợp + bảo trì; ưu tiên giữ **pockets of excellence** hiện có thay vì thay thế vô cớ.
- Ưu tiên đổi **input/output** hơn đổi **internal logic**; nhiều yêu cầu đổi lõi là tín hiệu sai phần mềm (ghi chú rủi ro này trong tài liệu).

## Liên hệ (Connects To)
- **Chương 1**: ABCs — phần mềm là C-item; phân biệt ERP vs ES.
- **Chương 5**: chi phí phần mềm (ratio 1:8 giữa mua và cài) trong cost/benefit.
- **Chương 7**: business meetings để nhận diện thay đổi cấu hình ES.
- **Chương 11**: conference-room pilot và cutover.
- **Chương 13–14**: Quick-Slice (phù hợp công ty đã có ES).
- **Mission Critical (Davenport)**: nguồn tham khảo về cài ES và bolt-on supply chain.
