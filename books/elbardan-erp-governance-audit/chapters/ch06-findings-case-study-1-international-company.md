# Chương 6: Kết quả nghiên cứu tình huống 1 — Công ty quốc tế (Findings from Case Study 1 — The International Company (IC))

## Ý tưởng cốt lõi (Core Idea)
Áp khung Chương 4 vào một công ty hàng tiêu dùng nhanh (FMCG) niêm yết London/New York, triển khai **SAP** năm 2010 (các module FI — kế toán tài chính, CO — kiểm soát/controlling, SD — bán hàng & phân phối, MM — quản lý vật tư, HR — nhân sự). Chương bóc tách *chín giả định kiểm soát (control assumptions)* mà ERP mang theo, cách tổ chức căn chỉnh (aligning) để khớp chúng, và cách chức năng kiểm toán nội bộ (IAF) thích nghi. Với BA, đây là chương giàu tri thức thiết kế ERP-chuẩn nhất: nó liệt kê rõ các cơ chế kiểm soát mà một hệ ERP tốt phải có.

## Framework được giới thiệu (Frameworks Introduced)
- **Nine control assumptions of ERP** — chín giả định kiểm soát vận hành hóa nguyên lý "control" của ERP (xem Bảng tham chiếu). Khi dùng: làm checklist nghiệm thu "thiết kế đã chuẩn ERP chưa?".
- **Four ERP control types (SAP)** — bốn loại kiểm soát mà ERP cung cấp:
  - **Inherent controls**: kiểm soát có sẵn, giao kèm ERP, *không cần thiết kế thêm*.
  - **Configurable controls**: kiểm soát tự động *phải định nghĩa lúc cấu hình/customise*.
  - **Security controls**: kiểm soát truy cập người dùng và phân tách nhiệm vụ (segregation of duties).
  - **Reporting controls**: dựa trên báo cáo chuẩn hoặc ad hoc.
- **Aligning efforts (căn chỉnh)** — ba nỗ lực thu hẹp sai lệch (misalignment) giữa ERP, quy trình và quản trị: change management, reengineering & customisation, internal auditors' involvement.
- **Strategic response path (Oliver, áp dụng thực tế)**: phản ứng dịch chuyển theo thời gian từ **compromise** (thỏa hiệp — bargaining/balancing) sang **acquiescence** (tuân thủ — compliance/habit/imitation).

## Khái niệm chính (Key Concepts)
- **Segregation of Duties (SoD)** — phân tách nhiệm vụ: quy tắc kiểm toán nền tảng; ERP dò xung đột SoD tự động và chạy định kỳ.
- **Authorisation profile** — hồ sơ phân quyền: mỗi user có một profile xác định được xem/sửa/xóa những bản ghi nào; nền của preventive control.
- **Audit trail** — vết kiểm toán: ERP tự sinh, truy được *ai, khi nào, tại sao* một thay đổi.
- **Standard chart of accounts / standard general ledger** — hệ thống tài khoản chuẩn / sổ cái chuẩn: giao dịch tự phân loại theo chart chuẩn ngay ở cấp vận hành.
- **Compensating controls** — kiểm soát bù: kiểm soát thứ hai phục vụ mục tiêu khi kiểm soát chính hỏng; SEC/PCAOB yêu cầu kiểm toán viên cân nhắc.
- **Exception / red-alert reports** — báo cáo ngoại lệ / cảnh báo đỏ khi có sử dụng bất thường.
- **Operational Control Assessment (OCA)** — đánh giá kiểm soát vận hành dựa trên rủi ro.
- **Integrated (comprehensive) auditing** — kiểm toán tích hợp: phủ kiểm soát xuyên suốt end-to-end theo vùng nghiệp vụ thay vì kiểm toán tách rời từng cụm kiểm soát.

