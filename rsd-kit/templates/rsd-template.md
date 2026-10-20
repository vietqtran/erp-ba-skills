# TÀI LIỆU ĐẶC TẢ YÊU CẦU (RSD)

## Quy trình {{BP}}: {{Tên quy trình}}

| Thông tin | Nội dung |
|---|---|
| Mã tài liệu | RSD-{{BP}} |
| Trạng thái | Bản nháp |
| Ngày cập nhật | {{dd/MM/yyyy}} |
| Phạm vi | {{các phân hệ, tiếng Việt}} |
| Người soạn | BA dự án |
| Người duyệt | {{vai trò trưởng các bộ phận tham gia}} |
| Tài liệu liên quan | Mô tả quy trình và sơ đồ BPMN {{BP}}; các quy trình {{BP liên quan}} |

**Phiên bản**

| Version | Lý do | Date | Người sửa | Mô tả |
|---|---|---|---|---|
| 0.1 | Thêm mới | {{dd/MM/yyyy}} | BA | Khởi tạo tài liệu từ mô tả quy trình {{BP}} |

**Nội dung tài liệu**

1. Mô tả chung
2. Mô tả các bước thực hiện
3. Input / Output
4. Phân quyền thực hiện
5. Tham số hệ thống
6. Flow Diagrams
7. Kiểm soát nội bộ
8. Yêu cầu phi chức năng
9. Tiêu chí nghiệm thu
10. Câu hỏi cần doanh nghiệp xác nhận
11. Tài liệu tham khảo

---

## Cách đọc tài liệu

**Mã tham chiếu.** Mỗi loại nội dung có một mã riêng để tiện trao đổi và truy vết:

| Mã | Loại nội dung | Ví dụ |
|---|---|---|
| Bước 1 … {{n}} | Các bước của quy trình (mục 2) | {{Bước 5 – …}} |
| QT-01 … | Quy tắc nghiệp vụ | {{…}} |
| TS-01 … | Tham số hệ thống (giá trị cấu hình được) | {{…}} |
| KS-01 … | Điểm kiểm soát nội bộ | {{…}} |
| TN-01 … | Nguyên tắc tách nhiệm vụ | {{…}} |
| BC-01 … | Báo cáo | {{…}} |
| NT-01 … | Tiêu chí nghiệm thu | {{…}} |
| CH-01 … | Câu hỏi cần doanh nghiệp xác nhận | {{…}} |

**Nhãn đánh dấu:**

- **[Cần xác nhận: CH-xx]** — thông tin chưa có, cần doanh nghiệp trả lời câu hỏi CH-xx.
- **[Đề xuất: CH-xx]** — BA đề xuất theo thông lệ ERP, chưa có trong mô tả quy trình gốc; doanh nghiệp quyết định giữ hay bỏ.

**Ký hiệu trong bảng phân quyền:**

- **✔** — được phép.
- **—** — không được phép.

---

## 1. Mô tả chung

| Đặc tả use case | Nội dung |
|---|---|
| Tên | {{Tên quy trình}} |
| Mã | {{BP}} |
| Mô tả | Là {{vai trò chính}}, tôi muốn {{…}}, để {{giá trị 1}}, {{giá trị 2}}… |
| Tác nhân | Chủ động: {{các vai trò nội bộ}}. Thụ động: Hệ thống ERP; {{các bên ngoài}} |
| Mức độ ưu tiên | High |
| Điều kiện kích hoạt | {{…}} — mục 1.4 |
| Tiền điều kiện | {{tóm tắt}} — mục 1.6 |
| Hậu điều kiện | {{tóm tắt}} — mục 1.6 |

### 1.1 Mục đích

### 1.2 Mục tiêu và chỉ số đo

| Mục tiêu | Cách đo | Chỉ tiêu đề xuất |
|---|---|---|

### 1.3 Phạm vi

**Trong phạm vi**

**Ngoài phạm vi**

| Nội dung | Quy trình đảm nhận |
|---|---|

