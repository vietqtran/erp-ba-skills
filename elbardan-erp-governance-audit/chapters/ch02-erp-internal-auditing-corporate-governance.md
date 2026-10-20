# Chương 2: ERP, Kiểm toán nội bộ và Quản trị công ty (ERP, Internal Auditing and Corporate Governance)

## Ý tưởng cốt lõi (Core Idea)
ERP là một "tác nhân thay đổi" (change agent) tái cấu trúc rủi ro, kiểm soát và vai trò nghề nghiệp trong tổ chức. Chương tổng quan tài liệu cho thấy: ERP làm thay đổi bản chất kiểm soát nội bộ (có thể vừa nới lỏng vừa thắt chặt), đặt ra loại rủi ro mới, và buộc **Internal Audit Function (IAF)** phải mở rộng từ "soi lỗi" sang đảm bảo rủi ro–kiểm soát trên toàn quy trình nghiệp vụ, nếu không muốn mất tính chính danh.

## Framework được giới thiệu (Frameworks Introduced)
- **Định nghĩa ERP của tác giả**: hệ thống quản lý doanh nghiệp dạng gói phần mềm tích hợp theo module, kiểm soát luồng thông tin tích hợp liền mạch xuyên các chức năng, *tối thiểu gồm module tài chính–kế toán* cộng bất kỳ module nào khác, dùng chung một cơ sở dữ liệu.
  - Khi dùng: để xác định phạm vi "một hệ thống có được tính là ERP không" — mức tích hợp là một *continuum* từ các hệ rời rạc đến tích hợp hoàn toàn.
- **Hakim & Hakim (2010) — phân loại rủi ro ERP**: 4 nhóm rủi ro triển khai.
  - *Organisational risks*: mức độ thay đổi cần có, năng lực tái thiết kế quy trình.
  - *Technical skills risks*: thu hút/giữ nhân sự giỏi, đào tạo chéo, chia sẻ tri thức.
  - *System risks*: nhận diện và hiểu các thay đổi cần thiết.
  - *User risks*: khả năng người dùng hiểu hệ thống, phối hợp liên phòng ban, kháng cự thay đổi.
- **COSO Internal Control–Integrated Framework (COSO 2011)**: 5 thành phần kiểm soát nội bộ (xem Bảng tham chiếu).
- **IIA (1999) — định nghĩa kiểm toán nội bộ**: "an independent, objective assurance and consulting activity designed to add value" — hoạt động đảm bảo và tư vấn độc lập, khách quan, nhằm gia tăng giá trị và cải thiện vận hành, qua cách tiếp cận có hệ thống để đánh giá risk management, control và governance.
- **Continuous Auditing (CA)**: kiểm toán và báo cáo thời gian thực, theo kiểu "kiểm toán bằng ngoại lệ" (auditing by exception). Hai phương pháp luận: *embedded audit module* (module kiểm toán nhúng) và *monitoring control layer* (lớp giám sát kiểm soát).

## Khái niệm chính (Key Concepts)
- **Control logic**: logic kiểm soát cài sẵn trong thiết kế ERP, định hình cách kiểm soát được thực thi.
- **Segregation of duties (SoD)**: phân tách nhiệm vụ — nguyên tắc kiểm soát kinh điển; ERP mở rộng phạm vi công việc khiến một số người "quyền lực hơn", mâu thuẫn trực tiếp với SoD.
- **CAAT (Computer-Assisted Auditing Techniques)**: kỹ thuật kiểm toán có máy tính hỗ trợ; cần thiết khi kiểm toán SoD và kiểm soát trong môi trường ERP.
- **Audit trail**: dấu vết kiểm toán — ERP tăng cường audit trail, hỗ trợ tuân thủ và quản trị.
- **Preventive vs detective controls**: kiểm soát phòng ngừa và kiểm soát phát hiện; ERP ảnh hưởng đến tỷ lệ pha trộn hai loại này.
- **Hybridisation**: hiện tượng "lai hóa" vai trò nghề nghiệp (kế toán quản trị trở thành tư vấn kinh doanh) sau ERP.
- **IT governance alignment**: cần căn chỉnh kiểm soát nội bộ + IAF + quản trị công ty + quản trị CNTT để tận dụng giá trị ERP (Chen 2009).

## Mô hình tư duy (Mental Models)
- **Nghịch lý kiểm soát của ERP**: coi ERP vừa có thể *nới lỏng* kiểm soát (mở rộng phạm vi công việc, chấp nhận dữ liệu ngầm định giữa các bước, "không có chỗ kiểm tra dọc đường") vừa có thể *thắt chặt* (tự động hóa kiểm soát, tăng khả năng nhìn thấy hành vi, dữ liệu bất nhất bị gắn cờ). Thiết kế spec phải chủ động chọn và ghi rõ.
- **"An error in one part brings down the entire system"**: do tính phụ thuộc lẫn nhau (interdependency) và dùng CSDL quan hệ, một lỗi/lỗ hổng bảo mật ở một phòng ban có thể gây gián đoạn toàn hệ thống — rủi ro bảo mật trở thành rủi ro toàn cục.
- **IAF giám sát, management thực thi**: ban quản lý triển khai kiểm soát; kiểm toán nội bộ đóng vai trò giám sát (oversight) — ranh giới trách nhiệm rõ ràng.
- **Kiểm soát sau ERP là "chuyện tập thể"**: kiểm soát nội bộ không còn thuộc riêng phòng kế toán mà gồm cả tác nhân con người và tác nhân máy (ERP tự định nghĩa logic kiểm soát — Dechow & Mouritsen).

