import requests
from bs4 import BeautifulSoup
import getHeaders

def get_source():
    headers = getHeaders.get_chrome()
    url = 'http://search.zqrb.cn/search.php?src=all&q=%E8%B4%B5%E5%B7%9E%E8%8C%85%E5%8F%B0+&f=_all&s=newsdate_DESC'
    response = requests.get(url, headers=headers, timeout=10).text
    return response

def parse_source(response):
    soup = BeautifulSoup(response, 'html.parser')
    a = soup.select('dt a')
    for i in range(len(a)):
        title = a[i].text
        href = a[i]['href']
        print(title)
        print(href)

def data_clean():
    pass

def main():
    response = get_source()
    parse_source(response)

if __name__ == '__main__':
    main()