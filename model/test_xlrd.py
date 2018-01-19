# -*- coding:utf-8 -*-
import xlrd
import sys
import codecs


reload(sys)
sys.setdefaultencoding("utf-8")
filename=r"C:\Users\simon\Desktop\test.xlsx"
print filename
workbook = xlrd.open_workbook(filename)
table = workbook.sheets()[0]
print workbook.nsheets

for i in range(workbook.nsheets):
    sheet = workbook.sheets()[i]
    print sheet.name
    #遍历行
    rowsLen = sheet.nrows
    for j in range(rowsLen):
        print sheet.row_values(j)
    #遍历列
    colsLen  = sheet.ncols
    for colIndex in range(colsLen):
        print sheet.col_values(colIndex)

