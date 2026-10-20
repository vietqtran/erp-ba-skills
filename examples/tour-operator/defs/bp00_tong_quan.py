from bpmn_gen import N, F, M, A, D
import _common  # noqa: F401 — đăng ký danh mục dự án
from bpmn_gen import lane, pool, book, core, bp, call_name, title

# (mã, nhóm, quy trình chuẩn ERP tương ứng, module chính)
CATALOG = [
    ('BP-01', 'Nền tảng', 'Master Data Management', 'MDM, AR, AP'),
    ('BP-02', 'Hoạch định – nguồn cung', 'Procure-to-Pay (nguồn cung, hợp đồng khung); Supplier Scheduling', 'PUR, AP'),
    ('BP-03', 'Hoạch định – sản phẩm', 'Thiết kế sản phẩm, định giá (BOM, costing, pricing)', 'Sản phẩm, COST, SAL'),
    ('BP-04', 'Hoạch định', 'Sales & Operations Planning', 'Hoạch định, BUD'),
    ('BP-05', 'Bán hàng', 'Order-to-Cash: nhận đơn, ATP, kiểm tra tín dụng', 'SAL, AR, CB'),
    ('BP-06', 'Bán hàng', 'Quote-to-Cash (thiết kế theo đơn); dựng chương trình thủ công hoặc bằng trợ lý AI', 'CRM, SAL, tích hợp AI'),
    ('BP-07', 'Điều hành', 'Master scheduling (mức chuyến), time fence, supplier scheduling', 'Lịch khởi hành, PUR'),
    ('BP-08', 'Điều hành', 'Procure-to-Pay: đặt hàng từ định mức', 'OPS, PUR, CB'),
    ('BP-09', 'Điều hành', 'Thực thi & phản hồi; nghiệm thu dịch vụ', 'OPS, SVC'),
    ('BP-10', 'Tài chính – giá thành', 'Giá thành theo đơn/dự án; đóng dự án', 'COST, CB, GL'),
    ('BP-11', 'Tài chính', 'Order-to-Cash: hóa đơn, thu tiền, đối chiếu', 'AR, TAX, CB'),
    ('BP-12', 'Tài chính', 'Procure-to-Pay: xác minh hóa đơn, thanh toán', 'AP, TAX, CB'),
    ('BP-13', 'Bán hàng – ngoại lệ', 'Change order, trả lại/giảm trừ', 'SAL, OPS, AR, TAX'),
    ('BP-14', 'Dịch vụ khách hàng', 'CRM dịch vụ: ticket, SLA, CSAT', 'CRM, SVC'),
    ('BP-15', 'Tài chính', 'Record-to-Report (month-end close)', 'GL, AR, AP, COST'),
    ('BP-16', 'Nhân sự', 'Quản lý cộng tác viên và chi trả', 'HR, AP, CB'),
]

_rows = ['| Mã | Quy trình | Nhóm | Quy trình chuẩn ERP | Module |', '|---|---|---|---|---|']
for code, group, std, mods in CATALOG:
    _rows.append('| %s | %s | %s | %s | %s |' % (bp(code), title(code), group, std, mods))
EXTRA = '## {sec}. Danh mục quy trình\n\n' + '\n'.join(_rows)

