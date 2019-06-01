import xlwings as xw
import string

filepath = "C:/Users/mushr/Desktop/433/联赛数据/前锋.xlsx"

app = xw.App(visible=False, add_book=False)
wb = app.books.open(filepath)
sheet = wb.sheets['sheet1']

_list_name = sheet.range('A1:P1').value
_list_value = sheet.range('A2:P2').value
i = 0
for item in _list_value:
    if i == 13:
        num = float(item)
    print("%d:%s" % (i, _list_name[i]), end=":")
    print("".join(item.split()))
    i = i + 1

wb.save()
wb.close()
app.quit()
