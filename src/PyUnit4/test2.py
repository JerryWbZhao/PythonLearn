#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, os
import HTMLTestRunner
class Youdao(unittest.TestCase):
    def setUp(self):
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.youdao.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    #百度搜索用例
    def test_youdao_search(self):
        u"""有道搜索用例"""
        driver = self.driver
        driver.get(self.base_url + "/")
        try:
            driver.find_element_by_id("query").send_keys(u"虫师")
            driver.find_element_by_id("qb").click()
            time.sleep(2)
        except:
            driver.get_screenshot_as_file("D:\\selenium_use_case\\error_png\\kw.png")
    #如果没有找到上面的元素就截取当前页面。
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Youdao("test_youdao_search"))
#这里可以添加更多的用例,如：
#suite.addTest(Youdao("aaaa"))
    unittest.TextTestRunner().run(suite)