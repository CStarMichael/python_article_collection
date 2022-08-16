import pandas as pd
import numpy as np
from pymysql import *


def mysql_create_conn():
    conn = connect(host='localhost', port=3306, database='hrs', user='michael', password='michael', charset='utf8')
    return conn


def mysql_select(conn):
    sql_cmd = 'select * from logsend_2021_abc_1th_season_rawdata'
    df = pd.read_sql(sql_cmd, conn)
    print(df.head(), '\n')
    print(df.info(),'\n')


def main():
    conn = mysql_create_conn()
    mysql_select(conn)


if __name__ == '__main__':
    main()
