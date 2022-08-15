import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def data_init():
    # s1 = pd.Series([1, 3, 5, np.nan, 6, 8])
    # s2 = pd.Series([1, 3, 5, np.nan, 6, 8], index=['A', 'B', 'C', 'D', 'E', 'F'])
    # print('1、创建默认index的Series: \n', s1)
    # print('1、创建指定index的Series: \n', s2)

    date = pd.date_range('20210101', periods=6)
    value = np.arange(1, 19).reshape(6, 3)
    df = pd.DataFrame(data=value, index=date, columns=['column1', 'column2', 'column3'])
    df['column4'] = ['one', 'two', 'three', 'four', np.nan, np.nan]
    # print('1、生成的日期为： \n', date)
    # print('2、生成的连续数组为： \n', value)
    print('3、创建的DataFrame为： \n', df, '\n')

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

    # 数据筛选
    print('7、选择column1列数据： \n', df['column1'], '\n')
    print('8、选择1到3行数据： \n', df[0:3], '\n')
    print('9、通过loc标签选择数据： \n', df.loc['2021-01-01':'2021-01-04', ['column1', 'column2']], '\n')
    print('10、通过行和列选择数据： \n', df.iloc[3:5, 0:2], '\n')
    print('11、行切片： \n', df.iloc[1:3, :], '\n')
    print('12、列切片： \n', df.iloc[:, 1:3], '\n')
    print('13、根据列值筛选： \n', df[df['column1'] > 5], '\n')
    print('14、根据字符串条件筛选： \n', df[df['column4'].isin(['two', 'four'])], '\n')

    # 数据处理
    print('15、删除缺失值的数据： \n', df.dropna(how='any'), '\n')
    print('16、填充缺失值的数据： \n', df['column4'].fillna('这是空值！'), '\n')

# 数据合并
def data_combine():
    print('')


def main():
    # data_init()
    data_combine()

if __name__ == '__main__':
    main()
