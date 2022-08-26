import pandas as pd


def dataframe_simple():
    # df = pd.read_excel('../files/feisu/course_participants.xlsx')
    # print(df)

    data = [['Mark', 55, 'Italy', 4.5, 'Europe'], ['John', 33, 'USA', 6.7, 'America'],
            ['Tim', 41, 'USA', 3.9, 'America'], ['Jenny', 12, 'Germany', 9.0, 'Europe']]
    df = pd.DataFrame(data=data, columns=['name', 'age', 'country', 'score', 'continent'],
                      index=[1001, 1000, 1002, 1003])
    df.index.name = 'user_id'
    print(df, '\n')
    # print(df.info(), '\n')
    # print(df.index, '\n')
    # print(df.reset_index(), '\n')
    # print(df.reset_index().set_index('name'), '\n')
    # print(df.reindex([999, 1000, 1001, 1003]), '\n')
    # print(df.sort_index(), '\n')
    # print(df.sort_values(['continent', 'age']), '\n')
    print(df.columns, '\n')
    df.columns.name = 'properties'
    print(df, '\n')
    # print(df.rename(columns={'name': 'First Name', 'age': 'Age'}), '\n')
    # print(df.drop(columns=['name', 'country']), '\n')
    print(df.T, '\n')
    print(df.loc[:, ['continent', 'country', 'name', 'age', 'score']], '\n')


def data_handle():
    data = [['Mark', 55, 'Italy', 4.5, 'Europe'], ['John', 33, 'USA', 6.7, 'America'],
            ['Tim', 41, 'USA', 3.9, 'America'], ['Jenny', 12, 'Germany', 9.0, 'Europe']]
    df = pd.DataFrame(data=data, columns=['name', 'age', 'country', 'score', 'continent'],
                      index=[1001, 1000, 1002, 1003])
    df.index.name = 'user_id'
    df.columns.name = 'properties'
    print(df, '\n')

    # print(df.loc[1000, 'name'], '\n')
    # print(df.loc[[1000, 1001], 'age'], '\n')
    # print(df.loc[: 1002, ['name', 'country']], '\n')

    # print(df.iloc[0, 0], '\n')
    # print(df.iloc[[0, 2], 1], '\n')
    # print(df.iloc[:3, [0, 2]], '\n')
    #
    # tf = (df['age'] > 40) & (df['country'] == 'USA')
    # print(tf, '\n')
    # print(df.loc[tf, :], '\n')
    # print(df.loc[df.index >= 1001, :], '\n')
    # print(df.loc[df['country'].isin(['Italy', 'Germany']), :], '\n')
    #
    # rainfall = pd.DataFrame(data={'City 1': [300.1, 100.2], 'City 2': [400.3, 300.4], 'City 3': [1008.5, 1100.6]})
    # print(rainfall, '\n')
    # print(rainfall < 400, '\n')
    # print(rainfall[rainfall<400], '\n')

    df_multi = df.reset_index().set_index(['continent', 'country'])
    df_multi = df_multi.sort_index()
    print(df_multi, '\n')
    print(df_multi.loc['Europe', :], '\n')
    print(df_multi.loc['Europe', 'Italy'], '\n')
    print(df_multi.reset_index(level=0), '\n')


