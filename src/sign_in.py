#coding=utf-8
import os
import time
from selenium import webdriver

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get("https://s.qa.bingotalk.cn/#/login")

#给用户名的输入框标红
#js="var q=document.getElementsByName(\"username\");q.style.padding=\"1px solid red\";"
#调用js
#driver.execute_script(js)
time.sleep(3)

driver.find_element_by_name("username").send_keys("username")
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/form/button").click()
time.sleep(3)

driver.quit()