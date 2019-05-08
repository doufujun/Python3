import requests
from multiprocessing import Pool
from requests.exceptions import RequestException
import re
import json

def getOnePage(url) :
    try :
        response = requests.get(url)
        if response.status_code == 200 :
            return response.text
        return None
    except RequestException :
        return None

def parseOnePage(html) :
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a></p>.*?star.*?>(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items :
        yield {
            '排名':item[0],
            '封面':item[1],
            '片名':item[2],
            '主演':item[3].strip()[3:],
            '上映时间':item[4].strip()[5:],
            '评分':item[5] + item[6]
        }

def writeToFile(content) :
    with open ('result.txt', 'a', encoding='utf-8') as f :
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = getOnePage(url)
    parseOnePage(html)
    for item in parseOnePage(html):
        print(item)
        writeToFile(item)

if __name__ == '__main__' :
    pool = Pool()
    pool.map(main, [i*10 for i in range(10)])