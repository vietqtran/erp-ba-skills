# Chương 10: Thiết kế ERP — Chọn mô hình, chứng từ và quy trình chuẩn (Designing ERP Systems: Choosing Standard Models, Artifacts, and Processes)

## Ý tưởng cốt lõi (Core Idea)
ERP buộc doanh nghiệp chọn một bộ **MAPs** — **Models, Artifacts, Processes** (mô hình tổ chức, chứng từ/tạo tác như danh mục nhà cung cấp/sản phẩm và hệ thống đánh số, quy trình như quản lý đơn hàng) dùng **chung và toàn cục** cho mọi đơn vị, thay vì mỗi đơn vị tự chọn như thời legacy. Việc chọn MAPs chung là quyết định cấp doanh nghiệp, mang tính chính trị vì mỗi lựa chọn làm lợi cho đơn vị này hơn đơn vị khác; cần phương pháp ra quyết định nhóm có hệ thống.

## Framework được giới thiệu (Frameworks Introduced)
- **MAPs (Models, Artifacts, Processes)** — ba loại đối tượng chuẩn phải thống nhất: models (mô hình tổ chức), artifacts (danh mục nhà cung cấp/khách hàng/sản phẩm, chart of accounts, hệ thống đánh số), processes (quy trình nghiệp vụ như order management, reserve inventory, month-end close).
- **Nguyên tắc "common... and global" + "input by many, design by few"** — MAPs phải chung và toàn cục nhưng được lấy ý kiến từ nhiều bên rồi thiết kế bởi số ít.
- **Nguồn gốc MAPs chuẩn** — portfolio dựng từ: (1) MAPs hiện có của từng division (mỗi cái là một ứng viên); (2) best practice database của ERP và của consultant; (3) MAPs lai (hybrid) kết hợp nhiều nguồn; (4) ở ngành đặc thù, MAPs bắt buộc theo quy định (Litton: biểu mẫu chính phủ, progress payment cho hợp đồng liên bang). Một nhóm đa chức năng quyết định.
- **Bốn phương pháp chọn giữa các chuẩn (group choice rules)**:
  - **Majority Vote** — "democratic governance": chọn MAP x thay y nếu nhiều division thích x hơn y.
  - **Borda Rule** — mỗi thành viên xếp hạng các phương án; hạng 1 được n điểm, hạng 2 được (n−1) điểm...; phương án tổng điểm cao nhất thắng. Litton dùng cách này: định nghĩa "key features" ngành (defense business processes, financial management), chấm điểm từng vendor theo khả năng đáp ứng, cộng điểm để chọn.
  - **Pareto Optimality** — chọn phương án mà không phương án nào khác có thể làm một division hài lòng hơn mà không làm division khác kém hài lòng đi.
  - **Dictatorship** — một division (thường là corporate office hoặc division lớn nhiều quyền lực) đơn phương quyết; Owens Corning (đội Toledo), Colgate (áp đặt quy trình cho nhà cung cấp dùng chung SAP).

## Khái niệm chính (Key Concepts)
- **Common / global MAPs**: dùng chung cho mọi đơn vị; menu giống nhau dù ở đâu (Colgate).
- **Product list (ví dụ artifact chuẩn)**: định danh duy nhất cho mỗi sản phẩm; nếu lấy danh mục của một division làm chuẩn thì division đó ít chi phí đào tạo nhất, division khác tốn đào tạo và có thể kém khớp.
- **Variance corporate vs division**: tỷ lệ MAPs cho division tự cấu hình rất nhỏ — Microsoft: HQ cấu hình 3.000 bảng, local ~30 bảng (~1%).
- **Strategic / political behavior**: ra quyết định nhóm trở thành chính trị vì lợi ích toàn cục và lợi ích division xung đột.

## Mô hình tư duy (Mental Models)
- Xem chuẩn hóa MAPs là đánh đổi: lợi ích toàn cục (hợp nhất dữ liệu, một view, phản hồi khách hàng nhanh) đổi lấy mất năng lực tùy biến tại chỗ ("common view may not be optimum for individual divisions").
- Nhận diện động cơ của mỗi division để dự đoán hành vi: **maximize corporate benefit** / **minimize divisional change cost** (giữ chuẩn của mình, hoặc chọn chuẩn gần nhất với mình) / **respond to competition** (chịu reengineering mạnh để khỏi bị outsource).
- "Không phương pháp nào tốt nhất trong mọi hoàn cảnh; mỗi phương pháp đều thất bại ở một tình huống" → chấp nhận việc chọn MAPs là quá trình chính trị, cần làm có hệ thống.

