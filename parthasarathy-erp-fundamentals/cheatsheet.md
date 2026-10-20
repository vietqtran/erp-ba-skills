# Cheatsheet — Phán đoán chuẩn ERP (Parthasarathy)

Trang tham khảo nhanh để *quyết định*, không phải tra nghĩa. Giữ bên cạnh khi viết spec ERP.

## Quy tắc quyết định (Decision rules)

| Khi... | Hãy... | Vì... |
|---|---|---|
| Đổi nền tảng công nghệ | Đổi luôn quy trình để khớp phần mềm (*fit org around software*) | Process change là tất yếu; giữ quy trình cũ làm dự án gãy (Ch5) |
| Phát sinh nhu cầu customize | Giữ tối thiểu, **không sửa base** | Customize cao = lợi ích ERP thấp + bảo trì/nâng cấp tốn (Ch5) |
| Cost-benefit bất lợi | **Dừng dự án** | Là analysis để quyết định, không phải justification (Ch4) |
| Tổ chức demo vendor | Ra điều kiện danh sách **50–100 chức năng** bắt buộc demo | Khách làm chủ thay vì bị vendor dẫn dắt (Ch4) |
| Rủi ro thất bại cao | Chọn Location/Module-wise, không Big Bang | Giảm chi phí/rủi ro, có feedback trước khi mở rộng (Ch5) |
| Chỉ cần thay một phần | Mua đúng module, không cả bộ | Giảm chi phí, thời lượng, rủi ro, kháng cự (Ch3) |
| Hoạch định vật tư | Dùng MPS + nổ BOM sinh order | Nhu cầu linh kiện là *dependent demand* phải tính, không dự báo (Ch2) |
| Đơn tăng đột biến vượt dự báo | Phân loại *abnormal* + ưu tiên | Giữ đơn/khách quan trọng (Ch3) |
| Viết tài liệu ERP | Mô tả luồng dữ liệu tự cập nhật liên module | Integration là ưu điểm số một, bản chất ERP (Ch1) |
| Đặc tả chức năng ERP | Bổ sung control procedure + audit trail + phân quyền | ERP có thể không để chứng từ, lỗi lan rộng khó phát hiện (Ch5) |
| Chọn OS "miễn phí" | Tính cả TCO (quản trị + nhân lực) | Chi phí thực có thể cao hơn kỳ vọng (Ch6) |
| Cần dự báo/tối ưu chuỗi | Dùng SCM; giao dịch thì dùng ERP | ERP một chiều/transaction; SCM hai chiều/tối ưu (Ch7) |
| Chọn phương thức vận chuyển | Đánh đổi chi phí ship ↔ chi phí tồn kho | Ship rẻ (tàu/sắt) buộc giữ tồn kho lớn + kế hoạch sớm (Ch7) |
| Triển khai CRM | Chiến lược lấy khách làm trọng tâm *trước*, công nghệ sau | CRM gãy nếu bỏ qua văn hóa/tổ chức (Ch8) |
| Phân bổ nguồn lực chăm khách | Ưu tiên khách sinh lời | Mục tiêu tối thượng của CRM là tối ưu profitability (Ch8) |
| Thiết kế ERP hiện đại | Chuẩn hóa + tách business rules (validation ≠ processing) | Kiến trúc tốt xoay quanh đóng gói/điều phối rule (Ch9) |
| Chọn vendor ERP | Ưu tiên phù hợp ngành dọc + **ít tùy biến nhất** | Triển khai nhanh/rẻ, hợp lộ trình (Ch10) |
| Đo thành công ERP | Lập bộ KPI, đo trước/sau | Lợi ích phải đo được, không nói chung chung (Ch11) |
| Quy trình chưa thấu hiểu | Mô hình hóa UML trước khi code | Không hiểu quy trình chỉ automation, không reengineering (Ch12) |
| Đặc tả "ai làm gì" | Dùng swimlanes trong activity diagram | Chỉ rõ role chịu trách nhiệm từng việc (Ch12) |

## Bảng đánh đổi (Trade-off tables)

**Cách triển khai**
| Approach | Lợi ích | Rủi ro / chi phí |
|---|---|---|
| Big Bang | Lợi ích đầy đủ, nhanh đạt tích hợp | Rủi ro cao khi hệ mới trục trặc |
| Location-wise | Giảm rủi ro, có feedback trước khi mở rộng | Chỉ lợi ích từng phần, kéo dài |
| Module-wise | Chi phí/rủi ro/kháng cự thấp nhất | Chỉ đạt tích hợp từng phần |

**ERP vs SCM** — ERP: giao dịch, một chiều, chuẩn hóa quy trình, giảm chi phí/thời gian/tồn kho. SCM: dự báo & hỗ trợ quyết định, hai chiều, khác biệt hóa, tăng doanh thu/độ tin cậy/khả năng đáp ứng.

## Ngưỡng & con số mặc định (Thresholds)

- Trọng số chọn vendor: Reputation **26%** · Functionality **24%** · Project cost **23%** · Complete solution **16%** · Future maintenance **11%** (Ch4).
- Chi phí ẩn: training contingency **~25%/năm** chi phí đào tạo ban đầu; miscellaneous **~10%** (gần như luôn bị vượt) (Ch4).
- Giữ tồn kho tốn **20–40%** giá trị hàng → quản tồn kho là đòn bẩy lớn nhất (Ch7).
- Migration ERP trung bình **~7 tháng**; nhân lực IT dồn cao nhất ở pha triển khai (Ch6).
- SAP dẫn đầu thị phần license ERP **~25%** (2002); Oracle ~7% (Ch10).
- KPI điển hình trước→sau: tồn kho **90→15 ngày**; on-time delivery **75→99%**; supplier on-time **30→>80%**; inventory turns **~2→6**/năm; chốt sổ **3 tuần→<1 tuần**; order cycle **−80%**; go-live SME **45–90 ngày** (Ch11).
- Benefits realization: hiện rõ sau **vài tháng tới ~1 năm**, không tức thì (Ch5).

## Dấu hiệu nhận biết rủi ro (Tells & smells)

- Chức năng mô tả rời rạc, không có luồng liên module → thiếu bản chất tích hợp ERP (Ch1).
- Nhu cầu linh kiện được "dự báo" thay vì tính từ BOM → sai nghiệp vụ MRP (Ch2).
- Spec không có audit trail / phân quyền / tham số hệ thống → thiếu NFR control của ERP (Ch5).
- Yêu cầu customize nhiều "cho giống hệ cũ" → cờ đỏ: lợi ích ERP tụt, bảo trì tốn (Ch5).
- Mục tiêu mơ hồ + thiếu cam kết lãnh đạo + đào tạo yếu → rủi ro thất bại hàng đầu (Ch5, Ch11).
- SD thiếu Master Data Management → thiếu key element bắt buộc (Ch3).

## Checklist bao phủ chức năng (một ERP đầy đủ)

Mỗi sản phẩm ERP cần: **phần mềm/module · danh mục (master data) · nghiệp vụ · phân quyền & tham số hệ thống · báo cáo**. Danh mục chức năng con để kiểm "cover đủ":
- **Finance** (5): Accounting · Investment mgmt · Cost controlling · Treasury mgmt · Planning & forecasting.
- **HR**: Managerial (Planning/Organizing/Directing/Controlling) · Operative (Employment/HRD/Compensation).
- **MM** (7): Inventory · MRP · Purchasing · Warehouse · Vendor evaluation · Invoice verification · Product costing.
- **SD** (6): Selling · Shipping · Billing · Master Data Mgmt · Order Mgmt · Pricing.
- **CRM** (3): Operational · Analytical · Collaborative.
