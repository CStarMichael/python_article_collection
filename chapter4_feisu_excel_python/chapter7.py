from pathlib import Path

import pandas as pd
import numpy as np


def path_init():
    this_dir = Path(__file__).resolve().parent
    return this_dir


def sales_report_pandas(this_dir):
    parts = []
    for path in (this_dir / 'files/sales_data').rglob('*.xls*'):
        print(f'Reading {path.name}')
        part = pd.read_excel(path, index_col='transaction_id')
        parts.append(part)

    df = pd.concat(parts)
    pivot = pd.pivot_table(df, index='transaction_date', columns='store', values='amount', aggfunc='sum')
    summary = pivot.resample('M').sum()
    summary.index.name = 'Month'
    summary.to_excel(this_dir / 'files/sales_report_pandas.xlsx')


def fix_missing(x):
    return False if x in ['', 'MISSING'] else x

def read_excel_test(this_dir):
    df = pd.read_excel(this_dir / 'files/stores.xlsx', sheet_name='2019', skiprows=1, usecols='B:F',
                       converters={'Flagship': fix_missing})
    print('stores.slxs表格原始数据：', '\n', df, '\n')
    print('stores.slxs表格数据类型：', '\n', df.info(), '\n')

    sheets = pd.read_excel(this_dir / 'files/stores.xlsx', sheet_name=['2019', '2020'], skiprows=1,
                           usecols=['Store', 'Employees'])
    print('sheets表格数据：', '\n', sheets['2019'].head(2), '\n')


def with_test(this_dir):
    with pd.ExcelFile(this_dir / 'files/stores.xlsx') as f:
        df1 = pd.read_excel(f, '2019', skiprows=1, usecols='B:F', nrows=2)
        df2 = pd.read_excel(f, '2020', skiprows=1, usecols='B:F', nrows=2)
    print('表单2019数据：', '\n', df1, '\n')
    print('表单2020数据：', '\n', df2, '\n')


def main():
    # df = pd.read_excel('../files/feisu/sales_data/new/January.xlsx')
    # print('文件信息：', '\n', df.info(), '\n')
    this_dir = path_init()
    # read_excel_test(this_dir)
    # sales_report_pandas(this_dir)
    with_test(this_dir)


if __name__ == '__main__':
    main()
