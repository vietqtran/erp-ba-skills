# Ngân hàng câu hỏi — tự kiểm & khảo sát khách hàng

## Mục lục
- A. Câu hỏi tự kiểm của agent (bắt buộc & mở rộng)
- B. Kỹ thuật hỏi khách hàng
- C. Câu hỏi khảo sát chung cho mọi dự án ERP
- D. Câu hỏi cho từng chứng từ / nghiệp vụ (dùng lặp lại)
- E. Câu hỏi về danh mục, phân quyền, tham số, báo cáo, tích hợp, dữ liệu, NFR, pháp lý
- F. Câu hỏi theo quy trình & ngành (chỉ dẫn)

---

## A. Câu hỏi tự kiểm của agent

**Bốn câu bắt buộc ở mỗi vòng kiểm (bước 4):**
1. Bạn có thắc mắc hay chưa rõ chỗ nào không?
2. Có chỗ nào cần xác nhận lại không?
3. Đối chiếu với yêu cầu ban đầu, tài liệu output có lệch / thiếu / thừa chỗ nào không?
4. Checklist đã done hết chưa? Template đã điền đủ chưa?

**Câu hỏi mở rộng (dùng khi viết và khi kiểm):**
- Câu này có nguồn không? Nếu khách hàng đọc, họ có nhận ra đây là điều họ đã nói?
- Mình có vừa thêm một con số, một bước, một vai trò mà không ai yêu cầu không?
- Nếu hai dev đọc câu này, họ có code ra hai thứ khác nhau không?
- Chuyện gì xảy ra khi: dữ liệu rỗng, số 0, số âm, vượt hạn mức, trùng lặp, hai người làm cùng lúc, kỳ đã khóa, danh mục bị ngừng dùng, người duyệt nghỉ phép, mạng lỗi khi gọi hệ thống ngoài?
- Hủy/đảo chứng từ này thì cái gì ở module khác phải hoàn tác?
- Vai trò nào được nhìn thấy dữ liệu này, ở phạm vi nào (của mình, phòng ban, chi nhánh, công ty)?
- Giá trị này có thể thay đổi theo khách hàng/thời gian không? Nếu có → tham số, không viết cứng.
- Quy trình chuẩn ERP (file `references/processes/…`) có bước nào mà tài liệu không có? Đó là thiếu, hay khách hàng chủ động bỏ (có nguồn)?
- Cùng khái niệm này ở file khác được gọi/định nghĩa thế nào?

## B. Kỹ thuật hỏi khách hàng

- **Đi từ mở đến đóng:** "Anh/chị mô tả cách đang làm việc X?" → "Vậy đơn trên 50 triệu thì ai duyệt?".
- **Xin mẫu thật:** biểu mẫu, file Excel, ảnh chụp phần mềm cũ, báo cáo đang dùng — mỗi mẫu thành một SRC. Một mẫu thật thay cho mười câu hỏi.
- **Hỏi ngoại lệ:** "Trường hợp nào thì không làm như vậy?", "Nếu người duyệt vắng thì sao?", "Đã bao giờ phải sửa sau khi duyệt chưa?".
- **Định lượng:** "Bao nhiêu đơn mỗi ngày?", "Bao nhiêu dòng mỗi đơn?", "Bao nhiêu người dùng cùng lúc?".
- **Đưa phương án để chọn:** "Khi nhận thiếu hàng: (A) đơn giữ trạng thái nhận một phần chờ giao tiếp, (B) đóng phần còn lại — anh/chị chọn?".
- **Nhắc lại để xác nhận:** diễn đạt lại bằng lời của mình và hỏi "đúng ý anh/chị chưa?" — ghi câu trả lời là DEC.
- **Hỏi đúng người:** quy trình hỏi người làm; quy tắc/hạn mức hỏi người có quyền quyết; hạch toán hỏi kế toán trưởng.
- Ghi mọi câu trả lời vào issue-log kèm nguồn (MTG/email) trước khi sửa tài liệu.

## C. Câu hỏi khảo sát chung cho mọi dự án ERP

**Doanh nghiệp & mục tiêu**
- Mô hình kinh doanh, sản phẩm/dịch vụ chính, kênh bán? Số pháp nhân, chi nhánh, kho, nhà máy, công trường?
- Ba vấn đề lớn nhất hiện nay mà hệ thống mới phải giải quyết? Đo thành công bằng chỉ số nào?
- Đang dùng phần mềm/Excel gì cho từng phần việc? Giữ lại hệ thống nào, thay hệ thống nào?

**Tổ chức & con người**
- Sơ đồ tổ chức, phòng ban, chức danh liên quan? Ai là người quyết định phạm vi và nghiệm thu?
- Số người dùng theo vai trò? Ai làm việc ngoài văn phòng (công trường, kho, xe)?

**Phạm vi & giai đoạn**
- Module nào cần trước, module nào sau? Mốc thời gian, ràng buộc ngân sách?
- Những gì chắc chắn KHÔNG nằm trong phạm vi?