## Điều cần tránh (Anti-patterns)
- **Phụ thuộc kiểm toán viên bên ngoài cho IT audit**: sau SOX (2002), ngoại kiểm bị cấm nhiều dịch vụ (Section 201) và trách nhiệm tài liệu hóa + đánh giá kiểm soát nội bộ chuyển sang management/nội kiểm (Section 404) — tổ chức không nên trông cậy chính vào ngoại kiểm cho IT audit.
- **"Audit around the computer"**: chỉ kiểm tra đầu vào–đầu ra mà bỏ qua xử lý bên trong hệ thống — lỗi thời trong môi trường ERP tích hợp chặt.
- **Bỏ mặc quan hệ với ERP cho nhóm khác**: nếu một chức năng (kế toán, kiểm toán) bỏ bê mối quan hệ với ERP, nhóm khác sẽ "giành quyền kiểm soát và biến ERP thành hình ảnh của họ".

## Bảng tham chiếu (Reference Tables)
**5 thành phần kiểm soát nội bộ — COSO (2011):**

| Thành phần | Nội dung |
|---|---|
| Control environment | Bầu không khí/nền tảng để cá nhân thực hiện trách nhiệm kiểm soát |
| Risk assessment | Đánh giá các rủi ro tác động xấu đến mục tiêu tổ chức |
| Control process/activities | Hoạt động giúp management xử lý rủi ro |
| Information | Thông tin về rủi ro và hoạt động kiểm soát |
| Communication & monitoring | Truyền thông và giám sát |

## Ví dụ minh họa (Worked Example)
**Vai trò kiểm toán nội bộ trong phân tích & quản lý rủi ro cho tổ chức dùng ERP** (tổng hợp Cerullo & Cerullo 2000; Hespenheide 2007; Madani 2009) — một quy trình có thể biến thành checklist spec:

1. Nhận diện dải rủi ro trong chu trình ERP đang kiểm toán.
2. Kết nối rủi ro đã nhận diện với các ứng dụng/chức năng tiềm năng liên quan.
3. Xác định chi phí hằng năm của mỗi "ERP exposure" (mức phơi nhiễm rủi ro).
4. Chọn kiểm soát nội bộ phù hợp cho từng exposure — ưu tiên kiểm soát *hiệu quả về chi phí* (cost-effective).
5. Tư vấn management về phân bổ nguồn lực tối ưu.
6. Dự liệu và đề xuất phương án ứng phó rủi ro.
7. Cung cấp tư vấn quản lý rủi ro.

Đây là mẫu biến một yêu cầu mơ hồ ("cần kiểm soát rủi ro") thành chuỗi bước có đầu ra rõ ràng cho từng chức năng.

## Điểm cần nhớ (Key Takeaways)
1. ERP luôn kèm rủi ro ở 3 trục: *implementation, technicality, functionality* — đặc biệt rủi ro chức năng do lệch (misalignment) giữa hệ thống và nhu cầu tổ chức (truy cập sai, thiếu bước kiểm tra, định dạng đầu ra sai).
2. Tích hợp làm tăng rủi ro gian lận bởi người dùng có *quá nhiều quyền* (excessive authority) → SoD phải được thiết kế chủ động trong ERP.
3. IAF có 2 hoạt động quản trị cốt lõi: *monitoring risks* và *assurance regarding controls*.
4. Sau ERP, trọng tâm kiểm soát dịch chuyển từ chỉ nghiệp vụ kế toán sang *toàn bộ vận hành kinh doanh* → củng cố quản trị.
5. Nội kiểm là "nhà vô địch" tự nhiên của CA (không bị ràng buộc độc lập như ngoại kiểm theo SOX 201); môi trường ERP đầy đủ chức năng là nơi lý tưởng triển khai CA.

## Ứng dụng cho BA ERP (BA Application)
- Mỗi module/chức năng trong spec phải nêu rõ nó thuộc trục rủi ro nào (triển khai/kỹ thuật/chức năng) và kiểm soát tương ứng — tránh "thừa chức năng" hoặc "thiếu kiểm soát".
- Thiết kế **Segregation of Duties**: liệt kê vai trò nào không được đồng thời nắm (ví dụ nhập liệu + phê duyệt), vì ERP mở rộng phạm vi công việc dễ phá vỡ SoD.
- Dùng 5 thành phần COSO làm khung mô tả kiểm soát cho mỗi chức năng (control environment → monitoring), đảm bảo cover đủ.
- Ghi rõ các điểm "dữ liệu được chuyển sang bước sau với chấp nhận ngầm" và chèn bước re-verification nếu cần — chống lỗ hổng "không kiểm tra dọc đường".
- Spec cần nêu tham số bảo mật/phân quyền theo từng bước xử lý; một lỗ hổng cục bộ có thể lan toàn hệ thống.
- Cân nhắc đưa yêu cầu **Continuous Auditing** (embedded module hoặc monitoring control layer) và **audit trail** vào tài liệu cho các chu trình trọng yếu.

## Liên hệ (Connects To)
- **Ch 1**: Bối cảnh và câu hỏi nghiên cứu về thích nghi của IAF.
- **Ch 3**: Các khía cạnh thực hành/cấu trúc của IAF và lý thuyết thể chế lý giải vì sao IAF thay đổi.
- **COSO, SOX, COBIT, Basel, Turnbull**: các chuẩn mực và luật tạo áp lực quản trị lên IAF.
