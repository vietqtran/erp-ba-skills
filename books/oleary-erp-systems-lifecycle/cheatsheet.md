# Cheatsheet — phán đoán ERP cho BA (O'Leary, 2000)

Trang tham khảo nhanh: luật quyết định, bảng đánh đổi, ngưỡng số. Giữ bên cạnh khi viết tài liệu ERP.

## Vòng đời ERP (định vị tài liệu đang viết)
Deciding to Go ERP → Choosing a System → Designing (đổi quy trình hay phần mềm; chọn MAPs chuẩn) → Implementing (big bang/phased) → After Go-Live → (Training xuyên suốt).

## Luật quyết định (Khi X → làm Y, vì Z)
| Khi... | Làm... | Vì... |
|---|---|---|
| Cần đổi năng lực phần mềm | Đặt **switch setting/tham số** trước, tùy biến mã sau | Tùy biến tốn chi phí 3 lần (sửa/nâng cấp/hỗ trợ) + cản nâng cấp (Ch 2, 9) |
| Gói chủ đạo đáp ứng gần đủ | Chọn **một gói duy nhất**, không best of breed | Module khác vendor không khả tương thích; best of breed sinh 6 chi phí ẩn (Ch 3) |
| Thiết kế theo một model ERP | Tuân **giả định của model** (mỗi đơn vị là cost/profit center) | Làm trái gây xung đột, buộc sửa lại mô hình tổ chức (Ch 3) |
| Áp dụng "nhập một lần" | Bắt buộc kèm **data input controls** | Hệ không còn redundancy để bắt lỗi; sai một chỗ lan toàn hệ (Ch 4) |
| Tỉ lệ màn hình ERP/legacy cao + volume lớn | Gộp màn hình hoặc thêm **lớp UI trung gian** | Nếu không, triển khai rất khó, có thể mất đơn (Hydro Agri 6:1, 90s) (Ch 4) |
| Báo cáo chuẩn không đủ | Ưu tiên **intranet/data warehouse** hơn report cứng | Report cứng ngắn hạn, tốn kém, cản nâng cấp (Ch 5) |
| Nhiều người sẽ truy vấn | Lập **capacity planning đầu ra** trước go-live | Nhiều ERP xử lý query như transaction ⇒ quá tải (Ch 5) |
| Nhỏ/ngân sách hạn chế/ép thời gian/quy trình chuẩn | **Technology enabled** reengineering | Nhanh, rẻ, khả thi, đã có bằng chứng chạy được (Ch 6) |
| Quy trình là lợi thế cạnh tranh độc nhất | **Clean slate** reengineering | Technology enabled để lộ thiết kế đối thủ cũng tiếp cận được (Ch 6) |
| Lý do dự án chỉ là Y2K / "đối thủ có" | Bổ sung rationale **business process/strategic** | Chỉ hai loại này cho đặc tả thiết kế + benchmark nghiệm thu (Ch 7) |
| Có process/strategic rationale | Chuyển thành **mục tiêu đo được** = acceptance criteria | Vừa hướng dẫn thiết kế vừa làm thước đo thành công (Ch 7) |
| Định tái cấu trúc mạnh | **Đừng** mô hình "as is" chi tiết | "As is" mất giá trị; fit chặt quy trình cũ cản tái cấu trúc (Ch 8) |
| Đánh giá vendor có trọng số | Chốt **factor + weight TRƯỚC demo** | Chọn sau khi xem chỉ là hợp lý hóa lựa chọn có sẵn (Ch 8) |
| Quy trình generic (tài chính, back office) | Theo chuẩn phần mềm (**small-r**), chỉ sửa cho quy trình khác biệt | Sửa phần mềm tốn chi phí 3 lần (Ch 9) |
| Các division bất đồng về MAPs chung | Dùng một **luật chọn nhóm công khai** (Majority/Borda/Pareto) | Chọn MAPs là quá trình chính trị, dễ bị thao túng (Ch 10) |
| Tổ chức nhỏ/phẳng/kiểm soát lỏng | **Big bang** | Khó duy trì cam kết suốt phased ở tổ chức phẳng (Ch 11) |
| Tổ chức lớn/nhiều tầng/kiểm soát chặt | **Phased** | Rủi ro big bang quá cao; phased giãn đỉnh tài nguyên (Ch 11) |
| Cần tính năng cross-module (ATP) ngay | **Big bang** | Phased trì hoãn tính năng đó tới tận cuối (Ch 11) |
| Lập kế hoạch test | Test **interface/interdependency giữa module**, không chỉ từng module | Các mảnh chạy riêng được vẫn có thể không chạy cùng nhau (SVT 1 Quantum sập) (Ch 11) |
| Đo benefit sau go-live | Đo vào **năm 1-2** | Cần thời gian để lợi ích hiện ra + đủ 1 năm dữ liệu (Ch 12) |
| Mỗi benefit mong muốn | Định nghĩa thành **metric** (baseline + owner + quy về ERP) | Không thì chỉ là goal, không nghiệm thu được (Ch 12) |
| Xếp lịch training | **Trong giờ làm** + dùng **super users** | Giờ training phát tín hiệu mức quan trọng; người quen dạy tạo buy-in (Ch 13) |
| Chọn kênh trao đổi với đối tác | **EDI** nếu volume lớn/đối tác lớn; **WFT** nếu originator ít; ERP-to-ERP chỉ khi chung MAPs | Sai lựa chọn gây double data-entry hoặc chi phí VAN cao (Ch 14) |
| Lập risk register | Ưu tiên rủi ro **organizational > business > technical** | Khảo sát xếp hạng vậy; technical dễ sửa nhất (nâng cấp) (Ch 15) |

