# attrs 通过标签查找属性

import requests
from bs4 import BeautifulSoup

html = requests.get('https://book.douban.com/latest?icn=index-latestbook-all').text
soup = BeautifulSoup(html, 'lxml')
test1 = soup.select('li')
for li in test1:
    print(li.get_text())
# for i in test1:
#     print(i['class'])