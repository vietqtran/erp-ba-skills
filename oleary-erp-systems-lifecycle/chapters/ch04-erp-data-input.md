# Chương 4: Nhập liệu đầu vào trong ERP (ERP Data Input)

## Ý tưởng cốt lõi (Core Idea)
ERP đẩy việc nhập liệu về *điểm phát sinh dữ liệu* (operations), thay cho mô hình legacy lọc qua kế toán. Thay đổi *ai nhập, nhập ở đâu, nhập bao nhiêu lần, khi nào nhập* tạo ra lợi ích nhưng cũng sinh **user resistance** (chống đối người dùng) và có thể làm chậm nhập liệu. BA phải cân bằng lợi ích tích hợp với chi phí nhập liệu và thiết kế kiểm soát đầu vào chặt.

## Framework được giới thiệu (Frameworks Introduced)
- **Five Reengineering Sources of Data-Input Benefit/Cost** — năm nguồn thay đổi nhập liệu khi tái cấu trúc theo ERP (theo Hammer 1990):
  - (1) **Gather data once** — nhập một lần: chi phí thấp, mọi người "cùng một trang"; rủi ro: nếu sai thì mọi người dùng đều sai, không còn dự phòng ⇒ phải có data input controls và process maps.
  - (2) **Gather more data** — thu thập nhiều dữ liệu hơn (dạng chi tiết, để hệ tổng hợp khi sinh báo cáo).
  - (3) **Gather data straight into the computer** — nhập thẳng vào máy, bỏ khâu giấy.
  - (4) **Gather data where it is generated** — nhập tại nơi phát sinh (loading dock thẳng vào general ledger).
  - (5) **Gather data with a process focus** — nhập theo quy trình liên chức năng thay vì theo chức năng.
  - Khi nào dùng: đánh giá lợi ích vs chi phí và rủi ро chống đối cho mỗi thay đổi nhập liệu.
- **Screens-to-Transactions Model of Implementation Difficulty** — mô hình độ khó triển khai theo số màn hình × số giao dịch:
  - Khi nào dùng: dự báo rủi ro nhập liệu khi chuyển từ legacy sang ERP.
  - Cách làm: so tỉ lệ số màn hình ERP / số màn hình legacy, nhân với khối lượng giao dịch. Tỉ lệ cao (Hydro Agri 6:1) + khối lượng lớn (30.000 đơn) ⇒ triển khai rất khó trừ khi giảm số màn hình.
  - Tỉ lệ màn hình còn là thước đo "fit" giữa phần mềm và quy trình: tỉ lệ lớn ⇒ quy trình tổ chức và quy trình phần mềm lệch nhau.

## Khái niệm chính (Key Concepts)
- **User resistance**: chống đối do thay đổi người/cách nhập liệu; ảnh hưởng chi phí và thành bại triển khai.
- **Event triggers** (SAP): các sự kiện xác định khi nào cần thu thập dữ liệu — ví dụ hoạt động bán hàng, nhận hàng từ PO, đặt giữ vật tư, xuất hàng, transfer posting, điều chuyển kho, xuất hàng cho lệnh sản xuất.
- **"Designed from the database out, not the user interface in"**: thiết kế ERP ưu tiên CSDL, giao diện làm sau — nguyên nhân khó dùng.
- **Window thrashing**: liên tục nhảy qua lại bàn phím/chuột và nhiều cửa sổ, giảm năng suất.
- **"Seat" cost**: giá ERP tính theo số người dùng (ghế), nên dễ sử dụng ảnh hưởng doanh thu vendor.

## Mô hình tư duy (Mental Models)
- Coi "nhập một lần" là con dao hai lưỡi: loại dư thừa nhưng cũng loại luôn "người quét dọn" (AR gọi nhắc) — nên kiểm soát đầu vào phải thay thế vai trò phát hiện lỗi đã mất.
- Nếu một chức năng cần nhiều màn hình hơn hẳn hệ cũ, hãy nghi ngờ "fit": có thể quy trình và phần mềm lệch nhau.
- Mặc định nhập thẳng tại nguồn, nhưng kèm đánh giá năng lực người nhập (công nhân bốc dỡ không phải kế toán) và nhu cầu đào tạo/giao diện phụ trợ.

## Điều cần tránh (Anti-patterns)
- **Thiết kế không ưu tiên giao diện người dùng**: "designed from the database out" làm nhập liệu chậm, tăng chống đối.
- **Bỏ bước xác nhận giao dịch mà không nhắc người dùng**: ví dụ A-dec — tồn kho không giảm vì người dùng không được nhắc sang màn xác nhận.
- **Không lường số màn hình tăng khi khối lượng giao dịch lớn**: dẫn tới mất đơn hoặc phải điều nhân sự IT đi nhập liệu.
- **Giả định dữ liệu sai sẽ được phát hiện**: trong ERP không có dự phòng, dữ liệu sai có thể không bao giờ bị phát hiện.