## D. Câu hỏi cho từng chứng từ / nghiệp vụ (lặp lại cho mỗi loại chứng từ)

1. Ai tạo chứng từ? Tạo từ đâu (chứng từ nguồn nào, nhập tay, nhập Excel)?
2. Thông tin bắt buộc trên chứng từ? Có mẫu giấy/Excel hiện tại không (xin mẫu)?
3. Có cần duyệt không? Bao nhiêu cấp, ai duyệt, theo điều kiện gì (giá trị, loại, phòng ban)? Người duyệt vắng thì sao?
4. Sau khi duyệt có được sửa không? Sửa những gì, ai sửa, có phải duyệt lại không?
5. Hủy chứng từ: được hủy ở trạng thái nào, ai hủy, cần lý do không? Chứng từ đã ghi sổ thì xử lý thế nào?
6. Thực hiện một phần (giao/nhận/thanh toán một phần) có xảy ra không? Phần còn lại xử lý ra sao?
7. Đánh số chứng từ: theo mẫu nào, theo chi nhánh/năm, có cần liên tục không?
8. Ngày chứng từ và ngày ghi sổ có khác nhau không? Được lùi ngày không?
9. Chứng từ ảnh hưởng gì: tồn kho, công nợ, sổ cái, ngân sách? Ở thời điểm nào (khi duyệt hay khi ghi sổ)?
10. Đính kèm file? In mẫu nào? Gửi cho ai (nhà cung cấp, khách hàng)?
11. Ai được xem chứng từ của ai (của mình, phòng ban, chi nhánh, toàn công ty)?
12. Cần thông báo/nhắc việc gì, cho ai, qua kênh nào?
13. Khối lượng: bao nhiêu chứng từ/ngày, bao nhiêu dòng/chứng từ?

## E. Câu hỏi theo thành phần

**Danh mục:** mã tự sinh hay tự đặt, quy tắc mã? Ai được tạo/sửa, có duyệt không? Danh mục đã phát sinh giao dịch thì xóa hay ngừng dùng? Có cần nhập từ Excel, đồng bộ từ hệ thống khác? Phân loại/nhóm theo những tiêu chí nào?

**Phân quyền:** vai trò thực tế là gì? Ai được thấy giá vốn, lương, đơn giá? Phân quyền theo chi nhánh/kho/dự án? Có ai vừa tạo vừa duyệt không (rủi ro SoD)? Hạn mức duyệt theo giá trị?

**Tham số:** ngưỡng, tỷ lệ, chính sách nào doanh nghiệp muốn tự thay đổi mà không cần lập trình? Thay đổi có hiệu lực theo ngày không?

**Báo cáo:** báo cáo này giúp ra quyết định gì, ai xem, bao lâu một lần? Lọc theo gì, nhóm theo gì? Có mẫu hiện tại không? Số liệu tính theo ngày chứng từ hay ngày ghi sổ, gồm chứng từ ở trạng thái nào? Xuất Excel/PDF? Báo cáo bắt buộc nộp cơ quan nào?

**Tích hợp:** hệ thống nào cần kết nối (hóa đơn điện tử, ngân hàng, chấm công, website/sàn TMĐT, phần mềm cũ)? Dữ liệu gì, chiều nào, bao lâu một lần? Khi lỗi thì ai xử lý?

**Chuyển đổi dữ liệu:** dữ liệu nào cần chuyển (danh mục, số dư đầu kỳ, chứng từ dở dang)? Ngày chốt số liệu? Ai làm sạch dữ liệu?

**NFR:** số người dùng đồng thời, khối lượng giao dịch, giờ cao điểm? Truy cập từ đâu (mobile, ngoài văn phòng)? Yêu cầu sao lưu, thời gian khôi phục tối đa? Cloud hay máy chủ riêng? Chính sách bảo mật, dữ liệu cá nhân?

**Pháp lý & kế toán:** chế độ kế toán áp dụng? Phương pháp tính giá xuất kho? Đơn vị cung cấp hóa đơn điện tử? Kê khai thuế theo tháng hay quý? Kỳ khóa sổ? Các đặc thù hạch toán của ngành?

## F. Câu hỏi theo quy trình & ngành

Mỗi file quy trình chuẩn có mục **14 — Lỗi BA hay mắc & câu hỏi cần hỏi khách hàng**, mỗi file ngành có mục **10 — Câu hỏi khảo sát**. Khi chuẩn bị buổi họp về quy trình nào, lấy câu hỏi từ file tương ứng:
- Mua hàng → `references/processes/p2p-procure-to-pay.md` §14
- Bán hàng → `references/processes/o2c-order-to-cash.md` §14
- Kho → `references/processes/inventory-warehouse.md` §14
- Sản xuất → `references/processes/manufacturing-mrp.md` §14
- Kế toán tổng hợp, công nợ, tiền, tài sản, thuế, giá thành, ngân sách → các file tương ứng trong `references/processes/`
- Nhân sự – tiền lương → `references/processes/hr-payroll.md` §14
- Xây dựng / Logistics / Phân phối → `references/industries/<ngành>.md` §10
