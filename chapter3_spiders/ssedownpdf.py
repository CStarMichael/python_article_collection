import requests
from selenium import webdriver
import time, re
import pandas as pd

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = 'http://www.sse.com.cn/disclosure/credibility/supervision/inquiries/'
browser.maximize_window()
browser.get(url)
time.sleep(3)
# data = browser.page_source
# print(data)

# p_title = '<td><a class="table_titlewrap" href=".*?" target="_blank">(.*?)</a></td>'
# p_href = '<td><a class="table_titlewrap" href="(.*?)" target="_blank">.*?</a></td>'
# title = re.findall(p_title, data)
# href = re.findall(p_href, data)
# print(title)
# print(href)
#
# for i in range(len(href)):
#     res = requests.get(href[i])
#     path = '上交所问询函\\' + title[i] + '.pdf'
#     file = open(path, 'wb')
#     file.write(res.content)
#     file.close()

#/html/body/div[8]/div/div[2]/div/div[1]/div[2]/ul/li[9]/a
#/html/body/div[8]/div/div[2]/div/div[1]/div[2]/ul/li[1]/a

data_all = ''
table_all = pd.DataFrame()

for i in range(3):  # 这里演示爬取10页3
    browser.find_element(By.XPATH, '/html/body/div[8]/div/div[2]/div/div[1]/div[2]/span[1]/input').send_keys(i + 1)
    browser.find_element(By.XPATH, '/html/body/div[8]/div/div[2]/div/div[1]/div[2]/span[2]/a').click()
    time.sleep(3)  # 这里必须加3秒的延迟，因为需要等待网页加载完毕
    data = browser.page_source

    p_title = '<td><a class="table_titlewrap" href=".*?" target="_blank">(.*?)</a></td>'
    p_href = '<td><a class="table_titlewrap" href="(.*?)" target="_blank">.*?</a></td>'
    title = re.findall(p_title, data)
    href = re.findall(p_href, data)

    table = pd.read_html(data)[0]
    table['网址'] = href
    table_all = table_all.append(table)

    for i in range(len(href)):
        res = requests.get(href[i])
        path = '上交所问询函\\' + title[i] + '.pdf'
        try:
            file = open(path, 'wb')
            file.write(res.content)
        except:
            print(title[i] + '下载失败')
        finally:
            file.close()
    # data_all = data_all + data  # 也可以简写为data_all += data

# print(data_all)
table_all.to_excel('上交所问询函.xlsx', index=False)
