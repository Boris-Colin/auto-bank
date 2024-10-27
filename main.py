import pandas as pd
import numpy as np
import xlwt
import openpyxl
from xlwt import Workbook

path = "C:\\Users\\1thom\\OneDrive\\Bureau\\Ultimate_Budget_Empty.xlsx"
path2 = "C:\\Users\\1thom\\Downloads\\export-operations-27-10-2024_08-51-13.csv"

df = pd.read_csv(path2, sep=';')
df_copy = df.drop(columns=['dateVal', 'categoryParent', 'comment', 'accountNum', 'accountLabel', 'accountbalance'])

df_copy['dateOp'] = pd.to_datetime(df_copy['dateOp'], errors='coerce')
# Remove commas and convert 'amount' to float
df_copy['amount'] = df_copy['amount'].str.replace(' ', '').str.replace(',', '.').astype(float)
# Sort by date
df_copy = df_copy.sort_values(by="dateOp")
df_copy['Type'] = np.where(df_copy['amount'] < 0, 'Expenses', 'Income')
cols = ['dateOp', 'Type', 'category', 'amount', 'label']
df_copy = df_copy[cols]

print(df_copy.info())


wb = openpyxl.load_workbook(path)
sheet = wb["Tracking Budget"]

# Define the starting row of the table
table_start_row = 11  # Adjust this to where your table actually begins

# Find the first empty row within the table
first_empty_row = table_start_row
while sheet.cell(row=first_empty_row, column=2).value is not None:
    first_empty_row += 1


for row_idx, row_data in enumerate(df_copy.values, start=first_empty_row):
    for col_idx, value in enumerate(row_data, start=2):  # Start from column 1
        sheet.cell(row=row_idx, column=col_idx, value=value)


wb.save(path)

