## Bảng tham chiếu (Reference Tables)
Năm nguồn lợi ích/chi phí do nhập liệu (Table 4.1) và hệ quả cho spec:

| Thay đổi nhập liệu | Lợi ích | Chi phí / rủi ro cần kiểm soát |
|---|---|---|
| Nhập một lần | chi phí thấp, dữ liệu nhất quán | sai một chỗ sai toàn hệ ⇒ cần input controls |
| Nhập nhiều dữ liệu hơn | hỗ trợ quyết định tốt hơn | tăng chi phí thu thập |
| Nhập thẳng vào máy | bỏ sao chép giấy | khó cho người ít kinh nghiệm máy tính |
| Nhập tại nguồn | dữ liệu chính xác hơn, bớt khâu trung gian | người nhập không phải kế toán ⇒ cần đào tạo/UI |
| Nhập theo quy trình | mô hình doanh nghiệp rộng hơn | đổi trình tự/người nhập ⇒ chống đối |

## Ví dụ minh họa (Worked Example)
**Hydro Agri (Canada)** — trước khi dùng SAP R/3, xử lý một đơn của nông dân mất ~20 giây trên một màn hình duy nhất của hệ tự xây. Sau R/3: ~90 giây trên *sáu* màn hình. Với ~30.000 đơn mỗi 4 tuần, tổng thời gian nhập tăng từ 600.000 giây lên 2.700.000 giây mỗi 4 tuần — tới mức nhân sự IT phải đi nhập đơn, và giám đốc thông tin gọi đây là nguy cơ "showstopper".

Áp mô hình độ khó: tỉ lệ màn hình 6:1 × khối lượng 30.000 ⇒ vùng "rất khó triển khai". Đây cũng là tín hiệu *lack of fit* giữa quy trình hiện tại và phần mềm. Giải pháp Hydro Agri chọn: *không* tùy biến R/3 lõi mà xây một ứng dụng trung gian giữa R/3 và người dùng để đơn giản hóa và gộp truy cập. **Bài học cho BA**: khi tỉ lệ màn hình cao + khối lượng lớn, phải chủ động đề xuất giảm/gộp màn hình hoặc lớp UI phụ trợ ngay trong spec, kèm ước tính thời gian nhập liệu như một tiêu chí nghiệm thu.

## Điểm cần nhớ (Key Takeaways)
1. Lợi ích nhập liệu luôn đi kèm user resistance; spec phải nêu biện pháp giảm chống đối (đào tạo, UI phụ trợ).
2. "Nhập một lần" bắt buộc đi kèm **data input controls** vì không còn dự phòng phát hiện lỗi.
3. So số màn hình ERP vs legacy nhân khối lượng giao dịch để dự báo độ khó và đo "fit".
4. Mô hình firm chuyển từ function-focus sang process-focus bằng event triggers.
5. Ease of use là tiêu chí đánh giá ERP, nhưng "dễ dùng" mang tính chủ quan.

## Ứng dụng cho BA ERP (BA Application)
- Với mỗi màn hình nhập liệu, đặc tả rõ **data input controls** (ràng buộc, kiểm tra, bắt buộc xác nhận) — vì dữ liệu sai nhập một lần sẽ lan toàn hệ thống.
- Ghi vào spec *ai* nhập (vai trò ở điểm phát sinh, không mặc định là kế toán), *ở đâu*, *bao nhiêu lần* — đây là thông tin role/quyền mà tài liệu ERP cần có.
- Ước tính số màn hình và thời gian nhập mỗi giao dịch; nếu tỉ lệ so với hệ cũ cao, đề xuất gộp màn hình hoặc lớp UI trung gian ngay trong tài liệu.
- Dùng danh sách **event triggers** làm checklist điểm bắt dữ liệu cho quy trình liên chức năng, đảm bảo không bỏ sót sự kiện cần ghi nhận.
- Thêm "bước xác nhận" tường minh vào luồng nếu hành động không tự hoàn tất (bài học A-dec), tránh lỗi nghiệp vụ âm thầm.

## Liên hệ (Connects To)
- **Chương 2**: thiết kế "từ database ra" bắt nguồn từ ưu tiên CSDL quan hệ.
- **Chương 3**: artifacts (chứng từ) chính là dữ liệu đầu vào/ra.
- **Chương 5**: đầu ra/báo cáo là mặt kia của luồng dữ liệu.
- **Chương 9**: fit giữa quy trình và phần mềm — đổi quy trình hay đổi phần mềm.
