#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
dr = webdriver.Chrome(chromedriver)

file_path =  'file:///' + os.path.abspath('checkbox.html')
dr.get(file_path)

# 选择页面上所有的input，然后从中过滤出所有的checkbox并勾选之
inputs = dr.find_elements_by_tag_name('input')
for checkbox in inputs:
    if checkbox.get_attribute('type') == 'checkbox':
        checkbox.click()
time.sleep(2)

dr.quit()