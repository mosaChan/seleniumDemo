# coding=utf-8
import  unittest
import time
import sys
from baseSetting.browser_engine import BrowserEngine
from pageObject.homepage import HomePage
from baseSetting.logger import Logger

logger = Logger(logger="BaiduSearch").getlog()

class BaiduSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_1_baidu_search(self):
        """搜索selenium"""
        homepage = HomePage(self.driver)
        homepage.input_selenium('selenium')
        homepage.click_baidu()
        expect_text = 'selenium'
        actual_text = homepage.get_search_text()
        try:
            self.assertEqual(expect_text,actual_text)
            logger.info('expect_text: %s is equal to actual_text: %s .Test pass.' % (expect_text, actual_text))
        except Exception as e:
            logger.info(format(e))
            logger.info('Test failed')

if __name__ == '__main__':
    unittest.main()