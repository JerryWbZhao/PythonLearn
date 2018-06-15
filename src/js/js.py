#coding=utf-8
from selenium import webdriver 
import time,os

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)

file_path =  'file:///' + os.path.abspath('js.html')
driver.get(file_path)
time.sleep(5)

#######通过JS 隐藏选中的元素#########
#第一种方法：
driver.execute_script('$("#tooltip").fadeOut();')
time.sleep(5)


#第二种方法：
button = driver.find_element_by_class_name('btn')
driver.execute_script('$(arguments[0]).fadeOut()',button)
time.sleep(5)

#driver.quit()