#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
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
    #百度搜索用例
    def test_baidu_search(self):
        u"""百度搜索用例"""
        driver = self.driver
        driver.get(self.base_url + "/")
        try:
        #是一个无法找到的元素id
            driver.find_element_by_id("kw").send_keys("selenium webdriver")
        except:
            driver.get_screenshot_as_file("D:\\selenium_use_case\\error_png\\kw.png")
        #如果没有找到上面的元素就截取当前页面。
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Baidu("test_baidu_search"))
#同样的，可以在这个文件中添加更多的用例。
#suite.addTest(Youdao("aaaa"))
    results = unittest.TextTestRunner().run(suite)