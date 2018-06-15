# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
dr = webdriver.Chrome(chromedriver)

file_path =  'file:///' + os.path.abspath('checkbox.html')
dr.get(file_path)

# 选择所有的checkbox并全部勾上
checkboxes = dr.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
    checkbox.click()
time.sleep(2)

# 把页面上最后1个checkbox的勾给去掉
dr.find_elements_by_css_selector('input[type=checkbox]').pop().click()
time.sleep(2)

# 打印当前页面上有多少个radio
print (len(dr.find_elements_by_css_selector('input[type=radio]')))
time.sleep(2)

dr.quit()