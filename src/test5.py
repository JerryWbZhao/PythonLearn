#!/usr/bin/python
#coding=utf-8

from selenium import webdriver
import time
import os
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

browser.get("https://www.baidu.com")
time.sleep(5)

#########百度输入框的定位方式##########

#通过id方式定位
browser.find_element_by_id("kw").send_keys("selenium")
time.sleep(5)

#通过name方式定位
browser.find_element_by_name("wd").send_keys("selenium")
time.sleep(5)

#通过tag name方式定位
#browser.find_element_by_tag_name("input").send_keys("selenium")
time.sleep(5)

#通过class name 方式定位
browser.find_element_by_class_name("s_ipt").send_keys("selenium")
time.sleep(5)

#通过CSS方式定位
browser.find_element_by_css_selector("#kw").send_keys("selenium")
time.sleep(5)

#通过xphan方式定位
browser.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")
time.sleep(5)

browser.find_element_by_id("su").click()
time.sleep(5)


############################################


browser.quit()