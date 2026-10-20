# Chương 15: Rủi ro ERP — Các yếu tố thành công và thất bại (ERP Risk: Success and Failure Factors)

## Ý tưởng cốt lõi (Core Idea)
**Risk** (rủi ro) là một phơi nhiễm (exposure): xử lý tốt thì thành success factor, xử lý kém thì thành failure factor — hai mặt của cùng một rủi ro, kèm trade-off risk/return (phơi nhiễm nhiều hơn có thể cho lợi ích lớn hơn). Chương dựng một **Risk Matrix** để nhận diện rủi ro theo hai chiều: **giai đoạn trong vòng đời ERP** × **loại rủi ro (technical, business, organizational)**. Khảo sát cho thấy thứ tự mức độ: **organizational > business > technical**.

## Framework được giới thiệu (Frameworks Introduced)
- **Risk Matrix (hai chiều)** — trục 1: vị trí trong life cycle (quyết định go/no-go → chọn hệ thống → thiết kế → triển khai → go-live → sau go-live, gồm cả training); trục 2: loại rủi ro.
  - **Technical risk** — từ công nghệ xử lý thông tin (OS, relational database, client server, network, software). Dễ sửa nhất, thường chỉ cần nâng cấp (thêm CPU server).
  - **Business risk** — từ (1) lựa chọn MAPs, (2) MAPs chạy tốt đến đâu trong tổ chức, (3) MAPs hỗ trợ tương tác với đối tác đến đâu; cùng với năng lực cạnh tranh.
  - **Organizational risk** — từ con người, cơ cấu tổ chức, môi trường chọn và triển khai hệ thống. Rủi ro cao nhất.
- **Links × Independence (Figure 15.2)** — ma trận 2×2: ERP standalone hay nối hệ khác × ERP có môi trường riêng hay dùng chung. Nối hệ khác làm tăng độ phức tạp và rủi ro, **nhưng cũng tăng return cao nhất** (ERP sinh lợi lớn nhất khi tích hợp); dùng chung môi trường kéo theo mọi rủi ro của hệ khác.

## Khái niệm chính (Key Concepts)
- **Technical risk theo life cycle**: ước lượng thiếu năng lực tính toán (Cisco thiếu capacity lúc đầu); network constraint (10 giây/giao dịch = 6 giao dịch/phút = ~3.600/ngày — không đủ cho firm hàng triệu giao dịch/năm → phải "matching" network với processing requirement); database quan hệ lưu một chỗ nên backup là sống còn.
- **Business risk — resources & volume**: thiếu nguồn lực là một trong các rủi ro lớn nhất (ERP tốn hàng triệu–hàng trăm triệu USD); hệ thống không chịu nổi volume (FoxMeyer chỉ xử lý 10.000 invoice line item/đêm trong khi cần 420.000).
- **Organizational risk — top management & domain buy-in**: "lack of executive support" là lý do chính của nhiều thất bại (US government, Perrier); cần cả domain manager buy-in vì thay đổi quy trình lớn (Microsoft thành công chỉ khi lãnh đạo tài chính buy-in). Nhưng thiếu hậu thuẫn đỉnh không luôn thất bại (Siemens Power vẫn thành công).
- **Cultural fit**: ERP có thể bị từ chối nếu không hợp văn hóa; "phần mềm một mình không đổi được văn hóa" (Davenport) — quản lý phải nỗ lực.
- **Bullet-proofing**: mainframe được bảo vệ chặt (giới hạn truy cập vật lý/ảo, có backup); môi trường client server dễ bị bỏ sót kiểm soát nên dễ tổn thương hơn.

## Mô hình tư duy (Mental Models)
- Xem mỗi rủi ro là hai mặt: hỏi "nếu xử lý tốt đây là success factor gì, nếu hỏng là failure factor gì" cho từng ô của ma trận.
- Vì organizational > business > technical, dồn chú ý vào con người/cơ cấu/văn hóa trước, đừng để technical (dễ sửa bằng nâng cấp) chiếm hết sự chú ý.
- Giảm rủi ro công nghệ bằng cách **theo cấu hình đã chạy được trước đó**: "chính con người làm khó mình khi chọn sai công nghệ hoặc cố đẩy giới hạn".
- Xem việc chọn vendor/hardware trong "gia đình" công ty (Siemens chọn Pyramid/SNI) như cách giảm rủi ro nguồn cung.

## Điều cần tránh (Anti-patterns)
- **Nối nhiều hệ cùng lúc với thay đổi lớn** (FoxMeyer: SAP + warehouse management + chuyển kho sang robotics đồng thời): độ phức tạp khổng lồ, góp phần làm engagement thất bại và phá sản.
- **Project team tự quyết các lựa chọn thiết kế vốn thuộc process owner/management**: quy trình không chạy như kỳ vọng, không khớp các quy trình khác.
- **Ước thấp computing/network capacity**: hệ chậm, không chạy như kỳ vọng; cần matching giữa network và processing requirement.
- **Để cost vượt và tiến độ trễ** (Hershey SAP–Siebel–Manugistics trễ 3 tháng → earnings lệch 10%, gián đoạn nhận đơn & phân phối; APS bỏ hệ vì trễ 1 năm do vendor phải phát triển quá nhiều cho khớp quy trình).
- **Để nhân sự dự án chủ chốt bị đối thủ hút mất sau triển khai**: người ở lại không hiểu triển khai → thất bại; cần lộ trình giữ người.

