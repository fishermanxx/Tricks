# -*- coding:utf-8 -*-
# 使用 Python 生成类似于下图中的字母验证码图片

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def rndChar():
	return chr(random.randint(65, 90))

def rndColor():
	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def compose(num):
	width, height = 60*num, 60
	image = Image.new('RGB', (width, height), (255,255,255))

	font = ImageFont.truetype('arial.ttf', 36)
	draw = ImageDraw.Draw(image)

	for x in range(width):
		for y in range(height):
			draw.point((x, y), fill=rndColor())

	letter = []
	for t in range(num):
		letter.append(rndChar())
		draw.text((60*t+10, 10), letter[t], font=font, fill=rndColor2())

	image.save('code.jpg', 'jpeg')
	image = image.filter(ImageFilter.BLUR)
	image.save('filter.jpg', 'jpeg')
	print letter

if __name__ == '__main__':
	num = 4
	compose(num)