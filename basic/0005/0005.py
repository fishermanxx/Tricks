# -*- coding:utf-8 -*-
#你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

import os
import re
from PIL import Image

#Read the image file
def load_pic(file_path):
	files = os.listdir(file_path)
	new_files, names = [], []
	for file in files:
		matchObj = re.match(r'(.*).png', file)
		if matchObj is not None:
			names.append(matchObj.group(1))
			new_files.append(path+file)
	# print names, new_files
	return names, new_files


#Change the resolution
def change_resolution(img_name, img_path, resolution):
	img = Image.open(img_path)
	print img_name, img.size
	x, y = img.size
	img.resize((resolution[0], resolution[1])).save('.//new_img//new_'+img_name+'.png')

if __name__ == '__main__':
	path = './/img//'
	names, paths = load_pic(path)
	# print names, paths
	resolution = [500, 500]
	for i in range(len(names)):
		change_resolution(names[i], paths[i], resolution)