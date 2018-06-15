# -*- coding: utf-8 -*-

'''
Created on 2018年4月19日

@author: Magic
'''

import os
import time
from selenium import webdriver

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

file_path =  'file:///' + os.path.abspath('frame.html')
browser.get(file_path)

browser.implicitly_wait(30)
#先找到到ifrome1（id = f1）
browser.switch_to_frame("f1")
#再找到其下面的ifrome2(id =f2)
browser.switch_to_frame("f2")

#driver.switch_to_window("windowName")


#下面就可以正常的操作元素了
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)

#browser.quit()