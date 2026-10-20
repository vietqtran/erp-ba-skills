# Chương 11: Triển khai ERP — Big Bang hay Theo giai đoạn (Implementing ERP Systems: Big Bang versus Phased)

## Ý tưởng cốt lõi (Core Idea)
Hai cách triển khai ERP đối lập: **big bang** (bật toàn bộ bộ module tại mọi địa điểm cùng lúc, chỉ trong vài ngày) và **phased** (triển khai từng module hoặc từng nhóm module, thường từng địa điểm một). Không cách nào tối ưu tuyệt đối — lựa chọn là mô hình tình huống (contingency) theo quy mô, độ phức tạp, cấu trúc/kiểm soát của tổ chức và phạm vi triển khai (số module × mức tùy biến).

## Framework được giới thiệu (Frameworks Introduced)
- **Big Bang** — quy trình ba bước: (1) chọn/dựng gần như toàn bộ process và artifact vào phần mềm; (2) test từng module và test interface giữa các module (lỗi phát hiện làm feedback để sửa); (3) tắt hệ cũ, bật hệ mới. Đòi hỏi lượng test khổng lồ trước go-live (Quantum: 6–8 tháng test cho 17 module tại 23 site, cutover ~1 tuần).
  - Khi nào dùng: tổ chức nhỏ/ít phức tạp, cấu trúc phẳng + kiểm soát lỏng (khó duy trì cam kết suốt phased), ít module và ít thay đổi, hoặc khi cần tính năng cross-module ngay (ATP).
- **Phased** — triển khai tuần tự: thiết kế–phát triển–test–cài từng "lát" module, phải duy trì legacy và **temporary interface** ở mỗi pha (Siemens: 3 pha SAP, pha 1 là finance/controlling/AR/AP/purchasing).
  - Khi nào dùng: tổ chức lớn/phức tạp, cấu trúc nhiều tầng + kiểm soát chặt, nguồn lực hạn chế (giãn đỉnh tài nguyên), nhiều module và/hoặc tùy biến nhiều, cần chứng minh "hệ chạy được" để lấy hậu thuẫn.
- **Ba mô hình tình huống (contingency)**:
  - **Size & Complexity**: càng lớn/phức tạp → càng nghiêng về phased (phức tạp đến từ số sản phẩm/khách hàng, quyền lực khách hàng, độ rộng dòng sản phẩm; quy mô đo bằng doanh thu/tài sản/số văn phòng/vùng địa lý).
  - **Hierarchy & Control**: tổ chức càng nhiều tầng + kiểm soát càng chặt → càng duy trì được phased; phẳng + lỏng → nên big bang.
  - **Extent of Implementation**: số module càng nhiều và **module fit** càng thấp (càng nhiều modification) → càng nghiêng phased; ít module + thay đổi tối thiểu → big bang.
- **Alternative approaches**:
  - **Waved** (Tektronix): chương trình thay đổi gồm nhiều "đợt sóng", mỗi sóng trao functionality cho một business unit/vùng, quản lý độc lập nhưng điều phối phụ thuộc chung; nằm giữa big bang và phased. Lợi: feedback từng sóng, mỗi sóng là một "chiến thắng" giữ tinh thần, linh hoạt thêm sóng khi có bản ERP mới.
  - **Aggressive schedule**: temporary interface thực sự tạm thời (không bán vĩnh viễn), có thể bật nhiều module cùng lúc nhưng không hẳn big bang.
  - **Running in parallel**: chạy song song hệ cũ và mới một thời gian (tháng/quý) để đối chiếu; low-risk nhưng tốn gấp đôi tài nguyên, và hệ cũ có thể bị "gieo" lỗi vì không ai còn động cơ giữ nó, lại kém giá trị đối chiếu nếu đã reengineering mạnh.

