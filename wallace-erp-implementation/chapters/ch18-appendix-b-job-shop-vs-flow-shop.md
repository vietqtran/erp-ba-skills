# Chương 18: Phụ lục B — Định dạng tổ chức xưởng: Job Shop và Flow Shop (Appendix B — Plant Floor Organization Formats: Job Shop versus Flow Shop)

## Ý tưởng cốt lõi (Core Idea)
Có hai cách cơ bản để tổ chức xưởng sản xuất: **job shop** (nhóm nguồn lực theo *loại giống nhau*) và **flow shop** (nhóm nguồn lực theo *trình tự trong quy trình*). Vấn đề không phải ở sản phẩm (đặc chế hay tiêu chuẩn) mà ở *cách tổ chức nguồn lực*. Trong hầu hết trường hợp, flow vượt trội job shop, và xu thế chung của ngành sản xuất là chuyển sang flow — điều này ảnh hưởng trực tiếp tới độ phức tạp và thời gian triển khai ERP.

## Framework được giới thiệu (Frameworks Introduced)
- **Job Shop** — "a form of manufacturing organization where the resources are grouped by like type" (nguồn lực nhóm theo loại giống nhau). Tên khác: *functional form of organization*, *single-function departments*. Ví dụ kinh điển: machine shop (tất cả máy tiện một khu, máy khoan khu khác, máy phay khu khác). Công việc di chuyển từ work center này sang work center khác theo **routing** riêng của từng item; nhiều job shop có hàng chục tới hàng trăm nguyên công trong một routing.
- **Flow Shop** — "a form of manufacturing organization where the resources are grouped by their sequence in the process" (nguồn lực nhóm theo trình tự quy trình). Tên khác: *process layout*. Ví dụ: nhà máy lọc dầu, một số sản xuất hóa chất, dây chuyền lắp ráp ô tô, dây chuyền chiết rót hàng tiêu dùng, hoặc một **manufacturing cell**.
- **Cellular manufacturing** — sản xuất theo ô/tế bào: cách chuyển từ job shop sang flow; còn gọi là flow lines, demand pull lines, kanban lines.

## Khái niệm chính (Key Concepts)
- **Back scheduling** — lập lịch lùi: trong job shop, *mỗi* nguyên công phải được lập lịch chính thức qua quy trình phức tạp này, rồi gom theo work center, sắp theo ngày hoàn thành nguyên công, và truyền xuống xưởng qua **dispatch list** (lặp ≥1 lần/ngày).
- **Dispatch list** — danh sách điều độ: sản phẩm của back scheduling, cho xưởng biết thứ tự ưu tiên job theo work center.
- **Routing trong flow shop**: nhiều flow shop *không* dùng routing chính thức trong máy tính vì routing đã được định nghĩa bởi cách bố trí thiết bị; nếu có, routing thường chỉ *một* nguyên công ("make the product").
- **FIFO** (first in, first out): bản chất của flow — job vào quy trình theo thứ tự nào thì ra theo thứ tự đó (trừ khi có sự cố).
- Cùng một item: trong job shop với routing 10 nguyên công cần *10 lịch* lập/duy trì qua back-scheduling; trong flow chỉ cần *1 lịch*.

## Mô hình tư duy (Mental Models)
- Một *sản phẩm* không quyết định job hay flow — *cách tổ chức nguồn lực* mới quyết định. (Nhà máy dược làm viên nén/viên nang có bộ phận đơn chức năng granulating/compressing/coating/filling = job shop; nhưng dây chiết rót-đóng gói của cùng nhà máy đó = flow.)
- "Flow means FIFO, flow means fast, FIFO và fast means simple schedules" — lịch flow thường chỉ là danh sách trình tự đơn giản lấy thẳng từ master schedule hoặc material plan (MRP).
- Flow = đơn giản: dễ hiểu, trực quan hơn, kiểm soát bằng mắt, feedback tức thời, cần công cụ lập lịch/kiểm soát đơn giản hơn nhiều.

## Điều cần tránh (Anti-patterns)
- **Đồng nhất "job shop" với "làm hàng đặc chế"**: sai — job shop cũng làm hàng tiêu chuẩn lặp đi lặp lại (ví dụ dược phẩm, theo yêu cầu FDA).
- **Đứng yên ở job shop khi đối thủ chuyển sang flow**: "it's too good not to do it" — ở đâu có thể, nên chuyển sang flow, nếu không sẽ gặp rắc rối cạnh tranh.

## Bảng tham chiếu (Reference Tables)
So sánh (Figure B-1 job shop, Figure B-2 flow shop — bị flatten khi extract; hình minh họa sản phẩm A/B/C chạy qua các production department):

