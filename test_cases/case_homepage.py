#coding=utf-8

import unittest,sys
sys.path.append('..')
import time
from functions.interface_case import InterfaceCase
from pages.banner_pages import BannerPages
from functions.appium_init import *
from pages.startup_page import StartupPage



class LoginTest(InterfaceCase):
    u"""验证首页banner获取加载页内容"""


    def setUp(self):
        self.driver = self.inital.get_driver()
        self.logger=self.inital.logger




    def test_click_banner(self):
        u"""验证点击banner"""
        try:
            startUp=StartupPage(self.driver)
            bannerpages=startUp.page_swipe()
            b=bannerpages.banner_click(id=6)
            time.sleep(3)
            self.assertEqual(str(b), u"新手专享")
        except Exception,e:
            self.logger.info(e)


    def tearDown(self):
        self.driver.quit()





if __name__ == '__main__':
    Init()
    unittest.main()