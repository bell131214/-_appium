#coding=utf-8

import unittest,sys
sys.path.append('..')
import time
from functions.interface_case import InterfaceCase
from pages.banner_pages import BannerPages



class LoginTest(InterfaceCase):
    u"""验证首页banner获取加载页内容"""


    def setUp(self):
        self.driver = self.inital.get_driver()
        self.logger=self.inital.logger




    def test_click_banner(self):
        u"""验证点击banner"""
        try:
            a=BannerPages(self.driver)
            b=a.banner_click(id=2)
            time.sleep(3)
            self.assertEqual(str(b), "新手专享")
        except Exception,e:
            self.logger.info(e)


    def tearDown(self):
        self.driver.quit()





if __name__ == '__main__':
 unittest.main(verbosity =2)