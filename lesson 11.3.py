import csv
from openpyxl import Workbook

csv_f = 'dz19.csv'

with open(csv_f, 'r', encoding="utf-8", newline=" ") as f:
    reader = csv.reader(f)
    header = next(reader)
    excel_file = 'dz20.xlsx'
    workbook = Workbook()
    sheet = workbook.active
    sheet.append(header)

    for row in reader:
        sheet.append(row)
    workbook.save(excel_file)

print('Дані успішно збережено у Excel-файл.')
