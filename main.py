import pandas as pd
import numpy as np
import xlwt
from xlwt import Workbook

workbook = xlwt.Workbook()

sheet = workbook.add_sheet("Sheet Name")

# Specifying style
style = xlwt.easyxf('font: bold 1')

# Specifying column
sheet.write(0, 0, 'SAMPLE', style)
workbook.save("sample.xls")