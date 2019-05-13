# -*- coding:utf-8 -*-

#请将上述内容写到 city.xls 文件中

import xlwt
import re
import json




def txt_to_xlsx(filename):
	file =  open(filename, 'r')
	file_dic = json.load(file, encoding='UTF-8')
	print type(file_dic)

	book = xlwt.Workbook(encoding='utf-8', style_compression=0)
	sheet = book.add_sheet('city', cell_overwrite_ok=True)

	items = file_dic.items()
	items.sort()
	row = 0
	for key, value in items:
		print key, value
		sheet.write(row, 0, key)
		sheet.write(row, 1, value)
		row += 1
	book.save('city.xls')
	file.close()


if __name__ == '__main__':
	filename = 'city.txt'
	txt_to_xlsx(filename)