#coding=utf-8
from selenium import webdriver
import os,time
source = open("D:\\data.txt", "r")
values = source.readlines()
source.close()
# 执行循环
for search in values:
    chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    browser = webdriver.Chrome(chromedriver)
    browser.get("https://www.baidu.com")
    browser.find_element_by_id("kw").send_keys(search)
    browser.find_element_by_id("su").click()
    time.sleep(3)
    browser.quit()