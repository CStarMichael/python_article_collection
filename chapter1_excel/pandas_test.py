import pandas as pd
import numpy as np


def data_init():
    # s1 = pd.Series([1, 3, 5, np.nan, 6, 8])
    # s2 = pd.Series([1, 3, 5, np.nan, 6, 8], index=['A', 'B', 'C', 'D', 'E', 'F'])
    # print('1、创建默认index的Series: \n', s1)
    # print('1、创建指定index的Series: \n', s2)

    date = pd.date_range('20210101', periods=6)
    value = np.arange(1, 19).reshape(6, 3)
    df = pd.DataFrame(data=value, index=date, columns=['column1', 'column2', 'column3'])
    df['column4'] = ['one', 'two', 'three', 'four', np.nan, np.nan]
    # print('1、生成的日期为： \n', date, '\n')
    # print('2、生成的连续数组为： \n', value, '\n')
    print('3、 创建的DataFrame为： \n', df, '\n')

    # df2 = pd.DataFrame({
    #     'column1': pd.date_range('20210101', periods=4, freq='7D'),
    #     'column2': pd.Series(np.arange(4), dtype='float'),
    #     'column3': np.array([1, 2, 3, 4]),
    #     'column4': ['This', 'is', 'Pandas', '!']
    # })
    # print('4、通过字典对象创建的DataFrame为： \n', df2, '\n')

    # print('1、查看前5行数据： \n', df.head(), '\n')
    # print('2、查看最后3行数据： \n', df.tail(3), '\n')
    # print('3、查看数据概览： \n', df.describe(), '\n')

    # print('1、查看DataFrame的行索引： \n', df.index, '\n')
    # print('2、查看DataFrame的列名： \n', df.columns, '\n')
    # print('3、查看DataFrame的数据： \n', df.values, '\n')

    # print(df.T)
    # print('4、按行索引进行排序： \n', df.sort_index(axis=0, ascending=False), '\n')
    # print('5、按列名进行排序： \n', df.sort_index(axis=1), '\n')
    # print('6、按column1列进行排序： \n', df.sort_values(by='column1', ascending=False), '\n')
    df['column1'].replace(4, value='NEW', inplace=True)
    print('数据替换后的DataFrame为： \n', df, '\n')

    # 数据筛选
    # print('7、选择column1列数据： \n', df['column1'], '\n')
    # print('8、选择1到3行数据： \n', df[0:3], '\n')
    # print('9、通过loc标签选择数据： \n', df.loc['2021-01-01':'2021-01-04', ['column1', 'column2']], '\n')
    # print('10、通过行和列选择数据： \n', df.iloc[3:5, 0:2], '\n')
    # print('11、行切片： \n', df.iloc[1:3, :], '\n')
    # print('12、列切片： \n', df.iloc[:, 1:3], '\n')
    # print('13、根据列值筛选： \n', df[df['column1'] > 5], '\n')
    # print('14、根据字符串条件筛选： \n', df[df['column4'].isin(['two', 'four'])], '\n')
    #
    # # 数据处理
    # print('15、删除缺失值的数据： \n', df.dropna(how='any'), '\n')
    # print('16、填充缺失值的数据： \n', df['column4'].fillna('这是空值！'), '\n')


# 数据合并
def data_combine():
    # merge
    # left = pd.DataFrame({'userid': ['user1', 'user2', 'user3'], 'age': [20, 30, 23]})
    # right = pd.DataFrame({'userid': ['user1', 'user2', 'user4'], 'score': [70, 80, 90]})
    # print('17、left初始数据： \n', left, '\n')
    # print('18、right初始数据： \n', right, '\n')
    # print('19、merge默认内连接： \n', pd.merge(left, right), '\n')
    # print('20、merge左连接： \n', pd.merge(left, right, left_on='userid', right_on='userid', how='left'), '\n')

    # join
    left1 = pd.DataFrame([{'name': '张三', 'age': 20}, {'name': '李四', 'age': 22},
                          {'name': '王五', 'age': 24}, {'name': '赵六', 'age': 26}],
                         index=['user1', 'user2', 'user3', 'user4'])
    right1 = pd.DataFrame([{'gender': '男'}, {'gender': '女'}, {'gender': '男'}], index=['user1', 'user2', 'user5'])
    print('21、left1初始数据： \n', left1, '\n')
    print('22、right1初始数据： \n', right1, '\n')
    print('23、join默认左连接： \n', left1.join(right1), '\n')
    print('24、join实现右连接： \n', left1.join(right1, how='right'), '\n')
    print('25、join实现内连接： \n', left1.join(right1, how='inner'), '\n')

    # concat
    print('26、concat上下进行合并： \n', pd.concat([left1, right1], axis=0), '\n')
    print('27、concat左右进行合并： \n', pd.concat([left1, right1], axis=1, join='outer'), '\n')