## Khái niệm chính (Key Concepts)
- **Temporary interface**: cầu nối tạm giữa module ERP mới và legacy, đặc trưng của phased; big bang không cần.
- **Available to Promise (ATP)**: khả năng xác nhận và giữ tồn kho theo thời gian thực, cắt ngang nhiều site và nhiều module — chỉ có khi đủ hạ tầng ERP; lý do Quantum phải chọn big bang.
- **Systems Validation Test (SVT)**: test diện rộng với ~100 user nhập khối lượng giao dịch lớn, mô phỏng tải tương lai và test cả phần cứng.
- **Conference room pilot**: test một module với dải giao dịch để xem có chạy đúng không.
- **Module fit**: mức khớp giữa module và yêu cầu (Siemens: finance ~100%, module khác 70–80% → cần modification).

## Mô hình tư duy (Mental Models)
- Quyết định nên là **cost–benefit điều chỉnh theo rủi ro**; nhưng vì rủi ro/lợi ích khó đo, thực tế dựa vào các biến trung gian (size, complexity, control, hierarchy, extent).
- Xem big bang là canh bạc "all or nothing": một module hỏng có thể làm sập cả triển khai, không có đường lùi — nhưng chính "không đường lùi" lại tạo cam kết tiến tới.
- Dùng phased như công cụ chính trị: cài module "dễ nhất" (fit cao, ít reengineering) trước để chứng minh hệ chạy được, lấy hậu thuẫn quản lý.

## Điều cần tránh (Anti-patterns)
- **Kéo dài triển khai (1–3 năm)**: yêu cầu đổi, nhân sự nghỉ việc, phe phản đối có thời gian chống phá → nguyên nhân thất bại hàng đầu.
- **Big bang mà không test interdependency giữa các module**: Quantum SVT 1 sập dù từng mảnh chạy độc lập — "sốc khi các mảnh chạy riêng được nhưng không chạy cùng nhau".
- **Running in parallel sau reengineering mạnh**: hệ cũ và mới ít điểm chung nên không còn là cơ sở đối chiếu hợp lý; hệ cũ còn chạy lại đe dọa sự sống của hệ mới.

## Ví dụ minh họa (Worked Example)
**Quantum — dự án WARP (worldwide ask replacement system)**, công ty lưu trữ $4.4 tỷ, 23 site toàn cầu:
- Bối cảnh: 9 legacy không chia sẻ dữ liệu, consolidate MRP thủ công mất 4 ngày, đóng sổ ≥17 ngày, không có ATP; mua lại mảng lưu trữ của DEC làm "độ phức tạp và quy mô dự án tăng gấp bốn", gấp đôi artifact (product list, vendor/client number) và quy trình → dự án tạm dừng 3 tháng, phải làm lại.
- Chọn hệ thống: phân tích quy trình bằng "play acting", chốt yêu cầu, chọn Oracle (financial + manufacturing) vì **chỉ Oracle có ATP**.
- Tổ chức: hậu thuẫn từ đỉnh; 3 nhóm — steering committee (các VP + Price Waterhouse), core team 16 quản lý, project team 100 người; nhóm 2 và 3 rời việc hằng ngày, làm full-time, dời tới một địa điểm riêng, cross-functional theo process.
- Chọn big bang: "nếu làm phased tôi sẽ không có ATP cho tới mãi về sau — buộc phải big bang" (Jackson). Tức big bang = bật 17 module tại 23 site gần như cùng lúc.
- Test: 6 tháng test (≈7–8 tháng thực tế). **SVT 1** (2 tuần, 100 user) sập ngay tuần đầu (mạng sập, đơn hàng không đổi lịch nhà máy). Delevati gia nhập, nâng cấp HP 9000/HP-UX và Oracle 10.4, rồi lập **bảng điều phối màu** cho mọi subtask trong các nhóm việc (business functionality, systems performance, data conversion, IS readiness, training, documentation, site readiness): green = ready, yellow = có thể cần can thiệp thủ công, red = chưa sẵn sàng → dồn sức vào các task đỏ. **SVT 2** (11/12/1995–08/01/1996) thành công, user bay về HQ dự; một test cuối tháng 2 vẫn lộ vấn đề (Penang Malaysia suýt nghẽn mạng, tăng băng thông mất 90 ngày → tạm cắt Internet, dồn toàn bộ băng thông cho Oracle).
- Training: lịch 24 tháng gồm 6 tuần training toàn cầu, nhân viên rời việc 2–4 tuần, quản lý địa phương **không được** rút người khỏi training dù có sự cố kinh doanh.
- Cutover: 05/05/1996 bật thật; 8 ngày "business ngừng" — không đặt hàng, không nhận vật tư, không ship, không post tiền (chỉ chạy payroll) — rồi đưa cả công ty lên cùng lúc với backlog, tất cả site tích hợp. Kết quả: hệ Oracle phân tán lớn nhất triển khai bằng big bang khi đó; đóng sổ tháng đầu 9 ngày (trước là 17), quý đầu 11 ngày. Không làm ROI study nhưng coi là thành công: "muốn tiết kiệm 10% chi phí nhưng sẽ đẩy rủi ro lên mức không chấp nhận được — muốn thành công phải chi tiền và chăm lo chi tiết".

