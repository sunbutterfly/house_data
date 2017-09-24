

import openpyxl
xls_path = '/Users/laura/desktop/2017-08_Median_Prices_of_Existing_Detached_Homes_(Historical_Data).xlsx'

def get_row_values(worksheet, row_num):
    rows = list(worksheet.iter_rows(min_row=row_num,max_row=row_num))
    return[cell.value for cell in rows[0]]

def data_for_region(xls_path, region):
    workbook = openpyxl.load_workbook(xls_path)
    sheet = workbook.get_sheet_by_name('Median Price')
    headings = get_row_values(sheet, 8)

    position = headings.index(region)

    data = {}

    for row in sheet.iter_rows(min_row=9):
        date = row[0].value
        amount = row[position].value
        if date == None:
            continue
        if amount == 'NA':
            continue
        data[date] = amount
    return data





housedata = data_for_region(xls_path,'Amador')

for date, amount in sorted(housedata.items()):
    print('%s : %s' % (date, amount))
