# -*- coding:utf-8 -*-

#一个HTML文件，找出里面的正文。

import requests
from bs4 import BeautifulSoup

# url = 'http://www.dota2.com.cn/index.htm'
# html = requests.get(url)
# soup = BeautifulSoup(html.text, "html.parser")
soup = BeautifulSoup(open('DOTA2.html'))

print soup.body.text
# print(soup.body.text.encode('GBK','ignore').decode('GBK'))

for link in soup.find_all('a'):
	print link.get('href')
# print soup.find()