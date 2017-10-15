
import numpy as np
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

    for row in sheet.iter_rows(min_row=285):
        date = row[0].value
        amount = row[position].value
        if date == None:
            continue
        if amount == 'NA':
            continue
        data[date] = amount
    return data

housedata = data_for_region(xls_path,'San Mateo')

for date, amount in sorted(housedata.items()):
   print('{0:%m}/{0:%Y}: ${1:.2f}'.format(date,amount))

x_raw_val = list(housedata.keys())
y_raw_val = list(housedata.values())

x_train_val = [
    d.month/12 + d.year
    for d in x_raw_val
]

x_train = np.array([x_train_val]).reshape(-1,1)
y_train = y_raw_val



import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(x_train,y_train)

def f(x):
    m, b = model.coef_[0], model.intercept_
    return m * x + b

fitted_x = x_train_val
fitted_y = [f(x) for x in fitted_x]


plt.figure()
plt.plot(x_train,y_train,'k.')
plt.plot(fitted_x,fitted_y,'r')
plt.title('House Data By Region')
plt.xlabel('Date')
plt.ylabel('Amount')
plt.show()

