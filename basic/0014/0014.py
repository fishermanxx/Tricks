# -*- coding:utf-8 -*-

#将上述内容写到 student.xls 文件中

# import xlwt
# import re

'''
	Method1===================================================================
'''
# book = xlwt.Workbook(encoding='utf-8', style_compression=0)
# sheet = book.add_sheet('student', cell_overwrite_ok=True)

# info = re.compile(r'\"(\d+)\":\[\"(.*?)\",(\d+),(\d+),(\d+)\]')

# with open('student.txt', 'r') as f:
# 	data = f.read()

# line = 0
# for x in info.findall(data):
# 	for i in range(len(x)):
# 		sheet.write(line, i, x[i])
# 	line += 1
# book.save('student.xls')

'''
	Method1===================================================================
'''
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
		for i in range(len(value)):
			# print i
			sheet.write(row, i+1, value[i])
		row += 1
	book.save('student.xls')
	file.close()


if __name__ == '__main__':
	filename = 'student.txt'
	txt_to_xlsx(filename)



