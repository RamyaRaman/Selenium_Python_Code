import openpyxl

path = 'G:\Python\WriteData.xlsx'
workbook = openpyxl.load_workbook(path)
sheet = workbook.active #if only one sheet
#sheet = workbook.get_sheet_by_name("Sheet1") #if many sheet are there

for r in range(1,6):
    for c in range(1,4):
        sheet.cell(row=r,column=c).value = "welcome"
workbook.save(path)

