# -*- coding:utf-8 -*-
# 用 Python 写一个爬图片的程序，爬链接里的日本动漫图片
# https://tieba.baidu.com/p/5668819609


import re
from bs4 import BeautifulSoup
import urllib2
import requests


url = 'https://tieba.baidu.com/p/3658246084?red_tag=0607879314#!/l/p1'

## method 1
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
# headers = {'User_agent':user_agent}
# html = requests.get(url, headers=headers)
# print html.text

## method2
# html = urllib2.urlopen(url)
# print html.read()

html = requests.get(url)
# print html.text
imgre = re.compile(r'src=\"(.*?\.jpg)\"')
results = imgre.findall(html.text)

count = 0
for result in results:
	print 'Saving for pic No.%d ...' % (count+1)
	try:
		img = urllib2.urlopen(result, timeout=5).read()
		f = open('./pic/'+str(count)+'.jpg', 'wb')
		f.write(img)
		f.close
		count += 1
	except:
		print 'There is some problem to save the image No.%s.' %(str(count))
