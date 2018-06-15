#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import unittest, time, re, os
import HTMLTestRunner
class Baidu(unittest.TestCase):
    def setUp(self):
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    #测试用例一
    def test_baidu_search(self):
        self.driver.get(self.base_url + "/")
        self.driver.maximize_window()  #将浏览器最大化显示
        time.sleep(2)
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        time.sleep(3)
        self.driver.quit()
    
    #测试用例二
    def test_baidu_set(self):    
        self.driver.get(self.base_url + "/")
        #进入搜索设置页
        self.driver.find_element_by_link_text("设置").click()
        self.driver.find_element_by_link_text("搜索设置").click()
        #设置每页搜索结果为50条
        WebDriverWait(self.driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath("//*[@id='general']/form/div").is_displayed())
        m=self.driver.find_element_by_xpath("//*[@id='general']/form/div").find_element_by_name("NR")
        m.find_element_by_xpath("//option[@value='50']").click()
        time.sleep(5)
        #保存设置的信息
        WebDriverWait(self.driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath("//*[@id='general']/form/div").is_displayed())
        self.driver.find_element_by_xpath("//*[@id='general']/form/div").find_element_by_xpath("//*[@id='gxszButton']/a[1]").click()
        time.sleep(5)
        self.driver.switch_to_alert().accept()
        #跳转到百度首页后，进行搜索表（一页应该显示50条结果）
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        time.sleep(5)
        self.driver.quit()    
    
    #....
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    testunit=unittest.TestSuite() #定义一个单元测试容器
    
    testunit.addTest(Baidu("test_baidu_search")) #将测试用例加入到测试容器中
    testunit.addTest(Baidu("test_baidu_set"))
    
    filename = 'D:\\result.html' #定义个报告存放路径，支持相对路径。
    fp = open(filename, 'wb')
    runner =HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='Report_title',
        description='Report_description')
    runner.run(testunit) #自动进行测试