### 1.4 Khi nào quy trình bắt đầu

| Tình huống | Người lập phiếu | Bằng chứng bắt buộc | Điểm khác biệt |
|---|---|---|---|

### 1.5 Các loại yêu cầu

### 1.6 Điều kiện trước khi bắt đầu và kết quả sau khi hoàn tất

### 1.7 Các bên tham gia

| Bên tham gia | Vai trò trong quy trình |
|---|---|

### 1.8 Quy trình liên quan

| Quy trình | Quan hệ với {{BP}} |
|---|---|

### 1.9 Thuật ngữ

| Thuật ngữ | Giải thích |
|---|---|

---

## 2. Mô tả các bước thực hiện

### 2.1 Tổng quan

| Giai đoạn | Các bước | Kết quả của giai đoạn |
|---|---|---|

### 2.2 Bảng tóm tắt các bước

| Bước | Tên bước | Người thực hiện | Áp dụng khi | Trạng thái phiếu sau bước |
|---|---|---|---|---|

### 2.3 Mô tả chi tiết từng bước

#### Bước 1 – {{Tên bước}}

- **Người thực hiện:** {{…}}
- **Việc cần làm:**
  - {{…}}
- **Hệ thống tự động:**
  - {{…}}
- **Quy tắc áp dụng:** QT-01 đến QT-0n.
- **Kết quả:** Phiếu ở trạng thái *Nháp*.

### 2.4 Các điểm quyết định

| Điểm quyết định | Điều kiện | Nếu ĐÚNG | Nếu KHÔNG |
|---|---|---|---|

### 2.5 Các tình huống đặc biệt

| Tình huống | Cách xử lý |
|---|---|

### 2.6 Các tình huống lỗi và thông báo hiển thị

| Bước | Tình huống | Hệ thống xử lý | Thông báo hiển thị cho người dùng |
|---|---|---|---|

### 2.7 Quy tắc nghiệp vụ

**a) {{Nhóm quy tắc}}**

| Mã | Quy tắc | Căn cứ |
|---|---|---|

### 2.8 Cách tính tiền

**Ví dụ 1 — {{tình huống}}**

| Nội dung | Giá trị |
|---|---|

---

## 3. Input / Output

### 3.1 Đầu vào và đầu ra theo từng bước

| Bước | Đầu vào (lấy từ đâu) | Đầu ra (gửi đi đâu) |
|---|---|---|

### 3.2 Thông tin trên phiếu {{chứng từ chính}}

| Thông tin | Bắt buộc | Ai nhập | Ghi chú |
|---|---|---|---|

### 3.3 Chứng từ được tạo ra và trạng thái

| Chứng từ | Các trạng thái | Ai tạo |
|---|---|---|

### 3.4 Dữ liệu được cập nhật ở các phân hệ khác

| Thời điểm | Phân hệ | Dữ liệu thay đổi | Nếu cần hoàn lại |
|---|---|---|---|

### 3.5 Bút toán kế toán

| Nghiệp vụ | Khi nào | Nợ | Có | Ghi chú |
|---|---|---|---|---|

### 3.6 Thông tin gửi ra bên ngoài

| Gửi cho | Khi nào | Nội dung | Kênh gửi |
|---|---|---|---|

### 3.7 Thông báo nội bộ tự động

| Khi nào | Ai nhận |
|---|---|

### 3.8 Báo cáo

| Mã | Báo cáo | Nội dung chính | Người dùng | Tần suất |
|---|---|---|---|---|

---

## 4. Phân quyền thực hiện

### 4.1 Vai trò

| Viết tắt | Vai trò | Phạm vi dữ liệu mặc định |
|---|---|---|

### 4.2 Tổng hợp: vai trò tham gia chức năng nào

| Chức năng | {{vai trò viết tắt …}} |
|---|---|

### 4.3 Ai được làm gì

**a) {{Chứng từ}}**

| Thao tác | {{vai trò …}} | Điều kiện |
|---|---|---|

