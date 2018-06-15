#coding=utf-8

from selenium import webdriver
import time,os

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get("https://www.baidu.com")

# 获得cookie信息
cookie= driver.get_cookies()
time.sleep(2)
#将获得cookie的信息打印
print (cookie)

driver.quit()