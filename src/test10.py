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

browser.find_element_by_id("kw").send_keys("selenium")
time.sleep(1) 

browser.find_element_by_id("su").submit()
time.sleep(1)


#browser.quit()