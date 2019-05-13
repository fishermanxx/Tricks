# -*- coding:utf-8 -*-
#你有一个目录，放了你一个月的日记，都是 txt，
#为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词
import re
import os

def loadfile(filepath):
	files = os.listdir(filepath)
	# print files
	new_files, names = [], []
	for file in files:
		name = re.match(r'(.*).txt', file).group(1)
		# print name
		if name is not None:
			names.append(name)
			new_files.append(filepath+file)
	return names, new_files

def count_word(filename, reject_dic):
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
				elif word in reject_dic or len(word)<=3:
					pass
				else:
					dic[word] = 1
	f.close()
	return dic

if __name__ == '__main__':
	reject_dic = ['from', 'with', 'which', 'that', 'this', 'where', 'there', 'Were',
			 'This', 'That', 'were', 'been']
	filepath = './/file//'
	names, paths = loadfile(filepath)
	# print names, paths
	for i in range(len(paths)):
		dic = count_word(paths[i], reject_dic)
		most_import = sorted(dic, key=lambda x:dic[x])[-1:-11:-1]
		print names[i]
		print most_import
		print '='*80