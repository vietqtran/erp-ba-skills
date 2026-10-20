# Chương 7: Quản trị Chuỗi cung ứng (Supply Chain Management - SCM)

## Ý tưởng cốt lõi (Core Idea)
**Supply Chain Management (SCM)** — quản trị chuỗi cung ứng là việc điều phối dòng hàng hóa, dịch vụ, thông tin và tài chính khi chúng di chuyển từ nguyên liệu thô → nhà cung cấp linh kiện → nhà sản xuất → nhà bán buôn → nhà bán lẻ → người tiêu dùng. ERP và SCM bổ sung cho nhau: ERP vượt trội ở quản lý giao dịch, còn SCM mạnh ở dự báo và hỗ trợ ra quyết định tối ưu.

## Framework được giới thiệu (Frameworks Introduced)
- **Four elements influencing SCM** — bốn yếu tố cấu thành chuỗi cung ứng.
  - Cách làm: **Location** (vị trí cơ sở sản xuất/kho/nguồn cung quyết định đường đi của hàng), **Production** (quyết định sản xuất gì, ở nhà máy nào, nhà cung cấp nào phục vụ), **Inventory** (giữ tồn kho đệm cho bất định; xác định điểm đặt hàng, lượng đặt tối ưu, tồn an toàn), **Transportation** (chọn phương thức vận chuyển, đánh đổi chi phí vận chuyển với chi phí tồn kho gián tiếp).
- **Three flows of the supply chain** — ba dòng chảy: **Product flow** (dòng hàng gồm cả hàng trả về), **Information flow** (truyền đơn hàng, cập nhật trạng thái giao), **Financial flow** (điều khoản tín dụng, thanh toán, quyền sở hữu hàng).
- **Four areas of SCM** — bốn mảng SCM: **Supply Chain Networking**, **Planning**, **Execution**, **Co-ordination** — có thể dùng riêng hoặc tích hợp.
- **Strategic / Tactical / Operational decision making** — ba cấp ra quyết định: dài hạn (thiết kế chuỗi) / trung hạn (phân bổ nguồn lực) / ngắn hạn (vận hành hằng ngày).

## Khái niệm chính (Key Concepts)
- **Computer-Integrated SCM Systems**: chuyển trọng tâm từ hệ thống sản xuất tích hợp máy tính sang hệ thống chuỗi cung ứng tích hợp máy tính; dùng CNC, robot, AGV, AMTS, ASRS.
- **CAD / CAM**: **Computer-Aided Design** (thiết kế sản phẩm bằng đồ họa máy tính tương tác) và **Computer-Aided Manufacturing** (tích hợp vận hành các máy điều khiển bằng máy tính, online và offline).
- **Key Performance Indicators (KPI)**: chỉ số hiệu năng dựa trên dữ liệu lịch sử, được tinh chỉnh theo thời gian.
- **Quality of Service (QoS)**: tham số để xây lợi thế khác biệt khi hợp tác chuỗi.

## Mô hình tư duy (Mental Models)
- Trong chuỗi, **vật liệu chảy xuôi** (từ nguồn cung tới khách hàng) còn **thông tin chảy ngược** (từ khách hàng về nguồn cung) — thiết kế dòng thông tin ngược chiều với dòng vật liệu.
- Coi ERP là "evaluative/transaction-focused, một chiều" còn SCM là "prescriptive, hỗ trợ quyết định, hai chiều": đừng kỳ vọng ERP một mình giải quyết tối ưu chuỗi.
- Một doanh nghiệp có thể dùng chiến lược khác nhau cho **inbound** và **outbound supply chain**, và theo từng nhóm sản phẩm: hãy tiếp cận theo danh mục (portfolio approach).

## Điều cần tránh (Anti-patterns)
- **Kỳ vọng quá mức ở ERP cho SCM mở rộng**: ERP thế hệ đầu được thiết kế để tích hợp một doanh nghiệp đơn lẻ, nên hạn chế khi đơn vị phân tích trở thành mạng lưới tổ chức.
- **Dùng sản phẩm chung chung (generic) làm lợi thế cạnh tranh**: sản phẩm chung chỉ dùng thông tin công khai, không tạo khác biệt — cần nhìn sâu vào hệ sinh thái chuỗi của chính mình.
- **Kiến trúc đóng, phi mô-đun**: khiến ERP thiếu linh hoạt trước nhu cầu chuỗi luôn thay đổi.

