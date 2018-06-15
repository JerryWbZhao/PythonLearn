#coding=utf-8

from selenium import webdriver
import time
import os

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

browser.get("https://www.baidu.com")
time.sleep(2)

print ("浏览器最大化")
browser.maximize_window()  #将浏览器最大化显示
time.sleep(2)

browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)
browser.quit()