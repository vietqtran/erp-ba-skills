# Chương 13: Đào tạo (Training)

## Ý tưởng cốt lõi (Core Idea)
Đào tạo là một trong những vấn đề quan trọng nhất của dự án ERP và là nguyên nhân thất bại thường bị đánh giá thấp nhất: "phần mềm chạy hoàn hảo nhưng nhân viên không biết dùng thì vẫn là thất bại". Training không phải một bước đứng trước/sau go-live mà **gắn vào mọi phần của vòng đời**, và áp dụng cho cả user lẫn implementor (người triển khai).

## Framework được giới thiệu (Frameworks Introduced)
- **FAQ về user training** — bộ câu hỏi định hình kế hoạch đào tạo:
  - **Timing**: quá sớm thì quên, quá muộn thì không kịp và kéo dài stabilization; tính theo khoảng cách tới go-live và thời gian user cần học (Purina Mills bắt đầu trước 4 tháng).
  - **How much**: tùy module; có thể tới 6 tháng để user thành thạo; nhóm tài chính Purina Mills học 7 giờ/ngày trong tháng cuối.
  - **Bù giờ mất vào training**: quản lý làm thêm giờ, user làm hai việc (Microsoft), hoặc dùng nhân viên tạm.
  - **When (trong hay ngoài giờ)**: giờ training phát tín hiệu mức quan trọng — xếp trong giờ = quan trọng, ngoài giờ/cuối tuần = bị coi kém quan trọng, user dễ bỏ buổi và "một buổi lỡ thì phần còn lại thành mờ mịt".
  - **Khuyến khích/ép**: Microsoft coi training là bắt buộc cho user quan trọng, dọa khóa tài khoản (chỉ phải khóa ~20).
  - **Chi phí**: ngân sách training có thể ≥ 10% tổng ngân sách dự án; thường vượt dự toán.
  - **Nội dung (IT hay nghiệp vụ)**: phải trộn technology + process + domain; nếu không sẽ thành "ERP Hokey Pokey" (chỉ dạy bấm nút); nhưng quá chung chung cũng vô dụng ("core... in other words, useless").
  - **Script-based vs general support**: xem mục Reference.
  - **Cấu trúc & super users**: hầu hết có classroom + Internet/CBT/self-study; dùng **"super users"** trong tổ chức khách để dạy lại người khác.
  - **Tăng tốc training**: có thể rút gọn (Microsoft) nhưng nguy hiểm, chi phí thất bại cao; dễ hơn nếu hệ mới giống hệ cũ.
- **Training the Implementor** — người triển khai cũng phải được đào tạo đúng phiên bản phần mềm; đào tạo sai/thiếu dẫn tới thay đổi không cần thiết, chậm và tốn (Dow Corning).

## Khái niệm chính (Key Concepts)
- **Super users**: thành viên tổ chức khách được đào tạo để huấn luyện người khác — tạo buy-in (người quen dạy), cho thấy học hệ thống là quan trọng, và vun hiểu biết ở cấp người dùng.
- **Script-based materials**: tài liệu dẫn user từng bước qua trọn một giao dịch, đặt trên LAN; context-based, kiêm tài liệu hệ thống và FAQ.
- **General support materials**: độc lập ngữ cảnh, liệt kê capability và định nghĩa thuật ngữ, giống "help".
- **"ERP Hokey Pokey"**: training thoái hóa thành dạy thao tác bấm nút không kèm ngữ cảnh nghiệp vụ.
- **Job-based training**: đào tạo theo công việc thực tế, không chỉ học cách dùng phần mềm (tiêu chí trong checklist Deloitte).

## Mô hình tư duy (Mental Models)
- Dùng lịch và giờ training như một **tín hiệu ưu tiên**: muốn user coi trọng thì xếp trong giờ làm.
- Thiết kế training như khóa nghiệp vụ dùng công cụ, không phải khóa công cụ: "khóa 6 giờ nhập journal entry vào SAP cũng là khóa general ledger như là khóa công cụ hệ thống".
- Cân bằng script-based (có ngữ cảnh, tra cứu nhanh) với rủi ro user "hoảng" khi gặp tình huống ngoài script → cần bổ sung năng lực tự tra.

## Điều cần tránh (Anti-patterns)
- **Đánh giá thấp thời gian và chi phí training end user**: "sai lầm dễ mắc nhất"; 43% site nói lượng training là bất ngờ lớn nhất.
- **Training toàn ngoài giờ/cuối tuần**: user coi nhẹ, bỏ buổi, học kém.
- **Training "core" quá chung chung** không bám functionality cụ thể của phiên bản → vô dụng.
- **Chỉ dựa vào script** mà không dạy cách tra cứu → user kẹt khi ra ngoài kịch bản.
- **Không đào tạo implementor đúng phiên bản**: dẫn tới sửa phần mềm oan.