## Bảng đánh đổi

**Reengineering quadrant (Ch 9)** — trục: mức đổi tổ chức × mức đổi phần mềm
| | Đổi phần mềm ít | Đổi phần mềm nhiều |
|---|---|---|
| **Đổi tổ chức ít** | small-r: nhanh/rẻ/dự đoán được (Microsoft) | giữ quy trình riêng, khó nâng cấp (Nestlé, Deere) |
| **Đổi tổ chức nhiều** | chuẩn hóa, dễ nâng cấp, cần change mgmt | big-R: đúng ý nhưng cực đắt, maintenance nightmare (Boeing) |

**Technology enabled vs Clean slate (Ch 6)**
| Yếu tố | Clean slate | Technology enabled |
|---|---|---|
| Quy mô / ngân sách / thời gian | lớn / deep pockets / dư | nhỏ-vừa / hạn chế / bị ép |
| Vai trò quy trình | lợi thế cạnh tranh, độc nhất | tương đối chuẩn |
| Chi phí / khả thi | cao / có thể bất khả thi | thấp / luôn khả thi |

**Big bang vs Phased (Ch 11)**
| | Big bang | Phased |
|---|---|---|
| Temporary interface | không cần | cần ở mỗi pha |
| Thời gian / chi phí tiền mặt | ngắn / thấp nếu suôn sẻ | dài / tổng cao hơn |
| Rủi ro | sập toàn hệ, không đường lùi | có legacy fallback |
| Tính năng cross-module | có ngay | trì hoãn |

## Ngưỡng & con số (rule of thumb)
- SAP R/3 có **>1.000 best practices** phải quyết khi triển khai (Ch 1).
- Ngân sách **training ≥ 10%** tổng dự án; thường vượt dự toán (Ch 13).
- **Stabilization period = 3-9 tháng** sau go-live, hiệu năng thường tụt (Ch 12).
- Tỷ lệ tham số local tự cấu hình thường **~1%** (Microsoft: HQ 3.000 bảng / local 30) (Ch 10).
- Mã/danh mục **dài gấp đôi mức cần ⇒ nhập liệu chậm gấp đôi + tăng lỗi** (Ch 10).
- Volume phải khớp hạ tầng: **FoxMeyer xử lý 10.000 vs cần 420.000** invoice line item/đêm ⇒ thất bại (Ch 15).
- Quantum virtual data warehouse: **40.000 bảng → 4.000 business view** (Ch 5).

## Tells & smells (dấu hiệu nhận biết)
- Một dữ liệu bị nhập lại ở nhiều chức năng trong spec ⇒ chưa đạt chuẩn "enter once" (Ch 1).
- Một chức năng cần nhiều màn hình hơn hẳn hệ cũ ⇒ nghi **lack of fit** quy trình/phần mềm (Ch 4).
- Business case chỉ có lý do technology/competitive ⇒ tài liệu sẽ mơ hồ, thiếu cơ sở nghiệm thu (Ch 7).
- "Đếm số yêu cầu được đáp ứng" để chọn vendor ⇒ sai vì không chuẩn hóa granularity (Ch 8).
- Security để ở mức group thay vì individual "tạm thời" ⇒ implementation compromise đang thành engagement compromise (Ch 12).
- Tồn kho phình / thiếu linh kiện bất thường sau go-live ⇒ nghi lỗi **data conversion** (sai part/vendor/inventory number) (Ch 12).
- Nhiều hệ tích hợp đồng thời với thay đổi lớn ⇒ độ phức tạp nhân lên, failure factor hàng đầu (FoxMeyer) (Ch 15).

## Module chuẩn SAP R/3 (đặt tên chức năng theo chuẩn)
FI (financial accounting: GL, AR, AP), CO (controlling: cost center, product cost, ABC), AM (asset mgmt), MM (materials mgmt: inventory, invoice verification, warehouse), **PP** (production planning: **SOP** + **MRP** + **CRP**), SD (sales & distribution), HR (human resources), PM (plant maintenance), QM (quality mgmt), PS (project system). Oracle nhóm theo Demand / Supply / Finance (Ch 3).