PROCESS = dict(
    extra_md=EXTRA,
    id='BP-00',
    name='Tổng quan chuỗi giá trị của doanh nghiệp điều hành tour',
    objective='Cho thấy các quy trình BP-01 → BP-16 nối với nhau thế nào: dòng hoạch định (sản phẩm, nguồn cung), '
              'dòng đơn hàng của từng đoàn (bán → điều hành → thực hiện → quyết toán → chăm sóc), và dòng tài chính định kỳ.',
    trigger='Ba điểm khởi động: chu kỳ hoạch định hằng tháng; khách có nhu cầu; cuối tháng kế toán. '
            'Dòng hoạch định và dòng khách hàng có nhịp khác nhau (tháng / từng yêu cầu) nên không nối bằng mũi tên tuần tự '
            'mà nối qua dữ liệu dùng chung: S&OP công bố lịch khởi hành, quỹ chỗ, giá → Kinh doanh chỉ bán trên đó; '
            'booking và số liệu bán quay về làm đầu vào cho kỳ S&OP sau.',
    outcome='Sản phẩm và chỗ sẵn sàng bán; mỗi đoàn được phục vụ và quyết toán; kỳ kế toán được khóa.',
    scope='Mức tổng quan: mỗi ô là một quy trình chi tiết (call activity), bấm vào tên để xem sơ đồ chi tiết.',
    modules=['Toàn bộ'],
    erp_standard='Chuỗi giá trị: Plan (S&OP) → Source (hợp đồng NCC) → Make (thiết kế, điều hành) → Sell/Deliver (bán, thực hiện) '
                 '→ Settle (quyết toán, công nợ) → Report (khóa sổ).',
    pool_name='Công ty lữ hành — chuỗi giá trị',
    lanes=[
        lane('DIR', 'Hoạch định mùa vụ (S&OP).'),
        lane('PROD', 'Nguồn cung và sản phẩm.'),
        lane('SALES', 'Bán tour ghép và tour thiết kế riêng.'),
        lane('OPS', 'Chốt chuyến, đặt dịch vụ, chuẩn bị đoàn.'),
        lane('GUIDE', 'Thực hiện tour.'),
        lane('ACC', 'Quyết toán, công nợ, khóa sổ.'),
        lane('CS', 'Chăm sóc khách hàng sau tour.'),
    ],
    lane_rows={'DIR': 2, 'PROD': 2, 'SALES': 2},
    pools=[pool('KH', 'top')],
    nodes=[
        N('S1', 'start', 'DIR', 0, 'Chu kỳ hoạch định hằng tháng', ev='timer'),
        N('C04', 'call', 'DIR', 1, call_name('BP-04'), called='BP-04'),
        N('P1', 'and', 'PROD', 2, ''),
        N('C02', 'call', 'PROD', 3, call_name('BP-02'), called='BP-02'),
        N('C03', 'call', 'PROD', 3, call_name('BP-03'), row=1, called='BP-03'),
        N('P2', 'and', 'PROD', 4, ''),
        N('E1', 'end', 'PROD', 5, 'Sản phẩm và chỗ sẵn sàng bán'),
        N('S2', 'start', 'SALES', 6, 'Khách có nhu cầu', ev='message'),
        N('G1', 'xor', 'SALES', 7, 'Loại tour?'),
        N('C05', 'call', 'SALES', 8, call_name('BP-05'), called='BP-05'),
        N('C06', 'call', 'SALES', 8, call_name('BP-06'), row=1, called='BP-06'),
        N('C07', 'call', 'OPS', 9, call_name('BP-07'), called='BP-07'),
        N('M2', 'xor', 'OPS', 10, ''),
        N('C08', 'call', 'OPS', 11, call_name('BP-08'), called='BP-08'),
        N('C09', 'call', 'GUIDE', 12, call_name('BP-09'), called='BP-09'),
        N('P3', 'and', 'ACC', 13, ''),
        N('C10', 'call', 'ACC', 14, call_name('BP-10'), called='BP-10'),
        N('C14', 'call', 'CS', 14, call_name('BP-14'), called='BP-14'),
        N('P4', 'and', 'ACC', 15, ''),
        N('E2', 'end', 'ACC', 16, 'Đoàn đã phục vụ và quyết toán xong'),
        N('S3', 'start', 'ACC', 0, 'Cuối tháng', ev='timer'),
        N('C15', 'call', 'ACC', 1, call_name('BP-15'), called='BP-15'),
        N('E3', 'end', 'ACC', 2, 'Kỳ kế toán đã khóa'),
    ],
    flows=[
        F('S1', 'C04'), F('C04', 'P1', route='vh'), F('P1', 'C02'), F('P1', 'C03'), F('C02', 'P2'), F('C03', 'P2'), F('P2', 'E1'),
        F('S2', 'G1'),
        F('G1', 'C05', 'Tour ghép', default=True),
        F('G1', 'C06', 'Thiết kế riêng'),
        F('C05', 'C07'), F('C07', 'M2'), F('C06', 'M2'),
        F('M2', 'C08'), F('C08', 'C09'), F('C09', 'P3'),
        F('P3', 'C10'), F('P3', 'C14'), F('C10', 'P4'), F('C14', 'P4'), F('P4', 'E2'),
        F('S3', 'C15'), F('C15', 'E3'),
    ],
    messages=[
        M('KH', 'S2', 'Yêu cầu, đặt chỗ'),
    ],
    data=[
        D('D1', 'store', 'Lịch khởi hành, quỹ chỗ, giá theo mùa', 'DIR', 7,
          links=[('C04', 'out'), ('C05', 'in')]),
        D('D2', 'store', 'Booking và số liệu bán thực tế', 'DIR', 5, row=1,
          links=[('C05', 'out'), ('C06', 'out'), ('C04', 'in')]),
    ],
    annotations=[
        A('N1', 'C02', 'Mọi quy trình dùng chung danh mục của BP-01 Quản lý dữ liệu gốc', 'DIR', 3, row=1),
        A('N2', 'C05', 'Gọi BP-11 thu cọc và thu đủ; BP-13 khi đổi hoặc hủy', 'PROD', 9, row=1),
        A('N3', 'C08', 'Gọi BP-12 trả trước NCC', 'SALES', 11, row=1),
        A('N4', 'C09', 'Gọi BP-13 khi sự cố làm đổi dịch vụ của khách', 'ACC', 12),
        A('N5', 'C10', 'Gọi BP-11, BP-12, BP-16 để chi phí và công nợ của tour đủ trước khi đóng', 'GUIDE', 14),
    ],
    references=[
        book('W', 'ch17-appendix-a-fundamentals-of-erp.md', 'Hệ phân cấp hoạch định ERP: kế hoạch kinh doanh → S&OP → lịch chi tiết → thực thi → phản hồi; một bộ số.'),
        book('W', 'ch03-company-wide-implementation-overview.md', 'Lập lịch triển khai theo chức năng nghiệp vụ, không theo module phần mềm.'),
        book('P', 'ch03-erp-modules.md', 'Luồng liên module Sales → Shipping → Billing; mỗi quy trình phải vẽ liên module.'),
        book('O', 'ch03-erp-systems-background.md', 'MAPs: Models – Artifacts – Processes; quy trình liên chức năng là xương sống của đặc tả.'),
        book('E', 'ch10-cross-case-analysis-discussion.md', '11 giả định kiểm soát của ERP: tích hợp, chuẩn hóa, tự động hóa, phòng ngừa, giám sát liên tục…'),
    ],
)