## Mô hình tư duy (Mental Models)
- Coi quy trình nghiệp vụ như "phải làm cho kiểm toán được (auditable) trước khi làm cho chạy": một quy trình chỉ chuẩn ERP khi nó để lại vết và có kiểm soát gắn vào.
- "Governance rules vẽ hướng dẫn quy trình, ERP thực thi quy trình có tính tới các quy tắc đó" — hai mặt của một đồng xu; đừng thiết kế tính năng mà không gắn với một quy tắc quản trị.
- Khi quy trình khách hàng *không customise được* trong ERP (ví dụ thủ tục bất hợp pháp/ưu đãi thuế trái quy định), đó là tín hiệu phải *reengineer*, không phải bẻ cong hệ thống.
- Một rủi ro không chỉ cần một kiểm soát: luôn hỏi "nếu kiểm soát này hỏng, có compensating control nào không?".

## Điều cần tránh (Anti-patterns)
- **Thiết kế ERP không có vai trò kiểm soát từ đầu**: ERP "không có module kiểm toán riêng" — nếu không nhúng kiểm soát vào từng module thì không có đảm bảo.
- **Bỏ qua internal auditor/kiểm soát khi gathering & mapping requirements**: dẫn tới sai SoD, access rights, thiếu report kiểm soát sau go-live.
- **Tin rằng báo cáo chuẩn là đủ**: phần lớn customise thực tế rơi vào vùng *báo cáo* vì format/khối lượng/phân loại dữ liệu chuẩn thường không hợp nhu cầu kiểm soát.
- **Customise để né chuẩn**: tùy biến hệ thống cho khớp thói quen cũ thay vì tận dụng cách kiểm soát tốt hơn của ERP.

## Bảng tham chiếu (Reference Tables)
Chín giả định kiểm soát của ERP (6.3.1–6.3.9):

| # | Giả định | Cơ chế cụ thể (BA cần thiết kế/đặc tả) |
|---|---|---|
| 1 | **Automation** | Tự động kiểm tra tính hợp lệ của quy trình ở mọi cấp; tự dò xung đột SoD; tự sinh audit trail; báo cáo discrepancy & reconciliation |
| 2 | **Continuous Timely Monitoring** | Xử lý real-time; giám sát định kỳ/ad hoc; specialised reports; red alerts; exception reports |
| 3 | **Data Consistency** | Cùng một định dạng dữ liệu cho mọi đơn vị; hợp nhất dễ; loại trùng lặp & dư thừa |
| 4 | **Control Through Integration** | Một CSDL; nhập một nơi tự chảy đi nơi khác; giảm đối soát thủ công; làm hành động hữu hình |
| 5 | **Multiple Methods of Control** | Nhiều kiểm soát cho một đối tượng (logistics / kết quả tài chính / matching); 4 loại: inherent, configurable, security, reporting |
| 6 | **Preventive Controls** | SoD + authorisation profile + access protection; ngăn vi phạm trước thay vì phát hiện sau |
| 7 | **Standardisation** | Standard business process, standard GL, standard chart of accounts; một cách làm duy nhất → dễ phát hiện sai lệch |
| 8 | **Transparency** | Visibility toàn giao dịch; audit trail ai/khi nào/tại sao; không giấu/thao túng được |
| 9 | **Compensating Controls** | Nhiều hơn một kiểm soát cho cùng vùng rủi ro |

## Ví dụ minh họa (Worked Example)
**Chuẩn hóa + kiểm soát phòng ngừa tại IC (tình huống thuế).** Trước SAP, IC có nhiều hệ thống rời, mỗi vùng một bộ dữ liệu, quy trình "rất linh hoạt" — bao gồm cả việc cho một số nhà cung cấp/đại lý ưu đãi thuế bằng giao dịch *không hóa đơn chính thức*. Khi triển khai SAP:
1. Các thủ tục bất hợp pháp này *không thể customise* vào hệ thống → buộc phải **reengineer** quy trình mua/bán để về định dạng *auditable*.
2. Giao dịch sau đó tự phân loại theo **standard chart of accounts** ngay ở cấp vận hành → kiểm toán viên chỉ phải theo dõi *một* cách làm thống nhất.
3. Phần localise hợp pháp (thuế theo luật nước sở tại) được giữ qua **customisation** có kiểm soát.
4. Kiểm soát phòng ngừa: mỗi user có **authorisation profile**; SAP automation controller kiểm tra một sự kiện có đăng ký trong bảng sự kiện không — nếu không thì bỏ qua, nếu có thì sinh mã OK và chuyển sang objects control framework. Nhờ full SoD trong hệ thống, kiểm toán viên *không còn* phải ký duyệt từng giao dịch thủ công; công việc dịch chuyển từ "checking" sang "monitoring".

