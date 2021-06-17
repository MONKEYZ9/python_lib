# -*- coding: utf-8 -*-

# LV2 : excel / 엑셀 파일을 불러와주세요.
# step2.xlsx

# 결과
# +hoodies 1072
# +hoody 990
# Google Merchandise Store 459
# +sweatshirt 566
# youtuber merch 345
# +tumbler 276
# (not set) 123
# hoodies 247
# +youtube +merchandise 203
# Google Apparel 110
# +youtubers +merch 128
# +youtuber +merch 120
# YouTube Merchandise Store 107
import openpyxl
from pathlib import Path

xlsx_file = Path('C://Users\mingzzang\Desktop\step2.xlsx')
obj = openpyxl.load_workbook(xlsx_file)
sheet = obj.active
for row in sheet.iter_rows(max_row=14):
    for cell in row:
        print(cell.value, end=" ")
    print()
