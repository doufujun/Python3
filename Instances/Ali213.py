import requests

def getOnePage(url) :
    response = requests.get(url)


def main () :
    url = 'http://www.ali213.net/zt/ztisitemap_hot.html'
    print(getOnePage(url))

if __name__ == '__main__' :
    main()