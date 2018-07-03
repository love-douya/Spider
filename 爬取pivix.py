from urllib import request
from bs4 import BeautifulSoup
import chardet
import sys

#邮箱匹配正则表达式
#[A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)
response = request.urlopen("https://www.pixiv.net/member_illust.php?mode=manga&illust_id=65998072")
html = response.read()
# charset = chardet.detect(html)
# print(charset)
html = html.decode("utf-8")
#print(html)

with open("Pivix_Picture.txt", "w", encoding = "utf-8") as f:
    f.write(html)

