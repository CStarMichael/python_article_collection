import requests
import re
import getHeaders

def get_source():
    headers = getHeaders.get_chrome()
    url = 'http://search.zqrb.cn/search.php?src=all&q=%E8%B4%B5%E5%B7%9E%E8%8C%85%E5%8F%B0+&f=_all&s=newsdate_DESC'
    response = requests.get(url, headers=headers, timeout=10).text
    return response

def parse_source(response):
    p_title = '<a href=".*?target="_blank"><h4>(.*?)</h4></a>'
    p_href = '<a href="(.*?)" target="_blank">.*?</h4></a>'
    p_date = '<span><strong>时间:</strong>(.*?)</span>'
    title = re.findall(p_title, response)
    href = re.findall(p_href, response)
    date = re.findall(p_date, response)
    return title, href, date

def data_clean(title, href, date):
    source = []
    number = min(len(title), len(href), len(date))
    for i in range(number):
        source.append('证券日报')
        title[i] = re.sub('<(.*?)>', '', title[i])
        date[i] = date[i].split(' ')[0]
        print(title[i] + '(' + source[i] + ' ' + date[i] + ')')
        print(href[i])

def main():
    response = get_source()
    title, href, date = parse_source(response)
    data_clean(title, href, date)

if __name__ == '__main__':
    main()
