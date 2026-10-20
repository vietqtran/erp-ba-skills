# Chương 13: Quick-Slice ERP — Tổng quan (Quick-Slice ERP — Overview)

## Ý tưởng cốt lõi (Core Idea)
**Quick-Slice ERP** — triển khai ERP theo "lát cắt nhanh": thay vì triển khai toàn công ty, chọn một *dòng sản phẩm có tác động lớn* (một "slice" quan trọng của doanh nghiệp), triển khai càng nhiều chức năng ERP càng tốt cho riêng slice đó, và hoàn thành pilot trong khoảng 120 ngày. Đây là cách lấy lại động lực và chứng minh giá trị ERP nhanh, chi phí thấp, rủi ro thấp, lợi ích lớn.

## Framework được giới thiệu (Frameworks Introduced)
- **Three knobs** — ba núm điều chỉnh (nhắc lại từ Ch2): khối lượng công việc, thời gian sẵn có, nguồn lực áp dụng. Giữ cố định hai núm bằng cách thay đổi núm thứ ba.
  - Triển khai *toàn công ty*: cố định work + time, vặn tăng núm *resource* — theo Roger Brooks: "never change the schedule; never change the load; simply add more horse".
  - *Quick-Slice*: vặn *giảm núm work* (chỉ làm một slice nhỏ) vì núm time đã bị vặn xuống ~4 tháng.
- **Quick-Slice approach** gồm 3 bước định nghĩa:
  1. Chọn một product line tác động cao — một slice rất quan trọng.
  2. Triển khai càng nhiều chức năng ERP càng tốt cho sản phẩm đó.
  3. Hoàn thành pilot trong thời gian rất ngắn, ~120 ngày.
- **Ba đòn bẩy làm nên tốc độ** (thu nhỏ critical path): (1) giáo dục tăng tốc chỉ cho người trực tiếp liên quan slice; (2) data integrity chỉ trên item của slice; (3) "software soon" — quyết định phần mềm trong vài ngày, dùng cái đang có hoặc phần mềm PC chi phí thấp.

## Khái niệm chính (Key Concepts)
- **Slice**: một dòng/họ sản phẩm được "cắt ra" để triển khai ERP đầy đủ, trong khi phần còn lại vẫn chạy hệ cũ.
- **Urgency and focus** — khẩn trương và tập trung: tâm thế bắt buộc của đội Quick-Slice ("chạy qua, vòng quanh, hoặc húc đổ chướng ngại"). Thiếu nó, Quick Slice biến thành "Slow Slice".
- **Window of risk** — cửa sổ rủi ro (Roger Brooks: "Time is the ultimate enemy"): triển khai càng lâu càng tốn kém và rủi ro càng lớn.
- **Self-funding / pay as you go**: dự án cải tiến tự trả chi phí bằng lợi ích nó tạo ra — một lý do mạnh để chọn Quick-Slice.

## Mô hình tư duy (Mental Models)
- Khi đánh giá có nên làm Quick-Slice không, *đừng* hỏi "Tại sao nên làm?" mà hỏi **"Why not?"** (tại sao không?) và xuất phát từ đó — vì nó nhanh, rẻ, ít rủi ro, kết quả lớn.
- Ẩn dụ "chiếc Rolls Royce chưa lấy khỏi showroom": nhiều công ty đã mua ES đắt tiền nhưng chưa "lái" được giá trị ra đường — Quick-Slice là cách đưa xe ra đường.
- "Nothing succeeds like success": một thắng lợi sớm trên slice làm hồi sinh nhiệt huyết tốt hơn mọi lời thuyết phục.

## Điều cần tránh (Anti-patterns)
- **"Slow Slice"**: nói lời khẩn trương nhưng không thật sự có urgency và nguồn lực → dự án lụn bại rồi bị bỏ.
- **Để phần mềm làm trễ dự án**: với Quick-Slice, không được phép chờ chọn/cài/nâng cấp ES; dùng cái đang có dù "phần mềm của ta dở" (thường vẫn đủ tốt cho slice).
- **Làm Quick-Slice khi không có slice hợp lý** (sản phẩm/linh kiện/quy trình đan xen chằng chịt, không tách được) hoặc **không tạo được flow manufacturing**.
- **Làm khi thiếu urgency**: Quick-Slice cường độ cao; thiếu áp lực thời gian thì không phải cách tốt.

