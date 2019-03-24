from bs4 import BeautifulSoup

html_sample = '\
    <html>\
        <body>\
            <h1 id = "title">Hello World</h1>\
                <a href = "#" class = "link">This is link1</a>\
                <a href = "# link2" class = "link">This is link2</a>\
        </body>\
    </html>'

soup = BeautifulSoup(html_sample, 'html.parser')
print(type(soup))
print(soup.text)

#使用select找出含有h1标签的元素
header = soup.select('h1')
print(header)
print(header[0])

#使用select找出所有id为title的元素(id前面需要加#)
alink = soup.select('#title')
print(alink)

#使用select找出所有class为link的元素(class前面需加.)
for link in soup.select('.link'):
    print(link)

#使用select找出所有a tag的href连结
alinks = soup.select('a')
for link in alinks:
    print(link['href'])

a = '<a href = "#" qoo = 123 abc = 456> i am a link</a>'
soup2 = BeautifulSoup(a)
print(soup2.select('a'))