| Tiêu chí | Job Shop | Flow Shop |
|---|---|---|
| Nhóm nguồn lực theo | Loại giống nhau (functional) | Trình tự quy trình |
| Routing | Riêng từng item, nhiều nguyên công | Thường định bởi layout; nếu có, 1 nguyên công |
| Số lịch cần lập (item 10 công đoạn) | 10 (qua back scheduling) | 1 |
| Lead time | Dài hơn | Ngắn hơn, nhanh hơn |
| Tồn kho (WIP & khác) | Lớn hơn | Nhỏ hơn (ít không gian, ít tiền, ít lỗi thời) |
| Material handling | Nhiều | Ít (ít rủi ro hư hại, tăng năng suất) |
| Công nhân gắn với sản phẩm | Thấp | Cao (tinh thần & cải tiến tốt hơn) |
| Ưu điểm được cho là của hình thức | Tận dụng thiết bị cao, linh hoạt | Đơn giản, nhanh, kiểm soát trực quan |
| Thời gian triển khai ERP | Dài hơn | Ngắn hơn (có thể vài tháng) |

## Ví dụ minh họa (Worked Example)
**Nhà máy dược vừa là job shop vừa là flow shop** — ví dụ chủ đạo của chương: khu làm viên nén/viên nang có các bộ phận đơn chức năng (granulating → compressing → coating → capsule filling); routing của sản phẩm quyết định đường đi (viên nén đi qua compressing, viên nang thì không; một số viên nén được coating, số khác không) → đây là *job shop* dù họ làm sản phẩm tiêu chuẩn lặp lại. Ngược lại, khu chiết rót-đóng gói của cùng nhà máy là *flow shop*: mỗi line gồm các thiết bị rất khác nhau xếp theo trình tự chính xác (máy rửa chai → máy chiết → máy nhồi bông → máy đóng nắp → máy dán nhãn → máy đóng thùng). Họ *không* gom tất cả máy nhồi bông vào một góc như layout job shop — làm vậy sẽ chậm, kém hiệu quả, lãng phí không gian. Cách chuyển job shop → flow: tạo manufacturing cell (chuyên dụng hóa + xếp liền kề theo dòng), liên kết bằng kanban.

## Điểm cần nhớ (Key Takeaways)
1. Job shop nhóm nguồn lực theo loại; flow shop nhóm theo trình tự quy trình — phân loại theo *tổ chức nguồn lực*, không theo sản phẩm.
2. Job shop cần back scheduling từng nguyên công + dispatch list; flow shop dùng danh sách trình tự đơn giản từ master schedule/MRP.
3. Flow thường vượt trội: nhanh hơn, tồn kho ít, ít material handling, trực quan, đơn giản hơn.
4. Chuyển job → flow bằng cellular manufacturing (cells/kanban lines).
5. Triển khai ERP ở flow shop thuần nhanh hơn job shop tương đương vài tháng.

## Ứng dụng cho BA ERP (BA Application)
- Xác định sớm trong tài liệu khách hàng là job shop hay flow shop (hoặc hỗn hợp theo khu) — vì nó quyết định bộ chức năng lập lịch phải đặc tả: job shop cần **routing nhiều nguyên công, back scheduling, dispatch list, CRP, input-output control**; flow shop cần lịch trình tự đơn giản (có thể không cần routing chính thức trong hệ thống).
- Khi dữ liệu routing là master data phụ thuộc: với job shop phải đặc tả routing chi tiết; với flow shop ghi rõ routing có thể chỉ một nguyên công hoặc được suy từ layout — tránh áp mô hình job shop lên flow một cách máy móc.
- Đặc tả tùy chọn chuyển đổi/cell (kanban, demand pull line) nếu khách hàng đang migrate từ job sang flow — ảnh hưởng tới cách hệ thống phát lệnh sản xuất.
- Dùng khác biệt thời gian/độ phức tạp này để ước lượng phạm vi tài liệu: phần job shop sẽ có nhiều chức năng/diagram lập lịch hơn flow shop tương đương.

## Liên hệ (Connects To)
- **Ch 12**: job shop vs flow shop quyết định trình tự triển khai plant scheduling (Phase II).
- **Ch 14**: physical/conceptual cells & kanban để tạo flow trong Quick-Slice.
- **Appendix A**: routing, work center, plant scheduling, CRP.
- **Just-in-Time: Making It Happen** (William A. Sandras, Jr.) — tham chiếu tác giả nêu cho cells/kanban.
