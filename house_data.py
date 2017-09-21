

import openpyxl

xls_path ='/Users/laura/desktop'
workbook = openpyxl.load_workbook('2017-08_Median_Prices_of_Existing_Detached_Homes_(Historical_Data).xlsx')
sheet = workbook.get_sheet_by_name('Median Price')


for row in sheet.iter_rows(min_row=8, min_col=1, max_row=10, max_col=4):

    for cell in row:
        value = cell.value
        print(value, end=' ')
    print()

