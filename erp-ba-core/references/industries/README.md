# Kiến thức theo ngành

| File | Ngành | Dùng khi |
|---|---|---|
| `construction.md` | Xây dựng (nhà thầu thi công, chủ đầu tư) | Dự án/demo cho doanh nghiệp xây dựng: dự toán, hợp đồng, công trường, thầu phụ, nghiệm thu, thanh toán theo khối lượng |
| `logistics.md` | Logistics (giao nhận, hải quan, vận tải, kho 3PL) | Forwarder, công ty vận tải, kho dịch vụ |
| `trading-distribution.md` | Thương mại – phân phối | Nhà phân phối, đại lý, bán lẻ, DMS, khuyến mại |

Ngành khác (sản xuất, dịch vụ, y tế, giáo dục…): dùng `references/processes/` cho phần chuẩn ERP (sản xuất xem `processes/manufacturing-mrp.md`), research thêm ở bước 1 và đề xuất với người dùng tạo file ngành mới.

## Cấu trúc bắt buộc của một file ngành mới

1. Tổng quan ngành & mô hình kinh doanh
2. Quy định pháp lý liên quan (bảng: văn bản, nội dung liên quan hệ thống, hiệu lực, tình trạng, ảnh hưởng thiết kế) — ghi "Cập nhật đến: <ngày>"
3. Bản đồ quy trình đầu-cuối của ngành (có sơ đồ Mermaid)
4. Chi tiết từng quy trình đặc thù (vai trò, chứng từ, bước, trạng thái, quy tắc, hạch toán đặc thù, tham số, báo cáo)
5. Danh mục (master data) đặc thù ngành
6. Module & chức năng chuẩn cho ERP ngành (Must/Should/Could cho demo và sản phẩm đầy đủ)
7. Báo cáo & KPI ngành
8. Đối thủ / sản phẩm tham chiếu (chỉ khẳng định tính năng có nguồn)
9. Thuật ngữ ngành (VI – EN – giải thích)
10. Câu hỏi khảo sát khách hàng của ngành
11. Rủi ro & lỗi thường gặp khi phân tích
12. Nguồn tham khảo

Quy ước viết: `references/conventions.md`; sơ đồ: `references/diagram-conventions.md`; mọi khẳng định về luật và đối thủ phải có nguồn.
