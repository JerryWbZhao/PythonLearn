#coding=utf-8
from selenium import webdriver
import os,time
from PyUnit3 import fun #导入函数
#循环调用字典里的用户名密码，分别赋值给k,v
for k,v in fun.zidian().items():
    chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get("https://t.qa.bingotalk.cn/#/login")
    driver.find_element_by_xpath("//*[@id='app']/div/div[1]/form/div/div[1]/div/div/div/input").clear()
    driver.find_element_by_xpath("//*[@id='app']/div/div[1]/form/div/div[1]/div/div/div/input").send_keys(k)
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='app']/div/div[1]/form/div/div[2]/div/div/div/input").clear()
    driver.find_element_by_xpath("//*[@id='app']/div/div[1]/form/div/div[2]/div/div/div/input").send_keys(v)
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='app']/div/div[1]/form/div/button").click()
    time.sleep(1)
    driver.close()