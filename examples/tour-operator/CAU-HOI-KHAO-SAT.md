# Bộ câu hỏi khảo sát khách hàng

> Sinh tự động từ mục "Điểm cần xác nhận" của từng quy trình (bpmn-kit). Mọi nội dung trong bộ sơ đồ là **đề xuất theo chuẩn ERP**, chưa được khách hàng xác nhận. Dùng danh sách này cho buổi khảo sát; câu trả lời nào khác đề xuất thì sửa định nghĩa quy trình rồi sinh lại.

## BP-01 — Quản lý dữ liệu gốc: tạo và thay đổi danh mục có kiểm soát

Sơ đồ: [BP-01](docs/BP-01-quan-ly-du-lieu-goc.md)

1. Chủ sở hữu từng danh mục: khách hàng/đại lý (Kinh doanh), NCC (Sản phẩm), HDV (Điều hành/Nhân sự), hệ thống tài khoản (Kế toán trưởng) — có đúng không?
2. Có tích hợp tra cứu mã số thuế tự động không?
3. Hộ chiếu, ngày sinh của khách là dữ liệu cá nhân: ai được xem, lưu bao lâu (Luật Bảo vệ dữ liệu cá nhân)?

Tham số đang dùng giá trị đề xuất — xác nhận con số của doanh nghiệp:

| Tham số | Ý nghĩa | Đề xuất | Doanh nghiệp xác nhận |
|---|---|---|---|
| Khóa chống trùng theo loại danh mục | Trường dùng để so trùng | MST; CCCD/hộ chiếu; SĐT; email; số TK | |
| Trường bắt buộc theo loại danh mục | Chặn gửi duyệt khi thiếu | Theo từng loại | |
| Danh mục cần Kế toán trưởng duyệt | Trường tài chính kích hoạt bước duyệt | TK ngân hàng, điều khoản TT, hạn mức | |

## BP-02 — Hợp đồng nhà cung cấp, bảng giá theo mùa và quỹ chỗ (allotment)

Sơ đồ: [BP-02](docs/BP-02-hop-dong-ncc-quy-cho.md)

4. Hạn mức duyệt hợp đồng theo giá trị cam kết là bao nhiêu? Có phân biệt NCC trong nước và nước ngoài?
5. NCC nào có quỹ chỗ cam kết cứng (phải trả tiền dù không bán được)?
6. Hợp đồng khách sạn quốc tế tính bằng ngoại tệ: dùng tỷ giá nào khi tính giá thành tour?

Tham số đang dùng giá trị đề xuất — xác nhận con số của doanh nghiệp:

| Tham số | Ý nghĩa | Đề xuất | Doanh nghiệp xác nhận |
|---|---|---|---|
| Hạn mức duyệt hợp đồng | Trưởng phòng Sản phẩm / Ban Giám đốc theo giá trị cam kết năm | ≤ 500 triệu / > 500 triệu | |
| Số báo giá tối thiểu | Cho dịch vụ trọng yếu | 3 | |
| Cảnh báo hết hạn hợp đồng | Số ngày trước khi hết hiệu lực | 60 ngày | |
| Hạn trả chỗ mặc định | Số ngày trước ngày sử dụng | 7 ngày | |

## BP-03 — Thiết kế sản phẩm tour và tính giá (chương trình tour mẫu)

Sơ đồ: [BP-03](docs/BP-03-thiet-ke-tour-tinh-gia.md)

7. Ai duyệt giá bán: Trưởng phòng Sản phẩm hay Ban Giám đốc? Có phân cấp theo biên lợi nhuận không?
8. Thuế suất GTGT áp cho tour inbound/nội địa/outbound từng loại là bao nhiêu (phần dịch vụ ở nước ngoài)?
9. Giá bán có khác nhau theo mùa/ngày khởi hành không, hay một giá cho cả chương trình?

Tham số đang dùng giá trị đề xuất — xác nhận con số của doanh nghiệp:

