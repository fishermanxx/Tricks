# -*- coding:utf-8 -*-
# 任一个英文的纯文本文件，统计其中的单词出现的个数

import re

#read the text information

def count_word(filename):
	dic = {}
	with open(filename, 'r') as f:
		lines = f.readlines()
		# print lines
		for line in lines:
			words = re.split('\W+', line)
			# print words

			for word in words:
				if word in dic:
					dic[word] += 1
				else:
					dic[word] = 1
	f.close()
	print dic

if __name__ == '__main__':
	filename='text.txt'
	count_word(filename)