## Điểm cần nhớ (Key Takeaways)
1. Big bang: không cần temporary interface, ít phải bảo trì legacy, thời gian ngắn hơn, chi phí tiền mặt thấp nhất nếu suôn sẻ, không đường lùi; nhưng đỉnh tài nguyên cao và rủi ro sập toàn hệ.
2. Phased: giãn đỉnh tài nguyên, dồn lực cho từng module, có legacy làm fallback, chuyển giao kiến thức qua từng pha, chứng minh hệ chạy được sớm; nhưng tốn temporary interface, bảo trì legacy, lâu hơn và tổng chi phí cao hơn.
3. Chọn cách triển khai theo tình huống: size/complexity, hierarchy/control, số module × module fit.
4. Test interface/interdependency giữa các module, không chỉ test từng module riêng — đây là điểm sập điển hình của big bang.
5. Nếu cần tính năng cross-module (như ATP) ngay từ đầu, phased sẽ trì hoãn nó → nghiêng về big bang.

## Ứng dụng cho BA ERP (BA Application)
- Trong tài liệu triển khai, ghi rõ chiến lược (big bang/phased/waved/parallel) và căn cứ theo các biến tình huống (quy mô, phức tạp, cấu trúc/kiểm soát, số module, module fit) thay vì mặc định.
- Với phased, đặc tả rõ các **temporary interface** tới legacy ở mỗi pha và kế hoạch gỡ bỏ — chúng là hạng mục công việc và rủi ro thực.
- Luôn có hạng mục **test interface giữa các module** riêng biệt trong kế hoạch test, không chỉ test đơn module; mô tả SVT/conference room pilot với khối lượng giao dịch mô phỏng tải thật và test phần cứng.
- Dùng bảng theo dõi trạng thái theo task/subtask có "owner" và mã màu (ready / cần can thiệp thủ công / chưa sẵn sàng) làm artifact quản lý readiness trong spec triển khai.
- Nếu một yêu cầu phụ thuộc tính năng cross-module (ví dụ available-to-promise), ghi rõ ràng buộc rằng tính năng chỉ có khi các module liên quan cùng go-live — ảnh hưởng tới lựa chọn big bang/phased.

## Liên hệ (Connects To)
- **Ch 8 & Appendix 11-1**: Quantum chọn hệ thống theo yêu cầu, ATP là feature khác biệt quyết định.
- **Ch 9**: extent of modification (module fit) gắn với small-r/big-R reengineering.
- **Ch 12**: sau cutover là giai đoạn ổn định (stabilization) và xử lý backlog.
- **Ch 13**: training như yếu tố then chốt của triển khai (ép tham dự, không rút người).
- **Ch 15**: thời gian triển khai dài là yếu tố rủi ro/thất bại.
