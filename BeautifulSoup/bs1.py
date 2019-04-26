import requests
from bs4 import BeautifulSoup

html = requests.get('https://book.douban.com/latest?icn=index-latestbook-all').text
# print(html)
soup = BeautifulSoup(html, 'lxml')
# print(soup.li.children)
test1 = soup.find_all('a')
# print(test1)
for i in test1:
    print(i.string)