## Bảng tham chiếu (Reference Tables)
Khi nào Quick-Slice phù hợp / không phù hợp (tổng hợp từ chương):

| Nên cân nhắc Quick-Slice khi | Không nên khi |
|---|---|
| Đã cài ES nhưng không cải tiến quy trình (người kiệt sức) | Không có slice tách được hợp lý |
| Re-implementers (làm lại sau lần thất bại) | Không tạo được flow manufacturing |
| Cần payback nhanh / tự tài trợ | Phải chạy hai hệ thống gây rắc rối (báo cáo/tuân thủ) |
| Middle management "bán lên" (top không quan tâm) | Công ty rất nhỏ (chênh lệch thời gian không đáng kể) |
| Công ty quy mô cực lớn (khó "ôm" cả công ty) | Thiếu urgency |
| Ngành "độc nhất", muốn thấy chạy trước khi đầu tư | Có thể lâu hơn mới tới Class A (về lý thuyết) |
| "Bleeding from the neck" — nguy cơ sống còn, cần cứu nhanh | |

## Ví dụ minh họa (Worked Example)
Phép tính "có thể lâu hơn tới Class A": làm slice 1 (~4 tháng) → slice 2 (~3 tháng, có learning curve) → slice 3 (~3 tháng). Sau ~1 năm công ty đã thu lợi ích lớn nhưng vẫn chưa có tất cả sản phẩm/chức năng trên hệ thống; tại điểm nào đó phải chuyển sang triển khai toàn công ty (thêm 6-12 tháng). Tác giả chấp nhận đánh đổi này để lấy payback sớm. Trường hợp thực tế: Engelhard Industries (Anh) do Andy Coldrick dẫn dắt làm Quick-Slice, chứng minh sức mạnh MRP II cho ban lãnh đạo, sau đó họ dẫn dắt triển khai toàn công ty đạt kết quả Class A.

## Điểm cần nhớ (Key Takeaways)
1. Quick-Slice = chọn một product line tác động cao, triển khai đầy đủ ERP cho nó, hoàn thành pilot ~120 ngày.
2. Dùng mô hình three knobs: ở Quick-Slice vặn *giảm work*, vì *time* đã khóa ở ~4 tháng.
3. Tốc độ đến từ ba đòn bẩy: giáo dục chỉ cho người của slice, data integrity chỉ trên item của slice, quyết phần mềm trong vài ngày.
4. Đánh giá bằng câu hỏi "Why not?"; chỉ bỏ khi thực sự không có slice, không tạo được flow, hoặc thiếu urgency.
5. Không có urgency + nguồn lực thật → Slow Slice → thất bại.

## Ứng dụng cho BA ERP (BA Application)
- Khi lập phạm vi (scope) tài liệu cho một khách hàng lớn hoặc đã có ES, cân nhắc đề xuất phạm vi "slice" đầu tiên thay vì toàn bộ: BA viết spec đầy đủ nhưng chỉ cho một product family tác động cao, các family khác giữ quy trình hiện tại — ghi rõ ranh giới "hai hệ thống" và các vấn đề common-parts sẽ phát sinh.
- Dùng tiêu chí chọn slice (tác động cao, tự chứa, người tốt, ổn định, bài học áp dụng được — chi tiết ở Ch14) làm checklist trong phần "scope & assumptions" của tài liệu yêu cầu.
- Ghi urgency/timebox (120 ngày) như một ràng buộc phi chức năng (NFR) ảnh hưởng tới mức độ chi tiết và số chức năng được đặc tả trong vòng đầu.

## Liên hệ (Connects To)
- **Ch 14**: chi tiết triển khai Quick-Slice (Proven Path điều chỉnh, tiêu chí chọn slice, physical process improvement).
- **Ch 2 (Three knobs)** & **Ch 5 (Proven Path)**: nền tảng khái niệm được tái sử dụng.
- **Appendix B (cells/flow)**: tạo flow manufacturing là điều kiện cho Quick-Slice trong job shop.
