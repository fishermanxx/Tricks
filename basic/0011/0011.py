# -*- coding:utf-8 -*-

#敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
#当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。


import os
import chardet

#import words
def spe_word(filename):
	words = []
	with open(filename, 'r') as f:
		lines = f.readlines()
		for line in lines:
			# print line.strip()
			word = line.strip().decode('utf-8') #utf-8 to unicode
			print word
			words.append(word)
	return words

def test(words):
	while True:
		s = raw_input("Input: ")
		s = s.decode('GBK')
		if s == 'quit':
			break
		elif s in words:
			print 'Freedom'
		else:
			print 'Human Rights'

if __name__ == '__main__':
	filename = 'filter_words.txt'
	words = spe_word(filename)
	test(words)