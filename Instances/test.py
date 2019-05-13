import requests
import re


url = 'http://www.ali213.net/zt/ztisitemap_hot.html'

def getOnePage(url) :
    rp = requests.get(url)

print(getOnePage(url))
