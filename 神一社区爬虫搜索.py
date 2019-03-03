#http://www.sy52.net/forum.php?mod=viewthread&action=printable&tid=6601开始
#http://www.sy52.net/forum.php?mod=viewthread&action=printable&tid=9330结束
 
import requests 
import urllib.request
import string
import sys
import bs4
import os
from multiprocessing import Pool
import re

def func():
	url = []
	xx = u"([\u4e00-\u9fff]+)"
	hanzi = re.compile(xx)
	keyword = re.compile(r'')
	pattern = re.compile(r'>(.*)-')
	for i in range(6601, 6620):
		try:
			with urllib.request.urlopen("http://www.sy52.net/forum.php?mod=viewthread&action=printable&tid=" + str(i)) as response:
				html = response.read()
				soup1 = bs4.BeautifulSoup(html, "html.parser").title
				modified = soup1.decode('utf-8')
				if  soup1.find("绞刑") != -1:
					url.append([hanzi.findall(soup1), "http://www.sy52.net/forum.php?mod=viewthread&action=printable&tid=" + str(i)])
				else:
					pass

			for link in url:
				print(link[0])
				print(link[1])
				print("\n")

		except Exception:
			print("Not Found!")
			
if __name__ == "__main__":
    #p = Pool()
    #res = [p.apply_async(func, args=(i,)) for i in range(10)]
	func()
