from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# browser = webdriver.Chrome(options=chrome_options)

browser = webdriver.Chrome()
# browser.maximize_window()
browser.get('https://www.baidu.com/')

# //*[@id="kw"]  //*[@id="su"]

# browser.find_element_by_xpath('//*[@id="kw"]').send_keys('python')
# browser.find_element_by_xpath('//*[@id="su"]').click()

# browser.find_element(By.XPATH, '//*[@id="kw"]').send_keys('python')
# browser.find_element(By.XPATH, '//*[@id="su"]').click()

# #kw
browser.find_element(By.CSS_SELECTOR, '#kw').clear()
browser.find_element(By.CSS_SELECTOR, '#kw').send_keys('电影')
browser.find_element(By.CSS_SELECTOR, '#su').click()

data = browser.page_source
print(data)