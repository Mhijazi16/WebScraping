#!/usr/bin/python3
from openpyxl import workbook, load_workbook

wb = load_workbook('Book1.xlsx')
sheetONE = wb.active

for row in range(1,7):
    for col in range(1,3):
        s = chr(64+col)
        print(sheetONE[s+str(1)].value,"\t",sheetONE[s+str(2)].value)
    