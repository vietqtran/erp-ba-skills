# Chương 12: Sau khi Go-Live (After Going Live)

## Ý tưởng cốt lõi (Core Idea)
Go-live không phải là "xong". Doanh nghiệp bước vào **stabilization period** (giai đoạn ổn định, 3–9 tháng) thường kéo tụt hiệu năng; phải lập **ERP support organization** để vận hành hằng ngày, rà soát những gì còn phải làm/làm lại (data conversion, bottleneck, tài liệu/training, implementation compromise), đối chiếu kế hoạch với thực tế, lên kế hoạch linkage/upgrade/extension, và đánh giá thành công — kèm ngân sách cho toàn bộ việc hậu triển khai.

## Framework được giới thiệu (Frameworks Introduced)
- **Stabilization Period** — 3–9 tháng sau go-live, hiệu năng thường tụt (khảo sát Deloitte: 1/4 doanh nghiệp giảm hiệu năng). Nguyên nhân: user chưa quen phần mềm/quy trình mới, thời gian xử lý & mạng chưa đủ (Cisco: hardware sizing). Cần training đúng lúc (sớm quá thì quên, muộn quá thì không kịp).
- **ERP Support Organization** — thường dưới quyền VP IS/CIO; hoạt động: bắt và xử lý bug; trả lời user (help desk/training); đổi tham số hệ thống khi tổ chức thay đổi (vendor list, chart of accounts, MAPs); đảm bảo bản production nhất quán; quản lý input/output và nhu cầu báo cáo thay đổi; duy trì tài liệu/training; bảo trì và nâng cấp. Giữ lại thành viên project team có "hot skills" là then chốt.
- **Compare Plan vs Reality** — kiểm toán ba chiều: (1) thiết kế & triển khai hệ thống; (2) use dự kiến vs thực tế; (3) năng lực hệ thống kỳ vọng vs thực tế. Khác biệt lớn đe dọa thành công vì lý do chọn ERP ban đầu có thể không đạt.
- **Implementation Compromises** — các sai lệch so với kế hoạch để tiết kiệm thời gian/tiền ("để phần này làm sau"). Hệ quả: hệ thống không chạy đúng như kỳ vọng; đôi khi biến thành **engagement compromise** (chính các quy trình/thay đổi then chốt — lý do đi ERP — bị cắt). Ví dụ: security đặt ở mức group thay vì individual; báo cáo không đủ (Geneva Steel phải cài data warehouse). Phát hiện bằng: so với kế hoạch; lắng nghe nhân viên; mời consultant soát (nhất là security).
- **Evaluate Success** — bốn trục:
  - **Timing**: đánh giá vào năm 1–2 sau go-live (bug đã sửa, có 1 năm dữ liệu để đo, ví dụ inventory turnover).
  - **Duration/Cost/Benefit**: khảo sát Austin & Cotteleer — benefit thường thấp hơn kỳ vọng, cost thường vượt (vì cost bị ước thấp và benefit bị thổi lên để bán dự án cho lãnh đạo); chỉ 44% doanh nghiệp theo dõi benefit chính thức.
  - **Choice Rationale**: lý do technology (client server, Y2K, "theo kịp đối thủ") ít đo được; lý do strategy/business process đo cụ thể được (mức tồn kho, % doanh thu, turnover, chi phí kho/vận tải).
  - **Independent vs Weighted Portfolio / Balanced Scorecard**: dùng nhiều thước đo; **balanced scorecard** (Kaplan & Norton) với 4 góc nhìn (financial, customer, learning & growth, internal process) ánh xạ sang 4 business-case rationale của ERP (technology, business process, strategic, competitive).

## Khái niệm chính (Key Concepts)
- **Data conversion**: đưa dữ liệu cũ về định dạng mới; lỗi chỉ lộ theo thời gian (tồn kho phình, thu hồi giảm, thiếu linh kiện có thể là triệu chứng sai part/vendor/inventory number). Giảm thiểu bằng **reconcile** (số tồn kho/sản phẩm/vendor có khớp không, vì sao không) và **mapping** từ CSDL này sang CSDL kia để bảo đảm không bỏ sót.
- **Process bottleneck**: nút thắt còn lại; phát hiện qua phàn nàn của khách/đối tác, help desk, phân tích dữ liệu ERP nội bộ (exception report), và trao đổi với người dùng.
- **Linkage / Upgrade / Extension**: nối hệ khác; nâng phiên bản để có feature (ABB cần bản R/3 mới hơn mới chạy được activity-based costing); mở rộng (supply chain, sales force automation) — ERP thành "backbone".
- **Hot skills retention**: giữ người có kỹ năng ERP có giá trị thị trường cao.

## Mô hình tư duy (Mental Models)
- Xem go-live là điểm "reality check": tầm nhìn ERP lần đầu đủ cụ thể để so với kỳ vọng của lãnh đạo.
- Phân biệt **metric vs goal**: một con số mong muốn chỉ là goal cho tới khi gắn được với thước đo quy được về chính ERP.
- Chỉ đo benefit khi đủ thời gian để nó hiện ra và đo được — đo quá sớm sẽ kết luận sai.

