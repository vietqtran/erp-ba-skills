"""Post-process a pandoc .docx: table borders, blue bold header row, 9.5pt text in tables, Arial font.
Formatting is written into each table directly, because Google Docs ignores Word table styles.

    python3 docx_style.py <in.docx> <out.docx>
"""
import re
import sys
import zipfile

src, dst = sys.argv[1:3]
B = ('<w:tblBorders>' + ''.join(f'<w:{s} w:val="single" w:sz="4" w:space="0" w:color="999999"/>'
                                 for s in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV')) + '</w:tblBorders>')
SH = '<w:shd w:val="clear" w:color="auto" w:fill="D9E2F3"/>'


def header_row(m):
    row = re.sub(r'<w:tcPr>', '<w:tcPr>' + SH, m.group(0))
    row = re.sub(r'<w:tc>(?!<w:tcPr>)', '<w:tc><w:tcPr>' + SH + '</w:tcPr>', row)
    row = re.sub(r'<w:r>(?!<w:rPr>)', '<w:r><w:rPr><w:b/></w:rPr>', row)
    return re.sub(r'<w:r><w:rPr>(?!<w:b/>)', '<w:r><w:rPr><w:b/>', row)


def table(m):
    t = re.sub(r'<w:tr>.*?</w:tr>', header_row, m.group(0), count=1, flags=re.S)
    t = re.sub(r'<w:r>(?!<w:rPr>)', '<w:r><w:rPr></w:rPr>', t)
    return t.replace('<w:rPr>', '<w:rPr><w:sz w:val="19"/><w:szCs w:val="19"/>')


zin, zout = zipfile.ZipFile(src), zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED)
for item in zin.infolist():
    data = zin.read(item.filename)
    if item.filename == 'word/document.xml':
        x = data.decode('utf-8').replace('<w:tblPr>', '<w:tblPr>' + B)
        data = re.sub(r'<w:tbl>.*?</w:tbl>', table, x, flags=re.S).encode('utf-8')
    elif item.filename == 'word/theme/theme1.xml':
        data = data.decode('utf-8').replace('typeface="Aptos Display"', 'typeface="Arial"').replace('typeface="Aptos"', 'typeface="Arial"').encode('utf-8')
    elif item.filename == 'word/styles.xml':
        data = (data.decode('utf-8').replace('<w:sz w:val="24" />', '<w:sz w:val="22" />', 1)
                .replace('<w:rFonts w:asciiTheme="minorHAnsi" w:eastAsiaTheme="minorEastAsia" w:hAnsiTheme="minorHAnsi" w:cstheme="minorBidi" />',
                         '<w:rFonts w:ascii="Arial" w:eastAsia="Arial" w:hAnsi="Arial" w:cs="Arial" />').encode('utf-8'))
    zout.writestr(item, data)
zout.close()