## Bảng tham chiếu (Reference Tables)
Bảng 13.1 — Chi phí training user & triển khai so với dự toán ban đầu (50 công ty lớn Mỹ, 8/1998, Forrester):

| Mức so với dự toán | Tỷ lệ |
|---|---|
| Vượt > 50% | 8% |
| Vượt 10%–50% | 26% |
| Trong khoảng ±10% | 58% |
| Thấp hơn > 10% | 6% |
| Không biết | 2% |

So sánh hai loại tài liệu hỗ trợ:

| | General support | Script-based |
|---|---|---|
| Bản chất | Độc lập ngữ cảnh, như "help" | Dẫn từng bước qua trọn giao dịch |
| Ưu | Bao quát capability, định nghĩa thuật ngữ | Có ngữ cảnh, kiêm tài liệu + FAQ |
| Nhược | Thiếu ngữ cảnh thao tác | User kẹt khi tình huống ngoài script |

## Ví dụ minh họa (Worked Example)
**Dow Corning — đào tạo implementor thiếu hụt** (Ross 1998):
- Đầu 1995 lãnh đạo chốt triển khai SAP R/3 như một phần chương trình reengineering toàn công ty. 6/1995 chọn 40 nhân sự hàng đầu vào implementation team. Vì định tự hỗ trợ SAP in-house, họ **quyết không dùng consultant** → càng cần project member được đào tạo kỹ.
- 9/1995 bắt đầu đào tạo, nhưng phần lớn là trên **SAP R/2**, không chuyển trực tiếp sang R/3. Sau đào tạo, team vẫn không hiểu cách thiết kế quy trình và cấu hình phần mềm → trì hoãn pilot đầu tiên tới tận 3/1997.
- Hệ quả lên chất lượng thay đổi: kế toán định giá giao dịch một kiểu cho quản trị, kiểu khác cho luật định; tưởng SAP không làm được nên viết thêm code để chuyển đổi. Về sau khi đã hiểu rõ quy trình và năng lực thật của SAP, họ nhận ra "sẽ có quy trình tốt hơn nhiều và không phải dùng các thay đổi đã nhét vào SAP". → Thiếu đào tạo implementor trực tiếp sinh ra customization oan.

## Điểm cần nhớ (Key Takeaways)
1. Training gắn vào mọi giai đoạn vòng đời và áp dụng cho cả user lẫn implementor.
2. Căn thời điểm training sát go-live vừa đủ; đừng quá sớm (quên) hay quá muộn (kéo dài stabilization).
3. Nội dung phải trộn công nghệ + quy trình + nghiệp vụ; tránh "ERP Hokey Pokey" và tránh "core" quá chung.
4. Lịch training trong giờ làm là tín hiệu ưu tiên; dùng super users để tạo buy-in và lan tỏa hiểu biết.
5. Đào tạo implementor đúng phiên bản phần mềm; thiếu điều này sinh customization oan, chậm và tốn.

## Ứng dụng cho BA ERP (BA Application)
- Trong spec/triển khai, lập kế hoạch training riêng cho từng module với timing, số giờ, hình thức (classroom/CBT/self-study/super users) và tiêu chí job-based.
- Đặc tả tài liệu hỗ trợ theo hướng **script-based**: dẫn user từng bước qua trọn một giao dịch, đặt trên mạng nội bộ, kiêm luôn tài liệu hệ thống và FAQ — đây cũng là nguồn tốt để viết user story có ngữ cảnh.
- Viết nội dung đào tạo và tài liệu gắn ngữ cảnh nghiệp vụ (vd general ledger) chứ không chỉ liệt kê thao tác, để tài liệu "đủ để làm" chứ không mơ hồ.
- Dự trù ngân sách training ≥ 10% và cảnh báo rủi ro vượt dự toán trong tài liệu dự án.
- Yêu cầu đào tạo implementor/đội cấu hình đúng phiên bản trước khi thiết kế quy trình, để tránh viết yêu cầu customization dựa trên hiểu sai năng lực phần mềm.

## Liên hệ (Connects To)
- **Ch 12**: training đúng lúc quyết định độ dài stabilization; checklist Deloitte yêu cầu job-based training.
- **Ch 9 & Appendix 9-1**: Microsoft ép training (dọa khóa tài khoản), redesign cho nhanh.
- **Ch 11**: Quantum dành 6 tuần training toàn cầu, cấm rút người khỏi lớp.
- **Ch 15**: thiếu training là yếu tố rủi ro/thất bại về con người (personnel).
