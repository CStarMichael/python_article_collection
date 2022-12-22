import csv
import random
import re
import time
from urllib import request, parse

class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://www.maoyan.com/board?timeStamp=1667716020270&channelId=40011&index=10&signKey=b433550d96a864d9f382476f338acf71'

    def get_html(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'}
        print(headers)
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        print(html)
        self.paser_html(html)

    def paser_html(self, html):
        re_maoyan = r'<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>'
        pattern = re.compile(re_maoyan, re.S)
        r_list = pattern.findall(html)
        print(r_list)
        self.save_html(r_list)

    def save_html(self, r_list):
        with open('maoyan.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for r in r_list:
                name = r[0].strip()
                star = r[1].strip()[3:]
                time = r[2].strip()[5:15]
                line = [name, star, time]
                writer.writerow(line)
                print(name, star, time)


    def run(self):
        for offest in range(0, 11, 10):
            url = self.url.format(offest)
            print(url)
            self.get_html(url)
            time.sleep(random.uniform(1, 2))

def main():
    try:
        maoyanspider = MaoyanSpider()
        maoyanspider.run()
    except Exception as e:
        print("错误", e)

if __name__ == '__main__':
    main()