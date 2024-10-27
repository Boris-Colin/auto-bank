import pandas as pd
import numpy as np
import xlwt
import openpyxl
from xlwt import Workbook


path = "C:\\Users\\1thom\\OneDrive\\Bureau\\Ultimate_Budget_Empty.xlsx"

wb = openpyxl.load_workbook(path)
sheet = wb["Tracking Budget"]

# Define the starting row of the table
table_start_row = 11  # Adjust this to where your table actually begins

# Find the first empty row within the table
first_empty_row = table_start_row
while sheet.cell(row=first_empty_row, column=2).value is not None:
    first_empty_row += 1

print(first_empty_row)
