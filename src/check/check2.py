# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
dr = webdriver.Chrome(chromedriver)

file_path =  'file:///' + os.path.abspath('checkbox.html')
dr.get(file_path)
time.sleep(2)

# 选择所有的checkbox并全部勾上
checkboxes = dr.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
    checkbox.click()
time.sleep(2)

# 打印当前页面上有多少个checkbox
print (len(dr.find_elements_by_css_selector('input[type=checkbox]')))
time.sleep(2)

dr.quit()