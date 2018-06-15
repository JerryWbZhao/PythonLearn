#!user/bin/env python3  
# coding = utf-8 

import os
import time
from selenium import webdriver

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

browser.get("https://www.baidu.com")
print (browser.title)
time.sleep(1)

#id = cp 元素的文本信息
data=browser.find_element_by_id("cp").text.replace(u'\xa9', u'©')

#打印信息
print (data)

#browser.quit()