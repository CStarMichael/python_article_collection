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


def main():
    dataframe_simple()


if __name__ == '__main__':
    main()