| Tham số | Ý nghĩa | Đề xuất | Doanh nghiệp xác nhận |
|---|---|---|---|
| Markup mặc định | % trên giá thành | 20% | |
| Thuế GTGT dịch vụ lữ hành | Theo thời kỳ giảm thuế | 8% hoặc 10% — Kế toán xác nhận | |
| Hoa hồng kênh | Theo kênh: đại lý, OTA | 10% | |
| Dự phòng chi phí | % trên giá thành | 3% | |
| Biên lợi nhuận tối thiểu | Dưới ngưỡng không gửi duyệt | 10% | |
| Giá trẻ em / em bé | % giá người lớn | 75% / 25% | |

## BP-04 — Hoạch định mùa vụ và lịch khởi hành (S&OP hằng tháng)

Sơ đồ: [BP-04](docs/BP-04-hoach-dinh-mua-vu-lich-khoi-hanh.md)

10. Doanh nghiệp chia dòng tour thế nào (theo tuyến, theo thị trường khách, theo loại tour)?
11. Ai là chủ trì S&OP (Giám đốc điều hành hay Phó Giám đốc kinh doanh)?
12. Có dùng phần mềm dự báo không, hay bảng tính trong giai đoạn đầu?

Tham số đang dùng giá trị đề xuất — xác nhận con số của doanh nghiệp:

| Tham số | Ý nghĩa | Đề xuất | Doanh nghiệp xác nhận |
|---|---|---|---|
| Danh sách dòng tour | Nhóm sản phẩm để hoạch định | 6–12 nhóm | |
| Tầm nhìn kế hoạch | Số tháng phía trước | 12–18 tháng | |
| Ngưỡng sai lệch phải giải trình | Thực tế so với kế hoạch | ±10% | |

## BP-05 — Bán tour ghép: giữ chỗ, thu cọc, xác nhận booking

Sơ đồ: [BP-05](docs/BP-05-ban-tour-ghep.md)

13. Thời hạn giữ chỗ và tỷ lệ cọc có khác nhau theo kênh (B2C, đại lý, OTA) và theo mùa không?
14. Khoản cọc là "đặt cọc bảo đảm hợp đồng" hay "thu trước tiền tour"? Câu trả lời quyết định thời điểm xuất HĐĐT.
15. Chỗ bán qua OTA trừ chung quỹ chỗ của chuyến hay có quỹ riêng cho từng kênh?
16. Đại lý nào được mua công nợ, hạn mức và kỳ thanh toán bao nhiêu?

Tham số đang dùng giá trị đề xuất — xác nhận con số của doanh nghiệp:

| Tham số | Ý nghĩa | Đề xuất | Doanh nghiệp xác nhận |
|---|---|---|---|
| Thời hạn giữ chỗ | Giữ chỗ chờ cọc, hết hạn tự hủy | 72 giờ | |
| Tỷ lệ cọc tối thiểu | Theo % giá trị booking | 30% | |
| Hạn thanh toán đủ | Số ngày trước khởi hành | D-15 | |
| Hạn mức ưu đãi | Nhân viên / Trưởng phòng / Giám đốc | 5% / 15% / trên 15% | |
| Dung sai hạn mức công nợ | Cho phép vượt hạn mức đại lý | 0–5% | |
| Hạn chốt nhận booking | Số ngày trước khởi hành | D-7 | |

## BP-06 — Bán tour thiết kế riêng: yêu cầu → dựng chương trình (thủ công hoặc AI) → bản chào → chốt → cọc

Sơ đồ: [BP-06](docs/BP-06-ban-tour-thiet-ke-rieng.md)

17. Ai dựng chương trình riêng: Kinh doanh hay phòng Sản phẩm?
18. Bản chào gửi giá trọn gói một con số hay tách theo người lớn/trẻ em?
19. Khi nào Điều hành được giữ chỗ tạm với NCC (trước hay sau khi khách chấp nhận)?
20. Luồng AI được dựng chương trình từ đầu, hay chỉ sửa bản đã dựng sẵn? (topas-crm hiện dựng bản đầu bằng trợ lý 9 bước, AI dùng ở bước sửa)
21. Dùng nhà cung cấp mô hình AI nào; hợp đồng xử lý dữ liệu có cho phép gửi yêu cầu của khách không? Có trần chi phí AI theo tháng không?

Tham số đang dùng giá trị đề xuất — xác nhận con số của doanh nghiệp:

| Tham số | Ý nghĩa | Đề xuất | Doanh nghiệp xác nhận |
|---|---|---|---|
| Hạn phản hồi yêu cầu | Từ khi tạo cơ hội | 24 giờ | |
| Hiệu lực bản chào | Sau đó bản chào hết hạn | 7 ngày | |
| Biên lợi nhuận tối thiểu | Dưới ngưỡng phải duyệt | 10% | |
| Ngưỡng giá NCC vượt dự toán | Phải Trưởng Điều hành duyệt | 10% | |
| Bật trợ lý AI | Tắt / bật | Tắt | |
| Thời gian chờ AI tối đa | Mỗi lượt dựng/sửa | 540 giây (theo topas-crm) | |
| Số lần thử lại khi bản nháp sai |  | 1 | |
| Trần kích thước chương trình AI dựng | Số ngày / số hoạt động mỗi ngày | 21 / 14 | |

## BP-07 — Chốt chuyến khởi hành và trả chỗ cho nhà cung cấp

Sơ đồ: [BP-07](docs/BP-07-chot-chuyen-tra-cho.md)

22. Hạn chốt và số khách tối thiểu có khác nhau theo dòng tour/mùa không?
23. Gộp chuyến: khách có quyền từ chối và được hoàn 100% không?
24. NCC nào cho trả chỗ sát ngày hơn hạn chung?

Tham số đang dùng giá trị đề xuất — xác nhận con số của doanh nghiệp:

| Tham số | Ý nghĩa | Đề xuất | Doanh nghiệp xác nhận |
|---|---|---|---|
| Hạn chốt chuyến | Số ngày trước khởi hành | D-10 | |
| Số khách tối thiểu | Theo từng chuyến / dòng tour | 15 | |
| Hạn trả chỗ | Theo hợp đồng NCC | D-7 | |
| Cảnh báo sớm thiếu khách | Số ngày trước hạn chốt | 3 ngày | |

## BP-08 — Đặt dịch vụ nhà cung cấp và chuẩn bị đoàn

Sơ đồ: [BP-08](docs/BP-08-dat-dich-vu-chuan-bi-doan.md)

25. Ai được gửi đơn đặt dịch vụ trực tiếp cho NCC (mọi điều hành viên hay chỉ người phụ trách đoàn)?
26. Bảo hiểm du lịch do công ty mua cho mọi đoàn hay chỉ khi hợp đồng có?
27. Tạm ứng cho HDV cộng tác hạch toán 141 hay 1388?

Tham số đang dùng giá trị đề xuất — xác nhận con số của doanh nghiệp:

| Tham số | Ý nghĩa | Đề xuất | Doanh nghiệp xác nhận |
|---|---|---|---|
| Ngưỡng lệch giá phải duyệt | So với hợp đồng / dự toán | 10% (cảnh báo từ 0,5%) | |
| Hạn phản hồi của NCC | Từ khi gửi đơn | 48 giờ | |
| Mốc checklist | Theo loại tour (inbound, nội địa) | D-21 … D+10 | |
| Tỷ lệ HDV theo khách | Số khách tối đa / 1 HDV | 25 | |

## BP-09 — Thực hiện tour và xử lý sự cố

Sơ đồ: [BP-09](docs/BP-09-thuc-hien-tour-xu-ly-su-co.md)

28. Ngưỡng chi phát sinh HDV được tự quyết là bao nhiêu? Có khác theo loại tour?
29. HDV có được trả tiền mặt cho NCC không, hay mọi khoản lớn phải để công ty chuyển khoản?
30. Mức độ sự cố và hạn xử lý có cần khác nhau giữa tour inbound và nội địa?

Tham số đang dùng giá trị đề xuất — xác nhận con số của doanh nghiệp:

| Tham số | Ý nghĩa | Đề xuất | Doanh nghiệp xác nhận |
|---|---|---|---|
| Ngưỡng chi phát sinh phải duyệt | Mỗi khoản | 3.000.000 đ | |
| Hạn xử lý sự cố theo mức độ | Nghiêm trọng / Cao / Trung bình / Thấp | 1 / 2 / 4 / 6 giờ | |
| Hạn duyệt bổ sung cho chi khẩn cấp | Sau khi chi | 24 giờ | |

## BP-10 — Quyết toán và đóng hồ sơ tour

