import xlwings as xw

# app=xw.App()
# pid = app.pid
# # 就是这个App的PID
# app1=xw.App()
# pid1 = app1.pid
# print(pid,pid1) # 6260
#
# count = xw.apps.count
# print(count)
# print(xw.apps.keys())

app = xw.App(visible=True, add_book=False)
app.display_alerts = False  # 关闭提示信息
app.screen_updating = False  # 关闭显示更新

# 创建一个工作薄
wb = app.books.add()
# 工作薄中创建一个sheet表
sht = wb.sheets.add()
# 向表格的A1单元格写入“Hello Python”
sht.range('A2').value = 'Hello Python'
print(sht.range('A2').value)  # 读取
# 保存
wb.save('../files/after/test.xlsx')

wb.close()
app.kill()
