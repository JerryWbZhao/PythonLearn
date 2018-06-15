#coding=utf-8

from selenium import webdriver
import time
import os

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)


url= 'https://www.baidu.com'

#通过get方法获取当前URL打印
print ("now access %s" %(url))
browser.get(url)

time.sleep(2)
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)
browser.quit()