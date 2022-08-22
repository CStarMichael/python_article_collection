import xlrd2

def main():
    xlsx = xlrd2.open_workbook('aaa.xlsx')
    table = xlsx.sheet_by_index(0)
    value = table.cell_value(2, 1)
    print(value)

    nrows = table.nrows
    print(nrows)

    name_list = [str(table.cell_value(i, 3)) for i in range(0, nrows)]
    print(name_list)

if __name__ == '__main__':
    main()

