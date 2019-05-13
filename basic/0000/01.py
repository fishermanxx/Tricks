# -*- coding:utf-8 -*-
# 在图片右上角添加红色数字，类似于未读提示.

import PIL
from PIL import Image, ImageDraw, ImageFont

def add_num(filename, text='4', fillcolor=(255, 0, 0)):
	img = Image.open(filename)
	width, height = img.size
	myfont = ImageFont.truetype('arial.ttf', 50)
	draw = ImageDraw.Draw(img)
	draw.text((width - width//8, 0), text , font = myfont,fill = fillcolor)
	img.save('target.jpg')


if __name__ == '__main__':
	filename = 'image.jpg'
	text = '6'
	fillcolor = (255, 0, 0)
	add_num(filename, text, fillcolor)