Sơ đồ: [BP-10](docs/BP-10-quyet-toan-dong-ho-so-tour.md)

31. Doanh nghiệp áp dụng TT99 hay chế độ cho doanh nghiệp nhỏ và vừa? (ảnh hưởng tài khoản 154/632 và 642)
32. Ngưỡng chênh lệch phải giải trình theo % hay theo số tiền?
33. Công nợ khách chưa thu đủ có được đóng hồ sơ và theo dõi riêng không?

Tham số đang dùng giá trị đề xuất — xác nhận con số của doanh nghiệp:

| Tham số | Ý nghĩa | Đề xuất | Doanh nghiệp xác nhận |
|---|---|---|---|
| Hạn quyết toán tạm ứng | Sau ngày kết thúc tour | 4 ngày làm việc | |
| Ngưỡng chênh lệch phải giải trình | So với dự toán, theo hạng mục | 10% hoặc 2.000.000 đ | |
| Hạn đóng hồ sơ | Sau ngày kết thúc tour | 10 ngày | |

## BP-11 — Thu tiền khách hàng và công nợ phải thu (kèm đối chiếu công nợ đại lý)

Sơ đồ: [BP-11](docs/BP-11-thu-tien-cong-no-phai-thu.md)

34. Khoản thu trước khởi hành của khách là "đặt cọc bảo đảm hợp đồng" hay "thu trước tiền dịch vụ"? Quyết định có phải lập hóa đơn khi thu không.
35. Đại lý nào được công nợ, kỳ thanh toán bao nhiêu ngày?
36. Hợp đồng đại lý có điều khoản "không phản hồi đối chiếu trong N ngày coi như xác nhận" không?
37. Thu ngoại tệ (khách inbound): tỷ giá ghi nhận theo ngân hàng nào?

Tham số đang dùng giá trị đề xuất — xác nhận con số của doanh nghiệp:

| Tham số | Ý nghĩa | Đề xuất | Doanh nghiệp xác nhận |
|---|---|---|---|
| Lịch thanh toán mặc định | Cọc khi đặt / đủ trước khởi hành | 30% / D-15 | |
| Cấp nhắc nợ | Số cấp và mốc ngày | 3 cấp: D-3, D0, D+3 so với hạn | |
| Chênh lệch thu thừa/thiếu tự xử lý | Không cần duyệt | ≤ 50.000 đ | |
| Kỳ đối chiếu đại lý | Tần suất | Hằng tháng | |
| Hạn đại lý phản hồi | Sau hạn coi như xác nhận (nếu hợp đồng quy định) | 7 ngày | |

## BP-12 — Thanh toán nhà cung cấp và công nợ phải trả

Sơ đồ: [BP-12](docs/BP-12-thanh-toan-ncc-cong-no-phai-tra.md)

38. NCC thường xuất một hóa đơn cho mỗi đoàn hay gộp theo tháng? (ảnh hưởng đối chiếu theo mã tour)
39. Hạn mức duyệt chi của Kế toán trưởng là bao nhiêu?
40. Có NCC nước ngoài thuộc diện thuế nhà thầu không?

Tham số đang dùng giá trị đề xuất — xác nhận con số của doanh nghiệp:

| Tham số | Ý nghĩa | Đề xuất | Doanh nghiệp xác nhận |
|---|---|---|---|
| Dung sai giá đối chiếu | So với đơn đặt dịch vụ | ±2% hoặc 100.000 đ | |
| Dung sai số lượng | Hóa đơn so với số lượng đã dùng | Không vượt số đã dùng | |
| Hạn mức duyệt chi | Kế toán trưởng / Ban Giám đốc | ≤ 500 triệu / > 500 triệu | |
| Kỳ chạy đề xuất thanh toán | Tần suất | Hằng tuần | |

## BP-13 — Thay đổi, hủy booking và hoàn tiền

Sơ đồ: [BP-13](docs/BP-13-thay-doi-huy-booking-hoan-tien.md)

41. Doanh nghiệp dùng một bảng phí hủy duy nhất hay theo từng loại tour/kênh? Lưu ý: repo topas-crm đang có hai bộ mốc khác nhau (4 mốc trong addons/topas/models/tour_pricing_rule.py, 5 mốc có mức 75% trong addons/topas/data/tour_terms_data.xml) — cần thống nhất trước khi cấu hình.
42. Phí hủy giữ lại hạch toán thu nhập khác hay doanh thu; có phải xuất hóa đơn không?
43. Khách đổi người đi (đổi tên) có tính phí không?

