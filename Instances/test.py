import requests
import re

url = 'http://www.ali213.net/zt/ztisitemap_hot.html'
response = requests.get(url)
html = response.content.decode('utf-8')
# print(html)
pattern = re.compile('<li\s.*?list-con-main-item.*?<a.*?<span>(.*?)</span></a>.*?item-title">(.*?)</a>.*?</li>', re.S)
items = re.findall(pattern, html)
print('-----------------------------')
# print(items)
def test() :
    for item in items :
        yield {
            'GameName': item[1],
            
            'Ratings' : item[0]
        }

for item in test():
    print(item)