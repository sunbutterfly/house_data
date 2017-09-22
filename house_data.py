

import openpyxl
xls_path = '/Users/laura/desktop/2017-08_Median_Prices_of_Existing_Detached_Homes_(Historical_Data).xlsx'

def get_row_values(worksheet, row_num):
    rows = list(worksheet.iter_rows(min_row=row_num,max_row=row_num))
    return[cell.value for cell in rows[0]]




def data_for_region(xls_path, region):
    workbook = openpyxl.load_workbook(xls_path)
    sheet = workbook.get_sheet_by_name('Median Price')
    headings = get_row_values(sheet, 8)

    position = 0
    for heading in headings:
        if region == heading:
            print(str(position))
            break
        position +=1

    for row in sheet.iter_rows(min_row=9,min_col=1, max_row=10, max_col=4):
        date = row[0].value
        amount = row[position].value
        print(date,amount)





data_for_region(xls_path,'Amador')