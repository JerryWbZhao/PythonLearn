#coding=utf-8

from selenium import webdriver
import time,os

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver

#第一次不勾选
driver = webdriver.Chrome(chromedriver)

driver.get("http://passport.cnblogs.com/login.aspx?ReturnUrl=http://www.cnblogs.com/fnng/admin/EditPosts.aspx")

time.sleep(3)
driver.maximize_window() # 浏览器全屏显示

#通过用户名密码登陆
driver.find_element_by_id("input1").send_keys("fnngj")
driver.find_element_by_id("input2").send_keys("123456")

#勾选保存密码
#driver.find_element_by_id("remember_me").click()
time.sleep(3)
#点击登陆按钮
driver.find_element_by_id("signin").click()

#获取cookie信息并打印
cookie= driver.get_cookies()
print (cookie)
print('\n')

#第二次勾选
driver1 = webdriver.Chrome(chromedriver)

driver1.get("http://passport.cnblogs.com/login.aspx?ReturnUrl=http://www.cnblogs.com/fnng/admin/EditPosts.aspx")

time.sleep(3)
driver1.maximize_window() # 浏览器全屏显示

#通过用户名密码登陆
driver1.find_element_by_id("input1").send_keys("fnngj")
driver1.find_element_by_id("input2").send_keys("123456")

#勾选保存密码
driver1.find_element_by_id("remember_me").click()
time.sleep(3)
#点击登陆按钮
driver1.find_element_by_id("signin").click()

#获取cookie信息并打印
cookie= driver1.get_cookies()
print (cookie)
print('\n')



time.sleep(2)
driver.close()
driver1.close()