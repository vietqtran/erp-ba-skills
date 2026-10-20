# Patterns — Thiết kế chức năng & kiểm soát chuẩn ERP

Các mẫu kỹ thuật rút từ sách, đã gộp trùng lặp giữa các tình huống. Mỗi mẫu: When (khi nào) / How (cách làm) / Trade-offs (đánh đổi). Số chương theo skill này.

## Checklist giả định kiểm soát ERP (9 → 11) để nghiệm thu "đã chuẩn ERP chưa"
**When**: Nghiệm thu thiết kế bất kỳ module/chức năng ERP có yếu tố kiểm soát. **How**: Với mỗi chức năng, trả lời yes/no + nêu cơ chế cho từng giả định trong bộ hợp nhất 11 ở Ch 10: integration, standardisation, automation, multiple methods of control, preventive, compensating, continuous monitoring, data security, centralisation, data consistency, transparency & visibility. (Mỗi case trong sách chỉ dùng một tập con: IC 9, NC/NB/IB 10.) **Trade-offs**: Không chức năng nào cần đủ 11; chọn theo vùng rủi ro để tránh over-engineering. (Ch 06, 07, 10)

## Phân loại kiểm soát theo 4 loại ERP (phân định code vs config)
**When**: Viết spec kiểm soát để dev biết việc phải làm. **How**: Gắn nhãn mỗi kiểm soát: inherent (có sẵn, không code), configurable (phải cấu hình lúc customise), security (phân quyền + SoD), reporting (báo cáo chuẩn/ad hoc). **Trade-offs**: Ranh giới configurable/security đôi khi mờ; cần thống nhất với đội kỹ thuật. (Ch 06)

## Kiểm soát phòng ngừa: SoD + authorisation profile + luật if/else
**When**: Thiết kế phân quyền và kiểm soát vận hành/tài chính cho một chức năng. **How**: Định nghĩa quy tắc SoD; gán authorisation profile cho mỗi role (xem/sửa/xóa bản ghi nào); thêm access protection; viết luật chặn code-able — chặn lệnh sản xuất nếu tồn kho vật tư < định mức, chặn post vào kỳ đã khóa, chặn post sai mã khách, chặn đặt hàng nhà cung cấp từng giao lỗi; kèm report dò xung đột SoD chạy định kỳ. **Trade-offs**: Chặn cứng mạnh về phòng ngừa nhưng cần thiết kế luồng ngoại lệ/override cho trường hợp hợp lệ; SoD quá chặt gây tắc ở tổ chức nhỏ (cân nhắc compensating control). (Ch 06, 07)

## Single data entry point + auto-journal
**When**: Tích hợp sự kiện phi tài chính với kế toán. **How**: Dữ liệu nhập một lần; nghiệp vụ phi tài chính tự sinh bút toán tài chính; các bước sau mặc nhiên chấp nhận dữ liệu bước trước (peer review nhúng trong luồng). **Trade-offs**: Giảm lỗi và can thiệp tay nhưng lỗi ở điểm nhập đầu dễ lan nếu kiểm soát thượng nguồn yếu. (Ch 07)

## RBAC hai lớp (function security + data security)
**When**: Thiết kế phân quyền. **How**: function security giới hạn menu/chức năng truy cập; data security giới hạn phạm vi dữ liệu user được xem/sửa; nhân viên chỉ thấy thông tin liên quan công việc để chống thông đồng. **Trade-offs**: Phân quyền mịn, chống thông đồng, nhưng phức tạp để duy trì khi nhân sự luân chuyển. (Ch 08, 10)

## Approval workflow + automatic submission check
**When**: Chứng từ cần phê duyệt. **How**: approval hierarchy + "Submit for Approval" chuyển tới người duyệt đúng cấp; submission check xác minh trường bắt buộc và prescribed ranges, sai → approval errors window; tự in/chuyển trạng thái khi duyệt. **Trade-offs**: Kiểm soát chặt nhưng cứng nhắc; cần thiết kế rõ ngưỡng và quy tắc kiểm. (Ch 08)

