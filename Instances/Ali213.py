import requests

def getOnePage(url) :
    response = requests.get(url)
    return response

def main () :
    url = 'http://www.ali213.net/zt/ztisitemap_hot.html'
    html = getOnePage(url).content.decode('utf-8')
    print(html)
    
if __name__ == '__main__' :
    main()