## Điều cần tránh (Anti-patterns)
- **Để mỗi division giữ bộ artifact riêng trong ERP**: tái tạo lại sự phân mảnh mà ERP muốn xóa, mất common view.
- **Danh mục chung dài hơn mức cần** (mã sản phẩm gấp đôi số chữ số): nhập liệu lâu gấp đôi, tăng lỗi, giảm chất lượng dữ liệu.
- **Áp chuẩn mà không lường chi phí thay đổi khác nhau giữa các division**: gây xung đột cảm xúc ("đội của tôi đã muốn giết người nếu nhượng quyền kiểm soát giá cho máy tính").

## Ví dụ minh họa (Worked Example)
**Litton Data Systems chọn ERP bằng Borda-like** (triển khai PeopleSoft/BAAN cho ngành quốc phòng):
1. Định nghĩa "key aerospace and defense features and thrusts":
   - Defense business processes: biểu mẫu chính phủ; progress payments; moving average actual costs.
   - Financial management: lập ngân sách & hoạch định nguồn lực cấp division; cost schedule control; nhiều mức labor và burden.
2. Chấm điểm và xếp hạng từng vendor ERP theo khả năng đáp ứng mỗi feature; hạng cao được nhiều điểm.
3. Cộng tổng điểm → chọn hệ thống theo thứ hạng cuối. Vì Litton làm hợp đồng liên bang, MAPs bắt buộc theo chuẩn chính phủ được đưa vào như yêu cầu cứng.

Tương phản nguồn MAPs — **Nestlé (US)**: quyết dùng MAPs chung cho cả 3 division; MAPs hiện có của mỗi division + best practice của SAP và của consultant làm ứng viên; có trường hợp dựng MAPs lai; một nhóm đa chức năng chốt chuẩn.

## Điểm cần nhớ (Key Takeaways)
1. Chất lượng MAPs tác động trực tiếp tới thành bại của ERP — MAPs tốt đẩy hiệu năng, MAPs kém kéo lùi cả doanh nghiệp.
2. ERP cần MAPs chung vì: phần mềm yêu cầu, phản hồi khách hàng tốt hơn, giành lại quyền kiểm soát quy trình, cần một view chung, tạo giá trị và giảm chi phí.
3. Portfolio chuẩn đến từ MAPs hiện có của các division + best practice của ERP/consultant + bản lai; đôi khi bị ràng buộc bởi quy định ngành.
4. Có bốn luật chọn nhóm (Majority Vote, Borda, Pareto, Dictatorship) — không cái nào tối ưu mọi lúc; chọn MAPs vẫn là quá trình chính trị.
5. Tỷ lệ MAPs cho local tự cấu hình thường rất nhỏ (cỡ 1%); phần còn lại là chung toàn cục.

## Ứng dụng cho BA ERP (BA Application)
- Khi viết spec master data, coi mỗi danh mục dùng chung (vendor list, customer list, product list, chart of accounts, numbering scheme) là một **quyết định chuẩn hóa cấp doanh nghiệp** cần ghi rõ: nguồn chuẩn được chọn, division nào chịu chi phí thay đổi, và ai được cấu hình phần nào.
- Ghi rõ tỷ lệ tham số/bảng mà đơn vị địa phương được tự cấu hình vs phần chốt cứng toàn cục (mô hình Microsoft 3.000/30) — đây là một quyết định thiết kế, không bỏ ngỏ.
- Khi mô tả quy tắc ra quyết định chọn chuẩn, nêu rõ phương pháp (Majority/Borda/Pareto/Dictatorship) và lý do, vì nó ảnh hưởng tính chấp nhận và xung đột.
- Cảnh báo trong spec về đánh đổi: danh mục/mã dài gây chậm nhập liệu và tăng lỗi; common view có thể không tối ưu cho division.
- Đưa các MAPs bắt buộc theo quy định ngành (ví dụ báo cáo hợp đồng chính phủ) thành yêu cầu cứng trong tài liệu, không để thương lượng.

## Liên hệ (Connects To)
- **Ch 9**: "to be" khi sửa phần mềm ít chính là bài toán chọn MAPs từ portfolio.
- **Ch 8**: MAPs là đối tượng của requirements analysis.
- **Ch 5 & 6**: artifacts (danh mục) và dữ liệu dùng chung là nền cho data warehouse và báo cáo.
- **Group decision theory**: Borda rule, Pareto optimality là công cụ lý thuyết lựa chọn nhóm áp dụng vào chọn chuẩn ERP.
