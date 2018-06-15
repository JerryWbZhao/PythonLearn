#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os,time

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get("http://www.baidu.com")

#输入框输入内容
driver.find_element_by_id("kw").send_keys("selenium")
time.sleep(3)

#ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(3)

#ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(3)

#输入框重新输入内容，搜索
driver.find_element_by_id("kw").send_keys(u"虫师 cnblogs")
driver.find_element_by_id("su").click()
time.sleep(3)

driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
driver.find_element_by_id("su").send_keys(Keys.ENTER)
time.sleep(3)

time.sleep(3)
driver.quit()