## Maker-checker (cấu hình bổ sung nếu ERP thiếu)
**When**: Đặc tả giao dịch tài chính/ngân hàng. **How**: Mỗi màn hình được người lập + người kiểm xử lý; màn hình không đi tiếp đến khi có approval + validation; nếu ERP mặc định không có thì đặc tả như một yêu cầu customisation có chủ đích. **Trade-offs**: Thêm bước/độ trễ nhưng phòng gian lận mạnh; chi phí customise. (Ch 08, 09)

## CAVAIR làm tiêu chí nghiệm thu dữ liệu
**When**: Đặc tả validation và di trú dữ liệu. **How**: Yêu cầu dữ liệu Complete, Accurate, Valid và Restricted Access; biến thành ràng buộc validation code-able trên từng bảng/giao diện nhập. **Trade-offs**: Validation chặt tăng chất lượng nhưng có thể gây ma sát khi nhập liệu. (Ch 09)

## Black-box test bằng dữ liệu giả
**When**: Nghiệm thu tính toán/xử lý tự động của hệ thống. **How**: Chạy fake data qua hệ thống, so sánh output với kỳ vọng để xác minh xử lý đúng. **Trade-offs**: Chỉ kiểm I/O, không kiểm logic bên trong; cần bổ sung review controls khác. (Ch 09)

## Risk-based audit với risk map
**When**: Lập kế hoạch kiểm toán/giám sát hệ thống ERP. **How**: Xếp hạng rủi ro cao→thấp trên risk map; vẽ phạm vi và lịch kiểm toán động theo bản đồ; theo dõi rủi ro cao nhất là thay đổi quyền truy cập theo luân chuyển nhân sự. **Trade-offs**: Hiệu quả nhưng đòi hỏi năng lực đánh giá rủi ro trưởng thành. (Ch 09, 11)

## Kế hoạch & đội kiểm toán tài chính + IT hợp nhất (horizontal)
**When**: Đặc tả kiểm soát/kiểm toán cho quy trình do ERP vận hành xuyên nhiều chức năng/địa điểm. **How**: Một integrated audit plan xác định ứng dụng nào ảnh hưởng số liệu tài chính và cần kiểm; mô tả kiểm soát end-to-end gộp tài chính + vận hành + IT thay vì rời rạc theo màn hình/địa điểm. **Trade-offs**: Cần auditor có kỹ năng IT và tổ chức quen kiểm theo tiến trình; đổi lại phủ được rủi ro liên kết. (Ch 09, 11)

## Đưa người kiểm soát vào từ giai đoạn requirements (early involvement / super users)
**When**: Từ khâu chọn hệ thống đến go-live. **How**: Cho kiểm toán/chủ quy trình tham gia định nghĩa roles & authorisations, SoD, risk framework, yêu cầu báo cáo; verify data migration; review đủ-kiểm-soát; làm super users; verify toàn bộ control trước go-live. **Trade-offs**: Kéo dài giai đoạn phân tích nhưng phòng được lỗi kiểm soát đắt giá sau triển khai và khiến mọi modification auditable. (Ch 06, 09, 11)

## Quyết định reengineer vs customise/localise vs workaround
**When**: Quy trình khách hàng lệch với quy trình chuẩn ERP. **How**: Nếu quy trình không customise được hoặc là thủ tục sai/bất hợp pháp → reengineer về chuẩn, làm auditable. Nếu lệch do luật địa phương (thuế) → customise/localise có kiểm soát. Tuyệt đối tránh workaround để giữ thao tác bất hợp lệ. Ghi rõ lựa chọn + lý do trong tài liệu. **Trade-offs**: Reengineer gây kháng cự thay đổi; customise nhiều làm hệ thống khó nâng cấp và lệch best-practice. (Ch 06, 10, 11)

