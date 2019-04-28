# attrs 通过标签查找属性

import requests
from bs4 import BeautifulSoup

html = requests.get('https://book.douban.com/latest?icn=index-latestbook-all').text
soup = BeautifulSoup(html, 'lxml')
test1 = soup.select('div')
print(test1)
# for i in test1:
#     print(i['class'])