Tham số đang dùng giá trị đề xuất — xác nhận con số của doanh nghiệp:

| Tham số | Ý nghĩa | Đề xuất | Doanh nghiệp xác nhận |
|---|---|---|---|
| Bảng phí hủy theo mốc ngày | Trước ngày khởi hành | ≥30 ngày 10%; 15–29: 30%; 8–14: 50%; 0–7: 100% | |
| Hạn mức miễn/giảm phí của Trưởng phòng | % hoặc số tiền | Doanh nghiệp quy định | |
| Hạn hoàn tiền | Từ khi duyệt | 7 ngày làm việc | |

## BP-14 — Chăm sóc khách hàng sau tour và xử lý khiếu nại

Sơ đồ: [BP-14](docs/BP-14-cham-soc-khach-hang-khieu-nai.md)

44. Hạn mức đền bù CSKH được tự quyết là bao nhiêu?
45. Khảo sát gửi qua kênh nào (email, Zalo, cổng khách hàng)?
46. Có chương trình khách hàng thân thiết (điểm, hạng) không?

Tham số đang dùng giá trị đề xuất — xác nhận con số của doanh nghiệp:

| Tham số | Ý nghĩa | Đề xuất | Doanh nghiệp xác nhận |
|---|---|---|---|
| Thời điểm gửi khảo sát | Sau khi tour kết thúc | 24 giờ | |
| Ngưỡng hài lòng | Để mời đánh giá công khai | 4/5 | |
| Hạn xử lý khiếu nại | Theo mức độ | Doanh nghiệp quy định | |
| Hạn mức đền bù của CSKH | Số tiền hoặc % giá trị booking | Doanh nghiệp quy định | |

## BP-15 — Khóa sổ cuối kỳ và báo cáo (Record-to-Report)

Sơ đồ: [BP-15](docs/BP-15-khoa-so-cuoi-ky.md)

47. Doanh nghiệp theo TT99 hay chế độ kế toán doanh nghiệp nhỏ và vừa?
48. Đánh giá lại ngoại tệ cuối kỳ ghi qua 413 hay thẳng 515/635?
49. Mục tiêu số ngày khóa sổ là bao nhiêu?

Tham số đang dùng giá trị đề xuất — xác nhận con số của doanh nghiệp:

| Tham số | Ý nghĩa | Đề xuất | Doanh nghiệp xác nhận |
|---|---|---|---|
| Ngày bắt đầu khóa sổ | Ngày làm việc thứ N sau cuối tháng | N = 3 | |
| Tài khoản bắt buộc mã tour | Danh sách | 131, 331, 141, 154, 335, 511, 632 | |
| Ngưỡng bút toán điều chỉnh cần Giám đốc duyệt | Số tiền | Doanh nghiệp quy định | |

## BP-16 — Hướng dẫn viên cộng tác: hồ sơ, hạn thẻ và chi trả thù lao

Sơ đồ: [BP-16](docs/BP-16-hdv-cong-tac-chi-tra-thu-lao.md)

50. HDV cộng tác hạch toán qua 334 hay 3388?
51. Thù lao chi theo từng tour hay gộp theo tháng?
52. Ngưỡng khấu trừ TNCN đang áp dụng là bao nhiêu (đã có đề xuất nâng ngưỡng — cần kế toán xác nhận)?

Tham số đang dùng giá trị đề xuất — xác nhận con số của doanh nghiệp:

| Tham số | Ý nghĩa | Đề xuất | Doanh nghiệp xác nhận |
|---|---|---|---|
| Ngưỡng khấu trừ TNCN mỗi lần chi | Áp cho cá nhân không ký HĐLĐ | 2.000.000 đ (xác nhận lại quy định hiện hành) | |
| Thuế suất khấu trừ |  | 10% | |
| Cảnh báo hạn thẻ HDV | Số ngày trước khi hết hạn | 60 ngày | |
| Kỳ chi thù lao | Theo tour hoặc gộp kỳ | Doanh nghiệp quy định | |

