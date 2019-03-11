import requests 
import time
from lxml import etree 
import os
#concurrent直接封装了Multiprocessing和Threading模块
from concurrent import futures

headers = {
    'Referer': 'http://www.doutula.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0'}

def download_img(src, dirname):
    filename = src.split('/')[-1]
    #img是图片 不能用字符串解析
    #img是图片的响应，img.content是图片的字节
    img = requests.get(src, headers = headers)
    with open(f'Picture/{dirname}/{filename}', 'wb') as file:
        file.write(img.content)

#解析网页上的标签 获取下一页
def get_page(url):
    resp = requests.get(url, headers = headers)
    dirname = "page" + url.split('=')[-1]
    os.mkdir('Picture/' + dirname + '/')
    print(resp, url)
    html = etree.HTML(resp.text)
    srcs = html.xpath('.//img/@data-original')
    #多线程
    ex = futures.ThreadPoolExecutor(max_workers = 40)
    for src in srcs:
        ex.submit(download_img, src, dirname)
    next_link = html.xpath('.//a[@rel = "next"]/@href')
    return next_link

def main():
    next_link_base = 'http://www.doutula.com/article/list/?page='
    current_num = 0
    next_link = 'http://www.doutula.com/'
    while next_link:
        time.sleep(0.2)
        current_num = current_num + 1
        next_link = get_page(next_link_base + str(current_num))
        if current_num >= 4:
            break

if __name__ == "__main__":
    main()