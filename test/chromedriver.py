import time

from selenium import webdriver

wd = webdriver.Chrome('C:\\Users\\dorothy\\PycharmProjects\\chromedriver_win32\\chromedriver')
wd.get('http://www.google.com')

time.sleep(3)
html = wd.page_source
print(html)

wd.close()