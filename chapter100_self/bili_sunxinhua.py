import numpy as np
import pandas as pd
import pymysql
import datetime as dtime

# def data_add(n):
#     a = np.arange(1, n+1) ** 3
#     b = np.arange(1, n+1) ** 2
#     return a + b
#
# print(data_add(3))

# a = np.array([1, 2, 3, 4, 5])
# b = np.array(range(1, 6))
# c = np.arange(1, 6)
#
# print(a)
# print(b)
# print(c)
# print(a.dtype)
# print(type(a))
# print(a.shape)
# print(a.size)
# print(a.ndim)


# a = np.ones(4)
# print(a)
# b = np.ones((2, 3,3))
# print(b)
# c = np.zeros((2, 4, 5))
# # print(c.ndim)
# d = np.full((3, 3), 520)

# a = np.array([[0, 1, 2], [3, 4, 5]])
# b = np.ones_like(a)
# print(a)
# print(b)

# c = np.random.randn(3,2,4)
# print(c)

# a = np.arange(10).reshape(2,5)
# print(a)
#
# print(a + 1)
#
# b = np.random.randn(2,5)
# print('-' * 30)
# print(b)
# print('-' * 30)
# print(a+b)

# a = np.arange(12).reshape(3, 2,2)
# b = np.random.randn(2,3)
# print(a)
# print('-'*50)
# print(b)
#
# print(a+b)

# a = np.arange(10)
# b = np.arange(20).reshape(4, 5)
# # print(a)
# # print('--'*40)
# # print(a[4])
# # print('--'*40)
# print(b)
# print('--'*40)
# print(b[0:2,2:4])
# print('--'*40)
# print(b[0:-1])
# print('--'*40)
# print(b[:,2])

# a = np.arange(10)
# print(a)
# # print('-'*40)
# # aa = a > 5
# # print(aa)
# # print('-'*40)
# # print(a[aa])
# # print('-'*40)
# # a[a<=5] = 0
# # a[aa] = 1
# # print(a)
# a[a>5] += 520
# print(a)

# a = np.arange(1,21).reshape(4,5)
# print(a,'\n')
# b = a > 10
# print(b,'\n')
# print(a[b],'\n')
#
# print(a[:,3],'\n')
# # c = a[:,3]>5
# # a[c] = 520
# # print(a,'\n')
# a[:,3][a[:,3]>5] = 520
# print(a)

# a = np.arange(10)
# print(a)
# b = (a%2==0)|(a<7)
# print(b)
# print(a[b])

# a = np.arange(36).reshape(9,4)
# print(a,'\n')
# # print(a[[4,3,0,6]],'\n')
# # print(a[[1,5,7,2],[0,3,2,1]])
# print(a[:,[1,2]])

# a = np.random.randint(1, 100, 10)
# print(a, '\n')
# b = a.argsort()[-3:]
# print(b,'\n')

# a = np.arange(24).reshape((4,6))
# print(a,'\n')
# b = a.transpose()
# print(b,'\n')
# c = a.swapaxes(1,0)
# print(c)

# a = np.random.randint(3)
# print(a,'\n')

# a = np.random.normal(1, 10, 10)
# print(a,'\n')

# a = np.array([1,2,3,4,5,6,5,4,3])
# print(a, '\n')
# # print(np.cumsum(a),'\n')
# # print(np.argmax(a),'\n')
# count = np.bincount(a)
# print(np.argmax(count),'\n')

# a = np.array([[1,2,3],[3,2,5],[4,5,6]])
# print(a,'\n')
# # print(np.sum(a, axis=0))
# # print(np.sum(a, axis=1))
# print(a>3,'\n')
# # print(np.where(a>3,520,1324))
#
# print((a>3).sum())

# a = np.array([3,4,5,6,3,5,8,32,4,63,2,1,90])
# a.sort()
# print(a,'\n')

# a = np.array([[1,2,32],[2,3,23],[56,4,6]])
# print(a,'\n')
# print(np.sort(a),'\n')
# print(np.sort(a,axis=0),'\n')
# print(np.sort(a, axis=1), '\n')


