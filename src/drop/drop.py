#-*-coding=utf-8

from selenium import webdriver

import os,time

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

file_path =  'file:///' + os.path.abspath('drop_down.html')

driver.get(file_path)

time.sleep(5)

m=driver.find_element_by_id("ShippingMethod")

m.find_element_by_xpath("//option[@value='10.69']").click()

time.sleep(5)

#driver.quit()