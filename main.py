import pandas as pd
import numpy as np
import xlwt
import openpyxl
from xlwt import Workbook

path = "C:\\Users\\1thom\\OneDrive\\Bureau\\Ultimate_Budget_Empty.xlsx"

wb = openpyxl.load_workbook(path)

sheet = wb["Tracking Budget"]

# Note: The first row or
# column integer is 1, not 0.

# Cell object is created by using
# sheet object's cell() method.
cell_obj = sheet.cell(row = 12, column = 4)

# Print value of cell object
# using the value attribute
print(cell_obj.value)




















