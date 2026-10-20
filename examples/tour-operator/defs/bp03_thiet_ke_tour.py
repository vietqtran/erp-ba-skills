from bpmn_gen import N, F, M, A, D
import _common  # noqa: F401 — đăng ký danh mục dự án
from bpmn_gen import lane, pool, book, core, bp, call_name, title

PROCESS = dict(
    id='BP-03',
    name='Thiết kế sản phẩm tour và tính giá (chương trình tour mẫu)',
    objective='Chương trình tour có lịch trình, danh sách dịch vụ và giá bán được tính từ giá NCC đã duyệt, '
              'đạt biên lợi nhuận tối thiểu và được khóa phiên bản trước khi mở bán.',
    trigger='Kế hoạch S&OP cần sản phẩm mới cho mùa tới, hoặc cần làm mới chương trình đang bán.',
    outcome='Chương trình tour Đã duyệt, có phiên bản; bảng giá bán theo kênh và độ tuổi; đã xuất bản lên website/OTA/đại lý.',
    scope='Tour mẫu bán theo lịch khởi hành (tour ghép). Lịch trình theo ngày, dịch vụ cấu thành, giá thành theo số khách, '
          'giá bán theo kênh, điểm hòa vốn, duyệt, xuất bản.',
    out_of_scope='Tour thiết kế riêng theo yêu cầu khách (%s — dùng lại các bước tính giá ở đây); '
                 'mở lịch khởi hành (%s).' % (bp('BP-06'), bp('BP-04')),
    modules=['Sản phẩm tour', 'Giá thành (COST)', 'Bán hàng – bảng giá (SAL)'],
    erp_standard='Thiết kế sản phẩm và định giá: chương trình tour đóng vai trò "định mức dịch vụ" (tương tự BOM), '
                 'lịch trình tương tự quy trình công nghệ; giá thành dự toán → giá bán → duyệt → khóa phiên bản.',
    upstream=[bp('BP-02', 'bảng giá NCC hiệu lực'), bp('BP-04', 'danh mục sản phẩm cần cho mùa')],
    downstream=[bp('BP-04', 'mở lịch khởi hành'), bp('BP-05', 'bán theo bảng giá chuyến')],
    pool_name='Công ty lữ hành — Thiết kế tour',
    lanes=[
        lane('PROD', 'Dựng lịch trình, chọn dịch vụ, điều chỉnh khi biên lợi nhuận thấp hoặc bị trả lại, xuất bản.'),
        lane('SYS', 'Tính giá thành, giá bán, điểm hòa vốn; khóa phiên bản đã duyệt.'),
        lane('DIR', 'Duyệt chương trình và giá bán.'),
    ],
    pools=[pool('KENH', 'top', name='Kênh phân phối (website, OTA, đại lý)')],
    nodes=[
        N('S1', 'start', 'PROD', 0, 'Cần sản phẩm mới cho mùa'),
        N('T1', 'user', 'PROD', 1, 'Tạo chương trình: lịch trình theo ngày, điểm đến',
          doc='Dựng từ đầu hoặc ghép module tour có sẵn; mỗi ngày gồm điểm đến, hoạt động, bữa ăn, lưu trú, di chuyển.',
          docs='Chương trình tour: DRAFT'),
        N('T2', 'user', 'PROD', 2, 'Chọn dịch vụ từ kho dịch vụ và bảng giá NCC',
          doc='Chỉ chọn được dịch vụ có bảng giá đang hiệu lực cho mùa dự kiến khởi hành.', ctrl=['C03-01']),
        N('M1', 'xor', 'SYS', 3, ''),
        N('T3', 'service', 'SYS', 4, 'Tính giá thành theo số khách',
          doc='Chi phí theo khách + chi phí cố định theo đoàn (xe, HDV) chia theo số khách + dự phòng; '
              'tính cho nhiều mức số khách và điểm hòa vốn.'),
        N('T4', 'service', 'SYS', 5, 'Tính giá bán theo kênh và độ tuổi',
          doc='Markup, thuế GTGT, hoa hồng kênh, làm tròn; giá người lớn / trẻ em / em bé, phụ thu phòng đơn.',
          ctrl=['C03-02']),
        N('G1', 'xor', 'SYS', 6, 'Biên lợi nhuận đạt tối thiểu?'),
        N('T6', 'user', 'DIR', 7, 'Duyệt chương trình và giá bán', ctrl=['C03-03'],
          docs='Chương trình tour: PENDING'),
        N('G2', 'xor', 'DIR', 8, 'Duyệt?'),
        N('M2', 'xor', 'PROD', 8, '', row=1),
        N('T5', 'user', 'PROD', 9, 'Điều chỉnh dịch vụ hoặc tham số giá', row=1,
          docs='Chương trình tour: RETURNED'),
        N('T7', 'service', 'SYS', 9, 'Khóa phiên bản, áp giá bán',
          doc='Chương trình đã duyệt chỉ đọc; mọi thay đổi sau đó tạo phiên bản mới và duyệt lại.',
          docs='Chương trình tour: APPROVED (phiên bản n)', ctrl=['C03-04']),
        N('T8', 'send', 'PROD', 10, 'Xuất bản lên website, OTA, đại lý', ctrl=['C03-05']),
        N('E1', 'end', 'PROD', 11, 'Sản phẩm sẵn sàng mở chuyến'),
    ],
    flows=[
        F('S1', 'T1'), F('T1', 'T2'), F('T2', 'M1', route='hv'), F('M1', 'T3'), F('T3', 'T4'), F('T4', 'G1'),
        F('G1', 'T6', 'Đạt', default=True),
        F('G1', 'M2', 'Không đạt'),
        F('T6', 'G2'),
        F('G2', 'M2', 'Trả lại'),
        F('G2', 'T7', 'Đồng ý', default=True, route='hv_in'),
        F('M2', 'T5'),
        F('T5', 'M1', loop='top'),
        F('T7', 'T8'), F('T8', 'E1'),
    ],
    messages=[
        M('T8', 'KENH', 'Sản phẩm, lịch, giá'),
    ],
    data=[
        D('D1', 'store', 'Kho dịch vụ và bảng giá NCC', 'PROD', 2, row=1, links=[('T2', 'in')]),
    ],
    annotations=[
        A('N1', 'T3', 'Giá vốn lấy từ bảng giá NCC hiệu lực, không nhập tay (C03-01)', 'PROD', 4, row=1),
        A('N2', 'T6', 'Người thiết kế không tự duyệt giá; dưới biên tối thiểu không gửi duyệt được (C03-03)', 'DIR', 7, row=1),
    ],
    controls=[
        ('C03-01', 'Giá vốn chỉ lấy từ bảng giá NCC đang hiệu lực theo ngày dự kiến sử dụng; không nhập tay giá vốn.',
         'Phòng ngừa · Cấu hình', "O'Leary ch04 (enter once)"),
        ('C03-02', 'Công thức giá bán tham số hóa (markup, hoa hồng kênh, thuế, làm tròn, giá trẻ em); chỉ Kế toán trưởng/Ban Giám đốc sửa tham số.',
         'Cấu hình · Phân quyền', 'Parthasarathy ch03 (pricing)'),
        ('C03-03', 'Biên lợi nhuận dưới ngưỡng thì không gửi duyệt được; người thiết kế không được duyệt giá của mình.',
         'Phòng ngừa · Phân quyền (SoD)', 'Elbardan ch07, ch08'),
        ('C03-04', 'Chương trình đã duyệt bị khóa; thay đổi tạo phiên bản mới và duyệt lại; booking giữ tham chiếu phiên bản đã bán.',
         'Có sẵn (audit trail)', 'Wallace ch09 (engineering change policy)'),
        ('C03-05', 'Chỉ chương trình đã duyệt mới được xuất bản ra kênh bán.',
         'Phòng ngừa', 'Elbardan ch07'),
    ],
    documents=[
        ('Chương trình tour', 'DRAFT → PENDING → RETURNED / APPROVED → CLOSED (ngừng bán); có phiên bản', 'Định mức dịch vụ của tour.'),
        ('Bảng tính giá', 'DRAFT → APPROVED', 'Giá thành theo mức số khách, điểm hòa vốn, giá bán theo kênh.'),
    ],
    parameters=[
        ('Markup mặc định', '% trên giá thành', '20%'),
        ('Thuế GTGT dịch vụ lữ hành', 'Theo thời kỳ giảm thuế', '8% hoặc 10% — Kế toán xác nhận'),
        ('Hoa hồng kênh', 'Theo kênh: đại lý, OTA', '10%'),
        ('Dự phòng chi phí', '% trên giá thành', '3%'),
        ('Biên lợi nhuận tối thiểu', 'Dưới ngưỡng không gửi duyệt', '10%'),
        ('Giá trẻ em / em bé', '% giá người lớn', '75% / 25%'),
    ],
    kpis=[
        ('Thời gian dựng một chương trình', 'Từ tạo tới gửi duyệt', 'Giảm so với làm tay'),
        ('Tỷ lệ chương trình bị trả lại', 'Bị trả lại / gửi duyệt', 'Theo dõi'),
        ('Sai lệch giá thành dự toán và thực tế', 'Từ BP-10 theo chương trình', '≤ 5%'),
    ],
    references=[
        book('P', 'ch03-erp-modules.md', 'SD có thành phần Pricing; MM có Product costing; Finance có Cost controlling.'),
        book('W', 'ch09-process-definition.md', 'Engineering change là một trong năm chính sách nền: thay đổi định mức phải có phiên bản và người duyệt.'),
        book('W', 'ch10-data-integrity.md', 'Định mức (BOM) phải đầy đủ, có cấu trúc và chính xác ≥ 98% — áp cho danh sách dịch vụ của chương trình.'),
        book('O', 'ch04-erp-data-input.md', 'Nhập một lần tại nguồn: giá NCC nhập ở hợp đồng, không gõ lại khi tính giá tour.'),
        book('E', 'ch07-case-study-2-national-company.md', 'Kiểm soát phòng ngừa dạng if/else: không cho đi tiếp khi điều kiện chưa đạt.'),
    ],
    questions=[
        'Ai duyệt giá bán: Trưởng phòng Sản phẩm hay Ban Giám đốc? Có phân cấp theo biên lợi nhuận không?',
        'Thuế suất GTGT áp cho tour inbound/nội địa/outbound từng loại là bao nhiêu (phần dịch vụ ở nước ngoài)?',
        'Giá bán có khác nhau theo mùa/ngày khởi hành không, hay một giá cho cả chương trình?',
    ],
)
