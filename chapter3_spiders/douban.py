import requests
import re
import getHeaders
from urllib.request import urlretrieve


def get_source(page):
    num = (page - 1) * 25
    headers = getHeaders.getChrome()
    url = 'https://movie.douban.com/top250?start=' + str(num)
    response = requests.get(url, headers=headers, timeout=10).text
    # print(response)
    return response


def parse_source(response):
    p_title = '<img width="100" alt="(.*?)" src=".*?"'
    p_img = '<img width="100" alt=".*?" src="(.*?)"'
    title = re.findall(p_title, response, re.S)
    img = re.findall(p_img, response)
    # print(title)
    # print(img)
    return title, img


def data_clean(num, title, img):
    number = min(len(title), len(img))
    for i in range(number):
        title[i] = re.sub('<(.*?)>', '', title[i])
        print(str(num * 25 + i + 1) + '.' + title[i])
        print(img[i] + '\n')

        # img_source = requests.get(img[i])
        # file = open('images/' + str(i + 1) + '.' + title[i] + '.jpg', 'wb')
        # file.write(img_source.content)
        # file.close()

        urlretrieve(img[i], 'images/' + str(num * 25 + i + 1) + '.' + title[i] + '.jpg')


def main():
    for i in range(10):
        response = get_source(i + 1)
        title, img = parse_source(response)
        data_clean(i, title, img)


if __name__ == '__main__':
    main()
