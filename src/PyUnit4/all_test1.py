#coding=utf-8
"Combine tests for gnosis.xml.objectify package (req 2.3+)"
import unittest, doctest
from PyUnit4 import test1, test2 #这里需要导入测试文件

suite = doctest.DocTestSuite()
#罗列要执行的文件
suite.addTest(unittest.makeSuite(test1.Baidu))
suite.addTest(unittest.makeSuite(test2.Youdao))
unittest.TextTestRunner(verbosity=2).run(suite)