# -*- coding:utf-8 -*-
# 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

import os
import re

# load file
def loadfile(path):
	files = os.listdir(path)
	# print files
	names, fpaths = [], []
	for file in files:
		name = re.match(r'(.*).py', file).group(1)
		if name is not None:
			names.append(name)
			fpaths.append(path+file)
	# print names, fpaths
	return names, fpaths

# count the code
def count_lines(filepath):
	with open(filepath, 'r') as f:
		lines = f.readlines()
		# print len(lines)
		nblank, ncomment, ncode = 0, 0, 0
		for line in lines:
			if line.strip() == '':
				nblank += 1
			elif line[0] == '#':
				ncomment += 1
			else:
				ncode += 1
		print 'blank number: %d, comment number: %d, code number: %d' % (nblank, ncomment, ncode)
		return nblank, ncomment, ncode

if __name__ == '__main__':
	path = './/file//'
	names, fpaths = loadfile(path)
	for i in range(len(names)):
		print names[i], ':'
		count_lines(fpaths[i])
		print '='*80