#
# # data = pd.read_csv(csv_path)
# # data = pd.DataFrame({'序号': [1,2,3], '姓名':['叶问', '李小龙', '蔡国强']})
# # data = data.set_index('序号')
# # data.to_csv(newfile)
#
# data = pd.read_csv(csv_path,skiprows=[2,3],nrows=4)
# print(data.head())

# conn = pymysql.connect(host='localhost', user='michael',
#                        password='michael', database='hrs',
#                        charset='utf8')
#
# data = pd.read_sql('select * from limit_word_all', con=conn)
# print(data)


# data = pd.read_excel(xls_path,index_col='日期', nrows=10)
# print(data)
# data = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=['a', 'b', 'c'])
# data = pd.read_excel(xls_path)
# print(data.head(3),'\n')
# print(data[['日期','总计']][1])


# print(data,'\n')
# print(data['a'][0],'\n')
# print(data.loc[0]['a'],'\n')
# print(data.iloc[0][2],'\n')
# print(data[['a','b']])

# data = {
#     ''
#     '姓名':['孙孙池','李小龙','蔡国强'],
#     '年龄':[20,30,40],
#     '功夫':['健身', '截拳道', '咏春']
# }
#
# df = pd.DataFrame(data)
# print(df, '\n')
# print(df.dtypes,'\n')
# print(df.index,'\n')
# print(df['姓名'],'\n')
# print(df.loc[1]['姓名'])

csv_path = r'E:\Work\Workspaces\Anaconda\data\模拟数据.csv'
xls_path = r'E:\Work\Workspaces\Anaconda\data\模拟数据.xlsx'
sun_xls_path = r'E:\Work\Workspaces\Anaconda\data\sun\多层索引.xlsx'
file_path = r'E:\Work\Workspaces\Anaconda\data'
newfile = r'E:\Work\Workspaces\Anaconda\data\data.csv'
# data = pd.read_excel(sun_xls_path, index_col='序号', parse_dates=['出生年月'])
data = pd.read_excel(sun_xls_path, sheet_name='无序',index_col=[0,1])
# data = pd.read_excel(sun_xls_path, sheet_name='有序')
# data = data.set_index('班级','学号')
print(data,'\n')

#
# data = pd.read_excel(xls_path, skiprows=8,usecols='F:I',
#                      dtype={'序号':str, '性别':str, '日期':str})
# print(data,'\n')
# print(data.head(3),'\n')
# print(data.tail(3),'\n')
# print(data.shape)
# print(data.fillna(0))
# print(data.replace('2022-12-01 00:00:00','aaa'))
# print(data.isnull())
# print(data.notnull())
# print(data['农行1069'].unique())
# df = data.apply(pd.to_numeric, errors='ignore')
# print(df.dtypes)

# data1 = pd.Series([0,1,2], index=['A','B','C'])
# data2 = pd.Series([3,4], index=['D','E'])
# data3 = pd.concat([data1,data2])
# data4 = pd.concat([data1, data2], axis=1)
# print(data1, '\n')
# print(data2, '\n')
# print(data3, '\n')
# print(data4, '\n')
# data = pd.read_csv(csv_path,dtype={'序号':str, '性别':str, '日期':str})
# startdate = dtime.date(2022,12,4)
#
# def add_month(date, inmonth):
#     year = inmonth // 12
#     month = date.month + inmonth % 12
#     if month != 12:
#         year = year + month // 12
#         month = month % 12
#     return dtime.date(date.year+year, month,date.day)
#
# for i in data.index:
#     data['序号'].at[i] = i + 1
#     data['性别'].at[i] = '男' if i%2 == 0 else '女'
#     # data['日期'].at[i] = startdate + dtime.timedelta(days=i)
#     # data['日期'].at[i] = dtime.date(startdate.year + i, startdate.month, startdate.day)
#     data['日期'].at[i] = add_month(startdate,i)
# #
# data.set_index('序号', inplace=True)
# # data.to_excel(xls_path)
# data.to_csv(csv_path)
# print(data)
#
# def add_price(x):
#     return x + 3