Kết quả (Fig 6.1): áp lực coercive yếu (luật Ai Cập không bắt buộc IAF) nhưng được *trụ sở chính nước ngoài* biến thành chính sách nội bộ bắt buộc; normative định ra tiêu chí chính danh; mimetic giúp sao chép mô hình từ chi nhánh IC khác. IAF phản ứng: compromise → acquiescence, và giữ được tính chính danh.

## Điểm cần nhớ (Key Takeaways)
1. ERP "chuẩn" là ERP nhúng chín giả định kiểm soát trên vào từng module, không để kiểm soát tách rời.
2. Phân biệt bốn loại kiểm soát (inherent/configurable/security/reporting) để biết cái nào có sẵn, cái nào phải cấu hình, cái nào thuộc phân quyền, cái nào thuộc báo cáo.
3. Giai đoạn gathering & mapping requirements là lúc quan trọng nhất để gắn SoD, access rights và risk framework.
4. Quy trình không customise được = tín hiệu reengineer; localise chỉ cho phần hợp pháp (thuế, luật địa phương).
5. Phần lớn customise thực tế nằm ở báo cáo — đặc tả báo cáo kiểm soát kỹ ngay từ đầu.
6. Thiết kế mỗi rủi ro với ít nhất một compensating control.

## Ứng dụng cho BA ERP (BA Application)
- Dùng bảng chín giả định kiểm soát làm **checklist nghiệm thu** cho mỗi module: tài liệu phải chỉ rõ chức năng đó hiện thực automation, monitoring, data consistency, integration, multiple controls, preventive, standardisation, transparency, compensating control như thế nào.
- Với mỗi chức năng, đặc tả rõ **danh mục (master data)** chuẩn: standard chart of accounts, sổ cái chuẩn, định dạng dữ liệu thống nhất giữa các đơn vị — đây là nền của data consistency và consolidation.
- Đặc tả **phân quyền/tham số hệ thống** ở mức code được: với mỗi role, authorisation profile cho phép xem/sửa/xóa bản ghi nào; định nghĩa các quy tắc SoD và report dò xung đột SoD chạy định kỳ.
- Phân loại mọi kiểm soát trong spec theo bốn loại SAP (inherent vs configurable vs security vs reporting) để dev biết cái nào phải code, cái nào chỉ cấu hình.
- Luôn kèm bộ **báo cáo kiểm soát** trong spec: discrepancy/reconciliation, exception, red-alert, báo cáo xung đột SoD — và nêu rõ format, khối lượng, cách phân loại dữ liệu vì báo cáo chuẩn thường không đủ.
- Yêu cầu **audit trail** cho mọi giao dịch: lưu ai/khi nào/tại sao, truy ngược về GL và sub-ledger — biến minh bạch thành yêu cầu phi chức năng bắt buộc.
- Khi quy trình khách hàng lệch chuẩn ERP, ghi rõ trong tài liệu quyết định: *reengineer* (về chuẩn, làm cho auditable) hay *customise/localise* (chỉ khi do luật địa phương), kèm lý do — tránh tài liệu mơ hồ gây conflict.

## Liên hệ (Connects To)
- **Ch 4**: hiện thực hóa RQ2 (control assumptions) và khung phản ứng chiến lược của Oliver.
- **Ch 5**: dữ liệu chương này được phân tích bằng directed content analysis với bộ mã từ khung Ch4.
- **Ch 7–9**: so sánh cross-case với công ty quốc nội (NC) và các tình huống khác theo literal/theoretical replication.
- **SOX (Sec 302, 404), COSO, IIA Standards, Segregation of Duties**: các chuẩn kiểm soát ngoài mà chín giả định kiểm soát của ERP ánh xạ tới.
