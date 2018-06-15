#coding=utf-8

from selenium import webdriver
import time
import os
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

browser.get("https://www.baidu.com")
time.sleep(2)
    
browser.find_element_by_link_text("贴吧").click()
time.sleep(2)
browser.quit()