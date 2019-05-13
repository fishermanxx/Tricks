# -*- coding:utf-8 -*-
# 做为 Apple Store App 独立开发者，你要搞限时促销，
#为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

import random
import string
import numpy as np

def gene_code(filename, length, n):
	result = {}
	source = list(string.ascii_uppercase)
	for i in range(0,10):
		source.append(str(i))
	while len(result) < n:
		print n
		key = ''
		for i in range(length):
			key += random.choice(source)
		print key
		if key in result:
			pass
		else:
			result[key] = 1

	f = open(filename, 'w')
	for key in result:
		f.write(key)
		f.write('\n')
	f.close()


if __name__ == '__main__':
	filename = 'code.txt'
	digit = 16
	num = 200
	gene_code(filename, digit, num)
