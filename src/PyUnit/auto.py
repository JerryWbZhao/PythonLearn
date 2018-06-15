#coding= utf-8
import unittest
from widget import Widget

# 执行测试的类
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()
        
    # 测试getSize()方法的测试用例    
    def testSize(self):
        self.assertEqual(self.widget.getSize(), (40, 40))
        
    # 测试resize()方法的测试用例
    def testResize(self):
        self.widget.resize(100, 100)
        self.assertEqual(self.widget.getSize(), (100, 100))    
        
    def tearDown(self):
        self.widget.dispose()
        self.widget = None

# 测试
if __name__ == "__main__":

# 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase("testSize"))
    suite.addTest(WidgetTestCase("testResize"))
# 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)    
    
    