### 4.4 Ai được xem dữ liệu gì

### 4.5 Thông tin nhạy cảm

### 4.6 Nguyên tắc tách nhiệm vụ

| Mã | Nhiệm vụ A | Nhiệm vụ B | Rủi ro nếu cùng một người | Hệ thống kiểm soát |
|---|---|---|---|---|

### 4.7 Hạn mức phê duyệt

| Nội dung | Điều kiện | Cấp duyệt 1 | Cấp duyệt 2 |
|---|---|---|---|

### 4.8 Ủy quyền và thay đổi người phụ trách

---

## 5. Tham số hệ thống

Tham số là các giá trị doanh nghiệp tự cấu hình được trên hệ thống mà không phải sửa chương trình: ngưỡng, tỷ lệ, số ngày, bật/tắt một bước.

Các giá trị dưới đây là **giá trị đề xuất**, doanh nghiệp phải chốt trước khi đưa vào sử dụng. Mọi lần thay đổi tham số đều được lưu lịch sử.

### 5.1 Nhóm {{…}}

| Mã | Tham số | Giá trị mặc định | Ảnh hưởng | Ai thay đổi |
|---|---|---|---|---|

---

## 6. Flow Diagrams

**Chú thích màu trong các sơ đồ:**

| Màu | Ý nghĩa |
|---|---|
| Trắng | Việc của {{vai trò 1}} |
| Xanh dương | Việc hệ thống tự làm |
| Tím | Việc của {{vai trò duyệt}} |
| Cam | Việc của {{vai trò 3}} |
| Xanh ngọc | Việc của {{vai trò 4}} |
| Vàng (hình thoi) | Điểm quyết định |
| Xanh lá | Điểm bắt đầu hoặc kết quả bình thường |
| Đỏ | Dừng lại hoặc báo lỗi |

### Hình 1 – Sơ đồ quy trình BPMN

Sơ đồ chuẩn BPMN 2.0 của quy trình, chia làn theo vai trò, kèm các bên bên ngoài.

![Hình 1 – Sơ đồ quy trình BPMN](images/h01-bpmn.png)

### Hình 2 – Các bên tham gia

![Hình 2 – Các bên tham gia](images/h02-context.png)

---

## 7. Kiểm soát nội bộ

| Mã | Điểm kiểm soát | Loại | Thực hiện bằng | Căn cứ | Tiêu chí nghiệm thu |
|---|---|---|---|---|---|

---

## 8. Yêu cầu phi chức năng

Các con số dưới đây là giá trị đề xuất, cần doanh nghiệp xác nhận [Cần xác nhận: CH-{{n}}].

| Nhóm | Yêu cầu |
|---|---|

---

## 9. Tiêu chí nghiệm thu

Mỗi tiêu chí mô tả theo dạng **Cho trước** (bối cảnh) – **Khi** (thao tác) – **Thì** (kết quả mong đợi), có số liệu cụ thể để kiểm thử.

| Mã | Tình huống | Cho trước | Khi | Thì |
|---|---|---|---|---|

**Tình huống biên cần có trong bộ kiểm thử**

| Tình huống | Kết quả mong đợi |
|---|---|

---

## 10. Câu hỏi cần doanh nghiệp xác nhận

### 10.1 Câu hỏi mở

**{{Người cần trả lời}}**

| Mã | Câu hỏi | Ảnh hưởng |
|---|---|---|

### 10.2 Giả định đang áp dụng

| Giả định | Nếu sai thì |
|---|---|

### 10.3 Điểm chưa thống nhất giữa các nguồn

| Nội dung | Cách xử lý trong tài liệu này |
|---|---|

---

## 11. Tài liệu tham khảo

**Tài liệu của dự án**

**Sách về ERP**

| Sách | Chương | Áp dụng trong tài liệu |
|---|---|---|

**Quy định pháp luật** (cần kiểm tra lại hiệu lực khi áp dụng)

| Văn bản | Nội dung áp dụng |
|---|---|
