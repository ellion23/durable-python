import openpyxl as xl
import matplotlib.pyplot as plt

wb = xl.load_workbook('excel11.xlsx')
sht = wb.active
print(sht['A4'].value)
print(sht.cell(row=4, column=1).value)
