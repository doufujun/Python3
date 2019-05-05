# re.findall 找到所有匹配的内容
# 抓取豆瓣读书的新书速递书单列表
import requests
import re

content = requests.get('https://book.douban.com/latest?icn=index-latestbook-all').text
pattern = re.compile('detail-frame.*?<h2>.*?a\shref=".*?">(.*?)</a>', re.S)
results = re.findall(pattern, content)
# print(results)
for result in results:
    print(result)