from bpmn_gen import N, F, M, A
import _common  # noqa: F401 — đăng ký danh mục dự án
from bpmn_gen import lane, pool, book, core, bp, call_name, title

PROCESS = dict(
    id='BP-01',
    name='Quản lý dữ liệu gốc: tạo và thay đổi danh mục có kiểm soát',
    objective='Mỗi đối tượng (khách hàng, đại lý, nhà cung cấp, dịch vụ, điểm đến, hướng dẫn viên) chỉ có một mã dùng chung '
              'toàn công ty, được nhập một lần tại nguồn, có người kiểm tra trước khi dùng cho giao dịch.',
    trigger='Bộ phận nghiệp vụ cần một đối tác/dịch vụ mới, hoặc cần đổi thông tin của bản ghi đang dùng '
            '(đặc biệt tài khoản ngân hàng, điều khoản thanh toán, hạn mức công nợ).',
    outcome='Bản ghi danh mục ở trạng thái Đang dùng, có lịch sử phiên bản, sẵn sàng cho mọi module; '
            'hoặc yêu cầu bị trả lại / từ chối có lý do.',
    scope='Khách hàng doanh nghiệp, đại lý, nhà cung cấp và tài khoản ngân hàng, dịch vụ, điểm đến, hướng dẫn viên, '
          'điều khoản thanh toán, hạn mức công nợ. Tạo mới, sửa, ngừng dùng, khóa.',
    out_of_scope='Bảng giá NCC theo mùa (%s); khách lẻ tạo ngay khi đặt chỗ (%s, có kiểm tra trùng); '
                 'thẻ và đơn giá hướng dẫn viên (%s).' % (bp('BP-02'), bp('BP-05'), bp('BP-16')),
    modules=['Dữ liệu gốc dùng chung (MDM)', 'Công nợ phải thu / phải trả (AR, AP)', 'Hệ thống (SYS)'],
    erp_standard='Master Data Management — chuẩn hóa danh mục dùng chung (MAPs) và kiểm soát đầu vào.',
    upstream=['Mọi bộ phận phát sinh nhu cầu'],
    downstream=['Tất cả quy trình giao dịch BP-02 → BP-16 chỉ tham chiếu mã đã kích hoạt ở đây'],
    pool_name='Công ty lữ hành — Dữ liệu gốc',
    lanes=[
        lane('REQ', 'Kinh doanh, Sản phẩm, Điều hành hoặc Kế toán: lập yêu cầu, đính kèm hồ sơ, sửa khi bị trả lại.'),
        lane('SYS', 'Kiểm tra trùng và định dạng, kích hoạt bản ghi, lưu phiên bản, đồng bộ sang các module.'),
        lane('MDM', 'Thẩm định, chuẩn hóa tên/mã/phân loại theo quy ước; trả lại khi chưa đạt.'),
        lane('CHIEF_ACC', 'Duyệt thông tin tài chính; gọi lại xác minh khi đổi tài khoản ngân hàng NCC.'),
    ],
    pools=[pool('NCC', 'bottom', name='Đối tác (NCC / khách hàng / đại lý)')],
    nodes=[
        N('S1', 'start', 'REQ', 0, 'Cần đối tác hoặc dịch vụ mới, hoặc cần đổi thông tin'),
        N('M0', 'xor', 'REQ', 1, ''),
        N('T1', 'user', 'REQ', 2, 'Lập yêu cầu tạo/sửa danh mục, đính kèm hồ sơ',
          doc='Chọn loại danh mục; nhập trường bắt buộc theo loại; đính kèm giấy phép kinh doanh, mã số thuế, '
              'xác nhận tài khoản ngân hàng, hợp đồng (nếu có).',
          docs='Yêu cầu danh mục: DRAFT → PENDING'),
        N('T2', 'service', 'SYS', 3, 'Kiểm tra trùng và hợp lệ',
          doc='So khóa chống trùng (mã số thuế, CCCD/hộ chiếu, số điện thoại, email, số tài khoản); '
              'kiểm tra định dạng và trường bắt buộc; tra cứu trạng thái mã số thuế nếu có tích hợp.',
          ctrl=['C01-01']),
        N('G1', 'xor', 'SYS', 4, 'Hợp lệ và không trùng?'),
        N('T4', 'user', 'MDM', 5, 'Thẩm định, chuẩn hóa dữ liệu',
          doc='Chuẩn hóa tên, phân loại, nhóm, khu vực, đơn vị tiền tệ; đối chiếu hồ sơ đính kèm.',
          ctrl=['C01-02', 'C01-03']),
        N('G3', 'xor', 'MDM', 6, 'Đạt chuẩn?'),
        N('G2', 'xor', 'MDM', 7, 'Có thông tin tài chính?'),
        N('T5', 'user', 'CHIEF_ACC', 8, 'Duyệt thông tin tài chính, xác minh tài khoản ngân hàng',
          doc='Tài khoản ngân hàng, điều khoản thanh toán, hạn mức công nợ. Đổi tài khoản ngân hàng NCC: '
              'gọi lại số điện thoại đã lưu trong hồ sơ (không dùng số trong email yêu cầu).',
          ctrl=['C01-04']),
        N('G4', 'xor', 'CHIEF_ACC', 9, 'Duyệt?'),
        N('E2', 'end', 'CHIEF_ACC', 10, 'Yêu cầu bị từ chối', docs='Yêu cầu danh mục: REJECTED'),
        N('M1', 'xor', 'SYS', 10, ''),
        N('T6', 'service', 'SYS', 11, 'Kích hoạt bản ghi, lưu phiên bản, đồng bộ module',
          doc='Bản ghi chuyển Đang dùng; lưu giá trị cũ/mới, người duyệt, thời điểm; thông báo người yêu cầu.',
          docs='Bản ghi: ACTIVE; Yêu cầu: APPROVED', ctrl=['C01-05', 'C01-06']),
        N('E1', 'end', 'SYS', 12, 'Danh mục sẵn sàng dùng'),
    ],
    flows=[
        F('S1', 'M0'), F('M0', 'T1'), F('T1', 'T2'), F('T2', 'G1'),
        F('G1', 'M0', 'Không - trả về', loop='top'),
        F('G1', 'T4', 'Có', default=True),
        F('T4', 'G3'),
        F('G3', 'M0', 'Chưa đạt - trả lại', loop='bottom'),
        F('G3', 'G2', 'Đạt', default=True),
        F('G2', 'T5', 'Có'),
        F('G2', 'M1', 'Không', default=True, route='hv_in'),
        F('T5', 'G4'),
        F('G4', 'M1', 'Duyệt', default=True),
        F('G4', 'E2', 'Từ chối', route='hv'),
        F('M1', 'T6'), F('T6', 'E1'),
    ],
    messages=[
        M('T5', 'NCC', 'Gọi lại xác minh', dx=-30),
        M('NCC', 'T5', 'Xác nhận của đối tác', dx=30),
    ],
    annotations=[
        A('N1', 'T4', 'Một đối tượng một mã; giao dịch chỉ tham chiếu mã (C01-02)', 'REQ', 5),
        A('N2', 'T5', 'Người lập yêu cầu không được duyệt; đổi TK ngân hàng phải gọi lại (C01-03, C01-04)',
          'CHIEF_ACC', 9, row=1),
        A('N3', 'T6', 'Không xóa bản ghi đã có giao dịch, chỉ ngừng dùng (C01-05)', 'REQ', 11),
    ],
    controls=[
        ('C01-01', 'Chặn tạo bản ghi trùng theo khóa: mã số thuế, CCCD/hộ chiếu, số điện thoại, email, số tài khoản.',
         'Phòng ngừa · Cấu hình', "O'Leary ch04 (input controls)"),
        ('C01-02', 'Một đối tượng có đúng một mã dùng chung toàn công ty; giao dịch chỉ lưu mã tham chiếu, không gõ lại tên/địa chỉ.',
         'Có sẵn (chuẩn hóa)', "O'Leary ch10; Elbardan ch07 (single data entry)"),
        ('C01-03', 'Maker-checker: người lập yêu cầu không được thẩm định/duyệt chính yêu cầu đó.',
         'Phân quyền (SoD)', 'Elbardan ch08'),
        ('C01-04', 'Thông tin tài chính phải được Kế toán trưởng duyệt; đổi tài khoản ngân hàng NCC bắt buộc gọi lại xác minh qua số đã lưu.',
         'Phòng ngừa · Phân quyền', 'erp-ba-core ap §7 BR-AP-11'),
        ('C01-05', 'Bản ghi đã phát sinh giao dịch không được xóa, chỉ chuyển Ngừng dùng hoặc Khóa.',
         'Có sẵn', 'erp-ba-core conventions §6'),
        ('C01-06', 'Lưu lịch sử phiên bản; báo cáo thay đổi danh mục (đặc biệt tài khoản ngân hàng) gửi Kế toán trưởng hằng tuần.',
         'Báo cáo (giám sát liên tục)', 'Elbardan ch06, ch10'),
    ],
    documents=[
        ('Yêu cầu danh mục', 'DRAFT → PENDING → RETURNED / REJECTED / APPROVED', 'Một yêu cầu cho một bản ghi; lưu hồ sơ đính kèm.'),
        ('Bản ghi danh mục', 'ACTIVE / INACTIVE / LOCKED', 'Trạng thái bản ghi, không dùng bộ trạng thái chứng từ.'),
    ],
    parameters=[
        ('Khóa chống trùng theo loại danh mục', 'Trường dùng để so trùng', 'MST; CCCD/hộ chiếu; SĐT; email; số TK'),
        ('Trường bắt buộc theo loại danh mục', 'Chặn gửi duyệt khi thiếu', 'Theo từng loại'),
        ('Danh mục cần Kế toán trưởng duyệt', 'Trường tài chính kích hoạt bước duyệt', 'TK ngân hàng, điều khoản TT, hạn mức'),
    ],
    kpis=[
        ('Tỷ lệ bản ghi trùng', 'Bản ghi trùng phát hiện khi rà soát / tổng bản ghi', '0%'),
        ('Thời gian xử lý yêu cầu', 'Từ gửi tới kích hoạt', '≤ 1 ngày làm việc'),
        ('Độ chính xác danh mục', 'Kiểm mẫu định kỳ', '≥ 98%'),
    ],
    references=[
        book('O', 'ch10-choosing-standard-maps.md',
             'Danh mục dùng chung (khách, NCC, sản phẩm, hệ thống tài khoản) là quyết định chuẩn hóa cấp doanh nghiệp; ghi rõ ai sở hữu, ai được cấu hình.'),
        book('O', 'ch04-erp-data-input.md', 'Nhập một lần tại nguồn bắt buộc đi kèm kiểm soát đầu vào, vì hệ thống không còn bản sao để đối chiếu.'),
        book('E', 'ch09-case-study-4-international-bank.md', 'Tiêu chí CAVAIR (Complete, Accurate, Valid, Restricted access) để nghiệm thu dữ liệu.'),
        book('E', 'ch08-case-study-3-national-bank.md', 'Maker-checker: màn hình không đi tiếp khi chưa có kiểm tra và duyệt.'),
        book('W', 'ch10-data-integrity.md', 'Dữ liệu dưới ngưỡng chính xác (≥ 98% với dữ liệu cấu trúc) thì chưa bật các chức năng hoạch định dựa trên nó.'),
        book('P', 'ch03-erp-modules.md', 'Master Data Management là một thành phần bắt buộc của module bán hàng.'),
        core('processes/ap-accounts-payable.md', '§7 BR-AP-11', 'đổi tài khoản ngân hàng NCC phải gọi lại xác minh.'),
    ],
    questions=[
        'Chủ sở hữu từng danh mục: khách hàng/đại lý (Kinh doanh), NCC (Sản phẩm), HDV (Điều hành/Nhân sự), hệ thống tài khoản (Kế toán trưởng) — có đúng không?',
        'Có tích hợp tra cứu mã số thuế tự động không?',
        'Hộ chiếu, ngày sinh của khách là dữ liệu cá nhân: ai được xem, lưu bao lâu (Luật Bảo vệ dữ liệu cá nhân)?',
    ],
)