## Cutover có kiểm soát + change management (tránh parallel-run thảm họa)
**When**: Chuyển đổi từ hệ thống cũ sang ERP. **How**: Tránh chạy song song thủ công + ERP không kiểm soát; bắt buộc nhập liệu vào ERP; đào tạo thật (không chỉ briefing); có change management plan tính cả thích nghi vai trò, rủi ro kháng cự, khen thưởng khi áp dụng. **Trade-offs**: Chuẩn bị tốn công nhưng tránh kịch bản phải kiểm toán lại hàng tháng giao dịch với hàng ngàn lỗi. (Ch 08, 10, 11)

## Phân tích rủi ro–kiểm soát 7 bước cho một chu trình
**When**: Thiết kế kiểm soát cho một chu trình/chức năng ERP cụ thể. **How**: Nhận diện dải rủi ro → gắn rủi ro với ứng dụng → định lượng chi phí mỗi exposure → chọn kiểm soát cost-effective → tư vấn phân bổ nguồn lực → dự liệu ứng phó → tư vấn quản lý rủi ro. **Trade-offs**: Định lượng chi phí exposure khó chính xác; vẫn hữu ích để ưu tiên. (Ch 02)

## Continuous Auditing (embedded module vs monitoring control layer)
**When**: Cần đảm bảo kiểm soát thời gian thực trên nền ERP đầy đủ chức năng. **How**: Chọn một trong hai — nhúng module kiểm toán vào hệ thống (embedded audit module) hoặc dựng lớp giám sát kiểm soát tách biệt (monitoring control layer); vận hành kiểu "auditing by exception". **Trade-offs**: Embedded gắn chặt hệ thống, khó độc lập; monitoring layer độc lập hơn nhưng cần tích hợp dữ liệu. (Ch 02, 12)

## Truy nguồn yêu cầu (coercive/normative/mimetic) + lường phản ứng (Oliver)
**When**: Research ngành và lọc features; lập kế hoạch change management. **How**: Gắn nhãn mỗi feature theo nguồn áp lực — coercive (luật, bắt buộc = must-have), normative (chuẩn ngành/best-practice), mimetic (đối thủ/trend). Xếp phản ứng dự kiến của người dùng vào 5 chiến lược Oliver (acquiescence/compromise/avoidance/defiance/manipulation) kèm tactic ứng phó. **Trade-offs**: Một yêu cầu chịu nhiều áp lực cùng lúc; phản ứng thay đổi theo thời gian, cần cập nhật. (Ch 03, 04, 10)

## Elicitation có kỷ luật: template + emergent coding + triangulation + member check
**When**: Thu thập/phân tích và verify yêu cầu, chống vừa hallucinate vừa bỏ sót. **How**: Khởi đầu từ template/checklist dựng sẵn từ chuẩn ERP (directed content analysis); cho yêu cầu mới của khách nổi lên và bổ sung mã; đối chiếu mỗi dữ kiện qua ≥2 nguồn (phỏng vấn nhiều vai, tài liệu, quan sát); gửi bản thảo cho stakeholder member-check. **Trade-offs**: Khung có sẵn dễ làm bỏ qua yếu tố ngoài khung nếu không chủ động để mã mới nổi lên; triangulation tốn thời gian. (Ch 05, 12)

## Bộ câu hỏi phỏng vấn theo vai trò (6 nhóm) + coding scheme làm checklist độ phủ
**When**: Khai thác yêu cầu ERP từ nhiều bên liên quan và nghiệm thu độ phủ tài liệu. **How**: Chia câu hỏi theo 6 nhóm (quản trị–IAF, logic ERP, sai khớp, thay đổi IAF, vai trò kiểm soát/rủi ro, chính danh) và theo role (CIA, kiểm toán viên, quản lý ERP, vendor, IT, kế toán, GĐ tài chính); gửi agenda trước; sắp dễ→khó→tích cực; gắn mỗi yêu cầu vào một nhãn trong coding scheme 5 nhóm, nhãn trống = nghi ngờ thiếu chức năng. Luôn hỏi "ai chịu trách nhiệm" (RACI) cho từng kiểm soát. **Trade-offs**: Chuẩn bị công phu; taxonomy mang màu kiểm toán/quản trị, cần ánh xạ sang ngôn ngữ nghiệp vụ dự án. (Ch 12)