# data = pd.read_excel(xls_path, index_col='序号')
# # data['销售金额'] = data['销售数量'] * data['单价']
# # for i in range(1,3):
# #     data['销售金额'].at[i] = data['单价'].at[i] * data['销售数量'].at[i]
# # data['单价'] = data['单价'].apply(add_price)
# # data['单价'] = data['单价'].apply(lambda x: x + 3)
# data['加分'] = data['民族'].apply(lambda x:5 if x != '汉' else 0)
# data['最终得分'] = data['总分'] + data['加分']
# data['姓名字数'] = data['姓名'].apply(len)
# print(data,'\n')
# print(list('xyz'))

# data = pd.DataFrame(np.arange(1,10).reshape([3,3]),
#                     columns=list('xyz'),index=list('abc'))
# print(data,'\n')
# # data2 = data.apply(np.square)
# data2 = data.apply(lambda m:np.square(m) if m.name in ['x','y'] else m)
# print(data2)

# data = pd.read_csv(csv_path, index_col='姓名')
# data.sort_values(by='语文', inplace=False, ascending=False)
# data.sort_values(by=['语文', '数学','英语'], inplace=True,ascending=False)
# data = pd.read_excel(xls_path, index_col='序号',sheet_name='Sheet1')
# # print(data.loc['廖婷婷':'龙兵',['出生年月','详细地址','所在省份']])
# # print(data.loc[['廖婷婷','龙兵'],['出生年月','详细地址','所在省份']])
# # print(data.loc[['廖婷婷','龙兵'],'详细地址':'Time'])
# # print(data.loc[(data['语文'] >= 66) & (data['数学'] <= 90), '手机号'])
# data.loc[data['性别'] == '男','称呼'] = '先生'
# data.loc[data['性别'] == '女','称呼'] = '女士'
# # data2 = data.loc[2:4]
# print(data.head(), '\n')

# look = data['性别'] == '男'
# print(data[look],'\n')
# look = "性别 == '男' and 语文 >= 90"
# look = "姓名 in ['牛金凤', '黄明']"
# print(data.query(look))
# look = data['姓名'].str.startswith('王')
# look = data['详细地址'].str.contains('河北 ')
# look = data['详细地址'].str.contains('[a-cA-C]座')
# print(data[look])
# look = "80 <= 语文 <= 100 and 性别 == '女'"
# print(data.query(look))


# print(data.head(),'\n')
# print(data.loc['2002-02'].head())
# data2 = data.sort_values('出生年月')
# print(data2.truncate(before='2002-02'))
# print(data2['1996':'2000'])
# look = (
#     '@data.出生年月.dt.year > 1999 and'
#     '@data.出生年月.dt.year < 2003'
#     'and 性别 == "男"'
# )
# print((data.query(look)).head())
# print(data.drop(labels=[1,2]))
# print(data.drop(labels=['性别','详细地址'], axis=1))
# data2 = data.drop(labels=['性别','详细地址'], axis=1)
#
# print(data2)
# print(data.notnull())

# print(data.dropna(subset=['性别']))
# print(data.fillna(540))
# print(data.fillna({'性别':'哈', '姓名':'哈哈'}))
# print(data.fillna(method='ffill'))
# print(data['语文'].describe())
# print(data['语文'].unique())
# print(data['语文'].value_counts())
# print(data.drop_duplicates(subset=['语文'], keep=False))

# print(data.duplicated())
# print(data['语文'].duplicated())
# repeat = data.duplicated(subset='语文')
# print(data[repeat])

# data_ji = data[['语文','数学','英文']]
# print(data_ji,'\n')

# result = data_ji['语文'] + data_ji['数学']
# result = data_ji['语文'].add(data_ji['数学'])
data2 = data.sort_index(level='科目')
data3 = data2.loc[('语文', slice(None)),:]
# data2 = data.loc[('1班',slice(None)),:]
print(data3, '\n')