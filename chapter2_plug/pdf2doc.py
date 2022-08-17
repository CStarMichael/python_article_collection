# PDF转Word1import pdfplumber
from pdf2docx import Converter
import re
import pdfplumber
import docx

# 传入文件绝对路径
def pdf_to_word():
    # 正则获取不含文件类型后缀的部分，用于组成word文档绝对路径
    pdf_file = 'aa.pdf'
    name = re.findall(r'(.*?)\.',pdf_file)[0]
    docx_file = f'{name}.docx'
    print(docx_file)

    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()


def pdf_2_word():
    with pdfplumber.open("aa.pdf") as p:
        textdata_all = ''
        for i in range(10):
            page = p.pages[i]
            textdata = page.extract_text()
            textdata_all += textdata
        document = docx.Document()  # 新建一个空白的word文档
        print(textdata_all)
        content = document.add_paragraph(textdata_all)  # 在文档中添加正文段落，将变量textdata导进去
        document.save("aa.docx")  # 保存文档docx，命名为word

def main():
    pdf_to_word()
    # pdf_2_word()

if __name__ == '__main__':
    main()
