# -*- coding:utf-8 -*-
#  敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，
# 当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

import os
import chardet

def spe_words(filename):
	words = []
	with open(filename, 'r') as f:
		lines = f.readlines()
		for line in lines:
			word = line.strip().decode('utf-8')  #utf-8 to unicode
			print word
			words.append(word)

	return words

def subst(words):
	while True:
		s = raw_input('Input:')
		s = s.decode('GBK')
		if s == 'quit':
			break
		else:
			for word in words:
				if word in s:
					s = s.replace(word, '*'*len(word))
			print s



if __name__ == '__main__':
	filename = 'filter_words.txt'
	words = spe_words(filename)
	subst(words)