def data_set():
    data = [['Mark', 55, 'Italy', 4.5, 'Europe'], ['John', 33, 'USA', 6.7, 'America'],
            ['Tim', 41, 'USA', 3.9, 'America'], ['Jenny', 12, 'Germany', 9.0, 'Europe']]
    df = pd.DataFrame(data=data, columns=['name', 'age', 'country', 'score', 'continent'],
                      index=[1001, 1000, 1002, 1003])
    df.index.name = 'user_id'
    df.columns.name = 'properties'
    print(df, '\n')

    # df2 = df.copy()
    # df2.loc[1000, 'name'] = 'JOHN'
    # print(df2, '\n')
    # df2.loc[[1000, 1001], 'score'] = [3, 4]
    # print(df2, '\n')
    #
    # tf = (df2['age'] < 20) | (df2['country'] == 'USA')
    # df2.loc[tf, 'name'] = 'xxx'
    # print(df2, '\n')
    #
    rainfall = pd.DataFrame(data={'City 1': [300.1, 100.2], 'City 2': [400.3, 300.4], 'City 3': [1008.5, 1100.6]})
    # rainfall2 = rainfall.copy()
    # print(rainfall2, '\n')
    # rainfall2[rainfall2 < 400] = 0
    # print(rainfall2, '\n')
    #
    # print(df2.replace('USA', 'U.S.'), '\n')
    # df2.loc[:, 'discount'] = 0
    # df2.loc[:, 'price'] = [49.9, 49.9, 99.9, 99.9]
    # print(df2, '\n')
    #
    # df3 = df.copy()
    # df3.loc[:, 'birth_year'] = 2021 - df3['age']
    # print(df3, '\n')

    # df4 = df.copy()
    # df4.loc[1000, 'score'] = None
    # df4.loc[1003, :] = None
    # print(df4, '\n')
    # print(df4.dropna(), '\n')
    # print(df4.dropna(how='all'), '\n')
    # print(df4.isna(), '\n')
    # print(df4.fillna({'score': df4['score'].mean()}), '\n')
    #
    # print(df.drop_duplicates(['continent', 'country']), '\n')
    # print(df['country'].is_unique, '\n')
    # print(df['country'].unique(), '\n')
    # print(df['country'].duplicated(), '\n')
    # print(df.loc[df['country'].duplicated(keep=False)], '\n')

    print(rainfall, '\n')
    print(rainfall + 100, '\n')

    more_rainfall = pd.DataFrame(data=[[100, 200], [300, 400]], index=[1, 2], columns=['City 1', 'City 4'])
    print(more_rainfall, '\n')
    print(rainfall + more_rainfall, '\n')
    print(rainfall.add(more_rainfall, fill_value=0), '\n')
    print(rainfall.loc[1, :], '\n')
    print(rainfall + rainfall.loc[1, :], '\n')
    print(rainfall.loc[:, 'City 2'], '\n')
    print(rainfall.add(rainfall.loc[:, 'City 2'], axis=0), '\n')

    print(rainfall.applymap(format_string), '\n')
    print(rainfall.applymap(lambda x: f'{x:,.2f}'), '\n')

    print(rainfall.mean(), '\n')
    print(rainfall.mean(axis=1), '\n')

    print(df.groupby(['continent']).mean(), '\n')
    print(df.groupby(['continent', 'country']).mean(), '\n')
    print(df.loc[:, ['age', 'score', 'continent']].groupby(['continent']).agg(lambda x: x.max() - x.min()), '\n')


def format_string(x):
    return f'{x:,.2f}'


def text_handle():
    users = pd.DataFrame(data=[' mArk ', 'JOHN  ', 'Tim', ' jenny'], columns=['name'])
    print(users, '\n')
    users_cleaned = users.loc[:, 'name'].str.strip().str.capitalize()
    print(users_cleaned, '\n')
    print(users_cleaned.str.startswith('J'), '\n')


def data_pivot_table():
    data = [['Oranges', 'North', 12.30], ['Apples', 'South', 10.55], ['Oranges', 'South', 22.00],
            ['Bananas', 'South', 5.90], ['Bananas', 'North', 31.30], ['Oranges', 'North', 13.10]]
    sales = pd.DataFrame(data=data, columns=['Fruit', 'Region', 'Revenue'])
    print(sales, '\n')

    pivot = pd.pivot_table(sales, index='Fruit', columns='Region', values='Revenue', aggfunc='sum', margins=True,
                           margins_name='Total')
    print(pivot, '\n')
    print(pd.melt(pivot.iloc[:-1, :-1].reset_index(), id_vars='Fruit', value_vars=['North', 'South'],
                  value_name='Revenue'), '\n')


def dataframe_concat():
    data = [['Mark', 55, 'Italy', 4.5, 'Europe'], ['John', 33, 'USA', 6.7, 'America'],
            ['Tim', 41, 'USA', 3.9, 'America'], ['Jenny', 12, 'Germany', 9.0, 'Europe']]
    df = pd.DataFrame(data=data, columns=['name', 'age', 'country', 'score', 'continent'],
                      index=[1001, 1000, 1002, 1003])
    df.index.name = 'user_id'
    df.columns.name = 'properties'

    data = [[15, 'France', 4.1, 'Becky'], [44, 'Canada', 6.1, 'Leanne']]
    more_users = pd.DataFrame(data=data, columns=['age', 'country', 'score', 'name'], index=[1000, 1011])
    print(more_users, '\n')
    print(pd.concat([df, more_users], axis=0), '\n')
    # print(pd.concat([df, more_users], axis=1), '\n')

    df1 = pd.DataFrame(data=[[1, 2], [3, 4], [5, 6]], columns=['A', 'B'])
    print(df1, '\n')
    df2 = pd.DataFrame(data=[[10, 20], [30, 40]], columns=['C', 'D'], index=[1, 3])
    print(df2, '\n')
    # print(df1.join(df2, how='inner'), '\n')
    # print(df1.join(df2, how='left'), '\n')
    # print(df1.join(df2, how='right'), '\n')
    # print(df1.join(df2, how='outer'), '\n')

    df1['category'] = ['a', 'b', 'c']
    df2['category'] = ['c', 'b']
    print(df1, '\n')
    print(df2, '\n')
    print(df1.merge(df2, how='inner', on=['category']), '\n')
    print(df1.merge(df2, how='left', on=['category']), '\n')


def main():
    # dataframe_simple()
    # data_handle()
    # data_set()
    # text_handle()
    # dataframe_concat()
    data_pivot_table()


if __name__ == '__main__':
    main()
