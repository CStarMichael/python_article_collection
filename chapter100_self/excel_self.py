import pandas as pd
import numpy as np


def pd_init():
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)


def data_read_from_excel():
    source_data = pd.read_excel('../files/before/excel_self.xlsx')
    # print(source_data, '\n')
    # print(source_data['日期'], '\n')
    return source_data


def data_init(source_data):
    print('1、查看前5行数据： \n', source_data.head(), '\n')
    print('2、查看最后3行数据： \n', source_data.tail(3), '\n')
    print('3、查看数据概览： \n', source_data.describe(), '\n')

    print('1、查看DataFrame的行索引： \n', source_data.index, '\n')
    print('2、查看DataFrame的列名： \n', source_data.columns, '\n')
    print('3、查看DataFrame的数据： \n', source_data.values, '\n')

    # 数据筛选
    print('7、选择日期列数据： \n', source_data['日期'], '\n')
    print('8、选择1到3行数据： \n', source_data[0:3], '\n')
    print('9、通过loc标签选择数据： \n', source_data.loc['2022-03-10':'2022-03-21', ['日期', '银行']], '\n')
    print('10、通过行和列选择数据： \n', source_data.iloc[3:5, 0:2], '\n')
    print('11、行切片： \n', source_data.iloc[1:3, :], '\n')
    print('12、列切片： \n', source_data.iloc[:, 1:3], '\n')
    print('13、根据列值筛选： \n', source_data[source_data['移动'] > 50000], '\n')
    print('14、根据字符串条件筛选： \n', source_data[source_data['渠道'].isin(['建设之路', '黑名单'])], '\n')


def data_analysis(source_data):
    print('分析1、source_data原始数据： \n', source_data, '\n')
    print('分析2、source_data前10行数据：\n', source_data.head(10), '\n')
    print('分析3、source_data的数据类型：\n', source_data.info(), '\n')
    print('分析4、选择前10行、前12列数据： \n', source_data.iloc[:10, 0:12], '\n')
    print('分析5、按照银行进行分组,并对合计进行sum求和: \n',
          source_data.groupby(['银行']).agg({'合计': 'sum'}), '\n')

    # 数据透视表
    pivot_data = pd.pivot_table(source_data, values='合计', index=['银行'], columns=['日期'],
                                aggfunc=[np.sum, np.mean])
    print('分析6、不同银行、每个月的合计及平均值。: \n', pivot_data, '\n')
    pivot_data.to_excel('../files/after/excel_self_analysis.xlsx')

    format_dict = {'移动': '${0:,.2f}', '联通': '${0:,.2f}', '电信': '${0:,.2f}', '合计': '${0:,.2f}',
                   '内容发送量': '${0:,.2f}', '内容占比': '{:.2%}', '当天总发送量': '${0:,.2f}', '当天占比': '{:.2%}'}
    print('分析7、格式化数据：', '\n', source_data.head().style.format(format_dict), '\n')


def main():
    pd_init()
    source_data = data_read_from_excel()
    # data_init(source_data)
    data_analysis(source_data)


if __name__ == '__main__':
    main()
