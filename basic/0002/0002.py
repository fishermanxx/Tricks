# -*- coding:utf-8 -*-
# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中

import random
import string
import numpy as np
import mysql.connector

def connectdb():
	print("Connect to Mysql Server")
	db = mysql.connector.connect(user="root", passwd="xx123456", database="test")
	print("connected!")
	return db

def createtable(db):
	cursor = db.cursor()
	cursor.execute("drop table if exists coupon")
	sql = """create table coupon (
			ID int(3) primary key,
			code varchar(20) NOT NULL
			)"""
	cursor.execute(sql)
	cursor.close()

def insertdb(db, data):
	# print data
	cursor = db.cursor()
	for i in range(len(data)):	
		print data[i]
		cursor.execute("insert into coupon (id, code) values (%s, %s)" , [i+1, data[i]])
	###check for record
	# cursor.execute('select * from coupon')
	# results = cursor.fetchall()
	# for row in results:
	# 	ID = row[0]
	# 	code = row[1] 
	# 	print "code: %s" % code
	db.commit()
	cursor.close()
	print "Inserte is done!"


def gene_code(filename, length, n):
	result = {}
	source = list(string.ascii_uppercase)
	for i in range(0,10):
		source.append(str(i))
	while len(result) < n:
		# print n
		key = ''
		for i in range(length):
			key += random.choice(source)
		# print key
		if key in result:
			pass
		else:
			result[key] = 1

	f = open(filename, 'w')
	for key in result:
		f.write(key)
		f.write('\n')
	f.close()

def file_read(filename):
	with open(filename, 'r') as f:
		lines = f.readlines()
		for n in range(200):
			lines[n] = lines[n].strip()
	return lines

if __name__ == '__main__':
	filename = 'code.txt'
	digit = 16
	num = 200
	# gene_code(filename, digit, num)
	data = file_read(filename)
	db = connectdb()
	createtable(db)
	insertdb(db, data)
	db.close()
