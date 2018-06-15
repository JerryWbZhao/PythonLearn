#!/usr/bin/python
#coding=utf-8

from selenium import webdriver
import time
import os
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

browser.get("https://www.baidu.com")

#xpath:attributer （属性）
browser.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")
#input标签下id =kw的元素 
browser.find_element_by_id("su").click()
time.sleep(5)

#xpath:idRelative （id相关性）
#browser.find_element_by_xpath("//div[@class='bg s_ipt_wr quickdelete-wrap']").send_keys("selenium")
#在/form/span/div 层级标签下有个div标签的id=kw_tip的元素
#browser.find_element_by_id("su").click()
#time.sleep(5)

#browser.find_element_by_xpath("//tr[@id='check']/td[2]").click() 
# id为'check' 的tr ，定闪他里面的第2个td
#time.sleep(5)

#xpath:position （位置）
#browser.find_element_by_xpath("//input").send_keys("selenium") 
#browser.find_element_by_xpath("//tr[7]/td[2]").click()
#第7个tr 里面的第2个td
#time.sleep(5) 

#xpath: href （水平参考）
browser.find_element_by_xpath("//*[@id='s_tab']/a[1]").click()
#在a标签下有个文本（text）包含（contains）'新闻' 的元素
time.sleep(5)

#xpath:link
#browser.find_element_by_xpath("//a[@href='//www.baidu.com/more']").click()
#time.sleep(5)

#有个叫a的标签，他有个链接href='http://www.baidu.com/ 的元素