# 统计分析
def data_analysis():
    df = pd.DataFrame({'Category': ['手机', '手机', '手机', '电脑', '电脑', '电视机', '电视机', '电视机', '电视机'],
                       'Product': ['HUAWEI', ' iPhone', 'XiaoMi', 'MacBook', '联想笔记本', 'TCL电视机', '创维电视机',
                                   '小米电视机', '索尼电视机'],
                       'Month': [' 2021-01', ' 2021-01', ' 2021-02', ' 2021-02', ' 2021-01', ' 2021-01', ' 2021-01',
                                 ' 2021-01', ' 2021-02'],
                       'Quantity': [10, 15, 10, 15, 20, 25, 10, 15, 25],
                       'Sales': [60000, 90000, 40000, 150000, 120000, 50000, 80000, 75000, 250000]})
    print('28、df原始数据： \n', df, '\n')
    print('29、按照产品类别Category进行分组，并对销量Quantity进行sum求和: \n',
          df.groupby(['Category']).agg({'Quantity': 'sum'}), '\n')
    print('30、每个产品类别下的最小销量、最大销售额和产品数: \n',
          df.groupby(['Category']).agg({'Quantity': 'min', 'Sales': 'max', 'Product': 'count'}), '\n')

    # 数据透视表
    print('31、不同产品类别、每个月的销售量总和及平均值。: \n',
          pd.pivot_table(df, values='Quantity', index=['Category'], columns=['Month'], aggfunc=[np.sum, np.mean]), '\n')


# 文件读写
def data_read_write():
    df = pd.DataFrame({'Category': ['手机', '手机', '手机', '电脑', '电脑', '电视机', '电视机', '电视机', '电视机'],
                       'Product': ['HUAWEI', ' iPhone', 'XiaoMi', 'MacBook', '联想笔记本', 'TCL电视机', '创维电视机',
                                   '小米电视机', '索尼电视机'],
                       'Month': [' 2021-01', ' 2021-01', ' 2021-02', ' 2021-02', ' 2021-01', ' 2021-01', ' 2021-01',
                                 ' 2021-01', ' 2021-02'],
                       'Quantity': [10, 15, 10, 15, 20, 25, 10, 15, 25],
                       'Sales': [60000, 90000, 40000, 150000, 120000, 50000, 80000, 75000, 250000]})

    df.to_csv('df_csv.csv', encoding='utf-8', index=False)
    df_csv = pd.read_csv('../files/before/df_csv.csv')
    print('32、csv文件数据： \n', df_csv, '\n')

    df.to_excel('df_excel.xlsx', sheet_name='Sheet1', index=False)
    df_excel = pd.read_excel('../files/before/df_excel.xlsx', 'Sheet1')
    print('33、xlsx文件数据： \n', df_excel, '\n')


# 数据库读写
def data_mysql():
    pass
    # df = pd.DataFrame({'Category': ['手机', '手机', '手机', '电脑', '电脑', '电视机', '电视机', '电视机', '电视机'],
    #                    'Product': ['HUAWEI', ' iPhone', 'XiaoMi', 'MacBook', '联想笔记本', 'TCL电视机', '创维电视机',
    #                                '小米电视机', '索尼电视机'],
    #                    'Month': [' 2021-01', ' 2021-01', ' 2021-02', ' 2021-02', ' 2021-01', ' 2021-01', ' 2021-01',
    #                              ' 2021-01', ' 2021-02'],
    #                    'Quantity': [10, 15, 10, 15, 20, 25, 10, 15, 25],
    #                    'Sales': [60000, 90000, 40000, 150000, 120000, 50000, 80000, 75000, 250000]})
    # engine = create_engine()


def main():
    data_init()
    # data_combine()
    # data_analysis()
    # data_read_write()


if __name__ == '__main__':
    main()
