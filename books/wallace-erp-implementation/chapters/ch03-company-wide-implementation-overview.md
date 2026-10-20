# Chương 3: Triển khai Toàn Công ty — Tổng quan (Company-Wide Implementation—Overview)

## Ý tưởng cốt lõi (Core Idea)
Cách "nuốt con voi" ERP toàn công ty mà vẫn xong trong ~18 tháng: chia dự án thành vài **phase lớn làm tuần tự (serial)**, trong mỗi phase lại làm **nhiều task song song (simultaneous)**. Lập lịch **theo chức năng nghiệp vụ (business function), không theo module phần mềm**. ERP là bộ công cụ đã có sẵn — việc của bạn là dùng nó, không phải thiết kế lại.

## Framework được giới thiệu (Frameworks Introduced)
- **Mô hình 3 phase**:
  - **Phase I — Basic ERP** (~9–12 tháng): S&OP, demand management, Rough-Cut Capacity Planning, master scheduling, MRP, plant scheduling (nếu phù hợp), các ứng dụng finance/accounting cần thiết, cùng inventory accuracy, BOM accuracy/structure, kích hoạt feedback loop từ xưởng và mua hàng.
  - **Phase II — Supply Chain Integration** (~3–6 tháng): mở rộng ERP ra chuỗi cung ứng — về phía nhà cung cấp (supplier scheduling, B2B e-commerce) và về phía khách hàng (**Distribution Requirements Planning (DRP)**, **Vendor Managed Inventories (VMI)** / Continuous Replenishment).
  - **Phase III — Extensions & Enhancements** (vài tháng tới >1 năm): phần finance/accounting còn lại, liên kết các đơn vị toàn cầu, HR, bảo trì, product development; và các "nice-to" như full simulation, APS, MES, supplier rating system.
  - Tổng dự án ~1 năm tới 2–3 năm. Phase I chặt chẽ nhất, II kém hơn, III "free form" nhất.
- **"Schedule by function, not software modules"**: business function là việc cần làm để điều hành; software module chỉ hỗ trợ thực thi. Lập lịch theo module (theo khuyến nghị vendor) sai vì hai lý do: **sequence** (vd cài MRP trước master scheduling là ngược) và **message** (gửi sai thông điệp rằng ERP là dự án máy tính).
- **"Cut the cloth to fit the pattern"** — ERP là bộ công cụ tổng quát nhưng phải may đo theo công ty. Các tình huống đặc thù: flow shops, financials-already-integrated, re-implementers, ES/No-ERP, multiplant, multiple business units, necessary nonstandard functions.
- **Multiplant: 3 cách** — Serial / Simultaneous / Staggered (xem Worked Example).

## Khái niệm chính (Key Concepts)
- **Phase**: khối công việc lớn làm tuần tự, phase sau thường phụ thuộc phase trước hoàn tất.
- **Scope creep**: đưa task không thiết yếu vào Phase I; phải giữ thái độ cứng rắn "chỉ làm have-to's, dồn nice-to's sang Phase II/III".
- **Time zero**: điểm bắt đầu tính đồng hồ (sau các bước sơ bộ); nguyên tắc: dành đủ thời gian học+đồng thuận trước, rồi khi đã quyết thì chạy quyết liệt.
- **Flow shop vs job shop**: flow shop (process hoặc repetitive) thường không cần shop-floor dispatching theo từng công đoạn hay detailed CRP — có thể làm capacity ở mức rough-cut (xem Appendix B).
- **Necessary nonstandard functions**: chức năng đặc thù ngành (lot traceability của dược, kế toán hợp đồng quốc phòng, shelf life hàng tiêu dùng) — không được giả định "không có trong phần mềm nghĩa là không cần".

## Mô hình tư duy (Mental Models)
- **"Swallow the elephant one chunk at a time"** — nhưng vẫn "make deliberate haste": chia nhỏ để tiêu hoá được, song song hoá để kịp ~18 tháng.
- **Đặt công cụ hoạch định cơ bản vào sớm**: supplier scheduling vô nghĩa nếu chưa có due date hợp lệ (từ MRP); MRP vô nghĩa nếu chưa có master schedule hợp lệ (cân bằng với S&OP) → đó là lý do các chức năng này nằm Phase I.
- **ERP như GAAP**: cấu trúc ERP là "cho sẵn"; đừng tái phát minh double-entry bookkeeping; tập trung vào *cách dùng* công cụ cho tốt nhất.

