import openpyxl

wb = openpyxl.load_workbook("octobre.xlsx")
print(wb.sheetnames)

sheet = wb['Feuil1']
cell = sheet['D8']

print(f"le nombres de ligne : {sheet.max_row}")
print(f"le nombre des colonnes : {sheet.max_column}")