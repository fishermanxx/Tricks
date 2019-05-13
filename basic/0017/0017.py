# -*- coding:utf-8 -*-
##将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中

import xlrd, json
# import codecs
from lxml import etree

def read_xls(filename):
	data = xlrd.open_workbook(filename)
	table = data.sheets()[0]
	dic = {}
	for i in range(table.nrows):
		# print table.cell(i, 0).value, table.row_values(i)[1:]
		dic[table.cell(i, 0).value] = table.row_values(i)[1:]
	# print dic
	# data = json.dumps(dic, ensure_ascii = False)
	# data = json.dumps(dic, ensure_ascii = False, indent=4, separators=(',', ': '))
	data = json.dumps(dic, ensure_ascii = False, separators=(',', ': '))
	# data = json.dumps(dic)
	print data
	return data

def save_xml(data, filename):
	root = etree.Element('root')
	student = etree.SubElement(root, 'student')
	student.append(etree.Comment(u'学生信息表\n\"id\": [名字, 数学, 语文, 英文]'))	
	student.text = data
	
	tree  =etree.ElementTree(root)
	tree.write(filename, encoding='utf-8', pretty_print=True, 
		xml_declaration=True)


if __name__ == '__main__':
	filename = 'student.xls'
	dic = read_xls(filename)
	output = 'student.xml'
	save_xml(dic, output)