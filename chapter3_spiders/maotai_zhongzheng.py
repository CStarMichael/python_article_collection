import requests
import re
import getHeaders

def get_source():
    headers = getHeaders.get_chrome()
    url = 'https://search.cs.com.cn/search?searchword=%E8%B4%B5%E5%B7%9E%E8%8C%85%E5%8F%B0&channelid=215308'
    response = requests.get(url, headers=headers, timeout=10).text
    # print(response)
    return response

def parse_source(response):
    p_title = '<a style="font-size: 16px;color: #0066ff;line-height: 20px" href=".*? target="_blank">(.*?)</a>'
    p_href = '<a style="font-size: 16px;color: #0066ff;line-height: 20px" href="(.*?)" target="_blank">'
    p_date = '&nbsp;&nbsp;.*?&nbsp;(.*?)</td>'
    title = re.findall(p_title, response)
    href = re.findall(p_href, response)
    date = re.findall(p_date, response, re.S)
    # print(title)
    # print(href)
    # print(date)
    return title, href, date


def data_clean(title, href, date):
    source = []
    number = min(len(title), len(href), len(date))
    for i in range(number):
        source.append('中证网')
        title[i] = re.sub('<(.*?)>', '', title[i])
        date[i] = date[i].strip()
        date[i] = re.sub('[.]', '-', date[i])
        print(title[i] + '(' + source[i] + ' ' + date[i] + ')')
        print(href[i] + '\n')

def main():
    response = get_source()
    # parseSource(response)
    title, href, date = parse_source(response)
    data_clean(title, href, date)

if __name__ == '__main__':
    main()