## Bảng tham chiếu (Reference Tables)
Bảng 15.1 — Cảm nhận mức rủi ro dự án ERP (%, trung bình 1998–1999, Austin & Cotteleer):

| Mức rủi ro | Technical | Business | Organizational |
|---|---|---|---|
| Very low | 10.5 | 4.5 | 1.5 |
| Low | 22.5 | 23.0 | 8.5 |
| Moderate | 39.5 | 32.5 | 18.5 |
| High | 15.0 | 26.0 | 37.5 |
| Very high | 11.5 | 14.5 | 35.0 |

→ Organizational dồn về High/Very high (72.5%), Business ở giữa, Technical dồn về Low/Moderate.

Risk Matrix (khung) — mỗi ô là giao của một giai đoạn life cycle × một loại rủi ro, dùng để liệt kê rủi ro có hệ thống:

| Giai đoạn | Technical | Business | Organizational |
|---|---|---|---|
| Quyết định go/no-go | vị thế công nghệ hiện tại | đủ nguồn lực? rationale | hậu thuẫn lãnh đạo & domain |
| Chọn hệ thống | chọn hardware/OS | volume, political, requirement đổi | chọn consultant |
| Thiết kế | — | political, process-owner quyết | org model đổi quyền lực |
| Triển khai | computing/network capacity | trễ & vượt chi phí | đổi lương/cơ cấu |
| Sau go-live | — | stabilization, mất khách/vendor | cultural fit |
| Training & personnel | kỹ năng công nghệ mới | training thiếu | mất người, data input dịch về nguồn |

## Ví dụ minh họa (Worked Example)
**FoxMeyer Drugs — thất bại ERP kinh điển (nhiều loại rủi ro cùng lúc)**:
- **Technical/complexity**: không chỉ triển khai SAP mà SAP + phần mềm warehouse management (cần tích hợp), lại đồng thời chuyển kho chính từ thâm dụng lao động sang robotics → độ phức tạp khổng lồ.
- **Business/volume**: hệ thống chỉ xử lý được 10.000 invoice line item/đêm trong khi yêu cầu 420.000 — không chịu nổi khối lượng.
- **Business/resources**: dự toán $65 triệu cho SAP; FoxMeyer phá sản và kiện SAP + Andersen Consulting, cho rằng SAP là một phần nguyên nhân. Cuối cùng SAP được chính công ty mua lại FoxMeyer triển khai.
- Đối chiếu — **Geneva Steel** phá sản ngay hôm sau khi hệ SAP $8 triệu go-live (rủi ro độc lập với ERP), cho thấy không phải mọi thất bại kinh doanh đều do ERP.
- Đối chiếu **Siemens Power**: không có hậu thuẫn đỉnh nhưng vẫn triển khai đúng hạn, đúng chi phí và dùng nhiều — minh họa rủi ro là xác suất, không tất định.

## Điểm cần nhớ (Key Takeaways)
1. Mỗi rủi ro có hai mặt success/failure; quản trị rủi ro là xử lý phơi nhiễm để nghiêng về mặt success, chấp nhận trade-off risk/return.
2. Dùng Risk Matrix (life cycle × technical/business/organizational) để liệt kê rủi ro có hệ thống, không bỏ sót ô nào.
3. Organizational > business > technical: ưu tiên con người, cơ cấu, văn hóa; technical dễ sửa nhất.
4. Nối hệ và dùng chung môi trường tăng cả rủi ro lẫn return — tích hợp cho lợi ích lớn nhất nhưng đắt nhất về phức tạp.
5. Kiểm tra sớm: đủ nguồn lực? hệ chịu nổi volume? có hậu thuẫn lãnh đạo + domain? network khớp processing requirement? có giữ được người sau triển khai?

## Ứng dụng cho BA ERP (BA Application)
- Thêm một mục **risk register** vào tài liệu dự án, tổ chức theo Risk Matrix (giai đoạn × technical/business/organizational), mỗi rủi ro ghi rõ success factor nếu xử lý tốt / failure factor nếu hỏng.
- Trong NFR, đặc tả rõ **volume requirement** cụ thể (ví dụ số invoice line item/đêm) và yêu cầu network/computing capacity khớp — FoxMeyer thất bại vì thiếu con số này.
- Ghi rõ ai quyết thiết kế quy trình: process owner/management chứ không phải project team, để tránh quy trình lệch kỳ vọng.
- Đặc tả yêu cầu backup cho database quan hệ (lưu một chỗ) và control cho môi trường client server/network tương đương mức "bullet-proofing" của mainframe.
- Đưa yêu cầu về top-management & domain buy-in, culture-change effort, và kế hoạch giữ nhân sự "hot skills" vào phần tổ chức của tài liệu — đây là nhóm rủi ro cao nhất.
- Cảnh báo trong tài liệu khi phạm vi gồm nhiều hệ tích hợp đồng thời (như FoxMeyer) rằng độ phức tạp nhân lên là failure factor hàng đầu.

## Liên hệ (Connects To)
- **Ch 7**: technology/strategy/business-process/competitive rationale làm cơ sở cost–benefit và đánh giá.
- **Ch 8–9**: chọn hệ thống và small-r/big-R là nguồn của business & organizational risk (đổi lương, đổi cơ cấu).
- **Ch 11**: trễ & vượt chi phí triển khai (Hershey, APS) là business risk.
- **Ch 12 & 13**: stabilization, implementation compromise, và training thiếu là các ô rủi ro theo life cycle.
- **Risk/return, balanced scorecard**: khung đánh giá và quản trị rủi ro xuyên suốt dự án.
