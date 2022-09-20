import pandas as pd
import numpy as np

pd.options.plotting.backend = 'plotly'

def main():
    daily_index = pd.date_range('2020-02-28', periods=4, freq='D')
    print(daily_index, '\n')

    weekly_index = pd.date_range('2020-01-01', '2020-01-31', freq='W-SUN')
    print(weekly_index, '\n')

    visitors = pd.DataFrame(data=[21, 15, 33, 34], columns=['visitors'], index=weekly_index)
    print(visitors, '\n')


if __name__ == '__main__':
    main()