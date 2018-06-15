# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os,time

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get("https://www.baidu.com")


#进入搜索设置页
driver.find_element_by_link_text("设置").click()

driver.find_element_by_link_text("搜索设置").click()


#设置每页搜索结果为50条
WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath("//*[@id='general']/form/div").is_displayed())

m=driver.find_element_by_xpath("//*[@id='general']/form/div").find_element_by_name("NR")

m.find_element_by_xpath("//option[@value='50']").click()

time.sleep(5)


#保存设置的信息

WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath("//*[@id='general']/form/div").is_displayed())

driver.find_element_by_xpath("//*[@id='general']/form/div").find_element_by_xpath("//*[@id='gxszButton']/a[1]").click()

time.sleep(5)

driver.switch_to_alert().accept()



#跳转到百度首页后，进行搜索表（一页应该显示50条结果）

driver.find_element_by_id("kw").send_keys("selenium")

driver.find_element_by_id("su").click()

time.sleep(5)

driver.quit()