## Điều cần tránh (Anti-patterns)
- **Time Wasters**: (1) "Document the current system in detail" và (2) "Design the new system" — khi làm như bước riêng biệt là lãng phí. Hệ thống cũ sắp bị thay; bộ công cụ mới đã được thiết kế (là ERP).
- **Lập lịch quanh module phần mềm** theo vendor: làm chậm dự án, giảm xác suất thành công, gửi sai thông điệp.
- **Serial cho multiplant lớn**: 4 nhà máy × 15 tháng = 60 tháng (5 năm) — quá dài, không chấp nhận được.
- **Giả định "không có trong package nghĩa là không cần"** cho các chức năng đặc thù bắt buộc.

## Bảng tham chiếu (Reference Tables)
Nội dung và thời lượng 3 phase:

| Phase | Tên | Nội dung chính | Thời lượng |
|---|---|---|---|
| I | Basic ERP | S&OP, demand mgmt, RCCP, master scheduling, MRP, plant scheduling, finance cốt lõi, inventory/BOM accuracy, feedback loops | 9–12 tháng |
| II | Supply Chain Integration | Supplier scheduling, B2B e-commerce, DRP, VMI/CR | 3–6 tháng |
| III | Extensions & Enhancements | Finance còn lại, liên kết đơn vị toàn cầu, HR, bảo trì, APS, MES, simulation, supplier rating | vài tháng – >1 năm |

## Ví dụ minh họa (Worked Example)
**Công ty Jones — 4 nhà máy**, muốn triển khai ERP cả bốn:
- **Serial**: xong hẳn nhà máy 1 rồi mới tới 2, 3, 4 → ~60 tháng. *Quá dài, loại.*
- **Simultaneous**: làm cả 4 cùng lúc → xong trong 15 tháng, nhưng quá tải nguồn lực tập trung (IS, quản trị dự án) và đụng catch-22 (ERP không phải ưu tiên 1).
- **Staggered** (được chọn nhiều nhất): lệch pha nhau, xong ~24 tháng cho 4 nhà máy. Ưu điểm: (1) phủ toàn công ty khá nhanh; (2) giảm tải nguồn lực tập trung; (3) chỉ 1 nhà máy pilot/cutover MS+MRP tại một thời điểm; (4) nhân sự nhà máy sau học từ nhà máy trước.
- **Lưu ý quan trọng**: dù staggered, **S&OP vẫn triển khai đồng loạt và sớm** — vì S&OP chỉ hiệu quả khi chạy toàn business unit, không tốn nhiều nguồn lực, độc lập với phần mềm, và là early win. Một công ty đã đưa cả 9 nhà máy từ time-zero lên Class A trong <3 năm bằng staggered.

## Điểm cần nhớ (Key Takeaways)
1. Chia dự án thành **phase tuần tự**, trong mỗi phase chạy **task song song**.
2. **Lập lịch theo business function, không theo software module.**
3. Giữ Phase I chỉ gồm **have-to's** của Basic ERP; dồn nice-to's sang II/III để tránh scope creep.
4. Multiplant: ưu tiên **staggered**; nhưng S&OP luôn làm đồng loạt và sớm.
5. Không lãng phí thời gian tài liệu hoá hệ thống cũ chi tiết hay "thiết kế hệ thống mới" như bước riêng.

## Ứng dụng cho BA ERP (BA Application)
- Tổ chức backlog/tài liệu **theo phase (I/II/III)** và **theo chức năng nghiệp vụ**, kèm ràng buộc phụ thuộc (vd master scheduling phải có trước MRP, MRP trước supplier scheduling) — đây là thứ tự đúng để spec không bị mâu thuẫn.
- Với mỗi chức năng đặc thù ngành (dược: lot traceability; FMCG: shelf life; quốc phòng: contract accounting), đặt 4 câu hỏi của sách: việc này có tiếp tục sau ERP? có thiết yếu? sẽ xử lý trong ERP hay ngoài? nếu ngoài thì làm sao? — và ghi câu trả lời vào tài liệu.
- Tránh viết tài liệu kiểu "triển khai module X": mô tả nghiệp vụ và luồng, rồi mới ánh xạ sang module/switch phần mềm.
- Không dành effort cho "tài liệu hiện trạng chi tiết"; thay vào đó chỉ xác định phần nào của vận hành hiện tại cần hoà vào ERP.

## Liên hệ (Connects To)
- **Chương 2**: Proven Path và Three Knobs (nền cho cách chia phase).
- **Chương 5, 6, 7**: chi tiết các bước đầu, project launch, và initial education được nhắc tới cuối chương.
- **Chương 11–12**: pilot/cutover Phase I và Supply Chain Integration Phase II.
- **Appendix B**: phân biệt job shop / flow shop.