## Bảng tham chiếu (Reference Tables)
So sánh ERP và SCM:

| Tiêu chí | ERP | SCM |
|---|---|---|
| Thế mạnh | Quản lý giao dịch | Dự báo & hỗ trợ quyết định |
| Phạm vi | Liên kết quy trình trong tổ chức | Trải toàn chuỗi cung ứng |
| Vai trò dữ liệu | Sinh dữ liệu giao dịch | Khai thác dữ liệu để ra quyết định |
| Bản chất | Tuyến tính, tương tác, một chiều | Dựa trên ràng buộc, tối ưu, hai chiều |
| Tác động | Chuẩn hóa quy trình, giảm chi phí/thời gian/tồn kho | Khác biệt hóa quy trình, tăng doanh thu/độ tin cậy/khả năng đáp ứng |

*Lưu ý trích xuất: đánh số mục nhảy từ 7.8 sang 7.11 (mục 7.7 "SCM Model", 7.9, 7.10 bị xáo trộn/mất một phần; có đoạn lạc về "software development lifecycle" chèn nhầm). Phần mô hình "ba trụ cột: Processes / Organizational structures / Enabling technologies" còn sót lại.*

## Ví dụ minh họa (Worked Example)
Quy trình ra quyết định SCM bốn bước mà tác giả trình bày:
- **Bước 1 — Location**: chọn vị trí địa lý cho cơ sở sản xuất/điểm tồn/nguồn cung; hệ quả dài hạn, ảnh hưởng doanh thu, chi phí, mức dịch vụ.
- **Bước 2 — Production**: quyết định "sản xuất gì / khi nào / bao nhiêu"; chiến lược chọn cơ sở & nguồn cung, chiến thuật là hoạch định tổng hợp, vận hành là lập lịch chi tiết + kiểm soát chất lượng + cân bằng tải.
- **Bước 3 — Inventory**: giữ tồn kho tốn 20–40% giá trị hàng, nên quản lý hiệu quả là then chốt; chính sách là chiến lược, nhập–xuất hằng ngày là vận hành.
- **Bước 4 — Transportation**: chọn phương thức vận chuyển tới thị trường; gắn chặt với quyết định tồn kho (ship bằng tàu/đường sắt rẻ nhưng chậm → phải lập kế hoạch sớm và giữ tồn kho lớn hơn).

## Điểm cần nhớ (Key Takeaways)
1. SCM = điều phối bốn yếu tố (Location, Production, Inventory, Transportation) qua ba dòng chảy (hàng, thông tin, tài chính).
2. ERP sinh giao dịch; SCM biến giao dịch thành quyết định tối ưu — hai hệ bổ sung chứ không thay thế.
3. Ra quyết định chuỗi phân theo ba cấp: chiến lược / chiến thuật / vận hành.
4. Giữ tồn kho tốn 20–40% giá trị → quản lý tồn kho là đòn bẩy lớn nhất.
5. ERP thế hệ đầu còn hạn chế cho chuỗi mở rộng liên tổ chức; cần tùy biến theo hệ sinh thái riêng.

## Ứng dụng cho BA ERP (BA Application)
- Khi đặc tả nghiệp vụ logistics, mô tả rõ ba dòng chảy (product/information/financial) và lưu ý dòng thông tin chảy ngược chiều dòng hàng — đây là cơ sở thiết kế luồng cập nhật trạng thái đơn hàng.
- Phân loại mỗi quyết định trong spec theo cấp strategic/tactical/operational để xác định ai (role) ra quyết định và tần suất.
- Đưa KPI (tồn kho, giao đúng hạn, hiệu suất nhà cung cấp) thành tiêu chí nghiệm thu đo được cho chức năng chuỗi cung ứng.
- Ghi rõ ranh giới ERP vs SCM trong spec: chức năng dự báo/tối ưu cần module SCM, tránh gán nhầm cho ERP lõi.

## Liên hệ (Connects To)
- **Ch 3 (ERP Modules)**: module Materials Management, Plant Maintenance liên quan tồn kho và sản xuất.
- **Ch 8 (ERP và CRM)**: SCM và CRM là mở rộng của ERP ra bên ngoài (nhà cung cấp và khách hàng).
- **Ch 9 (ERP và .NET)**: lập kế hoạch vật tư–năng lực thời gian thực qua web services across chuỗi.
