import re
import pdfplumber
import os
import pandas as pd
from PyPDF2 import PdfFileWriter, PdfFileReader
from pdf2docx import Converter
import docx


def split_pdf(filename, filepath, save_dirpath, step=5):
    """
    拆分PDF为多个小的PDF文件，
    @param filename:文件名
    @param filepath:文件路径
    @param save_dirpath:保存小的PDF的文件路径
    @param step: 每step间隔的页面生成一个文件，例如step=5，表示0-4页、5-9页...为一个文件
    @return:
    """
    if not os.path.exists(save_dirpath):
        os.mkdir(save_dirpath)
    pdf_reader = PdfFileReader(filepath)
    # 读取每一页的数据
    pages = pdf_reader.getNumPages()
    for page in range(0, pages, step):
        pdf_writer = PdfFileWriter()
        # 拆分pdf，每 step 页的拆分为一个文件
        for index in range(page, page + step):
            if index < pages:
                pdf_writer.addPage(pdf_reader.getPage(index))
        # 保存拆分后的小文件
        save_path = os.path.join(save_dirpath, filename + str(int(page / step) + 1) + '.pdf')
        print(save_path)
        with open(save_path, "wb") as out:
            pdf_writer.write(out)

    print("文件已成功拆分，保存路径为：" + save_dirpath)


def concat_pdf(filename, read_dirpath, save_filepath):
    """
    合并多个PDF文件
    @param filename:文件名
    @param read_dirpath:要合并的PDF目录
    @param save_filepath:合并后的PDF文件路径
    @return:
    """
    pdf_writer = PdfFileWriter()
    # 对文件名进行排序
    list_filename = os.listdir(read_dirpath)
    list_filename.sort(key=lambda x: int(x[:-4].replace(filename, "")))
    for filename in list_filename:
        print(filename)
        filepath = os.path.join(read_dirpath, filename)
        # 读取文件并获取文件的页数
        pdf_reader = PdfFileReader(filepath)
        pages = pdf_reader.getNumPages()
        # 逐页添加
        for page in range(pages):
            pdf_writer.addPage(pdf_reader.getPage(page))
    # 保存合并后的文件
    with open(save_filepath, "wb") as out:
        pdf_writer.write(out)
    print("文件已成功合并，保存路径为：" + save_filepath)


def extract_text_info(filepath):
    """
    提取PDF中的文字
    @param filepath:文件路径
    @return:
    """
    with pdfplumber.open(filepath) as pdf:
        # 获取第2页数据
        page = pdf.pages[1]
        print(page.extract_text())


def extract_table_info(filepath):
    """
    提取PDF中的图表数据
    @param filepath:
    @return:
    """
    with pdfplumber.open(filepath) as pdf:
        # 获取第18页数据
        page = pdf.pages[0]
        # 如果一页有一个表格，设置表格的第一行为表头，其余为数据
        table_info = page.extract_table()
        table_info = page.extract_tables()
        df_table = pd.DataFrame(table_info[1:], columns=table_info[0])
        # df_table.to_csv('../files/afer/dmeo.csv', index=False, encoding='gbk')
        df_table.to_csv('E:\\mm\\企业所得税季度A类(2022-07-01 至 2022-09-30).csv', index=False, encoding='gbk')

        # 如果一页有多个表格，对应的数据是一个三维数组
        # tables_info = page.extract_tables()
        # for index in range(len(tables_info)):
        #     # 设置表格的第一行为表头，其余为数据
        #     df_table = pd.DataFrame(tables_info[index][1:], columns=tables_info[index][0])
        #     print(df_table)
        #     # df_table.to_csv('dmeo.csv', index=False, encoding='gbk')


# 传入文件绝对路径 保留pdf原格式
def pdf_to_word():
    # 正则获取不含文件类型后缀的部分，用于组成word文档绝对路径
    pdf_file = 'E:\\mm\\增值税及附加税费（一般纳税人）(2022-07-01 至 2022-07-31).pdf'
    name = re.findall(r'(.*?)\.', pdf_file)[0]
    docx_file = f'{name}.docx'
    print(docx_file)

    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()


# 无法保留pdf原格式
def pdf_2_word():
    with pdfplumber.open("../files/before/aa.pdf") as p:
        textdata_all = ''
        for i in p.pages:
            page = p.pages[i]
            textdata = page.extract_text()
            textdata_all += textdata
        document = docx.Document()  # 新建一个空白的word文档
        print(textdata_all)
        content = document.add_paragraph(textdata_all)  # 在文档中添加正文段落，将变量textdata导进去
        document.save("../files/alfter/aa.docx")  # 保存文档docx，命名为word


def main():
    # 文件拆分
    filename = '22-11-MA.pdf'
    # filepath = '../files/before/22-11-MA.pdf'
    # save_dirpath = '../files/after/'
    # split_pdf(filename, filepath, save_dirpath, step=191)

    # 文件合并
    # read_dirpath = '../files/before/'
    # save_filepath = '../files/after/'
    # concat_pdf(filename, read_dirpath, save_filepath)
    #
    # 提取表格内容
    # filepath = 'E:\\mm\\企业所得税季度A类(2022-07-01 至 2022-09-30).pdf'
    # extract_table_info(filepath)
    pdf_to_word()


if __name__ == '__main__':
    main()
