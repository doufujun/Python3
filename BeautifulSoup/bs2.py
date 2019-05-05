# attrs 通过属性查找

import requests
from bs4 import BeautifulSoup

html = requests.get('https://book.douban.com/latest?icn=index-latestbook-all').text
# print(html)
soup = BeautifulSoup(html, 'lxml')
# print(soup.li.children)
# test1 = soup.find_all(class_='detail-frame')
test1 = soup.select('ul li div h2 a')
print(len(test1))
for i in test1:
    print(i.string)

# print(len(test1))