## Điều cần tránh (Anti-patterns)
- **Cạn ngân sách khi tới stabilization period**: mất người, mất tiến độ; phải lập ngân sách cho toàn vòng đời kể cả sau go-live.
- **Không theo dõi benefit** (56% không làm): do quản trị dự án kém, benefit khó đo, hoặc coi dự án là sunk cost.
- **Request báo cáo mới không qua process owner duyệt**: làm nghẽn hệ thống.
- **Để implementation compromise trở thành engagement compromise**: cắt đúng phần quy trình là lý do đi ERP.

## Bảng tham chiếu (Reference Tables)
**Deloitte Consulting Post-Implementation Checklist** (Appendix 12-2) — trả lời Yes/No; mỗi No phải chuyển thành Yes sớm nhất có thể:
- The Basics: Có kế hoạch hậu triển khai không?
- Benefit Targets: Benefit & capability của ERP đã thành một phần business plan của từng general manager chưa? Đã truyền thông benefit dự kiến tới toàn tổ chức chưa?
- Project Teams: Project team còn tại chỗ không? Có kế hoạch giữ nhân viên "hot skills" không? Thành viên có biết cơ hội nghề nghiệp nội bộ không?
- Business Metrics: Có metric đo benefit dự kiến vs thực đạt chưa? Mỗi metric đã gán owner chưa?
- Project Management: Có chương trình giúp cá nhân thích ứng với thay đổi vai trò và stress chưa? Đã lập center of expertise/support organization chưa?
- Process Expertise: Lãnh đạo có process-oriented hơn trước không? Có reward cho người dùng hệ thống không? Request báo cáo mới có được process owner duyệt không?
- ERP Foundation: Có kế hoạch mở rộng functionality không?
- Training: Training user có theo công việc (job-based) chứ không chỉ "học bấm nút" không?

Bảng 12.1 — Thực tế vs kỳ vọng (Austin & Cotteleer, % các dự án): benefit đa phần rơi vào 50–100% kỳ vọng (65%); cost đa phần 100–125% (43%); duration thường bằng hoặc vượt, có khi gần gấp đôi.

## Ví dụ minh họa (Worked Example)
**XYZ Company — nên đánh giá dự án ERP thế nào?** (Appendix 12-1). Một quản lý cấp trung nhận bộ "metric" cho trạng thái mong muốn ~1 năm sau go-live:
- Inventories: nguyên vật liệu tồn < 20 ngày; giảm work-in-process 40%; finished goods turnover từ 9 → 12 lần/năm.
- General Admin: phát hành báo cáo tài chính trong 6 ngày (hiện 24); customer service lên 99% với 90% giao đúng hạn (hiện 97%/70%); tăng năng suất sản xuất/bán hàng/tài chính/mua hàng/kỹ thuật/IS thêm 10%.
- Division A: tăng gross margin 6% doanh thu; Division B: tăng 2%.
- Băn khoăn: đây là metric hay goal? Triển khai không thêm functionality nào chưa có sẵn. → Bài học: con số đẹp vô nghĩa nếu (a) không phân biệt rõ metric/goal, (b) không quy được cải thiện về chính ERP, (c) không có owner và baseline để đo.

## Điểm cần nhớ (Key Takeaways)
1. Lập kế hoạch và ngân sách cho hậu go-live; stabilization 3–9 tháng sẽ kéo tụt hiệu năng — phải quản lý qua "cái hố" đó.
2. Giữ project team làm support organization; giữ người "hot skills" bằng lộ trình nghề nghiệp.
3. Reconcile và mapping dữ liệu sau chuyển đổi; lỗi data conversion ngụy trang thành triệu chứng kinh doanh.
4. Soát implementation compromise (nhất là security và báo cáo) để chúng không phá lý do đi ERP.
5. Đánh giá thành công sau 1–2 năm bằng thước đo cụ thể gắn với rationale; cân nhắc balanced scorecard thay vì một con số.

## Ứng dụng cho BA ERP (BA Application)
- Thêm một mục "post-implementation" vào spec: support organization (vai trò, help desk, quy trình đổi tham số), kế hoạch data conversion (reconcile + mapping), và cách phát hiện bottleneck.
- Với mỗi yêu cầu benefit, định nghĩa rõ **metric** (có baseline, có owner, quy được về ERP) chứ không chỉ ghi **goal**; đây là chuẩn để sau này nghiệm thu.
- Đưa Deloitte Post-Implementation Checklist (Yes/No) vào bộ acceptance criteria hậu triển khai của tài liệu.
- Ghi rõ các implementation compromise được chấp nhận và phần sẽ "làm sau", kèm hệ quả — để không âm thầm biến thành engagement compromise.
- Đặc tả quy trình duyệt báo cáo mới qua process owner (chống nghẽn hệ thống) và quy tắc ai được xem báo cáo nào (phân quyền output).

## Liên hệ (Connects To)
- **Ch 11**: big bang cutover (Quantum) dẫn thẳng vào stabilization period và xử lý backlog.
- **Ch 9**: implementation compromise (profit/cost center của Microsoft) là ví dụ compromise cần soát lại.
- **Ch 13**: training đúng lúc là yếu tố chính của stabilization.
- **Ch 2 & 6**: data warehouse (Geneva Steel) như giải pháp cho compromise về báo cáo.
- **Balanced Scorecard (Kaplan & Norton)**: khung đánh giá đa góc nhìn.
